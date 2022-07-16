# celery

## cmd

```text
celery --help

Usage: celery [OPTIONS] COMMAND [ARGS]...

  Celery command entrypoint.

Options:
  -A, --app APPLICATION
  -b, --broker TEXT
  --result-backend TEXT
  --loader TEXT
  --config TEXT
  --workdir PATH
  -C, --no-color
  -q, --quiet
  --version
  --help                 Show this message and exit.

Commands:
  amqp     AMQP Administration Shell.
  beat     Start the beat periodic task scheduler.
  call     Call a task by name.
  control  Workers remote control.
  events   Event-stream utilities.
  graph    The ``celery graph`` command.
  inspect  Inspect the worker at runtime.
  list     Get info from broker.
  logtool  The ``celery logtool`` command.
  migrate  Migrate tasks from one broker to another.
  multi    Start multiple worker instances.
  purge    Erase all messages from all known task queues.
  report   Shows information useful to include in bug-reports.
  result   Print the return value for a given task id.
  shell    Start shell session with convenient access to celery symbols.
  status   Show list of workers that are online.
  upgrade  Perform upgrade between versions.
  worker   Start worker instance.

Worker Options:
    -l, --loglevel

Pool Options:
    -P, --pool [prefork|eventlet|gevent|solo|processes|threads]
    -c, --concurrency Number of child processes processing the queue. 默认 CPU 核心or线程数目

Embedded Beat Options:
    -s, --schedule-filename, --schedule TEXT
```

## 一般任务

```bash
celery -A server worker -l INFO -c 4
celery -app
```

## 定时任务

```bash
celery -A server beat -l INFO
celery -app server beat -l INFO
celery -A server beat -l INFO -s ./tmp/celery-beat-schedule
```
