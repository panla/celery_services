#!/bin/bash
# 定时任务 + 开启 n 个 worker
celery -A server:app worker -l INFO -c 2 & celery -A server:app beat -l INFO
