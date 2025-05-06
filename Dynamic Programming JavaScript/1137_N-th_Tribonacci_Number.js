/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    let memo = {0:0, 1:1, 2:1};

    function f(n){
        if(n in memo){
            return memo[n];
        }else{
            memo[n] = f(n - 1) + f(n - 2) + f(n - 3);
            return memo[n];
        }
    }
    return f(n);
};