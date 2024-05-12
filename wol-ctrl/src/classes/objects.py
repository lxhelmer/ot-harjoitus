from dataclasses import dataclass

@dataclass
class Device:
    """Class for representing single device"""
    id: int
    name: str
    user_id: int
    mac: str
    ip: str
    
    def __repr__(self):
        return "id="+str(self.id)+","+"name="+self.name+"," + \
                "mac="+self.mac+","+"ip="+self.ip

@dataclass
class User:
    id: int
    username: str
    hash: str

