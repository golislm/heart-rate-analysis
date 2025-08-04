#!/usr/bin/env python
# coding: utf-8

# # Heart Rate Analysis Project  
# 
# In this project, we analyze data collected from 91 undergraduate students to investigate the effects of various factors on heart rate.  
# 
# ### Background  
# The students were divided into two groups:  
# 1. One group ran in place for one minute.  
# 2. The other group remained still.  
# 
# We recorded several variables:  
# - **Height** and **Weight** (to be converted into metric units)  
# - **Gender**  
# - **Smoking status**  
# - **Activity level**  
# - **Pulse1**: resting heart rate measured before any activity  
# - **Pulse2**: heart rate after the activity (if applicable)  
# 
# ### Objectives  
# - Convert height (inches) and weight (pounds) into meters and kilograms.  
# - Calculate **BMI** for each individual.  
# - Perform descriptive statistics and data visualization.  
# - Explore how different factors (gender, smoking, activity, BMI) affect heart rate.  
# - Draw conclusions about the main factors influencing heart rate.  
# 

# # Step 1: Load the Data  
# First, we load the dataset to inspect its structure and content.
# 

# In[1]:


import pandas as pd

data = pd.read_csv("C:/Users/goli/OneDrive/Desktop/Job/Heart rate Analysis/heart_rate_data.csv", sep=';')
data.head()


# # Step 2: Data Overview  
# We check the basic information about the data including data types and missing values.
# 

# In[3]:


data.shape


# In[5]:


data.info()
data.isnull().sum()


# In[7]:


data.info()


# In[9]:


data.isnull().sum()


# # Step 3: Data Cleaning and Preprocessing  
# In this step, we convert height from inches to meters and weight from pounds to kilograms.  
# We also calculate BMI for each individual.

# In[12]:


# Convert height from inches to meters
data['Height_m'] = data['Height'].astype(float) * 0.0254

# Convert weight from pounds to kilograms
data['Weight_kg'] = data['Weight'].astype(float) * 0.453592

# Calculate BMI = Weight (kg) / Height (m)^2
data['BMI'] = data['Weight_kg'] / (data['Height_m'] ** 2)

data[['Height', 'Height_m', 'Weight', 'Weight_kg', 'BMI']].head()


# ### Step 4: Descriptive Statistics  
# 
# We use `data.describe()` to generate a statistical summary of all numerical columns in the dataset.  
# 
# - **count**: number of non-missing values  
# - **mean**: average of the values  
# - **std**: standard deviation (spread of the data)  
# - **min**: smallest value  
# - **25%**: 25th percentile (quarter of the data is below this)  
# - **50% (median)**: middle value of the data  
# - **75%**: 75th percentile (three-quarters of the data is below this)  
# - **max**: largest value  
# 

# In[15]:


data.describe()


# # Step 5: Exploratory Data Analysis (EDA)  
# Here we explore the distribution and relationships between variables such as BMI, pulse, gender, smoking status, and activity level.
# 

# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(data['BMI'], kde=True)
plt.title('BMI Distribution')
plt.show()

sns.boxplot(x='Gender', y='Pulse1', data=data)
plt.title('Pulse1 by Gender')
plt.show()


# 
# ### Initial Observations: BMI Distribution  
# 
# - Most participants have a **BMI around 20**, which is in the normal weight range.  
# - The majority of BMI values fall between **19 and 23**.  
# - The distribution is slightly skewed to the right, meaning there are a few participants with higher BMI values.  
# - The spread of the data is moderate, with no extreme outliers.### Initial Observations: Pulse1 by Gender  
# 
# - The boxplot shows that the median **resting heart rate (Pulse1)** is slightly higher in females than in males.  
# - The variability (IQR) is larger in females, meaning their resting pulse rates vary more.  
# - There is at least one outlier in the male group (a higher pulse rate than the rest).  
# - Overall, gender may have some influence on resting heart rate, but further statistical analysis is needed to confirm.  
#   
# e box.  
# 

# ### Pulse1 by Smoking Status  
# 
# We compare the resting heart rate (Pulse1) between smokers and non-smokers to see if smoking status influences heart rate.
# 

# In[22]:


sns.boxplot(x='Smokes', y='Pulse1', data=data)
plt.title('Pulse1 by Smoking Status')
plt.show()


# 
# ### Observations: Pulse1 by Smoking Status  
# 
# - The median **resting heart rate (Pulse1)** is higher in smokers compared to non-smokers.  
# - Smokers also show slightly more variability in their resting heart rate.  
# - This suggests that smoking may have a negative impact on resting heart rate, but further statistical tests are needed to confirm this.  
# 
# **Why is Pulse1 higher in smokers?**  
# 
# - Nicotine stimulates the sympathetic nervous system, increasing heart rate even at rest.  
# - Smoking reduces oxygen-carrying capacity, so the heart must beat faster to deliver enough oxygen.  
# - Long-term smoking puts extra strain on the cardiovascular system, which can lead to elevated resting heart rates.  
# 

# ### Pulse1 by Activity Level  
# 
# We compare the resting heart rate (Pulse1) among different self-reported activity levels  
# (Slight, Moderate, A lot) to see if physical activity habits influence heart rate.
# 

# In[26]:


sns.boxplot(x='Activity', y='Pulse1', data=data)
plt.title('Pulse1 by Activity Level')
plt.show()


