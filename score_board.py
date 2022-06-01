class ScoreBoard:
    """Snake game Scoreboard"""
    def __init__(self, start_score, a_io, a_message):
        self.score = start_score
        self.io = a_io
        self.message = a_message

    def update_score(self, a_score):
        self.score += a_score

    def display(self):
        self.io.clear()
        self.io.write(self.message + f"{self.score}")
