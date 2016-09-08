[toc]

动态规划

和为s的两个数字
# 依次遍历第一个找到的两个数就是乘积最小的一个
# 设置两个指针，初始为第一个low和最后一个hight， low只能加， hight只能减
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:  # 数组为空返回[]
            return []
        low = 0
        hight = len(array)-1
        while low < hight:
            tmp_sum = array[low]+array[hight]
            if tmp_sum > tsum: # 当前和大于tsum，那么需要减值
                hight -= 1
            elif tmp_sum < tsum:
                low += 1
            else:
                return [array[low], array[hight]]
        return []

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 和为s的两个数字
        ret = []
        for i, num in enumerate(array):
            tmp = tsum - num
            if tmp in array[i+1:]:
                ret.append((num*tmp, num, tmp))
        if not ret:
            return ret
        tmp_ret = min(ret) #默认(num*tmp, num, tmp) num*tmp作为关键码求最小
        return tmp_ret[1:]


和为s的连续正数序列


考虑两个数ｓｍａｌｌ和ｂｉｇ分别表示当前最小值和最大值。初始设置为１，２．如果从ｓｍａｌｌ到ｂｉｇ序列的和大于ｓ，我们可以从序列中去掉较小值，否则增加ｂｉｇ值。
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:  # 验证至少2个数
            return []
        small, big = 1, 2
        middle = (1+tsum)>>1  # 最大值--终止条件
        cur_sum = small + big
        ret = []
        while small < middle:
            if cur_sum == tsum:
                ret.append(range(small, big+1))
            while cur_sum > tsum and small < middle: # 当前和大于tsum，减小small
                cur_sum -= small
                small += 1
                if cur_sum == tsum:
                    ret.append(range(small, big+1))
            big += 1
            cur_sum += big
        return ret


连续子数组和最大
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array: # 数组为空返回0
            return 0
        dp = [float('-inf')]  # 初始值负无穷
        for i,n in enumerate(array):
            if dp[i] <= 0:   # dp[i]前面最大的连续数组和，如果小于等于0，那么加上当前值只会更小，更新dp[i+1]=n
                dp.append(n)
            else:
                dp.append(dp[i]+n)  # 当前值为0，且前面连续最大和为正，说明加上当前数一定大于之前和
        return max(dp)


数组与矩阵

顺时针打印矩阵


输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每个数字
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > 2*start and cols > 2*start:
            endx = rows - 1 - start  
            endy = cols - 1 - start
            for i in range(start, endy+1):  # 左到右处理
                result.append(matrix[start][i])
            if start < endx:　　# 上到下处理
                for i in range(start+1,endx+1):
                    result.append(matrix[i][endy])
            if start < endx and start < endy:　　＃　右到左处理
                for i in range(endy-1, start-1, -1):
                    result.append(matrix[endx][i])
            if start < endx-1 and start < endy:　　＃　下到上处理
                for i in range(endx-1, start, -1):
                    result.append(matrix[i][start])
            start += 1
        return result


旋转数组的最小数字
# -*- coding:utf-8 -*-
# 所有元素都是大于0， 所以零pre=0
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray)==0:
            return 0
        pre = 0
        for num in rotateArray:
            if num < pre:
                return num
            pre = num
        return rotateArray[0] 
        #  有序，输出第一个元素


字符串

替换空格
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', '%20')


栈和队列

栈的压入、弹出序列
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        n = len(pushV)
        if not n: return False
        tmp = []
        j = 0
        for val in pushV:
            tmp.append(val)  # 依次入栈
            while j < n and tmp[-1]==popV[j]:  # tmp栈顶值等于popV[j]值 出栈
                tmp.pop()
                j += 1
        if tmp:return False
        return True


包含ｍｉｎ函数的栈


定义栈的数据结构，实现一个能够得到栈最小元素的ｍｉｎ函数
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []　# 存放数据
        self.stack_min = [] #　存放最小值
    def push(self, node):
        if not self.stack_min:
            self.stack_min.append(node)
        else:
            if self.min() <= node:
                self.stack_min.append(self.min())
            else:
                self.stack_min.append(node)
        self.stack.append(node)

        # write code here
    def pop(self):
        if not self.stack:
            return []
        else:
            self.stack_min.pop()
            return self.stack.pop()
        # write code here
    def top(self):
        if not self.stack:
            return []
        return self.stack[-1]
        # write code here
    def min(self):
        if not self.stack_min:
            return []
        else:
            return self.stack_min[-1]
        # write code here


链表

合并两个排序的链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1: # pHead1 为空返回ｐＨｅａｄ２
            return pHead2
        elif not pHead2:　＃　pHead2 为空返回pHead1
            return pHead1
        else:  # 都不为空，处理第一个元素
            if pHead1.val <= pHead2.val:
                p = pHead1
                pHead1 = pHead1.next
            else:
                p = pHead2
                pHead2 = pHead2.next
        pnode = p  
        while pHead1 and pHead2:  # 依次处理两个链表
            if pHead1.val <= pHead2.val:
                pnode.next = pHead1
                pnode = pHead1
                pHead1 = pHead1.next
            else:
                pnode.next = pHead2
                pnode = pHead2
                pHead2 = pHead2.next
        ＃处理剩余结点
        if pHead1:
            pnode.next = pHead1
        if pHead2:
            pnode.next = pHead2
        return p


