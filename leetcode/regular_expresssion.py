def match(s: str, p: str):
    if not p:
        return not s

    is_match = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == "*":
        return match(s, p[2:]) or (is_match and match(s[1:], p))
    else:
        return is_match and match(s[1:], p[1:])


if __name__ == "__main__":
    a = "aab"
    p = "c*a*b"

    result = match(a, p)
    print(result)
