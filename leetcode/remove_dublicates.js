// https://leetcode.com/problems/remove-duplicates-from-sorted-array/


var removeDuplicates = function(nums) {
    let i = 1;
    let prev = nums[0];

    while (i < nums.length){
        if (nums[i] === undefined){
            break
        }

        if (nums[i] === prev){
            for (let j = i; j < nums.length; j++){
                let next = nums[j + 1]
                nums[j] = next
            }
        } else {
            prev = nums[i]
            i++
        }
        console.log(nums)
    }

    return i;
};


const nums = [0,0,0,0,3]
console.log(removeDuplicates(nums), nums)
// console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
