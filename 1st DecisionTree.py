import math
from collections import Counter, defaultdict

# Play Tennis Dataset
data = [
    ["Sunny","Hot","High","Weak","No"],
    ["Sunny","Hot","High","Strong","No"],
    ["Overcast","Hot","High","Weak","Yes"],
    ["Rain","Mild","High","Weak","Yes"],
    ["Rain","Cool","Normal","Weak","Yes"],
    ["Rain","Cool","Normal","Strong","No"],
    ["Overcast","Cool","Normal","Strong","Yes"],
    ["Sunny","Mild","High","Weak","No"],
    ["Sunny","Cool","Normal","Weak","Yes"],
    ["Rain","Mild","Normal","Weak","Yes"],
    ["Sunny","Mild","Normal","Strong","Yes"],
    ["Overcast","Mild","High","Strong","Yes"],
    ["Overcast","Hot","Normal","Weak","Yes"],
    ["Rain","Mild","High","Strong","No"]
]

features = ["Outlook","Temperature","Humidity","Wind"]

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((c/total)*math.log2(c/total) for c in counts.values())

def information_gain(data, index):
    total_entropy = entropy([row[-1] for row in data])
    groups = defaultdict(list)
    for row in data:
        groups[row[index]].append(row)

    weighted_entropy = 0
    for group in groups.values():
        weighted_entropy += (len(group)/len(data)) * entropy([row[-1] for row in group])

    return total_entropy - weighted_entropy

def id3(data, features):
    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not features:
        return Counter(labels).most_common(1)[0][0]

    gains = [information_gain(data, i) for i in range(len(features))]
    best_attr = gains.index(max(gains))

    tree = {features[best_attr]: {}}
    attr_values = set(row[best_attr] for row in data)

    for value in attr_values:
        subset = [row[:best_attr] + row[best_attr+1:] for row in data if row[best_attr] == value]
        sub_features = features[:best_attr] + features[best_attr+1:]
        tree[features[best_attr]][value] = id3(subset, sub_features)

    return tree

print("Decision Tree (Play Tennis):")
print(id3(data, features))
