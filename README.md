# Gender Recognition WebApp 🎭  

## 🔍 Overview  

This is a **Flask-based web application** that uses **Deep Learning and Computer Vision** to detect gender from images and videos.  
It leverages **OpenCV, a pre-trained CNN model, and scikit-learn** to analyze facial features and classify gender.  

 

---

## 🛠️ Tech Stack  

The web app is built using the following technologies:  


| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| **Python**       | Core programming language                    |
| **Flask**        | Web framework                                |
| **OpenCV**       | Face detection and image processing          |
| **scikit-learn** | PCA and SVC (Support Vector Classifier) model  |
| **HTML/CSS/JS**  | Frontend development                         |
| **Bootstrap 5**  | Responsive UI design                         |


---

## 🎯 Features  

- **Image & Video Upload:** Upload images (PNG, JPG, JPEG) or videos (MP4, AVI) for gender recognition.
- **Webcam Capture:** Capture an image directly from your webcam.
- **Face Detection:** Uses OpenCV’s Haar Cascade classifier to detect faces.
- **SVC-Based Classification:** Processes the detected face using PCA and classifies it using an SVC model (trained with `probability=True`).
- **Interactive UI:** Modern, responsive, and dark-themed interface built with Flask and Bootstrap.
- **Detailed Report:** Displays annotated images or video frames along with prediction details and confidence scores.


---

## ⚙️ How It Works  

1️⃣ **User uploads an image or video**  
2️⃣ **OpenCV** detects faces in the input  
3️⃣ The image is converted to grayscale and resized  
4️⃣ **A pre-trained CNN model** extracts facial features  
5️⃣ **Prediction is made** (Male/Female)  
6️⃣ The result is displayed with a **confidence score**  

## Project Structure


ggender-recognition-webapp/
│
├── app.py                    # Main Flask application
├── face_recognition.py       # Gender recognition pipeline (SVC model, PCA, OpenCV)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── model/                    # Model files
│   ├── haarcascade_frontalface_default.xml
│   ├── model_svm2.pickle    # Trained SVC model (probability=True)
│   └── pca_dict2.pickle     # PCA model and mean face array
│
├── static/                   # Static files (CSS, JS, images, uploads, results)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   └── model_flow.png   # Diagram of model workflow (optional)
│   ├── uploads/             # Uploaded files
│   └── results/             # Processed output files
│
└── templates/                # HTML templates
    ├── base.html
    ├── index.html
    └── gender.html


