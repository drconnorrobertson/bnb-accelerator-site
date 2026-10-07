"""Scoped accuracy correction; preserves article structure and conversion flow."""
import html, json, math, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'airbnb-neighbors-and-noise'
URL = 'https://www.bnbaccelerator.com/blog/'+SLUG+'/'
DESC = 'Before buying an STR, check noise and parking rules, complaint history, responder coverage and disclosed monitoring. Plan a documented incident response.'

def main():
    p = ROOT/'blog'/SLUG/'index.html'
    s = p.read_text()
    replacements = {
      'Nearly every short-term rental ordinance in the country was written because of neighbor complaints. Managing that relationship is not a courtesy, it is the single most effective form of regulatory risk management available to an individual owner.': 'Before buying a short-term rental, evaluate how noise, parking and guest activity could affect adjacent properties. Neighbor communication and a workable response plan are useful controls, but neither replaces lawful rental permission or guarantees that complaints will be avoided.',
      'A noise complaint costs a warning or a penalty. A pattern of complaints from an organized set of neighbors produces council testimony, and council testimony produces ordinances. Individual owners cannot control a market\'s regulatory trajectory, but they can control whether they are the property cited as the reason for it.': 'A complaint is not automatically a proven violation. Before closing, distinguish allegations, notices, substantiated violations and unresolved proceedings. Read the applicable ordinance and permit conditions to understand possible penalties, response duties and renewal consequences; do not assume a universal escalation sequence.',
      'In permit limited markets the exposure is direct: complaint history can affect renewal. See <a href="/blog/nashville-airbnb-investing/">Nashville</a>, where regulation was driven substantially by exactly this dynamic.': 'Ask the seller for notices and incident records, and confirm any available enforcement history with the issuing authority. Check the existing <a href="/blog/str-complaint-permit-revocation/">complaint-history and revocation guide</a> and <a href="/blog/str-license-renewal-calendar/">renewal-calendar guide</a>. Neither an active seller permit nor a friendly neighbor confirms your purchase can operate lawfully.',
      'Prevention, in order of effectiveness': 'Prevention checks before buying and opening',
      'Lot size, tree cover, distance to the nearest structure, and whether the immediate neighbors are owner occupants or other rentals matter more than any policy you write afterward.': 'Inspect the spacing of outdoor gathering areas, property boundaries, access and adjoining uses. Do not assume trees provide adequate sound protection. Compare the intended occupancy and outdoor use with binding rules and the actual site.',
      'Sensors that report sound levels rather than recording audio, disclosed in the listing, let you intervene before a neighbor does.': 'A sound-level alert can prompt a response, but is not proof that a legal noise limit was violated or that someone will respond in time. Airbnb allows disclosed interior noise decibel monitors that do not record audio, excluding bedrooms, bathrooms and sleeping areas. Check device placement, privacy law, platform rules and who receives alerts.',
      'since blocked driveways and street parking generate more complaints than noise in many neighborhoods.': 'including designated spaces, unobstructed driveways and locally permitted street parking. Physical space is not the same as legally authorized capacity.',
      'The highest return action available: give the adjacent neighbors your phone number and ask them to call you first. It costs nothing and it changes the outcome of every incident.': 'Offer adjacent neighbors a reliable nonemergency contact and explain who handles overnight incidents. They remain free to contact authorities; do not ask them to waive reporting rights or promise a particular outcome. Test your own coverage rather than assuming a shared phone number is a response system.',
      'A neighbor with your number calls you at 11pm and you resolve it in ten minutes. A neighbor without it calls the police or codes enforcement, which creates a record that exists permanently and may appear in a renewal file or a council packet.': 'A late-night call may require guest contact, an on-site responder or emergency assistance. Agree on alert acknowledgement, backup coverage and documentation before opening. Record-retention periods and the use of complaint records in renewal or hearings depend on the authority and process, not a universal permanent-record rule.',
      'Some owners provide a small annual gesture around the holidays, which sounds trivial and is not.': 'Goodwill gestures are optional and do not substitute for compliance or accepted responder duties.',
      'Neighborhood composition is also a market signal. A submarket where short-term rentals sit among owner occupied primary residences carries higher political risk than a resort zone where the entire street is visitor accommodation. That difference belongs in underwriting rather than in hindsight.': 'Neighborhood context deserves diligence, not a categorical political-risk score. Review current zoning, permit conditions, HOA restrictions, recent notices and adopted or proposed changes. Visitor-oriented areas can also restrict rentals, while a residential setting does not by itself establish a violation or future ban. Include unresolved permission and operating questions in the purchase decision.',
      'In order of effectiveness: buy a property with lot size, tree cover, and distance from neighbors on your side, install disclosed decibel monitoring that reports sound levels rather than recording audio, enforce occupancy limits, state a clear no events policy, manage parking, and post quiet hours inside the property.': 'Evaluate the site and binding occupancy, parking and quiet-hour rules before buying. Plan guest communication and responder coverage. If using noise decibel monitors, check privacy and platform rules; Airbnb requires disclosure and excludes bedrooms, bathrooms and sleeping areas. These controls do not guarantee no complaints.',
      'Because nearly every short-term rental ordinance was written in response to neighbor complaints. A neighbor with your phone number calls you and the issue is resolved in ten minutes. A neighbor without it calls enforcement, creating a permanent record that can appear in a permit renewal file or a council packet.': 'Reliable communication can help identify an issue and coordinate a response, but neighbors may contact authorities and resolution time is not guaranteed. Determine locally how complaints, proven violations, response duties and records affect the permit. Keep an incident log without assuming records are permanent.',
      'Substantially. A property among owner occupied primary residences carries higher political risk than one in a resort zone where the whole street is visitor accommodation. That difference belongs in underwriting rather than being discovered after the first complaint.': 'Adjoining uses and outdoor gathering areas are relevant diligence inputs, but neighborhood type alone does not establish a political-risk ranking. Verify zoning, permit conditions, HOA restrictions, enforcement history and proposed changes for the actual property before underwriting its permitted use.'
    }
    for old, new in replacements.items():
        assert old in s, old
        s = s.replace(old,new)
    source = '<p><strong>Source reviewed October 7, 2026:</strong> <a href="https://www.airbnb.com/help/article/3061">Airbnb restrictions on security cameras and other devices in homes</a>, especially noise decibel monitors. This is document-based guidance published by BNB Accelerator, an interested acquisition service provider, not firsthand device testing or legal advice. Confirm local obligations with the authority and qualified counsel.</p>'
    s = s.replace('<h2 id="relationship">',source+'\n\n        <h2 id="relationship">',1)
    s = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*(">)',lambda m:m[1]+DESC+m[2],s)
    s = s.replace('property="article:published_time" content="2026-05-12"','property="article:published_time" content="2026-08-11"')
    article = re.search(r'<article class="article">(.*?)</article>',s,re.S)[1]
    words = len(html.unescape(re.sub('<[^>]+>',' ',article)).split())
    minutes = math.ceil(words/220)
    def schema(m):
        d=json.loads(m[1])
        for n in d.get('@graph',[d]):
            if n.get('@type')=='BlogPosting':
                assert n['datePublished']=='2026-08-11'
                n.update(description=DESC,dateModified='2026-10-07',wordCount=words)
        return '<script type="application/ld+json">\n'+json.dumps(d,indent=2)+'\n</script>'
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,s,flags=re.S)
    s = s.replace('Published August 11, 2026</span><span>&middot;</span><span>6 min read','Published August 11, 2026</span><span>&middot;</span><span>Updated October 7, 2026</span><span>&middot;</span><span>'+str(minutes)+' min read')
    p.write_text(s)
    a=ROOT/'blog/index.html'; archive=a.read_text()
    cards=re.findall(r'<article class="post-card".*?</article>',archive,re.S)
    card=next(c for c in cards if 'href="/blog/'+SLUG+'/' in c)
    new=re.sub(r'data-search="[^"]*"','data-search="managing neighbors and noise operations '+DESC.lower()+'"',card)
    new=re.sub(r'<p>.*?</p>','<p>'+DESC+'</p>',new,count=1,flags=re.S)
    new=new.replace('6 min read',str(minutes)+' min read')
    assert sum('href="/blog/'+SLUG+'/' in c for c in cards)==1
    a.write_text(archive.replace(card,new))
    p=ROOT/'sitemap-blog.xml';sm=p.read_text()
    sm,n=re.subn(r'(<loc>'+re.escape(URL)+r'</loc>\s*<lastmod>)[^<]+',r'\g<1>2026-10-07',sm);assert n==1;p.write_text(sm)
    print(json.dumps({'words':words,'minutes':minutes,'publication':'2026-08-11','new_509_credit':0}))

if __name__=='__main__': main()
