import os
from typing import Dict, List
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
                extracted_data[data_type] = pd.read_csv(path_to_data, header=None)
            exam_list[exam_path] = Exam(extracted_data[data_types[0]], extracted_data[data_types[1]])
        new_student = Student(exam_list['Midterm 1'], exam_list['Midterm 2'], exam_list['Final'])
        students[path] = new_student

    return students


def rename_dict_keys(new_keys, original_dict: dict):
    student_key = new_keys
    key_count = 0
    for key in original_dict.keys():
        new_key = student_key[key_count]
        original_dict[new_key] = original_dict.pop(key)
        key_count += 1


def read_and_create_datasets(datasets) -> Dict[str, Student]:
    data_path = os.path.join(os.getcwd(), "data")
    student_paths = [f.path for f in os.scandir(data_path) if f.is_dir()]
    students = extract_exam_data(['Final', 'Midterm 1', 'Midterm 2'], student_paths, datasets)
    rename_dict_keys(['S1', 'S10', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9'], students)

    return students
