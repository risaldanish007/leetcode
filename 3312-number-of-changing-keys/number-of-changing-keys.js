var countKeyChanges = function(s) {
    let keys = 0
    let m = s.toLowerCase()
    let temp = m[0]
    
    for(let i=1 ; i<=m.length -1 ; i++){
        if(temp !== m[i]){
            keys++
        }
        temp = m[i]
    }
    return keys
};