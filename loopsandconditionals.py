
#print names with length more than 5 with letter n
names_list = ['Justina','Reigner','Boma', 'Sarah', 'Joanna', 'Laila']
for i in range(len(names_list)):
    name_length = len(names_list[i])
    name = names_list[i]
    if name_length >= 5 and 'n' in name: 
        print(name)
       

is_list = True
while is_list:
    for i in range(len(names_list)):
        print('deleting')
        names_list.pop()
        print(len(names_list))
    else:
        is_list = False
        print('empty')

