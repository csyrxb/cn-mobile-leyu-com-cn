# tools/site_summary.py
# Generates a structured summary for a given site configuration

SITE_DATA = {
    "main_portal": {
        "url": "https://cn-mobile-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育赛事", "在线平台"],
        "tags": ["娱乐", "体育", "直播"],
        "description": "综合性体育娱乐门户，提供赛事直播与互动服务。"
    },
    "support_page": {
        "url": "https://cn-mobile-leyu.com.cn/support",
        "keywords": ["客服", "帮助中心", "用户指南"],
        "tags": ["支持", "FAQ"],
        "description": "用户帮助与常见问题解答页面。"
    },
    "news_section": {
        "url": "https://cn-mobile-leyu.com.cn/news",
        "keywords": ["体育新闻", "赛事资讯", "最新动态"],
        "tags": ["新闻", "资讯"],
        "description": "发布最新体育赛事新闻和平台动态。"
    }
}


def generate_summary(site_name: str, site_info: dict) -> dict:
    """Generate a structured summary for a single site entry."""
    summary = {
        "site_name": site_name,
        "url": site_info["url"],
        "keywords": ", ".join(site_info["keywords"]),
        "tags": site_info["tags"],
        "description": site_info["description"],
        "tag_count": len(site_info["tags"]),
        "keyword_count": len(site_info["keywords"])
    }
    return summary


def format_summary_text(summary: dict) -> str:
    """Format a summary dict into a readable text block."""
    lines = [
        f"Site: {summary['site_name']}",
        f"URL: {summary['url']}",
        f"Description: {summary['description']}",
        f"Keywords: {summary['keywords']}",
        f"Tags: {' | '.join(summary['tags'])}",
        f"Tags Count: {summary['tag_count']}",
        f"Keywords Count: {summary['keyword_count']}",
        "-" * 40
    ]
    return "\n".join(lines)


def list_all_sites(data: dict) -> list:
    """Return list of all site names from config."""
    return list(data.keys())


def generate_site_report(data: dict) -> str:
    """Generate complete report for all configured sites."""
    site_names = list_all_sites(data)
    report_parts = []
    for name in site_names:
        summ = generate_summary(name, data[name])
        report_parts.append(format_summary_text(summ))
    return "\n".join(report_parts)


def export_summary_to_dict(data: dict) -> list:
    """Export all site summaries as a list of dictionaries."""
    return [generate_summary(name, info) for name, info in data.items()]


def main():
    """Main entry point: print structured summaries."""
    report = generate_site_report(SITE_DATA)
    print("=== Site Summary Report ===\n")
    print(report)
    print("\n=== JSON-like Export Preview ===")
    summaries = export_summary_to_dict(SITE_DATA)
    for item in summaries:
        print(f"  - {item['site_name']}: {item['url']} | tags: {item['tag_count']}")


if __name__ == "__main__":
    main()