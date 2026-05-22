# A1 Form Lock — Decision Tree (web-service boundary)

根據不同的 Rule Type 決定該 atomic rule 套用哪份 Example Form template。讀 rule line 開頭之類型前綴後直接 map，AI 不另推。

1. Rule line 形如 `Rule: 前置（狀態） - <主詞> 必須 <條件>`：
   1. 套用：`precondition-state.tmpl`。
   2. 語意：測 rule 違反方向（Given 把狀態 setup 成違反條件、Then 操作失敗、And 驗 state 未變）。
2. Rule line 形如 `Rule: 前置（參數） - <參數名> 必須 <條件>`：
   1. 套用：`precondition-param.tmpl`。
   2. 語意：測無效參數值方向（Scenario Outline 包多無效值、Given setup 合法前置實體、When 帶無效參數、Then 操作失敗）。
3. Rule line 形如 `Rule: 後置（回應） - <回應主詞> 應為 <期望值>`：
   1. 套用：`postcondition-response.tmpl`。
   2. 語意：測 rule 滿足方向（Given setup 合法狀態、When 觸發、Then 操作成功、And 驗回應欄位）。
4. Rule line 形如 `Rule: 後置（狀態：<子類>） - <狀態主詞> 應 <狀態變更>`，子類 ∈ {`資料`、`外發`、`資源`、`行為`}：
   1. 套用：`postcondition-state.tmpl`。
   2. 語意：測 rule 滿足方向（Given setup 初始狀態、When 觸發、Then 操作成功、And 驗 state 變更）。
   3. 子類差異目前共用同一份 template；未來若需 per-子類 verify target 差異（資料查 DB / 外發查 inbox / 資源查餘額 / 行為跑兩次）再拆。

殘留路徑：

1. Rule line 不符上述任一前綴 → emit $QUESTIONS：`unknown rule type prefix; rule must use one of {前置（狀態）, 前置（參數）, 後置（回應）, 後置（狀態：*）}`，停在 A1。

2. 同一 atomic rule 出現多重前綴（譬如「前置（狀態）+ 前置（參數）」連寫）→ atomic rule 不夠原子，emit $QUESTIONS 提示 plan 拆 rule。
