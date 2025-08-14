var reverseStr = function(s, k) {
    let arr = s.split("");

    function swap(arr, left, right) {
        while (left < right) {
            let temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    for (let i = 0; i < arr.length; i += 2 * k) {
        swap(arr, i, Math.min(i + k - 1, arr.length - 1));
    }

    return arr.join("");
};

console.log(reverseStr("abcdefg", 2));