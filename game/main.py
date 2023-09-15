import random



class GetRandomWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]

    def get_word(self):
        return random.choice(self.words)


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed:
            self.guessed.append(letter)
            print("You guessed the letter!")
        if letter not in self.word:
            print("You guessed wrong!")
        if letter in self.guessed.append(letter):
            print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for letra in self.word:
            if letra in self.guess:
                print(letra, end="")
            else:
                print(letra,"_", end="")
        print('\n')

    def check_if_player_won(self):
        if self.word == self.guessed:
            return self.word



class Play:
    def __init__(self):
        self.word = GetRandomWord.get_word()
        self.hanged = Hangman(self.word)

    def play_game(self):
        while True:
            self.hanged.get_status()
            letter = input("Escribe una letra " )
            self.hanged.guess(letter)
            if self.hanged.check_if_player_won():
                print("You won!")
                break


if __name__ == "__main__":

 game = Play()
 game.play_game()