import setuptools
from distutils.core import setup, Extension

readme = open('README.md').read()

setup(name='spectrometer',
      version='1.0.0',
      author='Alexander Baker',
      license='MIT',
      author_email='baker.alexander@gmail.com',
      description='Spectrometer Package',
      long_description=readme,
      url='alexfb.com',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
      ],
      packages=[
          'spectrometer'
      ],
      include_package_data=True,
      keywords="spectrometer",
      install_requires=['pillow', 'picamera', 'fraction']
      )
