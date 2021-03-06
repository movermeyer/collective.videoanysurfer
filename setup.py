from setuptools import setup, find_packages
import os

version = '1.0.9.dev0'

setup(
    name='collective.videoanysurfer',
    version=version,
    description="Youtube Integration to be AnySurfer compliant",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
    ],
    keywords='plone video anysurfer',
    author='JeanMichel FRANCOIS',
    author_email='toutpt@gmail.com',
    url='https://github.com/collective/collective.videoanysurfer',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.js.nomensamediaplayer',
        'collective.captionmanager',
        # -*- Extra requirements: -*-
    ],
    extras_require=dict(
        test=['plone.app.testing'],
    ),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
