#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 11:51
# @Author  : tc
# @File    : TallestBillboard.py
"""
题号:956  最高的广告牌

你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。

返回广告牌的最大可能安装高度。如果没法安装广告牌，请返回 0。

 

示例 1：

输入：[1,2,3,6]
输出：6
解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
示例 2：

输入：[1,2,3,4,5,6]
输出：10
解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
示例 3：

输入：[1,2]
输出：0
解释：没法安装广告牌，所以返回 0。
 

提示：

0 <= rods.length <= 20
1 <= rods[i] <= 1000
钢筋的长度总和最多为 5000
"""
from typing import List
from functools import lru_cache

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            return max(dp(i + 1, s),
                       dp(i + 1, s - rods[i]),
                       dp(i + 1, s + rods[i]) + rods[i])

        return dp(0, 0)

if __name__ == '__main__':
    rods = [1,2,3,4,5,6]

    solution = Solution()

    print(solution.tallestBillboard(rods))
