while True:
    try:
        n=int(raw_input())
        list=['0','4','7']
        #print list[1]+'9999'
        for x in range(2,11):
            zh=int(pow(2,x)-1)
            q=int(pow(2,x-1)-1)
            #print zh,q
            j=zh
            #print j
            while q<zh:
                list.append(list[q]+'4')
                j+=1
                #print list
                list.append(list[q]+'7')
                j+=1
                q+=1
                #print j,q
        print list[n]
    except:
        break