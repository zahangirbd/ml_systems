import mlflow
# import numpy
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

db = load_diabetes()
# type(db)
# db.feature_names # return list - The names of the dataset columns.

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
# numpy.savetxt("diabetes_X_test.csv", X_test, delimiter=",")

model = mlflow.sklearn.load_model("runs:/343672f2f93a416f8c4764192244fc86/model")
predictions = model.predict(X_test)

print(predictions)
