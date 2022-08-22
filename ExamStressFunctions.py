import os
from typing import Dict
import pandas as pd
from ExamStressClasses import Exam, Student


def extract_exam_data(exam_type, student_paths, data_types):
    students: Dict[str, Student] = dict()
    for path in student_paths:
        exam_list = {}
        extracted_data = {}

        for exam_path in exam_type:
            for data_type in data_types:
                path_to_data = os.path.join(path, exam_path, data_type)
                extracted_data[data_type] = pd.read_csv(path_to_data)
            exam_list[exam_path] = Exam(extracted_data[data_types[0]], extracted_data[data_types[1]])
        new_student = Student(exam_list['Midterm 1'], exam_list['Midterm 2'], exam_list['Final'])
        students[path] = new_student

    # print(students[student_paths[1]].final.edaData)
    return students


def rename_dict_keys(new_keys, old_keys, original_dict):
    student_key = new_keys
    key_count = 0
    for key in old_keys:
        new_key = student_key[key_count]
        original_dict[new_key] = original_dict.pop(key)
        key_count += 1
