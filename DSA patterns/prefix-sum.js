// Prefix sum //
// create a new array with previous sum //

// if arr = [1,2,3,4,5,6] //
// then output = [1,3,6,10,15,21]

////////*******************************///////////////

/// IN THIS QUESTIUON WE SHOULD MAKE THE ANOTHER ARRAY AND PUSH THE ADDED NEW SUM OF THE ELEMENT INTO THIS ARRAY.//// 

////////*******************************///////////////


var arr = [1,2,3,4,5,6];
var p = [];

for (let i = 0 ; i < arr.length ; i++ ){
    var count = 0 ;
    if ( i <= 0){
        count = arr[i];
    }
    else {
        count = arr[i] + p[i-1]
    }
    p.push(count)
}

for (let i = 0; i <p.length; i ++){
    console.log(p[i])
}