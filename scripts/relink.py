"""Move markdown files and rewrite every relative link that points to or from them.

usage: python3 -I relink.py <repo-root> old/path.md=new/path.md [old=new ...]

Paths are relative to the repo root. Tracked files are moved with `git mv`, untracked ones with rename.
Links inside fenced code blocks are left alone. Folders with parentheses are percent-encoded in rewritten links.
"""
import os
import re
import subprocess
import sys
import urllib.parse

SKIP_DIRS = {'node_modules', '.git', '.next', 'worktrees', 'vendor', 'dist', 'build'}
LINK = re.compile(r'\]\(([^)\s]+)\)')


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    root = os.path.abspath(sys.argv[1])
    moves = {}
    for arg in sys.argv[2:]:
        old, sep, new = arg.partition('=')
        if not sep:
            sys.exit(f'bad move: {arg}')
        moves[os.path.join(root, old)] = os.path.join(root, new)
    for old in moves:
        if not os.path.exists(old):
            sys.exit(f'missing: {os.path.relpath(old, root)}')

    def rewrite(text, old_dir, new_dir):
        def fix(m):
            raw = m.group(1)
            target, _, frag = raw.partition('#')
            if not target or re.match(r'^[a-z]+:', target):
                return m.group(0)
            abs_t = os.path.normpath(os.path.join(old_dir, urllib.parse.unquote(target)))
            abs_t = moves.get(abs_t, abs_t)
            rel = os.path.relpath(abs_t, new_dir)
            if target.endswith('/') and not rel.endswith('/'):
                rel += '/'
            rel = rel.replace('(', '%28').replace(')', '%29')
            return '](' + rel + ('#' + frag if frag else '') + ')'

        parts = re.split(r'(```.*?```)', text, flags=re.S)
        return ''.join(p if p.startswith('```') else LINK.sub(fix, p) for p in parts)

    pending = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dp, fn)
            src = open(p, encoding='utf-8').read()
            dst = moves.get(p, p)
            out = rewrite(src, os.path.dirname(p), os.path.dirname(dst))
            if out != src or dst != p:
                pending[p] = (dst, out)

    for p, (dst, out) in pending.items():
        if dst != p:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            tracked = subprocess.run(['git', '-C', root, 'ls-files', '--error-unmatch', p],
                                     capture_output=True).returncode == 0
            if tracked:
                subprocess.run(['git', '-C', root, 'mv', p, dst], check=True)
            else:
                os.rename(p, dst)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(out)
        print(('moved  ' if dst != p else 'edited ') + os.path.relpath(dst, root))

    # non-markdown files that are moved (images, scripts) go through git mv only
    for old, new in moves.items():
        if os.path.exists(old) and not old.endswith('.md'):
            os.makedirs(os.path.dirname(new), exist_ok=True)
            subprocess.run(['git', '-C', root, 'mv', old, new], check=True)
            print('moved  ' + os.path.relpath(new, root))


if __name__ == '__main__':
    main()
