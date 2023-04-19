### Module 12 Report
# Credit Risk Analysis Report

## Table of contents 

- [Overview of the Analysis](##Overview-of-the-Analysis)
- [Results](##-Results)
- [Summary](##-Summary)

## Overview of the Analysis

The purpose of this analysis is to evaluate a model based on loan risk using machine learning. It will be possible to determine which [loans](https://github.com/stharshine/credit-risk-classification/blob/main/Credit_Risk/Resources/lending_data.csv) are healthy or non-healthy.

The information given included a list of loans provided by the lending company and by using the logistic regression algorithm I predicted which were high risk and which were low risk.

Taking a look at the code and using the value_counts function, I can see that the data is highly imbalanced. The majority class is healthy loans [0] and the minority class is non-healthy loans [1]

<img width="160" alt="image" src="https://user-images.githubusercontent.com/105055655/226736880-a223a794-041e-4f01-8711-1216489c87f4.png">

And looking at the prediction model below, we can see that out of the loan statuses, 18 663 were predicted as healhty (low risk) correctly but 102 were predicted as unhealhty incorrectly. In addition, out of the non healthy loans,  563 were predicted correctly, whilst 56 were wrongfully predicted as healthy.

<img width="399" alt="image" src="https://user-images.githubusercontent.com/105055655/226737796-632cd7f0-6ee4-4512-b5af-4cb6d1a189ea.png">

[RandomOverSampler](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html) allowed to perform random oversampling. This means that the data was oversampled by picking samples at random, which added more copied of the non healthy loans (the minority class in this analysis) to balance the dataset, as you can see in the image before.


<img width="383" alt="image" src="https://user-images.githubusercontent.com/105055655/226739838-add36147-a0d3-4e5f-b330-9b058c6a4f07.png">

The [0] class is healthy loans and the [1] non-healthy loans.

Using the regression model again, we can see the prediction model below. As you can see, 18649 models were predicted as healthy correctly but 116 were predicted incorrectly. Compared to unhealthy loans in which 615 were predicted correctly whilst 4 were predicted mistakenly.

<img width="603" alt="image" src="https://user-images.githubusercontent.com/105055655/226741146-1330214a-3133-4322-8da4-b2f3548a8b88.png">



### Stages of the machine learning process ###

To get to the solution, I imported all the modules needed, which include numpy, pandas, pathlib and sklearn.
After reading the CSV and splitting the datasets into two variables for loan statuses (healthy and not healthy), I fitted them into the logistic regression model. 

<img width="418" alt="image" src="https://user-images.githubusercontent.com/105055655/226745554-4318878c-456d-4475-8dcc-f112fa7929d7.png">

Succequently, I generated a confusion matrix for the model, which is a table that is used in classification problems to assess where errors in the model were made.
In this case, it was used to figure out which loans were mistakenly assigned.

After analysis, I resampled the data as seen in the image below:
<img width="442" alt="image" src="https://user-images.githubusercontent.com/105055655/226746292-8283fefa-41bb-4cfd-84f5-391b1159e68c.png">

And then analysed the data using the regression model and the confusion matrix.


### Method Used ###

[Logistic Regression](https://realpython.com/logistic-regression-python/#logistic-regression-overview) is a classification technique which is quite uncomplicated and allows to interpret results easily. 
It allows to predict categorical outcomes, as we have seen in the images before.
It is called by using the Sklearn module
<img width="575" alt="image" src="https://user-images.githubusercontent.com/105055655/226744660-c62537ec-0064-43ab-8db1-44fe2a22996d.png">

As mentioned previously, I utilised the [confusion matrix](https://www.w3schools.com/python/python_ml_confusion_matrix.asp) to build a table to assess the erros of the model.

<img width="801" alt="image" src="https://user-images.githubusercontent.com/105055655/226746736-32b8950c-e8c9-42dc-a995-d5dc5aa7544f.png">

 This is the code to create the confusion matrix for the imbalanced original data.

<img width="784" alt="image" src="https://user-images.githubusercontent.com/105055655/226746818-41e5062f-432b-4b6b-a08d-7ed1f695196e.png">
 This is the code to create the confusion matrix for the balanced original data.

## Results

To understand the results, we must understand what Precision, Recall and F1 score means:

*Precision* score measures the proportion of true positives over the number of true positives + false positives 

*Recall* score measures the proposions of true positives over the number of true positives + false negatives 

*F1 score* measures the model's accuracy and it combines both the precision and recall scores.


For the Logistic regression model with imbalanced data: 

<img width="335" alt="image" src="https://user-images.githubusercontent.com/105055655/227020859-b69c269f-5468-4e35-aeb0-da50dbf22b35.png">

Looking at the image above, it is possible to see that the oversampled dataset predicted precisely 100% of the healthy loans whilst predicted the non healthy loans 85% of the time.
The recall score is lower (91%) for Non-Healthy loans expected since the number of mistakenly predicted scores for non-healthy is higher (9% of mistakes). Whilst making 1% of mistakes when predicting healthy loans.
F1 score is 100% for healthy loans whilst 88% for non-healhty which is as expected for the results.


For the Logistic regression model with oversampled data: 

<img width="393" alt="image" src="https://user-images.githubusercontent.com/105055655/227027635-e10a4366-04f0-467e-8ae9-cc8c5dd0c5aa.png">

Looking at the image above, it is possible to see that the oversampled dataset predicted precisely 100% of the healthy loans whilst predicted the non healthy loans 84% of the time.
The recall score is lower (99%) for Non-Healthy loans same as predicting healthy loans.
F1 score is 100% for healthy loans whilst 91% for non-healhty which is as expected for the results.



## Summary

For a lending company such as a bank, the type of model utilised should be as accurate as possible to predict the best outcomes for their customers.
This means predicting healthy loans as such and non-healthy, as such.

Looking at the data analysied, it is possible to say that the logistic regression with oversampled data (Model 2) produced a more accurate model, which included having higher accuracy and higher recall scores.
In contrary, imbalanced data (Model 1) showed to have innacurate prediction, especially for non healthy loans. This means that if a company relied on imbalanced data, they would lose money in the long term.

Performance has an impact on the issue that is being solved, since the model has to predict correctly the loans without causing the bank to lose money nor customers. Therefore there is no prioritisation whether the model should predict better healthy loans or non healthy. They both should be predicted accurately.

Therefore, Model 2, Logistic regression with oversampled data is the most ideal model and the one that lending companies should use. 
