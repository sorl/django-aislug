from setuptools import setup, find_packages
from setuptools.command.test import test


class TestCommand(test):
    def run(self):
        from tests.runtests import runtests
        runtests()

setup(
    name='django-aislug',
    version='0.2.2',
    description='Intelligent slug computing',
    long_description=open('README.rst').read(),
    author='Mikko Hellsing',
    author_email='mikko@aino.se',
    license='BSD',
    url='https://github.com/aino/django-aislug',
    platforms='any',
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    cmdclass={"test": TestCommand},
    install_requires=[
        'django-stringfield>=0.1.5',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)

