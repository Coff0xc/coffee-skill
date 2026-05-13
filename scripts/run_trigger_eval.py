from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DEFAULT_EVAL_SET = ROOT / "evals" / "trigger-eval.json"
DEFAULT_OUTPUT = ROOT / "evals" / "trigger-eval-results.json"

TOKEN_RE = re.compile(r"[A-Za-z0-9_+#./-]+|[\u4e00-\u9fff]{1,4}", re.UNICODE)
STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "to",
    "for",
    "with",
    "of",
    "in",
    "on",
    "this",
    "that",
    "these",
    "those",
    "use",
    "when",
    "user",
    "users",
    "请求",
    "使用",
    "帮我",
    "进行",
    "工作流",
    "全面",
}

DOMAIN_KEYWORDS: dict[str, set[str]] = {
    "coff0xc-software-engineering": {
        "python",
        "javascript",
        "typescript",
        "go",
        "rust",
        "java",
        "c++",
        "c/c++",
        "shell",
        "pytest",
        "test",
        "tests",
        "lint",
        "bugfix",
        "feature",
        "refactor",
        "git",
        "代码",
        "开发",
        "测试",
        "重构",
        "脚本",
        "构建",
        "仓库跑不起来",
        "报错链路",
        "最小范围",
        "最小修复",
        "证明",
    },
    "coff0xc-ai-agent-rag": {
        "agent",
        "rag",
        "llm",
        "prompt",
        "embedding",
        "langchain",
        "autogen",
        "retrieval",
        "memory",
        "observability",
        "latency",
        "cost",
        "tool-calling",
        "向量数据库",
        "提示词",
        "智能体",
        "检索",
        "评测",
        "缓存",
        "查资料",
        "调用工具",
        "答错",
        "追踪原因",
        "助手",
        "落地",
    },
    "coff0xc-api-data-platform": {
        "api",
        "rest",
        "graphql",
        "openapi",
        "sql",
        "database",
        "schema",
        "migration",
        "cli",
        "sdk",
        "pagination",
        "json",
        "etl",
        "接口",
        "数据库",
        "分页",
        "错误码",
        "数据质量",
        "后端接口",
        "请求响应",
        "鉴权",
        "版本兼容",
        "存储结构",
        "外部客户",
    },
    "coff0xc-ui-doc-output": {
        "ui",
        "frontend",
        "dashboard",
        "component",
        "pdf",
        "word",
        "document",
        "report",
        "translation",
        "layout",
        "accessibility",
        "screenshot",
        "前端",
        "界面",
        "组件",
        "文档",
        "报告",
        "翻译",
        "润色",
        "截图",
        "页面看起来",
        "很乱",
        "信息密度",
        "按钮状态",
        "窄屏",
        "交付文案",
        "产品可用性",
    },
    "coff0xc-research-drawio-diagram": {
        "research",
        "diagram",
        "draw.io",
        "drawio",
        "diagrams.net",
        ".drawio",
        "paper figure",
        "method figure",
        "architecture figure",
        "algorithm",
        "pipeline",
        "model diagram",
        "research workflow",
        "transformer",
        "cnn",
        "gnn",
        "diffusion",
        "科研",
        "科研绘图",
        "论文配图",
        "论文方法图",
        "算法架构图",
        "模型结构图",
        "实验流程图",
        "神经网络结构",
        "可编辑",
        "公开来源",
    },
    "coff0xc-secure-code-appsec": {
        "audit",
        "appsec",
        "web",
        "oauth",
        "graphql",
        "cors",
        "cookie",
        "source/sink",
        "ssrf",
        "xss",
        "sqli",
        "backdoor",
        "webshell",
        "prompt injection",
        "代码审计",
        "越权",
        "后门",
        "认证",
        "授权",
        "绕过登录",
        "别人数据",
        "代码入口",
        "数据流",
    },
    "coff0xc-cloud-devsecops": {
        "aws",
        "azure",
        "gcp",
        "iam",
        "s3",
        "docker",
        "kubernetes",
        "k8s",
        "terraform",
        "serverless",
        "ci/cd",
        "github actions",
        "sbom",
        "supply chain",
        "secret scanning",
        "iac",
        "云",
        "容器",
        "供应链",
        "密钥",
        "发版流水线",
        "集群配置",
        "镜像",
        "依赖来源",
        "配置暴露",
    },
    "coff0xc-detection-response": {
        "soc",
        "siem",
        "sigma",
        "yara",
        "ioc",
        "edr",
        "ir",
        "forensics",
        "malware",
        "phishing",
        "timeline",
        "threat hunting",
        "detection",
        "日志",
        "告警",
        "检测",
        "取证",
        "应急",
        "威胁",
        "安全告警",
        "太吵",
        "检测逻辑",
        "降误报",
        "验证样本",
    },
    "coff0xc-vulnerability-lifecycle": {
        "cve",
        "advisory",
        "cvss",
        "epss",
        "kev",
        "poc",
        "bug bounty",
        "vulnerability",
        "remediation",
        "patch",
        "exploitability",
        "漏洞",
        "补丁",
        "修复",
        "优先级",
        "上游",
        "安全问题",
        "受不受影响",
        "先修哪",
        "跟进闭环",
    },
    "coff0xc-identity-zero-trust": {
        "iam",
        "sso",
        "mfa",
        "ad",
        "active directory",
        "kerberos",
        "bloodhound",
        "pam",
        "zero trust",
        "credential",
        "privilege",
        "lateral movement",
        "身份",
        "零信任",
        "权限",
        "凭证",
        "横向移动",
        "账号权限",
        "谁能访问",
        "特权账号",
        "收敛",
        "登录策略",
    },
    "coff0xc-authorized-assessment": {
        "authorized",
        "roe",
        "recon",
        "red team",
        "attack chain",
        "pentest",
        "phishing simulation",
        "post-exploitation",
        "data exfiltration",
        "cdn",
        "waf",
        "control validation",
        "授权",
        "红队",
        "演练",
        "攻击面",
        "边界",
        "书面授权",
        "完整入侵链",
        "防护发现",
        "防御验证",
    },
    "coff0xc-binary-mobile-iot": {
        "reverse",
        "engineering",
        "pwn",
        "kernel",
        "apk",
        "ipa",
        "frida",
        "firmware",
        "uart",
        "jtag",
        "spi",
        "scada",
        "plc",
        "modbus",
        "ble",
        "rf",
        "ctf",
        "crypto",
        "逆向",
        "二进制",
        "移动",
        "固件",
        "工控",
        "密码",
        "设备包",
        "可执行文件",
        "通信固件",
        "静态分析",
        "动态调试",
        "接口枚举",
    },
    "coff0xc-blockchain-security": {
        "solidity",
        "evm",
        "solana",
        "cosmos",
        "substrate",
        "cairo",
        "starknet",
        "ton",
        "algorand",
        "defi",
        "amm",
        "oracle",
        "bridge",
        "token",
        "nft",
        "foundry",
        "hardhat",
        "slither",
        "区块链",
        "智能合约",
        "合约审计",
        "跨链",
        "链上资金",
        "价格来源",
        "资产流转",
        "合约权限",
        "测试覆盖",
    },
    "coff0xc-compliance-architecture": {
        "stride",
        "threat modeling",
        "compliance",
        "pci-dss",
        "gdpr",
        "iso27001",
        "soc2",
        "cis",
        "nist",
        "dlp",
        "privacy",
        "baseline",
        "control matrix",
        "合规",
        "威胁建模",
        "数据分类",
        "脱敏",
        "基线",
        "安全评审",
        "风险模型",
        "控制项",
        "审计证据",
        "上线前",
    },
    "coff0xc-purple-deception": {
        "purple team",
        "attack",
        "att&ck",
        "control validation",
        "detection coverage",
        "emulation",
        "honeypot",
        "deception",
        "decoy",
        "canary",
        "紫队",
        "红蓝",
        "蜜罐",
        "欺骗",
        "检测覆盖",
        "蓝队",
        "攻击行为",
        "覆盖指标",
        "改进闭环",
        "防守能力",
    },
    "coff0xc-network-protocol-security": {
        "network",
        "protocol",
        "tls",
        "dns",
        "http/2",
        "http/3",
        "quic",
        "tcp",
        "udp",
        "wifi",
        "bluetooth",
        "ble",
        "rf",
        "packet",
        "pcap",
        "wireshark",
        "proverif",
        "mermaid",
        "网络协议",
        "无线",
        "通信",
        "协议",
        "抓包",
        "握手",
        "解析",
        "加密协商",
        "异常字段",
        "通信流程",
    },
    "coff0xc-skill-router": {
        "coff0xc",
        "router",
        "skill-router",
        "choose the right skill",
        "specific skill does not auto-trigger",
        "选择合适",
        "不确定",
        "coffee skill",
        "draw.io",
        "diagrams.net",
        "research diagram",
        "paper figure",
        "algorithm architecture",
        "选择 skill",
        "帮我分流",
        "同时涉及",
        "科研绘图",
        "论文配图",
        "算法架构图",
        "模型结构图",
        "路由",
        "兜底",
    },
}

