
'''
深度优先的遍历算法:
1,递归调用
2，设置访问过的标记位
3，设置提前返回的条件

找到最短的路径，并且返回路径中的元素
这里从1到8，最短的路径应该是1-4-5-8

1-----2-----3
|          |
|        |
4------5
|      |
|        |
6---7-----8

'''

class Node:

    def __init__(self, id:int, next_hop_number:int, next_hop_list:list[int]):
        self.id = id
        self.next_hop_number = min(next_hop_number, len(next_hop_list))
        self.next_hop_list = next_hop_list




'''
把地图画出来
1-----2-----3
|          |
|       |
4------5
|      |
|        |
6---7-----8
'''
def init_Map()->list[Node]:
    node_list = []
    node_infor = {{1,2,{2,4}},
                  {2,2,{1,3}},
                  {3,2,{2,5}},
                  {4,3,{1,5,6}},
                  {5,3,{3,4,8}},
                  {6,2,{4,7}},
                  {7,2,{6,8}},
                  {8,2,{5,7}}
                  }
    for temp_info in node_infor:
        temp_node = Node(temp_info[0], temp_info[1], temp_info[2])
        node_list.append(temp_node)
    return node_list

'''
确认节点是否在列表中
'''
def find_node(node_list:list[Node], id:int)->Node:
    for temp_node in node_list:
        if temp_node.id == id:
            return temp_node
    return None


min_deep = 0xffff

'''
深度优先
'''
def deep_fist_search(node_list:list[Node], current_node:Node,target_id:int, deep:int, stack:list[int]):
    global  min_deep
    deep += 1
    # 如果不是最短路径，没有必要再寻找
    if (deep >= min_deep):
        return

    stack.append(current_node.id)
    if (current_node.id == target_id):
        min_deep = min(min_deep, deep)
        print("now find the min route, step ={}, route = {}".format(deep,stack))
        return

    for id in current_node.next_hop_list:
        temp_node = find_node(node_list, id)
        # 如果这个节点已经在栈里，就没有必要再走下去
        if (temp_node != None) and (temp_node.id not in stack):
            deep_fist_search(node_list, temp_node, target_id, deep, stack)
    # 使用完了需要退出栈
    stack.pop()

    return


def test_deep_first_search():
    node_list = init_Map()
    stack=[]

    deep_fist_search(node_list, node_list[0], 8,0,stack)
