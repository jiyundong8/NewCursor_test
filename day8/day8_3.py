# pythonping：批量探测网关可达性

import pythonping

def ping_check(host):
    try:
        from pythonping import ping

        result = ping(host, count=1, timeout=2)

        if result.success():
            return True, result.rtt_avg_ms
        else:
            return False, None

    except OSError:
        return False, None

    except Exception:
        return False, None
    

if __name__ == '__main__':
    gateways = ['10.10.1.100', '192.168.0.18', '172.16.1.1']

    for gw in gateways:
        status, rtt = ping_check(gw)

        if status:
            print("{:<15}: 可达   | RTT: {:.2f} ms".format(gw, rtt))
        else:
            print("{:<15}: 不可达".format(gw))