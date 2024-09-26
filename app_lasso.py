
# Load the trained model
with open('lasso_regression_model.pkl', 'rb') as file:
  model = pickle.load(file)

# Create a title for the app
st.title("Monthly Revenue Prediction App (Lasso Regression)")

# Input features
st.header("Enter the following information:")

# Input features (replace with your actual feature names)
website_traffic = st.number_input("Website Traffic", value=0)
number_of_products = st.number_input("Number of Products", value=0)
marketing_spend = st.number_input("Marketing Spend", value=0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", value=0)

# Create a button to predict
if st.button("Predict Monthly Revenue"):
  # Create a DataFrame with the user input
  input_data = pd.DataFrame({
      'website_traffic': [website_traffic],
      'number_of_products': [number_of_products],
      'marketing_spend': [marketing_spend],
      'customer_acquisition_cost': [customer_acquisition_cost]
      # Add more columns as needed
  })

  # Make prediction using the loaded model
  prediction = model.predict(input_data)[0]

  # Display the prediction
  st.header("Predicted Monthly Revenue:")
  st.write(f"${prediction:.2f}")
