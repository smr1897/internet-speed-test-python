#Install speedtest-cli: pip install speedtest-cli
import speedtest

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers() # gets a List of servers that are avaliable for speedtest
print("Choosing best server...")
best = test.get_best_server() 

print(f"found: {best['host']} Located in {best['country']}")

print("performing download test...")
download_result = test.download()
print("performing upload test...")
upload_result = test.upload()

ping_result = test.results.ping

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")

#That's it! You can now run the script and see your internet speed.