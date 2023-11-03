def convert(word):
    map = {}
    val = 'A'
    for i in range(len(word)):
        if word[i] == 'X':
            map[word[i]] = 'X'
        if word[i] not in map.keys():
            map[word[i]] = val
            val = chr(ord(val) + 1)
    for i in range(len(word)):
        word = word[:i] + map[word[i]] + word[i+1:]
    return word

# Read rhyming groups and construct a dictionary mapping words to rhyme labels
n, m = map(int, input().split())
rhyme_dict = {}
rhyme_word = []
for _ in range(n):
    words = input().strip().split()
    rhyme_dict[_] = words
# print(rhyme_dict)

input()

for _ in range(m):
    line = input().strip().split()
    rhyme_word.append(line[-1].lower())
# print(rhyme_word)

result = ""
for word in rhyme_word:
    for count, st in rhyme_dict.items():
        if word in st:
            result += chr(65+int(count))
            break    
    else:
        result += 'X'

number_of_char = {}
for i in range(len(result)):
    if result[i] not in number_of_char.keys():
        number_of_char[result[i]] = 1
    else:
        number_of_char[result[i]] += 1
keys_with_value_one = {key: value for key, value in number_of_char.items() if value == 1}
del number_of_char
keys_list = list(keys_with_value_one.keys())
del keys_with_value_one
for l in keys_list:
    result = result.replace(l, 'X')
del keys_list
print(convert(result))



# Read and analyze the passage to construct the rhyme scheme
# rhyme_scheme = ''
# for _ in range(m):
#     line = input().strip().split()
#     line_rhyme_labels = set(rhyme_dict.get(word.lower(), 'X') for word in line)
#     rhyme_scheme += ''.join(line_rhyme_labels)

# # Output the rhyme scheme
# print(rhyme_scheme)


