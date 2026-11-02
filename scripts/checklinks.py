"""Report broken relative links in every markdown file of a repo.

usage: python3 -I checklinks.py <repo-root>

Skips node_modules, .git, build output and agent worktrees, ignores links inside fenced code blocks,
and decodes percent-encoding (e.g. %28app%29) before checking the target exists. Exit code 1 if anything is broken.
"""
import os
import re
import sys
import urllib.parse

SKIP_DIRS = {'node_modules', '.git', '.next', 'worktrees', 'vendor', 'dist', 'build'}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = os.path.abspath(sys.argv[1])
    broken = 0
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            text = open(p, encoding='utf-8', errors='ignore').read()
            text = re.sub(r'```.*?```', '', text, flags=re.S)
            for m in re.findall(r'\]\(([^)\s]+)\)', text):
                target = urllib.parse.unquote(m.split('#')[0])
                if not target or re.match(r'^[a-z]+:', target):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(dp, target))):
                    broken += 1
                    print(f'{os.path.relpath(p, root)} -> {m}')
    print('broken', broken)
    sys.exit(1 if broken else 0)


if __name__ == '__main__':
    main()
