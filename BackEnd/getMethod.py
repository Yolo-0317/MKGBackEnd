# -*- coding: utf-8 -*-
import requests

from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "database"))

# 获取所有节点和关系，用于查询一个label时返回
def getAllNodeAndRelation():
    # query = {
        # "query": "MATCH (n1)-[r1]-(m1)-[r2]->(m2) RETURN n1, r1, m1, r2, m2 LIMIT 40",
        # "query": "MATCH (n)-[]->(m) RETURN n, m",
        # "query": "MATCH (n) RETURN n",
        # "query": "MATCH ()-[r]->() RETURN r",
        # "query": "MATCH (n:`螺纹联接`) RETURN n",
        # "query": "MATCH (n)-[r]->(m) RETURN n, r, m",
        # "params": {}
    # }
    # res = requests.post("http://localhost:7474/db/data/cypher", data=query, auth=('neo4j', 'database'))
    # res = requests.post("http://localhost:7474/db/data/transaction/commit", data=query, auth=('neo4j', 'database'))
    allInfo = []
    session = driver.session()

    res = session.run("MATCH (a)-[r]->(b) RETURN a, r, b")
    for record in res:
        allInfo.append({
            'start': {
                'id': record['a'].id,
                'props': record['a'].properties
            },
            'relation': {
                'start': record['r'].start,
                'props': record['r'].properties,
                'end': record['r'].end,
                'type': record['r'].type
            },
            'end': {
                'id': record['b'].id,
                'props': record['b'].properties
            }
        })

    session.close()

    return {'res': allInfo, 'totalNum': len(allInfo)}

# 获取所有的节点
def getAllNodes():
    allNodes = []
    session = driver.session()
    result = session.run("MATCH (a) RETURN a")
    for record in result:
        allNodes.append({
            'id': record['a'].id,
            'props': record['a'].properties
        })
    session.close()
    return {'res': allNodes, 'totalNum': len(allNodes)}
#获取所有的关系
def getAllRelations():
    allRelations = []
    session = driver.session()
    result = session.run("MATCH (a)-[r]->(b) RETURN a, r, b")
    for record in result:
        allRelations.append({
            'start': {
                    'id': record['a'].id,
                    'props': record['a'].properties
            },
            'relation': {
                'start': record['r'].start,
                'props': record['r'].properties,
                'end': record['r'].end,
                'type': record['r'].type
            },
            'end': {
                'id': record['b'].id,
                'props': record['b'].properties
            }
        })
    session.close()
    return {'res': allRelations, 'totalNum': len(allRelations)}

# 查询 key 时的返回
def getSearchKey(key):
    query = {
        "query": "MATCH (n)-[r]->() where n.name = '%s' RETURN n, r" % (key),
        "params": {}
    }
    res = requests.post("http://localhost:7474/db/data/cypher", data=query, auth=('neo4j', 'database'))
    print(res.json())
    return res.json()


if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")