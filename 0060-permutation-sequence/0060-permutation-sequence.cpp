class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> nums;
        vector<int> fact(n + 1, 1);

        for (int i = 1; i <= n; i++) {
            nums.push_back(i);
            fact[i] = fact[i - 1] * i;
        }

        k--;

        string result;

        for (int i = n; i >= 1; i--) {
            int index = k / fact[i - 1];
            k %= fact[i - 1];

            result += to_string(nums[index]);
            nums.erase(nums.begin() + index);
        }

        return result;
    }
};