n=[2,1,3,5,4,7,6,8,9,10,5,14,12,13,17,16,18,20,19,22,23,21,25,24]
for c in n:
    if c==20:
        break
    if c%2==1:
        continue
    print(c)
