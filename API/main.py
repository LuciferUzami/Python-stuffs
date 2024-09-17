import requests
def quotes(ans):
    if ans == "yes":
        # Get url
        respond = requests.get(url="https://api.kanye.rest")
        # Raise some error will show up
        respond.raise_for_status()
        # Get quote
        quote = respond.json()["quote"]
        return quote

#
print(quotes("yes"))
condition = True
while condition:
    user = input("Do you want Generate more Quotes: ")
    if user.lower() == "yes":
        print(quotes(user.lower()))
    else:
        condition = False
        print("Thank you using Us...")
