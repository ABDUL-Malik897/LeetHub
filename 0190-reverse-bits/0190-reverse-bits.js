/**
 * @param {number} n
 * @return {number}
 */
var reverseBits = function(n) {
    let nBit = n.toString(2).padStart(32, "0")
    let arr = nBit.split('')
    let reverse = arr.reverse()
    let result = 0;
    function pack32Bits(r) {
    for (let i = 0; i < 32; i++) {
        result = (result << 1) | Number(r[i]);
    }
    return result >>> 0;
    }
    return pack32Bits(reverse)
};