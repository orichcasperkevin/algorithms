from logging import logMultiprocessing
import math

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def consecutive_primes(list):
  count = 0  
  primes = []
  for el in list:
    if is_prime(el):
      primes.append(el)
      count += len(primes)
    else:
      primes = []
  return count



# list = [8, 5, 6, 3, 7]
# print(consecutive_primes(list))


def sub_array_with_sum(array,k,x_sum):
  p1=0
  p2=0
  total = array[p1]
  while p2 < len(array)-1:    
    if p2 - p1 == k - 1:
      p1 += 1
      total -= array[p1-1]
    p2 += 1
    total += array[p2]    

    if total == x_sum:
      return True
  return False

  



# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# print(sub_array_with_sum(arr,4,18))


def longest_substring_with_distinct_characters(string,k):  
  p1=0
  p2=0
  seen = {}
  longest_substring =  ""
  this_string = ""
  while p2 < len(string):   
    this_string += string[p2]
    if string[p2] not in seen:
      seen[string[p2]] = 1
    else:
      seen[string[p2]] += 1

    if len(seen) > k:   
      seen[string[p1]] = seen[string[p1]] - 1      
      if seen[string[p1]] == 0:
        del seen[string[p1]]      
      p1+=1      
      this_string = this_string[p1:]    
    p2 += 1    
    longest_substring = this_string if len(this_string) > len(longest_substring) else longest_substring
  
  return longest_substring




string = "abcbdbdbbdcdabd"
print(longest_substring_with_distinct_characters(string,3))
