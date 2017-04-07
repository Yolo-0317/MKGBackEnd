import jieba
import jieba.posseg as pseg

# jieba.load_userdict("userdict.txt")

def jiebaCut(senStr):
    return jieba.cut(senStr)

def cutSenStr(senStr):
    seg_list = jieba.cut(senStr)
    se = ''
    for i in seg_list:
        se += i + ' / '
    return se
    # print(se)