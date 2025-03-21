# -*- coding: utf-8 -*-
"""topic_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12cxr_wEi_s-Z-ChQig2wpDYWqG4CYawM
"""

pip install transformers torch

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
model_name = "cardiffnlp/tweet-topic-21-multi"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
labels =[
    "arts_&_culture","business_&_entrepreneurs","celebrity_&_pop_culture","dairies_&_daily_life",
    "family","fashion_&_style"
]
texts = [
    "The latest iphone was just released with an incredible new camera!",
    "Manchester United won their match with a stunning goal in the last minute."
    "NASA just launched a new mission to explore the surface of Mars."
    "The Oscars had some surprising winnr this year!"
]
inputs  = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
ptobabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
#predictions = torch.argmax(probabilities, dim=-1)
#for text,pred,prob in zip(texts,predictions,probabilities):
# print(f"Text:{text}\nTopic:{[labels[pred.item()]]},Confidence:{prob[pred].item(:4f)\n}")

from transformers import pipeline
summarizer = pipeline("summarization")
text = """
Hugging Face is a company that specializes in natural language processing(NLP.)
It has developd the Transformers library,which provides state-of-artvmodels
for a wide range of NLP tasks such as text classification ,information extraction,
question answering,summarization,translation,and more.The library is widely used
in both academia and industry due to its ease of use and flexibily
 """
summary = summarizer(text,max_length=50,min_length=10,do_sample=False)
print(summary[0]['summary_text'])

##https://huggingface.co/cardiffnlp/tweet-topic-21-multi

from transformers import AutoModelForCasualLM, AutoTokenizer
import torch
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

