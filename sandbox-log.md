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

## 2026-07-07 ~11:09 ET — Check + tìm tin tức (cả nhóm miner giảm mạnh, không vào lệnh mới)

- Sandbox hiện không có vị thế nào (cash-only, sau khi bị stop-loss WULF lúc ~10:08 ET). Lưu ý: vị thế QBTS xuất hiện trong tài khoản KHÔNG thuộc sandbox — đó là giao dịch thay thế IONQ trong danh mục core-10, đã được Hogan duyệt riêng (xem `trading-log.md`), không liên quan đến vốn sandbox.
- Trước khi quyết định có mở lại vị thế nhóm bitcoin-miner/AI-pivot không (WULF, IREN, CIFR, HUT — đang theo dõi từ lần check trước), kiểm tra giá: cả nhóm giảm mạnh so với đóng cửa hôm qua — WULF -10.4% ($19.90 vs $22.21), IREN -7.65% ($40.55 vs $43.91), CIFR -7.96% ($20.00 vs $21.73), HUT -7.06% ($96.44 vs $103.78). Vượt xa ngưỡng 3-5% → tìm tin tức sâu.
- **Tin tức:** đây là đợt bán tháo toàn ngành, không phải tin riêng của từng mã: (1) Bitcoin giảm mạnh xuống dưới $60,000; (2) Bloomberg đưa tin Meta đang lập đơn vị "Meta Compute" để bán lại công suất GPU dư thừa cho khách hàng thứ 3 — thách thức trực tiếp giả thuyết "compute scarcity" vốn là nền tảng cho câu chuyện AI-pivot của WULF/IREN/CIFR/HUT; (3) riêng IREN có tin xấu cụ thể — doanh thu Q3 $144.8M thấp hơn kỳ vọng nhiều, phát hành $2B convertible notes, ưu đãi thuế Oklahoma bị gác lại.
  - Nguồn: [Benzinga](https://www.benzinga.com/markets/equities/26/07/60268929/bitcoin-mining-stocks-iren-riot-and-mara-slide-as-ai-pivot-faces-fresh-headwinds), [Tickeron](https://tickeron.com/blogs/iren-limited-iren-stock-drops-41-7-in-30-days-amid-bitcoin-decline-and-ai-spending-fears-14462/), [Seeking Alpha](https://seekingalpha.com/article/4855958-terawulf-vs-cipher-mining-winners-in-2026s-ai-acceleration-story)
- **Quyết định:** KHÔNG mở lại vị thế trong nhóm này hôm nay. Tin Meta Compute là rủi ro cấu trúc mới (đe dọa trực tiếp thesis "compute scarcity"), không đơn thuần là nhiễu ngắn hạn như đợt giảm trước đó (chốt lời sau tin Anthropic). Kết hợp với Bitcoin giảm dưới $60k, đây là ngày risk-off toàn ngành — bắt đáy lúc này rủi ro cao hơn lợi ích. Tiếp tục giữ cash, chờ tín hiệu ổn định rõ ràng hơn hoặc cơ hội ở nhóm high-risk khác trước khi vào lệnh mới.
- Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-07 ~12:08 ET — Check nhẹ (cloud routine, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ sau stop-loss WULF ~10:08 ET, quyết định không mở lại nhóm miner ở lần check 11:09 ET).
- Giá nhóm bitcoin-miner/AI-pivot đang theo dõi, so với lần check trước (11:09 ET): WULF $19.90→$20.40 (+2.51%), IREN $40.55→$40.83 (+0.69%), CIFR $20.00→$20.70 (+3.50%), HUT $96.44→$97.28 (+0.87%).
- CIFR chạm nhẹ ngưỡng 3-5% nhưng đây là mức hồi phục nhẹ chung cả nhóm sau đợt bán tháo hôm qua (Meta Compute + Bitcoin giảm dưới $60k), không phải catalyst mới đảo ngược thesis risk-off đã phân tích ở lần check trước — không tìm tin tức sâu thêm, không có tín hiệu đủ mạnh để mở lại vị thế.
- Quyết định: tiếp tục giữ cash, không mở lệnh mới. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-07 ~13:08 ET — Check nhẹ (cloud routine, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ sau stop-loss WULF ~10:08 ET hôm nay).
- Giá nhóm bitcoin-miner/AI-pivot đang theo dõi, so với lần check trước (12:08 ET): WULF $20.40→$20.50 (+0.49%), IREN $40.83→$41.58 (+1.84%), CIFR $20.70→$20.83 (+0.63%), HUT $97.28→$98.81 (+1.57%). Tất cả dưới ngưỡng 3-5% — không tìm tin tức sâu, thesis risk-off từ lần check 11:09 ET (Meta Compute + Bitcoin dưới $60k) vẫn là cơ sở, chưa có tín hiệu đảo ngược rõ ràng.
- Buying power tài khoản hiện $527.59 (giảm từ $1,024.15 sau stop-loss WULF sáng nay) — mức giảm này đến từ giao dịch QBTS (24 cp, ~$496.56) thuộc core-10 portfolio (thay IONQ, đã duyệt riêng trong `trading-log.md`), KHÔNG liên quan đến vốn sandbox. Cash $1,344.64, pending_deposits $5,000 vẫn chờ settle.
- Quyết định: tiếp tục giữ cash, không mở lệnh mới. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-07 ~14:08 ET — Check nhẹ (cloud routine, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ sau stop-loss WULF ~10:08 ET hôm nay). Xác nhận qua get_equity_positions: không có WULF/IREN/CIFR/HUT trong tài khoản, chỉ có các mã core-10 (RXRX, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL) + QBTS (thay IONQ, thuộc core-10, không phải sandbox).
- Giá nhóm bitcoin-miner/AI-pivot đang theo dõi, so với lần check trước (13:08 ET): WULF $20.50→$20.465 (-0.17%), IREN $41.58→$41.38 (-0.48%), CIFR $20.83→$20.86 (+0.14%), HUT $98.81→$98.599 (-0.21%). Tất cả dưới ngưỡng 3-5% — không tìm tin tức sâu, thesis risk-off từ lần check 11:09 ET (Meta Compute + Bitcoin dưới $60k) vẫn là cơ sở, chưa có tín hiệu đảo ngược rõ ràng.
- Buying power tài khoản $527.59 (không đổi so với lần check trước), cash $1,344.64, pending_deposits $5,000 vẫn chờ settle.
- Quyết định: tiếp tục giữ cash, không mở lệnh mới. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-07 ~15:08 ET — Check nhẹ (cloud routine, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ sau stop-loss WULF ~10:08 ET hôm nay). Xác nhận qua get_equity_positions: không có WULF/IREN/CIFR/HUT trong tài khoản, chỉ có các mã core-10 (RXRX, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL) + QBTS (core-10, không phải sandbox).
- Giá nhóm bitcoin-miner/AI-pivot đang theo dõi, so với lần check trước (14:08 ET): WULF $20.465→$20.185 (-1.37%), IREN $41.38→$40.52 (-2.08%), CIFR $20.86→$20.455 (-1.94%), HUT $98.599→$96.32 (-2.31%). Tất cả dưới ngưỡng 3-5% — không tìm tin tức sâu. (Lưu ý: so với đóng cửa hôm qua cả nhóm vẫn giảm sâu hơn — WULF -9.10%, IREN -7.72%, CIFR -5.87%, HUT -7.17% — tiếp diễn xu hướng risk-off đã phân tích ở lần check 11:09 ET, không phải tín hiệu mới.)
- Quyết định: tiếp tục giữ cash, không mở lệnh mới. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-07 ~16:08 ET — Đóng cửa phiên, check nhẹ (cloud routine, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ sau stop-loss WULF ~10:08 ET hôm nay). Xác nhận qua get_equity_positions: không có WULF/IREN/CIFR/HUT, chỉ có các mã core-10 (RXRX, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL) + QBTS (core-10, không phải sandbox).
- Giá đóng cửa nhóm bitcoin-miner/AI-pivot, so với lần check trước (15:08 ET): WULF $20.185→$20.27 (+0.42%), IREN $40.52→$39.815 (-1.74%), CIFR $20.455→$20.58 (+0.61%), HUT $96.32→$96.64 (+0.33%). Tất cả dưới ngưỡng 3-5% — không tìm tin tức sâu. So với đóng cửa hôm qua (2026-07-06), cả nhóm vẫn giảm: WULF -8.74%, IREN -9.35%, CIFR -5.29%, HUT -6.87% — risk-off (Meta Compute + Bitcoin dưới $60k, phân tích tại lần check 11:09 ET) vẫn chưa đảo chiều rõ ràng.
- Lưu ý wash-sale: còn trong cửa sổ 30 ngày kể từ khi bán lỗ WULF (2026-07-07) — tránh mua lại WULF trước ~2026-08-06 nếu cân nhắc mở lại vị thế nhóm này.
- Quyết định: tiếp tục giữ cash, không mở lệnh mới. Thị trường vừa đóng cửa (16:00 ET) — chuyển sang chế độ qua đêm, chờ phiên kế tiếp. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-08 ~09:08 ET — Check + tìm tin tức (WULF pre-market vượt ngưỡng, vẫn cash-only)

- Sandbox vẫn không có vị thế nào (cash-only kể từ stop-loss WULF ngày 2026-07-07). Xác nhận qua get_equity_positions: không có WULF/IREN/CIFR/HUT, chỉ có core-10 (RXRX, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL) + QBTS (core-10, không phải sandbox).
- Giá pre-market (so với previous close 2026-07-07): WULF $21.00 vs $20.24 (**+3.76%**, vượt ngưỡng) — CIFR $20.20 vs $20.47 (-1.32%), IREN $39.36 vs $39.815 (-1.14%), HUT $95.05 vs $96.74 (-1.75%) — 3 mã còn lại dưới ngưỡng.
- **Tin tức (do WULF vượt ngưỡng):** không có catalyst mới — vẫn là diễn biến tiếp nối của tin Anthropic $19B lease (2026-07-06), giá đã pullback -8.87% hôm 07-07 do lo ngại funding/dilution, nay hồi nhẹ pre-market. Không có tin tức mới đảo ngược hay củng cố thesis kể từ lần check 07-07 ~10:08 ET.
  - Nguồn: [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/07/07/stock-market-today-july-7-terawulf-pulls-back-after-anthropic-lease-draws-focus-to-ai-buildout/), [MarketBeat](https://www.marketbeat.com/instant-alerts/terawulf-nasdaqwulf-stock-price-down-99-should-you-sell-2026-07-07/)
- **Quyết định:** KHÔNG mua lại WULF — vẫn trong cửa sổ wash-sale 30 ngày kể từ khi bán lỗ WULF ngày 2026-07-07 (chỉ mới 1 ngày, tránh mua lại tới ~2026-08-06). Đây cũng chỉ là hồi kỹ thuật nhẹ, không phải catalyst mới đủ mạnh để đổi sang mã khác cùng nhóm (IREN/CIFR/HUT đều giảm nhẹ, không có tín hiệu entry). Tiếp tục giữ cash.
- Tài khoản: buying power $1,344.64, cash $1,344.64, pending_deposits $5,000 (chưa settle thêm), total_value $5,919.28. Không có circuit breaker nào bị kích hoạt (không có vị thế để tính giá trị sandbox).

## 2026-07-08 ~10:09 ET — Mở lại vị thế mới: mua HUT (nhóm miner rally mạnh, catalyst mới xác nhận)

- Giá check định kỳ: WULF $22.505 vs previous close $20.24 (**+11.2%**), IREN $42.25 vs $39.815 (**+6.1%**), CIFR $21.33 vs $20.47 (**+4.2%**), HUT $99.07 vs $96.74 (**+2.4%** so với close, nhưng **+4.23%** so với lần check trước 09:08 ET khi HUT ở $95.05) — tất cả vượt xa ngưỡng 3-5% so với lần check trước → tìm tin tức sâu.
- **Tin tức:** đây KHÔNG phải chỉ là hồi phục kỹ thuật sau đợt risk-off hôm qua (Meta Compute + Bitcoin <$60k) — có catalyst công ty cụ thể mới, khác biệt với đợt bán tháo: (1) IREN ký hợp đồng $1.6 tỷ với Dell để cung cấp hệ thống AI Blackwell, phục vụ hợp đồng cloud $3.4 tỷ đã ký trước đó — xác nhận hợp đồng doanh thu đang được triển khai thật; (2) Hut 8 (HUT) tăng giá lên mức đỉnh lịch sử mới nhờ hợp đồng thuê data center AI trị giá $9.8 tỷ gắn với Nvidia — quy mô/tính chất tương tự catalyst Anthropic $19B đã từng đẩy WULF tăng mạnh hôm 07-06. CIFR/HUT cũng lập đỉnh lịch sử mới, xác nhận dòng tiền tổ chức thật, không phải chỉ nhiễu ngắn hạn.
  - Nguồn: [The Block](https://www.theblock.co/post/402773/bitcoin-miner-ai-boom-stocks-soaring-cipher-hut-8-fresh-highs), [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/bitcoin-mining-stocks-jump-terawulf-151536170.html), [CCN](https://www.ccn.com/news/crypto/ai-boom-bitcoin-mining-stocks-hut8-cipher-iren-surge/)
- **Quyết định:** mở vị thế mới trong HUT (không phải WULF — còn trong cửa sổ wash-sale 30 ngày tới ~2026-08-06 sau khi bán lỗ WULF ngày 2026-07-07, không được mua lại). Chọn HUT thay vì IREN/CIFR vì catalyst ($9.8B Nvidia-tied lease) gần giống nhất về bản chất (hợp đồng thuê dài hạn tạo doanh thu) với catalyst Anthropic đã từng xác nhận hiệu quả cho nhóm này.
- **Mua 5 cp HUT @ $98.9699 (thị giá), tổng $494.85.** Order id `6a4e5a1c-44a9-4409-9e4e-e03c53bf8631`, state=filled.
- Đặt stop-loss -8% tại $91.05 (kỷ luật rủi ro cho nhóm biến động cao), order id `6a4e5a27-a403-4b82-8e6c-523da527af61`, state=confirmed/active ngay sau khi đặt.
- Chốt lời dự kiến (không đặt lệnh tự động, theo dõi thủ công): +15-20% từ vốn (~$114-119/cp), risk/reward ~1:2 so với stop-loss -8%.
- Rủi ro chính: mua sau khi giá đã tăng mạnh trong phiên (+4-11% tùy mã) — rủi ro chase đỉnh ngắn hạn, có thể pullback nếu thị trường chốt lời; nhóm miner/AI-pivot vẫn biến động rất cao, đã từng đảo chiều nhanh (như đợt risk-off hôm qua).
- Tài khoản sau lệnh: cần xác nhận buying power ở lần check tiếp theo để đảm bảo không có GFV do phần tiền dùng mua đã settled (buying power $1,344.64 trước lệnh là tiền mặt thực, không phải pending).
- Việc cần làm tiếp theo: theo dõi giá HUT sát hơn ở các lần check tiếp theo; nếu circuit breaker (giá trị sandbox ~gấp đôi $1400 hoặc về gần $0) kích hoạt thì xử lý theo quy định.
- **Lưu ý đồng bộ:** một phiên/tiến trình cloud routine khác chạy gần như đồng thời đã phát hiện cùng giao dịch này qua rà soát vị thế (cùng order id) và ghi một entry ngắn hơn — entry đầy đủ ở trên (với phân tích tin tức/catalyst gốc) là bản chính thức, thay thế cho entry rút gọn đó. Chỉ có 1 giao dịch mua HUT thực tế (5 cp), không bị mua trùng.

## 2026-07-08 ~11:08 ET — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $97.625 vs vốn $98.97 (-1.36%). So với lúc mua (~10:09 ET @ $98.9699), biến động nhỏ — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn state=`confirmed`/active, order id `6a4e5a27-a403-4b82-8e6c-523da527af61`, 5 cp giữ nguyên. Giá trị vị thế hiện ~$488.13 — chưa gần ngưỡng gấp đôi ($1400) hay về $0, không kích hoạt circuit breaker.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-08 ~12:08 ET — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $97.4795 vs vốn $98.97 (-1.51%). So với lần check trước (11:08 ET @ $97.625), biến động chỉ -0.15% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn state=`confirmed`/active, order id `6a4e5a27-a403-4b82-8e6c-523da527af61`, 5 cp giữ nguyên. Giá trị vị thế hiện ~$487.40 — chưa gần ngưỡng gấp đôi ($1400) hay về $0, không kích hoạt circuit breaker.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-08 ~13:08 ET — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $99.035 vs vốn $98.97 (+0.07%). So với lần check trước (12:08 ET @ $97.4795), biến động +1.60% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn state=`confirmed`/active, order id `6a4e5a27-a403-4b82-8e6c-523da527af61`, 5 cp giữ nguyên (xác nhận qua get_equity_positions). Giá trị vị thế hiện ~$495.18 — chưa gần ngưỡng gấp đôi ($1400) hay về $0, không kích hoạt circuit breaker.
- Tài khoản: cash $849.79, buying power $849.79, pending_deposits $5,000 (chưa settle), total_value $5,919.32.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-08 ~19:08 UTC (~15:08 ET) — Check + tìm tin tức (HUT chạm ngưỡng, vẫn giữ nguyên)

- Giá HUT hiện $102.73 vs vốn $98.97 (+3.80%). So với lần check trước (13:08 ET @ $99.035), biến động +3.73% — chạm ngưỡng, tìm tin tức sâu.
- **Tin tức:** không có catalyst tiêu cực mới. Đà tăng tiếp diễn từ thesis đã xác nhận (hợp đồng thuê Beacon Point 15 năm, 352MW, trị giá $9.8 tỷ gắn Nvidia). Điểm mới đáng chú ý: Hut 8 vừa đóng đợt phát hành $4.25 tỷ trái phiếu senior secured 6.129% đáo hạn 2042 để tài trợ Beacon Point — non-recourse, non-dilutive, xếp hạng Baa2 — trực tiếp giải quyết lo ngại "funding/dilution risk" từng khiến nhóm miner này (kể cả WULF) bị bán tháo trước đó. Analyst consensus vẫn Strong Buy/Buy (15/15 trong 3 tháng qua), dù định giá P/S 41.1x bị xem là cao.
  - Nguồn: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/hut-8-hut-stock-looks-182104307.html), [StockTitan](https://www.stocktitan.net/news/HUT/), [Nasdaq](https://www.nasdaq.com/market-activity/stocks/hut/news-headlines)
- **Quyết định:** giữ nguyên 5 cp HUT, không bán, không thêm. Catalyst xác nhận thesis, không phải rủi ro mới. Stop-loss $91.05 vẫn `confirmed`/active.
- Giá trị vị thế hiện ~$513.65 — chưa gần ngưỡng gấp đôi ($1400) hay về $0, không kích hoạt circuit breaker. Tài khoản: cash/buying power $849.79 (không đổi so với lần trước), pending_deposits $5,000 chưa settle.
- Không gửi push notification (không có hành động/thay đổi thật dù có tìm tin tức — theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-08 ~20:09 UTC (~16:09 ET) — Check + tìm tin tức (HUT chạm ngưỡng, vẫn giữ nguyên, gần đóng cửa)

- Giá HUT hiện $106.19 vs vốn $98.97 (+7.29%). So với lần check trước (15:08 ET @ $102.73), biến động +3.37% — chạm ngưỡng, tìm tin tức sâu.
- **Tin tức:** không có catalyst tiêu cực mới, đà tăng tiếp diễn từ thesis đã xác nhận (Beacon Point lease $9.8B, Q1 2026 backlog $16.8B trên 2 campus AI hyperscale 597MW, đợt phát hành trái phiếu $4.25B non-dilutive tuần này). Analyst consensus vẫn 15/15 Buy/Strong Buy, median price target $127. Một số nguồn ghi nhận lo ngại định giá cao (P/S 41.1x) và có tin về insider sales, nhưng không phải catalyst đảo chiều thesis.
  - Nguồn: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/hut-8-hut-stock-looks-182104307.html), [StockTitan](https://www.stocktitan.net/news/HUT/), [QuiverQuant](https://www.quiverquant.com/news/Hut+8+(HUT)+Falls+as+Rally+Cools+and+Investors+Digest+Recent+Financing+and+Insider+Sales)
- **Quyết định:** giữ nguyên 5 cp HUT, không bán, không thêm. Catalyst xác nhận thesis, không phải rủi ro mới; chưa đạt mức chốt lời dự kiến (+15-20%, hiện mới +7.29%). Stop-loss $91.05 vẫn `confirmed`/active.
- Giá trị vị thế hiện ~$530.95 (5 cp × $106.19) — chưa gần ngưỡng gấp đôi ($1400) hay về $0, không kích hoạt circuit breaker. Thị trường sắp đóng cửa (16:00 ET đã qua, giá là giá đóng/gần đóng cửa).
- Không gửi push notification (không có hành động/thay đổi thật dù có tìm tin tức — theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~09:08 ET (13:08 UTC) — Check + tìm tin tức (HUT pre-market vượt ngưỡng, GẦN chạm circuit breaker chốt lời)

- Giá HUT pre-market: $109.40 (last_non_reg_trade_price, 13:07:40 UTC) vs giá đóng cửa hôm qua $106.19/$106.11 (**+3.02%** so với lần check trước 16:09 ET 07-08) — chạm ngưỡng 3-5%, tìm tin tức sâu. Bid/ask pre-market khá rộng ($109.00/$110.00).
- **Tin tức:** không có catalyst mới, tiêu cực hay tích cực đột biến — tiếp diễn đà tăng 9% từ phiên 07-08 (đóng cửa $105.49, previous close trước đó $96.74) nhờ thesis AI-pivot đã xác nhận (Beacon Point lease $9.8B, trái phiếu $4.25B non-dilutive). Analyst vẫn Strong Buy, Piper Sandler PT $127, Loop Capital PT $226. Không có tin mới đảo chiều hay củng cố thêm so với lần check trước.
  - Nguồn: [Ticker Report](https://www.tickerreport.com/banking-finance/13498251/hut-8-nasdaqhut-trading-9-higher-should-you-buy.html), [Yahoo Finance](https://finance.yahoo.com/quote/HUT/)
- **Tính giá trị sandbox tổng (quan trọng — GẦN circuit breaker chốt lời):** cash/buying power $849.79 (đã fully settled, pending_deposits $0) + giá trị vị thế HUT (5 cp × $109.40 = $547.00, hoặc theo giá bid thực tế $109.00 = $545.00) → **tổng ~$1,394.79–$1,396.79**, tương đương **~99.6-99.8% ngưỡng gấp đôi ~$1,400** (vốn gốc $700, theo quy định chốt lời trong CLAUDE.md).
- **Quyết định:** CHƯA bán — giá hiện tại là pre-market với spread rộng ($109/$110, chưa đại diện giá phiên chính thức đáng tin cậy để thực hiện quyết định circuit breaker cấp danh mục), và mới đạt ~99.7% ngưỡng chứ chưa vượt hẳn. Giữ nguyên 5 cp HUT, không bán, không thêm vị thế mới. Stop-loss $91.05 vẫn `confirmed`/active. Sẽ đánh giá lại ngay khi có giá phiên chính thức (từ 9:30 ET) ở lần check tiếp theo — nếu tổng giá trị sandbox xác nhận ≥~$1400 với giá thanh khoản tốt, sẽ bán một phần/toàn bộ HUT để chốt lời và rút vốn gốc $700 theo đúng quy định.
- Không có circuit breaker nào chính thức kích hoạt (chỉ mới cận ngưỡng, chưa xác nhận) — nhưng do mức độ quan trọng (gần đạt mốc chốt lời gấp đôi), vẫn gửi push notification để Hogan biết trước khi thị trường mở cửa chính thức.

## 2026-07-09 ~09:16 ET (13:16 UTC) — Check đồng bộ, vẫn pre-market, GIỮ NGUYÊN kế hoạch chờ mở cửa

- Giá HUT pre-market hiện $109.85 (13:13:55 UTC), bid/ask $109.00/$113.00 — spread còn rộng hơn lần check trước (09:08 ET), chưa đủ tin cậy để chốt quyết định circuit breaker.
- Tổng giá trị sandbox ước tính: cash $849.79 (đã settle, pending_deposits $0) + HUT 5 cp × $109.85 = $549.25 → tổng **~$1,399.04** (theo giá bid $109 thận trọng hơn: ~$1,394.79) — vẫn quanh ngưỡng ~$1,400, chưa vượt hẳn với giá đáng tin cậy.
- Thị trường chính thức chưa mở cửa (9:30 ET/13:30 UTC) — giữ nguyên kế hoạch đã đặt ở lần check 09:08 ET: chờ giá phiên chính thức rồi mới quyết định chốt lời một phần/toàn bộ nếu tổng giá trị xác nhận ≥$1400.
- Không có lệnh mới. Không gửi push notification thêm (đã gửi ở lần check trước, chưa có thay đổi thật kể từ đó).

## 2026-07-09 ~09:44 ET (13:44 UTC) — SỬA LỖI công thức chốt lời (Hogan phát hiện)

> **Đính chính:** 2 entry ngay trên (09:08 ET và 09:16 ET) tính SAI công thức ngưỡng chốt lời — đã cộng thẳng cả $700 bucket đệm (buffer chờ settle) vào tổng để so với $1400, khiến tưởng nhầm là "gần chạm ngưỡng". Hogan chỉ ra công thức đúng: ngưỡng gấp đôi ($1400) chỉ áp dụng cho **phần đang xoay vòng $700 gốc** — tức (cash trừ $700 đệm) + giá trị vị thế hiện có, KHÔNG cộng nguyên $700 đệm vào.

- Giá HUT phiên chính thức (đã mở cửa, spread hẹp, đáng tin cậy): $108.49 (13:44:31 UTC), bid/ask $108.30/$108.90.
- **Tính lại đúng công thức:** cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $108.49 = $542.45) = **phần theo dõi ~$692.24** — bắt đầu từ mốc $700, hiện gần như đi ngang (chưa tính phí/lãi lỗ tích lũy từ WULF trước đó). Còn CÁCH RẤT XA ngưỡng chốt lời $1400 (mới ~49%), không phải 99% như 2 entry trước ghi nhầm.
- Đã sửa `CLAUDE.md` (mục "Chốt lời" trong phần sandbox) để ghi rõ công thức, tránh lặp lại lỗi. Đã cập nhật memory `sandbox_400_autonomous.md`.
- **Tác động:** không có circuit breaker nào cận kề. Có ~$149.79 cash thực sự rảnh (ngoài $700 đệm) sẵn sàng đầu tư thêm nếu có cơ hội tốt — không cần chờ ngưỡng gấp đôi.
- Không gửi push notification (đây là điều chỉnh nội bộ, không phải giao dịch/circuit breaker thật).

## 2026-07-09 ~10:03 ET (14:03 UTC) — Tìm cơ hội mới cho $150 cash rảnh (theo yêu cầu Hogan), quyết định GIỮ CASH

- Giá hiện tại nhóm miner/AI-pivot (phiên chính thức): HUT $108.51 (+2.26% ngày, +9.64% so vốn), WULF $23.50 (+2.94% ngày — còn cấm mua tới ~2026-08-06 do wash-sale), IREN $43.585 (+1.35% ngày), CIFR $22.86 (**+4.62% ngày** — chạm ngưỡng, tìm tin tức).
- **Tin tức:** tìm CIFR/IREN/HUT — không có catalyst MỚI riêng cho ngày 07-09. Tin đang lưu hành vẫn là các catalyst đã biết: CIFR bắt đầu triển khai giai đoạn 1 hợp đồng AWS 300MW/$5.5B (Needham nâng target lên $25), IREN có hợp đồng Microsoft GPU cloud $9.7B/5 năm (đã biết), HUT vẫn là Nvidia-tied lease $9.8B (đã có vị thế). Đà tăng hôm nay là tiếp diễn thesis AI-pivot đã phản ánh vào giá những ngày trước, không phải tín hiệu entry mới/riêng biệt.
  - Nguồn: [CCN](https://www.ccn.com/news/crypto/ai-boom-bitcoin-mining-stocks-hut8-cipher-iren-surge/), [The Block](https://www.theblock.co/post/402773/bitcoin-miner-ai-boom-stocks-soaring-cipher-hut-8-fresh-highs), [24/7 Wall St](https://247wallst.com/investing/2026/07/08/terawulf-rises-12-iren-climbs-7-as-ai-infrastructure-stocks-bounce-back/)
- **Quyết định:** KHÔNG mở vị thế mới. Không có catalyst riêng biệt đủ mạnh để chọn CIFR/IREN thay vì HUT (đã có exposure nhóm này qua HUT rồi — thêm CIFR/IREN chỉ là tăng gấp đôi cùng một thesis, không đa dạng hóa thật). $150 cash không đủ mua 1 cp nguyên của IREN/CIFR cộng đủ margin an toàn để còn dư cho biến động. Giữ nguyên cash rảnh, không ép giao dịch.
- Không đề xuất tăng vốn (chưa có cơ hội đủ tốt để cần vượt ngân sách hiện có).
- Không gửi push notification (không có hành động/thay đổi thật, không có đề xuất cần duyệt).

## 2026-07-09 ~10:08 ET (14:08 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $109.07 vs vốn $98.97 (+10.20%). So với lần check trước (10:03 ET @ $108.51), biến động +0.52% — dưới ngưỡng 3-5%, không tìm tin tức sâu (thesis AI-pivot/Nvidia-tied lease đã xác nhận các lần check trước vẫn là cơ sở).
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (còn cấm mua tới ~2026-08-06 do wash-sale), giá tham khảo $23.38.
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước.
- **Tính đúng công thức "phần theo dõi" (theo đính chính 09:44 ET):** cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $109.07 = $545.35) = **~$695.14** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.7%). Không có circuit breaker nào kích hoạt (chốt lời hay dừng hẳn).
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~11:09 ET (15:09 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $108.62 vs vốn $98.97 (+9.75%). So với lần check trước (10:08 ET @ $109.07), biến động -0.41% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (còn cấm mua tới ~2026-08-06 do wash-sale), giá tham khảo $23.725 (+3.92% ngày). CIFR $23.26 (+6.45% ngày) và IREN $43.18 (+0.41% ngày) — cả hai không phải vị thế hiện có, chỉ tiếp diễn thesis AI-pivot đã biết, không xét entry mới (đã có exposure nhóm này qua HUT).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước.
- "Phần theo dõi": cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $108.62 = $543.10) = **~$692.89** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.5%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~12:08 ET (16:08 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $109.75 vs vốn $98.97 (+10.89%). So với lần check trước (11:09 ET @ $108.62), biến động +1.04% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (còn cấm mua tới ~2026-08-06 do wash-sale), giá tham khảo $24.20 (+6.00% ngày). CIFR $23.745 (+8.68% ngày) và IREN $43.02 (+0.03% ngày) — không phải vị thế hiện có, không xét entry mới (đã có exposure nhóm AI-pivot/miner qua HUT).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước.
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $109.75 = $548.75) = **~$698.54** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.9%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~13:08 ET (17:08 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $108.79 vs vốn $98.97 (+9.92%). So với lần check trước (12:08 ET @ $109.75), biến động -0.87% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (còn cấm mua tới ~2026-08-06 do wash-sale), giá tham khảo $23.955 (+4.93% ngày).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước.
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $108.79 = $543.95) = **~$693.74** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.6%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~14:08 ET (18:08 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $107.84 vs vốn $98.97 (+8.96%). So với lần check trước (13:08 ET @ $108.79), biến động -0.87% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). Chỉ có core-10 khác (RXRX, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL) + QBTS (core-10, không phải sandbox) trong tài khoản.
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước.
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $107.84 = $539.20) = **~$688.99** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.2%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-09 ~15:08 ET (19:08 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $107.65 vs vốn $98.97 (+8.77%). So với lần check trước (14:08 ET @ $107.84), biến động -0.18% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). Không có vị thế sandbox nào khác (WULF vẫn cấm mua tới ~2026-08-06 do wash-sale, không nắm giữ).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước. Total account value $5,970.49.
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $107.65 = $538.25) = **~$688.04** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.1%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).


## 2026-07-09 ~16:03 ET (20:03 UTC) — Check nhẹ, thị trường vừa đóng cửa (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $106.28 (last_trade_price 19:59:59 UTC, cuối phiên chính thức; after-hours $105.72) vs vốn $98.97 (+7.39%). So với lần check trước (15:08 ET @ $107.65), biến động -1.27% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). Không có vị thế sandbox nào khác (WULF vẫn cấm mua tới ~2026-08-06 do wash-sale, không nắm giữ).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0 theo lần check gần nhất, không thay đổi).
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $106.28 = $531.40) = **~$681.19** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~48.7%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Thị trường vừa đóng cửa (16:00 ET) — chuyển sang chế độ qua đêm, chờ phiên kế tiếp. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).


