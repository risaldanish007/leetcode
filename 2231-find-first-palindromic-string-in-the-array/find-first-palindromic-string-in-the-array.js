var firstPalindrome = function(words) {
    for(let i=0 ; i<words.length ; i++){
        if(words[i].split("").reverse().join() === words[i].split("").join()){
            return words[i]
        }
    }
    return ""
};