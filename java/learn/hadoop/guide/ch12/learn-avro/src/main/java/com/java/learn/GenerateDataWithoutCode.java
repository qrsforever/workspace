package com.java.learn;

import java.io.File;
import java.io.IOException;

import org.apache.avro.Schema;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumWriter;

public class GenerateDataWithoutCode {
    public static void main(String[] args) throws IOException {
        // getResourceAsStream() clasess目录下
        Schema schema = new Schema.Parser().parse(
                GenerateDataWithoutCode.class.getClassLoader().getResourceAsStream("employee.avsc"));

        GenericRecord emp1 = new GenericData.Record(schema);
        emp1.put("name", "Siva");
        emp1.put("joining_date", "10-01-2013");
        emp1.put("role", "Architect");
        emp1.put("salary", 30000.0f);

        GenericRecord emp2 = new GenericData.Record(schema);
        emp2.put("name", "Krish");
        emp2.put("joining_date", "10-11-2008");
        emp2.put("role", "Lead Architect");
        emp2.put("dept", "BIFS");
        emp2.put("salary", 90000.0f);

        File file = new File("employees.avro");
        DatumWriter<GenericRecord> datumWriter = new GenericDatumWriter<GenericRecord>(schema);
        DataFileWriter<GenericRecord> dataFileWriter = new DataFileWriter<GenericRecord>(datumWriter);
        dataFileWriter.create(schema, file);
        dataFileWriter.append(emp1);
        dataFileWriter.append(emp2);        
        dataFileWriter.close();
    }
}
