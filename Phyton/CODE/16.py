def parse_retcode(code: int) -> str:
    if code == 200:
        return "OK"
    elif code == 301:
        return "Moved Permanently"
    elif code == 400:
        return "Bad Request"
    else:
        return "other reason"

while True:
    code = int(input("Enter status code: "))
    if code == -1:
        break
    print(parse_retcode(code))