# TÍNH GIÁ THÀNH / GIÁ CƯỚC VẬN TẢI (dùng cho Báo cáo thực hành – mục 2.3)

Nguồn: các file Excel "Hướng dẫn tính bài tập CPVT*.xlsx" (4 bản; cấu trúc 13 sheet giống nhau, chỉ khác số đầu vào). Công thức dưới đây trích từ bản "Copy of … _update (1).xlsx".
Bản gốc "Hướng dẫn tính bài tập CPVT.xlsx" = bộ số của mẫu hướng dẫn báo cáo (1 xe, 100 km/chuyến, 720 chuyến/năm → giá cước làm tròn 28.000 đ/km). Dùng bản này nếu chỉ cần "cho đủ".

## Sheet "Chung" (thông tin chung) – ô nhập: B4 t đầu cuối, B5 t xếp dỡ, B7 quãng đường huy động, B8 cự ly/chuyến, B9 V_T, B10 số chuyến/năm, B16 hệ số định biên, B17 số xe
- t lăn bánh B3 = B8/B9 ; t 1 chuyến B6 = B3+B4+B5
- Số chuyến/ngày B11 = B10/360 (bản update: /312) ; /tháng B12 = B11×30
- Quãng đường ngày đêm B13 = B8×B11 + B7
- **Quãng đường năm B14 = B13 × 360 × B17**  (mẫu số "đ/km xe chạy")
- t làm việc/ngày B15 = B6×B11 ; số lái xe B18 = B16×B17
- **Quãng đường quy đổi đường loại 1 B20 = B14×0,3×1 + B14×0,4×1,15 + B14×0,3×1,25** (dùng cho nhiên liệu, VLBT, săm lốp, BDSC)

## 12 khoản mục (đ/km xe chạy) – chia cho B14 (quãng đường thực) trừ khi ghi chú
1. **Lương lái xe** = (số lái × lương tháng × 12) / B14
2. **Trích theo lương** = quỹ lương năm × 23,5% (DN: BHXH 17,5 + BHYT 3 + BHTN 1 + KPCĐ 2) / B14 (người LĐ 10,5% không tính vào giá thành)
3. **Nhiên liệu** = (B20/100 × định mức l/100km) × đơn giá / B14
4. **VLBT** = lít nhiên liệu × 4% × đơn giá VLBT / B14
5. **Săm lốp** = (B20 / định ngạch đời lốp × số bộ lốp/xe) × giá lốp / B14
6. **BDSC** = [BDN: (số xe×hệ số vận doanh×360×hệ số BDN)×chi phí BDN] + [BDĐK: (B20/định ngạch BDĐK)×chi phí BDĐK] + [SCTX: (B20/1000)×chi phí SCTX/1000km] ; chia B14
7. **Khấu hao** = số xe × nguyên giá × tỷ lệ KH% / B14
8. **Trích trước SCL** = KH cơ bản × 50% / B14
9. **Bảo hiểm** = (số xe × nguyên giá × tỷ lệ BH vật chất%) + (BH TNDS/xe × số xe), / B14
10. **Lệ phí, bến phí** = số xe × (phí bảo trì đường bộ + đăng kiểm) + lệ phí cầu đường, / B14
11. **Thuế đầu vào/ lãi vay – thuê đất** = (tổng vốn xe × %vay × lãi suất) + tiền thuê đất 1 năm, / B14
12. **Quản lý phí** = 8% × tổng 11 khoản trên
- **Tổng chi phí 1 km** = Σ12 khoản ; Giá cước chưa VAT = Tổng × (1 + 10% lợi nhuận) ; Giá cước có VAT = ×1,08 ; Làm tròn ROUND(…, -2) ; Giá cước/chuyến = giá làm tròn × cự ly 1 chuyến (100 km).
- Tỷ trọng % = từng khoản / tổng chi phí.

## Mẫu số liệu của Hướng dẫn báo cáo (dùng sẵn, "cho đủ")
Bảng 1: t lăn bánh 2h; đầu cuối 1h; xếp dỡ 0; 1 chuyến 3h; huy động 5km; cự ly 100km; 720 chuyến/năm (2/ngày; 60/tháng); quãng đường ngày 205km; năm **73.800 km**; 1 xe, 1 lái; quy đổi **80.073 km**.
Kết quả: lương 4.878,05; trích lương 1.146,34; nhiên liệu 5.927,36 (30 l/100km, 18.210 đ/l); VLBT 1.562,40; săm lốp 1.392,42; BDSC 2.599,16; KHCB 2.032,52 (1,5 tỷ, 10%); SCL 1.016,26; bảo hiểm 268,29; lệ phí 241,46; thuế đầu vào 487,80 (thuê đất 36 tr); QLP 1.724,16 ⇒ **Tổng 23.276 đ/km → giá cước chưa VAT 25.604 → có VAT 27.652 → làm tròn 28.000 đ/km**.

## Bản mẫu sinh viên Bùi Anh Quốc (10 đầu kéo container 45', 636.000 km/năm): Tổng 35.006,26 đ/km → 41.600 đ/km (4.160.000 đ/chuyến 100km). Chỉ tham khảo cách viết, KHÔNG sao chép nội dung công ty.

## Lưu ý khi thay số
- Số liệu trong 4 file khác nhau: ví dụ bản update có B5=2h xếp dỡ, 450 chuyến/năm, 120 km, 5 xe, V_T 30 km/h, nhiên liệu 45 l/100km giá 29.120 đ/l. Chọn 1 bộ và dùng nhất quán trong toàn báo cáo (bảng 1 → bảng 13).
- Giá dầu: cần ghi ngày tra cứu (bản mẫu ghi "Petrolimex ngày …").
