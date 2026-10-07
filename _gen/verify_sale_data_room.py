"""Read-only exact live eligibility checks, not indexing evidence."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'str-sale-data-room': ('2026-09-23', 3)}
if __name__ == '__main__':
    verifier.main()
