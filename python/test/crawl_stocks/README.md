---

title: 爬取股票信息

date: 2019-04-11 15:03:18 tags: [test] categories: [python]

---

# 准备

1. `sudo pip3 install fake-useragent`
2. `sudo pip3 install scrapy-splash`
3. `sudo docker run -p 8050:8050 scrapinghub/splash`

# 创建工程

`scrapy startproject crawlstocks crawl_stocks --logfile=crawl_stocks/crawl.log
--loglevel=DEBUG --pidfile=crawl_stocks/crawl.pid`


# 从股城网获取信息

- `scrapy genspider GuchengStockList hq.gucheng.com`
- `scrapy genspider --template=crawl GuchengStockInfo hq.gucheng.com`

# 执行

- `scrapy crawl GuchengStockList`
- `scrapy crawl GuchengStockInfo`
- `scrapy crawl EastmoneyStockUrls`

- `scrapy crawl EastmoneyStockCwzb -a filename=stock_urls.txt`

# 数据网站

## 股城网(hq.gucheng.com)


## 东方财富网(quote.eastmoney.com)

2019.04之后`https://quote.eastmoney.com/stocklist.html`已经不能方便获取所有股票信息了,
可以结合股城网一起爬取数据.

(封号严重)

1. 股城网爬取所有股票的代码, 保存到文件中
2. 东方财富网根据具体的股票代码获取更多的信息, 把1中的文件通过-a NAME=VALUE传给spider

# Shell调试Selector

```html <section class="stockTable"> <h3>上海深圳股票代码一览表</h3> <a
href="https://hq.gucheng.com/SZ000001/">平安银行(000001)</a> <a
href="https://hq.gucheng.com/SZ000002/">万 科A(000002)</a> <a
href="https://hq.gucheng.com/SZ000004/">国农科技(000004)</a> <a
href="https://hq.gucheng.com/SZ000005/">世纪星源(000005)</a> </section> ```

``` # scrapy shell In[1]: fetch('https://hq.gucheng.com/gpdmylb.html') In[2]:
response.xpath('//section[has-class("stockTable")]/a/text()').get() ```

# 参考

1. [爬虫入门](https://www.cnblogs.com/derek1184405959/p/8451798.html)
2. [Scrapy文档](https://doc.scrapy.org/en/latest/intro/overview.html)
3. [Selector](https://docs.scrapy.org/en/latest/topics/selectors.html)
4. [随机代理](https://www.cnblogs.com/trunkslisa/p/9841658.html)

# 问题

## 动态页面

[how to scrape the dynamic website using scrapy][1]
[Scraping dynamic content using python-Scrapy][2]
[Splash][3]
[Scrapy+Splash实例][4]

[1]: https://medium.com/@vigneshgig/how-to-scrape-the-dynamic-website-using-sitemap-731f5e4651a9
[2]: https://stackoverflow.com/questions/30345623/scraping-dynamic-content-using-python-scrapy
[3]: https://splash.readthedocs.io/en/stable
[4]: https://github.com/scrapy-plugins/scrapy-splash


# 股票常识

## 术语

### 市盈率(Price to Earning Ratio, PE | PER)

每股市价与每股盈利的比率  用来作为比较不同价格的股票是否被高估或者低估的指标

### 市净率(Price to Book Ratio), PB | PBR)

每股股价与每股净资产的比率

### 市销率(Price-to-Sales, PS)

每股股价除以每股销售额
该项指标既有助于考察公司收益基础的稳定性和可靠性,又能有效把握其收益的质量水平

### 净资产(Net Asset)

企业所有,并可以自由支配的资产,即所有者权益或者权益资本

### 净利润(Net Profit)

企业的税后利润
净利润多,企业的经营效益就好;净利润少,企业的经营效益就差,它是衡量一个企业经营效益的主要指标

### 毛利率(Gross Profit Margin)

毛利与销售收入的百分比  毛利是收入和与收入相对应的营业成本之间的差额

### 净资产收益率(Rate of Return on Common Stockholders’ Equity, ROE)

公司税后利润除以净资产得到的百分比率  反映股东权益的收益水平,
一般负债增加会导致净资产收益率的上升

1、加权平均净资产收益率＝报告期净利润÷平均净资产，强调经营期间净资产赚取利润的结果,是
一个动态的指标,反应的是企业业的净资产创造利润的能力。 

2、摊薄净资产收益率，摊薄净资产收益率＝报告期净利润÷期末净资产，强调年末状况，是一个静
态指标，说明期末单位净资产对经营净利润的分享,多用来确定股票的价格。

### 每股净资产(Net Assets Per Share)

每股净资产是指股东权益与总股数的比率  反映每股股票所拥有的资产现值
净资产收益率可衡量公司对股东投入资本的利用效率

### 每股收益(Earning Per Share, EPS)

指税后利润与股本总数的比率 每股收益通常被用来反映企业的经营成果

### 扣非每股收益

扣除不是经常主营业务的每股收益，比方说制造业的公司 前年买了一块地皮 几年想用钱或者没用
了就把它高价卖了 所撰的收益就不是经常的收益

### 稀释每股收益(Diluted earnings per share)

从字面理解：在基本每股收益的基础上，潜在普通股（如公司发行的可转债）转换为普通股后，使
普通股总数增加，重新计算每股收益，导致每股收益被稀释

### 每股经营现金净流量

经营现金流量净额/普通股股数 => 现金流入量和流出量的差额/普通股股数
每股现金流过多则表明公司资产利用率低下

### 营业收入(Gross Sales)

从事主营业务或其他业务所取得的收入

### 预收账款和应收账款的区别

销售的时候先收钱后付货的是预收账款，先付货后收钱的是应收账款。应收账款主要用于赊销

1、应收账款是资产类科目。
应收账款指企业因销售商品、提供劳务等业务，应向购货或接受劳务单位收取的款项，是企业因销
售商品、提供劳务等经营活动所形成的债权。

2、预收账款是负债类科目。
预收账款指企业按照合同规定，向购货单位预先收取的款项。企业在发货前预收的货款，应作为企
业的一项负债。

### 总资产周转率(Total Assets Turnover)

总资产周转率是企业一定时期的销售收入净额与平均资产总额之比,它是衡量资产投资规模与销售
水平之间配比情况的指标。

### 资产负债率(Liability on asset ratio)

资产负债率又称举债经营比率,它是用以衡量企业利用债权人提供资金进行经营活动的能力,以及反
映债权人发放贷款的安全程度的指标,通过将企业的负债总额与资产总额相比较得出,反映在企业全
部资产中属于负债比率。

如果资产负债比率达到100%或超过100%说明公司已经没有净资产或资不抵债。
