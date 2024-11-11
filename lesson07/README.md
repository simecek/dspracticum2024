**Date**: Nov 11, 2024

**Studio**: https://lightning.ai/simecek/studios/lesson-07~01hv3p406bs3pebc3xm2qwtwz1

**Slides**: https://docs.google.com/presentation/d/1NhpORR4EiickA8jOaWbfbSMDTefSJl30qm2bJaQeojU/edit?usp=sharing

* Large language models: llama, mistral, gemma...
* Fine-tuning: LoRA, QLoRA, PEFT
* ChatGPT, Clade, Gemini API


**Links**:

* [Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch/tree/main)
* [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/pdf/2302.13971)

**Assignment 07** (due to Nov 18, 8:30 AM):

1. I have added questions we created today to a set of questions from the previous workshop, so the total is **90** [A/B/C/D questions](ABCD.csv). Choose some open large language model we have not used today (e.g. speakleash/Bielik-11B-v2.3-Instruct, google/gemma-2-27b-it, Qwen/Qwen2.5-7B-Instruct, mistralai/Ministral-8B-Instruct-2410, meta-llama/Llama-3.1-8B-Instruct...), evaluate it on this benchmark (analogously as [here](01_Talk_to_models.ipynb) or [there](04_ChatGPT_API.ipynb)) and share its *accuracy* and *3-4 examples* of its mistakes.

2. Take a sample of 50 rows from your HW05 dataset. Use [gpt-4o-mini](04_ChatGPT_API.ipynb) model to extract some small information from each text (e.g. summary in 1 sentence, 3 most important facts, list of mentioned characters, etc.). Save the results to a CSV file or push this data to HF Hub.

3. Train a small open model (e.g. gemma-2-2b) on dataset generated in 2), push the model to HF Hub and test it on some new text (not being used for training in 2).



