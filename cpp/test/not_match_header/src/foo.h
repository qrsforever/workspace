#ifndef __foo_H__
#define __foo_H__

#ifndef ONE

class Foo {
public:
    Foo();
    ~Foo();
    int init();
    int test();
};

#else

class Foo {
public:
    int test();
};

#endif


#ifdef __cplusplus


#endif /* __cplusplus */

#endif /* __foo_H__ */
