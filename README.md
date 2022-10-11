# M2D2: A Massively Multi-domain Language Modeling Dataset

Scripts and data links for [M2D2: A Massively Multi-domain Language Modeling Dataset](https://machelreid.github.io/resources/reid22_m2d2.pdf) (EMNLP 2022) by Machel Reid, Victor Zhong, Suchin Gururangan, and Luke Zettlemoyer.

![m2d2_image.png](m2d2_image.png)
## Data
*We're currently exploring ways to host this large amount of data online in an accessible manner, so please stay tuned! If you would like to access sooner, feel free to reach out at [machelreid@google.com](mailto:machelreid@google.com).*

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

Find scripts for finetuning language models in `lm_scripts/adapt.sh`. Furthermore, we provide meta-scripts for generating scripts for each subdomain: `lm_scripts/generate_l1.sh`, `lm_scripts/generate_l2.sh`, `lm_scripts/generate_l1_to_l2.sh`. Respective instructions/parameters are included in each file.

## Helper Scripts for Wikipedia Data Collection
For Wikipedia data collection, we include scripts for data dump processing (`data_scripts/wiki/get_data`), ontology gathering (`data_scripts/wiki/ontology`), and generating splits (`data_scripts/wiki/split_generation`).

## Helper Scripts for S2ORC Data Collection

*To be uploaded with documentation*
