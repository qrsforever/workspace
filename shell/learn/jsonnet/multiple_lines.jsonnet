local longtest(a) = {
    a: a,
};

{
    aaa: |||
        Hello longggggggggggggggggggggggggggg
        World
    |||,
    bbb: longtest(|||
        aaaaaaaaaaaaaaaaaaaaaaaaa
        bbbbbbbbbbbbbbbbbbbbbbbbb
    |||),
}
