/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let usedChars = {}
    let start = 0
    let maxLength = 0
    for(let i=0; i<s.length; i++) {
        if(s[i] in usedChars && start <= usedChars[s[i]])
            start = usedChars[s[i]] + 1
        else 
            maxLength = Math.max(maxLength, i - start + 1)
        usedChars[s[i]] = i
    }
    return maxLength
};