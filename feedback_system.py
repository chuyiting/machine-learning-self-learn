import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt

from data_generator import MedicalDataType, DATABASE_FILE_PATH


class RegressionLine:
    def __init__(self, regressor):
        self._regressor = regressor

    def __init__(self, regressor, x_train, y_train, medical_type):
        self._regressor = regressor
        self._x_train = x_train
        self._y_train = y_train
        self._medical_type = medical_type

    def predict(self, x):
        to_be_predicted = np.array([
            [x]
        ])
        return self._regressor.predict(to_be_predicted)

    def show(self):
        viz_train = plt
        viz_train.ylim(0, 10)
        viz_train.scatter(self._x_train, self._y_train, color='red')  # scattered data
        viz_train.plot(self._x_train, regressor.predict(self._x_train), color='blue')  # regression line
        viz_train.title('Medical Information VS Treatment (Training set)')
        viz_train.xlabel(self._medical_type.value)
        viz_train.ylabel('Treatment')
        viz_train.show()


# Initialize column list
data_col_list = MedicalDataType.list()

# Importing the dataset
dataset = pd.read_csv(DATABASE_FILE_PATH, usecols=data_col_list)

# Create regressors
regression_lines = {}
y = dataset.iloc[:, -1].values.reshape(-1, 1)

for medical_info in MedicalDataType:
    X = dataset[medical_info.value].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 10, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    regression_lines[medical_info] = RegressionLine(regressor, X_train, y_train, medical_info)


def view_training_result():
    # Visualizing the Training set results
    for medical_info in MedicalDataType:
        regression_lines[medical_info].show()


if __name__ == '__main__':
    view_training_result()
