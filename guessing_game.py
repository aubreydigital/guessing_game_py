import random

def guess_game(difficulty):
  guesses = []
  numToGuess = random.randint(0, 100)
  if difficulty == 'easy':
    guessNo = 10
  elif difficulty == 'hard':
    guessNo = 5
  win = False
  while guessNo > 0 and win == False:
    guess = int(input('Make a guess: '))
    if guess == numToGuess:
      print('You got it! That\'s amazing!')
      win = True
    elif guess < numToGuess and guessNo > 1 and guess not in guesses:
      guesses.append(guess)
      print('Too low.')
      print('Guess again.')
      print(f'You have {guessNo - 1} attempts remaining to guess the number.')
      guessNo -= 1
    elif guess > numToGuess and guessNo > 1 and guess not in guesses:
      guesses.append(guess)
      print('Too high.')
      print('Guess again.')
      print(f'You have {guessNo - 1} attempts remaining to guess the number.')
      guessNo -= 1
    elif guess in guesses:
      print('You already guessed that number')
      print('Guess again.')
      print(f'You have {guessNo} attempts remaining to guess the number.')
    elif guess != numToGuess and guessNo == 1:
      print('You lose.')

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
difSetting = input('Choose a difficulty. Typing \'easy\' or \'hard\':')
guess_game(difSetting)
