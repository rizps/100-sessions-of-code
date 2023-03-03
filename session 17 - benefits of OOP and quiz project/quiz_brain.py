# TODO: asking the question
# todo: checking if the answer was correct
# todo: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("that's wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"your score: {self.score}/{self.question_number}")
        print('\n')
        if self.question_number == len(self.question_list):
            print("you've completed the quiz")
            print(f"your final score was: {self.score}/{self.question_number}")

