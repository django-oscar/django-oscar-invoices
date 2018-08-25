from setuptools import find_packages, setup

test_requires = [
    'pytest>=3.6.0',
    'pytest-django',
    'django-webtest==1.9.3'
]

setup(
    name='django-oscar-invoices',
    version='0.1',
    url='https://github.com/oscaro/django-oscar-invoices',
    author='Metaclass Team',
    author_email='sasha@metaclass.co',
    description='Invoices generation for Django Oscar',
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'phonenumbers',
        'pillow==5.0.0',
        'django>=1.11,<2.2',
        'django-oscar>=1.6',
        'django-phonenumber-field>=2.0,<2.1',
    ],
    extras_require={
        'test': test_requires,
    },
    test_requires=test_requires
)
