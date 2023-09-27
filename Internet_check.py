import speedtest
import json
import time


def test_speed():
    st = speedtest.Speedtest()

    print("Connecting to best server based on ping...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000
    print(f"Download Speed: {download_speed:.2f} Mbps")
    ds = format(download_speed, ".2f")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    us = format(upload_speed, ".2f")

    ping = st.results.ping
    time = st.results.timestamp

    return {
        "download": ds,
        "upload": us,
        "ping": ping,
        "time": time
    }


def save_information(info):
    with open("text.json", "r") as file:
        data = json.load(file)
        data.append(info)

    with open("text.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    for n in range(3):
        results = test_speed()
        save_information(results)
        time.sleep(10)
