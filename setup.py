#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

setup(
    name='ms_tts_service',
    description='Convert text to mp3 via Microsoft tts',
    version=1.1,
    license='MIT',
    author='Jianqing Peng',
    author_email='pengjianqing@gmail.com',
    url='https://github.com/pjq/ms_tts_audio',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=['ms_tts_service'],
    scripts=['service.py'],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
