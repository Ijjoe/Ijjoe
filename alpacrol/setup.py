from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

setup(
    name='alpacrol',
    version='0.1',
    packages=find_packages(),
    description='cij frist simple library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='cij',
    author_email='your.email@example.com',
    url='https://github.com/Ijjoe/Ijjoe/alpacrol',  
    install_requires=[
        # 여기에 이 라이브러리를 설치하기 위해 필요한 다른 패키지들을 나열합니다.
      'requests',
      'bs4'
    ],
)
