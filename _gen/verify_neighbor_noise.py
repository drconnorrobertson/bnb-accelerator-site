"""Read-only exact serving verification, not confirmed indexing."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS = {'airbnb-neighbors-and-noise': ('2026-08-11', 4)}
if __name__ == '__main__': verifier.main()
