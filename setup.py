from setuptools import setup, find_packages

setup(
    name="django-youtubefield",
    version = ":versiontools:youtubeurl_field:",
    url='http://github.com/ko1es/django-youtubefield',
    #license='BSD',
    platforms=['OS Independent'],
    description="Youtube url field for django models.",
    setup_requires = [
        'versiontools >= 1.4',
    ],
    install_requires = [],
    #long_description=open('README.rst').read(),
    author='Kolesnikov Nikita',
    author_email='koles.web@gmail.com',
    maintainer='Kolesnikov Nikita',
    maintainer_email='koles.web@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
