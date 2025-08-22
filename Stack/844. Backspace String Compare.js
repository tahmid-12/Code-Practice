var backspaceCompare = function(s, t) {
    function processString(s) {
        const stack = [];
        for (const ch of s) {
            if (ch === '#') {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        return stack.join('');
    }

    if(processString(s) === processString(t)){
        return true;
    }else{
        return false;
    }
};