def hash(s, table_size):
    sum = 0
    for i in range(len(s)):
        sum = sum + ord(s[i]) * i
    return sum % table_size


print(hash("python",10))
print(hash("typhon",10))
