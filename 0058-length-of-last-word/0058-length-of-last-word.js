/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const stringS = s
    const clean = stringS.trim()
    const split = clean.split(' ')
    let len = split[split.length -1].length
    return len
};