from conans import ConanFile, tools
import os

class SyphonConan(ConanFile):
    name = 'syphon'

    source_version = '5'
    package_version = '1'
    version = '%s-%s' % (source_version, package_version)

    build_requires = (
        'llvm/5.0.2-1@vuo/stable',
        'macos-sdk/11.0-0@vuo/stable',
    )
    settings = 'os', 'compiler', 'build_type', 'arch'
    url = 'https://github.com/Syphon/Syphon-Framework'
    license = 'https://github.com/Syphon/Syphon-Framework/blob/master/License.txt'
    source_dir = 'Syphon-Framework-%s' % source_version

    def source(self):
        tools.get('https://github.com/Syphon/Syphon-Framework/archive/%s.tar.gz' % self.source_version,
                  sha256='0af48a58e07bc957e1f330dabf422973d50086f7ce6a9f623e2b3a5478ff5661')

        self.run('mv %s/License.txt %s/%s.txt' % (self.source_dir, self.source_dir, self.name))

    def build(self):
        with tools.chdir(self.source_dir):
            self.run('xcodebuild ARCHS="x86_64 arm64" VALID_ARCHS="x86_64 arm64" MACOSX_DEPLOYMENT_TARGET=10.11 OTHER_LDFLAGS="-Wl,-macos_version_min,10.11"')

    def package(self):
        self.copy('*', src='%s/build/Release/Syphon.framework' % self.source_dir, dst='lib/Syphon.framework', symlinks=True)
        self.copy('%s.txt' % self.name, src=self.source_dir, dst='license')

    def package_info(self):
        self.cpp_info.frameworkdirs = ['%s/lib' % self.package_folder]
        self.cpp_info.frameworks = ['Syphon']
