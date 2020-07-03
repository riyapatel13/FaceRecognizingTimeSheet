from deepface import DeepFace
import pandas as pd
import os

'''
TODO:
- delete pkl file after running everytime (will be slow to create representation but thats ok)
- If no, provide a list of all options and ask who and update - wrong_answer
- (another file/later) take picture and save it
- (another file/later) real-time analysis + take pic + save 
- works with os, have it work with cloud 
'''
'''
QUESTIONS:
- what to do when database gets too large? delete earlier pictures? set a threshold
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

database_path = "faces" # add this to setup file
img = "test.jpg" # somehow make this so that its not in the file


def extract_name(path):
    dir_name = path.split("/")[1]
    name = dir_name.replace("_", " ")
    return name

def update_database(pic, sim_img_path):
    dir_name = sim_img_path.split("/")
    dir_list = os.listdir(dir_name[0]+'/'+dir_name[1])
    file_count = len(dir_list)
    os.rename(pic,dir_name[0]+'/'+dir_name[1]+'/'+dir_name[1]+'_'+str(file_count)+'.jpg')


'''
Creates pkl file with representation of database
Delete pkl file when updating database
Optionally can choose model and metrics (but may need to load model)
'''
df = DeepFace.find(img_path = img, db_path = "faces")

if df.shape[0] > 0:
    most_sim_pic = df.iloc[0].identity
    person = extract_name(most_sim_pic) # extrace name from file path
    
    verify = None
    while verify != 'Y' and verify != 'N':
        verify = input(f"Is the person {person}? Please select Y/N.\n")
    
    if verify == 'Y':
        update_database(img, most_sim_pic)
        print(f"{person} has been signed in")  
    elif verify == 'N':
        # wrong_answer() # update_database() called in function
        print("oops")

else:
    print("Unable to identify person")
    # wrong_answer()
