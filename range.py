



>>> range(1,5) #代表从1到5(不包含5)

[1, 2, 3, 4]

>>> range(1,5,2) #代表从1到5，间隔2(不包含5)

[1, 3]

>>> range(5) #代表从0到5(不包含5)

[0, 1, 2, 3, 4] 


再看看list的操作:








array = [1, 2, 5, 3, 6, 8, 4]

#其实这里的顺序标识是

[1, 2, 5, 3, 6, 8, 4]

(0，1，2，3，4，5，6)

(-7,-6,-5,-4,-3,-2,-1)

 

>>> array[0:] #列出0以后的

[1, 2, 5, 3, 6, 8, 4]

>>> array[1:] #列出1以后的

[2, 5, 3, 6, 8, 4]

>>> array[:-1] #列出-1之前的

[1, 2, 5, 3, 6, 8]

>>> array[3:-3] #列出3到-3之间的

[3] 


 

那么两个[::]会是什么那？








>>> array[::2]

[1, 5, 6, 4]

>>> array[2::]

[5, 3, 6, 8, 4]

>>> array[::3]

[1, 3, 4]

>>> array[::4]

[1, 6] 

如果想让他们颠倒形成reverse函数的效果

>>> array[::-1]

[4, 8, 6, 3, 5, 2, 1]

>>> array[::-2]

[4, 6, 5, 1] 


感觉自己懂了吧，那么来个冒泡吧：








array = [1, 2, 5, 3, 6, 8, 4]

for i in range(len(array) - 1, 0, -1):

    print i

    for j in range(0, i):

        print j

        if array[j] > array[j + 1]:

            array[j], array[j + 1] = array[j + 1], array[j]

print array 


一行一行的来看：

line 1：array = [1, 2, 5, 3, 6, 8, 4]一个乱序的list没什么好解释的

line 2：for i in range(len(array) - 1, 0, -1):这就是上边给的例子的第二条，我们替换下就成为range(6,1,-1)，意思是从6到1间隔-1,也就是倒叙的range(2,7,1),随后把这些值循环赋给i，那么i的值将会是[6, 5, 4, 3, 2]

line 3：for j in range(0, i):这是一个循环赋值给j，j的值将会是[0, 1, 2, 3, 4, 5][0, 1, 2, 3, 4][0, 1, 2, 3][0, 1, 2][0, 1]
那么上边两个循环嵌套起来将会是

i------------6
j------------0j------------1j------------2j------------3j------------4j------------5

i------------5
j------------0j------------1j------------2j------------3j------------4
i------------4
j------------0j------------1j------------2j------------3
i------------3
j------------0j------------1j------------2
i------------2
j------------0j------------1

line 4：if array[j] > array[j + 1]:

>>> array = [1, 2, 5, 3, 6, 8, 4]
>>> array[0]
1
>>> array[1]
2
>>> array[2]
5
>>> array[3]
3
>>> array[4]
6
>>> array[5]
8
>>> array[6]
4
其实·就是使用这个把这个没有顺序的array = [1, 2, 5, 3, 6, 8, 4]排序

line 5：array[j], array[j + 1] = array[j + 1], array[j] 替换赋值

line 6：打印出来

其实要想省事儿，sort()函数一句就能搞定.......
