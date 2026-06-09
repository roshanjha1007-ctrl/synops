"""
Lucide icon helpers for Streamlit HTML blocks.
"""

from html import escape


def lucide_icon(name: str, size: int = 16, color: str = "currentColor") -> str:
    """Return a Lucide SVG string, or an empty string if the package is missing."""
    try:
        from lucide import lucide_icon as render_lucide
    except Exception:
        return ""

    try:
        svg = render_lucide(name, size=size, color=color, stroke_width=2)
    except TypeError:
        svg = render_lucide(name)

    if not isinstance(svg, str) or "<svg" not in svg:
        return ""

    if "width=" not in svg:
        svg = svg.replace("<svg", f'<svg width="{size}" height="{size}"', 1)
    if "color=" not in svg and "stroke=" not in svg:
        svg = svg.replace("<svg", f'<svg stroke="{escape(color)}"', 1)

    return svg.replace("<svg", '<svg aria-hidden="true" focusable="false"', 1)


def icon_label(icon_name: str, label: str, color: str = "currentColor", size: int = 16) -> str:
    """Render a compact icon + label row for HTML injected via st.markdown."""
    icon = lucide_icon(icon_name, size=size, color=color)
    gap = "6px" if icon else "0"
    return (
        f'<span style="display:inline-flex;align-items:center;gap:{gap};">'
        f"{icon}<span>{escape(label)}</span></span>"
    )
