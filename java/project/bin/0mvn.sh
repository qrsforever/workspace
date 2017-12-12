#!/bin/bash

# mvn archetype:generate -DgroupId=com.java.learn -DartifactId=top -DpacakgeName=com.java.learn -DinteractiveMode=false

default_groupId=com.java.learn
default_artifactId=demo
default_packageName=$default_groupId
default_interactiveMode=false

__archetype_generate() {
    echo -n "-DgroupId=[$default_groupId] "
    read groupId
    if [[ x$groupId == x ]]
    then
        groupId=$default_groupId
    fi
    echo -n "-DartifactId=[$default_artifactId] "
    read artifactId
    if [[ x$artifactId == x ]]
    then
        artifactId=$default_artifactId
    fi
    echo -n "-DpackageName=[$default_packageName] "
    read packageName
    if [[ x$packageName == x ]]
    then
        packageName=$default_packageName
    fi
    echo -n "-DinteractiveMode=[$default_interactiveMode] "
    read interactiveMode
    if [[ x$interactiveMode == x ]]
    then
        interactiveMode=$default_interactiveMode
    fi
    echo -e "mvn archetype:generate\n\t-DgroupId=$groupId\n\t-DartifactId=$artifactId\n\t-DpacakgeName=$packageName\n\t-DinteractiveMode=$interactiveMode"
    echo -n "Conform(y/n): "
    read n
    if [[ x$n == xy ]]
    then
        mvn archetype:generate -DgroupId=$groupId -DartifactId=$artifactId -DpacakgeName=$packageName -DinteractiveMode=$interactiveMode
    fi
}

__main() {
    if [[ x$1 == x ]]
    then
        echo "1. archetype:generate"
        echo "2. dependency:sources"
        echo "3. dependency:resolve -Dclassifier=javadoc"
        echo "4. eclipse:eclipse"
        echo "5. package without test" 
        echo -n "Select: "
        read n
    else
        n=$1
    fi

    case $n in 
        '1')
            __archetype_generate
            ;;
        '2')
            mvn dependency:sources
            ;;
        '3')
            mvn dependency:resove -Dclassifier=javadoc
            ;;
        '4')
            mvn eclipse:eclipse
            ;;  
        '5')
            mvn package -Dmaven.test.skip=true
            ;;
        *)
            echo "error select ($n)"
    esac
}

__main $*
