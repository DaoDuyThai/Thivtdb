# BẢN ĐỒ TOÀN BỘ – ĐỌC FILE NÀY TRƯỚC (dành cho AI hỗ trợ thi)

Người thi: **Đào Duy Thái**, lớp **SC26-VTDB38** (Trường CĐ Kinh tế Kỹ thuật Công nghiệp, khóa Quản lý & khai thác vận tải đường bộ).
Công ty (báo cáo): CÔNG TY TNHH THƯƠNG MẠI VÀ VẬN TẢI HT LOGISTICS – MST 4900946968.
**Ngày thi: Thứ Năm 29/10/2026, 08h30–11h30, Zoom (vào phòng từ 08h15)**. Hôm thi người dùng ĐƯỢC dùng AI/tài liệu (theo người dùng; tài liệu trường ghi "không được dùng tài liệu" → xem mục Rủi ro ở 01_NGAY_THI_CHECKLIST.md).

## Cách làm việc khi người dùng dán/chụp 1 câu hỏi
1. **Trắc nghiệm (Pháp luật / Thống kê / Khai thác 196 câu):**
   - Chạy `py _KB_THI/tools/tra_cuu.py "<nội dung câu hỏi>"` HOẶC grep từ khóa trong file ngân hàng bên dưới.
   - Đề thật có thể xáo thứ tự A-D → **trả lời theo NỘI DUNG đáp án đúng**, rồi nêu chữ cái tương ứng trong đề.
   - Nếu bank ghi "CHƯA CÓ ĐÁP ÁN" → nói rõ là chưa có đáp án chính thức; (người dùng đã quyết định tự tra rồi gửi lại – ghi vào `DAP_AN_BO_SUNG.md`). Không bịa đáp án chính thức; nếu bắt buộc phải gợi ý thì ghi "AI suy luận, chưa xác minh".
   - Đọc `DAP_AN_BO_SUNG.md` TRƯỚC (đáp án người dùng bổ sung).
2. **Bài tính (Khai thác – năng suất):** dùng `21_KHAI_THAC_CONG_THUC.md` + `tools/tinh_nang_suat.py`; làm tròn từng bước 2 (hoặc 3) số lẻ; chọn đáp án gần nhất.
3. **Tự luận Khai thác:** xem `22_KHAI_THAC_DE2_tuluan.md` (bài giải mẫu hành trình chạy xe + tính năng suất).
4. **Báo cáo thực hành:** xem `40_BAO_CAO_THUC_HANH.md`; file đã làm sẵn ở `../_NOP_BAI/`.

## Bản đồ file
| File | Nội dung |
|---|---|
| 01_NGAY_THI_CHECKLIST.md | Lịch, hạn chót, cần mang/in gì, quy trình Zoom, nộp bài, rủi ro/điểm mâu thuẫn |
| 10_PHAP_LUAT_400cau.md | 400 câu Pháp luật + đáp án + giải thích (đề thi Đề 2 = câu 41-80) |
| 11_PHAP_LUAT_DE2_dapan.md | Đáp án tích sẵn cho Đề 2 Pháp luật (40 câu, 100% có đáp án) |
| 20_KHAI_THAC_196cau.md | 196 câu trắc nghiệm Khai thác + đáp án (câu 181-196 là bài tính) |
| 21_KHAI_THAC_CONG_THUC.md | Công thức năng suất phương tiện (đã kiểm chứng) |
| 22_KHAI_THAC_DE2_tuluan.md | Đề 2 Khai thác dạng TỰ LUẬN: bài giải mẫu |
| 23_GIA_THANH_CONG_THUC.md | Công thức giá thành/giá cước (Excel CPVT) |
| 30_THONG_KE_bank.md | 5 bộ Thống kê (A có đáp án; B, C không; D1/D2 đáp án 1-20) |
| 31_THONG_KE_THIEU_DAP_AN.md | Danh sách câu Thống kê chưa có đáp án (Đề 2 câu 21-40) |
| 32_THONG_KE_DE2_dapan.md | Đáp án Đề 2 Thống kê: 1-20 có, 21-40 chưa |
| 40_BAO_CAO_THUC_HANH.md | Hướng dẫn hoàn thiện & nộp báo cáo |
| DAP_AN_BO_SUNG.md | Đáp án người dùng tự bổ sung |
| tools/ | tra_cuu.py (tìm theo nội dung), tinh_nang_suat.py (máy tính năng suất) |
| data/ | JSON ngân hàng (cho tra_cuu.py) |

## Tình trạng đáp án (tính đến 27/10/2026)
- Pháp luật: **400/400 có đáp án**. Đề 2: 40/40.
- Khai thác: **196/196 có đáp án**; tự luận Đề 2 đã giải.
- Thống kê: Đề 2 **20/40** (câu 21-40 chưa có). Bộ A 40/40. B, C chưa có; D1/D2 có 1-20.
- Tài liệu gốc ở thư mục cha (`..`): giáo trình "BG_KHAI THAC VAN TAI mới.pdf" (3,6MB) dùng để tra lý thuyết Khai thác nếu cần.

## QUY TRÌNH CÂU LẠ (đã được người dùng cho phép tìm trên mạng)
Thứ tự: (1) `tools/tra_cuu.py` / grep ngân hàng → (2) `DAP_AN_BO_SUNG.md` → (3) lý thuyết trong `data/giao_trinh_khai_thac.txt` (giáo trình Khai thác dạng text, grep được; công thức Hy Lạp có thể mất ký tự → ưu tiên file 21) → (4) **WebSearch** (ưu tiên nguồn chính thống: thuvienphapluat.vn, vbpl.vn, luatvietnam.vn; pháp luật vận tải: Luật Đường bộ 2024, NĐ 158/2024/NĐ-CP về kinh doanh vận tải bằng xe ô tô, NĐ 168/2024 xử phạt) → (5) tự suy luận, ghi rõ "chưa xác minh".
- Câu pháp luật: ưu tiên đáp án trong bộ 400 câu (bám đề cương nhà trường); chỉ lên mạng khi không có câu tương tự; nếu văn bản mới mâu thuẫn bank, báo cho người dùng cả hai.
- Sau khi tìm được đáp án mới: ghi vào `DAP_AN_BO_SUNG.md` (ghi nguồn) để lần sau không phải tìm lại.
- Tự luận Khai thác: trình bày theo khung "Công thức → Thay số → Kết quả + đơn vị", kết luận cuối; lý thuyết thì: khái niệm → phân loại → chỉ tiêu → ví dụ minh họa (xem file 22 làm mẫu). Chủ đề chưa có bài mẫu → dựng từ giáo trình.
