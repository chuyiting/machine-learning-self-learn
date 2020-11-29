import csv
import random
import abc
import os
from enum import Enum


DATABASE_PATH = 'data'
DATABASE_FILE_PATH = DATABASE_PATH + '/data.csv'


class MedicalDataType(Enum):
    TYPE_1 = "DATA1"
    TYPE_2 = "DATA2"
    TYPE_3 = "DATA3"
    TYPE_4 = "DATA4"
    TYPE_5 = "DATA5"
    TYPE_6 = "DATA6"
    TYPE_7 = "DATA7"
    TYPE_8 = "DATA8"
    TYPE_9 = "DATA9"
    TYPE_10 = "DATA10"
    TREATMENT = "Treatment"

    @staticmethod
    def list():
        return list(map(lambda mdt: mdt.value, MedicalDataType))


class RandomNumberGenerator(abc.ABC):
    @abc.abstractmethod  # {2}
    def gen_random_num(self):
        pass


class Type1(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 100.0


class Type2(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 100.0


class Type3(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 60.0


class Type4(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 55.0


class Type5(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 200.0


class Type6(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 150.0


class Type7(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 100.0


class Type8(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 80.0


class Type9(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 70.0


class Type10(RandomNumberGenerator):
    def gen_random_num(self):
        return random.random() * 50.0


class Treatment(RandomNumberGenerator):
    def gen_random_num(self):
        return float(random.randint(1, 10))


# create database directory
if not os.path.exists(DATABASE_PATH):
    os.makedirs(DATABASE_PATH)

# create the csv file database
with open(DATABASE_FILE_PATH, mode='a') as patient_file:
    patient_file.truncate()  # clean up the data

with open(DATABASE_FILE_PATH, mode='w') as patient_file:
    patient_writer = csv.writer(patient_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    headings = []
    for medical_info in MedicalDataType:
        headings.append(medical_info.value)
    patient_writer.writerow(headings)

    # generate fake patient data
    for i in range(0, 10):
        patient_writer.writerow([Type1().gen_random_num(), Type2().gen_random_num(), Type3().gen_random_num(),
                                 Type4().gen_random_num(), Type5().gen_random_num(), Type6().gen_random_num(),
                                 Type7().gen_random_num(), Type8().gen_random_num(), Type9().gen_random_num(),
                                 Type10().gen_random_num(), Treatment().gen_random_num()])
