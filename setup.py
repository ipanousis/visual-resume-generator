try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Resume Generator',
    'author': 'Yannis Panousis',
    'url': 'www.visual-resume.com/<your username>',
    'download_url': 'Where to download it.',
    'author_email': 'ipanousis156@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['resume-generator'],
    'scripts': [],
    'name': 'resume-generator'
}

setup(**config)
