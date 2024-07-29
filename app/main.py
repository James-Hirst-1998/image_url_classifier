from flask import Flask, render_template, request
from home_page import process_image, render_home_template
from models.machine_learning import Model
import os
import json
import validators

app = Flask(__name__)

images_metadata = []

# Define the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    model_instance = Model()
    
    if request.method == 'POST':
        image_url = request.form['image_url']
        if image_url and validators.url(image_url):
            try:
                return process_image(image_url, model_instance, images_metadata) 
            except Exception as e:
                print(f"Error processing image: {e}")
                return render_home_template(images_metadata=images_metadata, error="Failed to process image")    
        else:
            return render_home_template(images_metadata=images_metadata, error="Invalid URL")       
    
    return render_home_template(images_metadata=images_metadata)

@app.route('/classifications')
def classifications():
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'trained_classes.json')

    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    names = [item[1].replace("_", " ").capitalize() for item in data.values()]
    names.sort()
    
    return render_template("classifications.html", items=names)

if __name__ == '__main__':
    app.run(debug=True)


