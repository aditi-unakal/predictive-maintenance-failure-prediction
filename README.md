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

---

## Exploratory Data Analysis

Exploratory data analysis was performed to better understand feature distributions, relationships between variables, and potential patterns associated with machine failure.

Key observations from the analysis include:

- The dataset contains both categorical and numerical features relevant to machine operating conditions.
- Features such as **torque, rotational speed, and tool wear** show noticeable variation between failure and non-failure cases.
- Correlation analysis helped identify relationships between numerical variables.
- Distribution plots were used to detect outliers and understand feature behavior.

### Feature Distribution Example
<img width="562" height="432" alt="image" src="https://github.com/user-attachments/assets/818e8d3b-32c1-4cde-ba95-d466b2d51ad4" />


### Correlation Heatmap

<img width="800" height="665" alt="image" src="https://github.com/user-attachments/assets/6647e541-b5a2-4306-b4c1-83447bec99ad" />

---

## Data Preprocessing

To ensure robust model training and prevent data leakage, preprocessing was integrated directly into the machine learning pipeline.

The preprocessing workflow included:

- **Train-test splitting** using an 80:20 ratio with stratification to preserve class distribution.
- **Categorical encoding** of the `Type` feature using one-hot encoding.
- **Numerical feature passthrough** for continuous operational variables.
- Integration of preprocessing and model training into a unified pipeline using `ColumnTransformer` and `Pipeline`.

This approach ensures that the same preprocessing steps are consistently applied during both training and prediction.

---

## Model Comparison

Three machine learning classification models were evaluated for predictive maintenance failure detection.

Given the imbalanced nature of the dataset, evaluation focused not only on overall accuracy but also on the model’s ability to correctly detect failure cases.

| Model | Accuracy | Precision (Failure) | Recall (Failure) | F1-score (Failure) |
|------|---------:|-------------------:|----------------:|------------------:|
| Logistic Regression | 96.2% | 0.48 | 0.75 | 0.58 |
| Random Forest | 98.6% | 0.96 | 0.61 | 0.75 |
| XGBoost | 99.1% | 0.89 | 0.82 | 0.85 |

Among the evaluated models, **XGBoost achieved the best balance between accuracy, precision, and recall**, making it the final model selected for deployment.

---

## Model Explainability with SHAP

To improve model interpretability, **SHAP (SHapley Additive exPlanations)** was used to analyze the contribution of individual features to the XGBoost model’s predictions.

SHAP helps explain how each feature influences the prediction outcome, making the model more transparent rather than functioning as a complete black box.

Key insights from SHAP analysis:

- **Torque** emerged as the most influential feature in predicting machine failure.
- **Tool wear** also showed strong contribution to prediction outcomes.
- **Air temperature, rotational speed, and process temperature** demonstrated meaningful influence on model behavior.
- Encoded machine type features had comparatively lower impact.
  
This explainability analysis improves trust in the predictive maintenance model by providing insight into the reasoning behind predictions.

### SHAP Summary Plot
<img width="783" height="459" alt="image" src="https://github.com/user-attachments/assets/1cbe4934-df74-48c2-9113-b43ee65ee88c" />

---

---

## Streamlit Web Application

To make the predictive maintenance model interactive and accessible, a **Streamlit web application** was developed for real-time machine failure prediction.

The application allows users to:

- Select machine type
- Enter operational parameters such as temperature, torque, rotational speed, and tool wear
- Receive machine failure predictions instantly
- View prediction confidence (failure probability)
- Receive warnings when input values fall outside the model’s training data range

This deployment demonstrates the practical application of the trained machine learning model beyond notebook experimentation.

### Application Interface

<img width="902" height="644" alt="image" src="https://github.com/user-attachments/assets/1f8c4944-b102-46aa-84cd-670d2ba5fab9" />

