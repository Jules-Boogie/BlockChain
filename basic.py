username = input("Please enter first and lastname:")
user_age = int(input("Please enter age:"))

def user_info(name,age):
    """
    Prints user's info 

        Arguments:
        :name: name of the user
        :age: age of the user

        Conditions:
        :name: string
        :age:integer
    """
    print("My name is " + name + "I am " + str(age))

user_info(username,user_age)


def print_data(data1,data2):
    """
    function to print data of any kind
    """
    print(data1,data2)
print_data("sing", " a joyful song")


def decades_lived(age):
    """
    Calculates the decades a user has lived

    Argument:
    :age: the amount of time in  years the user has been on earth

    Conditions:
        :age: INTEGER

    Returns: the floor value of the age divided by 10. 
    Examples: 20/10 returns 2.
    """
    return age // 10

print(decades_lived(user_age))
