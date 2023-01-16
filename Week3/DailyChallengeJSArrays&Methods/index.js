// Exercise 1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
console.log("1. Remove Banana from the array = " + fruits);
fruits.sort();
console.log("2. Sort the array in alphabetical order = " + fruits);
fruits.push("Kiwi");
console.log("3. Add “Kiwi” to the end of the array = " + fruits);
fruits.splice(0,1);
console.log("4. Remove “Apples” from the array = " + fruits)
fruits.reverse();
console.log("5. Sort the array in reverse order  = " + fruits)

// Exercise 2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let org = moreFruits[1][1];
console.log(org);