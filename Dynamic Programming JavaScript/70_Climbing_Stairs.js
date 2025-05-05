/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let memo = {1:1, 2:2};

    function f(n){
        if(n in memo){
            return memo[n];
        }
        else{
            memo[n] = f(n-2) + f(n - 1);
            return memo[n];
        }
    }
    return f(n);
};