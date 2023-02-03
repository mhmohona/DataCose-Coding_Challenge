from setuptools import setup, find_packages

setup(
    name='apichallenge',
    version='0.0.1',
    author='Mahfuza',
    author_email='mhmohona@gmail.com',
    description='A Python project to test the API endpoint for People data and validate the response.',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest',
        're',
        'python-dotenv'
    ],
)
