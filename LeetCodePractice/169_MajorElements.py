'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：nums = [3,2,3]
输出：3
示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

"""
:type nums: List[int]
:rtype: int
知识点：dict字典的应用
"""
def majorityElement( nums):
    INVALID = 0
    num_couner = {}

    for i in nums:
        if num_couner.get(i, INVALID) == INVALID:
            num_couner[i] = 1
        else:
            num_couner[i] += 1

    max_key = INVALID
    max_value = INVALID

    # 找到最大值value，然后找到对应的key
    for key, value in num_couner.items():
        if (value > max_value):
            max_value = value
            max_key = key
    return max_key

def testMajorElement():
    nums = [2,2,1,1,1,2,2]
    result = majorityElement(nums)
    print("arrayLen = {}, element = ", len(nums), result)

testMajorElement()