## 2026-07-10 ~09:10 ET (13:10 UTC) — Check nhẹ, đầu phiên/pre-market (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $107.91 (pre-market, last_non_reg_trade_price 13:01 UTC) vs vốn $98.97 (+9.03%). So với lần check trước (16:03 ET hôm qua @ $106.28 close), biến động +1.53% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). Không có vị thế sandbox nào khác (WULF vẫn cấm mua tới ~2026-08-06 do wash-sale, không nắm giữ; giá tham khảo $23.215, không phải vị thế hiện có).
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước. Total account value $5,981.84.
- "Phần theo dõi" (đúng công thức đính chính 09:44 ET 07-09): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $107.91 = $539.55) = **~$689.34** — vẫn quanh mốc gốc $700, còn rất xa ngưỡng chốt lời $1400 (~49.2%). Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-10 ~10:09 ET (14:09 UTC) — Check + tìm tin tức (HUT giảm vượt ngưỡng, giữ nguyên)

- Giá HUT hiện $101.64 vs previous close $106.22 (**-4.31%** trong ngày) và vs vốn $98.97 (+2.70%). So với lần check trước (09:10 ET @ $107.91 pre-market), biến động **-5.81%** — vượt ngưỡng 3-5%, tìm tin tức sâu.
- **Tin tức:** không có catalyst tiêu cực mới về công ty/fundamentals. QuiverQuant ghi nhận "Hut 8 (HUT) slides 7.2% as crypto-sensitive names cool and recent insider selling weighs on sentiment" — pullback đến từ (1) nhóm crypto-sensitive hạ nhiệt chung (không riêng HUT), (2) tâm lý nhà đầu tư bị ảnh hưởng bởi tin insider selling đã biết trước đó (không phải tin mới), không có tin xấu về hợp đồng Beacon Point/Nvidia-tied lease hay tài chính công ty. Đây là điều chỉnh/chốt lời sau chuỗi tăng mạnh (~+10% so vốn những ngày trước), không phải đảo chiều thesis.
  - Nguồn: [QuiverQuant](https://www.quiverquant.com/news/Hut+8+(HUT)+slides+7.2%+as+crypto-sensitive+names+cool+and+recent+insider+selling+weighs+on+sentiment), [Yahoo Finance](https://finance.yahoo.com/quote/HUT/)
- Stop-loss @ $91.05 vẫn state=`confirmed`/active (order id `6a4e5a27-a403-4b82-8e6c-523da527af61`), 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). Giá hiện còn cách stop-loss ~10.4%, chưa gần kích hoạt.
- Tài khoản: cash/buying power $849.79 (đã settle, pending_deposits $0), total_value $5,902.92.
- "Phần theo dõi" (đúng công thức đính chính 2026-07-09): cash $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $101.64 = $508.20) = **~$657.99** — dưới mốc gốc $700 (~94%), còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt (chốt lời hay dừng hẳn).
- Quyết định: giữ nguyên vị thế, không có lệnh mới, không bán non — pullback do tâm lý/sector cooling chứ không phải tin xấu thesis-breaking, stop-loss -8% vẫn đủ để bảo vệ nếu tiếp tục giảm sâu hơn.
- Không gửi push notification (không có hành động/thay đổi thật; mức giảm nằm trong biên độ biến động bình thường của nhóm này, chưa chạm circuit breaker).

