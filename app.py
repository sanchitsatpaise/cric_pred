import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn

# Set page configuration
st.set_page_config(page_title="IPL Win Predictor", page_icon="🏏")

# 1. Load the trained assets with Version Check
@st.cache_resource
def load_assets():
    try:
        pipe = joblib.load('pipe.pkl')
        teams = joblib.load('teams.pkl')
        cities = joblib.load('cities.pkl')
        return pipe, teams, cities
    except AttributeError as e:
        st.error(f"### Model Version Mismatch")
        st.write(f"Your model was saved with a newer version of scikit-learn than what is installed.")
        st.info(f"**Current Version:** {sklearn.__version__} | **Required:** 1.6.1")
        st.code("pip install scikit-learn==1.6.1")
        return None, None, None
    except Exception as e:
        st.error(f"Error loading files: {e}")
        return None, None, None

pipe, teams, cities = load_assets()

if pipe:
    st.title('IPL Win Probability Predictor')

    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Select Batting Team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

    selected_city = st.selectbox('Select Host City', sorted(cities))
    target = st.number_input('Target Score', min_value=1)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input('Current Score', min_value=0)
    with col4:
        overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
    with col5:
        wickets = st.number_input('Wickets Down', min_value=0, max_value=10)

    if st.button('Predict Probability'):
        # 2. Replicate Feature Engineering from your notebook
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets_left = 10 - wickets
        
        # Avoid division by zero
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # 3. Create input dataframe (Must match the ColumnTransformer order)
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'target_score': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # 4. Predict
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display Results
        st.markdown("---")
        st.header(f"Probability of {batting_team} winning: {round(win * 100)}%")
        st.progress(win)
        st.header(f"Probability of {bowling_team} winning: {round(loss * 100)}%")