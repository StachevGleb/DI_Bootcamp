let sentence0 = "The movie is not that bad, I like it";
let sentence = sentence0.split(' ');
console.log(sentence)

let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad,');

if (wordNot < wordBad) {
    let newGoodSentence = sentence.splice(wordNot, 3, "good")
    let newGoodString = sentence.join(" ");
    console.log(newGoodString);
} else{
    console.log(sentence0)
}

// let arrNot = sentence.splice(wordNot, 1);
// console.log(wordNot);
// console.log(arrNot);

// let arrBad = sentence.splice(wordBad, 1);
// console.log(sentence);
// console.log(wordBad);
// console.log(arrBad)
