from collections import OrderedDict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        # Left = least recently used
        # Right = most recently used
        self.freq = {}

    def _increaseFreq(self, key):
        value, oldFreq = self.cache[key]

        # Remove from old frequency group
        del self.freq[oldFreq][key]

        # If this was the minimum frequency and became empty
        if oldFreq == self.minFreq and not self.freq[oldFreq]:
            self.minFreq += 1

        newFreq = oldFreq + 1
        self.cache[key] = [value, newFreq]

        # Add to new frequency group
        if newFreq not in self.freq:
            self.freq[newFreq] = OrderedDict()

        self.freq[newFreq][key] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.cache:
            return -1

        value = self.cache[key][0]

        self._increaseFreq(key)

        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            self.cache[key][0] = value
            self._increaseFreq(key)
            return

        # Cache is full -> remove LFU + LRU
        if self.size == self.capacity:
            keys = self.freq[self.minFreq]

            # First key = least recently used
            lruKey, _ = keys.popitem(last=False)

            del self.cache[lruKey]
            self.size -= 1

        # Insert new key with frequency 1
        self.cache[key] = [value, 1]

        if 1 not in self.freq:
            self.freq[1] = OrderedDict()

        self.freq[1][key] = None

        self.minFreq = 1
        self.size += 1