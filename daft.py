import schedule
import time
from requests_html import HTMLSession

session = HTMLSession()

def send_message(chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = f"https://api.telegram.org/bot{}/sendMessage"
        session.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)

def find_daft():
    url = "https://www.daft.ie/sharing/dublin-city?rentalPrice_from=200&rentalPrice_to=650&firstPublishDate_from=now-1d%2Fd&suitableFor=male"
    r = session.get(url)
    search_result = r.html.xpath('//ul[@data-testid="results"]/li/a/@href')

    with open("sented.txt", "r") as date:
        all_send = date.readlines()
        all_send = [x.strip("\n") for x in all_send]

    for result in search_result:
        if result in all_send:
            search_result.remove(result)
        else:
            send_message("-619768044", f"https://www.daft.ie{result}")
            with open("sented.txt", "a") as date:
                date.write(f"{result}\n")


schedule.every(2).minutes.do(find_daft)


while 1:
    try:
        schedule.run_pending()
    except:
        pass

    time.sleep(1)


# https://api.telegram.org/bot{}/getUpdates