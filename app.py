import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("predictive_maintenance_model.pkl")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: white;'>
⚙️ Predictive Maintenance AI Dashboard
</h1>
<p style='text-align: center; color: lightgray; font-size:18px;'>
Enter machine parameters to predict potential failure
</p>
""", unsafe_allow_html=True)

# # Title
# st.title("Predictive Maintenance Failure Prediction")
# st.write("Enter machine parameters to predict whether machine failure is likely.")


col1, col2 = st.columns(2)

with col1:
    machine_type = st.selectbox("Machine Type", ["L", "M", "H"])
    air_temp = st.number_input("Air Temperature [K]", 250.0, 400.0, 300.0)
    if not (295.3 <= air_temp <= 304.5):
        st.warning("Air temperature is outside training data range. Prediction may be less reliable.")
    rot_speed = st.number_input("Rotational Speed [rpm]", 0, 5000, 1400)
    if not (1168 <= rot_speed <= 2886):
        st.warning("Rotational speed is outside training data range. Prediction may be less reliable.")

with col2:
    process_temp = st.number_input("Process Temperature [K]", 305.0, 450.0, 310.0)
    if not (305.7 <= process_temp <= 313.8):
        st.warning("Process temperature is outside training data range. Prediction may be less reliable.")
    torque = st.number_input("Torque [Nm]", 0.0, 200.0, 55.0)
    if not (3.8 <= torque <= 76.6):
        st.warning("Torque is outside training data range. Prediction may be less reliable.")
    tool_wear = st.number_input("Tool Wear [min]", 0, 500, 180)
    if not (0 <= tool_wear <= 253):
        st.warning("Tool wear is outside training data range. Prediction may be less reliable.")

# # User inputs
# machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

# air_temp = st.number_input(
#     "Air Temperature [K]",
#     min_value=250.0,
#     max_value=400.0,
#     value=300.0
# )
# if not (295.3 <= air_temp <= 304.5):
#     st.warning("Air temperature is outside training data range. Prediction may be less reliable.")


# process_temp = st.number_input(
#     "Process Temperature [K]",
#     min_value=305.0,
#     max_value=450.0,
#     value=310.0
# )
# if not (305.7 <= process_temp <= 313.8):
#     st.warning("Process temperature is outside training data range. Prediction may be less reliable.")

# rot_speed = st.number_input(
#     "Rotational Speed [rpm]",
#     min_value=0,
#     max_value=5000,
#     value=1400
# )
# if not (1168 <= rot_speed <= 2886):
#     st.warning("Rotational speed is outside training data range. Prediction may be less reliable.")

# torque = st.number_input(
#     "Torque [Nm]",
#     min_value=0.0,
#     max_value=200.0,
#     value=55.0
# )
# if not (3.8 <= torque <= 76.6):
#     st.warning("Torque is outside training data range. Prediction may be less reliable.")

# tool_wear = st.number_input(
#     "Tool Wear [min]",
#     min_value=0,
#     max_value=500,
#     value=180
# )



# Predict button
if st.button("Predict Failure"):

    sample = pd.DataFrame({
        'Type': [machine_type],
        'Air temperature [K]': [air_temp],
        'Process temperature [K]': [process_temp],
        'Rotational speed [rpm]': [rot_speed],
        'Torque [Nm]': [torque],
        'Tool wear [min]': [tool_wear]
    })

    prediction = model.predict(sample)
    probability = model.predict_proba(sample)

    failure_probability = probability[0][1] * 100

    if prediction[0] == 1:
        st.error(f"Machine Failure Predicted")
        st.metric("Failure Probability", f"{failure_probability:.2f}%")
    else:
        st.success("No Failure Predicted")
        st.metric("Failure Probability", f"{failure_probability:.2f}%")