# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from link_migration.version import version


long_description = "A generic tool for migrate in python. https://github.com/takamuffin/link_migration"


setup(name='link_migration',
      version=version,
      description="A generic tool for migrate in python.",
      long_description=long_description,
      classifiers=[],
      keywords='migration',
      author='Alex Sansone',
      author_email='aeris1987@gmail.com',
      url='https://github.com/takamuffin/link_migration',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'link_migration']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "termcolor"
      ],

      entry_points={
            'console_scripts': [
                'link_migration = link_migration.runner:link_migration',
            ]
        },
      )
