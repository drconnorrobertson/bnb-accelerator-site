#!/usr/bin/env python3
"""Short-term rental regulation summaries by state.

Regulation changes constantly and varies at the city, county and HOA level.
Every page carries a prominent verification warning and points the reader at
the controlling local authority rather than presenting these as legal advice.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import guide, hub, write

VERIFY = ("Short-term rental rules change frequently and the controlling rule is usually local, "
          "not statewide. Treat this as orientation, then verify the current ordinance with the city "
          "or county directly, and read any homeowner association or condominium declaration separately. "
          "This is not legal advice.")

# slug, state, posture, summary, key points, cities table, faqs, markets
STATES = [
    dict(
        slug="tennessee", state="Tennessee", posture="Favorable, with strong local variation",
        blurb="A 2018 state act protects grandfathered units; Nashville caps non-owner-occupied permits by zone.",
        lead="Tennessee is one of the more workable states for short-term rental investing, largely because a 2018 state law limits how far local governments can go in banning units that were already operating, and because the Smoky Mountain corridor operates under county and small-city rules that have stayed comparatively stable.",
        points=[
            "The Tennessee Short Term Rental Unit Act, enacted in 2018, generally prevents local governments from prohibiting short-term rental units that were lawfully operating before the local ordinance took effect. This grandfathering is the state's most important protection for existing operators.",
            "Local governments retain broad authority over new units, including permitting, zoning, occupancy limits, noise and inspection requirements.",
            "Nashville distinguishes owner-occupied from non-owner-occupied permits and restricts non-owner-occupied permits by zoning district, which caps supply in the most desirable areas.",
            "Sevier County and the Smokies cities, Gatlinburg, Pigeon Forge and Sevierville, have long-established cabin rental economies and correspondingly established regulatory frameworks.",
            "Tennessee levies no state income tax on wages, which removes a layer of state-level complexity for high-earning buyers, though it does not change federal treatment.",
            "State and local occupancy and sales taxes apply. Platforms collect some of these automatically and not others, so confirm what remains your responsibility.",
        ],
        cities=[
            ["Nashville", "Permit required; non-owner-occupied restricted by zoning district", "High"],
            ["Sevierville / Pigeon Forge / Gatlinburg", "Established cabin rental frameworks, permits and inspections", "Moderate"],
            ["Chattanooga", "Permit and zoning requirements, restricted in some residential zones", "Moderate to high"],
            ["Memphis", "Permit program with density and separation limits", "Moderate"],
        ],
        markets=['<a href="/markets/smoky-mountains/">Smoky Mountains</a>',
                 '<a href="/markets/gatlinburg/">Gatlinburg</a>',
                 '<a href="/markets/nashville/">Nashville</a>'],
        faqs=[
            ("Are short-term rentals legal in Tennessee?",
             "Yes, subject to local rules. A 2018 state act generally prevents local governments from prohibiting units that were lawfully operating before a local ordinance took effect, but cities retain broad authority over new permits, zoning and operating standards."),
            ("How does Nashville regulate short-term rentals?",
             "Nashville separates owner-occupied from non-owner-occupied permits and restricts non-owner-occupied permits by zoning district. That cap on supply is a large part of why permitted Nashville properties hold their value."),
            ("Do I owe occupancy tax in Tennessee?",
             "State and local occupancy and sales taxes generally apply. Booking platforms collect some of these automatically and not others depending on the jurisdiction, so confirm with the local authority what remains your responsibility."),
        ],
    ),
    dict(
        slug="florida", state="Florida", posture="Favorable at the state level, mixed locally",
        blurb="State law preempts newer local bans, but pre-2011 ordinances are grandfathered and vary widely.",
        lead="Florida is the largest short-term rental state in the country and one of the more favorable at the state level, because a state preemption statute limits how far local governments can go. The complication is that ordinances predating the preemption were grandfathered, so the map is genuinely uneven from one city to the next.",
        points=[
            "Florida law preempts local regulation that prohibits vacation rentals or regulates their duration or frequency, for local ordinances adopted after June 1, 2011.",
            "Local ordinances in place before that date were grandfathered and remain enforceable. Several Florida cities operate under restrictive grandfathered rules that would not be permitted today.",
            "Local governments may still regulate in ways that apply to all residential properties, and may impose registration, life safety and noise requirements.",
            "A vacation rental license from the Florida Department of Business and Professional Regulation is generally required for properties rented more than three times a year for periods of less than 30 days, or advertised as such.",
            "State sales tax plus county tourist development tax apply. Platform collection varies by county, so confirm which taxes remain your responsibility.",
            "Coastal insurance, including wind and flood coverage, has repriced sharply and is a material underwriting factor rather than a footnote.",
        ],
        cities=[
            ["Destin / Fort Walton Beach", "Registration and life safety requirements; broadly workable", "Low to moderate"],
            ["Panama City Beach", "Registration; established vacation rental market", "Low"],
            ["Orlando area (Kissimmee, Davenport, Champions Gate)", "Zoning-dependent; purpose-built resort communities generally permitted", "Low in resort zones"],
            ["Fort Myers / Cape Coral", "Registration and local standards", "Low to moderate"],
            ["Miami Beach", "Restrictive grandfathered ordinance with substantial fines", "High"],
        ],
        markets=['<a href="/markets/destin/">Destin</a>',
                 '<a href="/markets/panama-city-beach/">Panama City Beach</a>',
                 '<a href="/markets/kissimmee/">Kissimmee</a>',
                 '<a href="/markets/cape-coral/">Cape Coral</a>'],
        faqs=[
            ("Does Florida preempt local short-term rental bans?",
             "Partly. State law preempts local ordinances adopted after June 1, 2011 that prohibit vacation rentals or regulate their duration or frequency. Ordinances in place before that date were grandfathered and remain enforceable, which is why the map is uneven."),
            ("Do I need a license for a Florida vacation rental?",
             "Generally yes. A vacation rental license from the Department of Business and Professional Regulation is typically required for properties rented more than three times a year for periods under 30 days, or advertised as such."),
            ("Which Florida cities are most restrictive?",
             "Cities operating under ordinances predating the 2011 preemption. Miami Beach is the most-cited example, with a restrictive framework and substantial penalties. Panhandle and Orlando-area vacation markets are generally far more workable."),
        ],
    ),
    dict(
        slug="arizona", state="Arizona", posture="Among the most favorable in the country",
        blurb="State law preempts municipal bans; cities may license and regulate but not prohibit.",
        lead="Arizona is among the most favorable short-term rental states in the country, because state legislation substantially preempts municipal bans. Cities can license, inspect and enforce nuisance standards, but they generally cannot prohibit short-term rentals outright, which removes the single largest risk that affects urban and resort markets elsewhere.",
        points=[
            "Arizona legislation enacted in 2016 broadly preempted municipal prohibition of short-term rentals, and subsequent legislation in 2022 restored meaningful local authority to license and regulate without permitting outright bans.",
            "Cities may require licensing, emergency contact information, notification of adjacent property owners, and may impose penalties for verified nuisance or noise violations.",
            "Municipalities may prohibit uses such as commercial events and non-residential activity at a short-term rental.",
            "A transaction privilege tax license is generally required, and state and local transaction privilege taxes apply to short-term rental income.",
            "The practical effect is unusual regulatory stability for Scottsdale, Phoenix, Mesa, Sedona and the surrounding desert markets compared with California desert markets across the border.",
            "Homeowner association restrictions still apply independently of state preemption, and many Arizona HOAs restrict or prohibit short-term rentals.",
        ],
        cities=[
            ["Scottsdale", "Licensing, notification and nuisance enforcement; no outright ban", "Low"],
            ["Phoenix / Mesa", "Licensing and registration; no outright ban", "Low"],
            ["Sedona", "Licensing and registration; strong demand, constrained housing supply", "Low to moderate"],
            ["Flagstaff", "Licensing; local political pressure around housing supply", "Low to moderate"],
        ],
        markets=['<a href="/markets/scottsdale/">Scottsdale</a>',
                 '<a href="/markets/phoenix-mesa/">Phoenix and Mesa</a>',
                 '<a href="/markets/sedona/">Sedona</a>'],
        faqs=[
            ("Can Arizona cities ban short-term rentals?",
             "Generally no. State legislation preempts municipal prohibition, though later legislation restored substantial local authority to license, require emergency contacts, notify neighbors and enforce nuisance standards."),
            ("Do I need a license for an Arizona short-term rental?",
             "Typically yes, both a municipal license where the city requires one and a transaction privilege tax license at the state level. State and local transaction privilege taxes apply to rental income."),
            ("Does state preemption override my HOA?",
             "No. Homeowner association restrictions operate independently, and many Arizona HOAs restrict or prohibit short-term rentals. Read the declaration separately from the municipal rules."),
        ],
    ),
    dict(
        slug="texas", state="Texas", posture="Generally permissive, with litigated city ordinances",
        blurb="No statewide ban; several city ordinances have been narrowed by courts. Unincorporated county land is often unregulated.",
        lead="Texas has no statewide short-term rental prohibition and a body of litigation that has narrowed several aggressive city ordinances. The practical result is a state where much of the best inventory sits on unincorporated county land outside city rules entirely, which is a meaningful part of why the Hill Country works so well.",
        points=[
            "There is no statewide prohibition. Regulation happens at the city level, and unincorporated county land is frequently outside any short-term rental ordinance.",
            "Texas appellate courts have limited the reach of some city ordinances. Austin's ordinance restricting non-owner-occupied short-term rentals has been the subject of significant litigation and portions have been held unconstitutional.",
            "The Texas Supreme Court has held that a general residential-use deed restriction does not by itself prohibit short-term rental use, which limits one common avenue of private restriction.",
            "Explicit HOA and subdivision restrictions that specifically address short-term rentals remain enforceable, so the deed restrictions still have to be read.",
            "State hotel occupancy tax applies, and many cities impose an additional local hotel occupancy tax. Registration is commonly required.",
            "Hill Country properties on unincorporated land in Blanco, Gillespie and surrounding counties often face far lighter regulation than properties inside city limits a few miles away.",
        ],
        cities=[
            ["Austin", "Licensing regime, litigated and partially narrowed by courts", "High"],
            ["Johnson City / Hill Country (unincorporated)", "Often outside city ordinances entirely", "Low"],
            ["Fredericksburg", "Permit program with density limits in some districts", "Moderate"],
            ["Galveston / Surfside Beach", "Registration and occupancy tax; established rental market", "Low to moderate"],
        ],
        markets=['<a href="/markets/austin/">Austin and the Hill Country</a>'],
        faqs=[
            ("Are short-term rentals legal in Texas?",
             "Yes. There is no statewide prohibition, and much of the desirable inventory sits on unincorporated county land outside city ordinances. City rules vary considerably, and several have been narrowed through litigation."),
            ("Can a deed restriction stop me from running a short-term rental in Texas?",
             "A general residential-use restriction alone generally does not, following Texas Supreme Court authority. An explicit restriction that specifically addresses short-term or transient rental remains enforceable, so read the actual deed restrictions."),
            ("Why is the Texas Hill Country attractive for STR investing?",
             "Much of the inventory sits on unincorporated county land outside city short-term rental ordinances, while still drawing wine weekend and wedding groups from Austin, San Antonio and Houston."),
        ],
    ),
    dict(
        slug="california", state="California", posture="Restrictive, with strong local control",
        blurb="No state preemption. Permit caps, waiting lists and coastal zone review make California the hardest large state.",
        lead="California gives local governments broad authority over short-term rentals and has no meaningful preemption protecting operators. The result is the most fragmented and most restrictive regulatory environment among the large states, and the one where verifying the permit position before an offer matters most.",
        points=[
            "There is no state preemption. Cities and counties set their own rules, and many have adopted permit caps, density limits or outright prohibitions in residential zones.",
            "Palm Springs operates a permit program with a cap and a waiting list, which makes an existing transferable permit a substantial part of a property's value.",
            "San Bernardino County, which includes Joshua Tree and Big Bear, has tightened repeatedly, including caps and density restrictions in unincorporated areas.",
            "Properties in the coastal zone may face additional review, since the California Coastal Commission has taken the position that restricting short-term rentals can affect coastal access.",
            "Transient occupancy tax applies at rates set locally, often among the highest in the country.",
            "Because rules change frequently and caps can close, the permit position must be verified for the specific parcel with the controlling jurisdiction before an offer is written.",
        ],
        cities=[
            ["Palm Springs", "Permit cap with waiting list; permit is a material asset", "High"],
            ["Joshua Tree / San Bernardino County", "Caps and density limits, tightened repeatedly", "High"],
            ["Big Bear", "Permit program with caps and occupancy limits", "High"],
            ["Lake Tahoe (Placer / El Dorado / South Lake Tahoe)", "Permit caps varying sharply by jurisdiction", "High"],
            ["Los Angeles", "Home-sharing ordinance effectively limits non-primary-residence rentals", "Very high"],
        ],
        markets=['<a href="/markets/joshua-tree/">Joshua Tree</a>',
                 '<a href="/markets/big-bear/">Big Bear</a>',
                 '<a href="/markets/lake-tahoe/">Lake Tahoe</a>'],
        faqs=[
            ("Is California a good state for short-term rental investing?",
             "It is the hardest large state. There is no state preemption, many jurisdictions run permit caps with waiting lists, and rules have tightened repeatedly. Where a transferable permit exists it can be extremely valuable precisely because supply is capped."),
            ("How do permit caps work in California desert markets?",
             "Palm Springs and several San Bernardino County jurisdictions cap the number of permits and maintain waiting lists. A property without a permit may not be able to obtain one, which means it is worth its long-term rental value rather than its short-term proforma."),
            ("Does the Coastal Commission affect short-term rentals?",
             "It can. The California Coastal Commission has taken the position that restrictions on short-term rentals in the coastal zone may affect public coastal access, which adds a layer of review in coastal jurisdictions."),
        ],
    ),
    dict(
        slug="oklahoma", state="Oklahoma", posture="Permissive, especially in McCurtain County",
        blurb="Light regulation overall; Broken Bow and Hochatown have grown into a major cabin market with modest rules.",
        lead="Oklahoma has among the lightest short-term rental regulation of any state with a major destination market. Broken Bow and the surrounding Hochatown area in McCurtain County have grown from a regional secret into one of the highest-performing cabin markets in the country largely without the regulatory friction that would have accompanied the same growth elsewhere.",
        points=[
            "There is no restrictive statewide framework. Regulation is local and generally light.",
            "McCurtain County, including Broken Bow and Hochatown, hosts a large and rapidly grown cabin rental economy. Hochatown incorporated as a town in recent years, which introduced a local government where previously there was effectively none.",
            "Lodging and sales taxes apply. Confirm collection responsibility with the platform and the local authority.",
            "The primary risk in this market is not regulation, it is supply. Rapid inventory growth in the Broken Bow area is the factor most likely to compress rates.",
            "The demand base is heavily Dallas-Fort Worth, roughly a three-hour drive, which makes the market sensitive to Texas economic conditions.",
            "The top tier of the market is luxury A-frame and architectural cabins competing on design and photography rather than bedroom count.",
        ],
        cities=[
            ["Broken Bow / Hochatown", "Light regulation; new town government since incorporation", "Low, supply risk instead"],
            ["Oklahoma City", "Registration requirements in some districts", "Low to moderate"],
            ["Tulsa", "Zoning-dependent, generally workable", "Low to moderate"],
        ],
        markets=['<a href="/markets/broken-bow/">Broken Bow</a>'],
        faqs=[
            ("Is Broken Bow regulated for short-term rentals?",
             "Lightly compared with most destination markets. Hochatown's recent incorporation introduced a local government where there previously was effectively none, so the regulatory picture is newer than the market itself."),
            ("What is the main risk in the Broken Bow market?",
             "Supply rather than regulation. Inventory has grown very fast, and rate compression from new cabins is the factor most likely to affect returns."),
            ("Where does Broken Bow demand come from?",
             "Primarily Dallas-Fort Worth, roughly a three-hour drive, which makes the market sensitive to Texas economic conditions and gives it a weekend-weighted booking pattern."),
        ],
    ),
    dict(
        slug="pennsylvania", state="Pennsylvania", posture="Highly local, township by township",
        blurb="No state framework. Poconos rules vary by township and HOA, sometimes property to property.",
        lead="Pennsylvania has no statewide short-term rental framework, which means the controlling rule is the township ordinance and, very often, the homeowner association declaration. In the Poconos this variation is granular enough that two properties on the same road can face different rules.",
        points=[
            "Regulation is set at the municipal and township level. There is no state preemption and no uniform framework.",
            "Monroe and Carbon counties, which contain most of the Pocono rental inventory, include dozens of townships with independently adopted ordinances.",
            "Large private communities in the Poconos, including gated lake and golf communities, impose their own rules through homeowner association declarations. These are frequently more restrictive than the township ordinance and are enforced privately.",
            "Local hotel and occupancy taxes apply at rates set by county.",
            "Because the variation is so granular, the permit and HOA position must be verified for the specific parcel before an offer. A property that cannot legally operate is worth nothing as a short-term rental regardless of how well it shows.",
            "The compensating advantage is demand. Roughly thirty million people live within a two-hour drive from New York and Philadelphia, and the region has four genuine seasons.",
        ],
        cities=[
            ["Monroe County townships", "Ordinances vary township by township", "Moderate, verify per parcel"],
            ["Carbon County / Jim Thorpe", "Local ordinances; established tourism economy", "Moderate"],
            ["Pocono private communities", "HOA declarations often more restrictive than township rules", "High, read the declaration"],
            ["Philadelphia", "Licensing regime with zoning restrictions", "High"],
        ],
        markets=['<a href="/markets/poconos/">Poconos</a>'],
        faqs=[
            ("How are short-term rentals regulated in the Poconos?",
             "By individual township ordinance, with no statewide framework. Monroe and Carbon counties contain dozens of townships that have adopted rules independently, so the position has to be verified for the specific parcel."),
            ("Do Pocono homeowner associations restrict short-term rentals?",
             "Frequently, and often more restrictively than the township ordinance. Large gated lake and golf communities enforce their own declarations privately, which is a separate check from the municipal one."),
            ("What makes the Poconos attractive despite the regulatory complexity?",
             "Demand. About thirty million people live within a two-hour drive from New York and Philadelphia, and the region has four genuine seasons, which produces a flatter annual revenue curve than most vacation markets."),
        ],
    ),
    dict(
        slug="colorado", state="Colorado", posture="Restrictive in mountain resort towns",
        blurb="Strong local control. Resort towns have adopted caps, license classes and higher tax rates.",
        lead="Colorado gives local governments broad authority, and the mountain resort towns have used it. Caps, license classes tied to zoning, and elevated lodging taxes are now standard across the major ski markets, driven by local housing pressure rather than by any state policy.",
        points=[
            "There is no state preemption. Counties and municipalities set their own rules and several have adopted hard caps on license counts.",
            "Summit County and its towns, Breckenridge, Frisco and Silverthorne, have adopted license caps and zone-based license classes.",
            "Steamboat Springs, Crested Butte and several other resort communities have adopted overlay zones or caps restricting where short-term rentals may operate.",
            "Denver restricts short-term rentals to a host's primary residence, which effectively excludes conventional investment purchases in the city.",
            "Local marketing district and lodging taxes apply on top of state and local sales tax, and rates in resort areas are among the higher ones in the country.",
            "Colorado has also debated changing the property tax classification of short-term rentals toward a commercial rate, which is a live risk worth monitoring in any Colorado underwriting.",
        ],
        cities=[
            ["Breckenridge / Summit County", "License caps and zone-based license classes", "High"],
            ["Steamboat Springs", "Overlay zone restrictions", "High"],
            ["Denver", "Primary residence requirement", "Very high for investors"],
            ["Colorado Springs", "Permit program with separation requirements in some zones", "Moderate"],
        ],
        markets=['<a href="/markets/denver/">Denver</a>'],
        faqs=[
            ("Can I buy an investment short-term rental in Denver?",
             "Generally not in the conventional sense. Denver restricts short-term rentals to a host's primary residence, which excludes non-owner-occupied investment purchases."),
            ("Do Colorado ski towns cap short-term rental licenses?",
             "Several do. Summit County and its towns operate license caps and zone-based license classes, and Steamboat Springs and other resort communities have adopted overlay restrictions."),
            ("What is the property tax risk in Colorado?",
             "The state has debated reclassifying short-term rentals toward a commercial property tax rate, which would materially change operating costs. It is worth monitoring in any Colorado underwriting."),
        ],
    ),
    dict(
        slug="utah", state="Utah", posture="Mixed, with meaningful advertising protections",
        blurb="State law limits enforcement based on advertising alone; Park City and Summit County regulate by zone.",
        lead="Utah occupies a middle position. State law limits a municipality's ability to use a short-term rental advertisement alone as the basis for enforcement, which is a genuine protection, but zoning still controls where rentals may operate and the resort markets regulate by district.",
        points=[
            "Utah law generally restricts municipalities from using an advertisement, by itself, as the sole basis for enforcement against a short-term rental. The underlying zoning rules still apply.",
            "Park City and Summit County permit short-term rentals in defined zones, with much of the resort-adjacent inventory in areas where rentals are allowed and residential neighborhoods more restricted.",
            "Homeowner association and condominium declarations are a major factor in Park City, where a substantial share of the desirable base-area inventory is attached product with its own rules.",
            "Salt Lake City restricts short-term rentals substantially in residential zones.",
            "Transient room tax and state and local sales taxes apply.",
            "The practical guidance in Utah is to focus on zones where short-term rental is an allowed use, rather than relying on the advertising protection, which addresses enforcement mechanics rather than legality.",
        ],
        cities=[
            ["Park City / Summit County", "Allowed by zone; HOA rules often decisive", "Moderate"],
            ["Salt Lake City", "Substantially restricted in residential zones", "High"],
            ["St. George / Washington County", "Allowed in designated zones and resort communities", "Moderate"],
        ],
        markets=['<a href="/markets/park-city/">Park City</a>'],
        faqs=[
            ("Does Utah protect short-term rental operators?",
             "Partly. State law generally limits a municipality from using an advertisement alone as the sole basis for enforcement, but the underlying zoning rules still control whether a short-term rental is an allowed use."),
            ("How does Park City regulate short-term rentals?",
             "By zone, with resort-adjacent districts generally permitting rentals and residential neighborhoods more restricted. Homeowner association and condominium declarations are often the decisive constraint on base-area inventory."),
        ],
    ),
    dict(
        slug="missouri", state="Missouri", posture="Permissive, light local regulation",
        blurb="Branson and Table Rock Lake operate with modest rules in an established tourism economy.",
        lead="Missouri regulates short-term rentals lightly, and the Branson and Table Rock Lake area operates within a long-established tourism economy where rental accommodation is an accepted and expected part of the local structure.",
        points=[
            "There is no restrictive statewide framework. Local rules are generally modest, particularly in tourism-dependent areas.",
            "Branson and Branson West have decades of tourism infrastructure and correspondingly settled expectations around rental accommodation.",
            "Table Rock Lake shoreline is substantially managed by the Army Corps of Engineers, which controls dock permits. Dock rights do not always transfer with a sale and must be verified independently of the short-term rental question.",
            "Kansas City and St. Louis operate registration and zoning regimes that are more restrictive than the tourism markets.",
            "State and local sales tax plus local tourism taxes apply.",
            "Lower property tax rates and construction costs than comparable lake markets in the Northeast or Great Lakes give Missouri an unusually low cost basis for large lake properties.",
        ],
        cities=[
            ["Branson / Branson West", "Light regulation, established tourism economy", "Low"],
            ["Table Rock Lake shoreline", "Corps of Engineers controls dock permits separately", "Low, but verify dock rights"],
            ["Kansas City", "Registration and zoning requirements", "Moderate"],
            ["St. Louis", "Registration and permitting", "Moderate"],
        ],
        markets=['<a href="/markets/branson/">Branson</a>'],
        faqs=[
            ("Is Branson friendly to short-term rentals?",
             "Yes. Branson and Branson West have decades of tourism infrastructure and light regulation, and rental accommodation is an accepted part of the local economy."),
            ("Do dock rights transfer on Table Rock Lake?",
             "Not automatically. The shoreline is substantially managed by the Army Corps of Engineers, which controls dock permits. Verify the permit status and transferability separately from any short-term rental question."),
        ],
    ),
    dict(
        slug="alabama", state="Alabama", posture="Permissive on the Gulf Coast",
        blurb="Gulf Shores and Orange Beach operate established vacation rental economies with registration requirements.",
        lead="Alabama's Gulf Coast is one of the more straightforward beach markets in the country to operate in. Gulf Shores and Orange Beach have built their local economies around vacation rentals, and the regulatory framework reflects that rather than resisting it.",
        points=[
            "There is no restrictive statewide framework. The Gulf Coast cities regulate through registration, life safety and occupancy requirements rather than prohibition.",
            "Gulf Shores and Orange Beach require registration and business licensing, with occupancy and parking standards.",
            "State lodging tax plus city and county lodging taxes apply. Rates on the Gulf Coast are meaningful and should be modeled.",
            "Condominium associations are a substantial factor, since much of the beachfront inventory is condominium product with its own rental rules and rental program requirements.",
            "Coastal wind and flood insurance is a material cost that has repriced along with the rest of the Gulf.",
            "The market is family-oriented and heavily summer-weighted, with a shorter shoulder than the Florida Panhandle.",
        ],
        cities=[
            ["Gulf Shores", "Registration and business license; established rental economy", "Low"],
            ["Orange Beach", "Registration, occupancy and parking standards", "Low"],
            ["Birmingham / Huntsville", "Local zoning and registration", "Moderate"],
        ],
        markets=['<a href="/markets/gulf-shores/">Gulf Shores</a>'],
        faqs=[
            ("Are short-term rentals allowed in Gulf Shores?",
             "Yes. Gulf Shores and Orange Beach require registration and business licensing with occupancy and parking standards, but the local economies are built around vacation rentals rather than resisting them."),
            ("What is the biggest constraint on Alabama Gulf Coast rentals?",
             "Condominium association rules, since much of the beachfront inventory is condominium product with its own rental restrictions and in some cases mandatory rental program participation."),
        ],
    ),
    dict(
        slug="south-carolina", state="South Carolina", posture="Mixed, city by city",
        blurb="Myrtle Beach and Hilton Head operate established markets; Charleston is among the most restrictive in the Southeast.",
        lead="South Carolina spans the full range. Myrtle Beach and Hilton Head have long-established vacation rental economies with workable rules, while Charleston operates one of the most restrictive short-term rental frameworks in the Southeast.",
        points=[
            "There is no state preemption. Regulation is set locally and varies dramatically between the beach markets and the historic cities.",
            "Charleston restricts short-term rentals heavily, with owner-occupancy requirements in most of the city and a narrow set of eligible properties.",
            "Myrtle Beach and the Grand Strand operate established vacation rental economies with zoning that broadly accommodates rentals in tourist districts.",
            "Hilton Head permits short-term rentals with registration and operating standards, though private community rules are frequently the binding constraint.",
            "State sales tax plus local accommodations taxes apply.",
            "Beach community property owner association rules are often more restrictive than municipal ordinances and must be reviewed separately.",
        ],
        cities=[
            ["Myrtle Beach / Grand Strand", "Zoning accommodates rentals in tourist districts", "Low to moderate"],
            ["Hilton Head", "Registration and operating standards; community rules often decisive", "Moderate"],
            ["Charleston", "Owner-occupancy requirements; narrow eligibility", "Very high"],
        ],
        markets=[],
        faqs=[
            ("Can I run a short-term rental in Charleston?",
             "Only in narrow circumstances. Charleston imposes owner-occupancy requirements across most of the city and limits eligibility substantially, which makes conventional investment purchases difficult."),
            ("Is Myrtle Beach friendly to short-term rentals?",
             "Generally yes. The Grand Strand has a long-established vacation rental economy and zoning that broadly accommodates rentals in tourist districts."),
        ],
    ),
    dict(
        slug="north-carolina", state="North Carolina", posture="Favorable, with a key court decision",
        blurb="A 2021 appellate decision limited registration-based restrictions; coastal markets are well established.",
        lead="North Carolina became meaningfully more favorable for short-term rental operators after a 2021 appellate decision limited how cities can use registration and permitting to restrict rentals, relying on a state statute that constrains local regulation of residential rental property.",
        points=[
            "A 2021 North Carolina Court of Appeals decision involving the City of Wilmington held that portions of a short-term rental registration ordinance conflicted with a state statute limiting local regulation of residential rental property.",
            "The practical effect has been to constrain registry-and-lottery style restrictions, though cities retain zoning authority and can regulate through land use.",
            "The Outer Banks and the coastal counties have long-established vacation rental economies with straightforward operating frameworks.",
            "Asheville restricts whole-house short-term rentals substantially in residential districts, permitting homestays more readily than whole-unit rentals.",
            "State and local sales tax plus county occupancy taxes apply.",
            "Coastal insurance, including wind and flood, is a material cost on the Outer Banks and the southern coast.",
        ],
        cities=[
            ["Outer Banks / Dare County", "Established vacation rental economy", "Low"],
            ["Wilmington", "Registration ordinance narrowed by appellate decision", "Low to moderate"],
            ["Asheville", "Whole-house rentals restricted in residential districts", "High"],
            ["Charlotte", "Zoning-dependent", "Moderate"],
        ],
        markets=[],
        faqs=[
            ("Did a court decision change North Carolina short-term rental rules?",
             "Yes. A 2021 Court of Appeals decision involving Wilmington held that portions of a registration ordinance conflicted with a state statute limiting local regulation of residential rental property, which has constrained registry-based restrictions."),
            ("Can I run a whole-house short-term rental in Asheville?",
             "In most residential districts, no. Asheville permits homestays more readily than whole-unit short-term rentals, which limits conventional investment purchases in much of the city."),
        ],
    ),
    dict(
        slug="georgia", state="Georgia", posture="Local control, generally workable outside Atlanta",
        blurb="Blue Ridge and the North Georgia mountains are established markets; Atlanta requires owner occupancy.",
        lead="Georgia leaves short-term rental regulation to local governments. The North Georgia mountain markets around Blue Ridge and Ellijay have grown into substantial cabin rental economies with workable rules, while Atlanta has adopted a framework that effectively excludes conventional investment purchases.",
        points=[
            "There is no state preemption. Counties and cities set their own rules.",
            "Fannin and Gilmer counties, containing Blue Ridge and Ellijay, host large cabin rental markets serving Atlanta drive-to demand with comparatively light regulation.",
            "Atlanta requires a short-term rental license tied to a host's primary residence, which excludes most non-owner-occupied investment purchases.",
            "Savannah operates a permit program with density caps in the historic districts.",
            "State and local sales tax plus county excise and hotel-motel fees apply.",
            "The North Georgia markets depend heavily on Atlanta drive-to demand, roughly one and a half to two hours, which makes them sensitive to metro Atlanta economic conditions.",
        ],
        cities=[
            ["Blue Ridge / Fannin County", "Light regulation, established cabin market", "Low"],
            ["Ellijay / Gilmer County", "Light regulation", "Low"],
            ["Savannah", "Permit program with density caps in historic districts", "High"],
            ["Atlanta", "License tied to primary residence", "Very high for investors"],
        ],
        markets=[],
        faqs=[
            ("Can I buy an investment short-term rental in Atlanta?",
             "Generally not. Atlanta ties short-term rental licensing to a host's primary residence, which excludes most non-owner-occupied investment purchases."),
            ("Is Blue Ridge, Georgia a good short-term rental market?",
             "It is an established cabin market with comparatively light regulation, serving Atlanta drive-to demand roughly ninety minutes to two hours away. That dependence also makes it sensitive to metro Atlanta economic conditions."),
        ],
    ),
    dict(
        slug="nevada", state="Nevada", posture="Very restrictive in the Las Vegas area",
        blurb="Clark County and Las Vegas operate tightly capped licensing; Lake Tahoe's Nevada side varies by jurisdiction.",
        lead="Nevada is one of the harder states for short-term rental investing, because the Las Vegas metropolitan area, which contains most of the demand, operates under some of the most restrictive licensing regimes in the country.",
        points=[
            "Clark County adopted a licensing framework with a strict cap on the number of licenses, distance separation requirements between rentals, and substantial penalties for unlicensed operation.",
            "The City of Las Vegas and other incorporated cities within the valley operate their own restrictive frameworks with separation and density requirements.",
            "Demand in the Las Vegas market is very strong, which is precisely why the licensing is contested and why unlicensed operation carries meaningful enforcement risk.",
            "The Nevada side of Lake Tahoe, in Douglas and Washoe counties, operates permit programs that vary by jurisdiction and have tightened over time.",
            "Transient lodging tax applies at rates set locally.",
            "In Nevada more than most states, the licensing position is the entire question. A property that cannot obtain a license is worth its long-term rental value.",
        ],
        cities=[
            ["Clark County (unincorporated Las Vegas)", "Capped licensing with separation requirements", "Very high"],
            ["City of Las Vegas", "Restrictive licensing with density limits", "Very high"],
            ["Lake Tahoe, Nevada side", "Permit programs varying by county", "High"],
            ["Reno", "Permit program with separation requirements", "High"],
        ],
        markets=['<a href="/markets/lake-tahoe/">Lake Tahoe</a>'],
        faqs=[
            ("Can I run a short-term rental in Las Vegas?",
             "Only with a license, and licenses are capped with distance separation requirements between rentals. Enforcement against unlicensed operation carries substantial penalties, so the licensing position has to be confirmed before purchase."),
            ("Is the Nevada side of Lake Tahoe easier than the California side?",
             "Not necessarily. Douglas and Washoe counties operate their own permit programs that have tightened over time. Both sides of the lake require verifying the specific jurisdiction's current rules."),
        ],
    ),
    dict(
        slug="new-york", state="New York", posture="Effectively prohibitive in New York City",
        blurb="NYC Local Law 18 ended most short-term rentals in the city; upstate markets are governed locally.",
        lead="New York splits sharply. New York City has effectively ended conventional short-term rental operation through a registration law that platforms must enforce, while upstate vacation markets in the Catskills, Adirondacks and Finger Lakes are governed by local rules that vary widely.",
        points=[
            "New York City Local Law 18 requires host registration and prohibits booking platforms from processing transactions for unregistered listings. Combined with existing multiple dwelling law, it has effectively ended most short-term rental activity in the city.",
            "The city's rules require the host to be present during the stay and limit occupancy to two guests, which excludes conventional whole-unit investment rentals.",
            "Upstate markets are regulated at the town and county level, with substantial variation. Several Catskills and Hudson Valley towns have adopted permit caps.",
            "Some upstate lake and Adirondack communities have adopted restrictions in response to housing pressure.",
            "State and local sales tax plus county occupancy taxes apply.",
            "For investors, New York City should be treated as closed to conventional short-term rental investment, and upstate purchases require town-level verification.",
        ],
        cities=[
            ["New York City", "Local Law 18 registration; host presence required", "Effectively closed"],
            ["Catskills towns", "Permit programs, several with caps", "Moderate to high"],
            ["Hudson Valley", "Town-level rules, varying widely", "Moderate"],
            ["Adirondacks / Lake George", "Local permit programs", "Moderate"],
        ],
        markets=[],
        faqs=[
            ("Are Airbnbs legal in New York City?",
             "Conventional whole-unit short-term rentals are effectively prohibited. Local Law 18 requires host registration, bars platforms from processing unregistered bookings, requires the host to be present, and limits occupancy to two guests."),
            ("Where can I invest in short-term rentals in New York State?",
             "Upstate vacation markets in the Catskills, Hudson Valley, Adirondacks and Finger Lakes, subject to town-level rules that vary widely and in several cases include permit caps."),
        ],
    ),
    dict(
        slug="michigan", state="Michigan", posture="Contested, no state preemption",
        blurb="Repeated preemption bills have failed; lakeshore townships regulate independently and have tightened.",
        lead="Michigan has debated statewide short-term rental preemption repeatedly without enacting it, leaving regulation to townships and municipalities. The lakeshore communities that contain most of the vacation rental demand have generally tightened rather than loosened.",
        points=[
            "No state preemption statute has been enacted despite repeated legislative attempts, so township and municipal zoning controls.",
            "Lake Michigan shoreline communities, including South Haven, Saugatuck and the Traverse City area, have adopted registration requirements, caps or density limits in various forms.",
            "Michigan courts have addressed whether short-term rental use is consistent with residential zoning classifications, and outcomes have depended on the specific ordinance language.",
            "Deed restrictions and homeowner association rules are frequently the binding constraint in lakeshore subdivisions.",
            "Use tax and local assessments apply; Michigan does not impose a broad statewide lodging tax comparable to some other states, but local assessments vary.",
            "The season is short in most of the state, roughly Memorial Day through Labor Day outside the ski markets, which requires a purchase basis that reflects fourteen productive weeks.",
        ],
        cities=[
            ["Traverse City area", "Registration and density limits in some districts", "Moderate to high"],
            ["South Haven / Saugatuck", "Registration and caps adopted in various forms", "High"],
            ["Northern Michigan ski areas", "Township-level rules", "Moderate"],
        ],
        markets=[],
        faqs=[
            ("Does Michigan have a statewide short-term rental law?",
             "No. Preemption bills have been introduced repeatedly without passing, so township and municipal zoning controls. Lakeshore communities have generally tightened rather than loosened."),
            ("How long is the Michigan rental season?",
             "Outside the ski markets, roughly Memorial Day through Labor Day, about fourteen productive weeks. A purchase basis has to reflect that rather than being set by peak July nightly rates."),
        ],
    ),
    dict(
        slug="hawaii", state="Hawaii", posture="Highly restrictive across all islands",
        blurb="Each county restricts sharply; Maui and Oahu have moved to eliminate much existing inventory.",
        lead="Hawaii is the most restrictive short-term rental environment in the United States. Each county regulates independently and all four have moved toward restriction, with Maui and Oahu taking significant steps to reduce existing inventory rather than merely limiting new entrants.",
        points=[
            "Regulation is set at the county level and all counties restrict substantially. There is no favorable statewide framework.",
            "Honolulu County, covering Oahu, adopted rules extending minimum stay requirements and limiting short-term rentals largely to resort-zoned areas.",
            "Maui County has pursued policy aimed at phasing out a substantial portion of existing transient vacation rental inventory in apartment-zoned districts.",
            "Kauai and Hawaii County restrict rentals largely to visitor destination areas and designated zones.",
            "Transient accommodations tax plus county surcharges apply at high effective rates.",
            "For investors, the practical guidance is that only resort-zoned or specifically designated properties should be considered, and even those carry policy risk that is unusually elevated by mainland standards.",
        ],
        cities=[
            ["Oahu / Honolulu County", "Restricted largely to resort zones; extended minimum stays", "Very high"],
            ["Maui County", "Policy aimed at phasing out apartment-district inventory", "Very high"],
            ["Kauai", "Limited to visitor destination areas", "Very high"],
            ["Hawaii County (Big Island)", "Designated zones only", "High"],
        ],
        markets=[],
        faqs=[
            ("Can I invest in a short-term rental in Hawaii?",
             "Only in resort-zoned or specifically designated properties, and even those carry elevated policy risk. All four counties restrict substantially, and Maui and Oahu have moved to reduce existing inventory rather than only limiting new entrants."),
            ("Why is Hawaii so restrictive?",
             "Housing supply pressure on the islands is acute, and county governments have responded by restricting transient vacation rental use in residential and apartment districts."),
        ],
    ),
    dict(
        slug="idaho", state="Idaho", posture="Favorable, with state preemption of bans",
        blurb="State law prevents outright local prohibition; McCall, Sun Valley and Coeur d'Alene regulate operationally.",
        lead="Idaho is among the more favorable states, because state law prevents local governments from prohibiting short-term rentals outright. Cities retain authority to regulate for health, safety and welfare, which most of the resort communities have used, but the outright ban risk that affects Colorado and California resort towns is not present.",
        points=[
            "Idaho Code generally prohibits counties and cities from enacting ordinances that expressly or effectively prohibit short-term rental or vacation rental operation.",
            "Local governments may still regulate to safeguard public health, safety and general welfare, including licensing and life safety requirements.",
            "McCall, Sun Valley, Ketchum and Coeur d'Alene have adopted operating requirements and licensing while remaining unable to ban outright.",
            "Local option sales and lodging taxes apply in resort communities, and rates vary.",
            "Homeowner association restrictions apply independently of the state preemption, and resort-area associations frequently restrict rentals.",
            "The combination of state preemption and strong resort demand has made Idaho comparatively attractive relative to neighboring mountain states.",
        ],
        cities=[
            ["McCall", "Licensing and operating standards; no outright ban", "Low to moderate"],
            ["Sun Valley / Ketchum", "Licensing and operating standards", "Low to moderate"],
            ["Coeur d'Alene", "Licensing and life safety requirements", "Low"],
            ["Boise", "Registration and operating standards", "Low to moderate"],
        ],
        markets=[],
        faqs=[
            ("Can Idaho cities ban short-term rentals?",
             "Generally no. Idaho Code prohibits counties and cities from enacting ordinances that expressly or effectively prohibit short-term or vacation rental operation, though they may regulate for health, safety and general welfare."),
            ("Does Idaho preemption override HOA rules?",
             "No. Homeowner association restrictions operate independently of the state statute, and resort-area associations frequently restrict short-term rentals."),
        ],
    ),
    dict(
        slug="montana", state="Montana", posture="Favorable, with local zoning control",
        blurb="No restrictive state framework; Whitefish, Bozeman and Big Sky regulate through zoning and permits.",
        lead="Montana has no restrictive statewide short-term rental framework, and the resort communities regulate through zoning and permitting rather than prohibition. Housing pressure in Bozeman and Whitefish has driven tightening in residential districts, while resort-zoned inventory remains workable.",
        points=[
            "There is no restrictive state framework. Cities and counties regulate through zoning, permitting and life safety requirements.",
            "Whitefish and Bozeman have adopted restrictions in residential districts in response to housing supply pressure, while permitting rentals in resort and commercial zones.",
            "Big Sky, in unincorporated Gallatin and Madison counties, has comparatively light regulation and a substantial resort rental economy.",
            "Montana has no general statewide sales tax, but a lodging facility use tax and lodging sales tax apply to short-term accommodation.",
            "Homeowner association and resort community rules are frequently the binding constraint in ski-adjacent inventory.",
            "The state is our own registered address, and the mountain markets have a genuine two-season profile with summer park traffic and winter ski demand.",
        ],
        cities=[
            ["Big Sky (unincorporated)", "Light regulation, substantial resort rental economy", "Low"],
            ["Whitefish", "Restricted in residential districts, permitted in resort zones", "Moderate"],
            ["Bozeman", "Tiered permit classes with residential restrictions", "Moderate to high"],
            ["Missoula", "Permit requirements", "Moderate"],
        ],
        markets=[],
        faqs=[
            ("Does Montana restrict short-term rentals statewide?",
             "No. There is no restrictive state framework. Cities and counties regulate through zoning and permitting, and housing pressure has driven tightening in Bozeman and Whitefish residential districts."),
            ("Is there lodging tax in Montana?",
             "Montana has no general statewide sales tax, but a lodging facility use tax and a lodging sales tax apply to short-term accommodation."),
        ],
    ),
]


def render_state(s):
    slug = s["slug"]
    rows = [[c, r, x] for c, r, x in s["cities"]]
    sections = [
        ("Where the state stands", [
            ("warn", VERIFY),
            *[f"<strong>{p.split('.')[0]}.</strong>{'.'.join(p.split('.')[1:])}" if False else p
              for p in s["points"][:3]],
        ]),
        ("The details that matter", [
            ("ul", s["points"][3:]),
        ]),
        ("City and county positions", [
            f"Regulation in {s['state']} is decided locally far more than at the state level. The table below is orientation, not a substitute for calling the jurisdiction.",
            ("table", ["Jurisdiction", "Position", "Investor risk"], rows),
        ]),
        ("How to verify before you write an offer", [
            "The verification sequence is the same in every state, and skipping any step is how buyers end up owning a property that cannot legally operate.",
            ("ol", [
                "Confirm the zoning designation for the specific parcel, not the neighborhood.",
                "Confirm whether short-term rental is an allowed use in that zone, and whether a permit is required.",
                "Confirm whether permits are capped, waitlisted, or transferable on sale.",
                "Read the homeowner association or condominium declaration in full. Private restrictions bind independently of any municipal rule.",
                "Confirm the lodging and occupancy tax registration obligations, and which taxes the booking platform collects on your behalf.",
                "Ask the jurisdiction directly, in writing, and keep the response.",
            ]),
            "We do this for every property we bring to a client before an offer goes out, because a property that cannot legally operate is worth its long-term rental value regardless of what the short-term proforma says.",
        ]),
    ]
    related = (s["markets"] + [
        '<a href="/regulations/">Short-term rental rules in other states</a>',
        '<a href="/property-types/city/">Why the permit is the asset in urban markets</a>',
        '<a href="/revenue-projections/">Modeling the long-term rental floor</a>',
    ])
    return guide(
        slug=slug, parent="/regulations/", parent_name="Regulations",
        title=f"{s['state']} Short-Term Rental Laws & Regulations (2026)",
        h1=f"{s['state']} Short-Term Rental Regulations",
        eyebrow=f"{s['state']} Regulations",
        description=f"How {s['state']} regulates short-term rentals in 2026: {s['posture'].lower()}. City positions, permit requirements, tax obligations and what to verify before you buy.",
        lead=s["lead"],
        sections=sections, faqs=s["faqs"], related=related,
        read_min=8, section_name="STR Regulations",
        cta=("Buying in a market you do not know yet?",
             "We verify zoning, permits and association rules on every property before an offer goes out."),
    )


def main():
    for s in STATES:
        write(f"/regulations/{s['slug']}/", render_state(s))

    write("/regulations/", hub(
        path="/regulations/",
        title="Short-Term Rental Regulations by State (2026)",
        h1="Short-term rental rules, state by state",
        eyebrow="Regulations",
        description="Short-term rental regulation summaries for 20 states: preemption laws, permit caps, city positions, tax obligations and what to verify before writing an offer.",
        sub="Regulation is the risk that does not show up in a revenue projection. These summaries cover where each state stands, which cities are workable, and the verification sequence we run before any offer goes out.",
        cards=[(f"/regulations/{s['slug']}/", s["state"], s["blurb"]) for s in STATES],
        sections=[
            ("The four regulatory postures", [
                "Every jurisdiction falls into roughly one of four positions, and knowing which one you are in tells you most of what you need about the risk.",
                ("ul", [
                    "<strong>State preemption of bans.</strong> Arizona and Idaho prevent local governments from prohibiting short-term rentals outright. This is the strongest protection available and it removes the largest single risk.",
                    "<strong>Local control, light regulation.</strong> Oklahoma, Missouri, Alabama's Gulf Coast and much of rural Texas. Workable, but nothing prevents a future tightening.",
                    "<strong>Local control, permit caps.</strong> Colorado ski towns, California desert markets, Nevada's Las Vegas metro, Nashville's non-owner-occupied zones. A permit here is a genuine asset because supply is capped, and a property without one may not be able to get one.",
                    "<strong>Effectively prohibitive.</strong> New York City, Denver, Atlanta and Charleston for non-owner-occupied purchases, and most of Hawaii. These are closed to conventional investment regardless of the numbers.",
                ]),
                "A permit cap is worth understanding properly, because it cuts both ways. It is a barrier to entry when you are buying and a moat once you are in. Nashville's zoning-restricted non-owner-occupied permits protect existing operators from exactly the supply growth that compresses rates in unregulated markets.",
            ]),
            ("The verification sequence", [
                "We run the same six steps on every property before an offer goes out, in every state.",
                ("ol", [
                    "Zoning designation for the specific parcel, not the neighborhood.",
                    "Whether short-term rental is an allowed use in that zone, and whether a permit is required.",
                    "Whether permits are capped, waitlisted, or transferable on sale.",
                    "The homeowner association or condominium declaration, read in full.",
                    "Lodging and occupancy tax registration obligations, and which taxes the platform collects.",
                    "Written confirmation from the jurisdiction, retained.",
                ]),
                "The homeowner association step is the one buyers skip most often and the one that most often kills a deal after closing. A private covenant binds independently of any municipal rule, and state preemption statutes in Arizona and Idaho do not override it.",
            ]),
        ],
        faqs=[
            ("Which states are best for short-term rental investing?",
             "On regulation alone, Arizona and Idaho lead because state law prevents local governments from banning short-term rentals outright. Tennessee, Oklahoma, Missouri and much of Florida and Texas are also workable, though for different structural reasons."),
            ("Which states are hardest for short-term rental investors?",
             "Hawaii, California and Nevada's Las Vegas metro, plus specific cities including New York City, Denver, Atlanta and Charleston, where non-owner-occupied short-term rentals are effectively excluded."),
            ("Do state preemption laws override homeowner association rules?",
             "No. Private covenants bind independently. Arizona and Idaho preempt municipal bans but do not affect an HOA or condominium declaration, which has to be read separately for every purchase."),
            ("What should I verify before buying a short-term rental?",
             "Parcel zoning, whether STR is an allowed use, whether permits are capped or transferable, the full HOA or condo declaration, lodging tax registration obligations, and written confirmation from the jurisdiction that you retain."),
        ],
        related=[
            '<a href="/markets/">Market analyses</a>',
            '<a href="/property-types/city/">Urban STRs and permit risk</a>',
            '<a href="/revenue-projections/">Modeling the long-term rental floor</a>',
            '<a href="/case-studies/">Client case studies by market</a>',
        ],
        list_name="Short-Term Rental Regulations by State",
    ))
    print(f"regulations: {len(STATES)} states + hub")


if __name__ == "__main__":
    main()
