# Patient Care Classification System
- This project focuses on classifying patients into two categories: "In Care" and "Out Care." The classification is based on various health indicators provided in the dataset. The machine learning models used for classification include Decision Tree, Random Forest, and Logistic Regression.

## Dataset
- The dataset, named "PatientCare.csv," contains information about patients, including their gender, age, and various health parameters such as HAEMATOCRIT, HAEMOGLOBINS, ERYTHROCYTE, LEUCOCYTE, THROMBOCYTE, MCH, MCHC, and MCV.

## Preprocessing
- The gender information is mapped to numerical values (1 for Male, 0 for Female) to facilitate model training. Exploratory Data Analysis (EDA) is performed to visualize the distribution of data using count plots and distribution plots.

## Model Training
The dataset is split into training and testing sets, and three machine learning models are trained: Random Forest, and Adaboost . The accuracy of each model is evaluated using the test set.

## Streamlit Application
A Streamlit application is created to allow users to input their health parameters. The trained Random Forest model then predicts whether the user requires "In Care" (Hospitalization) or "Out Care" (Home Care). The user input and the model's prediction are displayed in the application.

## Instructions for Running the Streamlit App
- Install the required Python libraries: numpy, pandas, matplotlib, seaborn, streamlit, and scikit-learn.
- Clone the repository.
- Navigate to the project directory in the terminal.
- Run the Streamlit app using the command: streamlit run your_streamlit_app_filename.py.

- 
![stream1](https://github.com/inayatph/Patient-Care-Classification/assets/164138014/0688725c-f8a9-4821-9806-13142c280c23)


![stream2](https://github.com/inayatph/Patient-Care-Classification/assets/164138014/8ce8b46a-8374-4172-a3fb-c28fd8386bad)

