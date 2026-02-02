import math
from collections import Counter, defaultdict

# Dataset
data = [
    [True,"Hot","High","No"],
    [True,"Hot","High","No"],
    [False,"Hot","High","Yes"],
    [False,"Cool","Normal","Yes"],
    [False,"Cool","Normal","Yes"],
    [True,"Cool","High","No"],
    [True,"Hot","High","No"],
    [True,"Hot","Normal","Yes"],
    [False,"Cool","Normal","Yes"],
    [False,"Cool","High","Yes"]
]

features = ["A1","A2","A3"]

# Entropy
def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

# Information Gain
def info_gain(data, idx):
    total_entropy = entropy([row[-1] for row in data])
    groups = defaultdict(list)
    
    for row in data:
        groups[row[idx]].append(row)
        
    weighted = 0
    for g in groups.values():
        weighted += (len(g)/len(data)) * entropy([r[-1] for r in g])
        
    return total_entropy - weighted

# ID3
def id3(data, features):
    labels = [row[-1] for row in data]
    
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    if not features:
        return Counter(labels).most_common(1)[0][0]
    
    gains = [info_gain(data,i) for i in range(len(features))]
    best = gains.index(max(gains))
    
    tree = {features[best]:{}}
    
    values = set(row[best] for row in data)
    for v in values:
        subset = [row[:best]+row[best+1:] for row in data if row[best]==v]
        sub_feat = features[:best]+features[best+1:]
        tree[features[best]][v] = id3(subset, sub_feat)
        
    return tree

# Pretty print tree
def print_tree(tree, indent=""):
    if isinstance(tree, dict):
        for key, value in tree.items():
            print(indent + str(key))
            for v, subtree in value.items():
                print(indent + " ├──", v)
                print_tree(subtree, indent + " │   ")
    else:
        print(indent + " →", tree)

tree = id3(data, features)

print("\nDecision Tree:\n")
print_tree(tree)
