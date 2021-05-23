# Cowrywise Assesment

## Assigenment Description

Build a simple API that will return a key-value pair of randomly generated UUID. Key will be a timestamp and value will be UUID. While the server is running, whenever the API is called, it should return all the previous UUIDs ever generated by the API alongside a new UUID. Push the code to a git repository and share the link to the repo.

Sample:

```
{

"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"

"2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",

"2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",

}
```

## Implementation
<br>

I approached the assigment considering two appraoches: 

- using a python list to imitate a cache memory

- using memcache for caching


## How to run:
<br>

- run docker compose command
```
docker-compose up --build -d
```

- visit localhost:8000/ to test api via swagger UI


## Endpoint Description

- api/naive/   - uses python list as cache memory
- api/cached/  - uses Memcache for Caching 