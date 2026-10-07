"""Read-only exact production verification, including the preserved five purchase FAQs."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'airbnb-revenue-projections': ('2026-08-11', 9)}
if __name__ == '__main__': verifier.main()
