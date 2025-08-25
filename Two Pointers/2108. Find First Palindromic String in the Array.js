var firstPalindrome = function(words) {
    const isPalindrome = (str) => {
        let left = 0, right = str.length - 1;
        while (left < right) {
            if (str[left] !== str[right]) return false;
            left++;
            right--;
        }
        return true;
    };

    for (let w of words) {
        if (isPalindrome(w)) return w;
    }
    return "";
};

console.log(firstPalindrome(["abc", "car", "ada", "racecar", "cool"])); 