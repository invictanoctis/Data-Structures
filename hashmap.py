class HashMap:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # Average: O(1) - constant time
    # Worst: O(n) - linear time 
    def __contains__(self, key) -> bool: # Returns whether the specified key was found or not
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, _ in bucket:
            if k == key:
                return True

    # O(1) - constant time
    def __len__(self) -> int: # Returns the amount of key-value pairs stored
        return self.size

    # Average: O(1) - constant time
    # Worst: O(n) - linear time 
    def put(self, key: any, value: any) -> None: # Adds the specified key-value pair to the hashmap
        index = self._hash_function(key)
        bucket = self.buckets[index]
    
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    # Average: O(1) - constant time
    # Worst: O(n) - linear time 
    def get(self, key: any) -> any: # Returns the value of the specified key
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError('Key not found')

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    def remove(self, key: any) -> None: # Removes the specified key and its value
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError('Key not found')

    # O(n) - linear time
    def keys(self): # Returns a list containing all keys
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear time
    def values(self): # Returns a list containing all values
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear time
    def items(self): # Returns a list containing all key-value pairs
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length
    def _hash_function(self, key: any): # The hash function used to add a hash to a specified key to serve as an index
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        
        return hash_result


if __name__ == '__main__':
    pass # type: ignore