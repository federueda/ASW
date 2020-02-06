from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")
use_plugin("python.sphinx") #documentation
use_plugin('pypi:pybuilder_pip_tools', '==1.*') #requirements.txt

default_task = "publish"

@init
def initialize(project):
    project.build_depends_on('mockito')
    project.build_depends_on('pybuilder', '>0.9.0')
    project.get_property('pybuilder_pip_tools_build_urls').extend(['git+https://github.com/pybuilder/pybuilder.git#egg=pybuilder-0'])
