---

title: 爬取股票信息

date: 2019-04-11 15:03:18
tags: [test]
categories: [python]

---

[Scrapy文档](https://doc.scrapy.org/en/latest/intro/overview.html)

[Selector](https://docs.scrapy.org/en/latest/topics/selectors.html)

# 创建工程

`scrapy startproject crawlstocks crawl_stocks --logfile=crawl_stocks/crawl.log --loglevel=DEBUG --pidfile=crawl_stocks/crawl.pid`


# 从股城网获取信息

- `scrapy genspider GuchengStockList hq.gucheng.com`
- `scrapy genspider --template=crawl GuchengStockInfo hq.gucheng.com`

# 执行

`scrapy crawl GuchengStockList`

# Shell调试Selector

```html
<section class="stockTable">
    <h3>上海深圳股票代码一览表</h3>
    <a href="https://hq.gucheng.com/SZ000001/">平安银行(000001)</a>
    <a href="https://hq.gucheng.com/SZ000002/">万 科A(000002)</a>
    <a href="https://hq.gucheng.com/SZ000004/">国农科技(000004)</a>
    <a href="https://hq.gucheng.com/SZ000005/">世纪星源(000005)</a>
</section>
```

```
# scrapy shell
In[1]: fetch('https://hq.gucheng.com/gpdmylb.html')
In[2]: response.xpath('//section[has-class("stockTable")]/a/text()').get()
```

# 参考

[爬虫入门](https://www.cnblogs.com/derek1184405959/p/8451798.html)

# 股票常识

## 术语

- 市盈率(Price to Earning Ratio, PE | PER)

每股市价与每股盈利的比率
用来作为比较不同价格的股票是否被高估或者低估的指标

- 市净率(Price to Book Ratio), PB | PBR)

每股股价与每股净资产的比率

- 市销率(Price-to-Sales, PS)

每股股价除以每股销售额
该项指标既有助于考察公司收益基础的稳定性和可靠性,又能有效把握其收益的质量水平

- 净资产(Net Asset)

企业所有,并可以自由支配的资产,即所有者权益或者权益资本

- 净利润(Net Profit)

企业的税后利润
净利润多,企业的经营效益就好;净利润少,企业的经营效益就差,它是衡量一个企业经营效益的主要指标

- 毛利率(Gross Profit Margin)

毛利与销售收入的百分比
毛利是收入和与收入相对应的营业成本之间的差额

- 净资产收益率(Rate of Return on Common Stockholders’ Equity, ROE)

公司税后利润除以净资产得到的百分比率
反映股东权益的收益水平, 一般负债增加会导致净资产收益率的上升

- 每股净资产(Net Assets Per Share)

每股净资产是指股东权益与总股数的比率
反映每股股票所拥有的资产现值
净资产收益率可衡量公司对股东投入资本的利用效率

- 每股收益(Earning Per Share, EPS)

指税后利润与股本总数的比率
每股收益通常被用来反映企业的经营成果

- 每股经营现金净流量

经营现金流量净额/普通股股数 => 现金流入量和流出量的差额/普通股股数
每股现金流过多则表明公司资产利用率低下

- 营业收入(Gross Sales)

从事主营业务或其他业务所取得的收入
