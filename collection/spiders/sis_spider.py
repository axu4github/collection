# -*- coding: utf-8 -*-

import scrapy


class SisSipder(scrapy.Spider):
    name = "sis"
    allowed_domains = ["162.252.9.10"]

    start_urls = [
        "http://162.252.9.10/forum/forum-143-1.html",   # 亚无原
        "http://162.252.9.10/forum/forum-25-1.html",    # 亚无转
        "http://162.252.9.10/forum/forum-58-1.html",    # 亚有转
        "http://162.252.9.10/forum/forum-230-1.html",   # 亚有原
        "http://162.252.9.10/forum/forum-229-1.html",   # 欧无原
        "http://162.252.9.10/forum/forum-77-1.html",    # 欧无转
        "http://162.252.9.10/forum/forum-231-1.html",   # 动漫原
        "http://162.252.9.10/forum/forum-27-1.html"     # 动漫转
    ]

    url = "http://162.252.9.10/forum/{link}"

    def parse(self, response):
        """解析列表"""
        items = self.extract_elements(
            response,
            "//table/tbody[contains(@id, 'normalthread_')]/tr"
        )

        if items is not None:
            for item in items:
                link_ele = item.xpath(
                    "th/span[contains(@id, 'thread_')]/a/@href")

                if len(link_ele) > 0:
                    link = link_ele.extract_first()
                    yield scrapy.Request(
                        self.url.format(link=link), callback=self.parse_detail)

            next_page = self.extract_element(
                response,
                "//div[@class='pages']/a[@class='next']/@href"
            )

            if next_page is not None:
                next_page_url = self.url.format(link=next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        """解析详情"""
        link = response.url
        title = self.extract_element(
            response,
            "//div[@class='postmessage defaultpost']/h2/text()"
        )

        downloads = self.extract_element(
            response,
            "//dl[@class='t_attachlist']/dd/p/text()"
        )

        if downloads is not None:
            try:
                downloads = downloads.split(": ")[1].split()[0]
            except Exception:
                downloads = 0

            yield {
                "title": title,
                "link": link,
                "downloads": downloads
            }

    def extract_elements(self, response, xpath):
        """提取元素集合"""
        result = None
        eles = response.xpath(xpath)
        if len(eles) > 0:
            result = eles

        return result

    def extract_element(self, response, xpath):
        """提取第一个元素"""
        result = None
        eles = self.extract_elements(response, xpath)
        if eles is not None:
            result = eles.extract_first()

        return result
