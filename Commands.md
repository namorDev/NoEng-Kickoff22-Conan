# Lesson 0
- conan --version
# Lesson 1
- conan search
- conan remote list
- conan profile list
- conan profile --help
- conan profile show default
- cd consumer
- Have a look at conanfile.txt
- Have a look at sources and CMakeLists.txt
- mkdir build
- cd build
- conan install ..
- Error: missing prebuilt package
- conan install .. --build=missing
- inspect what conan created: conanbuildinfo.cmake
- conan search
- conan search poco/1.9.4@
- look again how the library is included in CMakeLists.txt, make the link to conanbuildinfo.cmake
- cmake ..
- cmake --build .
- bin/Consumer

# Lesson 2
- cd ../../producer
- Explain conanfile.py
- Add build_requires to conanfile.py
- mkdir build
- cd build
- conan install .. --build=missing
- conan build ..
- bin/Producer

# Lesson 3 - Create the package
- conan create . user/testing
- conan search
- conan search producer/0.1@user/testing
- conan remove producer
- conan export . user/testing
- conan search
- conan search producer/0.1@user/testing
- conan install producer/0.1@user/testing --build=hello
- conan search producer/0.1@user/testing





#TODO
- make a profile (that works), and use it. show profiles stuff