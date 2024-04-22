import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the existing dataset
existing_data = pd.read_csv('C:\\Users\\solva\\Desktop\\Health Compus\\student_health_data.csv')

def home_page():
    st.title("Health Compass")
    
    st.markdown("""
    A big change in the approach towards student health is happening where it is getting proactive and data-driven nowadays. 
    Students are concerned with different types of health issues including seasonal diseases, allergies, and drug adherence. 
    In most cases, traditional reactive healthcare systems lack information that students desperately need.
    """)
    
    st.markdown("""
    **Overview of Health Compass Project:**
    - **Individualized Healthcare:** A growing focus on making medical care more suitable for individuals. Health Compass echoes this trend by giving personalized insights from anonymous data analysis.
    - **Technology as a means of managing health:** Research has shown the positive effects of technology on health management. By providing data-based insights and self-management tools for students, Health Compass empowers them.
    - **Significance of community backup:** Psychosocial support is important in maintaining wellness. On the other hand interactive features within the Health Compass may just promote individual welfare.
    - **Student health:** Universities recognize how important student wellness is and are taking measures to enhance it. In line with this, Health Compass offers focused interventions aimed at improving the health of students.
    """)
    
    st.markdown("""
    Health Compass' valid solution for universities that aim to enhance their student’s state of health can thus be seen from this point of view.
    """)
    
    st.markdown("### Navigate to Different Pages:")
    
    # Arrange buttons horizontally
    col1, col2, col3, col4, col5 = st.columns(5)
    
    if col1.button("Seasonal Disease Prediction", key="seasonal_disease"):
        seasonal_disease_prediction()
        
    if col2.button("Allergies Prediction", key="allergies"):
        allergies_prediction()
        
    if col3.button("Food Poisoning Prediction", key="food_poisoning"):
        food_poisoning_prediction()
        
    if col4.button("Input Form", key="input_form"):
        input_form_page()
        
    if col5.button("Analysis", key="analysis"):
        analysis_page()

def about_page():
    st.title("About Health Compass Project")
    
    st.markdown("""
    The Health Compass project is a proactive and data-driven initiative aimed at improving student health. It leverages data analytics and technology to provide personalized insights and interventions for students.
    """)
    
    st.markdown("""
    **Mission:** Our mission is to empower students to take control of their health and well-being through data-driven insights and interventions.
    """)
    
    st.markdown("""
    **Vision:** We envision a future where every student has access to personalized healthcare solutions that enhance their overall wellness and academic success.
    """)
    
    st.markdown("""
    **Values:**
    - Data-driven: We believe in the power of data to drive informed decision-making and improve health outcomes.
    - Student-centric: We prioritize the needs and preferences of students in designing our interventions.
    - Collaboration: We foster collaboration between students, healthcare professionals, and technology experts to create innovative solutions.
    - Privacy and security: We are committed to protecting the privacy and security of student data through strict adherence to ethical standards and regulations.
    """)
    
    st.markdown("""
    **Team:** The Health Compass project is led by a multidisciplinary team of healthcare professionals, data scientists, and technology experts dedicated to advancing student health.
    """)

