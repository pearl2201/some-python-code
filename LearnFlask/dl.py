from requests import get  # to make GET request


def download(url, file_name):
    # open in binary mode
    with open('D:\\file.rar', "wb") as file:
        # get request
        response = get('http://ser3.filedwon.info/files/8/n8mwahkhio376e/P@tch%201%20click%20IDM_New.rar')
        # write to file
        file.write(response.content)

download('hhaha','hahah')