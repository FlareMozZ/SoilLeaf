from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

class_names = {
    0: 'Pepper__bell___Bacterial_spot',
    1: 'Pepper__bell___healthy',
    2: 'Potato___Early_blight',
    3: 'Potato___Late_blight',
    4: 'Potato___healthy',
    5: 'Tomato_Bacterial_spot',
    6: 'Tomato_Early_blight',
    7: 'Tomato_Late_blight',
    8: 'Tomato_Leaf_Mold',
    9: 'Tomato_Septoria_leaf_spot',
    10: 'Tomato_Spider_mites_Two_spotted_spider_mite',
    11: 'Tomato__Target_Spot',
    12: 'Tomato__Tomato_YellowLeaf__Curl_Virus',
    13: 'Tomato__Tomato_mosaic_virus',
    14: 'Tomato_healthy',
}

model = models.load_model("plant_disease.keras")

def model_prediction(test_image):
    image = Image.open(test_image)
    image = image.convert("RGB")
    image = image.resize((128, 128))
    input_arr = np.asarray(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

content = ""
img_path = "placeholder_image.png"
pred = ""

index = """

<h1>Plant Disease Classifier</h1>

<|{content}|file_selector|extensions=.jpg|>
Upload an image of a plant

<|{pred}|>

<|{img_path}|image|>

"""

def on_change(state, var_name, var_val):
    if var_name == "content":
        state.pred = ""
        state.img_path = var_val
    elif var_name == "img_path":
        if var_val:
            result_index = model_prediction(var_val)
            state.pred = f"The model predicted the plant to be {class_names[result_index]}"
    # print(var_name, var_val)

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)
