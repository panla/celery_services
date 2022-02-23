#!/bin/bash
# 定时任务 + 开启 n 个 worker
celery -A server beat -l INFO & celery -A server worker -l INFO -c 4
