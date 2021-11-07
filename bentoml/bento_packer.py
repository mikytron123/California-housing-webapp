from bento_service import SVR 
import joblib
import os
import shutil
from distutils.dir_util import copy_tree

#Create a SVR service instance
SVR_service = SVR()
model = joblib.load('model.pkl')
# Pack the newly trained model artifact
SVR_service.pack('model', model)

# Save the prediction service to disk for model serving
saved_path = SVR_service.save()

# copy subdirectory example
fromDirectory = saved_path
toDirectory = os.getcwd()

copy_tree(fromDirectory, toDirectory)
