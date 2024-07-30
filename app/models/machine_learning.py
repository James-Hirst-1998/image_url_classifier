import io
import json
import os
from typing import Optional

import requests
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
from torchvision.models import ResNet50_Weights


class Model:
    def __init__(self):
        # Load pre-trained model
        self.model = models.resnet50(weights=ResNet50_Weights.DEFAULT)
        self.model.eval()

        # Load the pre-trained classes from file
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(current_dir)
        json_file_path = os.path.join(parent_dir, "trained_classes.json")
        with open(json_file_path, "r") as file:
            self.imagenet_classes = json.load(file)

    @staticmethod
    def fetch_image(url: str) -> Optional[Image.Image]:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
            img = Image.open(io.BytesIO(response.content))
            return img
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except IOError as e:
            print(f"Image open failed: {e}")
            return None

    @staticmethod
    def process_image(img: Image.Image) -> torch.Tensor:
        preprocess = transforms.Compose(
            [
                transforms.Resize(256),  # Resize images to be consistent
                transforms.CenterCrop(224),  # Take the center area
                transforms.ToTensor(),  # Convert to numpy tensor
                transforms.Lambda(lambda x: x[:3, :, :]),  # Ensure 3 channels
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )
        img_t = preprocess(img)
        img_t = img_t.unsqueeze(0)
        return img_t

    def predict(self, img_t: torch.Tensor) -> torch.Tensor:
        # TODO - Get the accuracry of the precition
        with torch.no_grad():
            output = self.model(img_t)
        return output

    def display_results(self, output: torch.Tensor) -> str:
        _, predicted_idx = torch.max(output, 1)
        predicted_class_id = str(predicted_idx.item())
        predicted_class_name = self.imagenet_classes[predicted_class_id][1]
        return predicted_class_name.replace("_", " ").capitalize()
