from setuptools import find_packages, setup


setup(
    name='django-oscar-invoices',
    version='0.2.2',
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
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9.18',
    ],
    install_requires=[
        'phonenumbers',
        'pillow',
        'django>=4.2.6',
        'django-oscar>=3.2.2',
        'django-phonenumber-field>=6.4.0',
    ]
)