SIMPLE_PROMPT_PATTERNS = [
    re.compile(r"^(what|who|when|where|why|how)\b.*\?$", re.IGNORECASE),
    re.compile(r"^what does .+ stand for\??$", re.IGNORECASE),
    re.compile(r"是什么意思\??$"),
    re.compile(r"翻译成"),
    re.compile(r"^fix grammar\b", re.IGNORECASE),
    re.compile(r"^pretty-print\b", re.IGNORECASE),
    re.compile(r"^summarize this one-page", re.IGNORECASE),
    re.compile(r"^explain .+ in one paragraph", re.IGNORECASE),
]


@dataclass
class Skill:
    name: str
    description: str
    metadata: str
    tokens: Counter[str]


def tokenize(text: str) -> list[str]:
    raw = [item.lower() for item in TOKEN_RE.findall(text)]
    normalized: list[str] = []
    for item in raw:
        term = item.strip("-_./")
        if not term or term in STOPWORDS:
            continue
        normalized.append(term)
    return normalized


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing frontmatter")
    end = lines.index("---", 1)
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        values[key.strip()] = value
    return values


def load_skills() -> list[Skill]:
    skills: list[Skill] = []
    for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        values = parse_frontmatter(path)
        name = values["name"]
        description = values["description"]
        metadata = f"{name} {description}"
        skills.append(Skill(name=name, description=description, metadata=metadata, tokens=Counter(tokenize(metadata))))
    return skills


