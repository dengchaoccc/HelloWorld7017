
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，
并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

'''

"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
"""

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        array_len = len(nums)

        if (array_len < 2 ) :
            return result

        for i in range(0, array_len):
            first_number = nums[i]
            second_number = target - first_number
            #index只会返回第一个出现的位置
            sencond_index = nums.index(second_number, i + 1)
            if (sencond_index < array_len):
                result.append(i)
                result.append(sencond_index)
                return result
        return result

    '''
    第二种方法，使用哈希,顺便训练一下字典的使用方法
    '''
    def twoSum2(self, nums, target):
        result = []
        num_index_map = {} #空字典的创建方式
        array_len = len(nums)

        if (array_len < 2):
            return result
        #建立映射关系，之后使用哈希查找
        for i in range(0, array_len):
            num_index_map[nums[i]] = i

        for i in range(0, array_len):
            first_num = nums[i]
            second_num = target - first_num
            #在字典里面查找元素
            if (num_index_map.get(second_num) != None) :
                result.append(i)
                result.append(num_index_map[second_num])
                return result
        return result
#简易用例
def test1():
    nums = [1,2,3,4,5]
    case1 = Solution()
    result = case1.twoSum(nums,6)
    print(result)
test1()