import redis

INFOBIP_DB = 1
DOTGTO_DB = 2
ROUTE_DB = 3
EXCHANGE_DB = 4


# Create database connection(s) here.
connect_infobip_database = redis.StrictRedis(
    host="localhost", port=6379, db=INFOBIP_DB, decode_responses=True
)


connect_dotgo_database = redis.StrictRedis(
    host="localhost", port=6379, db=DOTGTO_DB, decode_responses=True
)


connect_route_database = redis.StrictRedis(
    host="localhost", port=6379, db=ROUTE_DB, decode_responses=True
)


connect_exchange_database = redis.StrictRedis(
    host="localhost", port=6379, db=EXCHANGE_DB, decode_responses=True
)
