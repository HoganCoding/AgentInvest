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
- **Lưu ý quan trọng (2026-07-10):** đây là phân bổ vốn theo dõi trên GIẤY (mental accounting), KHÔNG phải sub-account vật lý tách biệt — `buying_power` là một pool DÙNG CHUNG giữa core-10 và sandbox trên cùng tài khoản Robinhood. Khi core-10 đặt lệnh mua (vd. thay mã sau stop-loss), `buying_power` giảm ngay và có thể tụt xuống DƯỚI mức $700 đệm đang theo dõi cho sandbox — đây không phải lỗi, chỉ cần kiểm tra `buying_power` thực tế mỗi lần trước khi tính "phần theo dõi" hoặc trước khi đặt lệnh sandbox mới, không giả định đệm luôn sẵn $700.
- **Quyền tự chủ:** agent tự chọn mã, tự vào/thoát lệnh, KHÔNG cần preview/duyệt trước khi đặt lệnh thật (khác với toàn bộ phần còn lại của tài khoản). Có thể nắm giữ NHIỀU mã cùng lúc trong sandbox (không giới hạn 1 mã/1 lần) — miễn tổng vốn dùng không vượt quá phần vốn sandbox (~$1400) và mỗi vị thế vẫn được log/theo dõi riêng.
- **Chốt lời (làm rõ công thức 2026-07-09 — QUAN TRỌNG, tránh nhầm như trước):** ngưỡng gấp đôi ($1400) áp dụng cho **phần đang xoay vòng/đầu tư ($700 gốc)**, KHÔNG tính luôn $700 bucket đệm (buffer chờ settle). Cách tính: lấy tổng cash + giá trị vị thế hiện có, TRỪ ra $700 giữ làm đệm → phần còn lại (cash rảnh ngoài đệm + giá trị vị thế) là "phần theo dõi", bắt đầu từ ~$700, chốt lời khi phần này đạt ~$1400 → bán bớt, rút $700 lời về, phần đệm lúc đó thành ~$1400, tiếp tục xoay vòng $700 còn lại. KHÔNG cộng thẳng buffer $700 vào tổng để so với $1400 (lỗi đã mắc phải 2026-07-08/09, làm tưởng gần chốt lời khi thực ra còn xa).
- **Đệm $700 không cứng nhắc (làm rõ 2026-07-09):** có thể lấy TỐI ĐA 30% phần đệm (~$210) khi cần để làm tròn đủ mua nguyên cổ phiếu (vd. thiếu vài đô để đủ 1 share nguyên, cần cho stop-loss tự động) — không cần giữ tuyệt đối $700. Khi dùng tới đệm, ghi rõ trong log số tiền đã lấy từ đệm để theo dõi, và ưu tiên bù lại đệm khi có cash mới settle/xoay vòng.
- **Công thức cân bằng Đầu Tư = Đệm (quy định 2026-07-09):** về nguyên tắc, phần Đầu Tư (đang xoay vòng, hiện $700) và phần Đệm (buffer chờ settle, hiện $700) nên bằng nhau. Khi Đầu Tư đạt ngưỡng gấp đôi (x2, vd. $700→$1400) → chuyển 1x mức gốc ($700) sang Đệm (Đệm_mới = Đệm_cũ + Đầu Tư×1), phần còn lại tiếp tục làm Đầu Tư ở mức 1x gốc ($700) — đây chính là cách thực hiện "Chốt lời" ở trên. Công thức này cũng áp dụng khi tăng vốn: nếu đề xuất tăng Đầu Tư, phải đề xuất kèm số tiền nạp thêm vào Đệm tương ứng để giữ Đầu Tư = Đệm.
- **Đề xuất tăng vốn / dùng thêm đệm khi có cơ hội tốt (làm rõ 2026-07-09):** nếu thấy cơ hội tốt nhưng vốn khả dụng (cash rảnh + tối đa 30% đệm) không đủ, agent CÓ THỂ CHỦ ĐỘNG ĐỀ XUẤT với Hogan: (a) nạp thêm vốn vào sandbox, hoặc (b) dùng thêm phần đệm vượt mức 30% thông thường. Khi đề xuất (a), TÍNH LUÔN số tiền nạp thêm cần thiết để giữ đúng công thức Đầu Tư = Đệm ở trên (không chỉ đủ cho riêng phần Đầu Tư). Đây là ĐỀ XUẤT cần Hogan duyệt trước (khác với giao dịch bình thường trong ngân sách hiện có, vẫn tự động không cần duyệt) — vì việc này mở rộng ngân sách sandbox đã thống nhất, không phải quyết định trong phạm vi tự chủ sẵn có. Gửi PushNotification khi có đề xuất loại này. **Sau khi được duyệt (làm rõ 2026-07-09):** KHÔNG gửi thêm push cho các bước tiếp theo của cùng cơ hội đó (nạp tiền đã settle, đặt lệnh mua thực hiện, v.v.) — chỉ ghi log. Chỉ gửi push trở lại khi có cơ hội MỚI khác cần đề xuất/xác nhận.
- **Dừng hẳn (làm rõ công thức 2026-07-09, đồng bộ với "Chốt lời" ở trên):** nếu **phần đang xoay vòng $700 gốc** (KHÔNG tính $700 đệm) về gần $0 → dừng hoàn toàn, báo tôi, KHÔNG tự nạp thêm vốn. Cùng công thức "phần theo dõi" dùng cho chốt lời — không cộng đệm vào để tính ngưỡng này.
- **Vẫn bắt buộc:** ghi log mỗi giao dịch vào `sandbox-log.md` (file riêng, KHÔNG chung với `trading-log.md` của 10 mã core); có thể dừng sandbox bất cứ lúc nào chỉ bằng cách yêu cầu "dừng".
- **PushNotification (làm rõ 2026-07-08):** CHỈ gửi khi có thay đổi thật — vào lệnh, thoát lệnh, stop-loss/circuit breaker kích hoạt (gấp đôi vốn hoặc về gần $0), hoặc bất cứ điều gì cần Hogan biết/xác nhận. KHÔNG gửi push cho các lần kiểm tra định kỳ không có hành động gì (vẫn giữ nguyên cash/vị thế) — những lần đó chỉ cần ghi log, không cần thông báo.
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
- **Cắt lỗ (stop-loss) — trailing theo đỉnh giá (cập nhật 2026-07-24):** tính theo % lùi từ **giá cao nhất đã đạt được kể từ khi mua** (không phải cố định từ giá mua ban đầu nữa) — mặc định -5% cho nhóm tech/blue-chip, **-12% cho nhóm rủi ro cao/biến động mạnh** (nới từ -8%/-10% cũ, xem lý do bên dưới). Stop-loss CHỈ được dời LÊN theo đỉnh giá mới, KHÔNG BAO GIỜ dời xuống. Cập nhật mỗi lần kiểm tra định kỳ nếu giá đã tạo đỉnh mới kể từ lần cập nhật gần nhất — với core-10 cần đề xuất/thực hiện qua phiên có quyền đặt lệnh như bình thường, với sandbox agent tự cập nhật theo quyền tự chủ đã có. Khi dời stop-loss, phải hủy lệnh stop-loss cũ trước rồi mới đặt lệnh mới (không thể sửa trực tiếp), lưu ý cổ phiếu có thể đang bị giữ bởi lệnh cũ (`shares_held_for_sells`) nên cần hủy trước khi bán/đổi.
  - **Vì sao nới lên -12% (2026-07-24):** review `get_pnl_trade_history` cho thấy realized P&L tổng -$254.94 (15 lệnh đã đóng: 4 thắng/+$91.79, 11 thua/-$346.73 — win rate 26.7%, lỗ trung bình/lệnh > lãi trung bình/lệnh). Phần lớn lệnh thua đến từ nhóm rủi ro cao (IONQ, QBTS, RXRX, SOUN, SERV, HIMS, WULF, HUT) — các mã này dao động tự nhiên 5-10%+/ngày, nên stop -8% cũ gần như trùng biên độ nhiễu bình thường, bị quẹt trước khi biết xu hướng thật. Nới stop lên -12% để giảm tỷ lệ bị quẹt bởi nhiễu ngắn hạn.
