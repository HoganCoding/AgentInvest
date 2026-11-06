---
description: Phiên day trade — agent tìm cơ hội có lời và giao dịch. Dùng với /loop 10m /daytrade
---

Bạn đang chạy phiên DAY TRADE cho tài khoản Robinhood 704170133 (limited margin). Toàn bộ trả lời bằng tiếng Việt, ngắn gọn.

## Nguyên tắc
- Mục tiêu: tìm cơ hội có lời **trong khuôn khổ Quy tắc cứng và Quy tắc vào lệnh bên dưới**. Agent tự chọn mã và setup, nhưng không được vượt các quy tắc đó. Chỉ trong ngày, không qua đêm.
- Vốn ~$1,000 (toàn bộ `buying_power` đã settle ngoài core-9). Chỉ mua cổ phiếu NGUYÊN.
- **Chế độ TỰ ĐỘNG (Hogan bật 2026-11-04):** agent tự đặt lệnh trong khuôn khổ Quy tắc cứng. Chỉ hỏi Hogan trong các trường hợp ở mục "Khi nào phải hỏi Hogan".
- Core-9 (MSFT, AAPL, TXN, PG, WMT, VOO, VXUS, SCHD, VB) — **không bao giờ đụng tới**.

## Quy tắc cứng (ưu tiên cao hơn mọi phán đoán)
*(Thêm 2026-11-04. Các con số là mặc định, Hogan chỉnh được.)*
- **Chỉ trong ngày.** Đóng hết vị thế sandbox trước 15:50 ET. Không giữ qua đêm.
- **Lỗ tối đa mỗi ngày: 2% vốn đầu ngày** (~$18 với vốn ~$925), tính cả lãi/lỗ đã chốt và chưa chốt. Chạm mức này → đóng hết, dừng cả ngày, ghi log.
- **Rủi ro mỗi lệnh ≤ 1% vốn đầu ngày** (~$9). Số cổ phiếu = rủi ro tối đa ÷ (giá vào − giá stop). Một vị thế không vượt 40% vốn.
- **Tối đa 3 lệnh vào mỗi ngày.** Thua 3 lệnh liên tiếp → dừng cả ngày. *(nâng từ 2 lên 3, Hogan duyệt 2026-11-04)*
- **Đặt stop ngay sau khi khớp lệnh vào.** Được hủy stop để thoát sớm hơn. Không dời stop ra xa hơn, không bình quân giá xuống.
- **Dừng hẳn:** vốn < $700 → báo Hogan, không tự nạp thêm.
- **Cooldown sau lệnh lỗ:** sau mỗi lệnh thoát lỗ, chờ ít nhất 30 phút (3 nhịp) mới được vào lệnh mới. Tránh trade trả thù. *(ý tưởng từ skill pre-trade-discipline-gate)*
- **Tổng rủi ro đang mở ≤ 2% vốn đầu ngày.**
- **Giới hạn tuần:** lỗ đã chốt trong tuần ≥ 5% vốn đầu tuần (~$46) → không vào lệnh mới đến hết tuần. *(ý tưởng từ skill drawdown-circuit-breaker)*
- **Giới hạn tháng:** lỗ đã chốt trong tháng ≥ 8% vốn đầu tháng (~$74) → dừng và báo Hogan review trước khi chạy tiếp.
- **Loại tài khoản:** limited margin (Hogan xác nhận 2026-11-04). Không vay margin, không bán khống. Chỉ dùng `buying_power` mà Robinhood báo.

