# -*- coding: utf-8 -*-
# CHAM BAI THI THU - NHOM B (Python)
# Cach dung: dat file cham.py nay vao cung thu muc voi bai lam
#   (vi du thu muc BAILAM), roi chay file nay (mo bang IDLE/Thonny, bam F5).
import os, re, sys, subprocess, time, zlib, base64

GIOI_HAN_GIAY = 2   # thoi gian toi da cho moi bo du lieu

_D = """
eNqdV1tzokgUfs+vOMPWVEDR6W7A63Sq9jKz+zIvmdS+GGsLlURGbVzARDeV/77ndCMgJtmtkCCH
c/363GLizTZJc0hDtUg2Fz9Bp7wgje6iNFLzCLJkvcvjRGUjiNV2l0OWp9C5gmSXl2/ldbGI7mDB
Z9zOnNEF4JXLrJtt13FuOxM2HaPjfJcquLOest3GjlVuzx24S1KYo3vInWd42oR7Gwnr6EyUzh7k
Os5yexNuydItPTvOGJR80AFCfPIRbyukv0sKEjrauIiMgG3ich11T1FDiO9g31JX3x3nGNQrgz5W
JxjDLMpy+YiBtKj08GhU6UJX60jZe+eKHqTvjIzZvg4DE0DyR+f5Vj2RuDqvX4YO3Zk8P+wYsgc5
O+RRmKbhwZ7wqdOyZ22uBQhNsosCyOxK8hExecmUwhxqGa8jiFvxZzk7wY7K8VTboHA0iqe1SAQY
m+U+slHmYkQ3xtRX1m3JX8o0+gpHqD09ZlfU+mPjHl444vEAGynF6OjPEkOLmPbhoy8lA2xbOHzk
jH2QzAEsBfIZI0m0ziJUH1h1OJbHtPmGCmb7bs8dupw7hbLHrSO49/fbN0m9e+w3Odk3e+zzt2oE
KD2knjoOydICSKcCUvWgkjQp9UlCBLlkYywobxZUnRRUfYwxJRVLD2VbxicM1Is/SPXpUzwiIRFv
ljUvK+n/v2S5K50ul1rR5EyMhM7ZQj49j2Fe9GeVrwrxvC0X3fsot1edvcvQ22KynxYsYrTP4M2d
i+svX+WTzV3ujGgfuUgKTQoiPU16RPqa9F1baF1BukLrCtIVWleQrtC6eOTn012Z4/TCfaSiNMyT
NGuuQ5TYi8idhXGRqGtpNm73Wj9Q2MImbpPCGG7kxOwWMsWxs5W7Ttwl2pZ9DFb3RxIrm0563SVf
1BxGy+zSvyiDZlJVNUxHFFKavJQJxphWwETfcq0hG+InUQipeZH87LKmlZ+2hMkpKgzEWq1VgWul
R88zoxe4fOAY42jdhCea8G6VBwMIgDPwEYd/qwToH4J6qzpBDQeFKtJGASc2Z24Hb84crDhDAsmC
1pJWa6hxDpEXsELBvNIzaOoYJrXRiwrT02m76YbbbaQWNu58Reu+XtZny3klBV4jBQDLZI70OtxC
nsZqCdtDvkwUAKbgz1hl82WSrJEOZzBfAHXespYU6qfHJF3YtU4qGum6i6bxPLLRdI5698v4x2q9
Ucn27zTLdw+P+8M/P//y629fvv7+h3XWYSfFFvU/CKRotm3gCkq/vpmrUzxgxStzXkmXjZ3eqrwz
zIhjAE8sa+q0S/zmWO1TdUpgE+rmiO48234j29hnHjU8B46fRZ8BN1OABziShme4vic4mKGoBMXU
sMKksBKeH/RgOOj3At96eQjE2YwiCiZ8DYcPtR+fOD0D8Iin4HChkQ/pPaB3lHCtgrq+JvpQG+Dz
8M0Z7N2qANAf3n3w0N67VT74eh5xBLn2jU+oVsd/DCV3g5cmkp8N2ul73+2/a8YaigYm6l7CZdFX
lxX0y2lLl7I9uSx33eX01XkVZ/PKdcvQTeUY0k7tC4a/xRodeM0te7JfB9REw57X73E+HJiC9Rgb
BNzv4+29WrZmJwfQo6IE4OGP0E3DGXEEvlPtelBtU71Rm0Vb1csW0NS6xTLFQUCyE9BMH6vXN8I3
CwRPq7eK9EJYU3m9rYu9UbWHWb2NJhHEqXSEh8Y4I+/GFWZZhP8s0XfgG0w0Z/UvHTcX/wKATVGc
"""
_ns = {}
exec(zlib.decompress(base64.b64decode("".join(_D.split()))).decode(), _ns)
REF, gen = _ns["REF"], _ns["gen"]

