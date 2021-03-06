"""
The Tunnel community package

Defines a ProxyCommunity which discovers other proxies and offers an API to
create and reserve circuits. A basic SOCKS5 server is included which reserves
circuits for its client connections and tunnels UDP packets over them back and
forth
"""

ORIGINATOR = 0
EXIT_NODE = 1

CIRCUIT_TYPE_DATA = 'DATA'
CIRCUIT_TYPE_IP = 'IP'
CIRCUIT_TYPE_RP = 'RP'
CIRCUIT_TYPE_INTRODUCE = 'INTRODUCE'
CIRCUIT_TYPE_RENDEZVOUS = 'RENDEZVOUS'

CIRCUIT_STATE_READY = 'READY'
CIRCUIT_STATE_EXTENDING = 'EXTENDING'
CIRCUIT_STATE_TO_BE_EXTENDED = 'TO_BE_EXTENDED'
CIRCUIT_STATE_BROKEN = 'BROKEN'

PING_INTERVAL = 15.0

