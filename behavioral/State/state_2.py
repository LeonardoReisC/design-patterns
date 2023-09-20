from __future__ import annotations
from abc import ABC, abstractmethod


class Speaker:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        print(f'Switching to {mode.__class__.__name__}...')
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return str(self.playing)


class PlayMode(ABC):
    def __init__(self, speaker: Speaker) -> None:
        self.speaker = speaker

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.speaker.playing += 1000

    def press_prev(self) -> None:
        self.speaker.playing -= 1000 if self.speaker.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.speaker.playing += 1

    def press_prev(self) -> None:
        self.speaker.playing -= 1 if self.speaker.playing > 0 else 0


if __name__ == '__main__':
    speaker = Speaker()
    speaker.press_next()
    speaker.press_next()
    speaker.press_next()
    speaker.press_next()
    speaker.press_prev()
    speaker.press_prev()

    print('')

    music_mode = MusicMode(speaker)
    speaker.change_mode(music_mode)
    speaker.press_prev()
    speaker.press_prev()
    speaker.press_next()
    speaker.press_next()
    speaker.press_next()
    speaker.press_prev()
