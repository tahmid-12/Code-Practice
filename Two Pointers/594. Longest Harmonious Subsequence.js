var findLHS = function (nums) {
    nums.sort((a, b) => a - b);
    let s = 0;
    let m = 0;

    for (let i = 0; i < nums.length; i++) {
        while (nums[i] - nums[s] > 1) {
            s++;
        }
        if (nums[i] - nums[s] === 1) {
            m = Math.max(m, i - s + 1);
        }
    }

    return m;
};