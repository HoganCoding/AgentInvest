---
description: Phiên day trade — agent tìm cơ hội có lời và giao dịch. Dùng với /loop 10m /daytrade
---

Bạn đang chạy phiên DAY TRADE cho tài khoản Robinhood 704170133 (cash account). Toàn bộ trả lời bằng tiếng Việt, ngắn gọn.

## Nguyên tắc
- Mục tiêu đơn giản: **thấy cơ hội có lời thì làm**. Agent tự quyết mã, kích thước, stop-loss, thời gian nắm giữ (có thể qua đêm).
- Vốn ~$1,000 (toàn bộ `buying_power` đã settle ngoài core-9). Chỉ mua cổ phiếu NGUYÊN.
- **Vài phiên đầu:** trình bày đề xuất → chờ Hogan duyệt ("ok"/"duyệt"). Khi Hogan bật tự động → tự đặt lệnh luôn.
- Core-9 (MSFT, AAPL, TXN, PG, WMT, VOO, VXUS, SCHD, VB) — **không bao giờ đụng tới**.

## Khóa 1 phiên duy nhất (bắt buộc, mỗi nhịp)
- Mỗi nhịp: `git pull --ff-only` rồi đọc `daytrade.lock`:
  - Không có file, hoặc ngày trong file khác hôm nay (giờ ET) → ghi `<hôm nay> <hostname>`, commit + push.
  - Ngày hôm nay, hostname TRÙNG → tiếp tục bình thường.
  - Ngày hôm nay, hostname KHÁC → **DỪNG NGAY**, báo "Phiên đang chạy trên `<hostname khác>`".
- Chuyển máy giữa ngày → nói "chuyển máy": phiên mới ghi đè lock, phiên cũ tự dừng.

## Mỗi nhịp
1. Nhịp đầu ngày: `git pull`, đọc ~100 dòng cuối `sandbox-log.md`.
2. Ngoài giờ 9:30–16:00 ET hoặc ngày nghỉ → báo 1 dòng và dừng nhịp.
3. `get_portfolio` (buying_power), `get_equity_positions`, `get_equity_quotes` cho vị thế đang có + SPY/QQQ + ứng viên đang xét.
4. Quản lý vị thế đang mở theo phán đoán (dời stop, chốt lời một phần, v.v.).
5. Tìm cơ hội mới: tin tức, momentum, volume bất thường, phá vỡ kỹ thuật — WebSearch khi cần.
6. Khi có đề xuất (vài phiên đầu): trình bày mã + hành động + lý do + stop/chốt lời, gọi `review_equity_order`, gửi `PushNotification` 1 dòng, **chờ Hogan duyệt**. Đề xuất hết hạn sau 10 phút hoặc giá lệch >1%.
7. Sau khi duyệt (hoặc tự động): `place_equity_order`, xác nhận khớp, đặt stop nếu cần. Ghi `sandbox-log.md` + commit + push ngay.
8. Nhịp không có gì: 1–2 dòng (SPY/QQQ, vị thế, tín hiệu), **không ghi log, không push**.
