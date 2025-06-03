import redis

# Shared Redis client for all agents
try:
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    r.ping()
    print("[REDIS] Connection successful.")
except redis.ConnectionError:
    print("[REDIS] ❌ Failed to connect to Redis. Make sure the server is running.")


def set_flag(key, value):
    r.set(key, value)


def get_flag(key):
    return r.get(key)


def delete_flag(key):
    r.delete(key)


def increment(key):
    r.incr(key)


def reset_counter(key):
    r.set(key, 0)


def fetch_all():
    return {k: r.get(k) for k in r.keys()}
