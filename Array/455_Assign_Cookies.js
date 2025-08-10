var findContentChildren = function(g, s) {
    greed = g.sort((a, b) => a - b);
    cookie = s.sort((a, b) => a - b);

    let i = 0;
    let j = 0;
    let counter = 0;

    while(i < greed.length && j < cookie.length){
        if(cookie[j] >= greed[i]){
            counter++;
            i++;
            j++
        }else{
            j++;
        }
    }
    return counter
};