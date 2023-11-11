# BLAH8: Using LLMs to generate and identify drug and druggable target associations

## Introduction
Drug development is arguably one of the most critical challenges in medicine. There are several crucial steps that get us from idea to an usable drug. One of those steps are drug and druggable target identification. Many research approaches involve manually going through articles to find drug and druggable targets. Although painfully tedious, this approach brings results. However, this process can be exponentially fast-tracked with the help of Large Language Models (LLMs). 

There are many resources that contain manually annotated, drug and druggable target information, such as [Therapeutic Target Database](https://db.idrblab.net/ttd/full-data-download) (TTD). These rich collection of annotated data can be used to fine-tune existing LLMs and explore possibilities for discovering novel drug-target associations.

This project for the BLAH8 hackathon is aimed as a pilot study to develop drug-target specific prompt-based corpora with fine-tuning LLMs in mind. Participants can aim to develop question/answer, instruction or context-based corpora based on the given (TTD) or additional datasets. 

## Proposal Summary
In this project for the BLAH8 hackathon, we aim for the following tasks:

* Task 1: Design context and structure of prompts based on TTD resources
* Task 2: Build the prompts corpora based on the design decisions
* Task 3: Run feasibility check with LLMs
* Task 4 (if time permits): Fine-tune a LM with one corpus

## Breakdown of tasks

### Task 1: Design context and structure of prompts based on TTD resources
The TTD dataset not only contains drug and druggable targets information, but also contains a barrage of information such as Uniprot IDs, biomarkers, disease, functionality, pathway information etc. They can be used to develop a variety of rich prompts that can be used to fine-tune LLMs. The more diverse the datasets are, the better. Not only that, additional datasets and annotations, such as KEGG, Uniprot etc can be used to incorporate contexual knowledge within these prompts. Several design decisions need to be made in order to develop a set of rich corpora for training LLMs. For example, the corpora can be in the form of question-answer, instruction-context based or other formats.

As a sample, a question answer corpus has been constructed from the target/drug information, available in the data folder. The corpus contains 44431 lines (38mb). 

### Task 2: Build the prompts corpora based on the design decisions
Based on the design decisions, the corpora need to be build by the participants. Each member may explore different attributes of the dataset(s) and build their own prompt-based corpora. They can also vary based on the biological questions behind each individual drug/target. This task can be done on a local computer or in Google Colab.


### Task 3: Run feasibility check with LLMs
Once the corpora are ready, a feasibility check should be run to observe if the prompt-based fine-tuning works for LLMs. While running and fine-tuning LLMs are computationally heavy and scheduling tasks on Google colab can be uncertain, the aim here is to try running the model(s) with a few epochs only. 

### Task 4 (if time permits): Fine-tune a LM with one corpus
If the corpora building and feasibily checks are successfull and performed within the timeframe, then the participants can aim to fully fine-tune an open source LLM. Theoritically, this should be doable with the help of approaches, such as qlora, within the timeframe.

## Proposed timeline

### Day 1 - 16th Jan
#### dataset exploration, understanding and prompt design
Most of the first day shall be spent exploring the TTD and additional datasets and designing the prompts. Depending on participants and time, additional datasets, paths and prompts may be added to the collection. Agreements on participant roles/contribution, annotations and augmentation shall also be made. There shall be aim to write documentation as a collective manuscript (eg. google doc)

### Day 2 - 17th Jan
#### Building the corpora
Following the design decisions, the second day will be spent on building the prompt/instruction based corpora. If there is time remaining, the participants may start with a feasibility check with LLMs.

### Day 3 - 18th Jan
#### Run feasibility check with LLMs
The plan for the third day of the BLAH8 hackathon is to try fine-tuning an LLM for one/few epochs. The participants may try several LLMs such as LLaMA, Mistral_7b, GPT_neo etc. and find one that is least computationally demanding and most efficient. If time is remaining, then a step towards full fine-tuning of an LLM shall be taken. 

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
