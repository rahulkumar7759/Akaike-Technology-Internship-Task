# -*- coding: utf-8 -*-
"""NLP_Tasks_Assignments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gjs1lY1KtUyX_vCbBGE-nc980YMNBLRP
"""

from google.colab import drive
drive.mount('/content/drive')

"""## *Import library's*"""

import spacy
import random
import numpy as np
import pandas as pd

"""##*Load the english language model*

"""

nlp = spacy.load("en_core_web_sm")

"""## *Define function*"""

def get_mca_questions(context: str, num_questions: int):
  doc = nlp(context)

"""## *Define MCQ generation function*"""

def generate_mcq_with_multiple_correct(question, correct_answers, other_options, num_options=4):
        options = correct_answers + other_options
        random.shuffle(options)

        mcq = {
            "question": question,
            "options": options,
            "correct_answers": correct_answers
        }

"""## *Generate a Diffrent MCQ Question*"""

def generate_variety_question():
        # randomly select the sentence from content
        sentence = random.choice(list(doc.sents))

        # randomly choose non- pronounciation words from sentence as blank word
        blank_word = random.choice([token for token in sentence if not token.is_punct])

        # create a question text with blank word ----
        question_text = sentence.text.replace(blank_word.text, "______")

        #set correct answers to the blank word
        correct_answers = [blank_word.text]

        #generating other possible answers
        other_options = [token.text for token in doc if token.is_alpha and token.text != correct_answers[0]]

        #randonly determine how many correct options
        num_correct_options = random.randint(1, 2)

        #randomly select correct options to the list of options
        correct_answers.extend(random.sample(other_options, num_correct_options))

        # no of incorrect answers
        num_other_options = min(4 - num_correct_options, len(other_options))
        other_options = random.sample(other_options, num_other_options)

        #generationg final MCQ
        mcq = generate_mcq_with_multiple_correct(question_text, correct_answers, other_options)
        return mcq

"""## *Generate questions & Process and format questions*"""

def mca_questions(questions):
  #created empty list to store multiple choice questions
  mca_questions = []
# enumerate function is used to iterate over the questions
  for i, question in enumerate(questions, start=1):

        #created a string for question number and question text.
        question_str = f"Q{i}: {question['question']}\n"

        #created empty string to store option for current question
        options_str = ""

        #iterate through options
        for j, option in enumerate(question['options']):
            options_str += f"{j+1}. {option}\n"

        #format the correct answers into human redable format
        correct_options_formatted = " & ".join([f"({chr(97+question['options'].index(ans))})" for ans in question['correct_answers']])

        #combine the questions and options and format the correct answes
        correct_options_str = f"Correct Options: {correct_options_formatted}"

        #add the questions into formated questions
        mca_question = f"{question_str}{options_str}{correct_options_str}\n"
        mca_questions.append(mca_question)

  return mca_questions

"""##Print the question"""

#user input for paragraph
context = input("Enter the paragraph: ")

#no of questions user want to generate
num_questions = int(input("Enter the number of questions: "))

#calls the function and generate MCQ questions
mca_questions = get_mca_questions(context, num_questions)
for question in mca_questions:
    print(question)

"""##MCQ finals codes"""

import spacy
import random

# Load English language model
nlp = spacy.load("en_core_web_sm")

def get_mca_questions(context: str, num_questions: int):
    doc = nlp(context)

    def generate_mcq_with_multiple_correct(question, correct_answers, other_options, num_options=4):
        options = correct_answers + other_options
        random.shuffle(options)

        mcq = {
            "question": question,
            "options": options,
            "correct_answers": correct_answers
        }

        return mcq

    def generate_variety_question():
        sentence = random.choice(list(doc.sents))
        blank_word = random.choice([token for token in sentence if not token.is_punct])

        question_text = sentence.text.replace(blank_word.text, "______")
        correct_answers = [blank_word.text]

        other_options = [token.text for token in doc if token.is_alpha and token.text != correct_answers[0]]
        num_correct_options = random.randint(1, 2)  # Generate 1 or 2 correct options
        correct_answers.extend(random.sample(other_options, num_correct_options))

        num_other_options = min(4 - num_correct_options, len(other_options))
        other_options = random.sample(other_options, num_other_options)

        mcq = generate_mcq_with_multiple_correct(question_text, correct_answers, other_options)
        return mcq

    questions = [generate_variety_question() for _ in range(num_questions)]

    mca_questions = []
    for i, question in enumerate(questions, start=1):
        question_str = f"Q{i}: {question['question']}\n"
        options_str = ""
        for j, option in enumerate(question['options']):
            options_str += f"{j+1}. {option}\n"

        correct_options_formatted = " & ".join([f"({chr(97+question['options'].index(ans))})" for ans in question['correct_answers']])
        correct_options_str = f"Correct Options: {correct_options_formatted}"

        mca_question = f"{question_str}{options_str}{correct_options_str}\n"
        mca_questions.append(mca_question)

    return mca_questions

context = input("Enter the paragraph: ")
num_questions = int(input("Enter the number of questions: "))
mca_questions = get_mca_questions(context, num_questions)
for question in mca_questions:
    print(question)

"""## **Thank You**"""