inp = input().split(" ")
n , h0 , a , c , q = map(int, inp)
heights =[h0]
h_new = h0
for i in range(n-1):
    h_new = (a * h_new + c) % q
    heights.append(h_new)
high = []
count = 1


for i in range(2 , n):
    count+= 1
    high = []
    high.append(heights[i-1])
    for j in range (i - 2 , -1 , -1):
        if heights[j] > max(high):
            high.append(heights[j])
            count += 1

print(count)
            



