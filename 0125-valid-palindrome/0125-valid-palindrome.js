/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let left = 0
    let right = s.length - 1
    s = s.toLowerCase()
    while (left <= right) {
        while (left <= right && !/^[a-z0-9]$/.test(s[left])) {left ++}
        while (left <= right && !/^[a-z0-9]$/.test(s[right])) {right --}
        if (left > right) {
            break;
        }
        if ((s[left] !== s[right])) return false
        left ++
        right --        
    }
    return true
};