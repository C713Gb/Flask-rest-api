# Flask REST Api for Youtube Data

## Installation

Assuming that [Docker](https://www.docker.com/) is already installed in the system


```sh
git clone https://github.com/C713Gb/Flask-rest-api.git
cd Flask-rest-api
docker-compose build
docker-compose up
```

## Testing

After successfully running the application, you can test the following apis

#### Get paginated result in sorted order

`http://127.0.0.1:5000/api?limit=10&offset=0&order=DESCENDING`
This is going to show the first 10 results in descending order of date and time.

#### Search for a query

`http://127.0.0.1:5000/api/search?q="IPL"`
This is going to show the results of the data that has IPL in its title.
