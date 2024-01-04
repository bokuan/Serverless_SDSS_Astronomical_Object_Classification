import gradio as gr
from PIL import Image
import requests
import hopsworks
import joblib
import pandas as pd

project = hopsworks.login(project="ID2223_23_lab1")
fs = project.get_feature_store()


mr = project.get_model_registry()
model = mr.get_model("star_model", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/star_model.pkl")
print("Model downloaded")

def star(u, g, r, i, z, redshift):
    print("Calling function")
#     df = pd.DataFrame([[sepal_length],[sepal_width],[petal_length],[petal_width]], 
    df = pd.DataFrame([[u, g, r, i, z, redshift]], 
                      columns=['u', 'g', 'r', 'i', 'z', 'redshift'])
    print("Predicting")
    print(df)
    # 'res' is a list of predictions returned as the label.
    res = model.predict(df) 
    # We add '[0]' to the result of the transformed 'res', because 'res' is a list, and we only want 
    # the first element.
#     print("Res: {0}").format(res)
    print(res)
    star_url = "https://raw.githubusercontent.com/bokuan/ID2223/main/res/" + res[0].lower() + ".jpg"
    img = Image.open(requests.get(star_url, stream=True).raw)            
    return img

demo = gr.Interface(
    fn=star,
    title="SDSS Astronomical Object Classification Predictive Analytics",
    description="Experiment with astronomical spectroscopical features to classify astronomical object.",
    allow_flagging="never",
    inputs=[
        gr.Number(value=20, label="u Filter (Ultraviolet)"),
        gr.Number(value=20, label="g Filter (Green)"),
        gr.Number(value=20, label="r Filter (Red)"),
        gr.Number(value=20, label="i Filter (Near Infrared)"),
        gr.Number(value=20, label="z Filter (Infrared)"),
        gr.Number(value=0.6, label="Redshift"),
        ],
    outputs=gr.Image(type="pil"))

demo.launch(debug=True)

