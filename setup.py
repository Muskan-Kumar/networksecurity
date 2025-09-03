'''
The setup.py file is an essential part of packaging and distributing python projects.
it is used by setuptools (or distutils in older python versions) to define the
configuration of your projects, such as its metadata, dependencies, and more
'''


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''This function will return list of requierements'''

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as f:
            #read lines from the file
            requirement=f.readline()
            #ignore empty line and -e .
            if requirement and requirement != '-e .':
                requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst


setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Muskan Kumar',
    author_email='muskankumar952593@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)



