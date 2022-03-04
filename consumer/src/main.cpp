#include <iostream>

#include <Poco/String.h>

using Poco::toUpper;

int main()
{
    std::string hello("Hello, world!");
    std::string s1(toUpper(hello)); 

    std::cout << s1 << std::endl;

    return 0;
}