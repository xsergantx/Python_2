calls = 0 # переменная
string = 'Capybara'
list_to_search = ('Urban', ['ban', 'BaNaN', 'urBAN'])

def count_calls():# функция
    calls = 4
    print(calls)

def string_info():
    print(len(string),(string.upper()),(string.lower()))

def string_info1():
    global string
    string = "Armageddon"
    print(len(string),(string.upper()),(string.lower()))

def is_contains():
    global list_to_search
    print('Urban' in list_to_search)

def is_contains1():
    global list_to_search
    print('Apple' in list_to_search)

string_info()
string_info1()
is_contains()
is_contains1()
count_calls()
