import java.io.InputStream;
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;

public class FileSystemCat {

    public static void main(String[] args) throws Exception {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(uri), conf);
        InputStream in = null;
        System.out.println("FileSystemCat Start!");
        try {
            in = fs.open(new Path(uri));
            IOUtils.copyBytes(in, System.out, 3096, false);
        } finally {
            IOUtils.closeStream(in);
        }
        System.out.println("FileSystemCat End!");
    }
}
