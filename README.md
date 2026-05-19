# predictive-maintenance-failure-prediction
## Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**, which contains simulated industrial machine operational data for predictive maintenance analysis.

The dataset consists of **10,000 observations** and includes machine operating conditions, product characteristics, and failure indicators.

### Features Used for Prediction

The machine learning model uses the following input features:

- **Type** – Product quality type (`L`, `M`, `H`)
- **Air temperature [K]** – Ambient operating temperature
- **Process temperature [K]** – Internal process temperature
- **Rotational speed [rpm]** – Machine rotational speed
- **Torque [Nm]** – Applied torque
- **Tool wear [min]** – Accumulated tool wear over time

### Target Variable

- **Machine failure**
  - `0` → No machine failure
  - `1` → Machine failure

### Additional Failure Labels in Dataset

The dataset also contains specific failure mode indicators:

- **TWF** – Tool Wear Failure
- **HDF** – Heat Dissipation Failure
- **PWF** – Power Failure
- **OSF** – Overstrain Failure
- **RNF** – Random Failure

For this project, the primary prediction target is the overall **Machine failure** label.

## Class Imbalance Analysis
The target variable **Machine failure** is highly imbalanced, with significantly fewer failure cases compared to normal operating cases.
This imbalance is common in predictive maintenance scenarios, where machine failures are rare events compared to normal functioning.

To address this:

- **Stratified train-test splitting** was used to preserve the original class distribution in both training and testing datasets.
- Certain models, such as **Logistic Regression**, were trained using `class_weight='balanced'` to improve sensitivity toward the minority class.
- Model evaluation focused not only on accuracy but also on metrics such as **precision, recall, F1-score, and confusion matrix analysis**.
<img width="589" height="450" alt="image" src="https://github.com/user-attachments/assets/f1a3f694-d5eb-4586-81c5-99a2ba43300a" />
