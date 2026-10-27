# KHAI THÁC VẬN TẢI – CÔNG THỨC & CÁCH TÍNH (đã kiểm chứng khớp đáp án câu 181-196)

Nguồn công thức: giáo trình "BG_KHAI THAC VAN TAI mới.pdf" (trang 24-28) + đối chiếu bảng đáp án 196 câu.
Công cụ chạy tự động: `py tools/tinh_nang_suat.py ...` (lệnh mẫu ở cuối file).

## 1. Ký hiệu
| Ký hiệu | Ý nghĩa |
|---|---|
| q | trọng tải (tấn) hoặc số chỗ (ghế) của xe |
| γ (gamma) | hệ số sử dụng trọng tải / hệ số sử dụng chỗ |
| β (beta) | hệ số lợi dụng quãng đường = Lch / Lchung |
| α_VD (avd) | hệ số ngày xe vận doanh |
| V_T | vận tốc kỹ thuật (km/h) |
| T_H | thời gian xe hoạt động trong ngày (h) |
| t_xd | thời gian xếp dỡ 1 chuyến (h) (hàng) |
| t_dđ | thời gian dừng đỗ đầu cuối 1 chuyến (h) (khách) |
| η_HK | hệ số thay đổi hành khách = L_M / L_HK |
| L_M | chiều dài tuyến (km) |
| Z_c | số chuyến/ngày; L_nđ quãng đường xe chạy ngày đêm |

## 2. VẬN TẢI HÀNH KHÁCH
Quãng đường trung bình 1 ghế (số chỗ TB) q̄ = Σ(số xe × số chỗ) / Σ số xe  (**làm tròn 2 số lẻ**, vd 38,33).

1. Năng suất 1 **ghế**-giờ: `W_gh,giờ = γ · V_T · η_HK / (L_M + V_T · t_dđ)`  (HK/ghế.xe-giờ) – làm tròn 2 số lẻ
2. 1 ghế-ngày: `= W_giờ × T_H`
3. 1 ghế-tháng: `= W_ngày × 30 × α_VD`
4. 1 **xe**-ngày: `= W_ghế-ngày × q̄`
5. 1 xe-tháng: `= W_xe-ngày × 30 × α_VD`
6. 1 xe-năm: `= W_xe-tháng × 12`   (giáo trình cho phép cách khác: ×365×α_VD – nếu đáp án đề dùng ×12 thì theo ×12)

(Nếu tính HK.Km: nhân thêm L_HK = L_M/η_HK.)

**Quy ước làm tròn của đề cương: làm tròn 2 số lẻ SAU TỪNG BƯỚC rồi mới nhân tiếp** (vd ghế-giờ 0,8265→0,83; 0,83×12=9,96). Làm tròn khác đi sẽ lệch đáp án một chút → luôn chọn đáp án GẦN NHẤT.

### Ví dụ mẫu = ĐỀ 2 KHAI THÁC (câu 2, 5 điểm)
Dữ liệu: 30 xe 35 chỗ + 20 xe 45 chỗ; γ=0,9; α_VD=0,85; V_T=45; T_H=12; t_dđ=0,5; η_HK=2,5; L_M=100.
- q̄ = (30×35+20×45)/50 = 39 chỗ
- W ghế-giờ = 0,9×45×2,5/(100+45×0,5) = 101,25/122,5 = **0,83 HK/ghế.xe-giờ**
- ghế-ngày = 0,83×12 = **9,96 HK/ghế.xe-ngày**
- ghế-tháng = 9,96×30×0,85 = **253,98 HK/ghế.xe-tháng**
- xe-ngày = 9,96×39 = **388,44 HK/xe-ngày**
- xe-tháng = 388,44×30×0,85 = **9.905,22 HK/xe-tháng**
- xe-năm = 9.905,22×12 = **118.862,64 HK/xe-năm**
(đây chính là đáp án câu 193-196 của ngân hàng).

## 3. VẬN TẢI HÀNG HÓA
- Trọng tải TB q̄ = Σ(số xe × tấn)/Σ số xe  (vd (25×10+15×15)/40 = 11,875)
- Quãng đường có hàng cả ngày: `Lch = β × L_nđ`;  có hàng 1 chuyến: `l_ch = Lch / Z_c`
- 1 **tấn trọng tải**-giờ: `W_Q = V_T · β · γ / (l_ch + V_T · β · t_xd)` (T/Tấn.xe-giờ)
- ngày: `× T_H`;  tháng: `× 30 × α_VD`
- 1 xe-ngày: `× q̄`;  xe-tháng: `× 30 × α_VD`;  xe-năm: `× 12`
- Làm tròn: bộ câu 181-184 làm tròn W_giờ 2 số lẻ (0,31); bộ 189-192 làm tròn 3 số lẻ (0,209) → thử `--nd 2` và `--nd 3`, chọn kết quả trùng 1 đáp án.
- Nhu cầu phương tiện = Nhiệm vụ (T.Km/năm) / (năng suất 1 xe-năm tính T.Km).

Kết quả mẫu: 25 xe 10T + 15 xe 15T; γ=0,85; α=0,8; β=0,75; V=45; txd=0,5; Zc=2; Lnđ=200; TH=8 →
0,31 T/Tấn.xe-giờ; 2,48 T/Tấn.xe-ngày; 59,52 T/Tấn.xe-tháng; 29,45 T/xe-ngày; 706,8 T/xe-tháng; (xe-năm 8.481,6 – đáp án 10.602 là SAI).

## 4. Các chỉ tiêu khác (giáo trình tr.24-26)
- T_H = t_lb + t_xd + t_đc ;  L_nđ = L_hđ + L_ch + L_rỗng
- Hệ số ngày xe tốt α_T = A_DT / A_dc ; hệ số vận doanh α_VD = A_DVD / A_dc
- γ_T (tĩnh) = Q_tt / q_TK ;  γ_đ (động) = P_tt / P_TK
- β = L_ch / L_chung ;  η_HK = L_M / L_HK
- Thời gian 1 chuyến hàng: t_ch = l_ch / V_T + t_xd ;  khách: t_c = L_M/V_T + t_dđ ;  Q_c (khối lượng 1 chuyến khách) = q·γ·η_HK
- Cự ly vận chuyển bình quân 1 tấn: l_hh = P / Q

## 5. Lệnh mẫu (chạy trong thư mục _KB_THI)
```
py tools/tinh_nang_suat.py khach --xe 30:35,20:45 --gamma 0.9 --avd 0.85 --vt 45 --th 12 --tdd 0.5 --eta 2.5 --lm 100
py tools/tinh_nang_suat.py hang  --xe 25:10,15:15 --gamma 0.85 --avd 0.8 --beta 0.75 --vt 45 --txd 0.5 --zc 2 --lnd 200 --th 8 --nd 2
```
