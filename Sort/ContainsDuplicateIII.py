# -*- coding: utf-8 -*-
# @File    : ContainsDuplicateIII.py
# @Date    : 2020-02-18
# @Author  : tc
"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

"""
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        pass


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    t = 0

    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate(nums,k,t))