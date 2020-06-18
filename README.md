# BlockChain

Building a data storage consisting of connected blocks using python. 


```
blockChainList = []

def addtoBlockList(x):
    blockChainList.append(x)
    print(blockChainList)
addtoBlockList(5)
```


#information about Blockchain
-multiple transactions in a block, 
- a transaction = sender, recipient, amount 
- list of multiple outstanding transactions


Data structures for the project:

transaction - data structure that stores key-value pairs
multiple transactions - list of transactions
block - list of processed transactions
participants - list to manage participants - datastructure should save unique strings


Iterable Datastructures in Python:
List = ['Milk','Honey','Milk'], mutable, ordered, can have duplicates. 

Set = {'Milk', 'Honey'}, can't have duplicate, unordered, mutable

Tuple = ('Milk', 'honey'), can't mutate, ordered list, duplicates allowed,
Dictionary = {"name": 'milk'}, key value pair, mutable, unordered


In cryptocurrency, transactions typically have a sender, a receiver ,and an amount. A new transaction is open until it has been added to a block. 