反转链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    # 非递归版本
    def ReverseList(self, pHead):
        if not pHead or not pHead.next: # 空或者只有一个元素直接返回
            return pHead
        q = None
        p = pHead
        while p:
            tmp = p.next #暂存下一个结点
            p.next = q # 修改当前结点指向
            q = p # 指向返回链表的第一个元素
            p = tmp # 访问下一个
        return q
        # write code here

#　递归版本
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pnode = self.ReverseList(pHead.next) # pnode新表头
            pHead.next.next = pHead # 新表头最后一个结点指向ｐｈｅａｄ
            pHead.next = None　# ｐｈｅａｄ指向None,修改尾指针
            return pnode
        # write code here


链表中倒数第k个结点
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 设置间隔为ｋ的两个指针
class Solution:
    def FindKthToTail(self, head, k):
    # 链表k可能大于链表长度，此时返回None
        i = 0
        p = head
        while p and i<k:
            p = p.next
            i += 1

        if i==k:  # k小于等于链表长度，正常处理
            q = head
            while p:
                q = q.next
                p = p.next
            return q
        return None
        # write code here


从尾到头打印链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        tmp = deque()  #　使用队列
        while listNode:
            tmp.appendleft(listNode.val)
            listNode = listNode.next
        return tmp
        # write code here


递归和循环

矩阵覆盖


矩阵覆盖类似与斐波拉契数列
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        a = [0, 1, 2] 
        if number<3:
            return a[number]
        for i in xrange(3, number+1):
            a.append(a[i-1]+a[i-2])
        return a[number]


变态跳台阶


动手推导一下：２^(n-1) ```py

-- coding:utf-8 --

class Solution: def jumpFloorII(self, number): return 2**(number-1)
#### 跳台阶

```py
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a = [0,1,2] # 起步不一样
        if number<3:
            return a[number]
        for i in xrange(3, number+1):
            a.append(a[i-1]+a[i-2])
        return a[number]
        # write code here


斐波拉契数列
# -*- coding:utf-8 -*-
# 使用记忆体函数，保存中间值。
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

class Solution:
    @memo
    def Fibonacci(self, n):
        if n==0:
            return 0
        if n<2:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)

# 使用list缓存中间值
class Solution_2:
    def Fibonacci(self, n):
        a = [0, 1, 1]
        if n<3:
            return a[n]
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]


树

二叉树的镜像


1) 空树返回空　２）层次遍历入队，栈出队。依次交换当前结点的左右子树

递归处理，交换当前结点左右子树，递归处理左右子树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    # 非递归解
    def Mirror(self, root):
        if not root:
            return None
        node_lst = [root]
        while node_lst:
            node = node_lst.pop()　#　默认弹出最后一个
            node.left, node.right = node.right, node.left
            if node.left:
                node_lst.append(node.left)
            if node.right:
                node_lst.append(node.right)
        return root

# 递归解
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # root is None
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


树的子结构


查找与根结点值相等的结点，依次判断左右子树是否包含同样结构
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        if not pRoot2:　# pRoot2遍历完，说明包含子结构
            return True
        if not pRoot1: # pRoot1遍历完，而pRoot2不为空
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)　# 递归处理左右子结构


    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:　# 空不是子结构
            return False
        result = False
        if pRoot1.val == pRoot2.val:  #当前结点值相等，判断是否包含子结构
            result = self.DoesTree1HasTree2(pRoot1, pRoot2)　# 
        if not result: #　遍历左子树
            result = self.HasSubtree(pRoot1.left, pRoot2)　# 
        if not result:　# 遍历右子树
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result


重建二叉树：给出前序和中序
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0]) #　构造根结点
        idx = tin.index(pre[0])
        left = self.reConstructBinaryTree(pre[1:idx+1], tin[:idx]) # 递归处理左子树
        right = self.reConstructBinaryTree(pre[idx+1:], tin[idx+1:])　# 递归处理右子树
        if left:
            root.left = left
        if right:
            root.right = right
        return root
        # write code here


数值运算

求１＋２＋３＋...+n(不使用乘除for/while/if/else/switch/case)
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
           # return (pow(n,2)+n)>>1  利用公式求解
        # return n and self.Sum_Solution(n-1)+n  利用递归求解,注意终止条件
        # return sum(range(1,n+1))  内建公式求解
        return (pow(n,2)+n)>>1


调整数组顺序使奇数位于偶数前面
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        num1 = []
        num2 = []
        for num in array:
            if num&0x1==0: # 利用位运算判断奇偶
                num1.append(num)
            else:
                num2.append(num)
        return num2+num1


数值的整数次方


指数可能正也可能负
# -*- coding:utf-8 -*-

class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        exp = abs(exponent)
        result = self.Power(base, exp>>1)  # 处理exp/2的情况
        result *= result
        if (exp & 0x1 == 1): # 最后一位是1还需要* base 奇数个base的情况
            result *= base
        if exponent > 0:
            return result
        return 1/result


二进制中1的个数
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # 内建bin转换为二进制统计1的个数,注意处理正负号的情况
        if n==0:
            return 0
        if n>0:
            return bin(n).count('1')
        else:
            return bin(n&0xffffffff).count('1')
