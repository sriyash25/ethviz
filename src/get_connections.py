import json
from collections import defaultdict

def get_new_connections(OG_GRAPH_PATH, NEW_GRAPH_CONNECTIONS_PATH):
    with open(OG_GRAPH_PATH, 'r') as f:
        original_graph = json.load(f)
        existing_nodes = set()

    for og_node in original_graph['nodes']:
        existing_nodes.add(og_node['id'])

    with open(NEW_GRAPH_CONNECTIONS_PATH, 'r') as f:
        data = json.load(f)

    new_edges = defaultdict(list)

    for node in data['links']:
        new_node = node['target']['id']
        connection = node['source']['id']

        if new_node not in existing_nodes:
            new_edges[new_node].append(connection)
    return new_edges

if __name__ == '__main__':

    # This is the original graph state
    og_graph_path = '/Users/sriyashcaculo/aic/ethvis/src/graphdata.json'

    # This is the the graph state after adding peers
    new_graph_connections_path = '/Users/sriyashcaculo/aic/ethvis/src/graph-data.json'
    
    new_edges = get_new_connections(og_graph_path, new_graph_connections_path)
    print(new_edges)