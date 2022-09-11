'''
Liter configuration file
'''

# Station info radio section
callsign = 'SQ5TK'
station_type = 'S' # S - subscribe simple client station , E - exchange coordinating station or part of the network, Internet connection needed


# Modem 
modem_address = '127.0.0.1'
modem_port = '8300'
modem_type = 'AX25' # or 'VARA'

# DataStore path
store_path='sqlite://data/storage.sqlite'

# workflow section
# main loop sleep interval
sleep_time = 1

# networking 
listen_address = '127.0.0.1'
listen_port = '1521'

