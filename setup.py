"""
This file is used for converting this whole code or application as a package, upload it to pypi, 
and then import this package 
"""
from setuptools import  find_packages, setup # this will find and import all the packages that we have imported
                                                #for this project in requirements.txt
from typing import List

HYPEN_E_DOT ="-e ."
def get_requirements(file_path : str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # from requirements.txt - each item gets read with this code, but \n(next line also gets read)
        requirements = [req.replace("\n","") for req in requirements] # this removes \n while reading requiements.txt
                                                                    # also we write '-e .' at the end of requirements.txt
                                                                    # it automatically triggers setup.py while read
                                                                    #we need to read it, but remove it too
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Mukul',
author_email = 'mukulmalik24@gmail.com',
packages = find_packages(), # this searches for __init__.py file, and wherever it is present, it includes them to behave as a package
# install_requires =['pandas', 'numpy', 'seaborn'] # instead of this we do this below
install_requires = get_requirements('requirements.txt') #  we will create t his function 'get_requirements' and whatever packages we write in requirement.txt, they gets installed
)
