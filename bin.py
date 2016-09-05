while True:
    try:
        n=int(raw_input())
        num=bin(n)
        str1=str(num)
        sum=0
        len1=len(str1)
        for i in range(2,len1):
            if str1[i]=='1':
                sum+=1
        print sum
    except:
        break