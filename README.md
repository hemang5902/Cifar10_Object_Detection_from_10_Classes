# Cifar10_Object_Detection_from_10_Classes

## Dataset used: The CIFAR-10 dataset
<p>
  The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.
<br><br>
Here are the classes in the dataset, as well as 10 random images from each:

![Screenshot 2023-07-07 144542](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/40b1bf63-d8d7-4e1c-8b69-bee284ef8a60)

The classes are completely mutually exclusive. There is no overlap between automobiles and trucks. "Automobile" includes sedans, SUVs, things of that sort. "Truck" includes only big trucks. Neither includes pickup trucks.
</p>
<hr>

## Industrial Scope:
<p>
  The CIFAR-10 dataset is primarily used for academic and research purposes, especially in the field of computer vision and machine learning. However, it can also find applications in various industrial domains. Here are some potential industrial use cases for the CIFAR-10 dataset:

1. Quality Control: In manufacturing industries, the CIFAR-10 dataset can be utilized for image classification to detect defects and anomalies in products during the production process. For instance, it could be employed to identify faulty items on assembly lines or ensure product compliance with quality standards.

2. Surveillance and Security: The dataset can be valuable for building image recognition systems in the security industry. It can be used for identifying and tracking objects, people, or vehicles in security footage, helping enhance surveillance and threat detection.

3. Autonomous Vehicles: In the automotive industry, CIFAR-10 can be used to develop algorithms for object recognition and classification. This enables self-driving cars to detect and interpret road signs, pedestrians, cyclists, and other vehicles, enhancing their safety and efficiency.

4. Medical Imaging: The CIFAR-10 dataset can be adapted for classifying medical images, such as X-rays or MRIs, to assist in diagnosing diseases, identifying abnormalities, and predicting patient outcomes.

5. Agriculture: The dataset can be employed to build systems that recognize and classify crops, pests, or diseases in agriculture. This can help optimize crop management and improve agricultural productivity.

6. Retail and E-commerce: CIFAR-10 can be applied in the retail industry for tasks like product recognition and recommendation. For example, it can be used to identify products based on customer images or recommend similar items.

7. Augmented Reality and Virtual Reality: The dataset can be utilized to enhance AR and VR experiences by enabling object recognition and scene understanding, making virtual objects interact more effectively with the real environment.

8. Robotics: In the robotics industry, CIFAR-10 can be used for object detection and manipulation, allowing robots to recognize and interact with various objects in their surroundings.

9. Environmental Monitoring: The dataset can be adapted to monitor environmental changes by identifying and classifying objects or events in satellite imagery, such as deforestation, urban growth, or natural disasters.
</p>
<hr>

## Algorithm Used:
<p>
  ResNet stands for Residual Network and is a specific type of convolutional neural network (CNN) introduced in the 2015 paper “Deep Residual Learning for Image Recognition” by He Kaiming, Zhang Xiangyu, Ren Shaoqing, and Sun Jian. CNNs are commonly used to power computer vision applications.

ResNet-50 is a 50-layer convolutional neural network (48 convolutional layers, one MaxPool layer, and one average pool layer). Residual neural networks are a type of artificial neural network (ANN) that forms networks by stacking residual blocks.

https://colab.research.google.com/drive/1BCObsIcrondvrovDtKskQtgrUiXDBo0O?usp=sharing --> link for the trained model<br>
Transfer learning means taking a pre-trained machine learning model and repurposing it for another related task for faster development. It helps achieve higher performance even if the model is trained on a smaller dataset.
</p>

## Error correction procedure
<p>
  As there is no error in data to be corrected, Only
<b>Normalizing the Pixel Values:
X_train = X_train/255 and X_test = X_test/255</b><br>
In deep learning models, it is common to normalize the input data to a range between 0 and 1. Since the pixel values in the CIFAR-10 dataset range from 0 to 255 (8-bit color depth), dividing all the pixel values by 255 scales them to the range [0, 1].</p>
<hr>

## Final deployment using flask server
**pip install -r requirements.txt** -> Use this command if you want ot install the compatible versions of libraries.<br>
**View on** : run the app.py file on your cmd prompt
![Screenshot (26)](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/909aac80-52a2-4567-852c-85045434d1a4)
<br>
![Screenshot (27)](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/60b12b90-9a15-4443-a106-ae00dc88a1b8)
<br>
![Screenshot (28)](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/7ad03fb3-ab1b-41a7-963f-76eada2ff920)
<br>
![Screenshot (29)](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/5e538d95-63c8-4f83-b4b5-27357f7c2a30)
<br>
![Screenshot (31)](https://github.com/hemang5902/Cifar10_Object_Detection_from_10_Classes/assets/107362216/02b1b43c-5cdd-47b9-aaa5-28706a7cd5be)
<hr>

# END
