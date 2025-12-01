"""
5. “Anagram-Group Detection” [Optional]

Problem: Given a list of strings (words), group them by anagram equivalence: i.e. output a list of groups,
where each group contains words that are anagrams of each other. Words that don't match any other stay
alone. Example: input ["eat", "tea", "tan", "ate", "nat", "bat"] → output e.g.
[["eat","tea","ate"], ["tan","nat"], ["bat"]]. Order within groups and order of
groups can follow input order or sorted — define specification clearly.

"""
s_list=["eat", "tea", "tan", "ate", "nat", "bat"]
d={}
for i in s_list:
    key="".join(sorted(i))
    #print(key)
    if key not in d:
        d[key]=[]
    d[key].append(i)
print(list(d.values()))
