import schedule
import time
from requests_html import HTMLSession

session = HTMLSession()
key_api = ""


def send_message(chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = f"https://api.telegram.org/{key_api}/sendMessage"
        session.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)

def find_rent():
    url = "https://www.rent.ie/rooms-to-rent/renting_dublin/room-type_either/rent_200-550/"
    r = session.get(url)
    search_result = r.html.xpath('//div[@class="search_result"]//a/@href')

    with open("sented_rent.txt", "r") as date:
        all_send = date.readlines()
        all_send = [x.strip("\n") for x in all_send]

    search_result = search_result[0:10]

    for result in search_result:
        if result in all_send:
            search_result.remove(result)
        else:
            send_message("-619768044", f"{result}")
            with open("sented_rent.txt", "a") as date:
                date.write(f"{result}\n")




schedule.every(2).minutes.do(find_rent)


while 1:
    try:
        schedule.run_pending()
    except:
        pass

    time.sleep(1)


# https://api.telegram.org/{key_api}/getUpdates