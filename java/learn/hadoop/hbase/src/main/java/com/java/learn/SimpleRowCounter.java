package com.java.learn;

import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.filter.FirstKeyOnlyFilter;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.mapreduce.TableMapper;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.output.NullOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class SimpleRowCounter extends Configured implements Tool {

    static class RowCounterMapper extends TableMapper<ImmutableBytesWritable, Result> {
        public static enum Counters { ROWS }

        @Override
        public void map(ImmutableBytesWritable row, Result value, Context context) {
            // Context 是 Mapper的内部里的， 可以记录些东西
            // public Counter getCounter(Enum<?> counterName)
            context.getCounter(Counters.ROWS).increment(1);
            System.out.println("Count: " + context.getCounter(Counters.ROWS).getValue());
        }
    }

    @Override
    public int run(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: SimpleRowCounter <tablename>");
            return -1;
        }
        String tableName = args[0];
        Scan scan = new Scan();
        scan.setFilter(new FirstKeyOnlyFilter());

        // 设置作业的类 Hadoop会根据这个类找到其所在的jar包
        // getConf <== HBaseConfiguration.create()
        Job job = Job.getInstance(getConf(), getClass().getSimpleName());
        job.setJarByClass(getClass());
        // scan Hbase表， 输出Key-Value : ImmutableBytesWritable - Result 
        TableMapReduceUtil.initTableMapperJob(tableName, scan,
                RowCounterMapper.class, ImmutableBytesWritable.class, Result.class, job);
        job.setNumReduceTasks(0);
        job.setOutputFormatClass(NullOutputFormat.class);
        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static void main(String[] args) throws Exception {
        // 方式一
        int exitCode = ToolRunner.run(HBaseConfiguration.create(),
                new SimpleRowCounter(), args);
        System.exit(exitCode);

        // 方式二
        // String tableName = args[0];
        // Scan scan = new Scan();
        // scan.setFilter(new FirstKeyOnlyFilter());

        // // 设置作业的类 Hadoop会根据这个类找到其所在的jar包
        // // getConf <== HBaseConfiguration.create()
        // Job job = Job.getInstance(HBaseConfiguration.create(), SimpleRowCounter.class.getName());
        // job.setJarByClass(SimpleRowCounter.class);
        // TableMapReduceUtil.initTableMapperJob(tableName, scan,
        //         RowCounterMapper.class, ImmutableBytesWritable.class, Result.class, job);
        // job.setNumReduceTasks(0);
        // job.setOutputFormatClass(NullOutputFormat.class);
        // job.waitForCompletion(true);
    }
}
