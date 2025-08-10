import streamlit as st
import joblib
import numpy as np
from streamlit_lottie import st_lottie
import requests

# Load model and scaler
ridge = joblib.load('ridge_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_rocket = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")

# Apply CSS styles with background image, overlay and glassmorphism container
st.markdown("""
<style>
/* Background image for whole app */
body, .stApp {
    background: url('https://img.freepik.com/premium-vector/blue-blurry-image-person-s-face_1065176-6288.jpg') no-repeat center center fixed;
    background-size: cover;
    color: #e0e0e0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Dark overlay so content is readable */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(20, 30, 48, 0.75);
    z-index: -1;
}

/* Glassmorphism container */
.main-content {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 30px 40px;
    max-width: 900px;
    margin: 30px auto;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f0f0f0;
}

/* Header styling */
h1 {
    text-align: center;
    font-weight: 900;
    font-size: 3rem;
    margin-bottom: 15px;
    text-shadow: 0 0 8px #72c6ef;
}

/* Input fields */
.stNumberInput>div>input, .stSelectbox>div>div>div>input {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    color: #fff;
    border: none;
    padding: 8px 12px;
    font-weight: 600;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-size: 1.2rem;
    border-radius: 25px;
    padding: 14px 36px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,114,255,0.6);
}

.stButton>button:hover {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
    box-shadow: 0 6px 20px rgba(0,198,255,0.8);
}

/* Lottie animation container */
.lottie-container {
    max-width: 350px;
    margin: 0 auto 20px auto;
    
}

/* Label styling */
label {
    color: #cce7ff !important;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Main content container start
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.title("Student Exam Score Predictor")

# Show rocket animation on top
if lottie_rocket:
    st_lottie(lottie_rocket, speed=1, height=180, key="rocket")

st.write("Enter student details to predict the exam score:")

# Numeric Inputs
Hours_Studied = st.number_input('Hours Studied', min_value=0, max_value=100, value=10)
Attendance = st.number_input('Attendance (%)', min_value=0, max_value=100, value=80)
Sleep_Hours = st.number_input('Sleep Hours per day', min_value=0, max_value=24, value=7)
Previous_Scores = st.number_input('Previous Scores', min_value=0, max_value=100, value=60)
Tutoring_Sessions = st.number_input('Number of Tutoring Sessions', min_value=0, max_value=20, value=0)
Physical_Activity = st.number_input('Physical Activity (hours per week)', min_value=0, max_value=20, value=3)

# Categorical Inputs
Parental_Involvement = st.selectbox('Parental Involvement', ['High', 'Medium', 'Low'])
PI_Low = 1 if Parental_Involvement == 'Low' else 0
PI_Medium = 1 if Parental_Involvement == 'Medium' else 0

Access_to_Resources = st.selectbox('Access to Resources', ['High', 'Medium', 'Low'])
AR_Low = 1 if Access_to_Resources == 'Low' else 0
AR_Medium = 1 if Access_to_Resources == 'Medium' else 0

Extracurricular_Activities_Yes = 1 if st.radio('Extracurricular Activities', ['No', 'Yes']) == 'Yes' else 0

Motivation_Level = st.selectbox('Motivation Level', ['High', 'Medium', 'Low'])
Motivation_Low = 1 if Motivation_Level == 'Low' else 0
Motivation_Medium = 1 if Motivation_Level == 'Medium' else 0

Internet_Access_Yes = 1 if st.radio('Internet Access', ['No', 'Yes']) == 'Yes' else 0

Family_Income = st.selectbox('Family Income', ['High', 'Medium', 'Low'])
FI_Low = 1 if Family_Income == 'Low' else 0
FI_Medium = 1 if Family_Income == 'Medium' else 0

Teacher_Quality = st.selectbox('Teacher Quality', ['High', 'Medium', 'Low'])
TQ_Low = 1 if Teacher_Quality == 'Low' else 0
TQ_Medium = 1 if Teacher_Quality == 'Medium' else 0

School_Type_Public = 1 if st.radio('School Type', ['Private', 'Public']) == 'Public' else 0

Peer_Influence = st.selectbox('Peer Influence', ['Positive', 'Neutral', 'Negative'])
PI_Neutral = 1 if Peer_Influence == 'Neutral' else 0
PI_Positive = 1 if Peer_Influence == 'Positive' else 0

Learning_Disabilities_Yes = 1 if st.radio('Learning Disabilities', ['No', 'Yes']) == 'Yes' else 0

Parental_Education_Level = st.selectbox('Parental Education Level', ['Less than High School', 'High School', 'Postgraduate', 'Bachelor'])
PE_HighSchool = 1 if Parental_Education_Level == 'High School' else 0
PE_Postgraduate = 1 if Parental_Education_Level == 'Postgraduate' else 0

Distance_from_Home = st.selectbox('Distance from Home', ['Far', 'Moderate', 'Near', 'Very Far'])
DFH_Moderate = 1 if Distance_from_Home == 'Moderate' else 0
DFH_Near = 1 if Distance_from_Home == 'Near' else 0

Gender_Male = 1 if st.radio('Gender', ['Female', 'Male']) == 'Male' else 0

# Prepare feature array in EXACT order of training data columns
features = np.array([[Hours_Studied, Attendance, Sleep_Hours, Previous_Scores,
                      Tutoring_Sessions, Physical_Activity,
                      PI_Low, PI_Medium,
                      AR_Low, AR_Medium,
                      Extracurricular_Activities_Yes,
                      Motivation_Low, Motivation_Medium,
                      Internet_Access_Yes,
                      FI_Low, FI_Medium,
                      TQ_Low, TQ_Medium,
                      School_Type_Public,
                      PI_Neutral, PI_Positive,
                      Learning_Disabilities_Yes,
                      PE_HighSchool, PE_Postgraduate,
                      DFH_Moderate, DFH_Near,
                      Gender_Male]])

# Scale features
features_scaled = scaler.transform(features)

if st.button('Predict Exam Score'):
    prediction = ridge.predict(features_scaled)
    st.success(f'Predicted Exam Score: {prediction[0]:.2f}')

# Close main content container
st.markdown('</div>', unsafe_allow_html=True)
