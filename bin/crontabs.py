# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

COMMAND_PATTERN = "cd {BASE_DIR}; python bin/start.py --spider_name=smzdm"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    os.system(COMMAND_PATTERN.format(BASE_DIR=BASE_DIR))


scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=5)
scheduler.start()
