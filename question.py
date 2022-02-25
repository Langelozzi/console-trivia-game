#Author: Lucas Angelozzi
#Date: 02/07/22

'''This file contains the question class for my trivia game'''

#imports
import random

class Question:
    '''This class formats data into a question object and allows for the question and answers to be printed to the console'''
    def __init__(self, question: str, correct_answer: str, incorrect_answers: list, category: str, difficulty: str) -> None:
        """The constructer is simply setting all the attributes of the question and ensuring difficulty is valid

        Args:
            question (str): The question to be asked
            correct_answer (str): The correct answer
            incorrect_answers (list): 3 other incorrect answers
            category (str): The category of question
            difficulty (str): How hard the question is (easy, medium or hard)

        Raises:
            AttributeError: if the difficulty is not one of the valid 3
        """
        
        self.question = question
        
        #shuffles the answers
        self.answers = incorrect_answers
        self.answers.append(correct_answer)
        random.shuffle(self.answers)
        
        self.answer_id = self.answers.index(correct_answer) + 1
        self.category = category.lower()
        
        #if difficulty is not valid then throw an error
        if difficulty.lower() in ['easy', 'medium', 'hard']:
            self.difficulty = difficulty.lower()
        else:
            raise AttributeError

    def __str__(self):
        """This method prints on the console the question as well as the possible answers numbers 1-4
        """
        final_string = f"{self.question}\n"

        #numbers each possible answer starting with 1
        for answer in enumerate(self.answers, 1):
            final_string += f"{answer[0]}  {answer[1]}\n"

        return final_string

    def get_score(self, elapsed) -> int:
        """This method takes the elapsed time the user took to answer the question and returns the
        score that is calculated based on their time.

        Args:
            elapsed (float): the time it took them to answer the question

        Returns:
            int: the score
        """
        dif_scores = {
            "easy": 1,
            "medium": 2,
            "hard": 3
        }

        if elapsed > 5:
            score = 10 * dif_scores[self.difficulty]
        elif elapsed < 5:
            score = dif_scores[self.difficulty] * ((225/elapsed) - (7 * elapsed))
        
        return int(score)

    