# 
# ### Observations: Pulse1 by Activity Level  
# 
# - Participants with **Slight** activity levels have a higher median resting heart rate (Pulse1), slightly above 80 bpm.  
# - Those with **Moderate** and **A lot** activity levels show a lower median resting heart rate, around 70 bpm.  
# - This suggests that individuals with more regular physical activity tend to have a healthier, lower resting heart rate.  
# 
# ---
# 
# **Why is Pulse1 higher in low-activity participants?**  
# 
# - Regular physical activity strengthens the heart muscle, allowing it to pump more efficiently and at a lower rate.  
# - Individuals with little physical activity often have less cardiovascular fitness, leading to higher resting heart rates.  
# 

# ### Pulse1 vs BMI  
# We explore the relationship between BMI and resting heart rate.

# In[35]:


sns.scatterplot(x='BMI', y='Pulse1', data=data)
plt.title('Pulse1 vs BMI')
plt.show()


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
sns.boxplot(x='Activity', y='Pulse1', data=data)
plt.title('Resting Pulse (Pulse1) by Activity Level')
plt.xlabel('Activity Level')
plt.ylabel('Pulse1 (Resting Heart Rate)')
plt.show()


# ### 💓 Pulse1 by Activity Level
# 
# - Participants with **Slight** activity levels have a **higher** resting heart rate (Pulse1), slightly above **80 bpm**.
# - Participants with **Moderate** or **A lot** activity have **lower** Pulse1 values, around **70 bpm**.
# - 🏃‍♂️ This implies that individuals with more physical activity tend to have better cardiovascular health, leading to a lower resting heart rate.
# 
# 💡 **Why does this happen?**  
# Regular physical activity increases heart efficiency and lowers resting heart rate. Sedentary individuals typically have weaker cardiovascular systems.
# 

# In[38]:


plt.figure(figsize=(7, 5))
sns.boxplot(x='Ran', y='Pulse1', data=data, palette='Set2')
plt.title('Pulse1 by Ran Status')
plt.xlabel('Ran (Yes/No)')
plt.ylabel('Pulse1 (Resting Heart Rate)')
plt.show()


# ### 🏃‍♀️ Pulse1 by Ran (Effect of Light Exercise on Resting Heart Rate)
# 
# - Participants who were assigned to the **running group** (i.e., ran in place for one minute) show a **slightly elevated resting heart rate (Pulse1)** compared to those who remained still.
# - Although **Pulse1** is ideally measured before any physical exertion, the observed values suggest a subtle increase in those who were expected to run.
# - This difference may result from:
#   - Measurement timing being too close to the physical activity, causing residual cardiovascular stimulation.
#   - Differences in **baseline fitness levels**—individuals who are less fit may exhibit higher resting heart rates post minor exertion.
#   - Natural variability in heart rate due to other unmeasured factors such as stress, hydration, or prior sleep.
# 
# 💡 **Interpretation:**  
# While the effect is not strongly pronounced, the trend suggests that even light activity (such as 1-minute running in place) can influence **resting heart rate readings** if measured shortly after exertion. This highlights the importance of ensuring standardized conditions when collecting physiological data.
# 

# In[42]:


import statsmodels.formula.api as smf

model = smf.ols("Pulse2 ~ Pulse1 + BMI + C(Gender) + C(Smokes) + C(Activity) + C(Ran)", data=data).fit()
model.summary()


# ## Linear Regression Analysis
# 
# In this section, we use Ordinary Least Squares (OLS) regression to examine the effects of several factors on post-activity heart rate (`Pulse2`).
# 
# ### 🎯 Objective
# To model `Pulse2` based on the following predictors:
# - `Pulse1` (resting heart rate)
# - `BMI` (Body Mass Index)
# - `Gender` (categorical)
# - `Smokes` (categorical)
# - `Activity` level (categorical)
# - `Ran` (whether the subject ran in place for one minute)
# 
# ### 🧠 Assumptions of Linear Regression
# 1. A linear relationship exists between predictors and the response.
# 2. Residuals (errors) are normally distributed.
# 3. Homoscedasticity: constant variance of residuals.
# 4. Observations are independent.
# 5. No strong multicollinearity between predictors.
# 
# ### ⚙️ Model Specification
# We apply OLS regression. The general model is:
# 
# \[
# \text{Pulse2} = \beta_0 + \beta_1 \cdot \text{Pulse1} + \beta_2 \cdot \text{BMI} + \text{(Gender + Smokes + Activity + Ran)} + \epsilon
# \]
# 
# Categorical variables (e.g., Gender, Activity) are automatically encoded as dummy variables.
# 
# ### 📊 Key Outputs and Interpretation
# - **R-squared**: Percentage of variation in `Pulse2` explained by the model.
# - **p-values**: Indicate whether each predictor is statistically significant (typically, p < 0.05).
# - **Coefficients (coef)**: Show the estimated effect of each variable on `Pulse2`, holding others constant.
# - **Durbin–Watson**: Tests for autocorrelation in residuals (values close to 2 are ideal).
# - **Jarque–Bera and Omnibus tests**: Assess normality of residuals (p > 0.05 means normality is not rejected).
# - **Condition Number**: Checks for multicollinearity (high values suggest potential issues).
# 
# ### ✅ Conclusion
# By analyzing regression outputs, we identify which variables (e.g., running, smoking, activity level) most influence post-exercise heart rate. We also evaluate whether model assumptions are reasonably met.
# 
# In the next cells, we will present the regression results and diagnostic plots.
# 
