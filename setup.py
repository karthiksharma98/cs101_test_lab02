from setuptools import setup

if __name__ == "__main__":
    setup(
       name='cs101_test_lab02',
       version='1.0',
       description='Unit tests for complex and interval labs',
       author='N E Davis',
       author_email='davis68@illinois.edu',
       packages=['cs101_test_lab02'],  #same as name
       install_requires=['pytest', 'numpy'], #external packages as dependencies
       license='MIT'
    )
