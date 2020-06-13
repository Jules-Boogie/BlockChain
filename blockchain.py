
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

def get_new_amount():
    user_input = float(input("please enter transaction amount: "))
    return user_input

def get_user_choice():
    print("enter 1 to add new transaction")
    print("enter 2 to see all blocks in the blockChain")
    user_choice = input("please enter 1 or 2: ")
    return user_choice

def print_blocks():
    for block in blockChainList:
        print(block)

## using a for loop to return all the blocks
# for block in blockChainList:
#     print(block)

## using  while loop

while True:
    user_choice = get_user_choice()
    if user_choice == '1':
        add_to_blockList(get_last_amount(), get_new_amount())
        print(blockChainList)
    else:
        print_blocks()
    
    

    

