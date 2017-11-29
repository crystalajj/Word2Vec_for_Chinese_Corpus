import time
import jieba
#import codecs

jieba.enable_parallel(8)

input_ = '/Users/admin/Desktop/Segmentation/WikiExtractor/text/AA/transformed_zh_wiki.txt'
output = '/Users/admin/Desktop/Segmentation/WikiExtractor/text/AA/seg_jieba_zh_wiki.txt '


content = open(input_,"rb").read()
t1 = time.time()
words = " ".join(jieba.cut(content)) 

t2 = time.time()
tm_cost = t2-t1

log_f = open(output,"w")
log_f.write(words.encode('utf-8'))

print('speed %s bytes/second' % (len(content)/tm_cost))