package com.java.learn;
 
import java.io.File;
import java.io.IOException;
 
import org.apache.avro.Schema;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumReader;
 
public class DeserializeWithoutCode {
    public static void main(String[] args) throws IOException {
        Schema schema = new Schema.Parser().parse(new File("employee.avsc"));
        GenericRecord emp = new GenericData.Record(schema);

        File file = new File("employees.avro");

        DatumReader<GenericRecord> datumReader = new GenericDatumReader<GenericRecord>(schema);
        DataFileReader<GenericRecord> dataFileReader = new DataFileReader<GenericRecord>(file, datumReader);

        while (dataFileReader.hasNext()) {
            emp = dataFileReader.next();
            System.out.println(emp);
        }
        dataFileReader.close();
    }
}
