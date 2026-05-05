// var addDigits = function(num) {
//     let res = num.toString().split("")
//     let ans = 0
//     for(let i=0 ; i<res.length ; i++){
//         ans+=Number(res[i])
//         res[i]
//     }return ans
// };

var addDigits = function(num) {
    while (num >= 10) {
        let sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        num = sum;
    }
    return num;
};