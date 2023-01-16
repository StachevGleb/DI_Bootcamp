// Exercise 1
let food = 'pancakes';
let meal = 'breakfast';
console.log('I eat ' + food + ' at every ' + meal);

// Exercise 2
// Part I
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length
console.log('myWatchedSeriesLength = ' + myWatchedSeriesLength);
let myWatchedSeriesSentence = myWatchedSeries.slice(" ");
console.log('myWatchedSeriesSentence = ' + myWatchedSeriesSentence);
console.log('I watched ' + myWatchedSeriesLength + ' series : ' + myWatchedSeriesSentence);
// Part II
myWatchedSeries.splice(2, 1, "friends")
console.log('withFriends = ' + myWatchedSeries);
myWatchedSeries.push("dragon");
console.log('withEnd = ' + myWatchedSeries);
myWatchedSeries.unshift("lion");
console.log('withBeginning = ' + myWatchedSeries);
myWatchedSeries.splice(1, 1);
console.log('delBLackMirror = ' + myWatchedSeries);
console.log('3d letter of the series “money heist” = ' + myWatchedSeries[1][2]);
console.log('myWatchedSeries array all the modifications = ' + myWatchedSeries);

// Exercise 3
let temperCel = 10; //celsius temperature 
let temperFar = ((temperCel/5)*9+32); //fahrenheit temperature 
console.log( "temperature °C = " + temperCel + " °C in fahrenheit °F = " + temperFar + " °F");

// Exercise 4
    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: It will output 55, because 34 and 21 are numbers
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: It will output 23, because 2 and 21 are numbers
    // Actual: 23

    console.log(c) //second expression
    // What is the value of c? - undefined;
    
    console.log(3 + 4 + '5');
    // number + number + string = string - "75"



    // Exercise 5

console.log(typeof(15));
// Prediction:number
// Actual:number

console.log(typeof(5.5));
// Prediction:number
// Actual:number

console.log(typeof(NaN));
// Prediction:NaN, because it's NaN ...
// Actual:number

console.log(typeof("hello"))
// Prediction:string - ""
// Actual:string

console.log(typeof(true))
// Prediction:boolean
// Actual:boolean

console.log(typeof(1 != 2))
// Prediction:boolean
// Actual:boolean

console.log("hamburger" + "s")
// Prediction:hamburgers, because of string + string
// Actual:hamburgers

console.log("hamburgers" - "s")
// Prediction:don't know
// Actual:NaN

console.log("1" + "3")
// Prediction:"13", because of string + string
// Actual:"13"

console.log("1" - "3")
// Prediction:NaN, like "hamburgers" - "s"
// Actual:-2

console.log("johnny" + 5)
// Prediction:johnny5, because string + number = string
// Actual:johnny5

console.log("johnny" - 5)
// Prediction:NaN, like "hamburgers" - "s"
// Actual:NaN

console.log(99 * "hello")
// Prediction:NaN, like "hamburgers" - "s"
// Actual:NaN

console.log(1 != 1)
// Prediction:false
// Actual:false

console.log(1 == "1")
// Prediction:true
// Actual:true

console.log(1 === "1")
// Prediction:false
// Actual:false


// Exercise 6
console.log(5 + "34")
// Prediction:534, number + string = string
// Actual:534

console.log(5 - "4")
// Prediction:1, like "1" - "3" in Exercise 5
// Actual:1

console.log(10 % 5)
// Prediction:0, after comma we have no digits after dividing process
// Actual:0

console.log(5 % 10)
// Prediction:5, after dividing process after comma we have 5
// Actual:5

console.log("Java" + "Script")
// Prediction:JavaScript
// Actual:JavaScript

console.log(" " + " ")
// Prediction:I think we'll get two invisible empty spaces
// Actual: I think we'll get two invisible empty spaces

console.log(" " + 0)
// Prediction:" 0", empty it's character + 0 number = string
// Actual:" 0"

console.log(true + true)
// Prediction:true
// Actual:2

console.log(true + false)
// Prediction:1, 1 + 0 = 1
// Actual:1

console.log(false + true)
// Prediction:1, 1 + 0 = 1
// Actual:1

console.log(false - true)
// Prediction:1, 0 - 1 = 1
// Actual:-1

console.log(!true)
// Prediction:0 or false
// Actual:false

console.log(3 - 4)
// Prediction:-1
// Actual:-1

console.log("Bob" - "bill")
// Prediction:NaN, the same as in Ex 5 "hamburgers" - "s"
// Actual:NaN






