Face Recognition Door Lock System:
A digital door lock system integrated with facial recognition technology was developed using Raspberry Pi 4B, Raspi Camera Module , the OpenCV library and a single channel relay module.
The system utilizes three software programs namely Capture, Trainer and Recognizer .
The Capture program captures the images of the user, extracts face from the image  using the Haar Cascade Classifier and stores it in the dataset folder .
Trainer program analyzes the facial features from the collected images of each user  using  the Local Binary Pattern Histogram  model and generates a dataset (YML File) that uniquely represents each user's facial characteristics.
Recognizer program detects a face in real-time and then uses the YML file to recognize the face. If the  face matches with the trained dataset, the system triggers a relay connected to one of the GPIOs on the Raspberry Pi to unlock the door. 
The Raspberry Pi was programmed in Thonny IDE using Python3.The system provides a high level of security by accurately identifying authorized users and preventing unauthorized access.
