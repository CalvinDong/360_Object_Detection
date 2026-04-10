# 📸 360° Object Detection using Synthetic Data

This project explores the use of synthetic datasets to train object detection models for 360° imagery, where real-world data is limited and difficult to collect.

The goal is to bridge the gap between synthetic and real-world performance by leveraging data generation techniques and transfer learning.

## 🚀 Overview

Object detection in 360° images presents unique challenges:

Limited availability of labelled datasets
Image distortion due to equirectangular projection
High cost of data collection and annotation

To address this, this project builds a full pipeline that:

Generates synthetic training data
Trains object detection models
Evaluates performance on real-world images

## 🧠 Key Features
- Synthetic dataset generation using real image compositing
- Augmentation techniques to simulate 360° distortion
- Training of YOLOv7 object detection models
- Evaluation using standard metrics (mAP@0.5, F1 score)
- Transfer learning to improve real-world performance

## 🏗️ Pipeline
1. Synthetic Data Generation
- Real object images (fruits) are extracted and composited onto 360° background images
- Augmentations applied:
    - Scaling and positioning
    - Distortion simulation based on spherical projection
    - Randomisation to improve dataset diversity
2. Model Training
- YOLOv7 used for object detection
- Models trained on:
    Synthetic dataset
    Open datasets (Flickr 360°, Fruits Dataset, etc.)
3. Evaluation
- Models evaluated on real-world 360° images
- Metrics used:
    mAP@0.5
    F1 Score

📊 Results
Model Type | 	mAP@0.5 |	F1 Score
---|---|---
Synthetic Only |	0.13	| 0.07
Real Data Only |	0.72 |	0.74
Transfer Learning |	0.85 |	0.87

👉 Transfer learning using synthetic pre-training significantly improved real-world performance.

## 🔍 Key Insights
Synthetic data alone is insufficient due to the reality gap
However, it is highly effective when used for pre-training
Combining synthetic + real data reduces the need for large labelled datasets
Data quality and diversity are critical for model performance

## 🛠️ Tech Stack
- Python
- YOLOv7
- TensorFlow / Keras
- OpenCV
- Google Colab (GPU training)

📁 Repository Structure
```
.
├── data/
├── training/
├── evaluation/
├── notebooks/
├── README.md
```

## 📄 Thesis
This project was developed as part of my Honours thesis at UTS.
Read the full thesis here

https://1drv.ms/b/c/549ce08b1f5c8b2d/IQAti1wfi-CcIIBUOAIBAAAAAV0uM9F2uPcpXc-wCNXml78?e=DLcPFV


## 💡 Future Improvements
Improve lighting augmentation to reduce dataset bias
Explore domain adaptation techniques to further close the reality gap
Extend to multi-class real-world datasets
Optimise for real-time inference in 360° video

## 🤝 Acknowledgements
UTS Faculty of Engineering and IT
Supervisor: Professor Stuart Perry
Open datasets (Flickr 360°, Fruits Dataset, etc.)

Now revisiting this project to explore improvements in model performance and modern tooling! 
