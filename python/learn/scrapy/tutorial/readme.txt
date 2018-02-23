1. 建立工程
scrapy startproject tutorial

2. 运行
scrapy crawl quotes

3. 单独爬取一个页面, 和工程没有关系
scrapy shell 'http://quotes.toscrape.com/page/1/'
>>> 
    response.css('title')
    response.css('title').extract()
    response.css('title::text').extract()
    response.css('title::text').extract_first()
    response.css('title::text')[0].extract()
    response.css('title::text').re(r'Quotes.*')
    response.css('title::text').re(r'Q\w+')
    response.css('title::text').re(r'(\w+) to (\w+)')

    response.xpath('//title')
    response.xpath('//title/text()').extract_first()

scrapy shell 'http://quotes.toscrape.com'
>>> 
    response.css("div.quote")
    quote = response.css("div.quote")[0]
    title = quote.css("span.text::text").extract_first() // .后面是class, ::后面是属性或者text
    author = quote.css("small.author::text").extract_first()
    tags = quote.css("div.tags a.tag::text").extract()   // div.tags a.tag 是css层包含关系 
    response.css('li.next a').extract_first()
    response.css('ul.pager li.next a').extract_first()
    response.css('li.next a::attr(href)').extract_first() // ::attr(属性名)


cmdline:
  
    scrapy genspider -l  // 列出spider模板
    scrapy genspider example example.com // 默认basic
    scrapy genspider -t crawl scrapyorg scrapy.org // 模板crawl
    scrapy crawl <spider>
    scrapy check [-l] <spider>
    scrapy list // 显示所有的spider
    scrapy fetch --nolog http://www.example.com/some/page.html
    scrapy fetch --nolog --headers http://www.example.com
    scrapy runspider <spider_file.py>


注意:
1. response.css 返回的是selector list, 是个列表


# settings.py: 
# EXTENSIONS = {
#     'scrapy.extensions.telnet.TelnetConsole': None,
# }
