scrapy startproject crawl51job
scrapy genspider -t crawl s51job search.51job.com
scrapy crawl --nolog s51job
scrapy crawl --nolog s51job  -o /tmp/file.csv
