import os, musify_client, json

if __name__ == '__main__':
    client = musify_client.MusifyClient('localhost:8888')

    print(">> Executing Upload test...")
    uploadResponse = json.loads(client.upload('../../storage/songs/highquality/1e70c0a2db1413f60519bfdd8223291e6352feca.bin', '2.mp3'))
    assert uploadResponse["status"] == "success"

    print(">> Executing Download test...")
    downloadResponse = client.download(uploadResponse["name"], "highquality")
    assert any(True for _ in downloadResponse)

    print("> All tests passed")
