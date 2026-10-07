"""Exact live serving and eligibility checks, not indexing evidence."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'str-management-agreement-termination': ('2026-09-24', 4)}
if __name__ == '__main__':
    verifier.main()
