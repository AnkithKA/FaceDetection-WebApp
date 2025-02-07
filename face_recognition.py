import numpy as np
import pickle
import cv2

# Load all models
haar = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')  # cascade classifier
model_svm = pickle.load(open('./model/model_svm2.pickle', mode='rb'))          # machine learning model (SVM)
pca_models = pickle.load(open('./model/pca_dict2.pickle', mode='rb'))          # pca dictionary
model_pca = pca_models['pca']      # PCA model
mean_face_arr = pca_models['mean_face']  # Mean Face

def faceRecognitionPipeline(filename, path=True):
    # Read image from file or use provided array
    if path:
        img = cv2.imread(filename)  # BGR
        if img is None:
            raise ValueError(f"Could not read the image from {filename}")
    else:
        img = filename  # array

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces using Haar Cascade
    faces = haar.detectMultiScale(gray, 1.5, 5)
    predictions = []

    for x, y, w, h in faces:
        roi = gray[y:y+h, x:x+w]

        # Normalize image (0-1)
        roi = roi / 255.0

        # Resize to (100, 100)
        if roi.shape[1] > 100:
            roi_resize = cv2.resize(roi, (100, 100), interpolation=cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi, (100, 100), interpolation=cv2.INTER_CUBIC)

        # Flatten the image (1x10000)
        roi_reshape = roi_resize.reshape(1, 10000)
        # Subtract the mean face
        roi_mean = roi_reshape - mean_face_arr
        # Get the eigen image using PCA
        eigen_image = model_pca.transform(roi_mean)
        # For visualization (optional)
        eig_img = model_pca.inverse_transform(eigen_image)
        # Predict gender using the SVM model
        results = model_svm.predict(eigen_image)
        prob_score = model_svm.predict_proba(eigen_image)
        prob_score_max = prob_score.max()

        # Generate report text and annotate the image
        text = "%s : %d" % (results[0], prob_score_max * 100)
        color = (255, 255, 0) if results[0] == 'male' else (255, 0, 255)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(img, (x, y - 40), (x + w, y), color, -1)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 5)

        output = {
            'roi': roi,
            'eig_img': eig_img,
            'prediction_name': results[0],
            'score': prob_score_max
        }

        predictions.append(output)

    return img, predictions
