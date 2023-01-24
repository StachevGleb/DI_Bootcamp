function playTheGame(){
    let asking = confirm("Do you wanna play?")
    let tries = 3
    if(asking === true){
        let userNumber = Number(prompt("Please, may you insert number from 0 to 10", "0-10"))
        console.log(userNumber)
        if(isNaN(userNumber)){
        alert("Sorry Not a number, Goodbye")
        }else if(userNumber < 0 || userNumber > 10){
        alert("Sorry it’s not a good number, Goodbye")
        }else{
            let computerNumber = Math.random()*10
            computerNumber = Math.ceil(computerNumber)
            console.log(computerNumber)
            let result = compareNumbers(userNumber,computerNumber)
            console.log(result)
            while(result == false){
                tries--
            }
        }
    }else {
        alert("See you ... very sad")
    }
}
playTheGame()

let counter = 0

function compareNumbers(userNumber,computerNumber){
    
        if(userNumber == computerNumber){
            alert("Great you are winner")
            }else if(userNumber > computerNumber){
                 userNumber = Number(prompt("Your number is bigger then the computer’s, guess again", "0-10"))
                 compareNumbers(userNumber,computerNumber)
            }else if(userNumber < computerNumber){
                 userNumber = Number(prompt("Your number is smaller then the computer’s, guess again", "0-10"))
                 compareNumbers(userNumber,computerNumber)
            }
}