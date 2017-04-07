from nltk.parse.stanford import StanfordDependencyParser

from BackEnd.NLP import NER, CUT

chi_parser = StanfordDependencyParser(r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser-3.6.0-models.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/chinesePCFG.ser.gz"
                                      )

# senStr = '在圆柱或圆锥母体表面上制出的螺旋线形的、具有特定截面的连续凸起部分。螺纹按其母体形状分为圆柱螺纹和圆锥螺纹；'

def sentence_re(senStr):
    seg_list = CUT.jiebaCut(senStr)
    se = ''
    for i in seg_list:
        se += i + ' '
    print(se)

    ner = NER.nerForRE(senStr)
    print(ner)

    res = list(chi_parser.parse(se.split()))
    print(res)
    for row in res[0].triples():
        for n in ner:
            if(n == row[0][0] or n == row[2][0]):
                print(row)

# sentence_re(senStr)
