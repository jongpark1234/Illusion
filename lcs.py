class LCS:
    def processWithNormalDP(s1: str, s2: str) -> str:
        from collections import deque
        result = deque()
        l1, l2 = len(s1), len(s2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if s1[i - 1] == s2[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
        i1, i2 = l1, l2
        while True:
            if dp[i1 - 1][i2] != dp[i1][i2] and dp[i1][i2 - 1] != dp[i1][i2]:
                result.appendleft(s2[i2 - 1])
                i1, i2 = i1 - 1, i2 - 1
            else:
                if dp[i1 - 1][i2] == dp[i1][i2]:
                    i1 -= 1
                elif dp[i1][i2 - 1] == dp[i1][i2]:
                    i2 -= 1
            if i1 == 0 or i2 == 0:
                break
        return '' if dp[l1][l2] == 0 else ''.join(map(str, result))
    def processWithHirschBurg(s: str, t: str) -> str:
        def hirschburg(s: str, sLength1: int, sLength2: int, t: str, tLength1: int, tLength2: int) -> str:
            ret, maxValue = '', -float('inf')
            S, T = sLength1 + sLength2 >> 1, 0
            if sLength1 == sLength2:
                return ''
            if sLength1 + 1 == sLength2:
                for i in range(tLength1 + 1, tLength2 + 1):
                    if s[sLength2] == t[i]:
                        return ret + t[i]
                return ''
            for i in range(tLength1, tLength2 + 1):
                LCS1[0][i] = LCS1[1][i] = LCS2[0][i] = LCS2[1][i] = 0
            for i in range(sLength1 + 1, S + 1):
                for j in range(tLength1 + 1, tLength2 + 1):
                    LCS1[i & 1][j] = LCS1[i + 1 & 1][j - 1] + 1 if s[i] == t[j] else max(LCS1[i + 1 & 1][j], LCS1[i & 1][j - 1])
            for i in range(sLength2 - 1, S - 1, -1):
                for j in range(tLength2 - 1, tLength1 - 1, -1):
                    LCS2[i & 1][j] = LCS2[i + 1 & 1][j + 1] + 1 if s[i + 1] == t[j + 1] else max(LCS2[i + 1 & 1][j], LCS2[i & 1][j + 1])
            for i in range(tLength1, tLength2 + 1):
                if LCS1[S & 1][i] + LCS2[S & 1][i] > maxValue:
                    maxValue = LCS1[S & 1][i] + LCS2[S & 1][i]
                    T = i
            return hirschburg(s, sLength1, S, t, tLength1, T) + hirschburg(s, S, sLength2, t, T, tLength2)
        sLength, tLength = len(s), len(t)
        LCS1 = [[0 for _ in range(sLength << 1)] for _ in range(2)]
        LCS2 = [[0 for _ in range(tLength << 1)] for _ in range(2)]
        s = ' ' + s
        t = ' ' + t
        return hirschburg(s, 0, sLength, t, 0, tLength)
