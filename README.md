# M2D2

Scripts and data links for [M2D2: A Massively Multi-domain Language Modeling Dataset](https://machelreid.github.io/resources/reid22_m2d2.pdf) (EMNLP 2022) by Machel Reid, Victor Zhong, Suchin Gururangan, and Luke Zettlemoyer.

![m2d2_image.png](m2d2_image.png)
## Data
*We're currently exploring ways to host this large amount of data online in an accessible manner, stay tuned! If you would like to access sooner, feel free to reach out at [machelreid@google.com](mailto:machelreid@google.com).*


## Reproduction Scripts for Modeling

Find scripts for finetuning language models in `lm_scripts/adapt.sh`. Furthermore, we provide meta-scripts for generating scripts for each subdomain: `lm_scripts/generate_l1.sh`, `lm_scripts/generate_l2.sh`, `lm_scripts/generate_l1_to_l2.sh`. Respective instructions/parameters are included in each file.

## Helper Scripts for Wikipedia Data Collection
For Wikipedia data collection, we include scripts for data dump processing (`data_scripts/wiki/get_data`), ontology gathering (`data_scripts/wiki/ontology`), and generating splits (`data_scripts/wiki/split_generation`).

## Helper Scripts for S2ORC Data Collection

*To be uploaded with documentation*
