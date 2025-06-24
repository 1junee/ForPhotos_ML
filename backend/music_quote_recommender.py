"""Music and quote recommendation module."""

import json
from typing import Dict

EMOTION_TABLE = {
    "happy": {
        "song": "Happy",
        "artist": "Pharrell Williams",
        "quote": "Happiness is the best makeup."
    },
    "sad": {
        "song": "Someone Like You",
        "artist": "Adele",
        "quote": "Tears come from the heart and not from the brain."
    },
    "nostalgic": {
        "song": "Photograph",
        "artist": "Ed Sheeran",
        "quote": "Sometimes you will never know the value of a moment until it becomes a memory."
    }
}


def recommend(emotion: str) -> Dict[str, str]:
    """Return music and quote for the given emotion."""
    return EMOTION_TABLE.get(emotion, EMOTION_TABLE["happy"])


def to_json(recommendation: Dict[str, str]) -> str:
    """Convert recommendation to JSON string."""
    return json.dumps(recommendation, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print(to_json(recommend("happy")))
