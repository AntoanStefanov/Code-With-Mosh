from pprint import pprint
sentence = 'This is a common interview question'
chars_occurances = {}
for char in sentence:
    if char not in chars_occurances:
        chars_occurances[char] = 0
    chars_occurances[char] += 1
print(chars_occurances)

sorted_chars_occurances = sorted(
    chars_occurances.items(),
    key=lambda x: -x[1])

print(sorted_chars_occurances[0])
