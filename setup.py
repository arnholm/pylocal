import setuptools
setuptools.setup(   name='examplepackage',
                    version='0.2',
                    description='An example package',
                    url='#',
                    author='max',
                    install_requires=['opencv-python','tk'],
                    author_email='',
                    packages=setuptools.find_packages(),
                    zip_safe=False)