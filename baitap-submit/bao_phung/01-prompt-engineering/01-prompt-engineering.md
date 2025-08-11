# Bộ Prompt Thực Hành – Prompt Engineering

---

## Prompt 1: Tạo Câu Hỏi Trắc Nghiệm Dựa Trên Bài Học

**Vai trò:** Giáo viên chuyên nghiệp  
**Yêu cầu:**
- Tạo 10 câu hỏi trắc nghiệm từ nội dung bài học.
- Mỗi câu có 4 phương án (A, B, C, D).
- Chỉ có 1 đáp án đúng.
- Ghi rõ đáp án đúng và giải thích ngắn gọn.
- Ngôn ngữ: tiếng Việt.
- Mức độ: trung bình, phù hợp học sinh trung học.

**Cách dùng:**  
Dán nội dung bài học vào vị trí `[Dán nội dung bài học vào đây]`.

---

## Prompt 2: Phân Tích & Viết Thêm Đoạn Văn

**Vai trò:** Chuyên gia ngôn ngữ & biên tập nội dung  
**Chế độ:**
- **Chế độ 1 – Chỉ phân tích:**
  - Tóm tắt ý chính.
  - Nêu điểm mạnh & điểm cần cải thiện.
  - Xác định thông điệp/chủ đề chính.
- **Chế độ 2 – Phân tích + Viết thêm:**
  - Thực hiện như chế độ 1.
  - Viết thêm một đoạn liền mạch, giữ phong cách/giọng điệu.
  - Mở rộng hoặc bổ sung ý cho đoạn văn giàu hơn.

**Yêu cầu khác:**
- Ngôn ngữ: [tiếng Việt/tiếng Anh].
- Độ dài: [số từ, số câu].
- Chế độ chọn: [1 hoặc 2].
- Đoạn văn: [Dán đoạn văn vào đây]

---

## Prompt 3: Phân Loại & Tổng Hợp Review Khách Hàng

**Vai trò:** Chuyên gia phân tích dữ liệu & cảm xúc khách hàng  
**Nhiệm vụ:**
- Phân loại mỗi review:
  - **Review tốt (tích cực):** Khen ngợi, hài lòng, cảm xúc tích cực.
  - **Review xấu (tiêu cực):** Phàn nàn, chê bai, không hài lòng.
- Đếm số lượng từng nhóm.
- Tổng hợp nội dung chính mỗi nhóm (ý phổ biến, điểm mạnh/yếu).

**Định dạng kết quả:**
```
Tổng số review: X
Số review tốt: X
Số review xấu: X
Tóm tắt review tốt: …
Tóm tắt review xấu: …
```
**Ví dụ:**
- Review tốt: "Dịch vụ giao hàng rất nhanh, nhân viên nhiệt tình."
- Review xấu: "Giao hàng trễ 3 ngày, sản phẩm bị trầy xước."

**Cách dùng:**  
Dán danh sách review vào vị trí `[Dán danh sách review vào đây]`.

---

## Prompt 4: Phân Tích Đoạn Code

**Vai trò:** Senior developer  
**Nhiệm vụ:**
1. **Tìm bug:** Liệt kê lỗi (nếu có), giải thích nguyên nhân.
2. **Gợi ý sửa:** Đề xuất cách sửa từng bug.
3. **Viết thêm comment:** Thêm chú thích ngắn, rõ ràng.
4. **Giải thích code:** Mô tả hoạt động & mục đích code.

**Cách dùng:**  
Dán code vào vị trí `[Dán code vào đây]`.

---

## Prompt 5: Tổng Hợp Thông Tin Địa Điểm Du Lịch

**Vai trò:** Chuyên gia du lịch  
**Nhiệm vụ với mỗi địa điểm:**
- Giới thiệu tổng quan (lịch sử, đặc điểm nổi bật).
- Liệt kê điểm tham quan chính.
- Gợi ý hoạt động trải nghiệm đặc sắc.
- Đề xuất món ăn nổi tiếng.
- Khuyến nghị thời gian tham quan lý tưởng (mùa, giờ).

**Định dạng trình bày:**
```
Tên địa điểm: …
Giới thiệu: …
Điểm tham quan: …
Hoạt động: …
Ẩm thực: …
Thời gian lý tưởng: …
```
**Ví dụ:**
```
Tên địa điểm: Hội An, Việt Nam
Giới thiệu: Phố cổ Hội An là di sản văn hóa thế giới, nổi tiếng với kiến trúc cổ kính và phố đèn lồng rực rỡ.
Điểm tham quan: Chùa Cầu, Nhà Cổ Tấn Ký, Chợ Hội An.
Hoạt động: Đi thuyền trên sông Hoài, tham gia lớp nấu ăn, thả đèn hoa đăng.
Ẩm thực: Cao lầu, mì Quảng, bánh mì Phượng.
Thời gian lý tưởng: Tháng 2–4, buổi chiều đến tối để ngắm đèn lồng.
```
**Cách dùng:**  
Dán danh sách địa điểm vào vị trí `[Dán danh sách địa điểm ở đây]`.

---

## Prompt 6: Tóm Tắt & Liệt Kê Nhân Vật Sách

**Vai trò:** Biên tập viên sách giàu kinh nghiệm  
**Nhiệm vụ:**
- Tóm tắt ngắn nội dung chính (bối cảnh, xung đột, cao trào, kết thúc nếu có).
- Liệt kê nhân vật, mô tả vai trò/tính cách từng nhân vật.
- Giữ giọng trung lập, không spoil nếu là truyện trinh thám/bất ngờ.

**Định dạng trình bày:**
```
Tóm tắt: …
Nhân vật:
Tên nhân vật: Mô tả ngắn …
Tên nhân vật: Mô tả ngắn …
```
**Ví dụ:**
```
Tóm tắt: “Nhà giả kim” kể về Santiago – một cậu bé chăn cừu Tây Ban Nha, rời quê hương để tìm kiếm kho báu ở Ai Cập...
Nhân vật:
Santiago: Cậu bé chăn cừu, nhân vật chính, kiên trì và đầy mơ mộng.
Nhà giả kim: Người chỉ dẫn giúp Santiago hiểu về “Ngôn ngữ của vũ trụ”.
Fatima: Cô gái sa mạc, tình yêu của Santiago.
```

**Cách dùng:**  
Dán nội dung sách/chương sách vào vị trí `[Dán nội dung sách/chương sách ở đây]`.

---