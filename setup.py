from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='payomail',
    version='8.0.0',
    packages=find_packages(),
    package_data={'': ['*.png']},  # Include all PNG files in the package
    include_package_data=True,
    # Metadata
    project_urls={
        'Icon': 'https://github.com/Roshangedam/payomail/blob/master/payomail/images/icon.png',
    },
    author='Roshan Gedam',
    author_email='roshangedam1998@gmail.com',
    description='mailing utilty',
    url='https://github.com/Roshangedam/payomail',
    long_description=long_description,
    long_description_content_type="text/markdown",
)

# for add in publish pacakge use commands

# py setup.py sdist

# twine upload dist/*

# give your api token key

# done