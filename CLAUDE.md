# Chiến lược đầu tư — Robinhood Agentic Trading

## Nguyên tắc bắt buộc
- CHỈ ĐỀ XUẤT lệnh, KHÔNG tự động đặt lệnh nếu chưa qua preview/duyệt của tôi.
- Mọi đề xuất phải giải thích rõ lý do (phân tích kỹ thuật, tin tức, sentiment, fundamentals).
- Không bao giờ vượt quá tỷ trọng tối đa mỗi vị thế đã quy định bên dưới.
- Nếu không chắc chắn hoặc dữ liệu không đủ, báo tôi thay vì đoán.
- Không tự ý đổi nhóm rủi ro của 1 mã khi thay thế (mã tech kém → thay bằng tech khác, không nhảy sang nhóm rủi ro cao).
- **Hạn chế tối đa các giao dịch làm phát sinh nghĩa vụ thuế không cần thiết (cập nhật 2026-07-07)** — áp dụng cho CẢ 10 mã core lẫn phần sandbox. Ưu tiên giữ vị thế đủ lâu để hưởng thuế suất dài hạn khi hợp lý; tránh mua/bán vòng quay ngắn hạn không có lý do quản trị rủi ro rõ ràng (không exit/entry chỉ để "chốt sổ"); đặc biệt tránh vi phạm wash sale rule — không mua lại đúng mã hoặc mã gần như tương đương trong vòng 30 ngày sau khi bán lỗ. Quy tắc này KHÔNG override kỷ luật cắt lỗ/chốt lời đã đặt (stop-loss vẫn tự động khớp bình thường) — chỉ áp dụng ở những chỗ có phần tự quyết (chọn mã thay thế, thời điểm vào/thoát lệnh không bắt buộc).

## Ngoại lệ đã duyệt: Sandbox tự động rủi ro cao (2026-07-06)
Đây là ngoại lệ DUY NHẤT cho nguyên tắc "chỉ đề xuất, không tự đặt lệnh" ở trên — chỉ áp dụng cho phần vốn sandbox dưới đây, KHÔNG áp dụng cho 10 mã danh mục chính.

- **Phạm vi vốn (cập nhật 2026-07-07):** ~$700 vốn gốc + $700 nạp thêm sau đó để luân phiên 2 "bucket" (một bucket chờ settle, một bucket sẵn sàng giao dịch) — tổng tối đa ~$1400 vốn xoay vòng (tăng từ mốc $400/$800 ban đầu ngày 2026-07-06), tách biệt hoàn toàn khỏi 10 mã core.
- **Quyền tự chủ:** agent tự chọn mã, tự vào/thoát lệnh, KHÔNG cần preview/duyệt trước khi đặt lệnh thật (khác với toàn bộ phần còn lại của tài khoản). Có thể nắm giữ NHIỀU mã cùng lúc trong sandbox (không giới hạn 1 mã/1 lần) — miễn tổng vốn dùng không vượt quá phần vốn sandbox (~$1400) và mỗi vị thế vẫn được log/theo dõi riêng.
- **Chốt lời:** khi tổng giá trị sandbox đạt ~gấp đôi (~$1400 nếu bắt đầu từ $700) → rút phần vốn gốc ($700) về, tiếp tục xoay vòng với phần còn lại.
- **Dừng hẳn:** nếu giá trị sandbox về gần $0 → dừng hoàn toàn, báo tôi, KHÔNG tự nạp thêm vốn.
- **Vẫn bắt buộc:** ghi log mỗi giao dịch vào `sandbox-log.md` (file riêng, KHÔNG chung với `trading-log.md` của 10 mã core); gửi PushNotification sau mỗi lệnh (chỉ để thông báo, không chờ phản hồi); có thể dừng sandbox bất cứ lúc nào chỉ bằng cách yêu cầu "dừng".
- **Tần suất & chi phí (để tiết kiệm token — quyết định 2026-07-06):** kiểm tra sandbox mỗi ~45-60 phút (không phải 25 phút) trong giờ giao dịch. Mỗi lần kiểm tra mặc định chỉ gọi quote/vị thế (rẻ) — CHỈ tìm tin tức/phân tích sâu khi giá biến động đáng kể (>3-5% so với lần kiểm tra trước) hoặc khi cân nhắc vào/thoát lệnh mới.
- **Ràng buộc tài khoản cần lưu ý:** tài khoản Agentic là cash account — xoay vòng tiền bán chưa settle có thể dính "good faith violation" (GFV) nếu không có instant settle; cần tự kiểm tra buying power thực tế sau mỗi lệnh bán trước khi mua tiếp.
- **Hạn chế giao dịch phát sinh thuế (cập nhật 2026-07-07):** dù sandbox được phép giao dịch tự động tần suất cao, vẫn tránh vòng quay ngoài mức cần thiết theo kỷ luật cắt lỗ/chốt lời — không exit/entry lặp lại một mã chỉ vì lý do không liên quan rủi ro. Đặc biệt tránh mua lại đúng mã (hoặc mã gần tương đương) trong vòng 30 ngày sau khi vừa bán lỗ mã đó (wash sale) — như đã áp dụng đúng sau khi WULF bị stop-loss (giữ cash, không mua lại ngay).
- Chi tiết đầy đủ điều khoản: xem memory `sandbox_400_autonomous.md` và `sandbox-log.md`.

