"""Exact live serving eligibility, not confirmed Google indexing."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'str-license-renewal-calendar': ('2026-09-23', 3)}
if __name__ == '__main__':
    verifier.main()
