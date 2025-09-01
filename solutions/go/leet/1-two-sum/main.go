// platform: leet
// id: 1
// title: Two Sum
// url: https://leetcode.com/problems/two-sum
// tags: array, hash-table
// date: 2025-09-02
// language: Go
// time: O(n)
// space: O(n)
// status: solved

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func twoSum(nums []int, target int) []int {
	mp := make(map[int]int) // 값 -> 인덱스
	for i, v := range nums {
		need := target - v
		if j, ok := mp[need]; ok {
			return []int{j, i}
		}
		mp[v] = i
	}
	return []int{} // 문제 조건상 항상 해답 존재
}

func mustAtoi(s string) int {
	x, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)

	// 1) n
	line1, _ := in.ReadString('\n')
	line1 = strings.TrimSpace(line1)
	if line1 == "" {
		return
	}
	n := mustAtoi(line1)

	// 2) nums (n개)
	line2, _ := in.ReadString('\n')
	line2 = strings.TrimSpace(line2)
	fields := strings.Fields(line2)
	nums := make([]int, n)
	for i := 0; i < n && i < len(fields); i++ {
		nums[i] = mustAtoi(fields[i])
	}

	// 3) target
	line3, _ := in.ReadString('\n')
	line3 = strings.TrimSpace(line3)
	target := mustAtoi(line3)

	ans := twoSum(nums, target)
	// 출력 포맷: [i, j]
	fmt.Printf("[%d, %d]\n", ans[0], ans[1])
}
