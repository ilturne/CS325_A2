from dataclasses import dataclass, asdict

@dataclass
class wii_sports:
    save_number: int
    games = 5
    training = 15
    campaign: float

new_save = wii_sports(save_number = 1, campaign = 15.0)

print(asdict(new_save))