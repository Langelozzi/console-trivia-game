#Author: Lucas Angelozzi
#Date: 02/07/22

#imports
import os
import time
import question_library

"""This file contains the Game class that will actually run the game"""

class Game:
    """This Class runs the gameplay of the trivia game
    """
    def __init__(self) -> None:
        """The constructer creates an instance of the question library then
        prints out the possible categories in a numbered list. It then asks
        the user for input for category, difficulty and a number of questions
        and then creates a list of filtered questions that will be asked to the user."""
        
        all_questions = question_library.QuestionLibrary()
        categories = all_questions.get_categories()

        for n, c in enumerate(categories, 1):
            print(n, c)
        
        #trying because if they don't enter an integer it will be an error so if its not then just make category none
        try:
            category_choice = int(input(f"Please enter a category (1-{len(categories)}): "))
            
            while category_choice not in range(1, len(categories) + 1):
                category_choice = int(input(f"Please enter a category (1-{len(categories)}): "))
            
            category = list(categories)[category_choice-1]
        except:
            category = None
        
        diff = input("Please enter a difficulty (easy, medium or hard): ").lower()

        #creates a list of all questions of length that user entered and that match the users desired category and difficulty
        self.questions = all_questions.get_questions(category, diff)

    def play(self):
        """This method is responsible for playing each round of the game (aka each question). It will show the question and the
        options for the answer, then start the timer, ask for an answer, stop the timer, calculate the score, show the user the 
        results of their guess and the score, then show the next question.
        """
        
        score = 0

        for question in self.questions:
            print("<---------------------------Question---------------------------->")
            
            print(question)
        
            #starts timer when question is shown
            start = time.time()

            #reprompts until its a number between 1-4
            guess = input("\nWhat is the correct answer? (enter number 1-4): ")
            while guess.isnumeric() is False or int(guess) not in [1,2,3,4]:
                guess = input("\nWhat is the correct answer? (enter number 1-4): ")

            #ends timer when user enters an answer and calculates the elapsed time
            end = time.time()
            elapsed = end - start

            if int(guess) == question.answer_id:
                print("\nCORRECT!\n")
                score += question.get_score(elapsed)
            else:
                print(f"\nINCORRECT\nThe correct answer is: {question.answer_id}\n")
            
            #wait 3 second before clearing the console and showing score and next question
            time.sleep(3)
            
            #clear console for windows OS
            if os.name == 'nt':
                os.system('cls')
            #clear console for any other OS
            else:
                os.system('clear')

            print(f"Score: {score}\n")
            
        return score


if __name__ == '__main__':
    game = Game()
    game.play()