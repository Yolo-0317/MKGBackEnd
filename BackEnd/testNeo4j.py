import requests

query_node = {
        "query": "MATCH (n) RETURN n",
        "params": {}
    }
rn = requests.post("http://localhost:7474/db/data/cypher", data=query_node, auth=('neo4j', 'database'))
rns = rn.json()
for i in rns:
    print(i)
    # print(i[0]['data']['name'], i[0]['metadata']['id'])