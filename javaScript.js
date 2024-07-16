/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

/**
 * counter @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */