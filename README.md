# FastAPI - Provinces, Districts, and Municipalities API

This is a FastAPI project that provides an API to retrieve information about provinces, districts, and municipalities in Nepal. The project uses Python and the FastAPI framework.

## Installation

To run this project, please follow the steps below:

1. Clone the repository:

```shell
git clone https://github.com/your-username/provinces-api.git
cd provinces-api
```

2. Create and activate a virtual environment (optional but recommended):

```shell
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies from the `requirements.txt` file:

```shell
pip install -r requirements.txt
```

## Serving the API

Once you have installed the required dependencies, you can serve the API using FastAPI.

To start the FastAPI server, run the following command:

```shell
uvicorn main:app --reload
```

This will start the server and automatically reload it whenever code changes are detected.

## Usage

Once the FastAPI server is running, you can access the API endpoints using a web browser or a tool like cURL or Postman.

### Endpoints

The API provides the following endpoints:

- http://127.0.0.1:8000/docs All endpints can found here


## Data Source

The data used in this API is taken from the [Nepal Data](https://github.com/sandipbgt/nepal-data/blob/master/json/provinces_with_districts_and_municipalities.json) repository by [sandipbgt](https://github.com/sandipbgt). Make sure to check the repository for any updates or additional data.

## Contributing

If you'd like to contribute to this project, you can follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository, describing the changes you have made.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

