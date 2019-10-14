/**
 * Hacktoberithms - Multiple Cash Registers
 * https://github.com/the-vampiire/hacktoberithms/issues/68
 * By sylvain1811, 7 oct 2019
 * node version v12.9.1
 */

const assert = require('assert')

function checkout_time(customers, n_cashier) {
    let cashiers = Array(n_cashier).fill(0)
    customers.forEach(customer => {
        const minIndex = cashiers.reduce((accIdx, current, index) => {
            return current < cashiers[accIdx] ? index : accIdx
        }, 0)
        cashiers[minIndex] = cashiers[minIndex] + parseInt(customer)
    });
    return Math.max(...cashiers)
}

function explicitTest() {
    cases = [
        [[[5, 1, 3], 1], 9],
        [[[10, 3, 4, 2], 2], 10]
    ]
    result = cases.reduce((acc, current, idx) => {
        res = checkout_time(...current[0])
        console.log("[Test case", idx, "] Inputs are ", current[0],
            ", expected result is ", current[1],
            ", result is ", res,
            " : ", res === current[1] ? "PASS" : "FAILED");
        return acc && res === current[1]
    }, true)
    result ? console.log("All tests passed successfully") : console.log("Some tests failed")
}

function assertionTest() {
    cases = [
        [[[5, 1, 3], 1], 9],
        [[[10, 3, 4, 2], 2], 10]
    ]
    cases.forEach((c) => {
        assert(checkout_time(...c[0]) === c[1], "Tests failed")
    })
}

assertionTest()
explicitTest()