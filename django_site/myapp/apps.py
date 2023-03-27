from django.apps import AppConfig

# import torch
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import TextClassificationPipeline


def pos_neg_search(arr):
    pn = np.argmax([np.sum(arr[:4]), np.sum(arr[6:])])
    if pn == 1:
        return 'positive'
    if pn == 0:
        return 'negative'
    return 'neutral'

def binary_search(arr):
    pn = np.argmax([np.sum(arr[:4]), np.sum(arr[6:])])
    if pn == 0:
        pn = np.argmax([np.sum(arr[:2]), np.sum(arr[2:4])])
        if pn == 0:
            return np.argmax([arr[0], arr[1]]) + 0 + 1
        else:
            return np.argmax([arr[2], arr[3]]) + 2 + 1
    else:
        pn = np.argmax([np.sum(arr[6:8]), np.sum(arr[8:10])])
        if pn == 0:
            return np.argmax([arr[6], arr[7]]) + 6 + 1
        else:
            return np.argmax([arr[8], arr[9]]) + 8 + 1

label2id = {
    "LABEL_0": 0,
    "LABEL_1": 1,
    "LABEL_2": 2,
    "LABEL_3": 3,
    "LABEL_4": 4,
    "LABEL_5": 5,
    "LABEL_6": 6,
    "LABEL_7": 7,
    "LABEL_8": 8,
    "LABEL_9": 9}

def get_arr_from_label_scores(ls):
    arr = np.zeros(10)
    for d in ls[0]:
        lab, score = d['label'], d['score']
        id = label2id[lab]
        arr[id] = score
    return arr

def get_prediction(ls):
    arr = get_arr_from_label_scores(ls)
    pred_3 = pos_neg_search(arr)
    pred_10 = binary_search(arr)
    return {'sentiment' : pred_3, 'stars' : pred_10}

class MyappConfig(AppConfig):
    name = 'bert'
    PATH = './bert_1/'
    PATH = 'bert-base-uncased'
    model = AutoModelForSequenceClassification.from_pretrained(PATH, num_labels=10)
    tokenizer = AutoTokenizer.from_pretrained(PATH)
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=True)
    get_prediction = get_prediction
