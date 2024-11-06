from setuptools import setup, find_packages
import os

# Function to read the requirements file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()
    
install_requires=parse_requirements('requirements.txt'),

setup(
    name='your_project_name',
    version='0.1.0',
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/yourproject',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'run-local=src.main:main',
        ],
    },
)