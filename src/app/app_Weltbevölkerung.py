import streamlit as st
#%%
st.title("Vorhersage der Weltbevölkerung")
#%%
"Autorin: Kathi Rinke"
#%%
from scipy.stats import linregress
import pandas as pd
df = pd.read_excel('/Users/kathi/Desktop/projects/biz_analytics_a_new_app/Daten_Weltbevölkerung_1960-2020_New.xls')
years = df['Jahr']
population = df['Weltbevölkerung']
regression_result = linregress(years, population)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept
def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result
desired_year = st.number_input('Jahr', value=2021)
prediction = scipy_model(desired_year)
prediction_rounded = round(prediction,2)
"Die Vorhersage der Weltbevölkerung für das ausgewählte Jahr ist:"
st.write(prediction_rounded)
"Millarden Einwohner weltweit"
#%%
st.subheader("Über das Modell und die Daten")
"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 1960 bis 2020."
"Es steht ein Datenpunkt pro Jahr zur Verfügung."
"Die Daten stammen aus der folgenden Quelle:"
"The World Bank Group, 2022"
#%%
#%%


