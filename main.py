from bin.web import Web

if __name__ == "__main__":
    url = input("Paste web url here: ")
    wix = Web(url)
    wix.to_code().convert_to_local()
