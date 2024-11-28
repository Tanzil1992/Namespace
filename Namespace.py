calls = 0
check_ = False
tuple_ = ""
def count_calls(b):
    global calls
    calls = calls + 1
    return calls

def string_info(string):
    global tuple_
    tuple_ = ""
    tuple_ = len(string), string.upper(), string.lower()
    count_calls(calls)
    return tuple_

def is_contains(string, list_to_search):
    global check_
    check_ = False
    for i in range(len(list_to_search)):
        string_1 = list_to_search[i].upper()
        string_ = string.upper()
        if string_ == string_1:
            check_ = True
            break
    count_calls(calls)
    return check_
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
