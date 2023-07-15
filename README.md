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
## Error correction procedure
<hr>

## Final deployment using flask server
**pip install -r requirements.txt** -> Use this command if you want ot install the compatible versions of libraries.<br>
**View on** : run the app.py file on your cmd prompt
