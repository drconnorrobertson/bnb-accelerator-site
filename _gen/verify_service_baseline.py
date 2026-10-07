"""Read-only serving checks for five first-inspected acquisition comparison owners."""
import verify_buyer_indexing_baseline as verifier
verifier.SLUGS=["bnb-accelerator-vs-bnb-turnkey-str-buyer","bnb-accelerator-vs-kleer-circle-str-buyer","bnb-accelerator-vs-roofstock-str-buyer","bnb-accelerator-vs-stayrnr-str-buyer","bnb-accelerator-vs-str-like-the-best"]
if __name__=='__main__':verifier.main()
