import unittest

import torch
from PIL import Image

from app.models.machine_learning import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def test_process_image(self):
        img = Image.open("tests/test_images/binoculars.png")
        img_t = self.model.process_image(img)

        # Check the shape and type of the output tensor
        self.assertIsInstance(img_t, torch.Tensor)
        self.assertEqual(img_t.shape, (1, 3, 224, 224))

    def test_predict(self):
        img = Image.open("tests/test_images/binoculars.png")
        img_t = self.model.process_image(img)

        output = self.model.predict(img_t)

        # Check if the output tensor is not empty and has the expected shape
        self.assertIsInstance(output, torch.Tensor)
        self.assertEqual(output.shape, (1, 1000))

        # Check if the predicted class is as expected
        predicted_class_name = self.model.display_results(output)
        expected_class_name = "Binoculars"
        self.assertEqual(predicted_class_name, expected_class_name)


if __name__ == "__main__":
    unittest.main()
