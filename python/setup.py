import setuptools


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
