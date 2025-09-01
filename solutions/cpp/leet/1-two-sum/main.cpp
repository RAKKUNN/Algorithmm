// platform: leet
// id: 1
// title: Two Sum
// url: https://leetcode.com/problems/two-sum
// tags: array, hash-table
// date: 2025-09-02
// language: C++
// time: O(n)
// space: O(n)
// status: solved

#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> mp; // 값 → 인덱스
    for (int i = 0; i < (int)nums.size(); i++) {
        int need = target - nums[i];
        if (mp.find(need) != mp.end()) {
            return {mp[need], i};
        }
        mp[nums[i]] = i;
    }
    return {}; // 문제 조건상 절대 오지 않음
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 입력 형식: 첫 줄 = 배열 크기, 둘째 줄 = 배열 원소, 셋째 줄 = target
    int n; 
    if (!(cin >> n)) return 0;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    int target; cin >> target;

    vector<int> ans = twoSum(nums, target);
    cout << "[" << ans[0] << ", " << ans[1] << "]\n";

    return 0;
}
