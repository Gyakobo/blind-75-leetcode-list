/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // If I felt like it I would make a dictionary counter of the characters and check if those matched
    return s.split("").sort().join("") === t.split("").sort().join("");
};