const nums = [2, 3, 5, 6]


const callback = (sum, v, i, array) => {
    return sum + v
}

// const result = nums.reduce((sum, v, i, nums) => sum + v, {})

let result = 0
for (const v of nums){
    result = callback(result, v, 0, nums)
}

console.log(result)
