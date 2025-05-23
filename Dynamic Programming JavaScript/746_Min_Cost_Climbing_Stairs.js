/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {

    let n = cost.length;

    let dp = Array(n+1).fill(0);

    for(let i=2;i<=n;i++){
        dp[i] = Math.min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
    }  
    return dp[n]
};