from cheaper import Handler
from datetime import datetime

if __name__ == "__main__":
  event = {"game_list": ("Overcooked! 2","Super Smash Bros.™ Ultimate","Animal Crossing™: New Horizons", "Fitness Boxing 2: Rhythm & Exercise","1-2-Switch", "Mario Kart™ 8 Deluxe", "Splatoon™ 2", "New Super Mario Bros.™ U Deluxe", "Super Mario Maker™ 2")}
  #event = {"game_list": ("Overcooked! 2", "Super Smash Bros.™ Ultimate","Animal Crossing™: New Horizons", "Fitness Boxing 2: Rhythm & Exercise","1-2-Switch", "Mario Kart™ 8 Deluxe", "Splatoon™ 2")}
  Handler(event, None)
  print(f"Done checking discount at: {datetime.now()}")

