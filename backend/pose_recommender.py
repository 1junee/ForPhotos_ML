"""Pose recommendation module."""

import json
from typing import List, Dict

# Example dataset of poses
POSE_DATA = [
    {
        "name": "Peace Sign",
        "image_url": "https://example.com/peace.jpg",
        "description": "A casual peace sign with one hand.",
        "keywords": ["happy", "casual", "trend"]
    },
    {
        "name": "Heart Hands",
        "image_url": "https://example.com/heart.jpg",
        "description": "Hands together forming a heart.",
        "keywords": ["love", "cute", "trend"]
    },
    {
        "name": "Look Away",
        "image_url": "https://example.com/lookaway.jpg",
        "description": "Gazing off to the side for a candid feel.",
        "keywords": ["nostalgic", "calm"]
    },
    {
        "name": "Finger Gun",
        "image_url": "https://example.com/finger_gun.jpg",
        "description": "Playful finger gun pose.",
        "keywords": ["playful", "happy"]
    }
]

def recommend_poses(emotion: str, time_of_day: str, trend: str) -> List[Dict[str, str]]:
    """Recommend top 3 poses based on emotion, time, and trend."""
    # Simple heuristic: select poses containing the emotion or trend keywords
    candidates = [p for p in POSE_DATA if emotion in p["keywords"] or trend in p["keywords"]]
    if not candidates:
        candidates = POSE_DATA
    return candidates[:3]

def to_json(recommendations: List[Dict[str, str]]) -> str:
    """Convert recommendations to JSON string."""
    return json.dumps(recommendations, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    recs = recommend_poses("happy", "morning", "trend")
    print(to_json(recs))
