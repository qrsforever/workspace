#include <iostream>

using namespace std;

void test_base()
{
	int tempA = 1;
	int tempB = 2;
	/*1.正常推断auto为int，编译通过*/
	auto autoTempA = tempA + tempB;

	/*2.正常推断auto为int，编译通过*/
	auto autoTempB = 1, *autoTempC = &autoTempB;

	/*3.autoTempD推断为int，autoTempE推断为double，编译不过*/
    /* auto autoTempD = 1, autoTempE = 3.14; */
}

void test_const()
{
	const int ctempA = 1;
	auto autoTempA = ctempA;

    /* error: assignment of read-only variable 'ctempA' */
    /* ctempA = 2; */

    /* cout << "autoTempA type: " << decltype(autoTempA) << endl; */

	/*1.cautoTempA推断为int，但是手动加了const，所以cautoTempA最终类型为const int*/
	const auto cautoTempA = ctempA;

    /* error: assignment of read-only variable 'cautoTempA' */
    /* cautoTempA = 3; */

    /* cout << "cautoTempA type: " << decltype(cautoTempA) << endl; */

	/*2.autoTempA推断为int，忽略顶层const*/
	autoTempA = 4;
}

void test_ref()
{
	int tempA = 1;
	int &refTempA = tempA;

	/*1.忽略引用，autoTempA推断为int，refAutoTempA被手动置为引用*/
	auto autoTempA = refTempA;
	auto &refAutoTempA = refTempA;

	autoTempA = 4;
	refAutoTempA = 3;

	/*2.输出为3,3,4,3*/
	cout << "tempA     = " << tempA << endl;
	cout << "refTempA  = " << refTempA << endl;
	cout << "autoTempA = " << autoTempA << endl;
	cout << "refAutoTempA = " << refAutoTempA << endl;
}

void test_pointer()
{
	int tempA = 1;
	const int ctempA = 2;

	/*1.ptrTempA中auto推断为int*，ptrTempB中推断为int  */
	auto  ptrTempA = &tempA;
	auto *ptrTempB = &tempA;    

	/*2.cptrTempA中auto推断为const int*，cptrTempB中推断为cosnt int  */
	auto  cptrTempA = &ctempA;
	auto *cptrTempB = &ctempA;

	/*3.ptrTempA和ptrTempB输出完全一致*/
	cout<<" ptrTempA = "<<ptrTempA<<endl;
	cout<<"*ptrTempA = "<<*ptrTempA<<endl;
	cout<<" ptrTempB = "<<ptrTempB<<endl;
	cout<<"*ptrTempB = "<<*ptrTempB<<endl;

	/*4.cptrTempA和cptrTempB输出完全一致*/
	cout<<" cptrTempA = "<<cptrTempA<<endl;
	cout<<"*cptrTempA = "<<*cptrTempA<<endl;
	cout<<" cptrTempB = "<<cptrTempB<<endl;
	cout<<"*cptrTempB = "<<*cptrTempB<<endl;
	/*5.cptrTempA指向的为const int，不能通过cptrTempA来修改其值，编译不过*/
	// *cptrTempA = 3;
}

int main(int argc, char *argv[])
{
	test_base();
	test_const();
    test_ref();
    test_pointer();
	return 0;
}
