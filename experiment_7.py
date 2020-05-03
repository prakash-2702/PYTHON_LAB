num=int(input("Enter the number:"))
pair=[]
if num >=0 and num<=1000:
    for i in range (1,num):
        for j in range(i+1,num):
            if (i**2) + (j**2)==num and i<=j:
                pair.append((i,j))
print('The pairs for given number are:{}'.format(pair))
