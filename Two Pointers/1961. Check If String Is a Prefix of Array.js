var isPrefixString = function(s, words) {
    let built = "";
    for (let w of words) {
        built += w;            
        if (built === s) return true;   
        if (built.length > s.length) return false; 
    }
    return false;
};

console.log(isPrefixString("iloveleetcode",["apples","i","love","leetcode"]))