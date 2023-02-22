#! /usr/bin/env python
import sys
def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
in_virtualenv = lambda  : get_base_prefix_compat() != sys.prefix
is_module = lambda : __name__ == "__main__"


def main():
    print(sys.prefix)

if is_module() and in_virtualenv():
    main()

