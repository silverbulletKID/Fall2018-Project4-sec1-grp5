# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:19:48 2018

@author: Chenghao
"""

from pyxdameraulevenshtein import damerau_levenshtein_distance
from nltk.metrics.distance import edit_distance
import py_common_subseq.py_common_subseq as CS #Need to change xrange() as range()
import math
import pandas as pd
import jieba
import copy
import sys
sys.path.append("..")
from lib.functions import project4 as p4 


Dictionary = pd.read_csv("../output/test_dictionary.csv").word
Threshold = 3
We = 'rah'
    
Candidates = p4.candidate_search(Dictionary, We, Threshold)
dist_score = p4.distance_score(Candidates, We, Threshold)
a1=0.25
a2=0.25
a3=0.25
a4=0.25
simi_score = p4.similarity_score(Candidates, We, a1, a2, a3, a4)

#------------------------------

# =============================================================================
# 
# from collections import Counter
# 
# file_object = open('../data/ground_truth/group1_00000005.txt')
# try:
#     file_context = file_object.read()
# finally:
#     file_object.close()
# 
# 
# 
# text = file_context
# data_ = jieba.cut(text)
# data = dict(Counter(data_))
# data['rch']
# =============================================================================
We = "eve"
Wc = "King"
test = ["apple bee car dog eve", "bee car dog eve fat", "car dog eve fat get", "dog eve fat get hi", "eve fat get hi ill"]
grams_e = []
grams_C_X = []
for grams in test:
    grams_e.append(grams.replace(We, Wc, 1))
for i in range(5):
    five_gram_s = list(jieba.cut(grams_e[i]))
    for k in range(5):
        if -i+4==k:
            continue
        else:
            five_gram_s_copy = copy.deepcopy(five_gram_s)
            five_gram_s_copy[2*k] = "*"
            gram_c_x = "".join(five_gram_s_copy)
            grams_C_X.append(gram_c_x)
            
print(grams_C_X)
        