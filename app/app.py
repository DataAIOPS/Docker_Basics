from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host="redis", port=6379)

@app.route("/")
def hello():
    # Increment visit count
    visits = redis_client.incr("counter")
    return f"Hello, World! This page has been visited {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
