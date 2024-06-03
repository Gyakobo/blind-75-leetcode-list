/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let d = {};
    s.split("").map((a) => d[a] = a in d ? d[a] + 1 : 1);
    t.split("").map((a) => d[a] = a in d ? d[a] - 1 : -1);
    for (let a in d) {
        if (d[a] !== 0) return false;
    }
    return true;
};