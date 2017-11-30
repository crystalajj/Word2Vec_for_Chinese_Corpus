# Word2Vec_for_Chinese_Corpus
Train character vector representation for Chinese Corpus.
## Processing Outline

### 1. Extract Chinses corpus files from Wiki dump

Use data set: *zhwiki-20170220-pages-articles1.xml.bz2*

[Data Download Site](http://wikimedia.bytemark.co.uk/zhwiki/20170220/)


Perform **WikiExtractor.py** to get wiki\_00~wiki\_07 files.

Use

```
cat wiki_* > processed_zhwiki.txt
```
to get these files together.


### 2. Chinese Convert

Perform Traditional Chinese to Simplified Chinese conversion by using **openCC**.
> Common Methods of Chinese convert:
> 
> - **OpenCC**: [Github](https://github.com/BYVoid/OpenCC#installation-安裝)
> - Wikipedia: [Wikipedia](https://zh.wikipedia.org/wiki/Wikipedia:繁简处理)

code:
```
/usr/local/Cellar/opencc/1.0.4/bin/opencc   -i processed_zhwiki.txt  -o transformed_zh_wiki -c /usr/local/Cellar/opencc/1.0.4/share/opencc/t2s.json 
```

### 3. Delete empty brackets 
Delete empty brackets caused by using WikiExtractor.py

### 4. Segmentation

Execute **Tokenization.py** to perform segmentation by using **Jieba**. 
> Common Methods of segmentation:
>
Methods of Chinese Segmentation         | Algorithm           | Related Link 
--------------------|------------------|-----------------------|
Jieba | Based on a **prefix dictionary structure** to achieve efficient word graph scanning. Build a directed acyclic graph (**DAG**) for all possible word combinations.Use **dynamic programming** to find the most probable combination based on the word frequency.For unknown words, a **HMM-based** model is used with the **Viterbi algorithm**.   | [Github](https://github.com/fxsjy/jieba)   | Sun, J. "‘Jieba’Chinese word segmentation tool." (2012).|
THULAC(THU Lexical Analyzer for Chinese)       | Based on Structured Perceptron   | [Github](https://github.com/thunlp/THULAC) [paper(2009)](http://www.mitpressjournals.org/doi/pdf/10.1162/coli.2009.35.4.35403)   |  Maosong Sun, Xinxiong Chen, Kaixu Zhang, Zhipeng Guo, Zhiyuan Liu. THULAC: An Efficient Lexical Analyzer for Chinese. 2016.|
StanfordSegmenter  | Based on CRF      |    [Github](https://github.com/banyh/PyStanfordNLP) [Tutorials](https://nlp.stanford.edu/software/segmenter.shtml) [paper(2005)](https://nlp.stanford.edu/pubs/sighan2005.pdf)  [paper(2008)](https://nlp.stanford.edu/pubs/acl-wmt08-cws.pdf)   |


### 5. Word2Vec(Skip-gram) In Gensim

Perform to **Word2Vec\_train.py** to train character vector for Chinese corpus.

Parameter Set:

- sg = 1 # use skip-gram
- hs = 0 and negative=5 # use negative sample not hierarchical softmax
- size = 100 # the dimensionality of the feature vectors
- alpha = 0.025 #  learning rate
- window = 5 # content window
- min_count=5 # ignore all words with total frequency lower than 5
- sample = 0.001 # threshold for configuring which higher-frequency words are randomly downsampled; default is 1e-3, useful range is (0, 1e-5).
- batch_words = 10000 # target size for batches of examples passed to worker threads 


[API document of Word2Vec in gensim](https://radimrehurek.com/gensim/models/word2vec.html#gensim.models.word2vec.LineSentence)

You can review the results at [here](https://www.dropbox.com/sh/eqftsar7jwmw375/AADxdbI6ueB5vTjHYIpaXn8Za?dl=0).
