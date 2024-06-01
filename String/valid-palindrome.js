/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.replaceAll(/[^A-Za-z0-9]/g, "");
    for (let i = 0; i < s.length / 2; i++) {
        if (s.charAt(i).toLowerCase() !== s.charAt(s.length - 1 - i).toLowerCase()) return false;
    }
    return true;
};