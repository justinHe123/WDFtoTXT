from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='wdftotxt',
      version='0.1',
      description='Extract data from wdf files and format in txt files',
      long_description=readme(),
      url='https://github.com/justinHe123/WDFtoTXT',
      author='Justin He',
      author_email='justinhe@ucla.edu',
      license='MIT',
      packages=['wdftotxt'],
      scripts=['bin/wdftotxt'],
      entry_points={
         'console_scripts': ['wdfconvert=wdftotxt.convert:main'],
      },
      install_requires=[
          'renishawWiRE'
      ],
      zip_safe=False)