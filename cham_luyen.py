# -*- coding: utf-8 -*-
# TU CHAM 20 DE LUYEN TAP NHOM B (Phan "Luyen viet chuong trinh" trong tai lieu on)
# Cach dung: luu bai De 1 thanh L1.py, De 2 thanh L2.py, ... De 20 thanh L20.py
#   trong CUNG thu muc voi file nay, roi mo file nay bang IDLE/Thonny va bam F5.
import os, sys, subprocess, time, zlib, base64
GIOI_HAN_GIAY = 2
_D = """
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
iE7BIzCljnh9Fu/9A1TWTng=
"""
_ns = {}
exec(zlib.decompress(base64.b64decode("".join(_D.split()))).decode(), _ns)
REF, gen = _ns["REF"], _ns["gen"]
TEN = {1: "Nam nhuan", 2: "Tong cac so chan", 3: "Chu so", 4: "Sap xep day",
       5: "Nguyen am va xau doi xung", 6: "Gia tri lon nhat va vi tri",
       7: "Dem so nguyen to trong day", 8: "UCLN va BCNN",
       9: "Dem va tinh tong co dieu kien", 10: "Dem uoc voi n rat lon",
       11: "Tam giac", 12: "Tong chia het cho 3 hoac 5", 13: "So dao nguoc",
       14: "Day giam dan", 15: "Chu hoa, chu thuong, chu so", 16: "Nho nhat, vi tri cuoi",
       17: "Tong so nguyen to", 18: "Rut gon phan so", 19: "Dem va tong co dieu kien 2", 20: "So hoan hao"}

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
    chon = input("Cham de so may? (go 1-20, hoac Enter de cham tat ca): ").strip()
    ds = [int(chon)] if chon.isdigit() and 1 <= int(chon) <= 20 else range(1, 21)
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