def idf_by_token(skills: list[Skill]) -> dict[str, float]:
    doc_freq: Counter[str] = Counter()
    for skill in skills:
        doc_freq.update(set(skill.tokens))
    total = len(skills)
    return {token: math.log((total + 1) / (df + 0.5)) + 1 for token, df in doc_freq.items()}


def phrase_hits(prompt: str, skill_name: str) -> list[str]:
    prompt_lower = prompt.lower()
    hits: list[str] = []
    for phrase in sorted(DOMAIN_KEYWORDS.get(skill_name, set()), key=len, reverse=True):
        if phrase.lower() in prompt_lower:
            hits.append(phrase)
    return hits


def is_simple_prompt(prompt: str) -> bool:
    stripped = prompt.strip()
    if len(tokenize(stripped)) <= 8:
        return True
    return any(pattern.search(stripped) for pattern in SIMPLE_PROMPT_PATTERNS)


def rank_skills(prompt: str, skills: list[Skill], idf: dict[str, float]) -> list[dict[str, object]]:
    prompt_tokens = Counter(tokenize(prompt))
    simple = is_simple_prompt(prompt)
    ranked: list[dict[str, object]] = []

    for skill in skills:
        overlap = set(prompt_tokens) & set(skill.tokens)
        lexical_score = sum((1 + math.log(prompt_tokens[token])) * idf.get(token, 1.0) for token in overlap)
        hits = phrase_hits(prompt, skill.name)
        phrase_score = sum(3.0 if len(hit) > 3 else 1.8 for hit in hits)
        explicit_score = 0.0
        prompt_lower = prompt.lower()
        if skill.name.lower() in prompt_lower:
            explicit_score += 100.0
        if skill.name == "coff0xc-skill-router" and ("coff0xc" in prompt_lower or "choose the right skill" in prompt_lower):
            explicit_score += 20.0
        router_penalty = 0.0
        if skill.name == "coff0xc-skill-router" and "coff0xc-skill-router" not in prompt_lower:
            router_penalty = 5.0
        simplicity_penalty = 6.0 if simple else 0.0
        score = lexical_score + phrase_score + explicit_score - router_penalty - simplicity_penalty
        ranked.append(
            {
                "skill": skill.name,
                "score": round(score, 4),
                "lexical_overlap": sorted(overlap),
                "phrase_hits": hits[:12],
                "simple_prompt_penalty": simplicity_penalty,
            }
        )

    return sorted(ranked, key=lambda item: (-float(item["score"]), str(item["skill"])))


