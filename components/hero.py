"""
components/hero.py
Glassmorphism hero banner for rsynops.
"""

import streamlit as st


def render_hero() -> None:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,
            rgba(0,245,255,0.06) 0%,
            rgba(191,90,242,0.06) 50%,
            rgba(0,245,255,0.03) 100%);
        border: 1px solid rgba(0,245,255,0.18);
        border-radius: 20px;
        padding: 48px 40px 40px;
        margin-bottom: 32px;
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    ">
        <!-- glow orbs -->
        <div style="
            position:absolute; top:-60px; left:-60px;
            width:220px; height:220px;
            background: radial-gradient(circle, rgba(0,245,255,0.15), transparent 70%);
            border-radius:50%; pointer-events:none;
        "></div>
        <div style="
            position:absolute; bottom:-80px; right:-40px;
            width:280px; height:280px;
            background: radial-gradient(circle, rgba(191,90,242,0.12), transparent 70%);
            border-radius:50%; pointer-events:none;
        "></div>

        <div style="position:relative; z-index:2;">
            <div style="display:flex; align-items:center; gap:14px; margin-bottom:10px;">
                <span style="
                    font-family:'Orbitron',monospace;
                    font-size:0.7rem; font-weight:700;
                    letter-spacing:.18em; text-transform:uppercase;
                    color:#00f5ff;
                    background: rgba(0,245,255,0.1);
                    border: 1px solid rgba(0,245,255,0.3);
                    padding: 4px 12px; border-radius:20px;
                ">Hackathon 2025</span>
                <span style="
                    font-family:'Space Mono',monospace;
                    font-size:0.68rem; color:#bf5af2;
                    background: rgba(191,90,242,0.1);
                    border: 1px solid rgba(191,90,242,0.3);
                    padding: 4px 12px; border-radius:20px;
                ">MNIST - Energy AI</span>
            </div>

            <h1 style="
                font-family:'Orbitron',monospace;
                font-size:clamp(2rem,4vw,3.4rem);
                font-weight:900;
                background: linear-gradient(90deg, #00f5ff 0%, #bf5af2 60%, #00f5ff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin: 8px 0 6px;
                letter-spacing: .04em;
                line-height: 1.1;
            ">rsynops</h1>

            <p style="
                font-family:'Space Mono',monospace;
                font-size:0.85rem;
                color:#8899aa;
                letter-spacing:.05em;
                margin-bottom: 18px;
            ">ANN vs SNN - Energy-Efficient MNIST Classification</p>

            <p style="
                font-family:'Inter',sans-serif;
                font-size:0.97rem;
                color:#cbd5e1;
                max-width:680px;
                line-height:1.75;
                margin-bottom:24px;
            ">
                Benchmarking <strong style="color:#00f5ff;">Artificial Neural Networks</strong>
                against <strong style="color:#bf5af2;">Spiking Neural Networks</strong> on the
                MNIST digit dataset. We quantify accuracy trade-offs, synaptic operations,
                FLOPs, inference latency, and most critically <em>energy consumption</em>,
                to demonstrate the neuromorphic advantage.
            </p>

            <div style="display:flex; gap:12px; flex-wrap:wrap;">
                <div style="
                    background:rgba(0,245,255,0.07);
                    border:1px solid rgba(0,245,255,0.2);
                    border-radius:10px; padding:10px 18px;
                ">
                    <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#8899aa;letter-spacing:.1em;text-transform:uppercase;">ANN Accuracy</div>
                    <div style="font-family:'Orbitron',monospace;font-size:1.3rem;color:#00f5ff;font-weight:700;">97.5%</div>
                </div>
                <div style="
                    background:rgba(191,90,242,0.07);
                    border:1px solid rgba(191,90,242,0.2);
                    border-radius:10px; padding:10px 18px;
                ">
                    <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#8899aa;letter-spacing:.1em;text-transform:uppercase;">SNN Accuracy</div>
                    <div style="font-family:'Orbitron',monospace;font-size:1.3rem;color:#bf5af2;font-weight:700;">96.8%</div>
                </div>
                <div style="
                    background:rgba(48,209,88,0.07);
                    border:1px solid rgba(48,209,88,0.2);
                    border-radius:10px; padding:10px 18px;
                ">
                    <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#8899aa;letter-spacing:.1em;text-transform:uppercase;">Energy Saved</div>
                    <div style="font-family:'Orbitron',monospace;font-size:1.3rem;color:#30d158;font-weight:700;">83.3%</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
