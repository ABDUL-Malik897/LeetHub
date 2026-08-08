/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    let previous = [1];
    for (let i = 0; i < rowIndex; i++) {
        let row = []
        row.push(1)
        for (let j = 1; j < previous.length; j++) {
            row.push(previous[j - 1] + previous[j]);
        }
        row.push(1)
        previous = row       
    }
    return previous
};