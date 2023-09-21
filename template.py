# To Get the generic Folder Path we need to import os  module
import os
# To create path of a folder we need to import the below module
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO)

project_name = "DS Project"

# Create a list of file which we need to create during this project 

list_of_files = [

    ".github/workflows/.gitkeep" ,# In the case of deployment we need to create pipe lines using git hub acctions and we have to write the code inside the workflows folder

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",# Create a component folder
    f"src/{project_name}/components/data_ingestion.py", # Create data ingestion folder inside components folder
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py", 
    f"src/{project_name}/components/model_monitering.py",

    # For creating Training and Prediction Pipelines we need to create a pipelines folder

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",

    # For Exception handeling and Logging

    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",

    "app.py","Dockerfile"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")