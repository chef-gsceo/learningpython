message = " python "
message = message.rstrip() # убирает пробелы справа
print(message)

message = " python "
message = message.lstrip() # убирает пробелы слева
print(message)

message = " python "
message = message.strip() # убирает пробелы справа и слева
print(message)

nostrach_url = "https://nostrach.com"
nostrach_url = nostrach_url.removeprefix('https://')
print(nostrach_url)