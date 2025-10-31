import threading

"""Thread-safe Singleton GameManager for managing game state in an RPG."""
class GameManager:
    _instance = None
    _initialized = False
    _lock = threading.Lock()  # class-level lock

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # acquire lock
                if cls._instance is None:  # double-checked locking
                    print("[GameManager] Creating new GameManager instance (Singleton)")
                    cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not GameManager._initialized:
            self.game_name = "Fantasy Quest"
            self.difficulty = "Normal"
            self.max_party_size = 4
            self.current_party = []
            self.game_settings = {
                'sound_enabled': True,
                'music_volume': 70,
                'graphics_quality': 'High'
            }
            GameManager._initialized = True
            print(f"[GameManager] Initialized: {self.game_name}")
    
    def add_to_party(self, character):
        if len(self.current_party) >= self.max_party_size:
            print(f"[GameManager] Party is full! Max size: {self.max_party_size}")
            return False
        self.current_party.append(character)
        print(f"[GameManager] Added {character.name} to the party")
        return True
    
    def get_party_info(self):
        if not self.current_party:
            return "Party is empty"
        
        info = f"\n=== Current Party ({len(self.current_party)}/{self.max_party_size}) ===\n"
        for i, character in enumerate(self.current_party, 1):
            info += f"{i}. {character.name} - {character.__class__.__name__} (Level {character.level})\n"
        return info
    
    def set_difficulty(self, difficulty: str):
        self.difficulty = difficulty
        print(f"[GameManager] Difficulty set to: {difficulty}")
    
    def get_game_info(self):
        return (f"\n{'='*50}\n"
                f"  {self.game_name}\n"
                f"  Difficulty: {self.difficulty}\n"
                f"  Party Size: {len(self.current_party)}/{self.max_party_size}\n"
                f"{'='*50}")
    
    @classmethod
    def reset_instance(cls):
        cls._instance = None
        cls._initialized = False
