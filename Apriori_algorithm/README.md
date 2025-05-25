## Introduction
---
This project is for the assignment in CSE data science class. 
The assignment was for checking the understanding of Apriori algorithm. (also brute force Association rule mining)
I chosed python to implement it because I thought data structure like dictionary and set would be useful.

The main operator I used in this project is set-union and set-intersection. 

### command
---
$ python3 apriori.py (min_support) (Input File name) (Output File name)
ex. $ python3 apriori.py 5 input.txt output.txt
(Unless output file, input file should exist in the root directory.)

This command will return the output file whose format will be explained below.
The file will appear in the root directory.

### input_format
---
[item_id]\t[item_id]\n
[item_id]\t[item_id]\t[item_id]\n
[item_id]\n

example.
4\t5\n
6\t7\t100\n
9\n

Each row means the transaction. And the item_id means the item bought in the transaction. (The item_id is numerical value.)
I assumed that each transaction does not contain duplicated item.
I recommend txt file.

### output_format
---
Even though you don't know the format of output file, the file would be generated corrctly.

[item_set]\t[associated_item_set]\t[support(%)]\t[confidence(%)]\n

Each row means one association rule.
item_set and associated_item_set's format is {a,b,c}. ex. {1,2,5}

Each association rule ([item_set] => [associated_item_set])'s support is over min_support. But the min_confidence is not considered because of assignment spec. (But It would be printed too)