# Code by Rebecca Roeth, CSE 210
from game.card import Card

class Director:
    '''
    Attributes:
        card (List[Card]): a list of card instances
        is_playing (boolean): Wheather or not the game is being played still
            If player reaches 0, game automatially over
            If player chooses to end game, game ends
        score(int): The score for one round of play.
            Starts at 300
        total_score (int): The score for the entire game.
            +100 if they guess correctly
            -75 if they guess incorrectly
    '''
    def __init__(self):
        '''Constructs a new Director
        
        Args:
            self (Director): an instance of Director
        '''
        self.cards = []
        self.is_playing = True
        self.score = 0
            # Represents card played
        self.h_l = ""
            # Represents high/low choice
        self.total_score = 300
            # Represents total
        
    # Revisit this and see where applicable to this game
        for i in range(5):
            die = Die()
            self.dice.append(die)
    
    def start_game(self):
        """Starts the game by running the main game loop

        Args:
            self (Director): an instance of director
        """
        # The game starts without asking if you want to play, unlike the dice
        while self.is_playing:
            self.do_firstcard
            self.get_inputs() # High/Low choice
            self.do_outputs()
            self.still_playing()

    def do_firstcard(self):
        """Updates the player's score.
        
        Args:
            self(Director): An instance of Director
        """
        if not self.is_playing:
            return
    
        # This probably doesn't work revisit
        for i in range(len(self.cards)):
            card = self.card[i]
            drawn = card.draw()

        print(f"\nThe card is: {drawn}")
    
    def get_inputs(self):
        '''Ask the user if they want to keep playing

        Args:
            self (director): An instance of Director
        '''
        self.h_l = input("Higher or lower? [h/l] ")

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to play again
        
        Args:
            self(Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        for i in range(len(self.cards)):
            card = self.card[i]
            values += f"{card.value}"
        
        print(f"Next card was: {values}")
        print(f"Your score is: {self.total_score}")

    def still_playing(self):
        '''Ask the user if they want to keep playing
            
            Args:
            self (director): An instance of Director
        '''
        playing = input("Play again? [y/n] ")
        self.is_playing = (playing == "y")