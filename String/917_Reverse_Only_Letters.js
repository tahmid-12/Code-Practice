var reverseOnlyLetters = function(s) {
    function isLetter(char) {
        let code = char.charCodeAt(0);
        return (code >= 65 && code <= 90) || (code >= 97 && code <= 122);
    }

    let arr = s.split("");
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        if (isLetter(arr[left]) && isLetter(arr[right])) {
            let temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        } else if (!isLetter(arr[left])) {
            left++;
        } else if (!isLetter(arr[right])) {
            right--;
        }
    }

    return arr.join("");
};