---
name: thi-vtdb
description: Hỗ trợ thi kết thúc học phần Quản lý & khai thác vận tải đường bộ (SC26-VTDB38) - tra đáp án trắc nghiệm Pháp luật/Khai thác/Thống kê, tính năng suất, giá thành, báo cáo thực hành, checklist ngày thi.
---
Đọc `_KB_THI/00_README_AI.md` trước (bản đồ + cách làm). Chỉ cần đọc thư mục `_KB_THI/`, không cần đọc tài liệu gốc.
- Câu trắc nghiệm: `py _KB_THI/tools/tra_cuu.py "<câu hỏi>"`; kiểm `_KB_THI/DAP_AN_BO_SUNG.md` trước; đề có thể xáo A-D nên trả lời theo nội dung đáp án.
- Bài tính năng suất: `_KB_THI/21_KHAI_THAC_CONG_THUC.md` + `tools/tinh_nang_suat.py`.
- Giá thành/giá cước: `_KB_THI/23_GIA_THANH_CONG_THUC.md`.
- Báo cáo & ngày thi: `40_BAO_CAO_THUC_HANH.md`, `01_NGAY_THI_CHECKLIST.md`.
- Câu chưa có đáp án: báo rõ là chưa có, không bịa đáp án chính thức.
- Câu lạ không có trong ngân hàng: grep `_KB_THI/data/giao_trinh_khai_thac.txt`, rồi được phép WebSearch (xem mục "QUY TRÌNH CÂU LẠ" trong 00_README_AI.md); ghi kết quả vào DAP_AN_BO_SUNG.md.
