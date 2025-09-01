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
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        # expect format: nums=[2,7,11,15], target=9
        # simple parsing
        ns, t = data.split("target=")
        nums = eval(ns.split("nums=")[1].strip().rstrip(","))
        target = int(t)
        print(twoSum(nums, target))
