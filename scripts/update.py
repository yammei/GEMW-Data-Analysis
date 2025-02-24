import datetime
import requests
import json
import os

class Update:
    def __init__(self):
        self.API_URLS = self.getApiUrls()

    # Retrieves urls from Gaz Lloyd GEBot @ https://chisel.weirdgloop.org/.
    def getApiUrls(self) -> list[str]:
        try:
            info = "relevant GEMW API urls"
            print(f"[-] Attempting to retrieve {info} ...")

            with open('./data/api_urls.json', 'r') as f:
                api_urls = json.load(f)

            print(f"[✔] Successfully retrieved {info}.\n")
            return api_urls
        except Exception as e:
            print(f"[✘] Failed to retrieve {info}.\n")

    # Retrieves updated GEMW data of all trade items from the past day.
    def pastDay(self) -> None:
        try:
            info = "all items' trade data from past day"
            print(f"[-] Attempting to retrieve {info} ...")

            response = requests.get(self.API_URLS["GEMW_all_past_day"])
            res_json = response.json()
            date_today = datetime.date.today()
            save_path = f"./data/GEMW_past_day/GEMW_{date_today}.json"

            with open(save_path, "w") as f:
                json.dump(res_json, f, indent=4)

            print(f"[✔] Successfully updated {info}.\n")
        except Exception as e:
            print(f"[✘] Failed to update {info}: {e}\n")

    # Retrieves updated GEMW data of ONLY ONE trade item from the past 90 days.
    def past90Days(self, item_name: str="", item_id: int=-1) -> any:
        try:
            def _getPast90Days(valid_item_name: str="", valid_item_id: int=-1) -> None:
                item_identifier_val = valid_item_name if valid_item_name != "" else valid_item_id
                item_identifier_key = "name" if type(item_identifier_val) == str else "id"

                date_today = datetime.date.today()
                save_path = f"./data/GEMW_past_90_days/GEMW_{item_name}_{date_today}.json"

                if os.path.exists(save_path):
                    print(f"[✔] Item data already up to date.\n")
                    return
                else:
                    api_url = f"{self.API_URLS["GEMW_all_past_90_days"]}?{item_identifier_key}={item_identifier_val}"
                    print(f"[-] Retrieving data from: {api_url} ...")
                    response = requests.get(api_url)
                    res_json = response.json()

                with open(save_path, "w") as f:
                    json.dump(res_json, f, indent=4)

                print(f"[✔] Successfully updated {info}.\n")

            info = f"[ {item_name} ]'s trade data from past 90 days"
            print(f"[-] Attempting to retrieve {info} ...")

            # Validate item identifier first.
            if item_name == "" and item_id == -1:
                print(f"[✘] No item identifier provided. Please provide valid item_name or item_id.\n")
                return
            else:
                if item_name != "":
                    if self._isValidItem(name_validation=item_name):
                        _getPast90Days(valid_item_name=item_name)
                        return
                if item_id != -1:
                    if self._isValidItem(id_validation=item_id):
                        _getPast90Days(valid_item_id=item_id)
                        return
        except Exception as e:
            print(f"[✘] Failed to update {info}: {e}\n")

    # Validate item identifier.
    def _isValidItem(self, name_validation: str="", id_validation: int=-1) -> bool:
        try:
            identifier = name_validation if name_validation != "" else id_validation
            info = f"item: {identifier}"
            print(f" ├─ [-] Attempting to validate {info} ...")

            save_path = "./data/GEMW_items/all_tradeable_GE_items.json"
            if os.path.exists(save_path):
                with open(save_path, "r") as f:
                    valid_items = json.load(f)
                if type(identifier) == str:
                    is_valid_item_name = True if identifier in valid_items.keys() else False
                    print(f" └─ [✔] Successfully validated item identification. Validity: {is_valid_item_name}.")
                    return is_valid_item_name
                if type(identifier) == int:
                    is_valid_item_id = True if identifier in valid_items.values() else False
                    print(f" └─ [✔] Successfully validated item identification. Validity: {is_valid_item_id}.")
                    return is_valid_item_id
            else:
                response = requests.get(self.API_URLS["GEMW_all_name_to_id"])
                res_json = response.json()

                with open(save_path, "w") as f:
                    json.dump(res_json, f, indent=4)

        except Exception as e:
            print(f" └─ [✘] Failed to update {info}: {e}")