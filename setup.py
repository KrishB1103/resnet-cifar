from setuptools import setup, find_packages

setup(
    name='resnet-cifar',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
    ],
    author='Krish Billa',
    description='A simple ResNet model for CIFAR-10',
    url='https://github.com/KrishB1103/resnet-cifar',
)
