x = [[5, 2, 3], [15, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Andres', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 30}]

def interateDictionary(some_list):
    for i in some_list:
        if i:
            sorted_keys = sorted(list(i.keys())-1)
            pairs = [f"{k} - {i[k]}" for k in sorted_keys]
            s = ", ".join(pairs)
            print(s)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i.get(key_name))
print(iterateDictionary2('first_name', students))
print( iterateDictionary2('last_name', students))

def printInfo(some_dictionary):
    for key, values in some_dictionary.items():
        print(f"{len(values)} {key.upper()}")
        for i in values:
            print(i)
        print()
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


