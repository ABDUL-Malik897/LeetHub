/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let x = BigInt("0b"+ a)
    let y = BigInt("0b"+ b)
    let z = x+y
    return z.toString(2)
};