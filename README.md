# parkinson-telemonitoring-uci-dataset
<font color='87cefa'><b><h1>Project Title:</h1></font></b>
*Parkinson's Disease Severity Prediction using Machine Learning*

<font color='87cefa'><b><h1>Project Objective</h1></font></b>
*The objective of this project is to develop a machine learning model that can accurately predict the severity of Parkinson's disease in patients based on various voice and speech attributes. The model will be trained on the Parkinson's Disease Dataset, which contains a range of acoustic features that are indicative of the disease severity. The model's performance will be evaluated using various metrics such as accuracy, mean squared error, and R2 score. The ultimate goal of the project is to develop a reliable and accurate tool that can assist doctors in the early detection and diagnosis of Parkinson's disease, potentially leading to improved patient outcomes.*
<font color='87cefa'><b><h1>Data</h1></font></b>

*The Parkinsons Telemonitoring dataset is a collection of voice recordings and corresponding clinical information from individuals with Parkinson's disease. The dataset was collected using a telemonitoring platform that allowed patients to record their voice while performing simple tasks, such as sustained phonation and vowel phonation. The dataset contains <font color='green'><b>5875</font></b> voice recordings from <font color='green'><b>42</font></b>  individuals with Parkinson's disease and 24 healthy controls.*

link: 
https://archive.ics.uci.edu/ml/datasets/parkinsons+telemonitoring

<font color='pink'><b><h2> Data Exploration and Preprocessing:</h2></font></b> 


a.   Load the dataset and examine the columns, their data types,and any missing values.

b.   Check for any outliers and remove them if necessary.

c. Convert any categorical features to numerical features using one-hot encoding or label encoding.

d. Split the data into training and testing sets.

<font color='pink'><b><h2> visualization </h2></font></b> 

![Screenshot](https://github.com/amnaahmad20/parkinson-telemonitoring-uci-dataset/blob/main/data.png)
<font color='teal'><b><h1> Step 3</h1></font></b>

Model Selection and Training:

a. Choose a machine learning model appropriate for your problem.

b. Train the model on the training set.

c. Evaluate the performance of the model on the testing set using metrics such as
accuracy, precision, recall, and F1-score.


it indicates that the Random Forest Regression model has performed reasonably well on the Parkinson's dataset.

The high R-squared values for both the training and test sets (0.9991 and 0.9942, respectively) indicate that the model is able to explain a large proportion of the variance in the target variable, which is a good sign.

The mean squared error (MSE) for the test set (0.6630) is higher than the MSE for the training set (0.1032), which is expected as the model usually performs better on the data that it was trained on than on new, unseen data. However, the difference between the two MSE values is not very large, which suggests that the model is not overfitting the training data excessively.
