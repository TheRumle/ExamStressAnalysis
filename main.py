
# Press the green button in the gutter to run the script.

# This guard is used to ensure that the file is not executed on import time
import os

import pandas as pandas


class Midterm:
    tempData:list
    edaData:list

class Student:
    midterm: Midterm

if __name__ == '__main__':

    # Få data i et bedre format
        # For each student folder: in final and both midterm folders: read TEMP.csv and EDA.csv
    # Visualiser data enkeltvis
        # Make folder to save the visualisations in (REMEMBER TO SAVE)
    x = [x[0] for x in os.walk(os.getcwd())]

    dataPath = os.path.join(os.getcwd(), "data")
    student_folders = [f.path for f in os.scandir(dataPath) if f.is_dir()]

    data: dict[str, Student] = dict()

    temperature = []
    for folder in student_folders:
        pathTemp = folder + '\\final\TEMP.csv'
        temperature.append(pandas.read_csv(pathTemp))
        data.get(folder).midterm.tempData.append(pandas.read_csv(pathTemp))

    dict.get('').

    print(temperature)


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
