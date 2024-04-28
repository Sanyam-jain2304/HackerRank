# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phoneBook = dict()
for i in range(n):
    details = input().split()
    phoneBook[details[0]] = details[1]
for i in range(n):
    try:
        name = str(input())
        if phoneBook.get(name):
            print(name +"="+ phoneBook[name])
        else:
            print("Not found")
    except:
        break
