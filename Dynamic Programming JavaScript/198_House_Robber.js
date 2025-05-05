/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    
    n = nums.length;

    if(n === 1){
        return nums[0];
    }
    if(n === 2){
        return Math.max(nums[0], nums[1]);
    }

    let dp = Array(n).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);

    // [2,7,9,3,1]
    for(let i = 2; i < n ; i++){
        dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
    }

    return dp[n - 1];
};