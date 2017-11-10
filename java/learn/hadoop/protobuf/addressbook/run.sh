#!/bin/bash

protoc -I=. --cpp_out=cpp --python_out=python --java_out=java/src facestyle.proto addressbook.proto 
