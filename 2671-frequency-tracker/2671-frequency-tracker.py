class FrequencyTracker:

    def __init__(self):
        self.datastr = {}
        self.count = {}

    def add(self, number: int) -> None:
        old_freq = self.datastr.get(number, 0)
        new_freq = old_freq + 1

        if old_freq > 0:
            self.count[old_freq] -= 1

        self.datastr[number] = new_freq
        self.count[new_freq] = self.count.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.datastr or self.datastr[number] == 0:
            return

        old_freq = self.datastr[number]
        new_freq = old_freq - 1

        self.count[old_freq] -= 1
        self.datastr[number] = new_freq

        if new_freq > 0:
            self.count[new_freq] = self.count.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.count.get(frequency, 0) > 0
