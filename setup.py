# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="julioe_lambdata",
    version="1.0",
    author="Julio E",
    author_email="je27@protonmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/julioe27/julioe_lambdata",
    #keywords="",
    packages=find_packages() # ["julioe_lambdata"]
)