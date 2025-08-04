from setuptools import setup, find_packages

setup(
    name='resnet-cifar',
    version='0.1',
    description='ResNet model for CIFAR-10 in PyTorch',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'matplotlib'
    ],
    python_requires='>=3.7',
)
