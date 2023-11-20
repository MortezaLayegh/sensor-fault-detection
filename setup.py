from setuptools import find_packages, setup

from typing import List

def get_requirements() -> List[str]:
    """Get the project requirements"""

    with open("requirements.txt", "r") as f:
        requirements_list:List[str] = f.read().splitlines()

    return requirements_list
 
setup(
    name="sensor",
    version="0.0.1",
    author="MortezaLayegh",
    author_email="layeghmorteza@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)