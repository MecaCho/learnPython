while True:
    try:
        str=raw_input()
        str=str.split()
        str.reverse()
        str1=' '.join(str)#连接单词，不可去掉
        print str1
    except:
        break