/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
    let left = 0
    let freq = new Map()
    let max = 0
    for (let right = 0; right < s.length; right++) {
        freq.set(s[right], (freq.get(s[right]) || 0) + 1);
        while (freq.get(s[right]) > 2) {
            freq.set(s[left], freq.get(s[left]) - 1)
            left++
        }
        max = Math.max(max, right - left + 1);
    }
    return max
};