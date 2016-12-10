import os
import sys

sys.path.append('tools')

from ModuleUtils import *

env = Environment(
        tools_path = 'tools'
        )

libs = SConscript(os.path.join('src', 'SConscript'), {'env':env}, variant_dir='build', duplicate=0)
print 'count_so:%d'%len(libs)
libs.extend(env.SharedObject('main.c'))
env.Program('test', libs)
