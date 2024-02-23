import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Read the data from CSV file into a DataFrame
df = pd.read_csv('email.csv')

# Checking for missing or duplicate values
df.drop_duplicates(inplace=True)

# Divide the data into training and test
x_train, x_test, y_train, y_test = train_test_split(df["Message"], df["Category"], test_size=0.2, random_state=42)

# Vectorize the data
cv = CountVectorizer()
x_train_vectorized = cv.fit_transform(x_train)
x_test_vectorized = cv.transform(x_test)

# KNN Classifier
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(x_train_vectorized, y_train)
y_pred_knn = classifier.predict(x_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred_knn)
print('Accuracy: %.2f' % (accuracy * 100))

# Confusion Matrix for KNN
cm_knn = confusion_matrix(y_test, y_pred_knn)

# Display the Confusion Matrix using Seaborn heatmap
sns.heatmap(cm_knn, annot=True, cmap="Blues", fmt="d")
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix - KNN')
plt.show()
