from setuptools import setup
import os


requirements = []
with open('requirements.txt', 'r') as f:
    lines = [x.strip() for x in f if 0 < len(x.strip())]
    requirements = [x for x in lines if x[0].isalpha()]

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='odc_tools',
    url='https://github.com/ocean-data-challenges/ODC_tools',
    author='Sammy Metref and Maxime Ballarotta',
    author_email='sammy.metref@datlas.fr',
    # Needed to actually package something
    packages=['odc_tools'],
    # Needed for dependencies
    install_requires=requirements,
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Python package of the tools used in the ocean data challenges',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),

)
