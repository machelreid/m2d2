# M2D2: A Massively Multi-domain Language Modeling Dataset

Scripts and data links for [M2D2: A Massively Multi-domain Language Modeling Dataset](https://machelreid.github.io/resources/reid22_m2d2.pdf) (EMNLP 2022) by Machel Reid, Victor Zhong, Suchin Gururangan, and Luke Zettlemoyer.

![m2d2_image.png](m2d2_image.png)
## Data
Update: The data is currently hosted on HuggingFace [here](https://huggingface.co/datasets/machelreid/m2d2)!

To load the dataset use the following steps:
```bash
pip install --upgrade datasets
```
```python
import datasets

dataset = datasets.load_dataset("machelreid/m2d2", "cs.CL") # replace cs.CL with the domain of your choice

print(dataset['train'][0]['text']
```
~~*We're currently exploring ways to host this large amount of data online in an accessible manner, so please stay tuned! If you would like to access sooner, feel free to reach out at [machelreid@google.com](mailto:machelreid@google.com).*~~

### Evaluation Sets

Feel free to download the test sets for all domains at [this Google Drive link](https://drive.google.com/file/d/1U5wki_V-IFQy733HC6NO5ZuM2jaOaw8y/view?usp=sharing).

or via [`gdown`](https://pypi.org/project/gdown/):
```bash
#!/bin/bash
# install and/or upgrade gdown with pip
pip install --upgrade gdown
# Download M2D2 test sets
gdown "1U5wki_V-IFQy733HC6NO5ZuM2jaOaw8y"
tar -xvzf m2d2_test_sets.tar.gz
# File structure
# m2d2_test_sets/
# ├─ DOMAIN_AA/
# │  ├─ test.txt
# ├─ DOMAIN_AB/
# │  ├─ test.txt/
```


## Reproduction Scripts for Modeling

Find scripts for finetuning language models in `lm_scripts/adapt.sh`. Furthermore, we provide meta-scripts for generating scripts for multiple domains given an input file containing a list of directories containing domain specfici data (within `train.txt` and `valid.txt` should exist): `lm_scripts/generate_multiple.sh`. Respective instructions/parameters are included in each file.

For validation on multiple files, we also include `lm_scripts/validate_on_multiple_files.py` for calculating perplexity measures given a file containing a list of evaluation text files and a model checkpoint.

## Helper Scripts for Wikipedia Data Collection
For Wikipedia data collection, we include scripts for data dump processing (`data_scripts/wiki/get_data`), ontology gathering (`data_scripts/wiki/ontology`), and generating splits (`data_scripts/wiki/split_generation`).

## Helper Scripts for S2ORC Data Collection

*To be uploaded with documentation*

## Scripts to reproduce analyses in the paper

*To be uploaded with documentation*
