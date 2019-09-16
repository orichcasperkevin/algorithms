import turtle

def swap(s1,s2):
    return s2 + s1

def reverse_recursive(s):
    list(s)

    if len(s) == 1:
        return s
    else:
        return swap(s[0],reverse_recursive(s[1:]))

def palindrome(s):
    if reverse_recursive(s) == s:
        return True
    else:
        return False

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(180)
        draw_spiral(my_turtle, line_len - 5)

#draw_spiral(my_turtle,200)
#my_win.exitonclick()
