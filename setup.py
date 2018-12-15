from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [Extension("example_cy", ["example_cy.pyx"])]

setup(name = 'example_cy', cmdclass = {'build_ext': build_ext}, ext_modules = ext_modules)
##setup(ext_modules = cythonize('example_cy.pyx'))