TEN_BAI = {
    1: {1: "CHU SO", 2: "TREN TRUNG BINH", 3: "TU DAI NHAT", 4: "SO NGUYEN TO TRONG DOAN"},
    2: {1: "SO NGAY TRONG THANG", 2: "LON THU HAI", 3: "TONG UOC", 4: "DEM CAP"},
}

def chuan_hoa(s):
    dong = [d.rstrip() for d in s.replace("\r\n", "\n").split("\n")]
    while dong and dong[-1] == "":
        dong.pop()
    return dong

def tim_file(thu_muc, bai):
    tat_ca = os.listdir(thu_muc)
    dung = [f for f in tat_ca if re.fullmatch(r"[A-Za-z]{2}\d{3}_B%d\.py" % bai, f)]
    return dung, tat_ca

def cham_mot_bai(de, bai, thu_muc):
    print("-" * 56)
    print("Bai B%d - %s (5 diem)" % (bai, TEN_BAI[de][bai]))
    dung, tat_ca = tim_file(thu_muc, bai)
    if not dung:
        nghi_ngo = [f for f in tat_ca if f.lower().endswith(".py") and ("b%d" % bai) in f.lower()]
        print("  KHONG TIM THAY file dung ten dang SoBaoDanh_B%d.py (vi du GP012_B%d.py)." % (bai, bai))
        if nghi_ngo:
            print("  Co file nhung SAI TEN:", ", ".join(nghi_ngo), "-> thi that se KHONG duoc cham!")
        print("  Diem: 0 / 5")
        return 0.0
    if len(dung) > 1:
        print("  Canh bao: co nhieu file:", ", ".join(dung), "- chi cham file", dung[0])
    ten = dung[0]
    print("  File:", ten)
    diem = 0.0
    for i, inp in enumerate(gen(de, bai), 1):
        dap_an = chuan_hoa(REF[(de, bai)](inp))
        try:
            t0 = time.time()
            p = subprocess.run([sys.executable, os.path.join(thu_muc, ten)], input=inp + "\n",
                               capture_output=True, text=True, timeout=GIOI_HAN_GIAY)
            tg = time.time() - t0
            if p.returncode != 0:
                loi = (p.stderr.strip().splitlines() or ["loi"])[-1]
                kq = "LOI CHUONG TRINH (%s)" % loi[:60]
            elif chuan_hoa(p.stdout) == dap_an:
                kq = "DUNG (%.2f giay)" % tg
                diem += 0.5
            else:
                ra = " | ".join(chuan_hoa(p.stdout))[:40]
                kq = "SAI  (em in: %s)" % (ra if ra else "khong in gi")
        except subprocess.TimeoutExpired:
            kq = "QUA THOI GIAN (> %d giay) - can cach lam nhanh hon" % GIOI_HAN_GIAY
        print("  Bo %2d: %s" % (i, kq))
        if i <= 2 and not kq.startswith("DUNG"):
            print("         Du lieu vao: " + inp.replace("\n", " | ")[:60])
            print("         Dap an dung: " + " | ".join(dap_an)[:60])
    print("  Diem: %.1f / 5" % diem)
    return diem

def main():
    thu_muc = os.path.dirname(os.path.abspath(__file__))
    print("CHAM BAI THI THU NHOM B - thu muc:", thu_muc)
    de = input("Cham de so may? (go 1 hoac 2 roi Enter): ").strip()
    while de not in ("1", "2"):
        de = input("Chi go 1 hoac 2: ").strip()
    de = int(de)
    tong = sum(cham_mot_bai(de, b, thu_muc) for b in range(1, 5))
    print("=" * 56)
    print("TONG DIEM DE %d: %.1f / 20" % (de, tong))
    print("(Moi bai 10 bo du lieu, moi bo 0,5 diem - giong cach cham that)")

if __name__ == "__main__":
    main()
    try:
        input("\nNhan Enter de thoat...")
    except EOFError:
        pass
