import os
import re
from typing import Dict, List

from flask import render_template
from models.machine_learning import Model
from PIL import Image


def get_existing_metadata(image_url: str, images_metadata: List[Dict[str, str]]):
    for item in images_metadata:
        if item["url"] == image_url:
            return item
    return None


def render_existing_metadata(
    metadata: Dict[str, str], images_metadata: List[Dict[str, str]]
):
    images_metadata.remove(metadata)
    images_metadata.insert(0, metadata)
    return render_home_template(
        image_url=metadata["path"],
        predicted_class_name=metadata["class_name"],
        images_metadata=images_metadata,
    )


def process_image(
    image_url: str, model_instance: Model, images_metadata: List[Dict[str, str]]
):
    # If the image has already been analysed then don't do it again
    existing_metadata = get_existing_metadata(image_url, images_metadata)
    if existing_metadata:
        return render_existing_metadata(existing_metadata, images_metadata)

    img = model_instance.fetch_image(image_url)
    img_t = model_instance.process_image(img)
    output = model_instance.predict(img_t)
    predicted_class_name = model_instance.display_results(output)

    img_path = save_image(img, image_url)
    new_metadata = {
        "path": img_path,
        "class_name": predicted_class_name,
        "url": image_url,
    }
    images_metadata.insert(0, new_metadata)

    return render_home_template(
        image_url=img_path,
        predicted_class_name=predicted_class_name,
        images_metadata=images_metadata,
    )


def save_image(img: Image.Image, image_url: str):
    cleaned_image_name = re.sub(r"[^a-zA-Z0-9_.-]", "", image_url.split("/")[-1])
    img_path = "static/images/" + cleaned_image_name
    directory = os.path.dirname(img_path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    img.save(img_path)
    return img_path


def render_home_template(
    image_url=None, predicted_class_name=None, images_metadata=None, error=None
):
    return render_template(
        "home.html",
        image_url=image_url,
        predicted_class_name=predicted_class_name,
        images_metadata=images_metadata,
        error=error,
    )
