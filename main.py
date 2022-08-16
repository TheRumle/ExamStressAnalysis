import os
import pandas as pd

# Få data i et bedre format
# For each student folder: in final and both midterm folders: read TEMP.csv and EDA.csv
# Visualiser data enkeltvis
# Make folder to save the visualisations in (REMEMBER TO SAVE)

class Midterm:
    tempData: dict
    edaData: dict
    def __init__(self, temp, eda):
        self.tempData = temp
        self.edaData = eda

class Final:
    tempData: list
    edaData: list
    def __init__(self, temp, eda):
        self.tempData = temp
        self.edaData = eda

class Student:
    midterm: Midterm
    final: Final
    def __init__(self, student, midterm, final):
        self.midterm =
        self.final =

if __name__ == '__main__':

    dataPath = os.path.join(os.getcwd(), "data")
    student_folders = [f.path for f in os.scandir(dataPath) if f.is_dir()]

    tempFinal = []
    tempMidterm1 = []
    tempMidterm2 = []
    edaFinal = []
    edaMidterm1 = []
    edaMidterm2 = []

    for student in student_folders:
        pathTempFinal = os.path.join(student, 'final\TEMP.csv')
        pathTempMidterm1 = os.path.join(student, 'Midterm 1\TEMP.csv')
        pathTempMidterm2 = os.path.join(student, 'Midterm 2\TEMP.csv')
        tempFinal.append(pd.read_csv(pathTempFinal))
        tempMidterm1.append(pd.read_csv(pathTempMidterm1))
        tempMidterm2.append(pd.read_csv(pathTempMidterm2))

        pathEDAFinal = os.path.join(student, 'final\EDA.csv')
        pathEDAMidterm1 = os.path.join(student, 'Midterm 1\EDA.csv')
        pathEDAMidterm2 = os.path.join(student, 'Midterm 2\EDA.csv')
        edaFinal.append(pd.read_csv(pathEDAFinal))
        edaMidterm1.append(pd.read_csv(pathEDAMidterm1))
        edaMidterm2.append(pd.read_csv(pathEDAMidterm2))

    tempMidterm = {'midterm1': tempMidterm1, 'midterm2': tempMidterm2}
    edaMidterm = {'midterm1': edaMidterm1, 'midterm2': edaMidterm2}
    midterm = Midterm(tempMidterm, edaMidterm)

    final = Final(tempFinal, edaFinal)

    # data.get(folder).midterm.tempData.append(pandas.read_csv(pathTemp))
    #dict.get('').
    #data: dict[str, Student] = dict()


    # start by making a simple dataclass (google it) for some of the data and analyse that part of the data.
    # Dataclasses will help you get autocompletion
    # put the dataclasses in a Python Project (top right corner of pycharm, right click ExamStressAnalysis --> new --> python package )
    # then right click on the new package --> new --> python class
    # ignore the __init__.py file. Do not touch it. The file is executed on import time, and the classes defined in it is bound to variable names
    # Pro tip when using pycharm: use alt+enter or ctrl+space to get autocompletion!

    #Step 1 - choose first data to analyse, maybe pick something easy.
    #Step 2 - create a dataclass for that data. Example:
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
