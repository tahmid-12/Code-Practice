var findRadius = function(houses, heaters) {
    houses.sort((a,b) => a-b);
    heaters.sort((a,b) => a-b);

    let radius = 0;
    let j = 0;

    for (let i = 0; i < houses.length; i++) {
        while (j < heaters.length - 1 && 
               Math.abs(heaters[j+1] - houses[i]) <= Math.abs(heaters[j] - houses[i])) {
            j++;
        }
        radius = Math.max(radius, Math.abs(heaters[j] - houses[i]));
    }
    return radius;
};