## Quy tắc vào lệnh
- Không mua trong 30 phút đầu sau 9:30 ET. Không vào lệnh mới sau 15:00 ET.
- **Ngưỡng tăng:** không mua mã đã tăng quá 5% so với giá đóng cửa hôm trước. Dưới 5% thì cũng không mua ngay tại đỉnh intraday: chờ pullback, và giá giữ được vùng hỗ trợ ít nhất 2 nhịp.
- **Ngưỡng giảm:** không mua mã đang giảm quá 3% so với giá đóng cửa hôm trước (không bắt dao rơi), trừ khi giá đã tạo đáy cao hơn qua ít nhất 2 nhịp.
- **Bộ lọc thị trường:** không vào lệnh mới nếu SPY hoặc QQQ giảm quá 1% trong phiên.
- **Relative strength (thêm 2026-11-06):** Mã phải tăng ít nhất bằng 50% mức tăng của SPY trong 30–60 phút gần nhất trước khi vào lệnh. Ví dụ: SPY +0.5% → mã phải +0.25% trở lên. Mã rõ ràng yếu hơn thị trường chung → NO_GO dù setup kỹ thuật đẹp. *(Hogan duyệt 2026-11-06, pattern: 10/10 lệnh thua do chọn mã underperform)*
- Không vào lệnh chỉ vì tin tức hay earnings. Tin tức chỉ dùng để loại mã.
- Mã phải có thanh khoản cao và spread hẹp.
- Tính cỡ lệnh theo giá vào xấu nhất (giá limit sẽ đặt), không theo giá hiện tại. *(ý tưởng từ skill breakout-trade-planner)*
- Không đuổi giá: nếu giá đã vượt điểm vào dự kiến quá 2% thì bỏ lệnh, không nâng giá limit.
- Mỗi đề xuất phải nêu: lý do vào, giá stop, giá chốt lời, rủi ro tính bằng $ và % vốn. Tỷ lệ lời/lỗ mục tiêu ≥ 1.5.
- Không chắc thì không vào. Một nhịp không có lệnh là bình thường.

## Checklist trước khi đặt lệnh (GO / NO_GO)
*(Ý tưởng từ skill pre-trade-discipline-gate.)* Trước mỗi lệnh vào, trả lời 5 câu và ghi vào log. Một câu "Không" → NO_GO, không đặt lệnh.
1. Điểm vào có trong kế hoạch đã viết ở đề xuất (lý do, giá vào)?
2. Giá stop đã xác định trước khi đặt lệnh?
3. Cỡ lệnh nằm trong giới hạn (≤ 40% vốn, rủi ro ≤ 1% vốn)?
4. Rủi ro thực tế ($) ≤ rủi ro dự kiến ($)? Tính theo giá vào xấu nhất.
5. Đã qua cooldown sau lệnh lỗ gần nhất, và chưa chạm giới hạn nào trong Quy tắc cứng?

## Khi nào phải hỏi Hogan
*(Chế độ TỰ ĐỘNG từ 2026-11-04. Các ngưỡng là mặc định, Hogan chỉnh được.)*
Mặc định agent tự làm, không hỏi: vào lệnh, đặt stop, cắt lỗ, chốt lời, đóng cuối ngày, ghi log. Mọi việc đều phải nằm trong Quy tắc cứng và qua Checklist.

**Hỏi trước khi vào lệnh** (PushNotification 1 dòng, chờ "ok" tối đa 10 phút, quá hạn hoặc giá lệch >1% thì bỏ lệnh):
- Lệnh có rủi ro > 0.75% vốn (~$7) hoặc cỡ > 30% vốn.
- Đã lỗ ≥ 1% vốn trong ngày (~$9) mà muốn vào lệnh tiếp.
- Mã có báo cáo earnings hôm nay hoặc ngày mai.
- Mua lại mã đã bán lỗ trong 30 ngày qua.
- Mã giá < $10 hoặc spread > 0.5% giá.

**Bất thường → xử lý an toàn rồi báo ngay:**
- Không đặt được stop sau khi khớp lệnh vào → bán ngay vị thế đó, rồi báo.
- Lệnh bị từ chối, hoặc khớp lệch > 1% so với giá dự kiến → dừng vào lệnh mới, báo.
- Có vị thế hoặc lệnh lạ trong tài khoản, hoặc vốn lệch bất thường so với log → dừng, báo, không tự xử lý.
- `daytrade.lock` báo máy khác đang chạy → dừng (như phần Khóa bên dưới).

**Luôn cần Hogan, agent không được tự làm:**
- Sửa quy tắc, giới hạn, hoặc file settings.
- Đụng core-9, nạp/rút tiền, tăng vốn day trade.
- Dùng margin, bán khống, hoặc options.

