#
#     Kwola is an AI algorithm that learns how to use other programs
#     automatically so that it can find bugs in them.
#
#     Copyright (C) 2020  Kwola Software Testing Inc.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#


import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requirements = [
    "kwola"
]

setup(
    name='kwolaenterprise',
    version='0.0.1',
    description='Kwola Enterprise is the premium version of Kwola, designed for the needs of paying customers.',
    long_description=open("README.md", "rt").read(),
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
    ],
    author='',
    author_email='',
    url='',
    keywords='torch pytorch artificial intelligence',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
    },
    package_data={
        'kwolaenterprise': [
        ]
    },
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
        ]
    }
)
