# -*- coding: utf-8 -*-

import click
# import commands
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

COMMAND_PATTERN = "cd {BASE_DIR}; scrapy crawl {spider_name} -o {output}"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DEFAULT_OUTPUT = "{BASE_DIR}/output.csv".format(BASE_DIR=BASE_DIR)


@click.command()
@click.option("--spider_name", default=None, help="爬虫名称")
@click.option("--output", default=DEFAULT_OUTPUT, help="爬虫名称")
def main(spider_name, output):
    """ 启动爬虫脚本 """
    if spider_name is None:
        pass

    command = COMMAND_PATTERN.format(
        BASE_DIR=BASE_DIR, spider_name=spider_name, output=output)
    # (status, output) = commands.getstatusoutput(command)

    # click.echo(output)
    os.system(command)


if __name__ == "__main__":
    main()
