# Sandbox Log — Giao dịch tự động rủi ro cao

Log riêng cho phần vốn sandbox (~$700–1400, tự động, KHÔNG cần duyệt từng lệnh) — tách biệt hoàn toàn khỏi 10 mã danh mục chính trong `trading-log.md`. Điều khoản đầy đủ: xem mục "Ngoại lệ đã duyệt: Sandbox tự động rủi ro cao" trong `CLAUDE.md`.

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

## 2026-07-06 ~14:54 ET — Check nhẹ, giá tiến gần stop-loss

- Giá WULF $22.125 vs vốn $23.7999 (-7.03%). So với lần check trước, giảm thêm nhưng biến động từng bước vẫn <3-5% nên không tìm tin tức mới (thesis từ 13:24 ET vẫn là cơ sở: Anthropic deal tích cực, đây là chốt lời/nhiễu ngắn hạn).
- **Chỉ còn ~1% (~$0.225) nữa là chạm stop-loss $21.90.** Không can thiệp sớm — để stop-loss tự động xử lý nếu chạm, đúng theo kỷ luật đã đặt ra. Không bán non trước hạn.
- Portfolio tổng: total_value $5,514.53, buying power $524.15 (không đổi), pending_deposits $5,500 (bucket 2 vẫn chưa settle thêm).
- Vì đang gần điểm quyết định, rút ngắn chu kỳ check tiếp theo xuống ~20 phút thay vì 45-60 phút để theo dõi sát hơn.

## 2026-07-06 ~15:16 ET — Check nhẹ, vẫn gần stop-loss

- Giá WULF $22.0701 vs vốn $23.7999 (-7.27%), cách stop-loss $21.90 chỉ ~0.77%. So với lần check trước ($22.125), biến động -0.25% — dưới ngưỡng, không tìm tin tức mới.
- Stop-loss vẫn `confirmed`, chưa khớp (cumulative_quantity=0). Không can thiệp, giữ nguyên kỷ luật để stop-loss tự xử lý.
- Vẫn duy trì chu kỳ check ~20 phút cho tới khi giá tách xa stop-loss hơn hoặc stop-loss khớp.

## 2026-07-06 ~15:37 ET — Check nhẹ, hồi nhẹ

- Giá WULF $22.265 vs vốn $23.7999 (-6.44%), cách stop-loss $21.90 ~1.64% (tách xa hơn lần trước 0.77%). Biến động +0.88% so với lần check trước — dưới ngưỡng, không tìm tin tức mới.
- Stop-loss vẫn `confirmed`, chưa khớp. Không hành động gì thêm.
- Thị trường đóng cửa trong ~23 phút (16:00 ET) — sẽ check lần cuối phiên rồi chuyển sang lên lịch qua đêm.

## 2026-07-06 ~16:00 ET — Đóng cửa phiên, chuyển qua đêm

- Giá đóng cửa (regular hours) $22.195 vs vốn $23.7999 (-6.75%). Stop-loss $21.90 KHÔNG bị khớp trong phiên — vẫn giữ nguyên 17 cp WULF qua đêm, `confirmed`/active.
- Kết quả trong ngày: mua ở $23.80 sáng nay theo tin Anthropic $19B, giá dao động -0.8% đến -7.3% trong phiên nhưng không chạm stop -8% ($21.90), đóng cửa ở -6.75%. Chưa hiện thực hóa lãi/lỗ (chưa bán).
- Chuyển sang chế độ qua đêm: không check liên tục, chờ tới phiên giao dịch kế tiếp (~9:45 ET thứ Ba 2026-07-07) để tiếp tục theo dõi.

## 2026-07-06 ~16:08 ET — Check nhẹ (cloud routine)

- Giá WULF hiện $22.13 vs vốn $23.80 (-7.02%). So với lần check trước ($22.77), biến động -2.81% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Đáng chú ý: giá hiện chỉ còn cách stop-loss $21.90 khoảng ~1% (rất gần). Đã xác nhận qua get_equity_orders: lệnh stop-loss (`6a4bce66-a34c-43f4-9d33-c890e50da8f6`) vẫn state=`confirmed`/active, stop_price=$21.90, gtc — sẽ tự kích hoạt nếu giá chạm mức này, không cần can thiệp thủ công.
- Giá trị vị thế hiện ~$376.21 (17 cp × $22.13) — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker khác.
- Buying power $524.15 (không đổi), pending_deposits $5,500 vẫn chờ settle.
- Không hành động gì thêm lần này; theo dõi sát hơn ở lần check tiếp theo do đã gần stop-loss.

## 2026-07-06 ~17:08 ET — Check nhẹ (cloud routine)

- Giá WULF hiện $22.195 vs vốn $23.80 (-6.75%). So với lần check trước ($22.13), biến động chỉ +0.29% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $21.90 vẫn state=`confirmed`/active, order id `6a4bce66-a34c-43f4-9d33-c890e50da8f6`, stop_price=$21.90, gtc, 17 cp giữ nguyên. Giá hiện chỉ còn cách stop-loss ~1.33% — vẫn khá gần, tiếp tục theo dõi sát.
- Giá trị vị thế hiện ~$377.32 (17 cp × $22.195) — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker.
- Không hành động gì thêm lần này.

## 2026-07-07 ~09:08 ET — Check nhẹ (cloud routine, mở phiên mới)

