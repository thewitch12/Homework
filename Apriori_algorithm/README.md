## Introduction
---
This project was created for the assignment given in my college data science class.
In the class, the task was to implement **Apriori algorithm** in language of my choice.

First, I chose **python** because I thought it would be the easiest.

However after completing assignment, the result wasn't satisfied though it worked.
The code was too rough to understand at first glance and too slow.
Also, I wanted implementing this algorithm in other languages.

So, I decided to rewrite Apriori algorithm implementation.
Each directory in this project is the version written in the language.
The python version was the first, which is messy.

Each version has the README.md file with specification.
All versions share the input format which was suggested by my class TA.
Although the input format is described in each version's README, I also wrote it here.


### Input Format
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