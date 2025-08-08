var findMaxAverage = function(nums, k) {
    const n = nums.length;
    if (n < k) {
        return -1;
    }

    let windowSum = 0;
    for (let i = 0; i < k; i++) {
        windowSum += nums[i];
    }

    let maxSum = windowSum;

    for (let i = k; i < n; i++) {
        windowSum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }

    return maxSum/k;
};