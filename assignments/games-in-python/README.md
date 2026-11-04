# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game in Python. You'll practice string manipulation, loops, conditionals, and random selection while creating a fun, interactive program.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Use the provided `starter-code.py` to choose a secret word at random and set up the variables that track the game state.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Keep track of the letters the player has already guessed
- Set a maximum number of incorrect guesses allowed (e.g., 6)


### 🛠️	Build the Game Loop

#### Description
Create the main loop that asks the player to guess letters and shows their progress after each guess.

#### Requirements
Completed program should:

- Accept one letter per guess from the player
- Display the current progress using underscores for hidden letters (e.g., `_ y t _ _ n`)
- Show how many incorrect guesses are remaining
- Let the player know if they already guessed a letter

Example:

```
Word: _ _ _ _ _ _
Guesses remaining: 6
Guess a letter: p
Word: p _ _ _ _ _
```


### 🛠️	End the Game

#### Description
Detect when the game is over and tell the player whether they won or lost.

#### Requirements
Completed program should:

- End the game when the whole word is guessed or no attempts remain
- Display a win message when the player guesses the word
- Display a lose message that reveals the secret word when attempts run out

Example:

```
🎉 You won! The word was: python
```

```
💀 Game over! The word was: python
```
