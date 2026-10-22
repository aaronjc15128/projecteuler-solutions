count = 0


array = []
for m in range(1000):
    n=m+1

    if n in {11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000}:
        array.append(n)
    elif int(str(n)[-2:]) in {11, 12, 13, 14, 15, 16, 17, 18, 19} and len(str(n)) == 3:
        array.append(int(str(n)[:1])*100)
        array.append(int(str(n)[-2:]))
    else:
        i = len(str(n))
        for d in str(n):
            if d == '0':
                i-=1
                continue
            else:
                array.append(int(d)*(10**(i-1)))
                i-=1
            

conversion = {
    1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 
    10:3, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
    11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8
}

for a in array:
    if a == 1000: count += 11
    elif a in {100, 200, 300, 400, 500, 600, 700, 800, 900}:
        count += conversion[int(str(a)[:1])] + 10
    else: count += conversion[a]

count -= 9*3

print(count)