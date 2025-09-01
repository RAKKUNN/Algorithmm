# platform: leet
# id: 1
# title: Two Sum
# url: https://leetcode.com/problems/two-sum
# tags: array, hash-table
# date: 2025-09-02
# language: Python
# time: O(n)
# space: O(n)
# status: solved

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

if __name__ == "__main__":
    import sys, json, re
    data = sys.stdin.read().strip()
    m = re.search(r"nums\s*=\s*(\[.*\])\s*,\s*target\s*=\s*(-?\d+)", data)
    if m:
        nums = eval(m.group(1))   # 문자열 → 리스트
        target = int(m.group(2))
        print(twoSum(nums, target))
