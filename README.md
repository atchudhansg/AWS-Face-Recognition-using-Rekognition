# AWS Face Recognition Service

## Overview

This repository demonstrates the results of an AWS Face Recognition Service built using AWS Rekognition. The project leverages a serverless architecture with Amazon S3, AWS Lambda, and DynamoDB to provide a scalable and efficient face recognition solution.

---

## Features

- **Serverless Architecture**: Event-driven design using AWS Lambda.
- **Facial Recognition**: Efficient face matching with AWS Rekognition.
- **Image Storage**: Centralized storage of images in Amazon S3.
- **Data Management**: Metadata and face data stored in DynamoDB.
- **Real-Time Processing**: Automatic processing of images upon upload.

---

## Results

Here are the results from the implemented AWS Face Recognition Service:

### Recognized Individuals
- **Name**: Elon Musk
- **Confidence**: 99.87%
- **Face ID**: `faceId_12345`

![Elon Recognized](./assets/elon-recognized.png)

### Unrecognized Individual
An unrecognized individual's face, which isn't stored in DynamoDB, will be flagged as "No Match."

![Unrecognized Face](./assets/unrecognized-face.png)

---

## Detailed Implementation Guide

For a step-by-step guide to implementing this project, including the setup of S3, Lambda, Rekognition, and DynamoDB, visit the detailed instructions here:

[**Detailed Implementation Guide**](https://example.com/implementation-guide)

---

## How It Works

### Architecture
The system follows this workflow:
1. Images are uploaded to an S3 bucket.
2. A Lambda function triggers automatically to process the uploaded image.
3. AWS Rekognition extracts and analyzes facial data.
4. The processed data is stored in DynamoDB for future recognition.
5. If a match is found, the name and confidence score are returned. If no match exists, it is flagged as unrecognized.

---

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
