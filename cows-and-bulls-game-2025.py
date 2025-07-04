"""
Created 2025
Based on a web tutorial
Author: Piotr M
"""
import random


SIZE = 4


class Game:
    def __init__(self, size:int):
        """Init function."""
        self.size = size
        self.trials = 0
        while True:
            self.number = random.randint(pow(10, size - 1), pow(10, size) - 1)
            self.number_str = str(self.number)
            if len(list(self.number_str)) == len(set(list(self.number_str))):
                break
        
    def guess(self):
        """Guessing function."""
        guess = input(f"Try to guess a {self.size}-digit number: ")
        bulls = 0
        cows = 0
        self.trials = self.trials + 1
        
        if len(guess) != self.size:
            print("Wrong size!")
            return False
        
        if len(list(guess)) != len(set(list(guess))):
            print("Digits should not repeat!")
            return False
        
        guess_list = list(guess)
        number_list = list(self.number_str)
        
        for i in range(self.size):
            if guess_list[i] == number_list[i]:
                bulls = bulls + 1
            
            else:
                for j in range(self.size):
                    if guess_list[i] == number_list[j]:
                        cows = cows + 1
        
        if bulls == self.size:
            print(f"You have won with {self.trials} trials!")
            return True
        
        print(f"{bulls} bulls and {cows} cows")
        return False
    
               
def new_game() -> bool:
    """Game repetition function"""
    while True:
        decision = input("Do you want to play again [y/n]?")
        if decision == 'y':
            return True
        elif decision == 'n':
            return False


def main():
    """Main function."""
    playing = True
    main_game = Game(SIZE)

    while playing:
        
        #print(main_game.number)
        game_end = main_game.guess()
        
        if game_end:
            playing = new_game()
            game_end = False
            main_game = Game(SIZE)


if __name__ == "__main__":
    main()