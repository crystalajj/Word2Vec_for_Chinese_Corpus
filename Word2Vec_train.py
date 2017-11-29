# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import sys
import time
reload(sys) #reload sys
sys.setdefaultencoding("utf8") #default coding format

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('/Users/admin/Desktop/Segmentation/WikiExtractor/text/AA/seg_jieba_zh_wiki.txt', max_sentence_length=10000, limit=None)  # corpus

time0 = time.time()
model = word2vec.Word2Vec(sentences,sg=1)  # skip-gram
time_cost = time.time()-time0
print 'time cost: {} seconds'.format(time_cost)

#save model
#model.save('wiki_Chinese_vector_vc')
model.wv.save_word2vec_format('wiki_Chinese_vector_txt', binary=False)
print 'training is over.'