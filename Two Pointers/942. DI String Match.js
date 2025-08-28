var diStringMatch = function(s) {
    let n = s.length;
    let low = 0, high = n;
    let result = [];

    for (let ch of s) {
        if (ch === "I") {
            result.push(low);
            low++;
        } else { 
            result.push(high);
            high--;
        }
    }
    result.push(low); 
    return result;
};