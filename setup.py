__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import setuptools

setuptools.setup(
    name='jinahub-text-sentencizer',
    version='1',
    author='Jina Dev Team',
    author_email='dev-team@jina.ai',
    description='The text sentencizer splits texts into sentences',
    url='https://github.com/jina-ai/executor-text-sentencizer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    py_modules=['jinahub.text.sentencizer'],
    package_dir={'jinahub.text': '.'},
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.7',
)
