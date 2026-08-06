/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
    var XYZ = function (n) {
            StrNum = String(n)
            let Mul = 1
            for (let i = 0; i< StrNum.length; i++) {
                Mul = Mul * Number(StrNum[i]) 
            }
            return Mul
        }
    let product = XYZ(n)
    while (true) {
        if (product % t === 0){
            return n
            false
        } else {
            n++
            product = XYZ(n)
        }
    }
};