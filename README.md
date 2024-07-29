

## TODO 
- Make the pages prettier and do some testing (add a limit of images before it begins removing them - set an upper limit)
- Protect against malicious input/ check error cases
- How to package it up for easy deployment
- Add tests?
- Write the readme


## Notes:
- It errors on `https://www.johnnyquinnusa.com/wp-content/uploads/2015/08/bobsled2.jpg`
`https://4.bp.blogspot.com/-JBpINz7jWfo/Uyn1ZIMM7UI/AAAAAAAAHLs/qtAY3kPNmjM/s1600/Roseate+Spoonbill%252C+Florida%252C+Merritt+Island%252C+13th+March+2014+075.jpg`



# ResNet-50
## ResNet-50 Strengths:
High Accuracy: ResNet-50 has been proven to achieve high accuracy in image classification tasks on various datasets, making it a reliable choice for similar tasks.
Deep Learning Efficiency: Its residual connections help in training very deep networks by addressing the vanishing gradient problem, allowing it to learn complex patterns without a significant increase in computational cost.
Pre-trained Models: Availability of pre-trained models on large datasets like ImageNet makes it easy to use for transfer learning, significantly reducing the time and resources required for training.
## ResNet-50 Limitations:
Specificity to Classification: While ResNet-50 excels in image classification, it might not be the best choice for other image processing tasks such as object detection, segmentation, or image generation without modifications or additional layers.
Resource Intensive: For applications with limited computational resources, smaller models or those optimized for efficiency (like MobileNet or EfficientNet) might be more appropriate.
Generalization: While pre-trained models provide a good starting point, they may not perform well on very specific or niche tasks without further fine-tuning on a relevant dataset.
## Alternatives:
For Object Detection and Segmentation: Models like Faster R-CNN, YOLO (You Only Look Once), and Mask R-CNN are designed specifically for these tasks, offering better performance than a straightforward application of ResNet-50.
For Efficiency: Models like MobileNet or SqueezeNet are designed to be lightweight and efficient, suitable for mobile or embedded devices.
For Image Generation: Generative models like GANs (Generative Adversarial Networks) or VAEs (Variational Autoencoders) are better suited for tasks involving image generation or style transfer.
