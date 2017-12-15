# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from epoch.items.DatasetItems import DatasetItems

class DatasetSpider(scrapy.Spider):
    name = 'Dataset'
    allowed_domains = ['www.bendixcarstensen.com/SDC/R-course']
    start_urls = ['http://www.bendixcarstensen.com/SDC/R-course/']

    # 如果urls有特殊处理可以放到这个函数中
    # def start_urls(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response):
        selector = Selector(response)
        item = DatasetItems()
        for link in selector.xpath('//ul/li/a'):
            uri = link.xpath('./@href')[0].get()
            file = link.xpath('./text()').get()
            # 排除/SDC/父目录
            if '.' in file:
                item['file_url'] = response.urljoin(uri)
                #  item['file'] = file
                yield item



""" index.html # {{{
 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">                              
 <html>
     <head>
         <title>Index of /SDC/R-course</title>
     </head>
     <body>
         <h1>Index of /SDC/R-course</h1>
         <ul>
             <li><a href="/SDC/"> Parent Directory</a></li>
             <li><a href="Fr31Oct14.pdf"> Fr31Oct14.pdf</a></li>
             <li><a href="Fr31Oct14.r"> Fr31Oct14.r</a></li>
             <li><a href="Fri12Dec2014.pdf"> Fri12Dec2014.pdf</a></li>
             <li><a href="Fri12Dec2014.r"> Fri12Dec2014.r</a></li>
             <li><a href="R-sq-demo.R"> R-sq-demo.R</a></li>
             <li><a href="Rinst.pdf"> Rinst.pdf</a></li>
             <li><a href="Rwork1.pdf"> Rwork1.pdf</a></li>
             <li><a href="Rwork2.pdf"> Rwork2.pdf</a></li>
             <li><a href="Simple.Rmd"> Simple.Rmd</a></li>
             <li><a href="cicurves.R"> cicurves.R</a></li>
             <li><a href="cont-eff.R"> cont-eff.R</a></li>
             <li><a href="cont-eff.pdf"> cont-eff.pdf</a></li>
             <li><a href="graphs.R"> graphs.R</a></li>
             <li><a href="linalg-notes-BxC.pdf"> linalg-notes-BxC.pdf</a></li>
             <li><a href="matrix-BxC.R"> matrix-BxC.R</a></li>
             <li><a href="models-BxC.R"> models-BxC.R</a></li>
             <li><a href="poppyr.R"> poppyr.R</a></li>
             <li><a href="reshape.r"> reshape.r</a></li>
             <li><a href="retin1.csv"> retin1.csv</a></li>
             <li><a href="retin2.csv"> retin2.csv</a></li>
             <li><a href="sdclr.R"> sdclr.R</a></li>
             <li><a href="vat.whr.Rda"> vat.whr.Rda</a></li>
         </ul>
         <address>Apache Server at www.bendixcarstensen.com Port 80</address>
     </body>
 </html>
"""# }}}
