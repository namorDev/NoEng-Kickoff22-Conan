from conans import ConanFile , tools, CMake
from conan.tools.cmake import CMakeToolchain

class MyProjectConan(ConanFile):
    name = "producer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Producer"]
        self.cpp_info.libdirs = ['lib']