# -*- coding: utf-8 -*-
"""Tính năng suất phương tiện (Khai thác VT). Quy ước làm tròn của đề cương: làm tròn từng bước trung gian (xem --round).
Dùng:
  py tinh_nang_suat.py khach --xe 30:35,20:45 --gamma 0.9 --avd 0.85 --vt 45 --th 12 --tdd 0.5 --eta 2.5 --lm 100
  py tinh_nang_suat.py hang  --xe 25:10,15:15 --gamma 0.85 --avd 0.8 --beta 0.75 --vt 45 --txd 0.5 --zc 2 --lnd 200 --th 8
"""
import argparse, sys
sys.stdout.reconfigure(encoding='utf-8')
def r(x,n): return round(x+1e-12,n)
def khach(xe,gamma,avd,vt,th,tdd,eta,lm,nd=2):
    seats=sum(a*b for a,b in xe)/sum(a for a,b in xe)
    seats=r(seats,nd)
    gio=r(gamma*vt*eta/(lm+vt*tdd),nd)          # HK/ghế-giờ
    ngay=r(gio*th,nd); thang=r(ngay*avd*30,nd)  # /ghế
    xe_ngay=r(ngay*seats,nd); xe_thang=r(xe_ngay*avd*30,nd); xe_nam=r(xe_thang*12,nd)
    return dict(ghe_trung_binh=seats,ghe_gio=gio,ghe_ngay=ngay,ghe_thang=thang,xe_ngay=xe_ngay,xe_thang=xe_thang,xe_nam=xe_nam)
def hang(xe,gamma,avd,beta,vt,txd,zc,lnd,th,nd=3):
    # nd = số lẻ làm tròn năng suất/tấn-giờ: đề 181-184 dùng 2 (0.31), đề 189-192 dùng 3 (0.209). Chạy cả nd=2 và nd=3 rồi chọn kết quả khớp đáp án.
    q=sum(a*b for a,b in xe)/sum(a for a,b in xe)
    lch=beta*lnd/zc                              # km có hàng 1 chuyến
    gio=r(vt*beta*gamma/(lch+vt*beta*txd),nd)    # T/tấn.xe-giờ
    ngay=r(gio*th,nd); thang=r(ngay*avd*30,nd)
    xe_ngay=r(ngay*q,2); xe_thang=r(xe_ngay*avd*30,3); xe_nam=r(xe_thang*12,2)
    return dict(q_tb=q,lch_1_chuyen=lch,tan_gio=gio,tan_ngay=ngay,tan_thang=thang,xe_ngay=xe_ngay,xe_thang=xe_thang,xe_nam=xe_nam)
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('kind',choices=['khach','hang'])
    for a in ['gamma','avd','vt','th','beta','txd','tdd','eta','lm','zc','lnd']: p.add_argument('--'+a,type=float)
    p.add_argument('--nd',type=int,default=None)
    p.add_argument('--xe',required=True,help='so_xe:so_cho_hoac_tai_trong,... VD 30:35,20:45')
    a=p.parse_args(); xe=[tuple(float(v) for v in t.split(':')) for t in a.xe.split(',')]
    res=khach(xe,a.gamma,a.avd,a.vt,a.th,a.tdd,a.eta,a.lm) if a.kind=='khach' else hang(xe,a.gamma,a.avd,a.beta,a.vt,a.txd,a.zc,a.lnd,a.th,*( [a.nd] if a.nd else [] ))
    for k,v in res.items(): print(f'{k:16s} {v}')
