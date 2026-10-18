# -*- coding: utf-8 -*-
# TU CHAM 10 DE LUYEN TAP NHOM B (Phan "Luyen viet chuong trinh" trong tai lieu on)
# Cach dung: luu bai De 1 thanh L1.py, De 2 thanh L2.py, ... De 10 thanh L10.py
#   trong CUNG thu muc voi file nay, roi mo file nay bang IDLE/Thonny va bam F5.
import os, sys, subprocess, time, zlib, base64
GIOI_HAN_GIAY = 2
_D = """
eNqVVm1v4zYM/t5foRkoTk6UVJLf09OHfegBBwS7oesGDGlxcBMn9Rorhe106Yr+95GSndhJh/XS
xqJCkXz4kFSSF0+bsiZlqhebgpEirR/OFtmSTAWt3MkZgdeLynUNu0tSZvW21MT58+o3h+RLQl/O
faU4AWPyci44/0lxl2xK2PicoyZbVxlxfvnmWKdy71TvnRZKX1zIvfOqLmkxoMVQuK418vZGtarG
oM+f6AHM0nldZ5rW7ht5rbYFRbdzlywBxZzkmoCiCe7v/TyrdV7VtEif8DgDp0/rvKauC25TVQEh
2YI+z8REDJ9n/O6ukzpxxn9tcm1sAQpLXXfo3GpnCDgwfIo4UjAyy0jctdGD/8sCrUUHNxJspE9p
lm+2P199/fb7J/cNY9F9BWql6tlkAnEOVDe0hR9Mt5MnFqNId5BEF1iBqYxzvch2tHCHosno+xPd
NQEAyO6znLQ2X1KAYhVKmvXvh3ydkXyQf1Y7a9KanefQJu9YGv1QCbNptDflNrO5RR/KrdNRB3J3
SGknZ0RhUmnbLd77Ttm9OnV8SVYKx2S8mi8oHOlxtUKuBvcXF6u27smPl6Gbc68xDPbU8uYBb23P
70600mgbCIK/M3YLxS+hPuK4PrpXH93UZzFUROAHsIVxzW23yf8sFXK+cM+ur76o13yyNPhytkSE
md4WWZnWGZ1NBZtKNvXY1GfTgE1DNo3YNGbThAHoOybcN5PBCgb8scngWtm7anxtFgq3Dh8+ukaH
Z9OypJqtN+whdycnY4u4rsfoAXmwp+xl8R2xgWKVUe26bVs/KiUm5EbNHMml7zBHJJzDInmzyBAX
YXe+WcwxczQJ7RnPsTXN1taltC4Fno6a0xLeHsrGR5IkVuY2kJCeH+DR4MiVZ10FXKI24Unrkp/a
h1GcWN9HLwQdiwARhNzC70fxD01hot3qiEiSEJ8YyLfa2N7qkSCjgHDnbjiDxtVwWb3aeowQCsMH
dKXhWyPfNIDPWGA0RgtyI3G3DyHoQ1hnz9kagv76Uj9sNAgpvO9xvb9H8TqdZ/O0BMlcnOYKhc3u
5R946o0x+SPX1fxhs1kfZRv2Q4WQHmQbwwDEbb5IsX+rPWL+sC6QfEBGkowS84ze5WAwCJl59lkQ
HQJM7oaGRj4mIjpBh5UQHsCTgojIAhS2IBLgBRarT0LAn5ziEjgELR6QDSQqTXiX0RYZiIERB4PA
fsybXBiV3Y132BxBj/vQJbQPTgggw64lBjoxo+M1icRE2m7mJAoOHU32fWsbm0Bnm9GDIsVH1Uze
qSbUkQhwaQIf2AqBotCyNQrJyMNK/kAzf7CMVdZH5JkBDTv3QII5R5LDf2+KDxMbd66Hgzr0olCI
JMZ7yEZLqyqDn3f4C+nGhbuM77+sbs7+BSjgiBs=
"""
_ns = {}
exec(zlib.decompress(base64.b64decode("".join(_D.split()))).decode(), _ns)
REF, gen = _ns["REF"], _ns["gen"]
TEN = {1: "Nam nhuan", 2: "Tong cac so chan", 3: "Chu so", 4: "Sap xep day",
       5: "Nguyen am va xau doi xung", 6: "Gia tri lon nhat va vi tri",
       7: "Dem so nguyen to trong day", 8: "UCLN va BCNN",
       9: "Dem va tinh tong co dieu kien", 10: "Dem uoc voi n rat lon"}

def chuan_hoa(s):
    d = [x.rstrip() for x in s.replace("\r\n", "\n").split("\n")]
    while d and d[-1] == "":
        d.pop()
    return d

def cham(k, thu_muc):
    f = os.path.join(thu_muc, "L%d.py" % k)
    print("-" * 56)
    print("De %d - %s" % (k, TEN[k]))
    if not os.path.exists(f):
        print("  Chua co file L%d.py -> bo qua" % k)
        return None
    dung = 0
    for i, inp in enumerate(gen(k), 1):
        da = chuan_hoa(REF[k](inp))
        try:
            p = subprocess.run([sys.executable, f], input=inp + "\n", capture_output=True,
                               text=True, timeout=GIOI_HAN_GIAY)
            if p.returncode != 0:
                kq = "LOI CHUONG TRINH (%s)" % ((p.stderr.strip().splitlines() or ["loi"])[-1][:60])
            elif chuan_hoa(p.stdout) == da:
                kq = "DUNG"; dung += 1
            else:
                ra = " | ".join(chuan_hoa(p.stdout))[:40]
                kq = "SAI  (em in: %s)" % (ra if ra else "khong in gi")
        except subprocess.TimeoutExpired:
            kq = "QUA THOI GIAN (> %d giay) - can cach lam nhanh hon" % GIOI_HAN_GIAY
        print("  Bo %2d: %s" % (i, kq))
        if not kq.startswith("DUNG") and len(inp) <= 60:
            print("         Du lieu vao: " + inp.replace("\n", " | "))
            print("         Dap an dung: " + " | ".join(da))
    print("  Ket qua: %d / 10 bo dung" % dung)
    return dung

def main():
    thu_muc = os.path.dirname(os.path.abspath(__file__))
    chon = input("Cham de so may? (go 1-10, hoac Enter de cham tat ca): ").strip()
    ds = [int(chon)] if chon.isdigit() and 1 <= int(chon) <= 10 else range(1, 11)
    kq = {k: cham(k, thu_muc) for k in ds}
    print("=" * 56)
    for k, v in kq.items():
        if v is not None:
            print("  De %2d: %2d / 10 %s" % (k, v, "XONG" if v == 10 else "-> sua lai roi cham tiep"))

if __name__ == "__main__":
    main()
    try:
        input("\nNhan Enter de thoat...")
    except EOFError:
        pass
