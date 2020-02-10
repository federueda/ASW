from pybuilder.core import init, use_plugin
from pybuilder.core import task
import os

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.sphinx") #documentation
use_plugin('pypi:pybuilder_pip_tools', '==1.*')

default_task = ["clean", "install_dependencies", "publish", "pip_sync", "pipreqs_task","sphinx_task"]

@init
def set_properties(project):
    project.set_property("coverage_exceptions", ['contracts','dsl'])

@init
def initialize(project):
	project.build_depends_on('pybuilder', '>0.9.0')
	project.get_property('pybuilder_pip_tools_build_urls').extend(['git+https://github.com/pybuilder/pybuilder.git#egg=pybuilder-0'])
	project.get_property('pybuilder_pip_tools_urls')
	project.build_depends_on('mockito')
	project.build_depends_on('pybuilder', '>0.9.0')
	project.set_property('sphinx_project_name', 'Pruebas')
	project.build_depends_on('pipreqs')

@task
def pipreqs_task():
	os.system("pipreqs ./src/main/python --force --savepath ./requirements.txt")

@task
def sphinx_task():
	os.system("pip3 install -r requirements.txt")
	os.chdir("./docs")
	os.system("make html")
