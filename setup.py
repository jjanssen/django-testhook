from setuptools import setup, find_packages
from testhook import __version__

# Testing dependencies
test_extras = [
    'coverage>=4.0.3',
    'flake8>=2.5.2',
    'tox>=2.3.1'
]

setup(
    name='django-testhook',
    version=__version__,
    license='Apache License, Version 2.0',

    requires=[
        'Django (>=1.8)',
    ],

    description='''A Django template tag to enable testhook
        attributes on HTML elements.''',
    long_description=open('README.md').read(),

    author='Janneke Janssen',
    author_email='j.janssen@lukkien.com',

    keywords='templatetag testhook django',

    url='http://github.com/jjanssen/django-testhook',

    packages=find_packages(),
    include_package_data=True,

    test_suite='runtests',

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],

    extras_require={
        'test': test_extras
    },
)
