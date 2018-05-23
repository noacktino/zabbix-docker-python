from pyzabbix import ZabbixMetric, ZabbixSender


def sender():
    zbx = ZabbixSender('127.0.0.1')
    metrics = [ZabbixMetric('my.local.sender', 'trap', 1)]
    print(zbx.send(metrics))


if __name__ == "__main__":
    sender()
