var isHappy = function(n) {
    function getNext(num) {
        let sum = 0;
        while (num > 0) {
            let digit = num % 10;
            sum += digit * digit;
            num = Math.floor(num / 10);
        }
        return sum;
    }

    let slow = n;
    let fast = getNext(n);

    while (fast !== 1 && slow !== fast) {
        slow = getNext(slow);          
        fast = getNext(getNext(fast)); 
    }

    return fast === 1;
};

console.log(isHappy(19)); 
// console.log(isHappy(2));