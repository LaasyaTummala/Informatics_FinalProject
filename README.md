ABSTRACT:

This project focused on analyzing a Medical Patient No Show dataset to uncover insights into the factors influencing patient'S attendance or non-attendance for scheduled appointments. Through exploratory data analysis and predictive modeling, the study aimed to identify patterns and risk factors associated with no-show instances. The findings provided valuable information on patient demographics, scheduling practices, and communication strategies, offering healthcare providers actionable recommendations to optimize appointment scheduling, enhance communication methods, and ultimately reduce no-show rates. This project contributes to improving resource utilization and efficiency in healthcare delivery by addressing the challenges posed by patient no-shows.


Data Description:

110.527 medical appointments its 14 associated variables (characteristics). 

Independent Variable: 
    PatientId: Identification of a patient
    AppointmentID: Identification of each appointment
    Gender: Male or Female
    ScheduledDay: The day of the actuall appointment
    AppointmentDay: The day someone called or registered the appointment
    Age: Pateint's day
    Neighbourhood: Where the appointment takes place.
    Scholarship:  1 or 0
    Hipertension: 1 or 0
    Diabetes:  1 or 0
    Alcoholism: 1 or 0
    Handcap: 1 or 0
    SMS_received:  1 or 0

Dependent Variable:
    No-show: Yes or No

The data extracted and cleaned includes:

    Patient ID: A unique identifier for each patient.
    Appointment ID: A unique identifier for each appointment.
    Gender: The patient's gender- Female or Male
    Appointment Date: The date of the scheduled appointment.
    Scheduling Date: The date the appointment was scheduled.
    Age: The patient's age.
    Neighborhood: The neighborhood where the appointment takes place.
    Scholarship: Whether or not the patient receives a scholarship.
    Hypertension: Whether or not the patient has hypertension. Changed the Coloumn name from "Hipertension" TO "Hypertension"
    Diabetes: Whether or not the patient has diabetes.
    Alcoholism: Whether or not the patient has alcoholism.
    Handicap: Whether or not the patient has a handicap.Changed the coloumn name from "Handcap" to "Handicap"
    SMS Received: Whether or not the patient received an SMS reminder about the appointment.
    NoShow: Whether or not the patient showed up for the appointment. Changed coloumn name from "No-show" to "NoShow"
The data was cleaned by removing missing values and outliers.


Algorithm Description:

1. **Load Data:**
   - Load patient data from the "PatientData.csv" file into a DataFrame.

2. **Feature Engineering:**
   - Select relevant features ('Age', 'Scholarship', 'Hypertension', 'Diabetes', 'Alcoholism', 'Handicap') and target variable ('NoShow').

3. **Train/Test Split:**
   - Split the data into training and testing sets (80% training, 20% testing).

4. **Model Training:**
   - Initialize a Random Forest Classifier with a specified random state.
   - Train the model using the training data.

5. **Streamlit App Setup:**
   - Configure Streamlit page settings, including title and icon.

6. **Streamlit App Layout:**
   - Create a Streamlit app layout with a title, description, and a two-column structure.
   - First column: Input widgets for user interaction (age, scholarship, hypertension, diabetes, alcoholism, handicap).
   - Second column: Display an image ("appointment.jpeg").

7. **User Input Section:**
   - Retrieve user input for features through Streamlit widgets.

8. **Prediction Section:**
   - When the user submits the form, create a DataFrame with the user's input.
   - Use the trained model to predict if the patient is likely to show up for the appointment.
   - Display a spinner during the prediction process.

9. **Prediction Results Section:**
   - Display the prediction results.
   - If predicted "No," show a success message indicating the patient is likely to show up.
   - If predicted "Yes," show an error message indicating the patient is unlikely to show up.

This algorithm represents the sequential flow of actions in the code, from loading data to making predictions and displaying the results in the Streamlit app.


Tools Used:

1. Streamlit (streamlit):

      Purpose: Streamlit is a Python library used for creating web applications with minimal code. In this project, Streamlit is employed to build an interactive web interface for the medical appointment no-show prediction model. It simplifies the process of turning data scripts into shareable web apps.


2.Pandas (pd):

      Purpose: Pandas is a powerful data manipulation and analysis library for Python. In this project, Pandas is used to read and manipulate the patient data from the "PatientData.csv" file. It provides data structures like DataFrame that are essential for organizing and analyzing tabular data.


3.scikit-learn (sklearn):

      Purpose: Scikit-learn is a machine learning library for Python that provides simple and efficient tools for data analysis and modeling, including classification, regression, clustering, and more. In this project, scikit-learn is used for:

4. train_test_split: To split the dataset into training and testing sets, which is crucial for evaluating model performance.

5. RandomForestClassifier: To create and train a random forest classifier model. Random Forest is an ensemble learning method that can be used for classification tasks.

6. accuracy_score: To evaluate the accuracy of the trained model by comparing predicted labels to true labels.
