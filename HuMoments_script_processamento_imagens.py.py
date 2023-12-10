import os
import cv2
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from progress.bar import Bar
import time

def main():
    mainStartTime = time.time()

    trainImagePath = './images_split/train/'
    testImagePath = './images_split/test/'
    trainFeaturePath = './features_labels/train/'
    testFeaturePath = './features_labels/test/'

    train_images, train_labels, encoder_classes = process_data(trainImagePath, trainFeaturePath)
    train_and_evaluate_classifier(train_images, train_labels, encoder_classes, trainFeaturePath, 'training')

    test_images, test_labels, encoder_classes = process_data(testImagePath, testFeaturePath)
    evaluate_classifier_on_test_set(trainFeaturePath, test_images, test_labels, encoder_classes)

    print(f'[INFO] Total execution time: {round(time.time() - mainStartTime, 2)}s')

def process_data(image_path, feature_path):
    images, labels = get_data(image_path)
    encoded_labels, encoder_classes = encode_labels(labels)
    features = extract_hu_moments_features(images)

    save_data(feature_path, encoded_labels, features, encoder_classes)

    return features, encoded_labels, encoder_classes

def train_and_evaluate_classifier(features, labels, encoder_classes, feature_path, set_type):
    print(f'[INFO] ========= {set_type.upper()} IMAGES ========= ')
    classifier, accuracy = train_and_evaluate(features, labels)
    print(f'[INFO] Classifier accuracy on {set_type.lower()} set: {accuracy * 100:.2f}%')

def evaluate_classifier_on_test_set(train_feature_path, test_images, test_labels, encoder_classes):
    train_encoded_labels, _ = get_data(train_feature_path + 'labels.csv')
    train_features, _ = get_data(train_feature_path + 'features.csv')

    classifier, _ = train_and_evaluate(train_features, train_encoded_labels)

    print(f'[INFO] =========== TEST IMAGES =========== ')
    test_encoded_labels, _ = encode_labels(test_labels)
    test_features = extract_hu_moments_features(test_images)

    test_accuracy = evaluate_classifier(classifier, test_features, test_encoded_labels)

    print(f'[INFO] Classifier accuracy on test set: {test_accuracy * 100:.2f}%')

    confusion_mat = confusion_matrix(test_encoded_labels, classifier.predict(test_features))
    print(f'[INFO] Confusion Matrix:\n{confusion_mat}')

    save_data(train_feature_path, test_encoded_labels, test_features, encoder_classes)

def get_data(path):
    images = []
    lab
