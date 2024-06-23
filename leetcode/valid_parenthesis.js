// 678. Valid Parenthesis String
// Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

// The following rules define a valid string:

//    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
//    Any right parenthesis ')' must have a corresponding left parenthesis '('.
//    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
//    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

// https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2024-04-07


/**
 * @param {string} s
 * @return {boolean}

"(()())"
"()()()()"

Useful test cases
"*"
"(**(*()**()**((**(*)"
"((*)(*))()*(*)****((*(*)())*()((()**(**)"
")(*()(**(*)())*))())())*)()()*(((*)()))(**()*)**(*"
")))(*)**)))*)))))*)*(((()(((*())(***)**(**((()))()((*((()((("
"()))))**)(()*()**)))()*)()())*(*)())**()*)))(**())))()**))*)*()**((*(*"
"*(*)(*))((*)*)))(*)())*())()(()*)*)****)())(()()*(*(*())()((())))*()****)(*(()))((*()*(**(*()*)*()"


"((**)"

 */
var checkValidString = function (s) {
  let openBrackets = [];
  let openStars = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      openBrackets.push(i);
    } else if (s[i] === '*') {
      openStars.push(i);
    } else {
      if (openBrackets.length) {
        openBrackets.pop();
      } else if (openStars.length) {
        openStars.pop();
      } else {
        return false;
      }
    }
  }

  for (let i = openBrackets.length - 1; i >= 0; i--) {
    if (!openStars.length || openStars.pop() < openBrackets.pop()) {
      return false;
    }
  }

  return true;
};


// checkValidString("(**))")
console.log(checkValidString("**(()"))


const sorted = nums.map((v, i) => [i, v]).sorted((item) => item[1])

function compareFn(a, b) {
  if (a[1] < b[1]) {
    return -1;
  } else if (a[1] < b[1]) {
    return 1;
  }
  // a must be equal to b
  return 0;
}
