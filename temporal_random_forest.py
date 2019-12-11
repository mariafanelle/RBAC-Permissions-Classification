import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn import tree

dataset = pd.read_csv('generated_data/training_with_dates.csv', header=0, sep=',')
data = dataset.iloc[:,:]

features = data.columns[1:17]
X = data.iloc[:, 1:17].values
y = dataset.iloc[:, 0].values

# Encoding the predicting variNoneable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the data into test and train dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,\
                                        random_state=0)

"""
# Print subset shapes
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)
print()
"""

# Use random forest classifier for the prediction
classifier = RandomForestClassifier(random_state=0)
classifierFit = classifier.fit(X_train, y_train)
predicted = classifierFit.predict(X_test)

# Print out feature importance
y = classifier.feature_importances_
fig, ax = plt.subplots()
width = 0.7
ind = np.arange(len(y))
ax.barh(ind, y, width, color="green")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(features, minor=False)

plt.title("Feature importance in RandomForest")
plt.xlabel("Relative importance")
plt.ylabel("Feature")
plt.figure(figsize=(5,5))
fig.set_size_inches(6.5,4.5,forward=True)
plt.show()

# Display the results
print('Confusion Matrix:')
print(confusion_matrix(y_test, predicted))
print('Accuracy Score:', accuracy_score(y_test, predicted))
print('Report:')
print(classification_report(y_test, predicted))
