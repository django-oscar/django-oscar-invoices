from setuptools import find_packages, setup


setup(
    name='django-oscar-invoices',
    version='0.2.1',
    url='https://github.com/django-oscar/django-oscar-invoices',
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
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'phonenumbers',
        'pillow',
        'django>=1.11,<4.0',
        'django-oscar>=2.0',
        'django-phonenumber-field>=3.0.0,<6.0.0',
    ]
)
