class Quiz:
    
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"], "answer": "Shakespeare"},
            {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"}
        ]
        self.score = 0  

    
    def ask_question(self, question_data):
        print(question_data["question"])
        for idx, option in enumerate(question_data["options"], start=1):
            print(f"{idx}. {option}")
        
        
        try:
            answer_idx = int(input("Please enter the number of your answer: "))
            if 1 <= answer_idx <= len(question_data["options"]):
                selected_answer = question_data["options"][answer_idx - 1]
                if selected_answer == question_data["answer"]:
                    print("Correct!\n")
                    return True
                else:
                    print(f"Wrong! The correct answer is {question_data['answer']}.\n")
                    return False
            else:
                print("Invalid option. Please choose a number between 1 and 4.\n")
                return False
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            return False

    
    def start_quiz(self):
        for question in self.questions:
            # Ask each question
            if self.ask_question(question):
                self.score += 1
        
        
        print(f"Quiz finished! Your score is {self.score}/{len(self.questions)}.")


def main():
    print("Welcome to the Quiz!\n")
    quiz = Quiz()  # Create a Quiz object
    quiz.start_quiz()  # Start the quiz

if __name__ == "__main__":
    main()
