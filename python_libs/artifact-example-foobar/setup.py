from setuptools import setup, find_packages
from artifact_example_foobar import __version__

setup(
      name='artifact-example-foobar',
      version=__version__,
      packages=find_packages(),
      install_requires=open('requirements.txt').read().splitlines()
)
