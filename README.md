# Thivtdb – Tra đáp án nhanh môn Quản lý & Khai thác vận tải đường bộ (lớp SC26-VTDB38)

Repo chứa **ngân hàng đáp án đã số hóa** (Pháp luật 400 câu, Khai thác 196 câu, Thống kê 5 bộ × 40 câu, công thức tính năng suất/giá thành, hướng dẫn báo cáo thực hành) và **bộ công cụ để AI tra đáp án giúp bạn**.

> ⚠️ Chỉ dùng để **ôn tập / tra cứu theo đúng quy định của kỳ thi**. Tài liệu của trường có ghi "không được dùng tài liệu" – bạn tự chịu trách nhiệm về việc dùng trong phòng thi. Đáp án do người dùng và AI tổng hợp, **không đảm bảo 100%**; câu nào đánh dấu ⚠ là độ chắc chắn thấp.

## Tình trạng đáp án

| Môn | Số câu | Tình trạng |
|---|---|---|
| Pháp luật | 400 | Đủ đáp án + giải thích |
| Khai thác | 196 | Đủ đáp án (câu 181-196 là bài tính) |
| Thống kê (bộ A, B, C, D1, D2) | 5 × 40 | Đủ đáp án (cập nhật 28/10/2026) – vài câu ⚠ độ chắc chắn thấp: B11, B40, C3, C14, C15, C17, C19, D1/D2-26, D1/D2-33 |
| Bài tính năng suất / giá thành | – | Có công thức + máy tính Python |

## Cách nhanh nhất: chụp ảnh câu hỏi → AI trả đáp án

**Bước 1 – Tải repo**
```bash
git clone https://github.com/<tên-bạn>/Thivtdb.git
```
(hoặc bấm *Code → Download ZIP* rồi giải nén).

**Bước 2 – Mở repo bằng một AI có đọc được file + nhận ảnh** (xem mục dưới theo từng loại AI).

**Bước 3 – Chụp màn hình câu hỏi và dán vào khung chat** (`Ctrl+V`, hoặc kéo-thả ảnh), kèm câu lệnh mẫu:

```
Đọc _KB_THI/00_README_AI.md trước. Đây là ảnh các câu trắc nghiệm.
Với mỗi câu: tra trong ngân hàng (tools/tra_cuu.py hoặc grep), trả về
"Câu N: <chữ cái trong ẢNH> – <nội dung đáp án>" . Đề có thể xáo thứ tự A-D
nên hãy chọn theo NỘI DUNG đáp án. Câu nào không có trong ngân hàng thì nói rõ, đừng bịa.
```

### Mẹo chụp ảnh để AI đọc chính xác
- Chụp **toàn bộ câu hỏi + đủ 4 đáp án** trong cùng một ảnh, chữ rõ, không bị cắt, không chói/lóa.
- Dùng **Win + Shift + S** (Windows) hoặc **Cmd + Shift + 4** (Mac) để chụp vùng chọn, dán thẳng vào chat – nhanh hơn chụp bằng điện thoại.
- Mỗi ảnh nên chứa **3–6 câu**; nhiều quá AI dễ đọc sót.
- Câu có **bảng số liệu / bài tính**: chụp cả bảng, dặn AI "tính lại, làm tròn từng bước 2–3 số lẻ, chọn đáp án gần nhất".
- Nếu AI trả lời khác ngân hàng: yêu cầu "cho xem câu tương ứng trong ngân hàng (mã câu)" rồi tự đối chiếu.

## Hướng dẫn theo từng loại AI

### 1) Claude Code (CLI hoặc extension VS Code) – tiện nhất
Repo đã có sẵn skill `thi-vtdb` (`.claude/skills/thi-vtdb/SKILL.md`). Chỉ cần mở thư mục repo bằng Claude Code rồi:
- gõ `/thi-vtdb` (hoặc nói "tra đáp án thi vận tải") và dán ảnh câu hỏi;
- Claude tự đọc `_KB_THI/`, chạy `tra_cuu.py`, trả đáp án.

