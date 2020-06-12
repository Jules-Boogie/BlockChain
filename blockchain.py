
blockChainList = [1]

def get_last_amount():
    """
    Retrieves the last value entered into the BlockChainList
    

    Arguments:
        :None
    """
    return blockChainList[-1]


def add_to_blockList(current_amount, last_amount):
    """
    Adds a last value in the blockchain and a new value to the blockchainList


    Arguments:
        :current_amount: the last value in the blockChainList
        :last_amount: the new value to be added to the blockChainlist
    """
    blockChainList.append([current_amount,last_amount])
    
add_to_blockList(get_last_amount(), 3)

# get user input

user_input = float(input("please enter transaction amount: "))
add_to_blockList(get_last_amount(), user_input)
print(blockChainList)