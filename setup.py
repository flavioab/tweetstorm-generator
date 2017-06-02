from setuptools import setup, find_packages
import os
import re


def get_version(package):
    """
    Based in https://github.com/tomchristie/django-rest-framework/blob/
    971578ca345c3d3bae7fd93b87c41d43483b6f05/setup.py
    :param package Package name
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


LONG_DESCRIPTION = open('README.md').read()


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='tweetstorm-generator',
    version=get_version('tweetstorm_generator'),
    packages=find_packages(),
    url='https://github.com/flavioab/tweetstorm_generator',
    license='MIT License',
    author='Flávio Briz',
    author_email='flavio.briz@gmail.com',
    keywords='twitter tweet storm generator',
    description='Don not limit yourself to 140 characters.',
    include_package_data=True,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': [
            'tweetstorm-generator = tweetstorm_generator.__main__:main'
        ]
    },
    test_suite='tests',
)
