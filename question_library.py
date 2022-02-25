#Author: Lucas Angelozzi
#Date: 02/07/22

'''This file contains the questionlibrary class for my trivia game'''

#imports
import json
import question
import random

class QuestionLibrary:
    """This class loads the JSON data and then can filter it based on the category and difficulty
    """
    def __init__(self, filename = 'C:/Users/lucas/OneDrive/Documents/BCIT/Level_2/ACIT_2515_(Object Oriented Programming)/Week6/lab5TriviaCont/trivia.json') -> None:
        self.questions = []
        
        with open(filename, 'r') as jf:
            file = json.load(jf)
            
            #creates Question object from each Json object provided in the file
            for data in file:
                x = question.Question(data["question"], data["correct_answer"], data["incorrect_answers"], data["category"], data["difficulty"])
                self.questions.append(x)
        
        random.shuffle(self.questions)

    def __len__(self):
        """This is a magic method that will return the length of the list with all the questions

        Returns:
            int: length of the list of all questions
        """
        return len(self.questions)

    def get_categories(self):
        """This method iterates through the questions and creates a set of all of the categories


        Returns:
            set: the set of categories possible
        """

        categories = set()
        for question in self.questions:
            categories.add(question.category)
        
        return categories

    def get_questions(self, category = None, difficulty = None, number = 10):
        """This method gets the category, difficulty and number of questions then returns that amount of questions
        with those categories and difficulties

        Args:
            category (str, optional): The category of questions the user wants to answer. Defaults to None and will return questions of any category.
            difficulty (str, optional): The difficulty of the questions the user wants to answer. Defaults to None and will return questions of any difficulty.
            number (int, optional): How many questions the user wants to play. Defaults to 0.

        Returns:
            list: the question objects that have been filtered based on the users input
        """
        
        #all of the questions copied to a new list
        filtered = self.questions.copy()
        categories = self.get_categories()
        diffs = ["easy", "medium", "hard"]

        #filter the questions based on their difficulty
        if difficulty in diffs:
            filtered = [q for q in filtered if q.difficulty == difficulty]

        #filter the questions based on their category
        if category in categories:
            filtered = [q for q in filtered if q.category == category]

        #if there is no defined category or difficulty then filtered stays as all of the questions

        #returns a list that is of length number or smaller
        return filtered[:number]

