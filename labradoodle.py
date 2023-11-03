n, m = map(int, input().split())
dict = []
pre_dict = {}
post_dict = {}
pot = []
for i in range(n):
    word = input()
    dict.append(word)
    if word[0:3] not in pre_dict.keys():
        pre_dict [word[0:3]] = [i]
    else:
        pre_dict [word[0:3]].append(i)

    if word[-3:] not in post_dict.keys():
        post_dict [word[-3:]] = [i]
    else:
        post_dict [word[-3:]].append(i)

    

for i in range(m):
    pot.append(input())

for i in range(m):
    if pot[i][0:3] in pre_dict.keys() and pot[i][-3:] in post_dict.keys():
        if len(pre_dict[pot[i][0:3]]) != 1 or len(post_dict[pot[i][-3:]]) != 1:
            print("ambiguous")
        else:
            print(dict[pre_dict[pot[i][0:3]][0]] + " " + dict[post_dict[pot[i][-3:]][0]])
    else:
        print("none")





