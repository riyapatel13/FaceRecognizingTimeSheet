from deepface import DeepFace
import os

# realtime facial recognition
# Issue: works well but cannot improve on mistakes

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

# if using the correct naming scheme, this will take the name from the pic
def name_from_pic(path):
    dir_name = path.split("/")[1]
    name = dir_name.replace("_", " ")
    return name

# given all the directories in the database, it will extract all the names of the people
def list_names(db_path):
    people_dir = os.listdir(db_path)
    # create list of people
    i = 0
    while i < len(people_dir):
        # do not include .pkl file or .DS_Store file
        # eliminate all non name files
        # any folder with a "." will not count
        if "." in people_dir[i]:
            people_dir.remove(people_dir[i])
        # extracting name
        else:
            people_dir[i] = people_dir[i].replace("_", " ")
            i += 1

    return people_dir

# if the program guessed incorrectly
def wrong_answer(db_path):
    name_list = list_names(db_path)
    person = None
    while person not in name_list:
        person = input(f"Type in the correct person. {name_list} \n")
    print(f"{person} has been signed in")


res = DeepFace.stream(database_path, 'VGG-Face', 'cosine')
# res returns the file that the stream is most similar to
person = name_from_pic(res)
print("person: ", person)

verify = None
while verify != 'Y' and verify != 'N':
    verify = input(f"Is the person {person}? Please select Y/N.\n")

if verify == 'Y':
    print(f"{person} has been signed in")
elif verify == 'N':
    wrong_answer(database_path) 