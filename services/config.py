from kombu import Queue, Exchange

from config import MQConfig, RedisConfig


class CeleryConfig:
    broker_url = f'amqp://{MQConfig.USER}:{MQConfig.PASSWD}@{MQConfig.HOST}:{MQConfig.PORT}'
    result_backend  = f'redis://{RedisConfig.USER}:{RedisConfig.PASSWD}@{RedisConfig.HOST}:{RedisConfig.PORT}'

    # default config
    DefaultExchangeType = 'direct'

    class ExchangeConst:
        # exchange name

        default = 'celery-default'
        test = 'celery-test'
        pay = 'celery-test'

    class RoutingKeyConst:
        # queue routing key

        default = 'default-tasks'
        test = 'test-tasks'
        pay = 'pay-tasks'

    class QueueNameConst:
        # queue name

        default = 'celery-default-tasks'
        test = 'celery-test-tasks'
        pay = 'celery-pay-tasks'

    # exchange
    define_exchange = {
        'default': Exchange(ExchangeConst.default, type=DefaultExchangeType),
        'test': Exchange(ExchangeConst.test, type=DefaultExchangeType),
        'pay': Exchange(ExchangeConst.pay, type=DefaultExchangeType)
    }

    # tasks queues
    task_queues = (
        Queue(QueueNameConst.default, routing_key=RoutingKeyConst.default, exchange=define_exchange.get('default')),
        Queue(QueueNameConst.test, routing_key=RoutingKeyConst.test, exchange=define_exchange.get('test')),
        Queue(QueueNameConst.pay, routing_key=RoutingKeyConst.pay, exchange=define_exchange.get('pay')),
    )

    task_routes = {
        'pay_task': {'exchange': define_exchange.get('pay').name, 'routing_key': RoutingKeyConst.test}
    }

    enable_utc = False
    accept_content = ['json']
