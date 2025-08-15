var sortColors = function(nums) {

    let left = 0;
    let right = nums.length - 1;
    let i = 0;

    function swap(i,j){
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    while(i <= right){
        if(nums[i] === 0){
            swap(left,i)
            left = left + 1
        }else if(nums[i] == 2){
            swap(i,right)
            right -= 1
            i -= 1
        }
        i += 1
    }

};