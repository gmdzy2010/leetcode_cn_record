from typing import List


def main(nums: List[int]) -> int:
    """乘积最大的子数组，DP-二维

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 最大乘积
    """
    size = len(nums)
    if size == 0:
        return 0

    # * dp[i][0]/dp[i][1] 代表以 i 结尾的数字连续子序列乘积最小值/最大值
    # ! 因为有负数存在
    dp = [[0 for _ in range(2)] for _ in range(size)]

    dp[0][0] = nums[0]
    dp[0][1] = nums[0]

    for i in range(1, size):
        # * 当前数字是正数，无论前一个状态是正还是负，乘积仍然保持大或者小的单调性
        if nums[i] > 0:
            dp[i][0] = min(nums[i], dp[i - 1][0] * nums[i])
            dp[i][1] = max(nums[i], dp[i - 1][1] * nums[i])

        # * 最大的正数乘以一个负数成为最小的负数，这个最小的负数在遇到后续的负数时有可能
        # * 变成最大正数
        else:
            dp[i][0] = min(nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = max(nums[i], dp[i - 1][0] * nums[i])

    ans = max(n[1] for n in dp)

    return ans


if __name__ == "__main__":
    test_nums = [2, 3, -2, 4, 8, -9]
    print(main(test_nums))
