from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n'," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "First ML Project",
    version = "0.0.1",
    author = "Shubhrajit Pal",
    author_email = "shubhrajitpal007@gmail.com",
    packages = find_packages(),
    # requires = ['pandas','numpy','seaborn']
    install_requirements = get_requirements('requirements.txt')
    
)