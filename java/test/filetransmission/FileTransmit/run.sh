#!/bin/bash

ant clean
ant jar
echo "java -cp bin/jar/FileTransmit-*.jar edu.logic.server.Server"
echo "java -cp bin/jar/FileTransmit-*.jar edu.logic.client.Client"
