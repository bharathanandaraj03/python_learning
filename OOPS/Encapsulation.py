class ScoreBoard:
    def __init__(self,score):
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score = score
s1 = ScoreBoard(9)
s1.set_score(10)
print(s1.get_score())