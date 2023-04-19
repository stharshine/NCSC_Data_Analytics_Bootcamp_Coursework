# Alphabet Soup Charity Analysis Charity Funding Predictor


## Sections
- [Overview and Purpose of the Analysis](Overview-and-Purpose-of-the-Analysis)
- [Results from Analysis](Results-from-Analysis)
- [Summary of Analysis](Summary-of-Analysis)

# Overview and Purpose of the Analysis
The nonprofit foundation Alphabet Soup wants a tool that can help it select the applicants for funding with the best chance of success in their ventures. 
By using a binary classifier, I was able to support them predict whether applicants will be successful if funded by Alphabet Soup.


# Results from Analysis

## Data Preprocessing

In all models, I started by deleting information that seemed irrelevant, to ensure variety of the models, I deleted different columns in each test.

For the original [model](https://github.com/stharshine/deep-learning-challenge/blob/main/Starter_Code.ipynb), I dropped the colums of NAME and EIN, which are both identification columns.

![image](https://user-images.githubusercontent.com/105055655/228674201-836acc46-4b6c-4869-90c4-d3d0115df967.png)

For the first [test](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation.ipynb), I dropped the column NAME.

![image](https://user-images.githubusercontent.com/105055655/228652968-a7882b8c-d509-4022-a5f5-503f9ff8f07f.png)

For the second [test](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation2.ipynb), I dropped the column EIN.

![image](https://user-images.githubusercontent.com/105055655/228653457-3f61a14a-72ca-4b25-851c-e21a8282bb16.png)

For the third [test](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation3.ipynb), I dopped the column CLASSIFICATION

![image](https://user-images.githubusercontent.com/105055655/228653801-f7338f6e-c3ba-4737-a7e4-371ded263aba.png)

For binning purposes, in the first test I utilised *APPLICATION TYPE* as I believed it would allow to improve the accuracy of the predictive model and utilised *NAME* instead.

For the analysis:

For the original [model](https://github.com/stharshine/deep-learning-challenge/blob/main/Starter_Code.ipynb),the target variable was labeled *IS_SUCCESSFUL* and has the value of 1 for yes and 0 for no. In addition, the *APPLICATION TYPE* value was used for binning. 

For the first [model](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation.ipynb), the target variable was labeled *IS_SUCCESSFUL* and has the value of 1 for yes and 0 for no. In addition, the *CLASSIFICATION* value was used for binning. 

For the second [model](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation2.ipynb),  the target variable was labeled *STATUS* and has the value of 1 for active and 0 for not active status. In addition, the *CLASSIFICATION* value was used for binning. 

For the third [model](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation3.ipynb), the target variable was labeled *STATUS* and has the value of 1 for active and 0 for not active status. In addition, the *ORGANIZATION* value (which describes the organization type) was used for binning. 

Categorical variables for each model were encoded by get_dummies() after checking to see if the binning was successful as they could have been removed due to the fact that thery were not the target nor the features


## Compiling, Training, and Evaluating the Model

For each of the neural network model, I selected 3 layers. To have a wider variety within the models, last two tests and the original model, contain the same number of hidden nodes per layers whilst the first model it contains 3 different ones.

![image](https://user-images.githubusercontent.com/105055655/228668663-db4f89e5-e895-4653-9e5b-926280cde526.png)
![image](https://user-images.githubusercontent.com/105055655/228668750-9c634391-0305-4f66-8ddf-ba67e2dfa2b7.png)

For the original model, 321 parametres were created, which provided an accuracy of 72% which was under the desired 75%.

![image](https://user-images.githubusercontent.com/105055655/228673991-10438c0f-8350-459f-854f-c67f16085ed6.png)

![image](https://user-images.githubusercontent.com/105055655/228674064-e49691b0-2166-4aee-bbb9-722aab31dcd7.png)


For the first model, 1226 parametres were created, which provided an accuracy of 72% which was under the desired 75%.

![image](https://user-images.githubusercontent.com/105055655/228673167-bf315cdb-259f-47ff-ba0f-efc216583bb7.png)

![image](https://user-images.githubusercontent.com/105055655/228673218-0eced910-f739-48bb-b3e6-554513c98d12.png)


To increase the performance of the modle, I changed the epochs from 100 to 50 and the layer nodes from 7-14-21 to 5-10-15.

For the second model, 1,941 parametres were created, which provided 100% of accuracy, proving itself to be the best model out of the three created.

![image](https://user-images.githubusercontent.com/105055655/228671172-85455ff6-d35b-4724-9ad0-b53d75add3bd.png)

![image](https://user-images.githubusercontent.com/105055655/228671216-71a903cd-4cd7-4167-904c-ebf997f07aa2.png)

For the third model, 1,591 parametres were created,  which provided an accuracy of 77%, well above the 75% target.

![image](https://user-images.githubusercontent.com/105055655/228671365-99507a63-9990-437b-8d03-b0ff35af5209.png)

![image](https://user-images.githubusercontent.com/105055655/228671428-fb17e528-c211-439e-8ff7-64b029dc35ab.png)

The last two models show that by changing the multiple layers, it is possible to achieve the target model perfomance.


# Summary of Analysis

The second [test](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation2.ipynb) optimised neural network trained models and achived 100% of the prediction accuracy with 0.019% of loss using a sequential model, with 3 hidden layers at 5, 10 and 15, neurons split and 50 training epochs.

To solve the same problem, I could have created an algorithm that automatically optimizes the model. 
Utilising different models apart from sequential would benefit as well. Maybe sigmoidal could be part of my next test. 

In addition, I believe that presenting multiple layers with lower hidden nodes can allow to accurately predict the information, as we can see with our best  performing model. By decreasing the number of epochs from 100 to 50 and the hidden nodes, the accuracy increased drastically.


To conclude, despite there are many more models which could be better suited at predicting whether applicants will be successful if funded by Alphabet Soup, I do belive my second [model](https://github.com/stharshine/deep-learning-challenge/blob/main/AlphabetSoupCharity_Optimzation/AlphabetSoupCharity_Optimzation2.ipynb) is the best and most accurate. 

