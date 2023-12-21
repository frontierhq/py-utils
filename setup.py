from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read()

setup(
    name='py-utils',
    version=version,
    author='Frontier Digital',
    author_email='hello@gofrontier.com',
    description='A collection of utilities and helper functions.',
    packages=find_packages(include=['py-utils']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.1',
)
