---
description: Một nhịp kiểm tra day trade sandbox (đề xuất → Hogan duyệt). Dùng với /loop 10m /daytrade
---

Bạn đang chạy phiên DAY TRADE THƯỜNG TRỰC cho sandbox, tài khoản Robinhood 704170133 (cash account). Mỗi lần lệnh này được gọi là 1 nhịp kiểm tra. Toàn bộ trả lời bằng tiếng Việt, ngắn gọn.

## Quy tắc
- Tuân thủ mục `### CHẾ ĐỘ DAY TRADE THỬ NGHIỆM 20 PHIÊN` trong CLAUDE.md (vốn, kích thước, stop −4%, hòa vốn ở +3%, chốt +6%, lỗ ngày $28, bộ lọc, wash sale, đóng hết trước 15:40 ET).
- **Mọi lệnh MUA/BÁN mới cần Hogan duyệt** trong chat ("ok"/"duyệt"/"mua"/"bán"). Ngoại lệ được duyệt sẵn, làm ngay không cần hỏi: đặt stop −4% ngay sau khi lệnh mua khớp, dời stop lên hòa vốn, và đóng hết vị thế lúc ≥15:35 ET.
- **Quy tắc sở hữu:** chỉ vị thế mà `sandbox-log.md` ghi là sandbox mua mới là của sandbox. Core (MSFT, AAPL, TXN, PG, WMT, VOO, VXUS, SCHD, VB, QCOM nếu còn) — không bao giờ đụng tới.

## Khóa 1 phiên duy nhất (bắt buộc, mỗi nhịp)
- Chỉ được có **1 phiên `/daytrade` chạy tại một thời điểm** trên mọi máy. Khóa là file `daytrade.lock` ở gốc repo, nội dung 1 dòng: `<YYYY-MM-DD> <hostname>` (hostname lấy bằng lệnh `hostname`).
- Mỗi nhịp: `git pull --ff-only` rồi đọc `daytrade.lock`:
  - Không có file, hoặc ngày trong file khác hôm nay (giờ ET) → ghi `<hôm nay> <hostname của máy này>`, commit "daytrade lock" + push. Nếu push bị từ chối → pull lại và kiểm tra lại từ đầu.
  - Ngày là hôm nay và hostname TRÙNG máy này → tiếp tục bình thường.
  - Ngày là hôm nay và hostname KHÁC → **DỪNG NGAY**: không đề xuất, không đặt/hủy lệnh nào, báo "Phiên day trade đang chạy trên <hostname khác> — phiên này dừng", rồi kết thúc loop.
- Hogan muốn chuyển máy giữa ngày → nói "chuyển máy": phiên mới ghi đè `daytrade.lock` bằng hostname của nó, phiên cũ sẽ tự dừng ở nhịp kế tiếp.

## Mỗi nhịp
1. Nhịp đầu tiên trong ngày: `git fetch origin main && git checkout -B main origin/main`, đọc CLAUDE.md, ~150 dòng cuối `sandbox-log.md` và `trading-log.md`. Các nhịp sau chỉ cần pull lại nếu có ghi file.
2. Ngoài giờ 9:30–16:00 ET hoặc ngày nghỉ → báo 1 dòng "ngoài giờ giao dịch" và dừng nhịp này.
3. `get_portfolio` (buying_power = tiền ĐÃ settle), `get_equity_positions`, `get_equity_orders` (state=confirmed), `get_equity_quotes` cho SPY, QQQ, vị thế sandbox và watchlist ứng viên.
4. Quản lý vị thế đang mở: chạm +3% → dời stop lên giá vốn (tự làm). Chạm +6% → ĐỀ XUẤT bán. Từ 15:35 ET → hủy stop, bán market toàn bộ (tự làm).
5. Tìm cơ hội (chỉ khi 9:50–14:00 ET, đủ mọi bộ lọc trong CLAUDE.md): tối đa 1–2 ứng viên có lý do rõ trong ngày (tin, volume bất thường, phá vỡ kỹ thuật). Chỉ WebSearch khi thực sự xét vào lệnh, để tiết kiệm.
6. Khi có đề xuất: trình bày theo định dạng CLAUDE.md (mã + mua/bán + số cp, lý do, rủi ro, stop/chốt lời), gọi `review_equity_order` để kèm preview, gửi `PushNotification` 1 dòng, rồi CHỜ Hogan trả lời. Đề xuất hết hạn sau 10 phút hoặc khi giá lệch >1% so với lúc đề xuất → hủy, nói rõ.
7. Sau khi Hogan duyệt: `place_equity_order` (market, regular_hours, cổ phiếu nguyên), xác nhận khớp, đặt stop_market GFD −4%. Ghi `sandbox-log.md` + commit + push ngay.
8. Nhịp không có gì: trả lời 1–2 dòng (SPY/QQQ, vị thế, "không có tín hiệu"), KHÔNG ghi log, KHÔNG push.
9. Nhịp cuối ngày (≥15:40 ET): ghi tổng kết ngày vào `sandbox-log.md` (lệnh, lãi/lỗ ngày, lũy kế từ 11-03, số phiên 1..20), commit + push, rồi dừng loop.
