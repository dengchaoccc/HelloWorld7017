
#这是一个注释，用#号开始
'''
这是成片的注释
'''
import math
import time
from collections import deque


def time_test():
    print(time.strftime("%Y-%m-%d %H:%M:%s", time.localtime()))

def print_data_type():
    x = 11
    y = '2.44'
    z = 3.1334
    zz = 3.1336

    print("x+z = {}".format(x+z))
    print("x^z = {}".format(x**z))
    a = int(z) #强制类型转换
    print("after convert to in, z = {}".format(a))
    print(type(a))
    print(type(x))
    print(type(y))
    #判断两个数字是否相等，浮点数不能直接用=号
    print(math.isclose(z,zz))

def print_range():
    x = range(0,6) #从0开始，到了5结束
    print((x))
    for i in x:
        print(i)
'''
假设姓名存在数组的第一个位置，直接用第一个元素
'''
def compare_student_with_name(single_student):
    return single_student[0]

'''
list. sort 会自动进行排序
backup = sorted(list) 会建立一个副本，本体不做变更
'''
def test_sort_list():
    students = [("lily", 156,88), ("Jack", 156, 88), ("Tom", 167,8872), ("Lee",132, 89), ("Ray", 178,67) ]
    #按照姓名逆序排序
    students.sort(key = lambda  inputList:inputList[0], reverse=True)
    print(students)

    #按照身高从小到大排序
    students.sort(key= lambda  inputList:inputList[1])
    print(students)

    #使用姓名作为关键字排序,用函数做入参调用
    students.sort(key = compare_student_with_name)
    print(students)

    #先按照身高倒序，再按照分数正序,可以设置多个参数
    students.sort(key = lambda x:(-x[1], x[2]))
    print(students)

    if students:
        print("list is not empty")
    else:
        print("list not empty")

def list_test1():
    list1 = ["Jack", "Mike", "lUCY", "Jane","Tom", "jerry"]
    print(list1)

    #模拟队列，剔除第一个元素
    final_element = list1.pop()
    print(final_element)
    print(list1)

    list1.remove("LUCY")
    print(list1)

    del list1[2]
    print(list1)

def dic_test():
    dic1 = {"one":1, "two":2, "thee":3}
    dic2 = {"tom": 1, "jerry": 2, "mark": 3}

    print(dic1["one"])
    print(dic1[2]) #输出key为2的值
    print(dic1.keys())
    print(dic1.values())

    #通过key值找到对应值，没有就是空
    result = dic2.get(1)
    print("find key = 1 value = {}".format(result))

    #字典的便利
    for k,v in dic1:
        print("key ={}, value = {}".format(k,v))

    for k in dic1.keys():
        print(k)

#基本上用不上
def set_test():
    set1 = ["a", "bb", "b", "cxb"]
    set1.sort(reverse=True)
    print(set1)

    a = {1,2,3,4,5}
    b = {4,5,56,6,7}

    c = a.union(b)
    print(c) #取并集

    d = a.intersection(b)
    print(d)

#一种缩写
def get_max(a,b):
    return a if (a>b) else b


def range_test():

    for i in range(3):
        print(i)
    for i in  range(1,4):
        print(i)
    for i in range(1,20,4):
        print(i)

#lambda 推导式测试
def lambda_test():
    list1 = [i*2  for i in range(0,3)]
    name  = ["google", "soft","oracle"]
    dic1 = {key:len(key) for key in name}
    tuple1 = (i*3 for i in range(0,10,3))
    print(name)
    print(dic1)
    print(tuple1)


'''
定义一个函数的输入和输出类型为 int
'''
def function_input_type(nums:list[int], target:int)->list[int]:
    array_len = len(nums)
    result = []

    for i in range(0, array_len-1):
        result.append(nums[i])
    return result

def list_as_stack():
    my_stack = [1,23,45,5,6]

    my_stack.append(34)
    my_stack.append(90)

    print(my_stack)

    #从最开始出栈
    top = my_stack.pop()
    print(top)
    print(my_stack)

#用列表做双向队列
def list_as_queue():
    my_queue = deque( [1,4,6,3,11])
    print(my_queue)

    #队尾插入元素
    my_queue.append(12)
    my_queue.append(44)
    my_queue.append(7)

    #队头出队
    my_queue.popleft()
    print(my_queue)
    #队尾先出
    my_queue.pop()
    print(my_queue)

#二维数组的排序
def matrix_sort():
    matrix1 = [
        [x for x in range(1,5)],
        [x for x in range(11, 15)],
        [x for x in range(3, 7)],
    ]
    print(matrix1)

    #按照第二个元素的大小排序
    matrix1.sort(key = lambda array:array[1])
    print(matrix1)

    #初始化为4行3列，但是这种初始化不要用，会附带修改内存
    matrix2 =  [0*3]*4
    matrix2[1][1] = 12
    print(matrix2)

    #通过不带*号的就没有问题
    matrix3 = [
        [i for i in range(0,3)] for j in range(2,6)
    ]
    print(matrix3)





