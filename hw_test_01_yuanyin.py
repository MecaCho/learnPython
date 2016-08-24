while True:
    try:
        str1=str(raw_input())
        str2=''
        n=len(str1)
        num=0
        sum=n-str1.count(' ')
        for i in str1:
        	if i in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']: 
                str2+=i
            	num += 1  
        other=sum-num
        str3=' '
        for x in range(len(str2)):
        	if x not in str3:
                str3+=x
        print len(str3)+' '+num+' '+other
        print str2
    except:
        break