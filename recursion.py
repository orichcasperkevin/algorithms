#given a list of words, how many times does e appear


#normal
from itertools import count


paragraph = "Since 2 is more than 1, we move it down one more level again. So far you’ve seen what the divide and conquer technique is. You should understand how it works and what code looks like. Next, let’s learn how to define an algorithm to a problem using divide and conquer. This part is the most important. Once you know this, it’ll be easier to create divide and conquer algorithms."
list_of_words = paragraph.split(" ")


def get_number_of_es(list):
    count = 0
    for item in list:              
        count += item.count("e")
    return count
        

def get_number_of_es_recusively(list):    
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0].count("e")
    
    middle = len(list) // 2
    left_count = get_number_of_es_recusively(list[:middle])
    right_count = get_number_of_es_recusively(list[middle:])    

    return left_count + right_count


# print(get_number_of_es(list_of_words))
# print(get_number_of_es_recusively(list_of_words))

#get all valid n pairs of parentheses 
def generate_valid_parentheses(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return

        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

# Test the function
n = 3
valid_parentheses = generate_valid_parentheses(n)
print(valid_parentheses)
