
cp www/* /var/www/html/

cmd:
    scrapy shell http://localhost
>>>
    response.selector.xpath('//title/text()')
    response.xpath('//title/text()')
    response.xpath('//title/text()').extract()
    response.css('title::text')


    // @后面是属性
    response.css('img').xpath('@src').extract()
    response.xpath('//img/@src').extract()
    response.xpath('//base/@href').extract()
    response.css('base::attr(href)').extract()

    
    // [ ]判断
    response.xpath('//div[@id="images"]/a/text()').extract_first()
    response.xpath('//div[@id="not-exists"]/text()').extract_first(default='not-found')
    response.xpath('//a[contains(@href, "image")]/@href').extract()
    response.xpath('//a[contains(@href, "image")]/img/@src').extract()

    response.css('a[href*=image]::attr(href)').extract()
    response.css('a[href*=image] img::attr(src)').extract()

    // re
    response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
    response.xpath('//a[contains(@href, "image")]/text()').re_first(r'Name:\s*(.*)')

    // 嵌套 绝对/相对 '/':绝对 '.':相对
    response.xpath('//div').xpath('./a/@href').extract()

    // 避免hardcode
    response.xpath('//div[@id=$val]/a/text()', val='images').extract_first()
    response.xpath('//div[count(a)=$cnt]/@id', cnt=5).extract_first()

    // tips
    see learn.py 
