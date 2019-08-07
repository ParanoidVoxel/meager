import meager
users = {
        "test": {"password": "thisisatest123"}
        }
app = meager.Server(host="127.0.0.1", port=8080)

@app.router.route("/")
def index(request):
    with open("./res/login.html") as f:
        return f.read()

@app.router.route("/login")
def login(request):
    print(request)
    return "OK"
app.serve()
