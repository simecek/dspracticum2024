**Date**: Oct 14, 2024

**Studio:** No new studio (just install `transformers` into the old one)

**Slides**: https://docs.google.com/presentation/d/1sHFei0MfeUJGxMtIPV0wRnk5RyEnh3qkrdaq9SMkJuY/edit?usp=sharing

* Embeddings 
* Explainability 
* Backprogation

**Assignment 04** (due to Oct 21, 8:30 AM):

* There are models that give you embeeddings both for images and texts. One of them is [CLIP](https://huggingface.co/openai/clip-vit-base-patch32), see [HW4_hints_CLIP.ipynb](HW4_hints_CLIP.ipynb) how to use it. Your goal is to use the model to find the most similar image(s) to a given text.
* To be more specific, take the dataset prepared in HW2, calculate its CLIP embeddings and save them into a file. Create gradio app that takes a text as an input and outputs 4 most similar images from the dataset.
* You can use code in [HW4_hints_CLIP.ipynb](HW4_hints_CLIP.ipynb) to guide you but the design of app is your task. Do not forget to add `transformers` into `requirements.txt` file. For similarity measure, I recommend to use [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity), i.e. dot product of normalized vectors.
* Fill in the link to the app into the form (the form distributed via Slack).

