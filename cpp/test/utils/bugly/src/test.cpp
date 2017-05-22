const char file_version[] __attribute__((section (".so_version"), used)) = "1.0.1";

const char* utils_so_version() 
{
    return file_version;
}

/* 
 * run:
 *     readelf -p .so_version out/libbugly.so
 * 
 * output:
 *     String dump of section '.so_version':
 *     [     0]  1.0.1
 *  */
