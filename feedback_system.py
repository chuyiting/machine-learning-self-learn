import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from data_generator import MedicalDataType


class RegressionLine:
    def __init__(self, regressor):
        self._regressor = regressor

    def predict(self, x):
        to_be_predicted = np.array([
            [x]
        ])
        return self._regressor.predict(to_be_predicted)


# Initialize column list
data_col_list = MedicalDataType.list()

# Importing the dataset
dataset = pd.read_csv('data.csv', usecols=data_col_list)

# Create regressors
regression_lines = {}
y = dataset.iloc[:, -1].values.reshape(-1, 1)


for medical_info in MedicalDataType:
    X = dataset[medical_info.value].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 10, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    regression_lines[medical_info] = RegressionLine(regressor)

    # Visualizing the Training set results
    '''
    viz_train = plt
    viz_train.scatter(X_train, y_train, color='red')
    viz_train.plot(X_train, regressor.predict(X_train), color='blue')
    viz_train.title('Medical Information VS Treatment (Training set)')
    viz_train.xlabel(medical_info.value)
    viz_train.ylabel('Treatment')
    viz_train.show()
    '''
