from fastapi import FastAPI
from src.sportsradar.extract.gamefeeds import GameFeeds
from src.sportsradar.transform.gamefeeds import GameFeedsTransformer
from config import TestConstants

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sportradar/boxscore/extract/{game_id}")
async def extract_boxscore(game_id: str):
    fetcher = GameFeeds(TestConstants.BASE_URL)
    bronze_data = fetcher.get_game_boxscore(
        game_id=game_id,
        access_level=TestConstants.ACCESS_LEVEL,
        api_key=TestConstants.API_KEY,
        file_format=TestConstants.FORMAT,
        version=TestConstants.VERSION,
        language_code=TestConstants.LANGUAGE_CODE,
    ).json()
    transformer = GameFeedsTransformer(bronze_data)
    gold_data = transformer.transform_boxscore()
    return gold_data


@app.get("/sportradar/boxscore/transform/{game_id}")
async def transform_boxscore(game_id: str):
    bronze_data = GameFeeds(TestConstants.BASE_URL).get_game_boxscore(
        game_id=game_id,
        access_level=TestConstants.ACCESS_LEVEL,
        api_key=TestConstants.API_KEY,
        file_format=TestConstants.FORMAT,
        version=TestConstants.VERSION,
        language_code=TestConstants.LANGUAGE_CODE,
    ).json()
    transformer = GameFeedsTransformer(bronze_data)
    gold_data = transformer.transform_boxscore()
    return gold_data
