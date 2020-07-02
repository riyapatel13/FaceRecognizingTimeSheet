from deepface import DeepFace
import pandas as pd

'''
TODO:
- delete pkl file after running everytime (will be slow to create representation but thats ok)
- return folder of where picture came from (folder will be name)
- User input if that is correct
- If yes, update database and add to folder with name (change pic name)
- If no, provide a list of all options and ask who and update - wrong_answer
- (another file/later) take picture and save it
- (another file/later) real-time analysis + take pic + save 
'''
'''
QUESTIONS:
- what to do when database gets too large?
'''


'''
Face Recognition Models
- default model is VGG-Face
- models have varying performance and speed
'''
models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Ensemble"]

'''
Similarity metrics
- default is cosine similarity
'''
metrics = ["cosine", "euclidean", "euclidean_l2"]

database_path = "faces"

'''
Creates pkl file with representation of database
Delete pkl file when updating database
Optionally can choose model and metrics (but may need to load model)
'''
df = DeepFace.find(img_path = "test.jpg", db_path = "faces")

if df.shape[0] > 0:
    most_sim_pic = df.iloc[0].identity
    print(most_sim_pic)
    # extract_name() # extrace name from file path

else:
    print("Unable to identify person")
    # wrong_answer()
