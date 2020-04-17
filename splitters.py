#import torch.nn as nn
from fastai2.basics import *

def bert_cls_splitter(m):
    "Split the classifier head from the backbone"
    groups = [nn.Sequential(m.transformer.bert.embeddings,
                m.transformer.bert.encoder.layer[0],
                m.transformer.bert.encoder.layer[1],
                m.transformer.bert.encoder.layer[2],
                m.transformer.bert.encoder.layer[3],
                m.transformer.bert.encoder.layer[4],
                m.transformer.bert.encoder.layer[5],
                m.transformer.bert.encoder.layer[6],
                m.transformer.bert.encoder.layer[7],
                m.transformer.bert.encoder.layer[8],
                m.transformer.bert.encoder.layer[9],
                m.transformer.bert.encoder.layer[10],
                m.transformer.bert.encoder.layer[11],
                m.transformer.bert.pooler)]
    groups = L(groups + [m.transformer.classifier]) 
    return groups.map(params)


def albert_cls_splitter(m):
    groups = [nn.Sequential(m.transformer.albert.embeddings,
                m.transformer.albert.encoder.embedding_hidden_mapping_in, 
                m.transformer.albert.encoder.albert_layer_groups,
                m.transformer.albert.pooler)]
    groups = L(groups + [m.transformer.classifier]) 
    return groups.map(params)


def distilbert_cls_splitter(m):
    groups = [nn.Sequential(m.transformer.distilbert.embeddings,
                m.transformer.distilbert.transformer.layer[0], 
                m.transformer.distilbert.transformer.layer[1],
                m.transformer.distilbert.transformer.layer[2],
                m.transformer.distilbert.transformer.layer[3],
                m.transformer.distilbert.transformer.layer[4],
                m.transformer.distilbert.transformer.layer[5],
                m.transformer.pre_classifier)]
    groups = L(groups + [m.transformer.classifier]) 
    return groups.map(params)


def roberta_cls_splitter(m):
    "Split the classifier head from the backbone"
    groups = [nn.Sequential(m.transformer.roberta.embeddings,
                  m.transformer.roberta.encoder.layer[0],
                  m.transformer.roberta.encoder.layer[1],
                  m.transformer.roberta.encoder.layer[2],
                  m.transformer.roberta.encoder.layer[3],
                  m.transformer.roberta.encoder.layer[4],
                  m.transformer.roberta.encoder.layer[5],
                  m.transformer.roberta.encoder.layer[6],
                  m.transformer.roberta.encoder.layer[7],
                  m.transformer.roberta.encoder.layer[8],
                  m.transformer.roberta.encoder.layer[9],
                  m.transformer.roberta.encoder.layer[10],
                  m.transformer.roberta.encoder.layer[11],
                  m.transformer.roberta.pooler)]
    groups = L(groups + [m.transformer.classifier])
    return groups.map(params)

splitters = {'bert_cls_splitter':bert_cls_splitter,
            'albert_cls_splitter':albert_cls_splitter,
            'distilbert_cls_splitter':distilbert_cls_splitter,
            'roberta_cls_splitter':roberta_cls_splitter}