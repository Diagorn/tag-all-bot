class FaqQuestionDto:
    def __init__(self, number, text, answer, category_number) -> None:
        self.number = number
        self.text = text
        self.answer = answer
        self.category_number = category_number
