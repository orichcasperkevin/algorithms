from adt import Stack

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

def symbol_checker(s):
    stack = Stack()
    for symbol in s:
        if symbol in "([{":
            stack.push(symbol)
        if symbol in ")}]":
            if stack.is_empty():
                return False
            if not matches(stack.pop(), symbol):
                return False
    if stack.is_empty():
        return True
    else:
        return False

def base(base,dec_number):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    binary_string = ""
    for i in rem_stack.reverse():
        binary_string = binary_string + digits[i]

    return binary_string

print(base(2,10))
