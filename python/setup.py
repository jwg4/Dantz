import setuptools


dantz_ext = setuptools.Extension(
    'dantz',
    sources=['src/DataObject.cpp', 'src/TableFactory.cpp'],
    headers=['src/DataObject.h', 'src/TableFactory.h']
)

setuptools.setup(
    name='Dantz',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    version='0.1.0',
    packages=['dantz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    ext_modules=[dantz_ext]
)
