var mergeAlternately = function(word1, word2) {
    let mergedResult = '';
    let i = 0;
    let j = 0;

    while( i < word1.length && j < word2.length){
        mergedResult += word1[i];
        mergedResult += word2[j];
        i++;
        j++
    }

    while(i < word1.length){
        mergedResult += word1[i];
        i++;
    }

    while(j < word2.length){
        mergedResult += word2[j];
        j++;
    }

    return mergedResult;
};