## Cơ cấu danh mục (10 mã)
- 2 mã rủi ro cao / tăng trưởng mạnh (high-risk/high-reward, mang tính đầu cơ)
- 4 mã large-cap công nghệ
- 2 mã blue-chip ổn định
- 2 ETF đa dạng hóa

## Tiêu chí chọn mã (agent tự sàng lọc, không dùng danh sách cố định)
- **Nhóm rủi ro cao (2 mã):** small/mid-cap tăng trưởng doanh thu >30%/năm nhưng chưa có lợi nhuận (growth story), HOẶC mã biến động (volatility) cao đang được quỹ mạo hiểm/tổ chức quan tâm gần đây.
- **Nhóm large-cap công nghệ (4 mã):** vốn hóa lớn, thanh khoản cao, có báo cáo tài chính minh bạch.
- **Nhóm blue-chip (2 mã):** công ty ổn định, trả cổ tức đều, biến động thấp.
- **ETF (2 mã):** đa dạng hóa rộng (ví dụ theo chỉ số thị trường chung hoặc theo ngành).

## Quản trị rủi ro
- Cắt lỗ (stop-loss): -5% đến -10% từ giá mua (mặc định -5% cho nhóm rủi ro cao/blue-chip, có thể nới đến -10% cho nhóm biến động mạnh nếu tôi xác nhận)
- Chốt lời (take-profit): +10% đến +20% (tối thiểu tỷ lệ risk/reward 1:2 so với mức cắt lỗ)
- Tỷ trọng tối đa 1 mã: 5-10% tổng danh mục Agentic account
- Số tiền tối đa mỗi lệnh đề xuất: 1-10%
- Tần suất kiểm tra/phân tích: 2-3 lần/ngày (ví dụ 9:45, 13h, 15:30 giờ ET Mỹ) — tránh overtrading
- Loại cổ phiếu (nguyên/fractional): linh hoạt theo từng lệnh, không cố định một kiểu.
  - Ưu tiên mua nguyên cổ phiếu khi cần đặt stop-loss/take-profit tự động (Robinhood không hỗ trợ lệnh stop-loss/limit tự động trên fractional shares, chỉ market order).
  - Có thể dùng fractional khi cần khớp chính xác tỷ trọng/ngân sách đề ra, đặc biệt với cổ phiếu giá cao hoặc tài khoản nhỏ.
  - Nếu đề xuất mua fractional, phải nêu rõ trong đề xuất rằng vị thế đó KHÔNG có stop-loss tự động và cần theo dõi thủ công trong các lần kiểm tra định kỳ cho tới khi đủ nguyên cổ phiếu hoặc thoát vị thế.

## Quy trình review & thay mã định kỳ (mỗi 30 ngày)
- Thời điểm: ngày 1 hàng tháng
- Tiêu chí đánh giá 1 mã "không đạt kỳ vọng" (không chỉ dựa vào % giảm giá đơn thuần, tránh phản ứng thái quá với nhiễu thị trường ngắn hạn):
  - Hiệu suất kém hơn đáng kể so với benchmark cùng nhóm (vd: mã tech so với QQQ, mã rủi ro cao so với nhóm ngành tương ứng) trong 30 ngày
  - Có tin tức tiêu cực nghiêm trọng về công ty (kiện tụng, gian lận kế toán, mất CEO đột ngột, hạ bậc tín nhiệm...)
  - Yếu tố cơ bản (fundamentals) xấu đi rõ rệt, không phải biến động ngắn hạn bình thường
- Khi 1 mã bị đánh giá không đạt: agent ĐỀ XUẤT thay thế bằng mã khác cùng nhóm rủi ro, trình bày rõ lý do và tối thiểu 2 lựa chọn thay thế để tôi chọn/duyệt — KHÔNG tự chọn 1 mã và đặt lệnh luôn.

## Nguồn thông tin agent nên dùng để phân tích
- Tin tức 24h gần nhất liên quan mã theo dõi
- So sánh hiệu suất với benchmark/chỉ số cùng ngành
- Volume giao dịch bất thường
- Chỉ số kỹ thuật cơ bản (RSI, moving average...) nếu có sẵn dữ liệu

## Định dạng đề xuất (mỗi lần gợi ý lệnh)
1. Mã + hành động (mua/bán) + số lượng/số tiền
2. Lý do (ngắn gọn, dẫn nguồn nếu có)
3. Rủi ro chính cần lưu ý
4. Mức cắt lỗ/chốt lời đề xuất cho lệnh này

## Ghi log
Sau mỗi phiên phân tích, lưu tóm tắt vào file `trading-log.md`: ngày giờ, đề xuất, quyết định của tôi (yes/no), lý do nếu từ chối.

---
*Lưu ý: Các con số trong file này (% cắt lỗ, tỷ trọng, ngân sách) là điểm khởi đầu tham khảo, cần điều chỉnh theo khẩu vị rủi ro và mục tiêu tài chính cá nhân. Nên tham khảo CPA/tax advisor về ảnh hưởng thuế (wash sale rule) nếu giao dịch tần suất cao.*
