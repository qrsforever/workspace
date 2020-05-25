{
    datasets: {
        b: 10,
    } + { a: std.parseJson('{"aa":10}') },

    len: std.length({ a: 10 }),

    test: if false then { v1: 1 }
    else if true then { v2: 2 }
    else {},
}
