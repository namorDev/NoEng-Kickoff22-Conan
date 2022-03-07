# Lesson 0
- conan --version
# Lesson 1 - Simple consumer
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

# Lesson 2 - Create producer application
- cd ../../producer
- Explain conanfile.py
- mkdir build
- cd build
- conan install .. --build=missing
- **conan build ..**
- bin/Producer

# Lesson 3 - Create the package as library
- modify hello.cpp and hello.h
- modify CMakeLists.txt and change to a library
- conan create . user/testing
- conan search
- conan search producer/0.1@user/testing
- conan remove producer
- show what conan create is doing actually
- conan export . user/testing
- conan search
- conan search producer/0.1@user/testing
- conan install producer/0.1@user/testing --build=hello
- conan search producer/0.1@user/testing
- inspect conan cache: code ~/.conan/data 

# Lesson 4 - Use the package in consumer
- conan remove producer (not really needed, if already there)
- modify creator main.cpp to use producer
- cd consumer/build
- conan install .. --build=missing
- conan export ../../producer user/testing (not needed if already there)
- cmake ..
- cmake --build .
- bin/Consumer

# Lesson 5 - Use the build_requires attribute, use a profile
- Add build_requires to conanfile.py
- cd producer/build
- inspect profiles
- conan install .. -pr ../../profiles/my_profile
- add remote from namordev (because already built with this profile, otherwise poco is built again)
- cd consumer/build
- conan install .. -pr ../../profiles/my_profile
- cmake .. -DCMAKE_CXX_COMPILER=clang++-12
- cmake --build .

TODO: get it from artifactory

optional to show: 
- how to upload a package
- how to install config / profile
- test_package
- Adding conan config and remotes is usually done within the dockerfile in enterprise usage
