from dataclasses import dataclass


@dataclass
class Exam:
    tempData: dict
    edaData: dict
    accData: dict
    bvpData: dict
    hrData: dict
    ibiData: dict

    def __init__(self, temp='Not defined', eda='Not defined', acc='Not defined', bvp='Not defined', hr='Not defined', ibi='Not defined'):
        self.tempData = temp
        self.edaData = eda
        self.accData = acc
        self.bvpData = bvp
        self.hrData = hr
        self.ibiData = ibi


@dataclass
class Student:
    first_midterm: Exam
    second_midterm: Exam
    final: Exam

    def __init__(self, first_midterm, second_midterm, final):
        self.first_midterm = first_midterm
        self.second_midterm = second_midterm
        self.final = final
