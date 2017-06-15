import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;

public class FileSystemCat {

    public static void main(String[] args) throws Exception {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(uri), conf);
        FSDataInputStream in = null;
        System.out.println("FileSystemCat Start!");
        byte[] buffer = new byte[20];
        try {
            in = fs.open(new Path(uri));
            in.seek(90);
            IOUtils.copyBytes(in, System.out, 4096, false);
            in.read(90, buffer, 0, 6);
            System.out.println("Read from offset (90 + 5) " + new String(buffer));
            in.seek(0);
            IOUtils.copyBytes(in, System.out, 4096, false);
        } finally {
            IOUtils.closeStream(in);
        }
        System.out.println("FileSystemCat End!");
    }
}
