var findDisappearedNumbers = function(nums) {
    const arrLength = nums.length;
    let initialIndex = 0;

    while (initialIndex < arrLength){
        let correctIndex = nums[initialIndex] - 1;

        if(nums[initialIndex] !== nums[correctIndex]){
            [nums[initialIndex], nums[correctIndex]] = [nums[correctIndex], nums[initialIndex]]
        }else{
            initialIndex++;
        }
    }

    let missingNums = [];
    for (let i = 0; i < arrLength; i++) {
        if (nums[i] !== i + 1) {
            missingNums.push(i + 1);
        }
    }

    return missingNums;
};