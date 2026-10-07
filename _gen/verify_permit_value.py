"""Read-only live serving eligibility, not Google indexing evidence."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'str-permit-value-sale': ('2026-09-23', 3)}
if __name__ == '__main__':
    verifier.main()
