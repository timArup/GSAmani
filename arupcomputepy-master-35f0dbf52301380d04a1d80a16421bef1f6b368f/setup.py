from setuptools import setup, find_packages

setup(name='arupcomputepy',
    version='0.4.2',
    description='Python library to interact with the Arup Compute API',
    url='https://github.com/arup-group/arupcomputepy',
    author='Hugh Groves',
    install_requires=['requests','msal','appdirs', 'jsons'],
    packages=find_packages(),
    zip_safe=False)
