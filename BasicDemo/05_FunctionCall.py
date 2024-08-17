
'''
验证形参的调用，是或否影响参数和结果
'''

def modify_para(id, num_list:list[int]):
    id += 1
    num_list.append(id)
    print("inside : id ={}, list = {}".format(id, num_list))

'''
传入单个单个元素，不会改变内容，但是数组会改变内部的内容
'''
def test_para_change():

    para_list = []

    for i in range(0,5):
        modify_para(i, para_list)
        print("outside : id ={}, list = {}".format(i, para_list))

test_para_change()