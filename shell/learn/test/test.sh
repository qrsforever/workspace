# !/bin/bash

# http://www.zsythink.net/archives/2252/

defA=abcdef

# unset undefB

nullStrC=""

echo "echo \$defA: $defA"
echo "echo \$undefB: $undefB"
echo "echo \$nullStrC: $nullStrC"

echo ""

[ $defA ]
echo "[ \$defA ] : $?"

[[ $defA ]]
echo "[[ \$defA ]] : $?"

[ ! $defA ]
echo "[ ! \$defA ] : $?"

[[ ! $defA ]]
echo "[[ ! \$defA ]] : $?"

! [ $defA ]
echo "! [ \$defA ] : $?"

! [[ $defA ]]
echo "! [[ \$defA ]] : $?"

echo ""

[ $undefB ]
echo "[ \$undefB ] : $?"

[[ $undefB ]]
echo "[[ \$undefB ]] : $?"

[ ! $undefB ]
echo "[ ! \$undefB ] : $?"

[[ ! $undefB ]]
echo "[[ ! \$undefB ]] : $?"

! [ $undefB ]
echo "! [ \$undefB ] : $?"

! [[ $undefB ]]
echo "! [[ \$undefB ]] : $?"

echo ""

[ $nullStrC ]
echo "[ \$nullStrC ] : $?"

[[ $nullStrC ]]
echo "[[ \$nullStrC ]] : $?"

! [ $nullStrC ]
echo "! [ \$nullStrC ] : $?"

! [[ $nullStrC ]]
echo "! [[ \$nullStrC ]] : $?"

[ ! $nullStrC ]
echo "[ ! \$nullStrC ] : $?"

[[ ! $nullStrC ]]
echo "[[ ! \$nullStrC ]] : $?"

echo ""

test $defA
echo "test \$defA : $?"

test -z $defA
echo "test -z \$defA : $?"

test -n $defA
echo "test -n \$defA : $?"

echo ""

test $undefB
echo "test \$undefB : $?"

test -z $undefB
echo "test -z \$undefB : $?"

test -n $undefB
echo "test -n \$undefB : $?"

echo ""

test $nullStrC
echo "test \$nullStrC : $?"

test -z $nullStrC
echo "test -z \$nullStrC : $?"

test -n $nullStrC
echo "test -n \$nullStrC : $?"

echo -e "\n --------------------test 命令垃圾啊 ---------------------- \n"
