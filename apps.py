import streamlit as st

st.title('Customizable Neural Network')

num_neurons = st.sidebar.slider('Number of neurons in hidden layer:', 1, 64)
num_epochs = st.sidebar.slider('Number of epochs:', 1, 10)
activation = st.sidebar.text_input('Activation function')


if st.button('Train The Model'):
    'WE are Training'

if st.button('Evaluate The Model'):
    'We are evaluating the model'
    
