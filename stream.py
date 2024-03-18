import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model=tf.keras.models.load_model('plant_disease.keras')
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    prediction = model.predict(input_arr)
    result_index=np.argmax(prediction)
    return result_index


#sidebar
st.sidebar.title('Navigation')
app_mode = st.sidebar.selectbox("Choose the page", ["Home", "About",'Prediction'])

#homepage
if app_mode == "Home":
    st.title('Home')
    st.write('This is a web application that uses a trained model to detect plant diseases. The model was trained using the PlantVillage dataset. You can upload an image of a plant and the model will predict if the plant is healthy or diseased.')
    st.markdown('**Note:** The model is not perfect and may not be accurate in some cases. It is recommended to consult a professional for accurate diagnosis.')

#about page
elif app_mode == "About":
    st.title('About')
    st.write('This web application was created by Manoj Sai Vardhan. The model used in this application was trained using a part of the PlantVillage dataset. The model was trained to detect 15 different classes of plant diseases. The model was trained using the TensorFlow and Keras libraries.')

#prediction page
elif app_mode == "Prediction":
    st.title('Prediction')
    st.write('Upload an image of a plant and the model will predict if the plant is healthy or diseased.')
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = uploaded_file.read()
        if(st.button("show image")):
            st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        # label=model_prediction(uploaded_file)
        # if label==0:
        #     st.write('The plant is healthy')
        # else:
        #     st.write('The plant is diseased')

        if(st.button("show prediction")):
            with st.spinner('Model is predicting...'):
                 
                st.balloons()
                result_index=model_prediction(uploaded_file)
                class_name= ['Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy']
                st.success('The model predicted the plant to be {} '.format(class_name[result_index]))