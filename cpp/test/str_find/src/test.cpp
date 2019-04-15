/***************************************************************************
 *  test.cpp - 
 *
 *  Created: 2019-03-20 10:08:37
 *
 *  Copyright QRS
 ****************************************************************************/

#include <string>
#include <iostream>

using namespace std;

int main(void)
{
    string service = "nativelog:-v";
    size_t found = service.find_first_of(':');
    if (found != string::npos) {
        cout << service.substr(0, found) << endl;
    }
    return 0;
}

