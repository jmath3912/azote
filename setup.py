import os
from setuptools import setup


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(
    name='azote',
    version='0.0.1',
    packages=['azote'],
    include_package_data=True,
    url='https://github.com/nwg-piotr/azote',
    license='GPL3',
    author='Piotr Miller',
    author_email='nwg.piotr@gmail.com',
    description='Wallpaper manager for Sway, i3 and some other WMs',
    long_description=read("README.md"),
    install_requires=['i3ipc', 'pygobject', 'pillow']
)