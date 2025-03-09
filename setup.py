from setuptools import setup, find_packages

setup(
    name='django-reality-polls',
    version='0.1',
    packages=find_packages(),
    description='A simple Django app to conduct web-based polls.',
    long_description=open('README.rst').read(),
    author='Yaswanth Reddy',
    author_email='yaswanthreddypanem@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
