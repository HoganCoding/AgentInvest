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

## 2026-07-06 ~13:57 ET — Check nhẹ

- Giá WULF hiện $22.52 vs vốn $23.7999 (-5.38%). So với lần check trước ($22.9125) chỉ giảm thêm -1.71% — dưới ngưỡng 3-5%, không tìm tin tức mới, giữ nguyên vị thế.
- Stop-loss $21.90 vẫn confirmed/active (còn cách ~2.7% nữa mới chạm), 17 cp giữ nguyên, không có lệnh mới.

## 2026-07-06 ~14:02 ET — Check nhẹ

- Giá WULF hồi nhẹ lên $22.865 vs vốn $23.7999 (-3.93%), so với lần check trước ($22.52) tăng lại +1.53% — biến động trong biên độ đã phân tích ở 13:24 ET (chốt lời/nhiễu ngắn hạn sau tin Anthropic, thesis không đổi), không cần tìm tin tức lại.
- Giữ nguyên 17 cp, không bán, không thêm. Stop-loss $21.90 confirmed/active.
- Bucket $400/$500 thứ 2: buying power vẫn $524.15, pending_deposits vẫn $5,500 — chưa settle thêm.

## 2026-07-06 ~14:07 ET — Check nhẹ (cloud routine, lần chạy thử tự động đầu tiên)

- Giá WULF hiện $22.72 vs vốn $23.80 (-4.54%). So với lần check trước ($22.9125), biến động chỉ -0.84% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $21.90 vẫn state=confirmed (active), 17 cp giữ nguyên. Giá trị vị thế hiện ~$386.24 — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker.
- Buying power $524.15 (không đổi so với lần trước), pending_deposits $5,500 vẫn chờ settle.
- Không hành động gì thêm lần này.

## 2026-07-06 ~15:08 ET — Check nhẹ (cloud routine)

- Giá WULF hiện $22.77 vs vốn $23.80 (-4.33%). So với lần check trước ($22.72), biến động chỉ +0.22% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $21.90 vẫn state=confirmed (active), order id `6a4bce66-a34c-43f4-9d33-c890e50da8f6`, 17 cp giữ nguyên. Giá trị vị thế hiện ~$387.09 — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker.
- Không hành động gì thêm lần này.

## 2026-07-07 ~09:30 ET — Stop-loss WULF khớp lúc mở cửa (giao dịch #1 đóng)

- Cổ phiếu WULF gap-down mạnh khi mở cửa phiên thứ Ba: giá mở dưới mức stop $21.90. Lệnh stop-loss (order id `6a4bce66-a34c-43f4-9d33-c890e50da8f6`) kích hoạt thành market order và khớp toàn bộ 17 cp @ **$21.55** trung bình lúc 13:30:00 UTC (~9:30 ET) — trượt giá (~-1.6% so với mức stop $21.90) do gap qua đêm, không phải lỗi hệ thống.
- **Kết quả giao dịch #1 (WULF):** mua 17 cp @ $23.7999 ($404.60) → bán 17 cp @ $21.55 ($366.35) → **lỗ hiện thực -$38.25 (-9.45%)**.
- Quote WULF lúc phát hiện (kiểm tra ~10:0x ET, giờ đã sang chiều khi log này được ghi lại): $20.42 (so với previous close $22.21, giảm thêm -8.06%) — giá tiếp tục giảm sau khi stop khớp, xác nhận thoát lệnh kịp thời là quyết định đúng, tránh lỗ sâu hơn.
- Vị thế sandbox hiện tại: **0 cổ phiếu WULF, toàn bộ về cash.** Portfolio tổng tài khoản (bao gồm cả 10 mã core, không tách riêng được vì chung 1 account): total_value $5,984.62, cash $1,390.50, buying_power $1,024.15, pending_deposits $5,000 (bucket 2 vẫn chờ settle).
- Chưa chọn lệnh mới — sẽ phân tích cơ hội tiếp theo ở lần check kế tiếp theo đúng chu kỳ 45-60 phút. Không có áp lực circuit breaker (vốn chưa gần $0 hay gấp đôi $800).
