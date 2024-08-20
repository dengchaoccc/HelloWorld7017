from collections import deque
'''
广度优先的遍历算法:
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
    def __init__(self, id:int, next_hop_number:int, next_hop_list:list[int], step:int):
        self.id = id
        self.next_hop_number = min(next_hop_number, len(next_hop_list))
        self.next_hop_list = next_hop_list
        self.step = step




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
        temp_node = Node(temp_info[0], temp_info[1], temp_info[2], 0)
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

'''
广度优先搜索：
1，遍历当前节点，当前节点进入队列。
2，处理完了当前节点以后，当前节点出队列
3，把当前节点的下一跳进入队列
'''
def wide_first_search(node_list, target_id,  visted_list, visit_queue):
    #对类已经空了，则目标找不到，直接返回
    if (len(visit_queue) == 0) :
        print("can't find the target id {}".format(target_id))
        return

    current_id = visit_queue.popleft()
    current_node = find_node(current_id)
    if (current_node == None) or (current_node.id in visted_list):
        return
    #标记已经访问过了
    visted_list.append(current_id)
    #找到目的程序终止跳出
    if (target_id == current_id):
        print("found the target id {}, step = {}".format(target_id, current_node.step))
        return

    #所有的下一跳节点进入队列
    for temp_id in current_node.next_hop_list:
        if temp_id in visted_list:
            continue
        visit_queue.append(temp_id)
        temp_node = find_node(node_list, temp_id)
        temp_node.step = current_node.step + 1
    wide_first_search(node_list,target_id,visted_list,visit_queue)



def wide_test_demo():
    visited_list = []
    visit_queue = deque([])
    node_list = init_Map()
    target_id = 8

    if (len(node_list) <= 0 ):
        return

    visit_queue.append(node_list[0].id)
    node_list[0].step = 1
    wide_first_search(node_list,target_id, visited_list, visit_queue)
