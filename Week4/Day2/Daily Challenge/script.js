let arr = prompt("Insert some words separated by comma - ',' ")
let array = arr.split(",")

for(let i = 0; i < (array.length-1);i++){
if(array[i].length > array[i+1].length){
    let astrCount= array[i].length
    // console.log(array[i].length)
} else{
    astrCount = array[i+1].length
    // console.log(array[i+1].length)
}
let astrArr =[]
    // console.log(array[i])
}
let astrArr = Array(astrCount+4).fill("*");
console.log(astrArr.join(""))

for(let j = 0; j < array.length;j++){
console.log("* " + array[j] + "array[j]-" + " *")
}
console.log(astrArr.join(""))

// console.log(array)