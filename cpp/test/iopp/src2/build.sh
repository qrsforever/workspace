if [[ $# = 1 ]]
then
    file=$1
    echo "gcc -g -o g${file%%.c} $file"
    rm -f g${file%%.c} ioppw.txt
    gcc -g -o g${file%%.c} $file
fi
