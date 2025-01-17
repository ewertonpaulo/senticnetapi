try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['senticnet']
requires = []

setup(name='senticnet',
      version='1.3',
      description='Access SenticNet API using Python',
      long_description=open('README.md').read(),
      author=u'Yuri Malheiros',
      author_email='yuri@dcx.ufpb.br',
      url='https://github.com/yurimalheiros/senticnetapi',
      packages=packages,
      package_data={'': ['LICENSE', 'README.md'], 'senticnet': []},
      package_dir={'senticnet': 'senticnet'},
      include_package_data=True,
      license=open('LICENSE', encoding="utf8").read(),
      zip_safe=False,
      install_requires=[],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries'],
)
