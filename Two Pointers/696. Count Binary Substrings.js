var countBinarySubstrings = function(s) {
    let prev = 0, curr = 1, result = 0;

    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i-1]) {
            curr++;
        } else {
            result += Math.min(prev, curr);
            prev = curr;
            curr = 1;
        }
    }
    result += Math.min(prev, curr);

    return result;
};