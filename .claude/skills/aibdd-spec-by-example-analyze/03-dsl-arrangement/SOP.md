銜接之前的 Feature Files 裡面的 `# @dsl` block 跑下列 reasoning SOP：

# 載入上文

1. READ 讀本 block 的 `# rule:` 指向之 selection-criteria markdown。

2. READ 本 block 的 `# handler-candidate-kinds:` union 與 `# candidates:` list。

3. DELEGATE 對每筆 candidate dsl's name (id) 反查 `dsl.cli query` EXTRACT 拿 `format` / `param_bindings` / `datatable_bindings`。
    > TODO python cli command

# 解 rule 之測試需求

1. 從 rule subject + condition 推「該 rule 要驗的欄位 / 參數」。
2. FAITHFUL REASONING: 推 EP 等價類代表值集合。
    READ `rules/equivalence-partition.md` and 推理
3. FAITHFUL REASONING: 推 BVA 邊界值集合（譬如 `> 0` 條件對應 `{-1, 0, 1}`）。
    READ `rules/equivalence-partition.md` and 推理
4. 


# 做完之後的範例
```gherkin
Rule: 前置（狀態） - 商品庫存必須大於 0

    # @test-values
    # field: products.stock
    # predicate-shape: numeric-range (one-sided, valid: > 0)
    # test-direction: failure (前置 - 違反 > 0)
    # ep-classes:
    #   - below-range
    # bva-points:
    #   - min-minus-1
    Example: 庫存違反 >0 時 加入購物車失敗
    # @dsl
    # handler-candidate-kinds: state-builder | operation-invoke | time-control | external-stub
    # rule: ${SKILL_HOME}/aibdd-core/assets/boundaries/web-service/rules/precondition_building.md
    # candidates:
    #   - product.state-builder
    #   - createProduct.operation-invoke
    #   - adjustProductStock.operation-invoke
    # @decision: product.state-builder
    # @rationale: createProduct.operation-invoke 之 OpenAPI minimum=1 reject 邊界值 {-1, 0}；state-builder 無 envelope 限制可讓 B1 灌任意 stock。
    Given 系統中有以下商品：
        | productId | stock   |
        | P1        | <stock> |
    ...
```