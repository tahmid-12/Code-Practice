var reversePrefix = function(word, ch) {
    let idx = word.indexOf(ch);
    if (idx === -1) return word;

    let arr = word.split("");
    let left = 0, right = idx;
    while (left < right) {
        let temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left++;
        right--;
    }
    return arr.join("");
};