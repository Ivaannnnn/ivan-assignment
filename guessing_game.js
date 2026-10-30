
// ==========================================
// GUESSING NUMBER GAME
// Created by: Ivan Firmansyah
// Description: Guess a random number from 0 to 10
// ==========================================

const readline = require("readline");

// Create an interface for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


// Function 1: Generate a random number
function generateNumber() {
    return Math.floor(Math.random() * 11);
}


// Function 2: Ask the player for a guess
function getGuess() {
    return new Promise((resolve) => {
        rl.question("Guess a number (0-10): ", (answer) => {
            const guess = Number(answer);

            if (
                answer.trim() === "" ||
                !Number.isInteger(guess) ||
                guess < 0 ||
                guess > 10
            ) {
                console.log("Please enter a valid number from 0 to 10.");
                resolve(getGuess());
            } else {
                resolve(guess);
            }
        });
    });
}


// Function 3: Check the player's guess
function checkGuess(guess, number) {

    if (guess === number) {
        console.log("Yeah, you guessed it!");
        return true;
    }

    else if (guess < number) {
        console.log("Too low, try again!");
        return false;
    }

    else {
        console.log("Too high, try again!");
        return false;
    }
}


// Function 4: Start the guessing game
async function guessingGame() {

    while (true) {

        console.log("\n================================");
        console.log("       GUESSING NUMBER GAME");
        console.log("================================");

        const number = generateNumber();

        console.log("I have selected a number between 0 and 10.");

        let correct = false;

        // Continue until the player guesses correctly
        while (!correct) {

            const guess = await getGuess();

            correct = checkGuess(guess, number);
        }

        // Ask if the player wants to play again
        const again = await new Promise((resolve) => {
            rl.question("\nDo you want to play again? (yes/no): ", resolve);
        });

        if (again.trim().toLowerCase() !== "yes" &&
            again.trim().toLowerCase() !== "y") {

            console.log("\nThank you for playing! Goodbye!");
            break;
        }
    }

    rl.close();
}


// Main program
guessingGame();
