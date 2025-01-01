class KMP:
    """Implementation of Knuth-Morris-Pratt string matching algorithm"""
    
    @staticmethod
    def compute_lps(pattern):
        """
        Compute Longest Proper Prefix which is also Suffix array
        
        Args:
            pattern: Pattern string
            
        Returns:
            list: LPS array
        """
        length = 0  # Length of previous longest prefix suffix
        lps = [0] * len(pattern)
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        return lps
        
    @staticmethod
    def search(text, pattern):
        """
        Search for pattern in text using KMP algorithm
        
        Args:
            text: Text string to search in
            pattern: Pattern to search for
            
        Returns:
            list: All positions where pattern occurs in text
        """
        if not pattern or not text:
            return []
            
        # Compute LPS array
        lps = KMP.compute_lps(pattern)
        
        positions = []
        i = j = 0  # i for text, j for pattern
        
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
            
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return positions

# Test implementation
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("ABABDABACDABABCABAB", "ABABCABAB"),
        ("AAAAAAAAA", "AAA"),
        ("ABCDEFGHIJK", "DEF"),
        ("Hello, World!", "World")
    ]
    
    for text, pattern in test_cases:
        positions = KMP.search(text, pattern)
        if positions:
            print(f"Pattern '{pattern}' found in '{text}' at positions: {positions}")
        else:
            print(f"Pattern '{pattern}' not found in '{text}'") 