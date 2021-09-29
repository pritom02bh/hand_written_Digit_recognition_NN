import streamlit as st

st.title('Customizable Neural Network')

num_neurons = st.sidebar.slider('Number of neurons in hidden layer:', 1, 64)
num_epochs = st.sidebar.slider('Number of epochs:', 1, 10)
activation = st.sidebar.text_input('Activation function')

"The number of neurons is : " + str(num_neurons)
"The activation function is : " + activation