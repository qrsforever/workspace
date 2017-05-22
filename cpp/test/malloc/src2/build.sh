if [[ $# = 1 ]]
then
    file=$1
    echo "gcc -g -o g${file%%.c} $file"
    gcc -g -o g${file%%.c} $file
fi
