# -*- coding: utf-8 -*-

import re
import subprocess

from setuptools import setup, find_namespace_packages


def version_from_git_tag():
    """Retrieve version from git history."""
    # Using package version according to PEP 440 -- Version Identification and Dependency Specification
    # https://www.python.org/dev/peps/pep-0440/#local-version-identifiers
    pattern = "^v((\\d+)\\.(\\d+)\\.(\\d+)((a|b|rc)\\d+)?(\\.post\\d+)?(\\.dev\\d+)?)(-(\\d+)-g([0-9a-f]{7}))?$"
    try:
        describe = subprocess.check_output(["git", "describe", "--tags", "--match", "v*", "--always"]).rstrip().decode()
    except subprocess.CalledProcessError:
        return "0.0.0+nogit"

    match = re.match(pattern, describe)
    if not match:
        return f"0.0.0+git{describe}"
    if match.group(10) and match.group(11):
        return f"{match.group(1)}+git{match.group(10)}.{match.group(11)}"
    return match.group(1)


setup(
    name='arm-avhclient',
    version=version_from_git_tag(),
    packages=find_namespace_packages(include=['arm.*']),
    install_requires=[
        'boto3~=1.20',
        'botocore~=1.20',
        'PyYAML~=6.0',
        'semantic_version~=2.9'
    ],
    extras_require={
        'dev': [
            'coverage~=6.2',
            'python-dateutil~=2.8',
            'pylint~=2.11',
            'restructuredtext_lint~=1.3',
            'setuptools~=59.4',
            'unittest-xml-reporting~=3.0'
        ]
    },
    entry_points={
        'console_scripts': ['avhclient=arm.avhclient.avh_cli:AvhCli']
    },
    python_requires='>=3.8',
    url='https://github.com/ARM-software/avhclient',
    author='Samuel Pelegrinello Caipers, Jonatan Antoni',
    author_email='Samuel.PelegrinelloCaipers@arm.com, Jonatan.Antoni@arm.com',
    description='Arm Virtual Hardware Command Line Interface',
    long_description=open('README.rst', encoding='UTF-8').read(),
    long_description_content_type='text/x-rst',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Build Tools"
    ]
)
