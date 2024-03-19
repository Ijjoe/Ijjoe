### 알파코 9기

### Hi there 👋

<!--
**Ijjoe/Ijjoe** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

파이썬 라이브러리 코랩 설정 방법 

!git clone https://github.com/your-username/your-library-name.git


import sys
sys.path.append('/content/your-library-name')
import your_module_name

구조
mylibrary/
│
├── mylibrary/
│   ├── __init__.py
│   └── module1.py
│
├── tests/
│   ├── __init__.py
│   └── test_module1.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py


------------
from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    description='A simple example library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mylibrary',  #https://github.com/Ijjoe/Ijjoe
    install_requires=[
        # 여기에 이 라이브러리를 설치하기 위해 필요한 다른 패키지들을 나열합니다.
    ],
)
