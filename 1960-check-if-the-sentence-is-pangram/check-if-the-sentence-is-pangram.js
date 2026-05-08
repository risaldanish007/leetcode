let sentence = "thequickbrownfoxjumpsoverthelazydog"

var checkIfPangram = function(sentence) {
    const comp = "abcdefghijklmnopqrstuwvxyz"

    for(let i=0 ; i<comp.length ; i++){
        if(!sentence.includes(comp[i])){
            return false
        }
    }
    return true
};
console.log(checkIfPangram(sentence))