/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const words = s.split(" ");
    const reversedWords = words.map((word)=>{
        return word.split("").reverse().join("");
    })
    const reversedString = reversedWords.join(" ");
    return reversedString;
};