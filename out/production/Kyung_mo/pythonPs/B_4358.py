import sys
from collections import defaultdict

trees = defaultdict(int)
tree_num = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if tree == '':
        break
    tree_num += 1
    trees[tree] += 1

tree_list = sorted(trees, key=lambda x: x[0])

for tree in tree_list:
    print('%s %.4f' %(tree, (trees[tree]/tree_num) * 100))