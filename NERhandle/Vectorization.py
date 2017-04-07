# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus(u'luowen_train.txt' )  # 加载语料
sentences = word2vec.Text8Corpus(u'testVec.txt' )  # 加载语料
model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5

model.save('w2v_model')


# 计算某个词的相关词列表
y2 = model.most_similar(u"螺纹", topn=20)  # 20个最相关的
# print(u"和【螺纹】最相关的词有：\n")
count = 0
for item in y2:
    # if(count < 3):
    #     count += 1
        print(item[0], item[1])