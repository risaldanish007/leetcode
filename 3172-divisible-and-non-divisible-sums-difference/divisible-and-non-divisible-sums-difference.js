/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let nonDiv = 0
    let Div = 0
    for(let i=0; i<=n ; i++){
        if(i%m!==0){
            nonDiv += i
        }else{
            Div+=i
        }
    }
    return nonDiv-Div
};