import streamlit as st
import requests

def main():
    st.title("Model Prediction App")
    st.header("Enter Car Details")

    # Numeric inputs
    prod_year = st.number_input("Production Year", value=2020, step=1)
    mileage = st.number_input("Mileage", value=0.0, step=0.1)
    cylinders = st.number_input("Cylinders", value=4, step=1)
    airbags = st.number_input("Airbags", value=2, step=1)

    # Boolean inputs using checkboxes
    fuel_cng = st.checkbox("Fuel CNG")
    fuel_diesel = st.checkbox("Fuel Diesel")
    fuel_hybrid = st.checkbox("Fuel Hybrid")
    fuel_hydrogen = st.checkbox("Fuel Hydrogen")
    fuel_lpg = st.checkbox("Fuel LPG")
    fuel_petrol = st.checkbox("Fuel Petrol")
    fuel_plugin_hybrid = st.checkbox("Fuel Plug-in Hybrid")

    if st.button("Predict"):
        payload = {
            "prod_year": prod_year,
            "mileage": mileage,
            "cylinders": cylinders,
            "airbags": airbags,
            "fuel_cng": fuel_cng,
            "fuel_diesel": fuel_diesel,
            "fuel_hybrid": fuel_hybrid,
            "fuel_hydrogen": fuel_hydrogen,
            "fuel_lpg": fuel_lpg,
            "fuel_petrol": fuel_petrol,
            "fuel_plugin_hybrid": fuel_plugin_hybrid
        }
        # Send POST request to the FastAPI predict endpoint
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Prediction: {prediction}")
        else:
            st.error("An error occurred during prediction.")

if __name__ == "__main__":
    main()