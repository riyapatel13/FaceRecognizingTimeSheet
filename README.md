# FaceRecognizingTimeSheet

This is a software that uses facial recognition to update a timesheet for employees. The employees must take a picture of themselves / show their face in real-time and the software will use facial recognition and the system clock to sign employees in and out.

## Installation

This software requires use of [deepface](https://pypi.org/project/deepface/) framework.

```bash
pip install deepface
```

Additional installations such as pandas, keras, OpenCV, and TensorFlow may need to be installed/updated as well. 

## Setup

1. Create a folder with all the faces of the staff named **faces**. 
2. For each person, create a folder with their name and each person's picture in their respective folder. Name the person's picture with the following scheme: `[FirstName_LastName_0.jpg]` (picture type can be JPG or PNG). For example, if a staff member was named **John Doe**, then 
  - folder: John_Doe 
  - image: John_Doe_0.jpg
