# Gender Recognition WebApp 🎭

A Flask-based web application that leverages Deep Learning and Computer Vision technologies to detect and classify gender from images and videos in real-time.

![Gender Recognition Demo](https://github.com/yourusername/gender-recognition-webapp/raw/main/static/images/demo.gif)

## 🔍 Overview

This web application uses **Deep Learning and Computer Vision** techniques to detect gender from images and videos. It combines **OpenCV** for face detection, a pre-trained **CNN model**, dimensionality reduction via **PCA**, and classification with a **Support Vector Classifier (SVC)** to analyze facial features and predict gender with confidence scores.

## 🌟 Key Features

- **Multiple Input Sources**
  - Upload images (PNG, JPG, JPEG)
  - Upload videos (MP4, AVI)
  - Capture from webcam in real-time

- **Advanced Processing Pipeline**
  - Face detection using OpenCV's Haar Cascade classifier
  - Feature extraction with pre-trained CNN
  - Dimensionality reduction using PCA
  - Gender classification with SVC (trained with `probability=True`)

- **Interactive Results**
  - Annotated output with gender prediction
  - Confidence scores
  - Real-time processing for video streams
  - Detailed analytics report

- **Responsive UI**
  - Modern, dark-themed interface
  - Bootstrap 5 responsive design
  - Mobile-friendly layout

## 🛠️ Technology Stack

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| **Python**       | Core programming language                    |
| **Flask**        | Web framework                                |
| **OpenCV**       | Face detection and image processing          |
| **scikit-learn** | PCA and SVC (Support Vector Classifier) model|
| **HTML/CSS/JS**  | Frontend development                         |
| **Bootstrap 5**  | Responsive UI design                         |

## ⚙️ How It Works

1. User uploads an image/video or captures from webcam
2. The application detects faces using OpenCV's Haar Cascade classifier
3. Each detected face is:
   - Converted to grayscale
   - Resized to a standard dimension
   - Pre-processed for feature extraction
4. The pre-trained model extracts facial features
5. PCA reduces the dimensionality of the feature space
6. SVC classifies the gender with probability scores
7. Results are displayed with bounding boxes and confidence metrics

## 📸 Screenshots

| Home Page | Results Page |
|:-:|:-:|
| ![Home Page](https://github.com/yourusername/gender-recognition-webapp/raw/main/static/images/home.png) | ![Results Page](https://github.com/yourusername/gender-recognition-webapp/raw/main/static/images/results.png) |

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Steps

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/gender-recognition-webapp.git
   cd gender-recognition-webapp
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://localhost:5000`

## 📦 Dependencies

```
flask==2.0.1
opencv-python==4.5.3.56
scikit-learn==0.24.2
numpy==1.21.2
pillow==8.3.1
```

## 🔧 Usage

1. **Image Upload**:
   - Click on the "Upload Image" button
   - Select an image file (PNG, JPG, JPEG)
   - Click "Process"

2. **Video Upload**:
   - Click on the "Upload Video" button
   - Select a video file (MP4, AVI)
   - Click "Process"

3. **Webcam Capture**:
   - Click on the "Capture from Webcam" button
   - Allow camera access when prompted
   - Click "Capture" when ready

4. **View Results**:
   - See gender predictions with confidence scores
   - Download or share the results

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [OpenCV](https://opencv.org/) for the computer vision tools
- [scikit-learn](https://scikit-learn.org/) for machine learning algorithms
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components

## 📧 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/gender-recognition-webapp](https://github.com/yourusername/gender-recognition-webapp)

---

⭐️ If you found this project useful, please consider giving it a star on GitHub!
