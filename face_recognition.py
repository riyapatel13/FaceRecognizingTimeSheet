from deepface import DeepFace
import pandas as pd
import os
import glob

'''
TODO:
- (another file/later) take picture and save it
- (another file/later) real-time analysis + take pic + save 
- works with os, have it work with cloud 
- error check for if the image cannot be found (generally shouldn't happen)
'''
'''
QUESTIONS:
- what to do when database gets too large? delete earlier pictures? set a threshold
- deleted pkl file after every verification bc we are updating database, but it runs 3x slower
    - 11s for 5 pictures --> doesn't scale well
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


def name_from_pic(path):
    dir_name = path.split("/")[1]
    name = dir_name.replace("_", " ")
    return name

def update_database(pic, db_path, person):
    dir_list = os.listdir(db_path+'/'+person)
    file_count = len(dir_list)
    os.rename(pic,db_path+'/'+person+'/'+person+'_'+str(file_count)+'.jpg')
    # copy instead of just move because you lose the file (potentially an issue)
    print(f"{person} has been signed in")  

def list_names(db_path):
    people_dir = os.listdir(db_path)
    # create list of people
    i = 0
    while i < len(people_dir):
        # do not include .pkl file or .DS_Store file
        # eliminate all non name files
        if "." in people_dir[i]:
            people_dir.remove(people_dir[i])
        # extracting name
        else:
            people_dir[i] = people_dir[i].replace("_", " ")
            i += 1

    return people_dir

def wrong_answer(pic, db_path):
    name_list = list_names(db_path)
    person = None
    while person not in name_list:
        person = input(f"Type in the correct person. {name_list} \n")
    update_database(pic, db_path, person)
    
'''
Creates pkl file with representation of database and deletes at end
Optionally can choose model and metrics (but may need to load model)
'''
df = DeepFace.find(img_path = img, db_path = database_path)

if df.shape[0] > 0:
    most_sim_pic = df.iloc[0].identity
    person = name_from_pic(most_sim_pic) # extrace name from file path
    
    verify = None
    while verify != 'Y' and verify != 'N':
        verify = input(f"Is the person {person}? Please select Y/N.\n")
    
    if verify == 'Y':
        update_database(img, database_path, person)
    elif verify == 'N':
        wrong_answer(img, database_path) # update_database() called in function

else:
    print("Unable to identify person")
    wrong_answer(img, database_path)

# remove pkl file from database because it has been updated
pkl_files = glob.glob(database_path+'/'+ '*.pkl')
for file in pkl_files:
    os.remove(file) 