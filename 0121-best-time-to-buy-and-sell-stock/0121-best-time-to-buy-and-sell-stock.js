/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let cheapest = prices[0]
    let maxProfit = 0
    for (let i = 0; i< prices.length; i++) {
        if (prices[i+1] < cheapest) {
            cheapest = prices[i+1]
        } 
        let profitToday = prices[i +1] - cheapest
        if (profitToday > maxProfit) {
            maxProfit = profitToday
        }
    }
    return maxProfit
};