from bin.web import Web

if __name__ == "__main__":
    wix = Web("https://sanbope.wixsite.com/ccicolombia")
    wix.to_code().convert_to_local()
