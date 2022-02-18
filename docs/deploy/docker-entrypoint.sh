#!/bin/bash
# 开启 n 个 worker
celery -A server worker -l INFO -c 4