- Giá WULF hiện $21.9225 (pre-market) vs vốn $23.80 (-7.89%). So với lần check trước ($22.195 lúc 17:08 ET hôm qua), biến động chỉ -1.23% — dưới ngưỡng 3-5%, không tìm tin tức sâu. Previous close (2026-07-06) = $22.21.
- Đáng chú ý: giá hiện chỉ còn cách stop-loss $21.90 khoảng ~0.1% (rất sát). Đã xác nhận qua get_equity_orders: lệnh stop-loss (`6a4bce66-a34c-43f4-9d33-c890e50da8f6`) vẫn state=`confirmed`/active, stop_price=$21.90, gtc, market_hours=regular_hours — hiện đang pre-market nên chưa thể kích hoạt; sẽ tự kích hoạt khi phiên chính thức mở nếu giá vẫn ở dưới/gần mức này.
- Giá trị vị thế hiện ~$372.68 (17 cp × $21.9225) — chưa gần ngưỡng gấp đôi ($800) hay về $0, không kích hoạt circuit breaker khác.
- 17 cp giữ nguyên, không có lệnh mới. Không hành động gì thêm lần này; theo dõi sát ở lần check tiếp theo do rất gần stop-loss và phiên chính thức sắp mở.

## 2026-07-07 ~10:08 ET — Stop-loss WULF đã kích hoạt (đóng vị thế)

- **Stop-loss đã filled:** lệnh `6a4bce66-a34c-43f4-9d33-c890e50da8f6` khớp lúc 13:30:00 UTC (~09:30 ET, ngay đầu phiên) — bán 17 cp WULF @ giá TB $21.55, stop trigger $21.90. Vốn mua $23.7999 → lỗ thực hiện **-9.45%** (~$38.25), thu về ~$366.35.
- Giá WULF hiện tại (quote) $20.11 vs previous close $22.21 — giá tiếp tục giảm sau khi stop-loss khớp, xác nhận việc kích hoạt stop-loss là đúng thời điểm, không phải bị "quét" bởi nhiễu ngắn hạn rồi hồi ngay.
- **Tin tức đã tìm:** Fundamentals/analyst vẫn tích cực — Needham nâng price target lên $33 (Buy), Compass Point nâng lên $40 (Buy) sau tin hợp đồng Anthropic. Tuy nhiên giá cổ phiếu tiếp tục giảm vì lo ngại "execution and funding risk" — hợp đồng thuê 20 năm trị giá $19 tỷ đòi hỏi capex/tài trợ lớn, thị trường đang lo ngại về pha loãng cổ phần (dilution) hoặc rủi ro triển khai, không phải công ty có tin xấu nội tại.
  - Nguồn: [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/07/06/stock-market-today-july-6-terawulf-gains-on-usd19-billion-anthropic-ai-lease-deal/), [FX Leaders](https://www.fxleaders.com/news/2026/07/07/will-terawulf-wulf-stock-break-above-25-after-anthropics-19-billion-ai-data-center-deal/), [MarketBeat](https://www.marketbeat.com/instant-alerts/terawulf-nasdaqwulf-stock-price-expected-to-rise-needham-company-llc-analyst-says-2026-07-07/)
- **Quyết định:** đóng vị thế WULF hoàn toàn (do stop-loss tự động, không phải quyết định thủ công). KHÔNG mua lại WULF ngay lập tức dù thesis dài hạn vẫn tích cực — tránh whipsaw ngay sau khi bị stop ra, chờ giá ổn định hoặc có setup entry rõ ràng hơn (vd: xác nhận đáy kỹ thuật hoặc tin tức về kế hoạch tài trợ cụ thể). Tạm thời giữ cash, không mở vị thế mới đợt này.
- **Tài khoản:** buying power hiện $1,024.15 (tăng từ $524.15 — một phần bucket $500 nạp thêm đã settle, pending_deposits giảm còn $5,000 từ $5,500). Cash $1,390.50. Proceeds từ WULF ($366.35) đã phản ánh trong buying power (real-time từ broker).
- **Việc cần làm tiếp theo:** ở lần check kế tiếp, đánh giá lại WULF (có ổn định/hồi phục không) và/hoặc sàng lọc mã high-risk khác (nhóm bitcoin miner chuyển AI: IREN, CIFR, HUT vẫn đáng theo dõi) trước khi mở vị thế mới.

## 2026-07-07 — Tăng vốn sandbox lên $700/$1400

**Quyết định của Hogan:** tăng vốn gốc sandbox từ $400 lên $700 — chốt lời (circuit breaker) giờ kích hoạt khi tổng giá trị sandbox đạt ~$1400 (gấp đôi $700, thay cho mốc $800 cũ), lúc đó rút $700 gốc về, tiếp tục xoay vòng phần còn lại. Ngoài ra Hogan nạp thêm $700 nữa (tách biệt với $700 gốc) để luôn có sẵn bucket tiền thứ 2 dùng mua tiếp mà không phải chờ settle T+1 của bucket đầu — cùng logic 2-bucket đã thiết lập từ 2026-07-06, chỉ tăng quy mô. Tổng vốn thực tế đưa vào sandbox hiện ~$1400. Điều khoản dừng hẳn khi về gần $0 và không tự nạp thêm vẫn giữ nguyên. Cũng xác nhận sandbox không giới hạn 1 mã — có thể nắm giữ nhiều mã cùng lúc miễn tổng vốn dùng trong ngân sách. (Diễn ra sau sự kiện stop-loss WULF ở trên — sandbox hiện đang giữ cash, chưa mở vị thế mới.)
