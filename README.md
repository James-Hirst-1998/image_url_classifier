# Image URL Classifier

## Overview
This is a simple URL image classifier that uses a ResNet-50 model to classify images. The project is built using Flask for the web framework and provides an easy-to-use interface for uploading and classifying images.

## Running the Project
To run the project, follow these steps:

1. Install the required dependencies:
    ```sh
    poetry install
    ```

2. Start the Flask application:
    ```sh
    poetry run python app/main.py
    ```

3. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Why ResNet-50 and Flask?
### ResNet-50
- **High Accuracy**: ResNet-50 achieves high accuracy in image classification tasks, making it a reliable choice.
- **Pre-trained Models**: Availability of pre-trained models on large datasets like ImageNet makes it easy to use for transfer learning. Note, the pre-trained classes were specified via this [link](https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json)

### Flask
- **Lightweight**: Flask is a lightweight web framework that is easy to set up and use.
- **Flexibility**: It provides the flexibility to structure the project in a way that suits the application's needs.
- **Community Support**: Flask has a large community and extensive documentation, making it easier to find solutions and support.

## Testing
To run the tests for this project, follow these steps:

1. Ensure all dependencies are installed:
    ```sh
    poetry install
    ```

2. Run the tests using pytest:
    ```sh
    poetry run pytest
    ```

## Extensions
Here are some potential extensions for the project:
- **Improve UI**: Make the pages prettier and add a limit on the number of images before it begins removing them.
- **Testing**: Add more comprehensive tests to ensure the reliability of the application.

## Design Choices
- **File Structure**: The project is split into multiple files to enhance maintainability. For example, the main application logic is in `app/main.py`, while other functionalities are modularised.
- **Maintainability**: The code is organised in a way that makes it easy to extend and maintain in the long term. This includes using clear naming conventions and separating concerns within the codebase. Additionally, the project uses:
  - **Poetry**: For dependency management and packaging, which simplifies the process of managing project dependencies and virtual environments.
  - **Black**: For code formatting to ensure a consistent code style -> `poetry run black .`
  - **isort**: For sorting imports to maintain a clean and organised import structure -> `poetry run isort .`
  - **mypy**: For static type checking to catch type-related errors early in the development process -> `poetry run mypy .`

# TODO 
- Check if an easier way to deploy it
