let userNumberChoice
function playTheGame() {
    let asking = confirm("Do you wanna play?")
    let tries = 3
    if (asking === true) {
        userNumberChoice = Number(prompt("Please, may you insert number from 0 to 10", "0-10"))
        console.log(userNumberChoice)
        if (isNaN(userNumberChoice)) {
            alert("Sorry Not a number, Goodbye")
        } else if (userNumberChoice < 0 || userNumberChoice > 10) {
            alert("Sorry it’s not a good number, Goodbye")
        } else {
            let computerNumber = Math.random() * 10
            computerNumber = Math.ceil(computerNumber)
            console.log(computerNumber, 'computerNumber')
            let result = true;
            // console.log(result, 'result')
            while (tries > 1 && result) {
                result = compareNumbers(userNumberChoice, computerNumber);
                tries--
            }

        }
    } else {
        alert("See you ... very sad")
    }
}

playTheGame();

let counter = 0;

function compareNumbers(userNumber, computerNumber) {

    if (userNumber == computerNumber) {
        alert("Great you are winner");
        return false
    } else if (userNumber > computerNumber) {
        userNumberChoice = Number(prompt("Your number is bigger then the computer’s, guess again", "0-10"))
       return true
    } else if (userNumber < computerNumber) {
        userNumberChoice = Number(prompt("Your number is smaller then the computer’s, guess again", "0-10"))
        return  true
    }
}
