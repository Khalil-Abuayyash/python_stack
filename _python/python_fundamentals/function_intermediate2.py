
#### Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

### Solution ::::
x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z) 

#### Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#### Solution ::::
def iterateDictionary(sts):
    for student in students:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']} ")

iterateDictionary(students) 

#### Get Values From a List of Dictionaries
#### Solution ::::
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(f"{item[key_name]}")

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#### Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#### Solution ::::
def printInfo(some_dict):
    for key, associatedList in some_dict.items():
        print(f"{len(associatedList)} {key}")
        for item in associatedList:
            print(item)

printInfo(dojo)

