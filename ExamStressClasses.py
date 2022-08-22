
class Exam:
    tempData: dict
    edaData: dict

    def __init__(self, temp, eda):
        self.tempData = temp
        self.edaData = eda


class Student:
    first_midterm: Exam
    second_midterm: Exam
    final: Exam

    def __init__(self, first_midterm, second_midterm, final):
        self.first_midterm = first_midterm
        self.second_midterm = second_midterm
        self.final = final