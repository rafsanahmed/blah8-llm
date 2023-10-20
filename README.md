# BLAH8: Using LLMs to generate drug target associations

## Introduction
Drug development is arguably one of the most critical challenges in medicine. There are several crucial steps that get us from idea to an usable drug. One of those steps are drug and druggable target identification. Many research approaches involve manually going through articles to find drug and druggable targets. Although painfully tedious, this approach brings results. However, this process can be exponentially fast-tracked with the help of Large Language Models (LLMs). 

There are many resources that contain manually annotated, drug and druggable target information, such as [Therapeutic Target Database](https://db.idrblab.net/ttd/full-data-download) (TTD). These rich collection of annotated data can be used to fine-tune existing LLMs and explore possibilities for discovering novel drug-target associations.

This project for the BLAH8 hackathon is aimed as a pilot study to develop drug-target specific prompt-based corpora and locally fine-tune existing LLMs on such corpora to evaluate the capabilities for drug-target identification. 

## Proposal Summary
In this BLAH8 hackathon, we aim for the following tasks:

* Task 1: Develop prompt datasets from TTD resources to locally fine-tune LLMs.
* Task 2: Fine-tune LLMs such as LLAMA on the prompts dataset.
* Task 3: Evaluate the findings on different LLMs
* Task 4 (if time permits): Create a prompt based chat interface for the best model 

## Breakdown of tasks

### Task 1: Develop prompt datasets from TTD resources
The TTD dataset not only contains drug and druggable targets information, but also contains a barrage of information such as Uniprot IDs, biomarkers, pathway information etc. They can be used to develop a variety of rich prompts that can be used to fine-tune the LLMs chosen by the user. The more diverse the datasets are, the better. The datasets will be split into train, dev, test splits for model training.

### Task 2: Fine Tune LLMs
The generated prompts datasets shall be used to fine tune locally tunable LLMs such as LLAMA and gptneo. Some models are fine tunable on local laptops but the other need the help of qlora. In this task, the participants explore options of fine tuning LLMs locally or using google colab.

### Task 3: Evaluate findings
The fine tuning of chosen LLMs will then be evaluated on test datasets and external datasets, such as Drugbank or a drug-target interaction network. Full text articles may also be provided to evaluate the inference on the text.

### Task 4: Chat interface
Due to the generative nature of LLMs, a chat interface can be a user friendly approach for using the models, if time permits.

## Proposed timeline

### Day 1 - 16th Jan
#### dataset curation and prompt engineering 
Most of the first day will be spent curating the prompt datasets and documenting the attributes of the datasets. Depending on participants and time, additional datasets, paths and prompts may be added to the collection. There should be aim to write documentation as a collective manuscript (eg. google doc)

### Day 2 - 17th Jan
#### testing viability of LLM models
The second day will be spent on testing the fine-tunability of the datasets on a few LLMS. The primary target will be the LLAMA model, but additional LLMs can also be tested. By the end of the day, the expected outcome will be to successfully fine-tune at least one LLM on the dataset collection.

### Day 3 - 18th Jan
#### Continuation of fine-tuning and evaluation
The plan for the third day of the BLAH8 hackathon is to finish fine-tuning the models and run evaluations. There will be an option to develop a chat interface through huggingface spaces if time permits.

### Day 4 - 19th Jan
#### Finalizing
The last day will incorporate finalizing the details of the project and presentation.


## Resources

TTD Datasets: https://db.idrblab.net/ttd/full-data-download

LLaMA access request: https://ai.meta.com/resources/models-and-libraries/llama-downloads/

Fine tuning LLAMA: https://www.leewayhertz.com/fine-tuning-llama2/

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
@misc{touvron2023llama,
      title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
      author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
      year={2023},
      eprint={2307.09288},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
