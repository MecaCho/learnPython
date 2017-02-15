while True:
    try:
        str=raw_input()
        list1=list(str)
        list1.reverse()
        str1=''.join(list1)
        print str1
    except:
        break