let userAnswer = 0
let bottles = 99
let loopCount = 0
 function songCounter(){
    console.log("We start the song at 99 bottles")
    while(bottles > 0){
        userAnswer = parseInt(prompt("Tell me a number to begin counting down bottles in your song","1-12"))
        if(isNaN(userAnswer) || userAnswer <=0 || userAnswer > 12){
            userAnswer = parseInt(prompt("Tell me a digit and only correct range of numbers, please","1-12"))
        }
        loopCount += loopCount
        bottles = bottles - userAnswer
        if(userAnswer == 1){
            console.log(`Take ${userAnswer} down, pass it around`)
        }else{
            console.log(`Take ${userAnswer} down, pass them around`)
        }
        console.log(`we have now ${bottles} bottles`)
    }
    console.log("no bottle of beer on the wall")
 }