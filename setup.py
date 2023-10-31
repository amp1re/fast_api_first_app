from setuptools import setup

setup(
    name='first_api',
    version='0.0.1',
    description='FastApi first app',
    install_requires=[
        'fastapi==0.104.0',
        'uvicorn==0.23.2'

    ],
    scripts=['app/main.py']
)