### Exercise #1 <br>
# Reverse the list below in -place using an in -place algorithm. For extra credit: Reverse the strings at the same time.



from operator import le


words = ['this', 'is', 'a', 'sentence', '.']

def reverse(a_list):
    
    a_list[0], a_list[1], a_list[2], a_list[3], a_list[4] = a_list[4], a_list[3], a_list[2], a_list[1], a_list[0]
    
    for each in a_list:
        list_of_each = list(each)
        left = 0
        right = len(each) - 1
        while left < right:
            list_of_each[left], list_of_each[right] = list_of_each[right], list_of_each[left]
            left += 1
            right -= 1
        print(list_of_each)
        reversed_list_of_each = ''.join(list_of_each)
        print(reversed_list_of_each)
        a_list[a_list.index(each)] = reversed_list_of_each


    print(a_list)
    return a_list

reverse(words)





### Exercise #2 <br>
# <p>Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.<br>Should output:<br>{'a': 5,<br>
#  'abstract': 1,<br>
#  'an': 3,<br>
#  'array': 2, ... etc...</p>

# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


# def count_words(str):
#     list_of_words = a_text.split(' ')
#     print(list_of_words)
#     num_words = len(a_text.split(' '))
#     print(num_words)
#     text_dic = {}
#     for each in list_of_words:
#         each = each.lower()
#         if each not in text_dic:
#             text_dic[each] = 1
#         else:
#             text_dic[each] += 1
#     print(text_dic)
#     return text_dic

# count_words(a_text)

  ## Exercise#3                                                                   # Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.                                                                               #### Hint: Linear Searching will require searching a list for a given number.


# a_list = [4, 8, 2, 6, 1, 9, 23]

# def search(arr, val):
#     for each in arr:
#         if each == val:
#             print(arr.index(each))
#             return arr.index(each)

# search(a_list, 1)


