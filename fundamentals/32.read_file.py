# with open('D:\\Python Code\\Bro Code\\text.txt') as file:
try:
    with open('text.txt') as file: # for same directory it's also works
        print(file.read())
except Exception as e:
    print(e)