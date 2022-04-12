import setuptools
setuptools.setup(   name='examplepackage',
                    version='0.1',
                    description='An example package',
                    url='#',
                    author='max',
                    install_requires=['opencv-python'],
                    author_email='',
                    packages=setuptools.find_packages(),
                    zip_safe=False)