'''
用于测试字典的一些样例
'''

'''
搞个递归的样例耍耍
def add(x: int, y: int) -> int:
测试斐波那契的递归调用，现在是把临时状态都存储起来
这里有个知识点：如果是符合类型的入参，要声明类型比如 y:list[int]
入参传入的是引用，通过函数修改以后入参的值也发生了改变，这个和C语言不一样
字典可以用get函数，有可能会是空值，所以可以填写一个默认值
'''
def fibnacci(n:int, tempDict:dict[int:int]):
    tempDict[0] = 0
    tempDict[1] = 1
    tempDict[2] = 1

    #range (a,b)实际遍历的是【a,b)
    for i in range(3,n+1):
        tempDict[i] =  tempDict.get(i-1,0) +  tempDict.get(i-2,0)

'''
使用字典存储斐波那契的结果
'''
def testFib():
    dict = {}
    fibnacci(7, dict)

    #如果不指明，默认只遍历key值，或者指定values，keys，items都可以
    for key,value in dict.items():
        print("key = {}, fibb value={}", key, value)

    dict.clear()
    print("afer clear, the len of dict is {}", len(dict))





testFib()

