# NFL Stats - FastAPI Project

This project is a simple FastAPI application for extracting NFL game statistics, called NFL Stats. With this application, you can obtain detailed game data in a structured format for further analysis and processing.

## Features

- Fetch game boxscore by providing specific Game ID.
- Data transformation into a more structured format for easy analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need Python 3.10, FastAPI and the necessary packages installed.

### Running the Application

To start the application, use the command:
```bash
uvicorn main:app --reload
```

The application is now running on http://localhost:8000.

### API Endpoints

- **/ (GET):** Test endpoint, returns a Hello World message.
- **/boxscore/{game_id} (GET):** Fetches and returns the boxscore data for a specific game. Replace `{game_id}` with the ID of the game you want to get data for.

## Code Structure

- `main.py` - This is the main FastAPI application file where the routes/endpoints are defined.


## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

