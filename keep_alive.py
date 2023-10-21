from gradio_client import Client
import time

HF_TOKEN = "123456" #os.environ.get("HF_TOKEN")

count = 0

while (count < 3):
    client = Client("https://si1444-mycode2.hf.space", hf_token=HF_TOKEN)
    result = client.predict(
                    "free -h",  # str  in 'command' Textbox component
                    api_name="/predict"
    )
    print(result)
    time.sleep(3)
    result2 = client.predict(
                    "df -h",  # str  in 'command' Textbox component
                    api_name="/predict"
    )
    print(result2)
    time.sleep(6)
    result3 = client.predict(
                    "ps -A",  # str  in 'command' Textbox component
                    api_name="/predict"
    )
    print(result3)
    time.sleep(10)
    result4 = client.predict(
                    "ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10",  # str  in 'command' Textbox component
                    api_name="/predict"
    )
    print(result4)

    time.sleep(600)
