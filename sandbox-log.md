# Sandbox Log — Giao dịch tự động rủi ro cao

Log riêng cho phần vốn sandbox (~$400–800, tự động, KHÔNG cần duyệt từng lệnh) — tách biệt hoàn toàn khỏi 10 mã danh mục chính trong `trading-log.md`. Điều khoản đầy đủ: xem mục "Ngoại lệ đã duyệt: Sandbox tự động rủi ro cao" trong `CLAUDE.md`.

## 2026-07-06 ~11:48 ET — Bật sandbox $400 tự động (KHÔNG qua duyệt)

**Quyết định của Hogan:** dùng ~$400 buying power còn dư để "day trade" hoàn toàn tự động, không cần duyệt từng lệnh, tối đa rủi ro, chấp nhận mất trắng. Tách biệt hoàn toàn khỏi 10 mã core portfolio. Điều khoản đầy đủ đã lưu vào memory (`sandbox_400_autonomous.md`):
- Gấp đôi (~$800) → rút $400 gốc, tiếp tục trade phần còn lại.
- Về ~$0 → dừng hẳn, báo Hogan, không nạp thêm.
- Vẫn ghi log + push notification (không chờ phản hồi) sau mỗi lệnh.
- Hogan có thể yêu cầu "dừng" bất cứ lúc nào.
- Lưu ý kỹ thuật: cash account bị giới hạn bởi good-faith violation (GFV) nếu xoay vòng tiền chưa settle — Hogan cho biết tài khoản có "instant settle" nên rủi ro này giảm, sẽ xác nhận thực tế qua buying power sau mỗi lệnh bán. Hogan cũng đã nạp thêm $400 để có 2 "bucket" luân phiên (một bucket chờ settle, một bucket sẵn sàng) — khoản nạp mới này cần vài ngày để settle trước khi dùng được.

**Giao dịch #1 — WULF (TeraWulf):**
- Lý do: cả nhóm bitcoin miner chuyển hướng AI/HPC (IREN, WULF, CIFR, HUT) tăng mạnh hôm nay; catalyst cụ thể — Morgan Stanley nâng price target WULF lên $41.50 (giữ Overweight) đúng ngày hôm nay. WULF có relative volume 1.17x (xác nhận dòng tiền thật) tốt hơn CIFR (0.36x, dù CIFR đã chạy 313%/6 tháng — có thể đã phản ánh hết vào giá).
- Mua 17 cp WULF @ $23.7999 (thị giá), tổng ~$404.60. Order id `6a4bce50-9ece-4de8-b524-d2cc1cee2cb9`, state=filled.
- Đặt stop-loss bảo vệ -8% tại $21.90 (tự áp dụng kỷ luật rủi ro cơ bản dù không bắt buộc), order id `6a4bce66-a34c-43f4-9d33-c890e50da8f6`, state=unconfirmed lúc đặt.
- Rủi ro chính: đây là momentum play theo tin tức, có thể đảo chiều nhanh nếu thị trường chốt lời; cổ phiếu miner nhóm này biến động rất cao.
- Việc cần làm tiếp theo: theo dõi giá WULF, quyết định chốt lời/thoát lệnh ở các lần kiểm tra tần suất cao tiếp theo; xác nhận stop-loss đã active.

## 2026-07-06 ~12:18 ET — Check nhẹ

- Stop-loss WULF đã chuyển sang state=`confirmed` (active).
- Giá WULF hiện $23.605 vs vốn $23.7999 (-0.82%) — biến động nhỏ, dưới ngưỡng 3-5% nên không tìm tin tức sâu, giữ nguyên vị thế.
- Bucket $400 nạp thêm: pending_deposits tăng lên $5,500 (từ $5,000), buying power $524.15 — có vẻ một phần đã khả dụng sớm hơn dự kiến (có thể do instant settle), nhưng chưa xác nhận chắc chắn đã settle đầy đủ; sẽ dùng thận trọng, kiểm tra thêm ở lần sau.

## 2026-07-06 ~13:06 ET — Check nhẹ

- Giá WULF hiện $23.345 vs vốn $23.7999 (-1.91%) — vẫn dưới ngưỡng 3-5%, không tìm tin tức sâu, giữ nguyên vị thế.
- Stop-loss @ $21.90 vẫn state=confirmed (active), 17 cp giữ nguyên, không có lệnh mới.
- Không hành động gì thêm lần này.

## 2026-07-06 ~13:24 ET — Check + tìm tin tức (vượt ngưỡng 3-5%)

- Giá WULF hiện $22.9125 vs vốn $23.7999 (-3.73%) — chạm ngưỡng, tìm tin tức sâu.
- Tin tức: TeraWulf vừa công bố hợp đồng thuê 20 năm với Anthropic tại campus Hawesville, Kentucky (~$19 tỷ doanh thu hợp đồng, ~401MW), kèm bán 50.1% cổ phần Abernathy JV cho nhóm do Fluidstack dẫn đầu — catalyst nền tảng rất tích cực. Trước đó cổ phiếu đã giảm ~26%/7 phiên do nhóm AI data-center hạ nhiệt, nên biến động hiện tại nhiều khả năng là chốt lời/nhiễu ngắn hạn sau đợt tăng, không phải đảo chiều thesis. Analyst consensus: Buy (14 analysts), giá mục tiêu ~$28.
- Nguồn: [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/terawulf-shares-surge-anthropic-lease-131745434.html), [CNBC](https://www.cnbc.com/2026/07/06/anthropic-terawulf-data-center-ai.html), [ts2.tech](https://ts2.tech/en/terawulf-heads-into-july-6-after-shares-drop-26-as-ai-data-center-trade-falters/)
- Quyết định: giữ nguyên vị thế 17 cp, không bán, không thêm. Stop-loss $21.90 vẫn confirmed/active, còn cách xa (~-8% từ vốn, giá hiện mới -3.73%).

## 2026-07-06 ~14:07 ET — Check nhẹ

- Giá WULF hiện $22.72 vs vốn $23.80 (-4.54%). So với lần check trước ($22.9125), biến động chỉ -0.84% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $21.90 vẫn state=confirmed (active), 17 cp giữ nguyên. Giá trị vị thế hiện ~$386.24 — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker.
- Buying power $524.15 (không đổi so với lần trước), pending_deposits $5,500 vẫn chờ settle.
- Không hành động gì thêm lần này.
