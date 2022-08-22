import os
from typing import Dict
import pandas as pd
from ExamStressClasses import Exam, Student

# Få data i et bedre format
# For each student folder: in final and both midterm folders: read TEMP.csv and EDA.csv
# Visualiser data enkeltvis
# Make folder to save the visualisations in (REMEMBER TO SAVE)

if __name__ == '__main__':

    dataPath = os.path.join(os.getcwd(), "data")
    student_paths = [f.path for f in os.scandir(dataPath) if f.is_dir()]
    myStudents = {}

    students: Dict[str, Student] = dict()
    for path in student_paths:
        exam_type = ['Final', 'Midterm 1', 'Midterm 2']
        exam_list = {}

        for exam_path in exam_type:
            pathToTemp = os.path.join(path, exam_path, "TEMP.csv")
            temp = pd.read_csv(pathToTemp)
            pathToEDA = os.path.join(path, exam_path, "EDA.csv")
            eda = pd.read_csv(pathToEDA)
            exam_list[exam_path] = Exam(temp, eda)

        myStudentTest = Student(exam_list['Midterm 1'], exam_list['Midterm 2'], exam_list['Final'])
        myStudents[path] = myStudentTest

    student_names = ['S1', 'S10', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']
    name_count = 0
    for paths in student_paths:
        name = student_names[name_count]
        myStudents[name] = myStudents.pop(paths)
        name_count += 1




    # start by making a simple dataclass (google it) for some of the data and analyse that part of the data.
    # Dataclasses will help you get autocompletion
    # put the dataclasses in a Python Project (top right corner of pycharm, right click ExamStressAnalysis --> new --> python package )
    # then right click on the new package --> new --> python class
    # ignore the __init__.py file. Do not touch it. The file is executed on import time, and the classes defined in it is bound to variable names
    # Pro tip when using pycharm: use alt+enter or ctrl+space to get autocompletion!

    # Step 1 - choose first data to analyse, maybe pick something easy.
    # Step 2 - create a dataclass for that data. Example:
    '''
    @dataclass
    class TemperatureContainer:
        date: datetime
        temperatures: List[Number] #In a dataclass we annotate the data with types. The right hand side of the ':' defines the type of the field.
    @dataclass <-- This is called an annotation! It helps the coder to define some behaviour for the code. In this case
    we tell the coder, interpreter and IDE that the class cannot contain methods, only fields. 
    '''

    # Consider making a dataclass for the data itself --- for instance, a HeartRateMeasurementContainer that has a list of HeartRateMeasurement

    # Step 3 - Analyse the data, and save the result in a file at some reasonable place
    pass
