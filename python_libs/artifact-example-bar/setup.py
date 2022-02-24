from setuptools import setup, find_packages
from artifact_example_bar import __version__

setup(
      name='artifact-example-bar',
      version=__version__,
      packages=find_packages(),
      install_requires=open('requirements.txt').read().splitlines()
)
