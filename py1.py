# file_path = 'D:\JustUseIt.txt'
file_path = 'everyday.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

string = ''
for line in lines:
    string += line.rstrip()

birthday = input("enter your birthday, in the form mmddyy:")
if birthday in string:
    print("you birthday appears in the first million digits of pi!")
    print(string.find(birthday))
else:
    print("your birthday does not appear in the first million digits of pi.")
    prnit("test github.")