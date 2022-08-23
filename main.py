import matplotlib.pyplot as plt
import pandas as pd

from ExamStressFunctions import read_and_create_datasets

if __name__ == '__main__':
    student_datasets = read_and_create_datasets(['TEMP.csv', 'EDA.csv'])

    max_length = max(len(student_datasets['S1'].final.tempData), len(student_datasets['S2'].final.tempData))
    print(max_length)

    dataframe_data = [[student_datasets['S1'].final.tempData], [student_datasets['S2'].final.tempData], [student_datasets['S3'].final.tempData], [student_datasets['S4'].final.tempData], [student_datasets['S5'].final.tempData], [student_datasets['S6'].final.tempData], [student_datasets['S7'].final.tempData], [student_datasets['S8'].final.tempData], [student_datasets['S9'].final.tempData], [student_datasets['S10'].final.tempData]]
    temperature = pd.DataFrame(data=dataframe_data)
    # columns=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6', 'Student 7', 'Student 8', 'Student 9', 'Student 10']
    # temperature.drop(index=temperature.index[:2], axis=0, inplace=True)
    print(temperature)
    plt.plot(temperature)
    plt.show()
    # Visualiser data enkeltvis
    # Make folder to save the visualisations in (REMEMBER TO SAVE)

    # put the datacontainers in a Python Project (top right corner of pycharm, right click ExamStressAnalysis --> new -->
    # python package )
    # then right click on the new package --> new --> python class
    pass