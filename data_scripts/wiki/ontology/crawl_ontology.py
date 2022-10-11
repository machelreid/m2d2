import requests
import tqdm
from multiprocessing import Pool
from bs4 import BeautifulSoup
import time
import argparse
import json

r = requests.get("https://en.wikipedia.org/wiki/Wikipedia:Contents/Categories")
soup = BeautifulSoup(r.text, "html.parser")
rank1 = soup.find_all("div", {"class": "contentsPage__section"})

MAX_DEPTH = 5


def recursive_get_dict(url, prepend_str=None, all_links=[], depth=0, max_depth=5):
    if "lists" in url or "List" in url:
        return {}
    if prepend_str is None:
        prepend_str = url + " -> "
    cur_dict = {}
    depth += 1
    url = f"https://en.wikipedia.org/{url}"
    r = ""
    while r == "":
        try:
            r = requests.get(url)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(20)
            print("Was a nice sleep, now let me continue...")
            continue
    soup = BeautifulSoup(r.text, "html.parser")
    try:
        cur_dict["pages"] = [
            s.a["href"] for s in soup.find("div", {"id": "mw-pages"}).find_all("li")
        ]
    except AttributeError:
        return {}
    try:
        category_pages = [
            i
            for i in soup.find("div", {"id": "mw-subcategories"}).find_all("a")
            if "Category:" in i["href"]
        ]
        category_pages = [i for i in category_pages if i not in all_links]
        all_links += category_pages
        cur_dict["subcategories"] = {}
        if depth == max_depth:
            return cur_dict
        for cp in category_pages:
            cur_dict["subcategories"][cp.text] = recursive_get_dict(
                cp["href"],
                prepend_str=prepend_str
                + url.replace("https://en.wikipedia.org/", "")
                + " -> ",
                all_links=all_links,
                depth=depth,
                max_depth=max_depth,
            )
    except AttributeError:
        pass
    print(prepend_str, url, "DONE", f" | Depth {depth}")
    return cur_dict


# for rank1s in tqdm.tqdm(rank1):
#     r1_dict = {}
#     rank2 = rank1s.find_all("div", {"class": "hlist"})
#     for rank2s in rank2:
#         r2_dict = {}
#         init = rank2s.find_all("li")
#         for itr, rank in enumerate(init[1:]):
#             r2_dict[rank.text] = recursive_get_dict(rank.a["href"])
#             print("Done", rank.text)
#         r1_dict[init[0].text] = r2_dict
#     # overall_dict[rank1s_text] = r1_dict
#     overall_dict.append(r1_dict)


# @ray.remote
def get_rank1s(rank1s, args):
    r1_dict = {}
    rank2 = rank1s.find_all("div", {"class": "hlist"})
    for rank2s in tqdm.tqdm(rank2):
        r2_dict = {}
        init = rank2s.find_all("li")
        for itr, rank in tqdm.tqdm(enumerate(init[1:]), total=len(init[1:])):
            r2_dict[rank.text] = recursive_get_dict(
                rank.a["href"], max_depth=args.max_depth
            )
            print("Done", rank.text)
        r1_dict[init[0].text] = r2_dict
    return r1_dict


def main(args):
    print(len(rank1))
    out = get_rank1s(rank1[args.idx], args)
    print(out.keys())

    with open(f"output{args.idx}.json", "w") as f:
        json.dump(out, f)
    with open(f"output_txt{args.idx}.json", "w") as f:
        f.write(json.dumps(out))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idx", type=int)
    parser.add_argument("--max-depth", type=int, default=5)
    args = parser.parse_args()
    main(args)
