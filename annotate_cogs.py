#!/usr/bin/env python

import sys
import gzip
from collections import Counter

func_categories_file = sys.argv[1]
func_file = sys.argv[2]
# func_file = sys.stdin
cog_file = sys.argv[3]

# Initialize variables
category2description = {}
cog2category = {}
category2count = Counter()
my_cogs = set()


# Step 1: Read description of functional categories
with open(func_categories_file) as fin:
    for line in fin:
        if len(line) > 1 and line[1] == "[":        
            category = line[2]
            description = line[5:-2]
            category2description[category] = description


# Step 2: Read file with OGs of interest
with open(cog_file) as fin:
    next(fin)
    for line in fin:
        my_cogs.add(line.split("\t")[0])


# Step 3: Read file with functional annotations
# and remember those for OGs of interest
# gzip: "rt" required for text mode, see https://docs.python.org/3/library/gzip.html
with gzip.open(func_file, "rt") as fin:
    for line in fin:
        level, cog_id, category, comment = line.split("\t")
        cog2category[cog_id] = category


# Step 4: Count and output the categories for OGs of interest
# print(cog2category)
# print(category2description)
# print(my_cogs)
for cog in my_cogs:
    # Counter.update adds and counts all characters in the string
    category2count.update(cog2category[cog])

    #print(category2count.most_common())
for cat, i in category2count.most_common():
    # print(cat)
    # print(i)
    print(f"{i}\t{category2description[cat]}")
