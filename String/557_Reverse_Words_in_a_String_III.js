var reverseWords = function(s) {
    
    let arr = s.split(" ");
    
    for(let i=0; i < arr.length; i++){
        let wordArr = arr[i].split(""); 
        let left = 0;
        let right = wordArr.length - 1;
        while(left < right){
            let temp = wordArr[left];
            wordArr[left] = wordArr[right];
            wordArr[right] = temp;
            left++;
            right--;
        }
        arr[i] = wordArr.join("");
    }

    return arr.join(" ");
};

s = "Let's take LeetCode contest"
console.log(reverseWords(s))