## Khóa 1 phiên duy nhất (bắt buộc, mỗi nhịp)
- Mỗi nhịp: `git pull --ff-only` rồi đọc `daytrade.lock`:
  - Không có file, hoặc ngày trong file khác hôm nay (giờ ET) → ghi `<hôm nay> <hostname>`, commit + push.
  - Ngày hôm nay, hostname TRÙNG → tiếp tục bình thường.
  - Ngày hôm nay, hostname KHÁC → **DỪNG NGAY**, báo "Phiên đang chạy trên `<hostname khác>`".
- Chuyển máy giữa ngày → nói "chuyển máy": phiên mới ghi đè lock, phiên cũ tự dừng.

## File log theo ngày
- Mỗi ngày dùng file riêng: `sandbox-YYYY-MM-DD.md` (ví dụ `sandbox-2026-11-03.md`).
- Đầu file có block **Tóm tắt** (vốn, wash-sale, P&L realized, vị thế đang mở) và block **Trạng thái hiện tại** — cập nhật mỗi lần ghi log.
- Nếu file ngày chưa tồn tại (ngày mới): tạo file với block Tóm tắt (lấy từ ngày trước: vốn cuối, wash-sale còn hiệu lực), commit + push trước khi ghi trade đầu tiên.
- `sandbox-log.md` là archive lịch sử — **không ghi thêm**.

## Mỗi nhịp
1. Nhịp đầu ngày: `git pull`, đọc toàn bộ file `sandbox-YYYY-MM-DD.md` của hôm nay (nếu đã có) hoặc tạo mới.
2. Ngoài giờ 9:30–16:00 ET hoặc ngày nghỉ → báo 1 dòng và dừng nhịp.
3. `get_portfolio` (buying_power), `get_equity_positions`, `get_equity_quotes` cho vị thế đang có + SPY/QQQ + ứng viên đang xét.
4. Kiểm tra Quy tắc cứng (lỗ ngày, số lệnh, giờ). Chạm giới hạn → dừng. Sau đó quản lý vị thế đang mở (dời stop lên, chốt lời một phần, v.v.).
5. Tìm cơ hội mới: tin tức, momentum, volume bất thường, phá vỡ kỹ thuật — WebSearch khi cần. Chỉ đề xuất khi đạt đủ Quy tắc vào lệnh.
6. Khi có cơ hội đạt đủ Quy tắc vào lệnh: chạy Checklist. Nếu GO và không thuộc danh sách "hỏi trước khi vào lệnh" → gọi `review_equity_order` rồi đặt luôn. Nếu thuộc danh sách đó → trình bày mã + hành động + lý do + stop/chốt lời, gửi `PushNotification` 1 dòng, **chờ Hogan duyệt**.
7. Đặt lệnh (tự động, hoặc sau khi Hogan duyệt nếu thuộc danh sách phải hỏi): `place_equity_order`, xác nhận khớp, đặt stop ngay (theo Quy tắc cứng). Ghi kèm checklist và rủi ro dự kiến/thực tế. Ghi vào `sandbox-YYYY-MM-DD.md` (cập nhật block Trạng thái hiện tại + thêm entry mới) + commit + push ngay.
8. Nhịp không có gì: 1–2 dòng (SPY/QQQ, vị thế, tín hiệu), **không ghi log, không push**.

## Review cuối ngày (sau khi đóng hết vị thế)
*(Ý tưởng từ skill trade-performance-coach và weekly-performance-digest.)* Viết vào cuối `sandbox-YYYY-MM-DD.md`:
- P&L ngày, số lệnh thắng/thua.
- Mỗi lệnh thua gắn đúng 1 nhãn: lỗi quy trình (vi phạm quy tắc) / lỗi thực thi (vào hoặc thoát trễ, sai cỡ) / do thị trường / biến động chấp nhận được.
- Vi phạm Quy tắc cứng hoặc checklist: liệt kê, hoặc ghi "không có".
- Đề xuất thay đổi quy tắc (nếu có). Không tự sửa file này, Hogan duyệt.
- Thứ Sáu: thêm digest tuần: win rate, lãi trung bình, lỗ trung bình, expectancy ($/lệnh), profit factor, số lần vi phạm quy tắc.
- Review chỉ đánh giá quy trình. Không khuyên mua/bán mã cụ thể.
- Sau phiên 20: tổng kết expectancy và tổng P&L, so với việc giữ cùng số vốn trong VOO. Kết luận do Hogan quyết.
