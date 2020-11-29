from data_generator import MedicalDataType
from feedback_system import regression_lines


def print_hi(name):
    print(f'Hi, {name}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    treatment_suggestion = None
    print_hi('this is David\n Please input the patient data:')
    for medical_info in MedicalDataType:
        medical_data = input(medical_info.name + ": ")
        regression_line = regression_lines[medical_info]
        print("Suggested treatment: " + str(regression_line.predict(int(medical_data))[0][0]))


