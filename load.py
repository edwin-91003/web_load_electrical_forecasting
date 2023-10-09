from pydantic import BaseModel
class Load(BaseModel):
    T1: float
    T2: float
    T3: float
    T4: float
    T24: float
    T48: float
    T72: float
    T96: float
    DAY: float
    SEASON: float
    TEMP: float
    HUMIDITY: float
    