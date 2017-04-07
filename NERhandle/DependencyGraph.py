from nltk.parse.stanford import StanfordDependencyParser
import jieba
import jieba.posseg as pseg
from gensim.models import word2vec
import logging

jieba.load_userdict("userdict.txt")

yuliao = open('yuliao.txt')
seg_list = jieba.cut(yuliao.read())

# seg_list = jieba.cut("螺纹按其截面形状（牙型）分为三角形螺纹、矩形螺纹、梯形螺纹")
se = ''
for i in seg_list:
    se += i + ' '

print(se)

count = 0
res = ''
words = pseg.cut(se)
for word, flag in words:
    if (flag == 'n'):
        print('%s %s' % (word, flag))
        # res += word + ' / '
        res += word + ' '

#词向量需要分词文本语料
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u'testVec.txt' )  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

# 计算某个词的相关词列表
y2 = model.most_similar(u"螺纹", topn=40)  # 20个最相关的
count = 0
for item in y2:
        print(item[0], item[1])

chi_parser = StanfordDependencyParser(r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser-3.6.0-models.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/chinesePCFG.ser.gz"
                                      )
res = list(chi_parser.parse(se.split()))

for row in res[0].triples():
    print(row)