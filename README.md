# FaceRecognizingTimeSheet

This is a software that uses facial recognition to update a timesheet for employees. The employees must take a picture of themselves / show their face in real-time and the software will use facial recognition and the system clock to sign employees in and out.

## Installation

This software requires use of [deepface](https://pypi.org/project/deepface/) framework.

```bash
pip install deepface
```

Additional installations such as pandas, keras, OpenCV, and TensorFlow may need to be installed/updated as well. 

*Note*: deepface framework is not compatible with the latest version of OpenCV, so the OpenCV version may need to be downgraded.

## Setup Database

1. Create a folder with all the faces of the staff named **faces**. 
2. For each person, create a folder with their name and each person's picture in their respective folder. Name the person's picture with the following scheme: `[FirstName_LastName_0.jpg]` (picture type can be JPG or PNG). For example, if a staff member was named **John Doe**, then 
  - folder: John_Doe 
  - image: John_Doe_0.jpg

## Running Code

Once you have set up your database, you can run the facial recognition software using 2 different methods: using an already existing image or using realtime streaming with a webcam.

### Existing Image
1. Save the image you want to classify as ```test.jpg``` in the main repo.
2. Run the following:
```bash
python3 face_recognition.py
```
3. While the program is running, it will ask you to verify if the person is correctly idenitified. Please verify the results.
4. The image used will now be added to the database and can be used for comparison next time the program is run.

### Realtime Stream
1. Run the following:
```bash
python3 stream_face.py
```
2. While the program is running, it will ask you to verify if the person is correctly idenitified. Please verify the results.
