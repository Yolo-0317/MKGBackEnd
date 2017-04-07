from nltk.parse.stanford import StanfordDependencyParser

chi_parser = StanfordDependencyParser(r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/stanford-parser-3.6.0-models.jar",
                                      r"/Users/baymax/Dev/library/stanford/segmenter/chinesePCFG.ser.gz"
                                      )

se = ''
for line in open(u'testDG.txt').readlines():
    se += line
print(se)

res = list(chi_parser.parse(se.split()))

print(res)
for row in res[0].triples():
    print(row)