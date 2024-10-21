**Date**: Oct 21, 2024

**Studio:** No new studio, no GPU needed (just install `datasets` and `tiktoken`)

**Slides**: https://docs.google.com/presentation/d/1Ywu1ojaWHUUl8mdqyaNmCyAw33e9IakuKf3p_P5Gygg/edit?usp=sharing

* Adversarial examples
* [Datasets](Datasets_intro.ipynb) package
* [Tokenizers](Tokenization.ipynb)

**Links**:

* [Tiktokenizer app](https://tiktokenizer.vercel.app)
* [HuggingFace NLP Course](https://huggingface.co/learn/nlp-course/en/chapter1/1)
* [Andrej Karpathy: Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)

**Assignment 05** (due to Nov 4, 8:30 AM):

Your goal is to create a text dataset and push it to HuggingFace Hub:

 * Language of dataset *must* be Czech or Slovak
 * 1000 - 50 000 examples in train split
 * 200 000 - 2 000 000 GPT2 tokens in train split, use `tiktoken` to compute the number of tokens (`len(enc.encode(text))`)
 * You may or may not include test split
 * More details and link to the submission form on Slack


