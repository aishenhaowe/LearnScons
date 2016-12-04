import os

class Module(object):
    def __init__(self, name, env, components=None):
        self.name = name
        self.env = env
        if components is None:
            self.components = []
        else:
            self.components = components
        self.subproducts = []
        self.test_libs_name = []
        self.need_libs = []

    def add_lib_into_list(self, lib_name):
        self.test_libs_name.append(lib_name)

    def build(self):
        print '---->name:%s'%self.name
        for component in self.components:
            build_lib = self.env.SConscript(os.path.join(component, 'SConscript'), {'env':self.env})
            self.subproducts.extend(build_lib)

            if component in self.test_libs_name:
                self.need_libs.append(build_lib)
                self.env.Append(LIBS=[build_lib])
                self.env.Append(LIBPATH=[os.path.join(component, 'private')])

        self.env.Append(CPPPATH=[os.path.join(os.path.abspath('.'), 'private')])
        source_files = self.env.Glob(os.path.join('.', 'private', '*.c'))
#        libs = self.env.SharedObject(source_files, LINKFLAGS='-static-libgcc')
        libs = self.env.SharedObject(source_files)
        self.subproducts.extend(libs)

        return self.subproducts
