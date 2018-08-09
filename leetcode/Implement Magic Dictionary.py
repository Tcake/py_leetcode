class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for a_str in dict:
            if len(a_str) in self.cache:
                self.cache[len(a_str)].append(a_str)
            else:
                self.cache.update({len(a_str): [a_str]})

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        l_word = len(word)
        if l_word in self.cache:
            for item in self.cache[l_word]:
                flag = 0
                for i in range(l_word):
                    if flag > 1:
                        break
                    if word[i] != item[i]:
                        flag += 1
                if flag == 1:
                    return True
        return False


a = MagicDictionary()
a.buildDict(["hello", "hallo", "leetcode"])
print(a.search('eello'))