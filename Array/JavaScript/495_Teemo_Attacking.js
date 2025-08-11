var findPoisonedDuration = function(timeSeries, duration) {
    let total = 0;
    for(let i = 0; i < timeSeries.length - 1; i++){
        let gap = timeSeries[i + 1] - timeSeries[i];
        total += Math.min(gap, duration);
    }
    if(timeSeries.length > 0){
        total += duration;
    }
    return total
};