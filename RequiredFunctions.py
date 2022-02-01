import requests


class RequiredFunctions():

    def _checkInternet(self):
        url = "https://www.google.com"
        timeout = 3
        try:
            requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False