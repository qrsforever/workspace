#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scrapy.selector import Selector

sel = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')

# tips: Using text nodes in a condition
# 结果是两个元素 ['Click here to go to the ', 'Next Page']
print(sel.xpath('//a//text()').extract())

# ['Click here to go to the ']
print(sel.xpath("string(//a[1]//text())").extract())

print("-------------- ")

print(sel.xpath("//a[1]").extract())
# ['Click here to go to the Next Page']
print(sel.xpath("string(//a[1])").extract())

print("-------------- ")

# Nothing
print(sel.xpath("//a[contains(.//text(), 'Next Page')]").extract())
# Ok
print(sel.xpath("//a[contains(., 'Next Page')]").extract())

print("-------------- ")

# tips: Beware of the difference between //node[1] and (//node)[1]
sel = Selector(text="""
    <ul class="list">
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    <ul class="list">
        <li>4</li>
        <li>5</li>
        <li>6</li>
    </ul>
    """)

xp = lambda x: sel.xpath(x).extract()
# ['<li>1</li>', '<li>4</li>']
print(xp("//li[1]"))
# ['<li>1</li>']
print(xp("(//li)[1]"))

# tips:  When querying by class, consider using CSS
sel = Selector(text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>')
print(sel.css('.shout').xpath('./time/@datetime').extract())
