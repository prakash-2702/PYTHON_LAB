"""
Here we assumed that the index number with 1 after allocating zero for composite numbers,are strictly prime numbers.We find out the
prime numbers based on "INDEX NUMBER" 
"""

def prime_generator(c,d):
    List=[1 for i in range(0,d+1)]
    p=2
    while (p * p <= d): 
        if (List[p] == 1):  
            for i in range(p * p, d+1, p): 
                List[i] = 0
        p += 1
    prime_list=[]
    for j in range(c,d+1,1):
        if List[j]==1 and j!=0 and j!=1:
            prime_list.append(j)
    print(prime_list)
    


testcase_no=int(input("enter a number of testcases\n"))
while(testcase_no!=0):
    print("Enter the range :")
    a=int(input("enter a first number for a range\n"))
    b=int(input("enter a second number for a range\n"))
    prime_generator(a,b)
    testcase_no-=1






