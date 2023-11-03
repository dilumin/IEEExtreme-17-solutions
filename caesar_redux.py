def return_new_ord_en(i ,q):
    if ord(i) - q < 97:
        return ord(i) - q + 26
    else:
        return ord(i) - q
        
def return_new_ord_dec(i ,q):
    if ord(i) + q > 122:
        return ord(i) + q - 26
    else:
        return ord(i) + q

n = int(input())

for _ in range(n):
    ans = ""
    q = int(input())
    text = input()

    if " the " in text:
        for i in text:
            if i == " ":
                ans += " "
            else:
                ans += chr(return_new_ord_en(i, q))
    else:
        for i in text:
            if i == " ":
                ans += " "
            else:
                ans += chr(return_new_ord_dec(i, q))
                
    print(ans)

