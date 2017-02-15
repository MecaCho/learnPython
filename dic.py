while True:
    try:
        n=int(raw_input())
        list=[]
        for i in range(n):
            str=raw_input()
            list.append(str)
        list.sort()
        for x in list:
            print x
    except:
        break