def run():
    my_list= [1, "hi", True, 4.5]
    my_dic={'firstname': 'john', 'lastname': 'smith'}


    ##nesting: dic in list
    super_list=[
        {'firstname': 'John', 'lastname': 'Smith'},
        {'firstname': 'Bob', 'lastname': 'Smith'},
        {'firstname': 'Mary', 'lastname': 'Smith'},
        {'firstname': 'Sue', 'lastname': 'Smith'},
        {'firstname': 'Joe', 'lastname': 'Smith'},
        {'firstname': 'Sally', 'lastname': 'Smith'},
        {'firstname': 'Sue', 'lastname': 'Smith'},
    ]
    ##nesting: list in dic
    super_dic={
        'natural_nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'integers': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        'floats': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    }
    for i in super_list:
        print(i['firstname'], i['lastname'])



if __name__ == "__main__":
    run()