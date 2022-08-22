from attr import dataclass


class Exam:
    tempData: dict
    edaData: dict
    accData: dict
    bvpData: dict
    hrData: dict
    ibiData: dict

    def __init__(self, temp=None, eda=None, acc=None, bvp=None, hr=None, ibi=None):
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