### 2) Các AI "agent" đọc được thư mục (Codex CLI, Gemini CLI, Cursor, Copilot Chat, Windsurf, Cline…)
Mở thư mục repo trong công cụ đó (file `AGENTS.md` ở gốc repo sẽ chỉ AI tới `_KB_THI/00_README_AI.md`). Nếu công cụ không tự đọc `AGENTS.md`, dán câu đầu tiên:
```
Hãy đọc AGENTS.md và _KB_THI/00_README_AI.md trong repo này, rồi làm theo để tra đáp án cho các ảnh tôi gửi.
```

### 3) AI chat trên web, không đọc được thư mục (ChatGPT, Gemini, Claude.ai, Copilot web, Grok…)
Tạo một cuộc trò chuyện / Project / GPT / Gem mới và **tải lên các file trong `_KB_THI/`** (chỉ cần các file `.md` sau, tổng nhẹ):
`00_README_AI.md`, `DAP_AN_BO_SUNG.md`, `10_PHAP_LUAT_400cau.md`, `20_KHAI_THAC_196cau.md`, `21_KHAI_THAC_CONG_THUC.md`, `23_GIA_THANH_CONG_THUC.md`, `30_THONG_KE_bank.md`.
Sau đó dán *system prompt* này (hoặc đặt vào phần Instructions của Project/GPT/Gem):
```
Bạn là trợ lý tra đáp án thi môn Quản lý & khai thác vận tải đường bộ.
Chỉ dùng các file đã tải lên làm nguồn. Khi tôi gửi ảnh câu hỏi: đọc từng câu,
tìm câu tương ứng trong file (khớp theo NỘI DUNG, vì đề có thể xáo A-D),
trả lời dạng "Câu N: <chữ cái trong ảnh> – <nội dung đáp án>".
Bài tính: dùng công thức trong file 21/23, làm tròn từng bước, chọn đáp án gần nhất.
Câu không có trong file: nói rõ "chưa có trong ngân hàng", không bịa đáp án chính thức.
```
Rồi gửi ảnh như bình thường. (Nếu AI giới hạn số file, gộp bớt hoặc chỉ tải file của môn đang thi.)

### 4) Không có AI – tra tay bằng Python
```bash
py _KB_THI/tools/tra_cuu.py "nội dung câu hỏi (có thể kèm các đáp án)"
py _KB_THI/tools/tinh_nang_suat.py        # máy tính năng suất phương tiện
```
Hoặc dùng Ctrl+F trong VS Code tìm từ khóa trong `_KB_THI/*.md`.

## Cấu trúc repo

| Đường dẫn | Nội dung |
|---|---|
| `_KB_THI/00_README_AI.md` | **Bản đồ cho AI – đọc đầu tiên** |
| `_KB_THI/10_PHAP_LUAT_400cau.md` | 400 câu Pháp luật + đáp án + giải thích |
| `_KB_THI/20_KHAI_THAC_196cau.md` | 196 câu Khai thác + đáp án |
| `_KB_THI/21_…`, `23_…` | Công thức năng suất / giá thành |
| `_KB_THI/30_THONG_KE_bank.md` | 5 bộ Thống kê (A, B, C, D1, D2) đủ đáp án |
| `_KB_THI/32_THONG_KE_DE2_dapan.md` | Đáp án Thống kê Đề 2 (mã 002) |
| `_KB_THI/DAP_AN_BO_SUNG.md` | Đáp án bổ sung/cập nhật mới nhất (AI đọc trước) |
| `_KB_THI/data/` | JSON ngân hàng cho `tra_cuu.py` (`tk_answers.json` = đáp án Thống kê) |
| `_KB_THI/tools/` | `tra_cuu.py`, `tinh_nang_suat.py` |
| `_KB_THI/40_BAO_CAO_THUC_HANH.md`, `_NOP_BAI/` | Hướng dẫn & bài báo cáo thực hành mẫu |
| Các file `.pdf/.docx/.xlsx` ở gốc | Tài liệu gốc của trường/thầy (bản gốc để đối chiếu) |

## Bổ sung / sửa đáp án
Phát hiện đáp án sai? Sửa trong `_KB_THI/DAP_AN_BO_SUNG.md` (ghi nguồn) rồi tạo Pull Request – AI luôn đọc file này trước khi trả lời.
