
if [ x$1 == x ];
then
    echo "no input"
    exit 0
fi

str=$1

# test.apk.apk ----> apk
if [ ${str##*.} == "apk" ]
then
    echo "apk"
fi

# test.apk.apk ----> apk.apk
if [ ${str#*.} == "apk.apk" ]
then
    echo "apk.apk"
fi

# test.apk.apk ----> test
if [ ${str%%.*} == "test" ]
then
    echo "test"
fi

# test.apk.apk ----> test
if [ ${str%.*} == "test.apk" ]
then
    echo "test.apk"
fi
