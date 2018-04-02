import os
from setuptools import setup, find_packages
import sys
import uuid

from bear_to_paper import __version__ as version_string


requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except ImportError:
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-')
            and not req.startswith('#')
        ]


setup(
    name='bear-to-paper',
    version=version_string,
    url='https://github.com/coddingtonbear/bear-to-paper',
    description=(
        'Migrate your Bear notes to Paper.'
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bear-to-paper = bear_to_paper.cmdline:main'
        ],
    },
)
