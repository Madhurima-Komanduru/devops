from collections import deque

def water_jug(x, y, t):
    q, v = deque([(0, 0)]), set()
    while q:
        a, b = q.popleft()
        if (a, b) in v: continue
        print(f"Jug1: {a}L, Jug2: {b}L")
        if t in (a, b): return f"Target {t}L reached!"
        v.add((a, b))
        q.extend([(x, b), (a, y), (0, b), (a, 0), 
                  (a - min(a, y - b), b + min(a, y - b)), 
                  (a + min(b, x - a), b - min(b, x - a))])
    return "Not possible."

print(water_jug(4, 3, 2))
