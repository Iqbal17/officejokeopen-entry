"""Make the AI Judge Laugh: the Office Joke Open (u-aldy998-...-9920f232).

One line of office comedy, 1-200 characters. The judge is a stand-up comic
who has sat through a thousand office meetings; it weighs, most important
first: (1) the joke is about office life and works as a joke, not a
complaint; (2) the laugh is earned by a turn that pays off in the last few
words; (3) the office detail is specific; (4) it is fresh; (5) it reads
cleanly in one pass.

DECISION RECORD — candidates weighed:

A. Reply-all: "I hit reply-all to say 'please remove me from this thread,'
   and now 400 people know I exist and none of them will remove me."
   Specific and recognisable, but reply-all is the most crowded setup in
   office comedy; freshness (criterion 4) suffers against the field.

B. Printer: "The office printer has been 'warming up' since Tuesday, which
   is the longest any of us has stayed committed to anything here."
   Good misdirection — warming up becomes a commitment joke — but the
   punch is slightly predictable once "since Tuesday" lands.

C. Calendar: "My calendar says I'm free all day, which is how I know nobody
   actually read it before booking me solid." A remark, not a joke: no turn,
   no payoff in the last words (fails criterion 2).

D. Meeting/email: "This meeting could have been an email, but then nobody
   would have watched me nod for forty-five minutes." The setup is the
   single most overused office joke alive; the turn is decent but the
   familiar setup loses on freshness (criterion 4).

E. Out of office: "I set my out-of-office reply to 'back Monday,' and the
   office took it as a suggestion." Clean and tight, but the laugh is thin
   — more a remark than a joke with a turn (fails criterion 2).

F. "Per my last email" — CHOSEN. A concrete office artifact (the exact
   phrase every office worker has typed), and the escalation is unexpected:
   HR doesn't punish the passive aggression, it forwards it company-wide as
   a masterclass. The payoff lands in the last few words, exactly as
   criterion 2 wants.

WRITING PASSES on F:
Pass 1: "I wrote 'per my last email' so politely that HR forwarded it to
   the whole company as a masterclass in passive aggression." (121 chars)
   Clean, but "to the whole company" is five words doing the work of one.
Pass 2: "I wrote 'per my last email' so politely that HR forwarded it
   company-wide as a masterclass in passive aggression." (113 chars)
   "company-wide" replaces "to the whole company" with no loss; "that"
   kept, because dropping it ("so politely HR forwarded") reads rushed
   and costs criterion 5. Final line below.
"""

import os
import sys

LINE = (
    "I wrote 'per my last email' so politely that HR forwarded it "
    "company-wide as a masterclass in passive aggression."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"chars: {len(LINE)}", file=sys.stderr)
    # Read-back verification: the file must be byte-for-byte the intended
    # line, one line, inside the 1-200 character gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt does not match the intended line"
    assert written == written.strip() + "\n", "entry.txt has stray whitespace"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, outside 1-200"
    assert "\n" not in LINE, "entry must be a single line"


if __name__ == "__main__":
    main()
