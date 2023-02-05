/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let txt = "";
    let word = "";
    for(let i=0; i<s.length; i++) {
        if(s[i] == " ") {
            if(txt != "")
                txt += " " + word;
            else
             txt += word;
            word = "";
        }
        else {
            word = s[i] + word;
        }        
    }
    if(word != "") {
        if(txt != "")
            txt += " " + word;
        else
            txt += word;
    }
    return txt;
};