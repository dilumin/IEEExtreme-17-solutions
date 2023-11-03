n = int(input())
for _ in range(n):
    sentence = input()
    words = {}
    for i in sentence:
        if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g':
            if i not in words.keys():
                words[i] = 1
            else:
                words[i] += 1
        else:
            continue
    max_key = max(words, key=words.get)
    print(max_key.upper())

        