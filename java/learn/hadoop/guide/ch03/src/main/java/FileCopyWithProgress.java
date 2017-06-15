import java.io.InputStream;
import java.io.OutputStream;
import java.net.URI;
import java.io.FileInputStream;
import java.io.BufferedInputStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.util.Progressable;

public class FileCopyWithProgress {
    public static void main(String[] args) throws Exception {
        String srcPath = args[0];
        String dstPath = args[1];

        InputStream in = new BufferedInputStream(new FileInputStream(srcPath));
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem.get(URI.create(dstPath), conf);
        OutputStream out = fs.create(new Path(dstPath), new Progressable() {

            @Override
            public void progress() {
                System.out.print(".");
            }

        });
        // true: 执行完之后关闭out
        IOUtils.copyBytes(in, out, 4096, true);
    }
}
