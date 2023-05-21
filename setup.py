from setuptools import setup, find_packages

setup(
    name='TabularStats',
    version='1.0.0',
    author='ductileasy',
    description='A package for descriptive analysis of tabular data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/freefunction/TabularStats',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
    ],
)
