from deepface import DeepFace

result = DeepFace.verify("faces/RiyaPic.jpg", "faces/RiyaPic.jpg")
print("Is verified: ", result["verified"])