def input_form_page(existing_data=None):
    st.header('Medical Form')

    # Define the form inputs
    timestamp = st.text_input('Timestamp', value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=1, max_value=100, value=25)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    height = st.text_input('Height (in CMs/ Inches)')
    weight = st.text_input('Weight (in KGs)')
    wear_spectacles = st.selectbox('Do You Wear Spectacles?', ['Yes', 'No'])
    food_preference = st.selectbox('Food Preference', ['Vegetarian', 'Non-Vegetarian', 'Vegan'])
    visited_hospital = st.selectbox('Have you visited CU hospital recently?', ['Yes', 'No'])
    purpose_hospital = st.text_input('Purpose of visiting hospital')
    referred_hospital = st.selectbox('Were you referred to Another Hospital ?', ['Yes', 'No'])
    helped_by_cu_hospital = st.selectbox('Has CU hospital helped you?', ['Yes', 'No'])
    medical_leave = st.selectbox('Have you received medical leave from cu hospital?', ['Yes', 'No'])
    hours_sleep = st.number_input('How many hours do you sleep in a day?', min_value=0, max_value=24, value=8)
    mentally_exhausted = st.selectbox('Do you feel mentally exhausted sometimes?', ['Yes', 'No'])
    mental_health = st.slider('Rate your mental health on a scale of 1 to 5', 1, 5, 3)
    need_mental_relaxation = st.selectbox('Do you need Mental Relaxation Sessions', ['Yes', 'No'])
    blood_group = st.selectbox('Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=22.0)

    # Create a new DataFrame for the input data
    new_data = pd.DataFrame({
        'Timestamp': [timestamp],
        'Name': [name],
        'Age': [age],
        'Gender': [gender],
        'Height': [height],
        'Weight': [weight],
        'Wear Spectacles': [wear_spectacles],
        'Food Preference': [food_preference],
        'Visited Hospital': [visited_hospital],
        'Purpose Hospital': [purpose_hospital],
        'Referred Hospital': [referred_hospital],
        'Helped by CU Hospital': [helped_by_cu_hospital],
        'Medical Leave': [medical_leave],
        'Hours Sleep': [hours_sleep],
        'Mentally Exhausted': [mentally_exhausted],
        'Mental Health': [mental_health],
        'Need Mental Relaxation': [need_mental_relaxation],
        'Blood Group': [blood_group],
        'BMI': [bmi]
    })

    # Submit button
    if st.button('Submit'):
        # Concatenate the new data with existing data
        if existing_data is None:
            existing_data = new_data
        else:
            existing_data = pd.concat([existing_data, new_data], ignore_index=True)

        # Write the updated data to the CSV file
        existing_data.to_csv('Updated Data set.csv', index=False)  # Assuming the CSV file is named 'user_credentials.csv'

        # Display the updated data
        st.write(existing_data)

    return existing_data


def seasonal_disease_prediction():
    st.header('Seasonal Disease Prediction')

    # Convert 'Timestamp' to datetime format
    existing_data['Timestamp'] = pd.to_datetime(existing_data['Timestamp'])

    # Extract month from Timestamp
    existing_data['Month'] = existing_data['Timestamp'].dt.month

    # Map month numbers to month names for better visualization
    month_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 
                 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    existing_data['Month'] = existing_data['Month'].map(month_map)

    # Count occurrences of diseases for each month
    disease_counts_by_month = existing_data.groupby('Month')['Purpose of visiting hospital'].value_counts().unstack().fillna(0)

    # Plotting disease occurrences by month
    plt.figure(figsize=(12, 8))
    sns.heatmap(disease_counts_by_month, cmap='viridis', annot=True, fmt='g')
    plt.title('Disease Occurrences by Month')
    plt.xlabel('Purpose of visiting hospital')
    plt.ylabel('Month')
    # st.pyplot(plt)

    predicted_diseases = predict_diseases(existing_data)  # This function should return a dictionary mapping seasons to predicted diseases

    # Display the predicted diseases and precautions
    st.subheader('Predicted Diseases and Precautions by Season')
    for season in ['Spring', 'Summer', 'Autumn', 'Winter']:
        disease = predicted_diseases.get(season, "No prediction")
        st.write(f"{season}, Predicted Disease: {disease}")
        # Add precautions based on the predicted disease
        if disease == 'Flu':
            st.write("Precautions: Get vaccinated, wash hands frequently, avoid close contact with sick individuals, cover mouth and nose when sneezing or coughing.")
        elif disease == 'Allergies':
            st.write("Precautions: Keep windows closed during high pollen seasons, use air purifiers, avoid outdoor activities on high pollen days.")
        elif disease == 'Common Cold':
            st.write("Precautions: Washing your hands, Avoiding touching your face, Cleaning frequently used surfaces, Using hand sanitizers, Strengthening your immune system and Staying home.\n suggested medicines:  aspirin, ibuprofen and naproxen.")
        elif disease == 'Dehydration':
            st.write("Precautions: Drink plenty of water, Eat foods with high amounts of water like fruits and vegetables, Avoid or limit drinks with caffeine like coffee, teas and soft drinks and Avoid or limit drinks with alcohol.")
        elif disease == 'Fever':
            st.write("Precautions: Limiting exposure to infectious agents, Drink plenty of fluids to stay hydrated, Dress in lightweight clothing, Use a light blanket if you feel chilled, until the chills end.")

# Function to predict diseases based on analyzed data
def predict_diseases(data):
    # Perform analysis on the data to predict diseases for each season
    # This function should return a dictionary mapping seasons to predicted diseases
    predicted_diseases = {}
    # Example: Predicting flu for the winter season
    predicted_diseases['Spring'] = 'Allergies'
    predicted_diseases['Summer'] = 'Dehydration'
    predicted_diseases['Autumn'] = 'Fever'
    predicted_diseases['Winter'] = 'Common Cold'
    return predicted_diseases


def allergies_prediction():
    st.header('Allergies Prediction')

    # Analyze the existing data to identify patterns or correlations
    predicted_allergies = predict_allergies(existing_data)  # This function should return a list of predicted allergies

    # Display the predicted allergies and precautions
    st.subheader('Predicted Allergies and Precautions')
    if not predicted_allergies:
        st.write("No allergies predicted.")
    else:
        for allergy in predicted_allergies:
            st.write(f"Allergy: {allergy}")
            # Add precautions based on the predicted allergy
            if allergy == 'Peanuts':
                st.write("Precautions: Avoid eating peanuts and peanut-containing products.")
            elif allergy == 'Shellfish':
                st.write("Precautions: Avoid consuming shellfish, and be cautious of cross-contamination in cooking.")
            # Add precautions for other allergies

# Function to predict allergies based on analyzed data
def predict_allergies(data):
    # Perform analysis on the data to predict allergies

    # Define a list to store predicted allergies
    predicted_allergies = []

    # Check for potential allergies based on the data
    # Example: Check if there's a correlation between certain food items and hospital visits related to allergies
    # For demonstration purposes, let's assume that if a person visited the hospital due to allergies related to food, they may have an allergy to that food
    food_allergy_indicators = ['Peanuts', 'Shellfish', 'Eggs', 'Milk', 'Wheat', 'Soy', 'Fish', 'Tree Nuts']
    for indicator in food_allergy_indicators:
        if indicator in data['Purpose of visiting hospital'].values:
            predicted_allergies.append(indicator)

    # Return the predicted allergies
    return predicted_allergies




def food_poisoning_prediction():
    st.header('Food Poisoning Prediction')
    
    # Define the relevant columns for food poisoning prediction
    food_poisoning_columns = ['Purpose of visiting hospital', 'Food Preference']

    # Count occurrences of food poisoning for each reason of hospital visit and food preference
    food_poisoning_counts = existing_data.groupby(['Purpose of visiting hospital', 'Food Preference']).size().unstack(fill_value=0)

    # Plotting food poisoning occurrences by hospital visit reason and food preference
    plt.figure(figsize=(12, 8))
    sns.heatmap(food_poisoning_counts, cmap='Reds', annot=True, fmt='g')
    plt.title('Food Poisoning Occurrences by Hospital Visit Reason and Food Preference')
    plt.xlabel('Food Preference')
    plt.ylabel('Purpose of visiting hospital')
    # st.pyplot(plt)

    predicted_food_poisoning = predict_food_poisoning(existing_data)  # This function should return a list of predicted food poisoning cases

    # Display the predicted food poisoning cases and precautions
    st.subheader('Predicted Food Poisoning Cases')
    if not predicted_food_poisoning:
        st.write("No food poisoning cases predicted.")
    else:
        for case in predicted_food_poisoning:
            st.write(f"Food Poisoning Case: {case}")
            # Add precautions based on the predicted food poisoning case
            if case == 'Raw Meat':
                st.write("Precautions: Ensure meat is thoroughly cooked before consumption.")
            elif case == 'Contaminated Water':
                st.write("Precautions: Drink only bottled or boiled water.")
            # Add precautions for other food poisoning cases

# Function to predict food poisoning cases based on analyzed data
def predict_food_poisoning(data):
    # Perform analysis on the data to predict food poisoning cases
    # This function should return a list of predicted food poisoning cases
    predicted_food_poisoning = []  # Placeholder, replace with actual predictions
    return predicted_food_poisoning


import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

def analysis_page():
    st.header("Analysis Page")
    
    # Display summary statistics for numerical columns
    st.subheader("Summary Statistics for Numerical Columns")
    st.write(existing_data.describe())

    # Display distribution of numerical columns
    st.subheader("Distribution of Numerical Columns")
    numerical_columns = {
        'Age': 'Age',
        'Height': 'Height (in CMs/Inches)',
        'Weight': 'Weight (in KGs)',
        'How many hours do you sleep in a day?': 'Hours of Sleep',
        'Rate your mental health on a scale of 1 to 5': 'Mental Health Rating',
        'BMI': 'BMI'
    }
    for column, label in numerical_columns.items():
        fig, ax = plt.subplots()
        sns.histplot(existing_data[column], kde=True, ax=ax)
        ax.set_title(f"Distribution of {label}")
        st.pyplot(fig)

    # Display counts of categorical columns
    st.subheader("Counts of Categorical Columns")
    categorical_columns = {
        'Gender': 'Gender',
        'Do You Wear Spectacles?': 'Wear Spectacles',
        'Food Preference': 'Food Preference', 
        'Have you visited CU hospital recently?': 'Visited CU Hospital Recently',
        'Purpose of visiting hospital': 'Purpose of Hospital Visit',
        'Were you referred to Another Hospital ?': 'Referred to Another Hospital',
        'Has CU hospital helped you?': 'CU Hospital Helped You?', 
        'Have you received medical leave from cu hospital?': 'Received Medical Leave from CU Hospital?', 
        'Do you feel mentally exhausted sometimes?': 'Mental Exhaustion',
        'Do you need Mental Relaxation Sessions': 'Need Mental Relaxation Sessions',
        'Blood Group': 'Blood Group'
    }
    for column, label in categorical_columns.items():
        st.write(existing_data[column].value_counts().rename_axis(label).reset_index(name='Counts'))

    # Display correlation heatmap for numerical columns
    st.subheader("Correlation Heatmap for Numerical Columns")
    correlation_matrix = existing_data[list(numerical_columns.keys())].corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True, ax=ax)
    st.pyplot(fig)


# Sidebar navigation
st.sidebar.title('Navigation')
options = ['Home', 'About', 'Input Form', 'Predictions', 'Analysis']
selection = st.sidebar.radio('Go to', options)

# Page selection
if selection == 'Home':
    home_page()
elif selection == 'About':
    about_page()
elif selection == 'Input Form':
    input_form_page()
elif selection == 'Predictions':
    seasonal_disease_prediction()
    allergies_prediction()
    food_poisoning_prediction()
elif selection == 'Analysis':
    analysis_page()
