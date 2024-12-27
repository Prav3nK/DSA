/* Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).  */



const input = [-2, 0, 3, -5, 2, -1]
const output = [] ;
var min_range = 1 ;
var max_range = 4;


function rangeSum(min_range, max_range, input){
    var p = 0
    for (let i = 0; i < input.length ; i ++ ){
        p = p + input[i]
        output.push(p)
     
    }
     let sum = 0
    for (let i = min_range ;  i <= max_range ; i ++ ) {
        
        sum = sum = output[i];
    }
    console.log(sum)
   
}
rangeSum( min_range, max_range, input)

/// in the above solution the nums is the class with different number of objects with different range.. 
// so the array must be made like class and the different objects will use the functions
