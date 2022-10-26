from setuptools import setup

setup(name='pythonwhois-internet.nl',
      version='1.0.0',
      description='Internetnl fork of python-whois 2.4.3: Module for retrieving and parsing the WHOIS data for a domain. Supports most domains. No dependencies.',
      author='Sven Slootweg',
      author_email='pythonwhois@cryto.net',
      url='http://cryto.net/pythonwhois',
      packages=['pythonwhois'],
      package_dir={"pythonwhois":"pythonwhois"},
      package_data={"pythonwhois":["*.dat"]},
      install_requires=['argparse'],
      provides=['pythonwhois'],
      scripts=["pwhois"],
      license="WTFPL"
     )
