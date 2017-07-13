import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MaxTemperature {

    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Usage: MaxTemperature <input path> <output path>");
            System.exit(-1);
        }

        Job job = new Job();
        job.setJarByClass(MaxTemperature.class);
        job.setJobName("Max temperature");

        // 输入/输出文件
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        /**
         *  InputFormat类的作用是将输入的数据分割成splits,并将splits进一步拆成<K,V>
         *  可以通过setInputFormatClass()方法进行设置
         *  默认为TextInputFormat.class，默认情况可以不写
         **/
        // job.setInputFormatClass(TextInputFormat.class);

        /**
         *  OutputFormat类，负责输出最终结果
         *  可以通过setOutputFormatClass()方法进行设置
         *  默认TextOutputFormat.class，默认情况可以不写，此时输入即输出
         */
        // job.setOutputFormatClass(TextOutputFormat.class);

        /**
         *  Mapper类的作用是实现map函数，将splits作为输入生成一个结果
         *  可以通过setMapperClass()方法进行设置
         *  默认为Mapper.class，默认情况可以不写,此时输入即输出
         */
        job.setMapperClass(MaxTemperatureMapper.class);
        job.setReducerClass(MaxTemperatureReducer.class);

        /**
         *  Combiner类的作用是实现combine函数，将mapper的输出作为输入，合并具有形同key值得键值对
         *  可以通过setCombinerClass()方法进行设置
         *  默认为null，默认情况不写，此时输入即输出
         */
        // job.setCombinerClass(xx.class);
        
        /**
         *  Partitioner类的作用是实现getPartition函数，用于在洗牌过程中将由Mapper输入的结果分成R份，每份交给一个Reducer
         *  可以通过setPartitionerClass()方法进行设置
         *  默认为HashPartitioner.class,默认情况可以不写，此时输入即输出
         */
        // job.setPartitionerClass(xx.class);


        // 设置map/reduce函数输出类型
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        // 等待结果
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
