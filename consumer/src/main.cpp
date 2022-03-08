#include <iostream>

#include <Poco/String.h>


using Poco::toUpper;

int main()
{
    std::string hello_string("Hello, world from Consumer!");
    std::string s1(toUpper(hello_string)); 

    std::cout << s1 << std::endl;


    return 0;
}