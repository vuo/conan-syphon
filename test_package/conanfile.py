from conans import ConanFile, CMake
import platform

class SyphonTestConan(ConanFile):
    generators = 'cmake'
    requires = (
        'llvm/5.0.2-1@vuo/stable',
        'macos-sdk/11.0-0@vuo/stable',
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.run('install_name_tool -change @loader_path/../Frameworks/Syphon.framework/Versions/A/Syphon @loader_path/../lib/Syphon.framework/Versions/A/Syphon bin/test_package')

    def imports(self):
        self.copy('*', src='bin', dst='bin')
        self.copy('*', src='lib', dst='lib')

    def test(self):
        self.run('./bin/test_package')
