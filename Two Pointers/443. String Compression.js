var compress = function(chars) {
    let write = 0; 
    let count = 1;   

    for (let i = 0; i < chars.length; i++) {
        if (i + 1 < chars.length && chars[i] === chars[i + 1]) {
            count++;
        } else {
            chars[write++] = chars[i];

            if (count > 1) {
                for (let digit of String(count)) {
                    chars[write++] = digit;
                }
            }

            count = 1; 
        }
    }
    return write;
};