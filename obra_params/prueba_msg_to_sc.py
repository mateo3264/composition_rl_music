import pyOSC3

client = pyOSC3.OSCClient()
client.connect(('127.0.0.1',57120))
msg = pyOSC3.OSCMessage()
msg2 = pyOSC3.OSCMessage()

msg.setAddress('/msg10')
msg2.setAddress('/msg11')

msg.append(1)
msg2.append('asdsdsfs22222')
client.send(msg)
client.send(msg2)
