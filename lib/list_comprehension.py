#!/usr/bin/env python3

def return_evens(num_list):
    new_list = []
    for n in range(len(num_list)):
        if num_list[n] % 2 == 0:
             new_list.append(num_list[n])
    return new_list

print(return_evens([1,3,5,4,7,11,2,7,9,8]))

def make_exclamation(sentence_list):
    new_list = []
    for s in range(len(sentence_list)):
        a = sentence_list[s] +"!"
        new_list.append(a)
    return new_list
print(make_exclamation(['hi', 'hello']))