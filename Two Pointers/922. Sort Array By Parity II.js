var sortArrayByParityII = function(nums) {
    let even = 0, odd = 1;

    while (even < nums.length && odd < nums.length) {
        if (nums[even] % 2 === 0) {
            even += 2; 
        } else if (nums[odd] % 2 === 1) {
            odd += 2;  
        } else {
            let temp = nums[even]
            nums[even] = nums[odd];
            nums[odd] = temp;
            even += 2;
            odd += 2;
        }
    }
    return nums;
};

console.log(sortArrayByParityII([4,2,5,7])); 