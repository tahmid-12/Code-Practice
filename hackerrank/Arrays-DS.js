function reverseArray(a) {
    // Write your code here
    let left = 0;
    let right =  a.length - 1;
    
    while(left < right){
        let temp = a[left];
        a[left] = a[right];
        a[right] = temp;
        
        left++;
        right--;
    }
    return a;
}