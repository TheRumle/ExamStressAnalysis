import os
from typing import Dict
import pandas as pd
from ExamStressClasses import Exam, Student
from ExamStressFunctions import rename_dict_keys, extract_exam_data

if __name__ == '__main__':

    dataPath = os.path.join(os.getcwd(), "data")
    student_paths = [f.path for f in os.scandir(dataPath) if f.is_dir()]
    students = extract_exam_data(['Final', 'Midterm 1', 'Midterm 2'], student_paths, ['TEMP.csv', 'EDA.csv'])

    rename_dict_keys(['S1', 'S10', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'], student_paths, students)

    # Visualiser data enkeltvis
    # Make folder to save the visualisations in (REMEMBER TO SAVE)

    # put the dataclasses in a Python Project (top right corner of pycharm, right click ExamStressAnalysis --> new --> python package )
    # then right click on the new package --> new --> python class
    pass