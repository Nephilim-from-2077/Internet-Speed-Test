import speedtest


speed = speedtest.Speedtest()
print("Getting Download Speed...")
download_speed=speed.download()
print("Getting Upload Speed...")
upload_speed=speed.upload()
print("Gotchaaa!!!!")

download_speed_mb = download_speed/1048576
upload_speed_mb = upload_speed/1048576
download_speed_msg=(f" {download_speed_mb} mbps")
upload_speed_msg=(f" {upload_speed_mb} mbps")

print("Download Speed: ", download_speed_msg)
print("Upload Speed: ", upload_speed_msg)