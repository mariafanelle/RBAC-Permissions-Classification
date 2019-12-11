import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

dataset = pd.read_csv('original_data/train.csv', sep=',', header=0)
data = dataset.iloc[:,:]

X = data.iloc[:, 1:9].values
y = dataset.iloc[:, 0].values
print(X)

# Encoding the predicting variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the data into test and train dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,\
                                        random_state=0)

# Print subset shapes
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)
print()

# Using the random forest classifier for the prediction
classifier = RandomForestClassifier()
classifier = classifier.fit(X_train, y_train)
predicted = classifier.predict(X_test)

# Printing the results
print('Confusion Matrix:')
print(confusion_matrix(y_test, predicted))
print('Accuracy Score:', accuracy_score(y_test, predicted))
print('Report:')
print(classification_report(y_test, predicted))
