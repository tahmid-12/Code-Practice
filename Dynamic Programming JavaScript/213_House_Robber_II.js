/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const n = nums.length;

    if (n === 1) return nums[0];
    if (n === 2) return Math.max(nums[0], nums[1]);

    function robRange(l, r) {
        let dp1 = 0, dp2 = 0;

        for (let i = l; i <= r; i++) {
            let temp = dp1;
            dp1 = Math.max(dp1, dp2 + nums[i]);
            dp2 = temp;
        }

        return dp1;
    }

    return Math.max(robRange(0, n - 2), robRange(1, n - 1));
};