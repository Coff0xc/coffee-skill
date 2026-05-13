# coffee-skill 日本語リファレンス

## これは何か

`coffee-skill` は Codex 用のスキルパックです。ソフトウェア開発、AI Agent/RAG、API とデータ設計、UI と文書出力、防御的セキュリティ、検知、インシデント対応、脆弱性管理を扱います。

## なぜ作ったのか

- 小さなスキルが多すぎると、自動トリガーが不安定になります。
- 多くのクライアントは `SKILL.md` の frontmatter `name` と `description` を主に見てスキルを選びます。
- セキュリティ作業には、認可範囲と防御目的の境界が必要です。
- 実務では助言だけでなく、検証可能な手順が必要です。

## 何が良いのか

- 87 個の元スキルを 15 個の包括的な能力スキルに整理しています。
- `coff0xc-skill-router` が、自動トリガー失敗時のフォールバックになります。
- 各スキルに適用範囲、非適用範囲、能力マトリクス、作業段階、証拠レベル、ハードゲート、検証チェック、アンチパターンがあります。
- セキュリティ内容は、認可された防御、検知、強化、検証、報告に限定しています。

## 使い方

自然に依頼できます:

```text
Use coff0xc-ai-agent-rag to design a RAG Agent.
Use coff0xc-secure-code-appsec to review this project.
Use coff0xc-cloud-devsecops to review Kubernetes and CI/CD risk.
```

自動トリガーされない場合:

```text
Use coff0xc-skill-router to choose the right skill.
```

## どこで使えるか

- ローカルの Codex スキルディレクトリ。
- `SKILL.md` フォルダー形式を読み込める互換クライアント。
- 開発、AI システム、文書化、防御的セキュリティ、検知、脆弱性管理。

## トリガー失敗時

1. フォルダー名と frontmatter `name` が一致していることを確認します。
2. コピー後に Codex を再起動または更新します。
3. 重複したスキル名を削除します。
4. `coff0xc-skill-router` を明示的に呼び出します。

## セキュリティ境界

所有または明示的に認可された資産、コード、ログ、サンプル、ラボ、訓練環境に限定してください。未認可アクセス、認証情報の窃取、永続化、回避、C2、フィッシング収集、データ持ち出し、破壊行為には使わないでください。
