---
name: aibdd-core
description: 跨 skill 共用 reference hub。包含 report contract、authentication binding、spec package paths、feature granularity 等共用 reference。LOAD-only — 由其他 sibling skill 透過 `aibdd-core::FILENAME.md` 載入；禁止重抄內容至自身 references。SKIP when caller 試圖直接 invoke 本 skill 而非 LOAD reference 檔。
metadata:
  user-invocable: false
  skill-type: reference-hub
  source: project-level dogfooding
---

# aibdd-core

跨 skill 共用 reference hub — LOAD-only，不執行任何流程。Sibling skill 透過 `aibdd-core::FILENAME.md` 形式 LOAD references；禁止複製本檔內容至自身 references/。

## §1 REFERENCES（Hub Exports）

下表是 sibling skill 透過 `aibdd-core::FILENAME.md` 可載入的 reference manifest。新增 / 移動 reference 必同步更新此表（YAML 區塊供 analyzer 機械審計，table 供人類閱讀）。

```yaml
references:
  - path: references/report-contract.md
    purpose: Planner 匯報格式 + user-facing message style
  - path: references/authentication-binding.md
    purpose: Actor key 為 authentication prerequisite 的跨 skill 慣例
  - path: references/spec-package-paths.md
    purpose: spec 路徑慣例 SSOT（boundary-aware）
  - path: references/feature-granularity.md
    purpose: feature 粒度 anti-pattern token + 命名規範
  - path: references/filename-axes-convention/nn-prefix-then-title.md
    purpose: NN-title 命名軸 SSOT
  - path: references/gherkin-rule-body-prefix-policy/four-rules-prefix.md
    purpose: Rule body 四種 prefix 寫作規範
  - path: references/preset-contract/web-backend.md
    purpose: web-backend boundary preset 規章
  - path: references/i18n/en-us.md
    purpose: en-US locale prose 慣例
  - path: references/i18n/ja-jp.md
    purpose: ja-JP locale prose 慣例
  - path: references/i18n/ko-kr.md
    purpose: ko-KR locale prose 慣例
  - path: references/i18n/zh-hans.md
    purpose: zh-Hans locale prose 慣例
  - path: references/i18n/zh-hant.md
    purpose: zh-Hant locale prose 慣例
```

| ID | Path | Phase scope | Purpose |
|---|---|---|---|
| R1 | `references/report-contract.md` | global | Planner 匯報格式、user-facing message style、scope 欄位慣例 |
| R2 | `references/authentication-binding.md` | global | Actor key 作為 authentication prerequisite 的跨 skill 共用慣例 |
| R3 | `references/spec-package-paths.md` | global | spec 路徑慣例 SSOT — kickoff boundary-aware（`arguments.yml` + `boundary.yml` 解析） |
| R4 | `references/feature-granularity.md` | global | feature 粒度 anti-pattern token 篩檢 + 命名規範（`/aibdd-form-feature-spec` 寫檔守門用）|
| R5 | `references/filename-axes-convention/nn-prefix-then-title.md` | global | spec package 與 feature 檔的 `NN-title` 命名軸 SSOT |
| R6 | `references/gherkin-rule-body-prefix-policy/four-rules-prefix.md` | global | Rule body 四種 prefix（must/should/shall/may）寫作規範 |
| R7 | `references/preset-contract/web-backend.md` | global | `web-backend` boundary preset 規章（step-classification / plugin-contract / handlers / variants 對應） |
| R8 | `references/i18n/en-us.md` | global | en-US locale prose 慣例 |
| R9 | `references/i18n/ja-jp.md` | global | ja-JP locale prose 慣例 |
| R10 | `references/i18n/ko-kr.md` | global | ko-KR locale prose 慣例 |
| R11 | `references/i18n/zh-hans.md` | global | zh-Hans locale prose 慣例 |
| R12 | `references/i18n/zh-hant.md` | global | zh-Hant locale prose 慣例 |

## §2 ASSETS（Hub Exports）

| Path | Purpose |
|---|---|
| `assets/boundaries/` | Boundary preset SSOT — `<preset.name>/{step-classification.yml, plugin-contract.md, handlers/, variants/, shared-dsl-template.yml, scripts/part_to_dsl.py}`；`/aibdd-red` 透過此處解析 preset assets |

## §4 CROSS-REFERENCES

- `/aibdd-discovery`、`/aibdd-form-activity`、`/aibdd-form-feature-spec`、`/aibdd-plan`、legacy `/speckit.aibdd.bdd-analyze`、legacy `/speckit.aibdd.test-plan`、`/clarify-loop` — sibling skills LOAD 本 hub references
