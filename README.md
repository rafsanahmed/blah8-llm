# BLAH8: Using LLMs to generate drug target associations

## Introduction
Drug development is arguably one of the most critical challenges in medicine. There are many resources that contain rich drug and druggable target information, such as Therapeutic Target Database (TTD). With the current advancements in Large Language Models (LLMs), drug-target data can be used to fine tune models and explore the findings.

## Proposal
In this short hackathon, we aim for the following tasks:

*Task 1: Develop prompt datasets from TTD resources to locally fine-tune LLMs.
*Task 2: Fine-tune LLMs such as LLAMA on the prompts dataset.
*Task 3: Evaluate the findings on different LLMs
*Task 4 (if time permits): Create a prompt based chat interface for the best model 

## Breakdown of tasks

### Task 1: Develop prompt datasets from TTD resources
The TTD dataset not only contains drug and druggable targets information, but also contains a barrage of information such as Uniprot IDs, biomarkers, pathway information etc. They can be used to develop a variety of rich prompts that can be used to fine-tune the LLMs chosen by the user. The datasets will be split into train, dev, test splits.

### Task 2: Fine Tune LLMs
The generated prompts datasets shall be used to fine tune locally tunable LLMs such as LLAMA and gptneo. Some models are fine tunable on local laptops but the other need the help of qlora. In this task, the participants explore options of fine tuning LLMs locally or using google colab.

### Task 3: Evaluate findings
The fine tuning of chosen LLMs will then be evaluated on test datasets and external datasets, such as Drugbank or a drug-target interaction network. Full text articles may also be provided to evaluate the inference on the text.

### Task 4: Chat interface
Due to the generative nature of LLMs, a chat interface can be a user friendly approach for using the models, if time permits.


## Motivation

Several

## Resources

TTD Datasets: https://db.idrblab.net/ttd/full-data-download

LLaMA access request: https://ai.meta.com/resources/models-and-libraries/llama-downloads/

Drugbank: https://go.drugbank.com/releases/latest



## References

```bibtex
@article{10.1093/nar/gkad751,
    author = {Zhou, Ying and Zhang, Yintao and Zhao, Donghai and Yu, Xinyuan and Shen, Xinyi and Zhou, Yuan and Wang, Shanshan and Qiu, Yunqing and Chen, Yuzong and Zhu, Feng},
    title = "{TTD: Therapeutic Target Database describing target druggability information}",
    journal = {Nucleic Acids Research},
    pages = {gkad751},
    year = {2023},
    month = {09},
    issn = {0305-1048},
    doi = {10.1093/nar/gkad751},
    url = {https://doi.org/10.1093/nar/gkad751},
}
```