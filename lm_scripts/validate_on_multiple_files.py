from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from datasets import load_dataset
from tqdm import tqdm
import json
import torch
import argparse


def main(args):
    model = GPT2LMHeadModel.from_pretrained(args.model_id).to("cuda")
    tokenizer = GPT2TokenizerFast.from_pretrained(args.model_id)

    with open(args.list_of_valid_paths, "r") as f:
        list_of_datasets = [x.strip() for x in f.readlines()]

    try:
        with open(args.output_file, "r") as f:
            output_ppls = json.load(f)
    except:
        output_ppls = {}

    for ds in tqdm(list_of_datasets):
        if ds in output_ppls:
            continue
        dataset = load_dataset(
            "text",
            data_files=ds,
            # cache_dir=os.path.join(os.environ["HOME"], "storage4", ".cache"),
        )
        encodings = tokenizer("\n".join(dataset["train"]["text"]), return_tensors="pt")
        with torch.no_grad():
            ppl = eval_ppl(model, encodings, stride=1024)
        output_ppls[ds] = ppl.item()
        print(output_ppls)
        with open(args.output_file, "w") as f:
            json.dump(output_ppls, f)


def eval_ppl(model, encodings, stride, device="cuda"):
    max_length = model.config.n_positions
    nlls = []
    for i in tqdm(range(0, encodings.input_ids.size(1), stride)):
        begin_loc = max(i + stride - max_length, 0)
        end_loc = min(i + stride, encodings.input_ids.size(1))
        trg_len = end_loc - i  # may be different from stride on last loop
        input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
        target_ids = input_ids.clone()
        target_ids[:, :-trg_len] = -100

        with torch.no_grad():
            outputs = model(input_ids, labels=target_ids)
            neg_log_likelihood = outputs[0] * trg_len

        nlls.append(neg_log_likelihood)

    ppl = torch.exp(torch.stack(nlls).sum() / end_loc)
    return ppl


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_id", type=str)
    parser.add_argument("--list_of_valid_paths", type=str)
    parser.add_argument("--output_file", type=str)
    args = parser.parse_args()

    main(args)
