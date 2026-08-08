/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let result = [];
    for (let i = 0; i < numRows; i++) {
        let row = [];
        row.push(1);
        if (i > 0) {
            let previous = result[i - 1];
            for (let j = 1; j < previous.length; j++) {
                row.push(previous[j - 1] + previous[j]);
            }
            row.push(1);
        }
        result.push(row);
    }
    return result;
};