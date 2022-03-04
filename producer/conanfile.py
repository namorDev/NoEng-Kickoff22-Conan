from conans import ConanFile
from conan.tools.cmake import CMake

class MyProjectConan(ConanFile):
    name = "my_project"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.10.0"

    generators = "CMakeToolchain", "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()