# -*- coding: utf-8 -*-

import scrapy


class SmzdmSipder(scrapy.Spider):

    name = "smzdm"
    allowed_domains = ["www.smzdm.com"]
    start_urls = ["http://www.smzdm.com/jingxuan/"]

    def parse(self, response):
        """解析列表"""
        end_page = 6
        paging_url = "http://www.smzdm.com/jingxuan/p{page}"

        items = self.extract_elements(
            response,
            "//div/ul[contains(@id, 'feed-main-list')]/li[contains(@class, 'feed-row-wide')]"
        )

        if items is not None:
            for item in items:
                unique = item.xpath("@articleid").extract_first()
                url = item.xpath(
                    "h5[contains(@class, 'feed-block-title')]/a/@href").extract_first()
                title = item.xpath(
                    "h5[contains(@class, 'feed-block-title')]/a/text()").extract_first()
                price = item.xpath(
                    "h5[contains(@class, 'feed-block-title')]/a/span/text()").extract_first()

                yield {
                    "unique": unique,
                    "url": url,
                    "title": title,
                    "price": price
                }

        for i in range(2, end_page):
            yield scrapy.Request(paging_url.format(page=i), callback=self.parse)

    def extract_elements(self, response, xpath):
        """提取元素集合"""
        result = None
        eles = response.xpath(xpath)
        if len(eles) > 0:
            result = eles

        return result