## 2026-07-10 ~11:10 ET (15:10 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $101.675 vs vốn $98.97 (+2.73%), vs previous close $106.22 (-4.31% trong ngày, không đổi so với lần check trước). So với lần check trước (10:09 ET @ $101.64), biến động +0.03% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn state=`confirmed` (order id `6a4e5a27-...`), 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale).
- Tài khoản: buying power $849.79 (đã settle, pending_deposits $0), không đổi so với lần check trước. Lưu ý: cash tổng tài khoản tăng lên $1,305.64 do stop-loss RXRX (core-10, 131 cp @ $3.48) vừa khớp lúc 14:33 UTC hôm nay — đây là sự kiện core-10, không thuộc phạm vi sandbox, không ảnh hưởng tới buying_power dùng cho công thức dưới đây, để routine core-10/`trading-log.md` xử lý riêng.
- "Phần theo dõi" (đúng công thức đính chính 2026-07-09): buying power $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $101.675 = $508.38) = **~$658.17** — dưới mốc gốc $700 (~94%), còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-10 ~12:09 ET (16:09 UTC) — Check nhẹ (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $102.475 vs vốn $98.97 (+3.54%), vs previous close $106.22 (-3.53% trong ngày). So với lần check trước (11:10 ET @ $101.675), biến động +0.79% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss @ $91.05 vẫn active, 5 cp HUT giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale). Không có vị thế sandbox nào khác.
- Tài khoản: buying power $849.79 (không đổi so với lần check trước), cash tổng $1,305.64 (bao gồm proceeds stop-loss RXRX core-10, không thuộc sandbox), total_value $5,881.68.
- "Phần theo dõi" (đúng công thức đính chính 2026-07-09): buying power $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5 cp × $102.475 = $512.38) = **~$662.16** — dưới mốc gốc $700 (~94.6%), còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-10 ~13:10 ET (17:10 UTC) — Check định kỳ (giữ nguyên HUT; SOUN xuất hiện trong tài khoản KHÔNG thuộc sandbox)

