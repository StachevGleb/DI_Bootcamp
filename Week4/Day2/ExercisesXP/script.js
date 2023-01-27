// Exercise 1 
// Part I
function infoAboutMe(){
console.log("My name is Gleb Stachev, I am student in developers institute")
}
infoAboutMe()
// Part II
function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

// Exercise 2
function calculateTip() {
    let bill = prompt("John, dear ... what's amount of the bill ?")
    bill=+bill
    let tip = 0;
    if(bill <=50){
        tip = bill*1.2
    }else if(bill > 50 && bill < 200){
        tip = bill*1.15
    }else{
        tip = bill*1.1
    }
    console.log(`Tip amount and the final bill ${bill} and ${tip}`)
}
// calculateTip() 

// Exercise 3
function isDivisible(divisor = 23){
    let divis23=[]
    let sum = 0;
    for(let i = 0; i <= 500; i++){
        if(i%divisor == 0){
            divis23.push(i)
            console.log(i)
            sum += i
        }
    }
    console.log(divis23)
}
// isDivisible(20)

// Exercise 4
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
let shoppingList = ["banana", "orange", "apple"]

function myBill(){
    let price=0
    for(let i = 0; i <= 2; i++){
       let j = shoppingList[i]
    if(stock[j] != 0){
        // console.log(j, stock[j])
        stock[j] -= 1
        price +=  prices[j]
    }
}
console.log(stock)
console.log(`total price: ${price}`)
}
// myBill()

// Exercise 5
function changeEnough(itemPrice, amountOfChange){
let moneySum = ((amountOfChange[0]*0.25) + (amountOfChange[1]*0.1) + (amountOfChange[2]*0.05) + (amountOfChange[3]*0.01))
if(itemPrice <= moneySum){
return true
}else{
return false
}
}
// console.log(changeEnough(9.25, [25, 20, 5, 0]))

// Exercise 6
function hotelCost(nightsNum){
    let cost= 140;
    if(isNaN(nightsNum)){
        nightsNum = parseInt(prompt("Number of nights you would like to stay in our hotel (only numbers)?"))
    }
    return cost*nightsNum
}
// console.log("Total price = ", hotelCost(), '$')

function planeRideCost(destination){
    let cost = 0;
    if(!isNaN(destination) || destination === ''){
       destination = prompt('Where are you searching for hotel ? (London, Paris, etc)' )
    }else if (destination === "London"){
        cost = 183
    }else if(destination === "Paris"){
        cost = 220
    }else{
        cost = 300
    } 
    return cost
}
// console.log("Total price = ", planeRideCost())

function rentalCarCost(dayNum){
    let cost = 0;
    if(isNaN(dayNum) || dayNum === ''){
        dayNum = parseInt(prompt("Number of days you would like to rent the car ? (Please, insert only numbers)"))
    }else if(dayNum > 10){
        cost = 40*dayNum*0.95 
    }else{
        cost = 40*dayNum
    }
    return cost
}
// console.log("Total amount = ",rentalCarCost())

function totalVacationCost() {
    let nightsNum = parseInt(prompt("Number of nights you would like to stay in our hotel ?"))
    let destination = prompt('Where are you searching for hotel ?')
    let dayNum = parseInt(prompt("Number of days you would like to rent the car ?"))


    return rentalCarCost(dayNum) + planeRideCost(destination) + hotelCost(nightsNum)
}
console.log("Total amount = ",totalVacationCost())
