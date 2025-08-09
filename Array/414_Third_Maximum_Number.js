var thirdMax = function(nums) {
    const uniqueSorted = [...new Set(nums.sort((a,b) => b -   a))];
    return uniqueSorted.length >= 3 ? uniqueSorted[2] : uniqueSorted[0];                                 
};