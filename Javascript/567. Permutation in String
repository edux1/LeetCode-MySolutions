/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if(s1.length > s2.length)
        return false
    let h1 = {}
    let h2 = {}
    let k = s1.length
    for(let i=0; i<k; i++) {
        if(!(s1[i] in h1)) {  
            h1[s1[i]] = 1
            h2[s1[i]] = 0
        }
        else
            h1[s1[i]]++
    }
    for(let i=0; i<k; i++) {
        if(s2[i] in h2)
            h2[s2[i]]++
        if(JSON.stringify(h2) == JSON.stringify(h1))
            return true
    }
    for(let i=k; i<s2.length; i++) {
        if(s2[i-k] in h2)
            h2[s2[i-k]]--
        if(s2[i] in h2)
            h2[s2[i]]++
        
        if(JSON.stringify(h2) == JSON.stringify(h1))
            return true
    }
    return false
};