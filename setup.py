from setuptools import setup, find_packages

with open('README.txt') as f:
    readme = f.read()
    f.close()

with open('LICENSE.txt') as f:
    license = f.read()
    f.close()

setup(
    name='ds-algorithms',
    version='0.1.0',
    description='Data structures and algorithms',
    long_description=readme,
    author='Utku Çam',
    author_email='utkucam2@gmail.com',
    url='https://github.com/utkucm/DS-Algorithms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
)