- Giá HUT hiện $102.84 vs vốn $98.97 (+3.91%), vs previous close $106.22 (-3.18% trong ngày). So với lần check trước (12:09 ET @ $102.475), biến động +0.36% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss HUT @ $91.05 vẫn `confirmed`/active (order `6a4e5a27-...`), 5 cp giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale).
- **Lưu ý quan trọng — phát hiện vị thế SOUN mới trong tài khoản, KHÔNG thuộc sandbox:** ban đầu nhầm tưởng đây là giao dịch sandbox chưa được log và đã soạn nhầm 1 entry gán SOUN vào sandbox — đã tự phát hiện và sửa lại trước khi commit. Xác nhận qua `git log`/`trading-log.md`: SOUN (76 cp @ $6.5899, tổng $500.83, order `6a511f3c-...`, stop-loss -8% @ $6.06 order `6a511f46-...`) là **giao dịch thay thế RXRX trong core-10** — Hogan đã duyệt chọn SOUN thay vì TEM từ đề xuất 2 lựa chọn, đã ghi log đầy đủ tại `trading-log.md` (~12:35 ET) và commit riêng ("Replace RXRX with SOUN in core-10 (approved)"). SOUN KHÔNG phải vị thế sandbox — sandbox vẫn chỉ nắm giữ HUT.
- Tài khoản: buying power $348.96 (giảm từ $849.79) — mức giảm này đến từ việc mua SOUN $500.83 (core-10) được thanh toán từ pool tiền mặt chung, TRƯỚC KHI proceeds stop-loss RXRX ($455.85, cũng thuộc core-10) kịp settle vào buying power. Đây là hiệu ứng thời điểm settle giữa 2 giao dịch core-10, KHÔNG liên quan đến vốn/đệm sandbox — buying power sandbox thực tế không đổi, dự kiến buying power tổng sẽ tự phục hồi về ~$804-849 khi RXRX proceeds settle xong (thường T+1). Cash $804.81, total_value $5,891.82.
- "Phần theo dõi" sandbox (chỉ tính HUT, dùng buying power $849.79 trước giao dịch core-10 làm cơ sở tạm thời do buying power hiện tại đang bị ảnh hưởng bởi timing của core-10, sẽ xác nhận lại ở lần check sau khi settle xong): $849.79 − $700 đệm = $149.79 cash rảnh + HUT (5×$102.84=$514.20) = **~$663.99** (~94.9% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên HUT, không có lệnh mới cho sandbox. Không gửi push notification thay đổi/circuit breaker vì không có hành động sandbox thật — nhưng gửi 1 push thông tin ngắn nhắc rằng SOUN thuộc core-10 (không phải sandbox), để tránh nhầm lẫn nếu Hogan thấy vị thế mới trong tài khoản.

## 2026-07-10 ~14:07 ET (18:07 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $103.88 vs vốn $98.97 (+4.96%), vs previous close $106.22 (-2.20% trong ngày). So với lần check trước (13:10 ET @ $102.84), biến động +1.01% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Stop-loss HUT @ $91.05 vẫn `confirmed`/active (order `6a4e5a27-...`), 5 cp giữ nguyên (xác nhận qua get_equity_positions). WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale). Không có vị thế sandbox nào khác.
- Xác nhận vị thế 10 mã core hiện tại (không thuộc phạm vi sandbox, chỉ ghi chú tham khảo): SOUN, AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL, QBTS — khớp `trading-log.md`, không có mã lạ.
- Tài khoản: buying power $348.96 — vẫn ở mức thấp giống lần check 13:10 ET (chưa hồi phục về ~$804-849 như dự kiến, có thể proceeds RXRX/timing settle core-10 chưa hoàn tất). total_value $5,893.68, cash $804.81. Đây là hiệu ứng timing từ giao dịch core-10 (SOUN/QBTS), không phải giao dịch sandbox.
- "Phần theo dõi" sandbox: do buying power hiện tại đang bị ảnh hưởng bởi timing settle core-10 (chưa phản ánh đúng phần sandbox), tạm dùng baseline $849.79 (mức buying power sandbox xác nhận gần nhất trước khi bị ảnh hưởng) − $700 đệm = $149.79 cash rảnh + HUT (5×$103.88=$519.40) = **~$669.19** (~95.6% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-10 ~15:08 ET (19:08 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $102.80 (last_trade_price 19:08:01 UTC) vs vốn $98.97 (+3.87%), vs previous close $106.22 (-3.22% trong ngày). So với lần check trước (14:07 ET @ $103.88), biến động -1.04% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên, không có vị thế sandbox nào khác. Core-10 hiện tại: AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL, QBTS, SOUN — khớp `trading-log.md`, không có mã lạ.
- Tài khoản: buying power $348.96 (vẫn thấp, chưa hồi phục về ~$804-849 — hiệu ứng timing settle core-10 từ SOUN/RXRX, không phải giao dịch sandbox), cash $804.81, total_value $5,895.20.
- "Phần theo dõi" sandbox: tạm dùng baseline $849.79 (buying power sandbox xác nhận gần nhất trước ảnh hưởng timing core-10) − $700 đệm = $149.79 cash rảnh + HUT (5×$102.80=$514.00) = **~$663.79** (~94.8% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-10 ~16:05 ET (20:05 UTC) — Check định kỳ (giữ nguyên HUT, gần cuối phiên)

- Giá HUT: last_trade_price $102.191 (19:59:59 UTC, regular hours) vs last_non_reg_trade_price $101.21 (20:02:57 UTC, sau giờ — dùng giá này vì mới hơn) — so với vốn $98.97: +2.26%; so với previous close $106.22: -4.72% trong ngày. So với lần check trước (15:08 ET @ $102.80), biến động -1.55% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. Stop-loss HUT @ $91.05 vẫn `confirmed`/active (order `6a4e5a27-...`, last_transaction_at 2026-07-10T12:21:49Z). WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale).
- Core-10 hiện tại: AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL, QBTS, SOUN — khớp `trading-log.md`, không có mã lạ, không chạm vào.
- Tài khoản: buying power $348.96 (vẫn thấp, chưa hồi phục về ~$804-849 như 2 lần check trước dự đoán — hiệu ứng timing settle core-10 từ SOUN/RXRX kéo dài hơn dự kiến, không phải giao dịch sandbox), cash $804.81, total_value $5,885.82.
- "Phần theo dõi" sandbox: tạm dùng baseline $849.79 (buying power sandbox xác nhận gần nhất trước ảnh hưởng timing core-10) − $700 đệm = $149.79 cash rảnh + HUT (5×$101.21=$506.05) = **~$655.84** (~93.7% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-13 ~09:00 ET (13:00 UTC) — Check đầu tuần, pre-market (cloud routine, giữ nguyên HUT)

- Giá HUT hiện $99.31 (pre-market, last_non_reg_trade_price 12:45 UTC) vs vốn $98.97 (+0.34%), vs previous close (Fri 07-10) $102.22 (-2.85%). So với lần check trước (07-10 16:05 ET @ $101.21), biến động -1.88% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale), giá tham khảo $21.42 (pre-market).
- Xác nhận get_equity_orders (từ 07-10 20:05 ET tới nay): không có lệnh mới nào trong toàn tài khoản — không có hoạt động sandbox hay core-10 nào chưa được log.
- Tài khoản: buying power $804.81 (đã settle đầy đủ, pending_deposits $0, khớp với cash $804.81) — đã phục hồi từ mức thấp tạm thời $348.96 ghi nhận cuối tuần trước do hiệu ứng timing settle core-10 (SOUN mua $500.83 trước khi RXRX proceeds $455.85 settle xong). Baseline sandbox mới xác nhận: $804.81 (thấp hơn $849.79 cũ ~$44.98, đúng bằng chênh lệch ròng SOUN/RXRX của core-10, không phải thay đổi sandbox). Total account value $5,869.37.
- "Phần theo dõi" sandbox (dùng buying power $804.81 đã settle xác nhận): $804.81 − $700 đệm = $104.81 cash rảnh + HUT (5×$99.31=$496.55) = **~$601.36** (~85.9% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-13 ~10:09 ET (14:09 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $98.49 vs vốn $98.97 (-0.49%), vs previous close (Fri 07-10) $102.22 (-3.65% trong ngày). So với lần check trước (09:00 ET pre-market @ $99.31), biến động -0.83% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale).
- **Lưu ý (không thuộc sandbox):** buying_power tổng tài khoản giảm còn $307.18 (từ $804.81) — xác nhận qua get_equity_orders là do core-10 mua 87 cp SERV @ $5.7199 ($497.63) lúc 14:00 UTC hôm nay, thay thế QBTS sau stop-loss (đã Hogan duyệt lúc ~9:59 ET, đã log đầy đủ ở `trading-log.md`). Đây thuần túy là hiệu ứng timing/pool tiền mặt chung giữa core-10 và sandbox, không phải giao dịch sandbox — không cần push riêng vì Hogan đã duyệt việc này qua core-10 routine.
- "Phần theo dõi" sandbox: dùng baseline buying power đã settle gần nhất trước ảnh hưởng core-10 ($804.81, xác nhận 09:00 ET sáng nay) − $700 đệm = $104.81 cash rảnh + HUT (5×$98.49=$492.45) = **~$597.26** (~85.3% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật cho sandbox, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-13 ~11:09 ET (15:09 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $101.02 vs vốn $98.97 (+2.07%), vs previous close (Fri 07-10) $102.22 (-1.17% trong ngày). So với lần check trước (10:09 ET @ $98.49), biến động +2.57% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale), giá tham khảo $21.02.
- Tài khoản: buying power $307.18 (vẫn thấp — hiệu ứng timing settle core-10 từ SERV/QBTS đã ghi nhận lần check trước, chưa hồi phục), cash $763.90, total_value $5,879.10. Core-10 hiện có thêm SERV (87 cp) xác nhận qua get_equity_positions — khớp ghi nhận trước, không phải sandbox.
- "Phần theo dõi" sandbox: dùng baseline buying power đã settle gần nhất trước ảnh hưởng core-10 ($804.81, xác nhận 07-13 09:00 ET) − $700 đệm = $104.81 cash rảnh + HUT (5×$101.02=$505.10) = **~$609.91** (~87.1% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật cho sandbox, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-13 ~12:08 ET (16:08 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $98.34 vs vốn $98.97 (-0.64%), vs previous close (Fri 07-10) $102.22 (-3.80% trong ngày). So với lần check trước (11:09 ET @ $101.02), biến động -2.65% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale).
- Tài khoản (qua get_portfolio): buying power $307.18 (vẫn thấp, không đổi so với lần check trước — hiệu ứng timing settle core-10 từ SERV/QBTS chưa hồi phục, không phải sandbox), cash $763.90, total_value $5,854.41. Core-10 hiện tại không đổi (AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL, SOUN, SERV) — khớp `trading-log.md`, không có mã lạ.
- "Phần theo dõi" sandbox: dùng baseline buying power đã settle gần nhất trước ảnh hưởng core-10 ($804.81, xác nhận 07-13 09:00 ET) − $700 đệm = $104.81 cash rảnh + HUT (5×$98.34=$491.70) = **~$596.51** (~85.2% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật cho sandbox, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).

## 2026-07-13 ~13:08 ET (17:08 UTC) — Check định kỳ (giữ nguyên HUT)

- Giá HUT hiện $97.95 (last_trade_price 17:07 UTC) vs vốn $98.97 (-1.03%), vs previous close (Fri 07-10) $102.22 (-4.18% trong ngày). So với lần check trước (12:08 ET @ $98.34), biến động -0.40% — dưới ngưỡng 3-5%, không tìm tin tức sâu.
- Vị thế xác nhận qua get_equity_positions: 5 cp HUT giữ nguyên (avg cost $98.97), không có vị thế sandbox nào khác. WULF vẫn ngoài vị thế (cấm mua lại tới ~2026-08-06 do wash-sale). Core-10 không đổi (AMZN, RSP, KO, MSFT, GOOGL, VOO, JNJ, AAPL, SOUN, SERV) — không có mã lạ, không chạm vào.
- Tài khoản (qua get_portfolio): buying power $307.18 (vẫn thấp, không đổi — hiệu ứng timing settle core-10 từ SERV/QBTS chưa hồi phục, không phải sandbox), cash $763.90, total_value $5,849.78.
- "Phần theo dõi" sandbox: dùng baseline buying power đã settle gần nhất trước ảnh hưởng core-10 ($804.81, xác nhận 07-13 09:00 ET) − $700 đệm = $104.81 cash rảnh + HUT (5×$97.95=$489.75) = **~$594.56** (~84.9% mốc gốc $700) — còn rất xa ngưỡng chốt lời $1400 và không gần $0. Không có circuit breaker nào kích hoạt.
- Quyết định: giữ nguyên vị thế, không có lệnh mới. Không gửi push notification (không có hành động/thay đổi thật cho sandbox, theo quy định làm rõ 2026-07-08 trong CLAUDE.md).
