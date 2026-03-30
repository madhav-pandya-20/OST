import matplotlib.pyplot as plt

models = ['XGB', 'RF', 'KNN', 'DT', 'SVM', 'NB']
accuracy = [85.93, 84.06, 80.36, 78.41, 78.19, 66.03]

plt.figure()
plt.bar(models, accuracy)
plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.title("Model Comparison")
plt.show()