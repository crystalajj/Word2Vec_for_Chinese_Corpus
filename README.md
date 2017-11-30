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
