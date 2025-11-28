def is_cyclic_shift(s, t):
    if len(s) != len(t):
        return -1
    
    if s == t:
        return 0
    
    double_s = s + s
    
    def build_prefix(pattern):
        n = len(pattern)
        prefix = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            prefix[i] = j
        return prefix
    
    def kmp_search(text, pattern):
        if not pattern:
            return []
        
        prefix = build_prefix(pattern)
        result = []
        j = 0
        
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = prefix[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                result.append(i - len(pattern) + 1)
                j = prefix[j - 1]
        
        return result

    positions = kmp_search(double_s, t)
    
    if not positions:
        return -1
    
    min_shift = len(s)
    for pos in positions:
        if pos < len(s):
            shift = (len(s) - pos) % len(s)
            min_shift = min(min_shift, shift)
    
    return min_shift

S = input().strip()
T = input().strip()


result = is_cyclic_shift(S, T)
print(result)