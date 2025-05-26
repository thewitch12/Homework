import sys
from math import floor

# return the list of subsets (it's length is len(superset)-1 )
def find_subset_nminus1(super_set: list):
    set_len = len(super_set)
    tmp_subset = []
    ret_subset = []
    for i in range(set_len):
        tmp_subset = []
        for j in range(set_len):
            if (1<<i) ^ (1<<j):
                tmp_subset.append(super_set[j])
        ret_subset.append(set(tmp_subset))
    return ret_subset

#find the line of transaction where the super set of the target set appears
def where_they_appear(target_set: set):
    target_list = list(target_set)
    where = set(line_list)
    for num in target_list:
        where = where & set(tmp_pattern[num])
    return where

def hand_round(num, place):
    return floor(num * 100 + 0.5) / 100

file = open(sys.argv[2], 'r')
raw_transactions = file.readlines()
file.close()

transactions = []
tmp_pattern = {} 
frequent_patterns = [[]]

#data preprocessing
for raw_trans_list in raw_transactions: 
    transactions.append(list(map(lambda x: int(x), raw_trans_list.split())))
line_num = len(transactions)
line_list = list(range(line_num))
min_sup = line_num * int(sys.argv[1]) / 100

#frequency counting
for i in line_list:
    for num in transactions[i]:
        if num in tmp_pattern:
            tmp_pattern[num].append(i)
        else:
            tmp_pattern[num] = []
            tmp_pattern[num].append(i)

# one frequent item
for item in tmp_pattern:
    if len(tmp_pattern[item]) >= min_sup:
        frequent_patterns[0].append(set([item]))

item_len = 2
while True:
    candidate_selfjoin = []
    candidate_pruning = []
    frequent_patterns.append([])
    #self joining
    for base_num_set in frequent_patterns[item_len-2]:
        for base_num2_set in frequent_patterns[item_len-2]:
            if len(base_num_set & base_num2_set) == item_len-2:
                tmp_or_set = base_num_set | base_num2_set
                if tmp_or_set not in candidate_selfjoin:
                    candidate_selfjoin.append(tmp_or_set)
    
    #pruning
    for item_set in candidate_selfjoin:
        isPass_itemset = True
        #check each subset of item set
        for subset in find_subset_nminus1(list(item_set)):
            isPass_subset = False
            for compare_set in frequent_patterns[item_len-2]:
                if subset == compare_set:
                    isPass_subset = True
                    break
            if isPass_subset == False:
                isPass_itemset = False
                break
        
        if isPass_itemset:
            candidate_pruning.append(item_set)

    #check frequency
    for item_set in candidate_pruning:
        if len(where_they_appear(item_set)) >= min_sup:
            frequent_patterns[item_len-1].append(item_set)

    if len(frequent_patterns[item_len-1]) == 0:
        frequent_patterns.pop()
        break
    
    item_len += 1

#preprocessing for association rule mining
flatten_pattern = []
for pat_list in frequent_patterns:
    for item_set in pat_list:
        flatten_pattern.append(item_set)

#calculate and print assciation (brute force)
fw = open(sys.argv[3], "w")
for set1 in flatten_pattern:
    for set2 in flatten_pattern:
        if set1==set2 or len(set1 & set2) > 0: continue
        and_tmp = where_they_appear(set1) & where_they_appear(set2)
        if len(and_tmp) >= min_sup:
            sup = format(hand_round((len(and_tmp) / line_num * 100), 2), '.2f')
            conf = format(hand_round(len(and_tmp) / len(where_they_appear(set1)) * 100, 2), '.2f')

            #write file
            for_write = "{"
            for_write += ",".join(list(map(lambda x: str(x), list(set1))))
            for_write += '}\t'

            for_write += "{"
            for_write += ','.join(list(map(lambda x: str(x), list(set2))))
            for_write += '}\t'

            for_write += str(sup)
            for_write += '\t'

            for_write += str(conf)
            for_write += '\n'

            fw.write(for_write) 
fw.close()

print('Done')









