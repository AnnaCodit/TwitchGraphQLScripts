from dataclasses import dataclass
from datetime import datetime


@dataclass
class FollowerData:
	name: str
	created_at: datetime
	followed_at: datetime
