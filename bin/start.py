# -*- coding: utf-8 -*-

import click
import commands
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

COMMAND_PATTERN = "cd {BASE_DIR}; scrapy crawl {spider_name}"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@click.command()
@click.option("--spider_name", default=None, help="爬虫名称")
def main(spider_name):
    """ 启动爬虫脚本 """
    if spider_name is None:
        pass

    (status, output) = commands.getstatusoutput(COMMAND_PATTERN.format(
        BASE_DIR=BASE_DIR, spider_name=spider_name))

    click.echo(output)


if __name__ == "__main__":
    main()
