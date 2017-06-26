package com.java.learn;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Admin;
import org.apache.hadoop.hbase.client.Append;  
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.util.Bytes;

public class ExampleClient {
    public static void main(String[] args) throws IOException {
        Configuration config = HBaseConfiguration.create();
        Connection connection = ConnectionFactory.createConnection(config);
        try {
            // Create table
            Admin admin = connection.getAdmin();
            try {
                TableName tableName = TableName.valueOf("test");
                // 表名
                HTableDescriptor htd = new HTableDescriptor(tableName);
                // 列族
                HColumnDescriptor hcd = new HColumnDescriptor("data");
                // 表中增加列族
                htd.addFamily(hcd);
                if (admin.tableExists(tableName)) {
                    System.out.println("TableName " + tableName + " exists");
                    admin.disableTable(tableName);
                    // Truncate 操作
                    admin.truncateTable(tableName, false);
                } else 
                    admin.createTable(htd);
                HTableDescriptor[] tables = admin.listTables();
                if (tables.length != 1 
                        && Bytes.equals(tableName.getName(), tables[0].getTableName().getName())) {
                    throw new IOException("Failed create of table");
                }
                // Run some operations -- three puts, a get, and a scan -- against the table.
                Table table = connection.getTable(tableName);
                try {
                    // Put 操作
                    for (int i = 1; i <= 3; i++) {
                        byte[] row = Bytes.toBytes("row" + i);
                        Put put = new Put(row);
                        byte[] columnFamily = Bytes.toBytes("data");
                        byte[] qualifier = Bytes.toBytes(String.valueOf(i));
                        byte[] value = Bytes.toBytes("value" + i);
                        put.addColumn(columnFamily, qualifier, value);
                        table.put(put);
                    }

                    // Append 操作 (追加到原来value的后面)
                    Append append = new Append(Bytes.toBytes("row3")); 
                    append.add(Bytes.toBytes("data"), Bytes.toBytes("3"), Bytes.toBytes("3"));
                    table.append(append);

                    // Get 操作(通过Key查找)
                    Get get = new Get(Bytes.toBytes("row1"));
                    Result result = table.get(get);
                    System.out.println("Get: " + result); // 二进制存储所以只打印出了结构

                    // Scan 操作
                    Scan scan = new Scan();
                    ResultScanner scanner = table.getScanner(scan);
                    try {
                        for (Result scannerResult: scanner) {
                            System.out.println("Scan: " + scannerResult);
                        }
                    } finally {
                        scanner.close();
                    }

                    // Drop 操作
                    // admin.disableTable(tableName);
                    // admin.deleteTable(tableName);
                } finally {
                    table.close();
                }
            } finally {
                admin.close();
            }
        } finally {
            connection.close();
        }
    }
}
