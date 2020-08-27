class Sol:
    def canConvertString(self, s, t, k):
        cnt = [0] * 26
        for cs, ct in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26
            if diff > 0 and cnt[diff] * 26 + diff > k:
                return False
            cnt[diff] += 1
        return len(s) == len(t)

if __name__ == "__main__":
    s = "mpzzwh"
    t ="kaeblv"
    k = 24
    sol = Sol()
    print(sol.canConvertString(s,t,k))