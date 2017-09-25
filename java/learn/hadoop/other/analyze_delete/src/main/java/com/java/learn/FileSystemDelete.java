package com.java.learn;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class FileSystemDelete {
    public static final Log LOG = LogFactory.getLog(FileSystemDelete.class);

    public static void main(String[] args) throws Exception {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(conf);
        LOG.info("FileSystemDelete Start!");
        Path p = new Path(uri);
        fs.delete(p, true);
        fs.close();
        LOG.info("FileSystemDelete End!");
    }
}
