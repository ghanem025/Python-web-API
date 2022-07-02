import webbrowser

new=2

tabUrl = "https://www.google.com/search?q="
term = input("Enter search query")

webbrowser.open(tabUrl+term, new=0, autoraise=True)