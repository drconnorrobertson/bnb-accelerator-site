"""Read-only exact production check using established batch verifier."""
import verify_dscr_purchase_methods as verifier
verifier.SLUGS={'str-long-term-rental-fallback':('2026-09-23',4)}
if __name__ == '__main__':
    verifier.main()