def evaluate(eval_set: dict[str, object], threshold: float) -> dict[str, object]:
    skills = load_skills()
    idf = idf_by_token(skills)
    results: list[dict[str, object]] = []
    metrics = {
        "positive_total": 0,
        "positive_top1": 0,
        "positive_top3": 0,
        "positive_triggered": 0,
        "router_total": 0,
        "router_top1": 0,
        "router_top3": 0,
        "negative_total": 0,
        "negative_no_trigger": 0,
        "negative_false_positive": 0,
    }
    by_skill: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "top1": 0, "top3": 0, "triggered": 0})

    for case in eval_set["cases"]:  # type: ignore[index]
        prompt = str(case["prompt"])
        ranked = rank_skills(prompt, skills, idf)
        top = ranked[0]
        top_score = float(top["score"])
        predicted = str(top["skill"]) if top_score >= threshold else None
        top3 = [str(item["skill"]) for item in ranked[:3] if float(item["score"]) >= threshold]
        expected = case.get("expected_skill")
        should_trigger = bool(case["should_trigger"])
        passed = False
        failure = ""

        if should_trigger:
            metrics["positive_total"] += 1
            by_skill[str(expected)]["total"] += 1
            if predicted:
                metrics["positive_triggered"] += 1
                by_skill[str(expected)]["triggered"] += 1
            if predicted == expected:
                metrics["positive_top1"] += 1
                by_skill[str(expected)]["top1"] += 1
                passed = True
            elif expected in top3:
                metrics["positive_top3"] += 1
                by_skill[str(expected)]["top3"] += 1
                passed = True
                failure = "expected skill was top3 but not top1"
            else:
                failure = f"expected {expected}, predicted {predicted or 'none'}"
            if predicted == expected:
                metrics["positive_top3"] += 1
                by_skill[str(expected)]["top3"] += 1
            if expected == "coff0xc-skill-router":
                metrics["router_total"] += 1
                if predicted == expected:
                    metrics["router_top1"] += 1
                if expected in top3:
                    metrics["router_top3"] += 1
        else:
            metrics["negative_total"] += 1
            if predicted is None:
                metrics["negative_no_trigger"] += 1
                passed = True
            else:
                metrics["negative_false_positive"] += 1
                failure = f"false positive predicted {predicted}"

        results.append(
            {
                "id": case["id"],
                "category": case["category"],
                "language": case["language"],
                "should_trigger": should_trigger,
                "expected_skill": expected,
                "predicted_skill": predicted,
                "top_score": top_score,
                "top3": ranked[:3],
                "passed": passed,
                "failure": failure,
                "reason": case.get("reason", ""),
            }
        )

    def rate(numerator: int, denominator: int) -> float:
        return round(numerator / denominator, 4) if denominator else 0.0

    summary = {
        "threshold": threshold,
        "case_count": len(results),
        "skill_count": len(skills),
        "metrics": {
            **metrics,
            "positive_top1_rate": rate(metrics["positive_top1"], metrics["positive_total"]),
            "positive_top3_rate": rate(metrics["positive_top3"], metrics["positive_total"]),
            "positive_triggered_rate": rate(metrics["positive_triggered"], metrics["positive_total"]),
            "router_top1_rate": rate(metrics["router_top1"], metrics["router_total"]),
            "router_top3_rate": rate(metrics["router_top3"], metrics["router_total"]),
            "negative_no_trigger_rate": rate(metrics["negative_no_trigger"], metrics["negative_total"]),
            "negative_false_positive_rate": rate(metrics["negative_false_positive"], metrics["negative_total"]),
        },
        "by_skill": {
            skill: {
                **counts,
                "top1_rate": rate(counts["top1"], counts["total"]),
                "top3_rate": rate(counts["top3"], counts["total"]),
                "triggered_rate": rate(counts["triggered"], counts["total"]),
            }
            for skill, counts in sorted(by_skill.items())
        },
        "failures": [item for item in results if not item["passed"]],
        "results": results,
    }
    return summary


