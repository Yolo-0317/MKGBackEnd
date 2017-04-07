import jieba
import jieba.posseg as pseg

jieba.load_userdict("userdict.txt")

yuliao = open('yuliao.txt')

seg_list = jieba.cut(yuliao.read())

se = ''
for i in seg_list:
    # print(i)
    # se += i + ' / '
    se += i + ' '
print(se)

count = 0
result = ''
words = pseg.cut(se)
for word, flag in words:
    #只取名词
    if flag == 'n':
        print('%s %s' % (word, flag))
        result += word + ' '
print(result)