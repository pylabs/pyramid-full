import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'alembic',
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_mailer',
    'pyramid_wtforms',
    'pyramid_tm',
    'pyramid_sqlalchemy',
    'pyramid_redis_sessions',
    'pyramid_i18n_wrapper',
    'waitress',
    'invoke'
]

tests_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
    'pytest-mock'
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.0',
    description='{{ cookiecutter.project_name }}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = {{ cookiecutter.repo_name }}:main',
        ],
    },
)
