let sentences = ["alice and bob love leetcode"]

var mostWordsFound = function(sentences) {
    let max = 0

    for(let words of sentences){
        let count = words.split(" ").length

        if(count>max){
            max = count
        }
    }
    
    return max
};

console.log(mostWordsFound(sentences))