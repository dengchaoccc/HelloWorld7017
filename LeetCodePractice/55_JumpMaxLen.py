'''
你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''

"""
:type nums: List[int]
:rtype: bool
使用贪心算法，假设当前的位置是x， 那么[x,x+nums[x]]都是可以达到的
每次都更新最大可以到达的距离，如果最大距离是最后的值，就是可以到达
"""


def canJump(nums):
    max_distance = 0
    for i in range(0, len(nums)):
        if i <= max_distance:
            max_distance = max(max_distance, i + nums[i])
            if max_distance >= len(nums) - 1:
                return True

    return False


def test_jump_max_distance():
    nums = [2, 3, 1, 1, 4]
    result = canJump(nums)
    print(f"nums={nums}, result = {result}")


test_jump_max_distance()
