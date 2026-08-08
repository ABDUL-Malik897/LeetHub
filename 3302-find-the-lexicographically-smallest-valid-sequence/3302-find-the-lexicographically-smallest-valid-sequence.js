/**
 * @param {string} word1
 * @param {string} word2
 * @return {number[]}
 */
var validSequence = function(word1, word2) {
    let n = word1.length;
    let m = word2.length;
    let last = new Array(m).fill(-1);
    let i = n - 1;
    let j = m - 1;
    while (i >= 0 && j >= 0) {
        if (word1[i] === word2[j]) {
            last[j] = i;
            j--;
        }
        i--;
    }
    let ans = [];
    let usedMismatch = false;
    j = 0;
    for (i = 0; i < n && j < m; i++) {
        if (word1[i] === word2[j]) {
            ans.push(i);
            j++;
        }
        else if (
            !usedMismatch &&
            (j === m - 1 || i < last[j + 1])
        ) {
            ans.push(i);
            j++;
            usedMismatch = true;
        }
    }
    if (j === m) {
        return ans;
    }
    return [];
};