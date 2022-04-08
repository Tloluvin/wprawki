# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    result = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for l in sentence:
        if l in vowel:
            result += 1
    return result


print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))
