"""
Big Animated CLI Timer
- Shows start time
- Shows large elapsed time (big-font)
- Has animated spinner and progress-like bar
- Uses `rich` + `pyfiglet` if available for best visuals
- Falls back to pure-ASCII big digits if not
Run: python big_timer.py
Stop: Ctrl+C
"""

import time
import os
import sys
from datetime import datetime

# Utility: clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Attempt to use rich + pyfiglet for best output
try:
    from rich.console import Console
    from rich.live import Live
    from rich.panel import Panel
    from rich.align import Align
    import pyfiglet
    RICH = True
except Exception:
    RICH = False

# Pure-Python big-digit font (7 rows per digit). Fallback if pyfiglet isn't available.
BIG_DIGITS = {
    "0": [
        " █████ ",
        "██   ██",
        "██  ███",
        "██ █ ██",
        "███  ██",
        "██   ██",
        " █████ ",
    ],
    "1": [
        "  ██   ",
        " ███   ",
        "  ██   ",
        "  ██   ",
        "  ██   ",
        "  ██   ",
        "██████ ",
    ],
    "2": [
        " █████ ",
        "██   ██",
        "     ██",
        "   ███ ",
        "  ██   ",
        " ██    ",
        "███████",
    ],
    "3": [
        " █████ ",
        "██   ██",
        "     ██",
        "  ████ ",
        "     ██",
        "██   ██",
        " █████ ",
    ],
    "4": [
        "    ██ ",
        "   ███ ",
        "  █ ██ ",
        " █  ██ ",
        "███████",
        "    ██ ",
        "    ██ ",
    ],
    "5": [
        "███████",
        "██     ",
        "██████ ",
        "     ██",
        "     ██",
        "██   ██",
        " █████ ",
    ],
    "6": [
        " █████ ",
        "██   ██",
        "██     ",
        "██████ ",
        "██   ██",
        "██   ██",
        " █████ ",
    ],
    "7": [
        "███████",
        "    ██ ",
        "   ██  ",
        "  ██   ",
        " ██    ",
        " ██    ",
        " ██    ",
    ],
    "8": [
        " █████ ",
        "██   ██",
        "██   ██",
        " █████ ",
        "██   ██",
        "██   ██",
        " █████ ",
    ],
    "9": [
        " █████ ",
        "██   ██",
        "██   ██",
        " ██████",
        "     ██",
        "██   ██",
        " █████ ",
    ],
    ":": [
        "   ",
        " ██",
        " ██",
        "   ",
        " ██",
        " ██",
        "   ",
    ],
    " ": ["   "]*7
}


def render_big_ascii_fallback(text):
    """Render large ASCII using BIG_DIGITS mapping."""
    lines = [""] * 7
    for ch in text:
        ch = ch if ch in BIG_DIGITS else " "
        seg = BIG_DIGITS[ch]
        for i in range(7):
            # add spacing between digits
            lines[i] += seg[i] + "  "
    return "\n".join(lines)


def format_elapsed(elapsed: float):
    secs = int(elapsed)
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return hours, minutes, seconds


def two(x):
    return f"{x:02d}"


def run_rich_mode():
    console = Console()
    start = datetime.now()
    spinner_chars = ["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈"]
    spin_i = 0

    with Live(console=console, refresh_per_second=10) as live:
        try:
            while True:
                now = datetime.now()
                elapsed = (now - start).total_seconds()
                h, m, s = format_elapsed(elapsed)
                hhmmss = f"{two(h)}:{two(m)}:{two(s)}"

                # big text via pyfiglet
                try:
                    big = pyfiglet.figlet_format(hhmmss, font="big")
                except Exception:
                    # fallback to our ascii
                    big = render_big_ascii_fallback(hhmmss)

                # spinner + progress-like visualization using seconds within minute
                pct = (s / 60)
                bar_width = 30
                filled = int(pct * bar_width)
                bar = "█" * filled + "-" * (bar_width - filled)
                spinner = spinner_chars[spin_i % len(spinner_chars)]
                spin_i += 1

                left_panel = Panel.fit(
                    Align.center(big, vertical="middle"),
                    title=f"Started: {start.strftime('%Y-%m-%d %H:%M:%S')}",
                    subtitle=f"[bold]Elapsed[/bold] {hhmmss}  {spinner}",
                    padding=(1, 2),
                )

                right_text = (
                    f"[b]Current:[/b] {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                    f"[b]Progress (minute):[/b]\n[{bar}]\n\n"
                    f"Press CTRL+C to stop"
                )

                right_panel = Panel.fit(right_text, title="Status", padding=(1, 2))
                # assemble
                from rich.table import Table
                table = Table.grid(expand=True)
                table.add_column(ratio=3)
                table.add_column(ratio=1)
                table.add_row(left_panel, right_panel)

                live.update(table)
                time.sleep(0.2)
        except KeyboardInterrupt:
            console.print("\n[b red]Timer stopped.[/b red] Bye.")


def run_fallback_mode():
    start = datetime.now()
    spinner = ["|", "/", "-", "\\"]
    spin_i = 0
    try:
        while True:
            now = datetime.now()
            elapsed = (now - start).total_seconds()
            h, m, s = format_elapsed(elapsed)
            hhmmss = f"{two(h)}:{two(m)}:{two(s)}"

            # big ascii
            try:
                # try figlet if present in sys.modules (but this branch is for fallback, so likely not)
                import pyfiglet as _pf
                big = _pf.figlet_format(hhmmss, font="big")
            except Exception:
                big = render_big_ascii_fallback(hhmmss)

            # progress bar based on seconds
            pct = (s / 60)
            bar_width = 40
            filled = int(pct * bar_width)
            bar = "█" * filled + "-" * (bar_width - filled)
            spin_char = spinner[spin_i % len(spinner)]
            spin_i += 1

            clear()
            print("="*80)
            print(" " * 20 + "🕒  BIG CLI TIMER")
            print("="*80)
            print(f"Started : {start.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Now     : {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-"*80)
            print(big)
            print("-"*80)
            print(f"[{bar}]  {two(h)}h {two(m)}m {two(s)}s   {spin_char}")
            print("-"*80)
            print("Press CTRL+C to stop")
            # update fast enough for animation
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nTimer stopped. Bye.")


def main():
    clear()
    print("Starting big animated CLI timer...")
    time.sleep(0.5)
    if RICH:
        try:
            run_rich_mode()
            return
        except Exception:
            # if something in rich mode breaks, fallback
            pass
    # fallback mode:
    run_fallback_mode()


if __name__ == "__main__":
    main()
