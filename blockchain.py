
blockChainList = []

def get_last_amount():
    """
    Retrieves the last value entered into the BlockChainList
    

    Arguments:
        :None
    """
    if len(blockChainList) == 0:
        return None
    return blockChainList[-1]


def add_to_blockList(current_amount, last_amount):
    """
    Adds a last value in the blockchain and a new value to the blockchainList


    Arguments:
        :current_amount: the last value in the blockChainList
        :last_amount: the new value to be added to the blockChainlist
    """

    if current_amount == None:
        current_amount = [1]
    blockChainList.append([current_amount,last_amount])
    
add_to_blockList(get_last_amount(), 3)

# get user input

def get_new_amount():
    user_input = int(input("please enter transaction amount: "))
    return user_input

def get_user_choice():
    print("enter 1 to add new transaction")
    print("enter 2 to see all blocks in the blockChain")
    print("enter hack to manipulate a past transaction")
    print("please type in quit to quit program")
    user_choice = input("please enter 1 or 2 or hack or quit: ")
    return user_choice

def print_blocks():
    for block in blockChainList:
        print(block)


#verify our chain by checking if the first element of a given block matches the elements of the previous block. 

def validate_blockChain():
 
    is_valid = True
    for current_block_index in range(len(blockChainList)):

        #the range function can take in 1 to 3 arguments 
        #argument 1: is the start of the loop
        # argument 2: is the end of the loop
        # argument 3: is the step of the loop
        # eg for i in range(5,11,2)
        #         print (i)
        # 5,7,9,11
        if current_block_index == 0:
            continue
        if blockChainList[current_block_index][0] == blockChainList[current_block_index - 1]:
            is_valid = True
        elif blockChainList[current_block_index][0] != blockChainList[current_block_index - 1] :
            is_valid = False
            break
        
    return is_valid
    


## using a for loop to return all the blocks
# for block in blockChainList:
#     print(block)

## using  while loop
# set a variable to true so that you can end the program without break

getting_input = True
while getting_input:
    user_choice = get_user_choice()
    if user_choice == '1':
        add_to_blockList(get_last_amount(), get_new_amount())
        print(blockChainList)
    elif user_choice =='2':
        print_blocks()
    elif user_choice == 'hack':
        if len(blockChainList) > 0:
            blockChainList[0] = 5
    elif user_choice == 'quit':
        getting_input = False
    else:
        print("Invalid choice, please choose 1 or 2")
        get_user_choice()
    if not validate_blockChain():
        print("not a valid chain")
        break
    
    
#use and and or to join conditionals    
# use parenthesis to group 



