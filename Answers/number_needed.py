from collections import Counter


def counter(string):
    counter_dict = {}
    for c in string:
        if c not in counter_dict:
            counter_dict[c] = 1
        else:
            counter_dict[c] += 1
    return counter_dict


def number_needed(a, b):
    a_dict = counter(a)
    b_dict = counter(b)
    match = 0
    for letter in a_dict.keys():
        if letter in b_dict:
            if b_dict[letter] == a_dict[letter]:
                match += b_dict[letter]
            else:
                match += min(b_dict[letter], a_dict[letter])
    a_remove = len(a) - match
    b_remove = len(b) - match
    return a_remove + b_remove


# An Optimized Solution I found after solving myself
def number_needed_2(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

##########
# Test
#########
string1 = "a"
string2 = "a"

print "String 1: ", string1
print "String 2: ", string2
print "Number of character removals needed for anagrams: ", number_needed(string1, string2)

string1 = "abc"
string2 = "abd"

print "String 1: ", string1
print "String 2: ", string2
print "Number of character removals needed for anagrams: ", number_needed(string1, string2)

string1 = ""
string2 = "abc"

print "String 1: ", string1
print "String 2: ", string2
print "Number of character removals needed for anagrams: ", number_needed(string1, string2)

string1 = "aaaaaaa"
string2 = "aaaaa"

print "String 1: ", string1
print "String 2: ", string2
print "Number of character removals needed for anagrams: ", number_needed(string1, string2)

string1 = "xxxxxyyyyyzzzzaaaaa"
string2 = "abcxxxzzz"

print "String 1: ", string1
print "String 2: ", string2
print "Number of character removals needed for anagrams: ", number_needed(string1, string2)

