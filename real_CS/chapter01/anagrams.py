def anagram_quadratic(s1,s2):

    if (len(s1) != len(s2)):
        return False

    for letter in list(s1):
        s2index = 0
        match = False
        while s2index < (len(s2)-1):
            for letter_s2 in s2:
                if letter_s2 == letter:
                    match = True
                s2index += 1
            if match == False:
                return False
    return True


def anagram_linear_if_sorted(s1,s2):
    # the sorting is typically an O(n^2) or O(n log n) so it dominates the algorithm
    # otherwise the algorithm is linear

    if (len(s1) != len(s2)):
        return False

    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def anagram_linear(s1, s2):
    # 2n + 26
    counter1 = [0] * 26
    counter2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        counter1[pos] = counter1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        counter2[pos] = counter2[pos] + 1

    j = 0
    while j < 26 :
        if counter1[j] == counter2[j]:
            j = j + 1
        else:
            return False
    return True


print(anagram_linear("typhon","python"))
