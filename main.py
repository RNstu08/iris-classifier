from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
data = load_iris()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Create the RandomForestClassifier model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Print the accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.model_selection import GridSearchCV

# Define the hyperparameters you want to tune
params = {'n_estimators': [10, 50, 100]}

# Set up GridSearchCV for cross-validation
clf = GridSearchCV(RandomForestClassifier(), params, cv=5)
clf.fit(X_train, y_train)

# Print the best hyperparameters and score
print("Best Parameters:", clf.best_params_)
print("Best Score:", clf.best_score_)


