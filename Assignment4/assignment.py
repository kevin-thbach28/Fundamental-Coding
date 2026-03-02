def is_course_code(s: str) -> bool:
    if len(s) != 6:
        return False
    letters = s[:3]
    digits = s[3:]
    return letters.isalpha() and letters.isupper() and digits.isdigit()


def is_hex_color(s: str) -> bool:
    if len(s) != 7 or s[0] != "#":
        return False
    allowed = set("0123456789abcdefABCDEF")
    return all(ch in allowed for ch in s[1:])


def sum_numbers(text: str) -> int:
    total = 0
    current = ""

    for ch in text:
        if ch.isdigit():
            current += ch
        else:
            if current:
                total += int(current)
                current = ""

    if current: 
        total += int(current)

    return total


def redact_phones(text: str) -> str:
    n = len(text)
    i = 0
    out = []

    def is_digit_at(idx: int) -> bool:
        return 0 <= idx < n and text[idx].isdigit()

    while i < n:
        if text[i] == "+" and text[i:i+3] == "+84":
            after = i + 3
            # must have 9 digits after +84
            if after + 9 <= n and all(text[j].isdigit() for j in range(after, after + 9)):
                prev_ok = not is_digit_at(i - 1)
                next_ok = not is_digit_at(after + 9)
                if prev_ok and next_ok:
                    out.append("[REDACTED]")
                    i = after + 9
                    continue

        if text[i].isdigit():
            start = i
            while i < n and text[i].isdigit():
                i += 1
            run = text[start:i]
            prev_ok = not is_digit_at(start - 1)
            next_ok = not is_digit_at(i)
            if prev_ok and next_ok and len(run) == 10:
                out.append("[REDACTED]")
            else:
                out.append(run)
            continue

        out.append(text[i])
        i += 1

    return "".join(out)


if __name__ == "__main__":
    print(is_course_code("TEC001"))   # True
    print(is_course_code("tec001"))   # False

    print(is_hex_color("#A1b2C3"))    # True
    print(is_hex_color("#123ABZ"))    # False

    s = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
    print(sum_numbers(s))             # 2052

    doc = "Call 0912345678 or +84912345678. Not this: 12345678901."
    print(redact_phones(doc))
    # Call [REDACTED] or [REDACTED]. Not this: 12345678901.