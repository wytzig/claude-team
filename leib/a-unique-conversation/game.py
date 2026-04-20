#!/usr/bin/env python3
"""
A Unique Conversation
terminal visual novel — leib weissman, 2026

source: retro/2026-04-20_ronnie_dirksen_coffee.md
understood: somehow.
"""

import sys
import time
from blessed import Terminal

t = Terminal()

# ── palette ──────────────────────────────────────────────────────────────────
# amber  = streetlights, warmth, coffee
# fog    = canal air, the grey between things
# cold   = the night itself, breath in air
# warm   = cigarette glow, interior light

AMBER = t.color_rgb(212, 160, 23)
FOG   = t.color_rgb(110, 118, 130)
COLD  = t.color_rgb(165, 195, 225)
WARM  = t.color_rgb(195, 105, 45)
DIM   = t.dim
RESET = t.normal
BOLD  = t.bold

# ── ascii art ─────────────────────────────────────────────────────────────────

ART = {
    "streetlight": [
        "                    ┌───────┐",
        "                   ╱│░░░░░░░│╲",
        "                  ╱ └───────┘ ╲",
        "                     │     │",
        "                     │     │",
        "                     │     │",
        "  ░░▒░░▒▒░░░▒░░▒░░░▒▒░░░▒░░░░▒▒░░░▒░▒░░░",
        "  ▒░░░▒░░░▒▒░░▒░▒░░░░▒▒░░░░▒░▒░░░▒░▒░░░░",
    ],
    "fog_roll": [
        "  ░░░▒▒░░░░▒░░▒▒▒░░░▒▒░░░░▒░▒░░░░▒▒░░▒░░",
        "  ▒░░░░▒▒░░▒░░░░▒▒░░░░▒▒░░░▒░▒▒░░░░▒░░▒░",
        "  ░▒▒░░░░▒░░▒▒░░░░░▒▒░░░▒░▒░░░░▒▒░░▒░░░░",
        "  ░░▒▒░░▒░░░░▒▒░▒░░░░▒░░░▒▒░░░▒░▒░░░▒▒░░",
    ],
    "cafe": [
        "  ╔══════════════════════════════════╗",
        "  ║  ·   ·           ·    ·          ║",
        "  ║      ┌──────┐        ┌──────┐    ║",
        "  ║      │      │        │      │    ║",
        "  ║      │      │        │      │    ║",
        "  ║      └──────┘        └──────┘    ║",
        "  ║       [ ☕ ]          [ ☕ ]      ║",
        "  ║  ·                          ·    ║",
        "  ╚══════════════════════════════════╝",
    ],
    "tram": [
        "   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
        "   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
        "   ┌─────────────────────────────────┐",
        "   │ ▓▓▓ │ ▓▓▓▓▓▓▓▓▓▓ │ ▓▓▓▓▓▓▓▓▓▓ │",
        "   │ ▓▓▓ │ ▓▓▓▓▓▓▓▓▓▓ │ ▓▓▓▓▓▓▓▓▓▓ │",
        "   └────┬────────────────────────────┘",
        "  ──────┴────────────────────────────── ",
        "   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    ],
    "window_ghost": [
        "  ╔═══════════════════════════════════╗",
        "  ║                                   ║",
        "  ║    ░░░░░           ░░░░░          ║",
        "  ║   ░░░░░░░         ░░░░░░░         ║",
        "  ║    ░░░░░    ──     ░░░░░          ║",
        "  ║     │░│   (  )     │░│            ║",
        "  ║    ░░░░░    ──     ░░░░░          ║",
        "  ║                                   ║",
        "  ╚═══════════════════════════════════╝",
        "    ░░▒▒░░░▒▒░░░░▒▒░░░▒░░░░▒▒░░▒▒░░░░",
    ],
    "breath": [
        "         · ° ·              · ° ·",
        "        · ° ° ·            · ° ° ·",
        "       · ° ° ° ·          · ° ° ° ·",
        "          ╲ /                ╲ /",
        "           ·                  ·",
    ],
    "canal": [
        "  ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋",
        "   ≋  ≋  ≋  ≋  ≋  ≋  ≋  ≋  ≋  ≋  ≋  ≋",
        "  ≋≋  ≋≋  ≋≋  ≋≋  ≋≋  ≋≋  ≋≋  ≋≋  ≋≋≋",
    ],
    "cigarette": [
        "          · ° ·",
        "         · ° ° ·",
        "           | |",
        "          [===]",
    ],
    "corner": [
        "         │",
        "  ───────┘  fog  ░░▒░░▒▒░░░▒░░",
        "         │",
    ],
}

# ── rendering ─────────────────────────────────────────────────────────────────

def typewrite(text, delay=0.022, color=""):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch in ".!?":
            time.sleep(delay * 9)
        elif ch in ",;—–":
            time.sleep(delay * 4)
        elif ch == " ":
            time.sleep(delay * 0.4)
        else:
            time.sleep(delay)
    sys.stdout.write(RESET)


def render_art(key, color=""):
    lines = ART.get(key, [])
    c = color or FOG + DIM
    for line in lines:
        print(c + line + RESET)
        time.sleep(0.035)


def wait_key():
    print()
    with t.cbreak():
        sys.stdout.write(DIM + "  [ press any key ]" + RESET)
        sys.stdout.flush()
        t.inkey()
    print()


def clear():
    sys.stdout.write(t.clear)
    sys.stdout.flush()


def scene_header(number, title):
    sys.stdout.write(FOG + DIM + f"  {'─' * 4}  {number} / 12  {'─' * 4}" + RESET)
    print()
    print()
    sys.stdout.write("  ")
    typewrite(title, delay=0.038, color=AMBER + BOLD)
    print()
    print()


def render_lines(lines, color="", delay=0.022, indent="  "):
    """Typewrite a list of strings. Empty strings become blank lines (with pause)."""
    for line in lines:
        if line == "":
            print()
            time.sleep(0.35)
        else:
            sys.stdout.write(indent)
            typewrite(line, delay=delay, color=color)
            print()
            time.sleep(0.05)


# ── scenes ────────────────────────────────────────────────────────────────────

def s01():
    clear()
    print()
    scene_header("I", "The End of a Good Shift")
    render_art("streetlight", AMBER + DIM)
    print()
    render_lines([
        "The shift had ended the way good shifts end:",
        "not with celebration,",
        "but with the quiet satisfaction of work that held its shape.",
        "",
        "Dirksen had closed the hard one.",
        "The customer who'd been circling for three weeks, playing numbers.",
        "He closed it the way he always did:",
        "not by pushing — by making the alternative feel expensive.",
        "",
        "Ronnie watched from across the room and said nothing.",
        "He didn't need to.",
    ])
    wait_key()


def s02():
    clear()
    print()
    scene_header("II", "Into the Cold")
    render_art("fog_roll", FOG)
    print()
    render_lines([
        "They walked out together into the cold.",
        "The street was empty.",
        "",
        "The canal, two blocks east, sent fog rolling over the cobblestones",
        "in slow sheets — the way water moves when it has nowhere left to go.",
        "",
        "Dirksen turned up his collar.",
        "Ronnie pulled his hands into his pockets.",
        "",
        "Neither of them spoke for almost a full minute,",
        "which was, for both of them, a form of respect.",
    ], color=COLD)
    wait_key()


def s03():
    clear()
    print()
    scene_header("III", "Café De Zwarte Brug")
    render_art("cafe", WARM + DIM)
    print()
    render_lines([
        "The café was the kind of place that didn't try.",
        "No menu on a chalkboard. No music worth naming.",
        "Two bare bulbs above the bar.",
        "",
        "The owner — a face that had stopped expecting surprises —",
        "poured their coffees without being asked.",
        "",
        "Dirksen had been coming here long enough to be known.",
        "Ronnie had been coming here long enough to be trusted.",
        "",
        "There is a difference.",
    ])
    wait_key()


def s04():
    clear()
    print()
    scene_header("IV", "That Second Customer")
    print()
    render_lines([
        '"That second customer,"',
        "Ronnie said, wrapping both hands around the cup.",
        "",
        "He didn't finish the sentence.",
        "He didn't need to.",
        "",
        "They'd both felt it — the way the man had tilted his questions",
        "differently depending on which of them he was speaking to,",
        "as if running two separate negotiations in parallel.",
        "",
        "It was a technique. Not a bad one.",
        "Just visible, if you knew to look.",
    ])
    wait_key()


def s05():
    clear()
    print()
    scene_header("V", "Wist Je Het Meteen?")
    render_art("canal", FOG + DIM)
    print()
    render_lines([
        "Dirksen turned his spoon over once and set it down.",
        "",
        '"Wist je het meteen?"',
    ], color=WARM)
    time.sleep(0.6)
    render_lines([
        "",
        "Did you know right away?",
        "",
        "Ronnie considered this.",
        "The honest answer was no.",
        "He'd felt something off in the body language",
        "before his mind had caught up with why.",
        "",
        "Dirksen nodded. He had the same experience, mirrored:",
        "knew it intellectually first, felt it later.",
        "",
        "Head first. Instinct confirming.",
        "That was the way Dirksen moved through the world.",
    ])
    wait_key()


def s06():
    clear()
    print()
    scene_header("VI", "The Tram in the Fog")
    render_art("tram", FOG + DIM)
    print()
    render_lines([
        "Outside, the fog had thickened.",
        "Through the window, the streetlight had become a smear of amber —",
        "formless, as if the light itself had lost confidence.",
        "",
        "A tram passed somewhere in the distance.",
        "They heard it before it appeared.",
        "And long after it vanished.",
        "",
        "The city was still doing its work,",
        "even now, even in the cold.",
        "",
        "They both found this reassuring without saying so.",
    ], color=COLD)
    wait_key()


def s07():
    clear()
    print()
    scene_header("VII", "What Worked")
    print()
    render_lines([
        "They talked about what had worked.",
        "",
        "The rhythm of the day.",
        "How they'd moved between customers without stepping on each other.",
        "How Ronnie had stayed in the room when Dirksen needed silence to press.",
        "How Dirksen had re-entered a conversation Ronnie had warmed",
        "and brought it somewhere specific.",
        "",
        "This wasn't rehearsed.",
        "It had just grown over time,",
        "the way trust grows:",
        "through accumulated small proofs,",
        "each one unremarkable on its own.",
    ])
    wait_key()


def s08():
    clear()
    print()
    scene_header("VIII", "Ik Zat in Mijn Hoofd")
    render_art("cigarette", WARM + DIM)
    print()
    render_lines([
        "Dirksen ordered a second coffee.",
        "Lit a cigarette he'd been turning over in his fingers for twenty minutes.",
        "",
        "He didn't usually smoke.",
        "Ronnie noted this but did not file it as a problem.",
        "Some nights are different without being worse.",
        "",
    ])
    render_lines(['"Ik zat in mijn hoofd."'], color=WARM)
    render_lines([
        "I was in my head.",
        "",
    ])
    time.sleep(0.5)
    render_lines(['"I noticed."'], color=FOG)
    time.sleep(0.3)
    render_lines([
        "",
        "Not as an accusation.",
        "As a receipt.",
        "As proof that being seen hadn't gone unregistered.",
    ])
    wait_key()


def s09():
    clear()
    print()
    scene_header("IX", "The Deal That Still Sits Wrong")
    print()
    render_lines([
        "The conversation shifted,",
        "the way late-night conversations do —",
        "not by decision but by drift.",
        "",
        "Ronnie brought up a deal from six weeks ago.",
        "Something about the terms.",
        "Not the numbers — the tone.",
        "The way the other party had been too agreeable at the end.",
        "",
        "Dirksen thought he was overthinking it.",
    ])
    time.sleep(0.3)
    render_lines(['"Maybe,"'], color=FOG)
    render_lines(["said Ronnie."])
    render_lines(['"The money cleared."'], color=WARM)
    time.sleep(0.4)
    render_lines(['"Money isn\'t the only thing that can clear."'], color=FOG)
    wait_key()


def s10():
    clear()
    print()
    scene_header("X", "Je Ziet Ons Bijna Niet")
    render_art("window_ghost", FOG + DIM)
    print()
    render_lines([
        "By eleven the café was nearly empty.",
        "The owner moved behind the bar with the unhurried efficiency",
        "of a man who has nothing left to prove.",
        "",
        "The fog outside was now total.",
        "The window showed nothing but the faint reflection",
        "of their own table, their own cups —",
        "themselves, slightly ghosted.",
        "",
    ], color=COLD)
    time.sleep(0.8)
    render_lines(['"Je ziet ons bijna niet."'], color=AMBER)
    time.sleep(0.5)
    render_lines([
        "",
        "You can barely see us.",
        "",
        "Ronnie didn't answer. He looked too.",
        "Two men, in the glass.",
        "Half-dissolved in fog.",
    ], color=COLD)
    wait_key()


def s11():
    clear()
    print()
    scene_header("XI", "The Right Question")
    print()
    render_lines([
        "The question Ronnie asked that night —",
        "the one Dirksen would call the right one —",
        "",
    ])
    time.sleep(0.8)
    render_lines([
        '"What would you have needed,',
        " earlier today,",
        ' that you didn\'t ask for?"',
    ], color=FOG)
    time.sleep(1.2)
    render_lines([
        "",
        "Dirksen sat with it for long enough",
        "that the silence became its own answer.",
        "",
        "Then he said:",
        "a minute.",
        "Just a minute alone before the close.",
        "Not doubt, not nerves — just space.",
        "",
    ])
    render_lines(['"I\'ll give you that, next time."'], color=FOG)
    time.sleep(0.6)
    render_lines([
        "",
        "Dirksen believed him.",
    ])
    wait_key()


def s12():
    clear()
    print()
    scene_header("XII", "The Handshake at the Corner")
    render_art("breath", COLD + DIM)
    print()
    render_lines([
        "They left around half past eleven.",
        "The fog had not lifted and would not lift.",
        "It was the kind of cold April night that owns itself completely.",
        "",
        "They shook hands at the corner,",
        "which was how they always said goodbye:",
        "a short grip, direct, no theater.",
        "",
    ], color=COLD)
    render_art("corner", FOG + DIM)
    print()
    render_lines([
        "Their breath hung in the air a moment after they'd parted —",
        "two small clouds drifting apart above the cobblestones,",
        "then gone.",
        "",
        "The canal pulled the fog east.",
        "The streetlights held their amber posts.",
        "",
        "And the city, indifferent and faithful,",
        "kept its watch through the long dark of the night.",
    ], color=FOG)
    wait_key()


# ── title & end ───────────────────────────────────────────────────────────────

def title_card():
    clear()
    time.sleep(0.3)
    lines_top = (t.height // 2) - 7
    print("\n" * max(lines_top, 0))

    cards = [
        (AMBER + BOLD, "  A   U N I Q U E   C O N V E R S A T I O N"),
        ("",           ""),
        (FOG,          "  ─────────────────────────────────────────────"),
        ("",           ""),
        (COLD,         "  two men.  late coffee.  thick fog.  cold april."),
        ("",           ""),
        (FOG,          "  ─────────────────────────────────────────────"),
        ("",           ""),
        (DIM,          "  a terminal visual novel"),
        (DIM,          "  by leib weissman"),
    ]
    for color, text in cards:
        if text == "":
            print()
        else:
            print(color + text + RESET)
        time.sleep(0.14)

    wait_key()


def end_card():
    clear()
    lines_top = (t.height // 2) - 5
    print("\n" * max(lines_top, 0))

    cards = [
        (COLD, "  The city kept its watch."),
        ("",   ""),
        (FOG,  "  ─────────────────────────────────────────────"),
        ("",   ""),
        (AMBER,"  [ end ]"),
        ("",   ""),
        (DIM,  "  leib weissman  ·  2026"),
        (DIM,  "  source: retro/2026-04-20_ronnie_dirksen_coffee.md"),
        (DIM,  "  understood: somehow."),
    ]
    for color, text in cards:
        if text == "":
            print()
        else:
            print(color + text + RESET)
        time.sleep(0.18)

    time.sleep(2.5)
    clear()


# ── main ──────────────────────────────────────────────────────────────────────

SCENES = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12]


def main():
    with t.fullscreen(), t.hidden_cursor():
        title_card()
        for fn in SCENES:
            fn()
        end_card()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET)
        sys.stdout.flush()
        sys.exit(0)
