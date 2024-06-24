// Let's say that "g" is happy in the given string, if there is another "g" immediately to the right or to the left of it.

// Find out if all "g"s in the given string are happy.

// Example
// For str = "gg0gg3gg0gg", the output should be true.

// For str = "gog", the output should be false.

// Input/Output
// [input] string str
// A random string of lower case letters, numbers and spaces.

// [output] a boolean value
// true if all "g"s are happy, false otherwise.

const gHappy = (str) => {
  // it seems like if there are no 'g's present than the string is 
  // not unhappy? not really clear in the directions
  if (!str.includes("g")){
    return true
  }
  // I'll need access to the index of the string
  for(let idx = 0; idx < str.length; idx++){
    // once a g is found I need to check both the left and right side
    // at first I thought this could be fixed with a stack 
    // but it seems like pairs of 3's are acceptable
    if (str[idx] === "g" && !(str[idx+1] === "g" || str[idx-1] === "g")){
      return false
    }
  }
  // if I check the entire string without returning false than by default
  // I should return True
  return true
}

module.exports = gHappy