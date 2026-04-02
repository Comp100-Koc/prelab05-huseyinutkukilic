def longest_palindromic_substring(s):
    best_palindrom = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            current = s[i:j]
            if current == current[::-1] and len(current) > 2:
                if len(current) > len(best_palindrom):
                    best_palindrom = current
    return best_palindrom                
            
    """
    Given a string find the longest palindromic substring
    """
    