- **Tỷ trọng nhóm rủi ro cao: giảm xuống ~5% danh mục/mã (cập nhật 2026-07-24)** thay vì 7-10% như các nhóm khác — để giữ rủi ro tính bằng $ mỗi lệnh gần như không đổi so với trước khi nới stop (-8%×7.5% ≈ -12%×5% ≈ 0.6% danh mục/lệnh). Các nhóm còn lại (tech/blue-chip/ETF) vẫn theo tỷ trọng 5-10% như cũ.
- **Chốt lời (take-profit) — cập nhật 2026-07-24, khác nhau theo nhóm:**
  - **Nhóm rủi ro cao:** +15% lãi tích lũy từ giá vốn là ngưỡng BÁN MẶC ĐỊNH 50% vị thế (chốt lời chủ động một phần, không chỉ cảnh báo) — theo đúng cách đã hiệu quả với AEHR (2 đợt bán +23.1%/+14.47%, lệnh thắng đậm nhất trong lịch sử tài khoản). Phần còn lại (50%) tiếp tục chạy theo trailing stop-loss như bình thường. Core-10 vẫn cần tôi duyệt trước khi bán; sandbox agent tự quyết theo quyền tự chủ đã có.
  - **Nhóm tech/blue-chip/ETF:** giữ nguyên như cũ — +15% đến +20% là ngưỡng CẢNH BÁO, không tự động bán, agent đề xuất cân nhắc chốt lời một phần/toàn bộ khi chạm ngưỡng.
- **Bộ lọc trước khi vào lệnh mới — chỉ áp dụng nhóm rủi ro cao (mới, 2026-07-24):**
  - Cần xác nhận giá đã ổn định/có volume xác nhận thật (ít nhất 1 phiên) trước khi mua — KHÔNG mua ngay giữa lúc chính mã đó hoặc cả nhóm ngành đang giảm mạnh trong phiên (tránh lặp lại tình huống QBTS mua giữa lúc nhóm quantum -8.7%/ngày).
  - KHÔNG mở vị thế rủi ro cao mới vào ngày benchmark liên quan (SPY/QQQ hoặc ETF ngành tương ứng) đang giảm >1.5-2% trong phiên — tránh lặp lại tình huống HIMS (mua đúng lúc thị trường bắt đầu bán tháo vì lo AI-capex, bị quẹt trong chưa đầy 1 giờ).
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
