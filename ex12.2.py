logging_profile = ("192.168.1.10", 8080)

ip_address, server_port = logging_profile

print("IP Address:", ip_address)
print("Server Port:", server_port)

try:
    logging_profile[0] = "192.168.1.20"
except TypeError:
    print("Settings cannot be modified because the tuple is immutable.")