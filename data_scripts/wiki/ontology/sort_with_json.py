import json
import sys
import subprocess
import os

json_path = sys.argv[1]
wiki_files_path = sys.argv[2]
out_path = sys.argv[3]


all_files = "/home/machel_reid/storage/all_wikipedia_files"


l_of_pages = []

with open("only_ones.txt", "r") as f:
    only_ones = set([i.strip() for i in f.readlines()])


def symlink(orig_path, sympath, filename):
    valid = ""
    if filename + ".txt" in only_ones:
        valid = "VALID__"
    orig_path = os.path.join(orig_path, filename[:2].upper(), filename + ".txt")
    assert os.path.isfile(orig_path), "File doesn't exist"
    sympath = os.path.join(sympath, valid + filename + ".txt")
    os.symlink(orig_path, sympath)


with open(json_path, "r") as f:
    json_file = json.load(f)


def recursive_thing(cur_dict, prev_path, name, l_of_pages):

    current_path = os.path.join(prev_path, name).replace(" ", "_").replace("\n", "_")
    os.makedirs(current_path, exist_ok=True)

    try:
        for page in cur_dict["pages"]:
            pg = page.split("/")[-1]
            try:
                symlink(all_files, current_path, pg)
            except Exception as e:
                l_of_pages.append(pg)
    except KeyError:
        pass
    try:
        for key in cur_dict["subcategories"]:
            recursive_thing(
                cur_dict["subcategories"][key], current_path, key, l_of_pages
            )
    except KeyError:
        try:
            for key in cur_dict:
                recursive_thing(cur_dict[key], current_path, key, l_of_pages)
        except:
            pass


for key in json_file:
    recursive_thing(json_file[key], out_path, key, l_of_pages)
with open(os.path.join(out_path, "not_included.txt"), "w") as f:
    f.write("\n".join(l_of_pages))
