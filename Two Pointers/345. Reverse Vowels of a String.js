var reverseVowels = function(s) {
    
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);

    const characters = s.split('');

    let leftPointer = 0;
    let rightPointer = characters.length - 1;

    while (leftPointer < rightPointer) {
        while (leftPointer < rightPointer && !vowels.has(characters[leftPointer])) {
            leftPointer++;
        }
        while (leftPointer < rightPointer && !vowels.has(characters[rightPointer])) {
            rightPointer--;
        }

        let temp = characters[leftPointer];
        characters[leftPointer] = characters[rightPointer];
        characters[rightPointer] = temp;

        leftPointer++;
        rightPointer--;
    }
    return characters.join('');
};