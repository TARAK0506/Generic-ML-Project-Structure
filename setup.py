from setuptools import find_packages,setup # type: ignore
from typing import List

HYPEN_E_DOT = '-e .' 
def get_requirements(file_path: str) -> list:
    """
    Read the requirements file and return the list of requirements
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()

    # Remove the -e. from the requirements
    requirements = [requirement.split(HYPEN_E_DOT)[-1] for requirement in requirements]
    return requirements
    
# print(get_requirements('requirements.txt'))

setup(
    name = 'Ml_Project',
    version = '0.1',
    author = 'Tarak',
    author_email = 'tarakaramarao0506@gmail.com',
    packages = find_packages(),

    # install_requires = ['pandas','numpy','scikit-learn','matplotlib','seaborn','joblib'],
    install_requires = get_requirements('requirements.txt'),
)