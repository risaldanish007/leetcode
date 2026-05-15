var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let emps = 0
    for(let i=0 ; i<hours.length ; i++){
        if(target<=hours[i]){
            emps++
        }
    }
    return emps
};