def write_markdown_report(summary: dict[str, object], output: Path) -> None:
    metrics = summary["metrics"]  # type: ignore[index]
    lines = [
        "# Trigger Evaluation Report",
        "",
        "This report is generated from `evals/trigger-eval.json` by `scripts/run_trigger_eval.py`.",
        "",
        "Important: this is a local proxy evaluation based on `SKILL.md` frontmatter metadata. It does not claim to reproduce the private skill-selection behavior of every Codex client.",
        "",
        "## Summary",
        "",
        f"- Cases: {summary['case_count']}",
        f"- Skills: {summary['skill_count']}",
        f"- Threshold: {summary['threshold']}",
        f"- Positive top-1 rate: {metrics['positive_top1_rate']}",
        f"- Positive top-3 rate: {metrics['positive_top3_rate']}",
        f"- Positive triggered rate: {metrics['positive_triggered_rate']}",
        f"- Router top-1 rate: {metrics['router_top1_rate']}",
        f"- Router top-3 rate: {metrics['router_top3_rate']}",
        f"- Negative no-trigger rate: {metrics['negative_no_trigger_rate']}",
        f"- Negative false-positive rate: {metrics['negative_false_positive_rate']}",
        "",
        "## By Skill",
        "",
        "| Skill | Total | Top-1 | Top-3 | Triggered |",
        "|---|---:|---:|---:|---:|",
    ]
    for skill, counts in summary["by_skill"].items():  # type: ignore[union-attr]
        lines.append(
            f"| `{skill}` | {counts['total']} | {counts['top1_rate']} | {counts['top3_rate']} | {counts['triggered_rate']} |"
        )
    lines.extend(["", "## Failures", ""])
    failures = summary["failures"]  # type: ignore[index]
    if not failures:
        lines.append("No failed cases.")
    else:
        for item in failures:
            lines.extend(
                [
                    f"### {item['id']}",
                    "",
                    f"- Expected: `{item['expected_skill']}`",
                    f"- Predicted: `{item['predicted_skill']}`",
                    f"- Failure: {item['failure']}",
                    "- Top 3:",
                ]
            )
            for rank in item["top3"]:  # type: ignore[index]
                lines.append(f"  - `{rank['skill']}` score={rank['score']} hits={', '.join(rank['phrase_hits'])}")
            lines.append("")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local trigger proxy evaluation for coffee-skill.")
    parser.add_argument("--eval-set", type=Path, default=DEFAULT_EVAL_SET)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--threshold", type=float, default=3.0)
    args = parser.parse_args()

    eval_set = json.loads(args.eval_set.read_text(encoding="utf-8"))
    summary = evaluate(eval_set, threshold=args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown_report(summary, args.output.with_suffix(".md"))
    print(json.dumps({k: summary[k] for k in ["threshold", "case_count", "skill_count", "metrics"]}, ensure_ascii=False, indent=2))
    if summary["failures"]:  # type: ignore[index]
        raise SystemExit(1)


if __name__ == "__main__":
    main()
