from setuptools import setup

setup(
    name = 'quantum',
    version = '0.0.1',
    author = 'Matt Hoffman',
    author_email = 'mjhoffman65@gmail.com',
    description = 'money management tool',
    license = 'BSD',
    packages=['quantum', 'tests'],
    install_requires = [
        'Flask==0.10.1',
        'uWSGI==2.0.12',
    ],
)
