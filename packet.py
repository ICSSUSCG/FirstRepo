from scapy.all import scapy, sniff, Ether

print("importing cool stuff")

val = input("How many packets?")

print(f"You selected ~{val}")

packets = sniff (filter="not ip6", count=int(val))

for i in packets:
	print(i.summary())
