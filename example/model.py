# 5-9 Create creature
from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    description: str
    country: str
    area: str
    aka: str

thing = Creature(name="yeti",
    aka="Abominable Snowman",
    country="CN",
    area="Himalayas",
    description="Hapless Himalayan")

print("Name is", thing.name)
