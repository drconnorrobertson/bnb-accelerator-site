#!/usr/bin/env python3
"""Property type guides: beach, mountain, lake, city, ski, desert."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpl
from pillars import guide, hub, write

P = "/property-types/"

TYPES = [
    dict(
        slug="beach",
        name="Beach STRs",
        eyebrow="Beach Properties",
        h1="Beach Short-Term Rentals: What Actually Drives the Numbers",
        title="Beach Short-Term Rental Investing Guide (2026)",
        description="How beach STRs actually perform: why walking distance to sand outweighs square footage, what coastal insurance really costs, and which Gulf and Atlantic markets price best.",
        blurb="Distance to sand, insurance repricing, and why the Gulf outperforms the Atlantic on cash-on-cash.",
        lead="Beach short-term rentals are the most requested property type we underwrite and the one where buyers most consistently misjudge the cost side. The revenue is real. So is coastal insurance, so is the assessment risk, and so is the fact that a house four blocks from the sand and a house one block from the sand are not the same asset at any price.",
        sections=[
            ("The one variable that outranks everything else", [
                "In every beach market we transact in, walking distance to a public beach access point moves nightly rate more than square footage, finish level, bedroom count relative to comparables, or anything else you can change with money. A four-bedroom one block back can command 30% or more over an otherwise identical four-bedroom four blocks back.",
                "That gap is permanent. You can renovate a kitchen, add a pool, upgrade the photography and fix bad pricing. You cannot move the house closer to the water. When we underwrite a beach property, distance to access is the first filter, and a property that fails it does not get a second look regardless of how well it shows.",
                "The corollary matters for buyers on a budget. A smaller property close to the beach will almost always outperform a larger property further back at the same purchase price. Buyers instinctively optimize for bedrooms because bedrooms are easy to count. The market pays for the walk.",
            ]),
            ("Gulf Coast versus Atlantic economics", [
                "The Gulf Coast generally produces better cash-on-cash returns than the Atlantic at comparable latitudes, for two reasons. The Gulf's season runs longer, with water warm enough to sustain an autumn shoulder into October that most Atlantic markets lose in September. And Gulf purchase prices outside the top tier of 30A are materially lower for a comparable guest experience.",
                "Within the Gulf, the spread between submarkets is wide. Destin and 30A sit at the top on both nightly rate and price. Fort Walton Beach and Panama City Beach sell the same Emerald Coast water at a much lower basis, which is why our clients have bought in both. Southwest Florida markets like Fort Myers and Cape Coral invert the calendar entirely, peaking in February on snowbird demand rather than in July.",
                ("table", ["Submarket", "Character", "Typical entry", "Peak season"], [
                    ["Destin, FL", "Premium Emerald Coast", "$900K to $1.2M for 4-5BR", "Summer, long shoulder"],
                    ["Fort Walton Beach, FL", "Value Emerald Coast", "$600K to $700K for 4BR", "Summer plus base traffic"],
                    ["Panama City Beach, FL", "Value Gulf, long season", "$500K to $600K for 4BR", "Spring break to October"],
                    ["Fort Myers / Cape Coral, FL", "Snowbird waterfront", "$700K to $1.7M", "January to March"],
                    ["Gulf Shores, AL", "Family Gulf market", "$500K to $800K", "Summer"],
                ]),
            ]),
            ("The cost side buyers underestimate", [
                "Coastal insurance has repriced sharply across Florida and the Gulf in recent years. Wind and flood coverage on a beach property is now a material line item that can run several times what an inland property of the same value pays. A proforma that carries an inland insurance assumption will overstate cash flow by thousands of dollars a year.",
                "Association assessments are the second surprise. Condominium and homeowner associations in coastal Florida can issue large special assessments after a storm season or in response to structural reserve requirements. These arrive as one-time bills, not as a smooth monthly line, and they can absorb a full quarter of cash flow.",
                "Turnover cost also runs higher at the beach than most buyers expect. Sand, salt and humidity are hard on interiors, linens and outdoor furniture, and beach properties turn more frequently in peak season than mountain properties do. Budget replacement cycles accordingly rather than assuming a ten-year furniture life.",
                ("warn", "Hurricane exposure is not just an insurance question. A named storm can close a market to bookings for weeks and disrupt an entire peak season. Model a disrupted year, not just an average one, before committing to a coastal purchase."),
            ]),
            ("Bedroom count and the guest bracket", [
                "The single highest-leverage step in most beach markets is three bedrooms to four. Three bedrooms is a family. Four is two families splitting a week, and the second household roughly doubles the willingness to pay because the cost divides.",
                "The step from four to five repeats the pattern with a thinner competitive set, because most beach housing stock is two to four bedrooms. Our client Tiffany bought a five-bedroom in Destin at $1,100,000 partly for that reason. Mark and Farrah bought a four-bedroom in the same market at $950,000 targeting the more liquid bracket.",
                "Above five bedrooms in a beach market the economics get less reliable. Very large beach houses exist but the group that books them is a narrower slice of demand than the equivalent group in the Smokies, where large-cabin culture is established.",
            ]),
            ("Amenities that pay for themselves", [
                ("ul", [
                    "<strong>Private heated pool.</strong> In Florida and the Gulf this is close to mandatory above the entry tier. Heating specifically matters because the snowbird and spring shoulder seasons have cool evenings.",
                    "<strong>Outdoor shower.</strong> Cheap, universally mentioned in reviews, and it materially reduces sand damage to interiors.",
                    "<strong>Covered outdoor living space.</strong> Gulf afternoons produce daily summer thunderstorms. Covered space keeps guests outside and shows well in photography.",
                    "<strong>Beach gear.</strong> Chairs, umbrellas, a wagon and boogie boards cost a few hundred dollars and remove a friction point that guests otherwise pay a rental company for.",
                    "<strong>Reliable, fast wifi.</strong> Remote workers extend shoulder-season stays, and they will not book a property with vague internet claims.",
                ]),
            ]),
        ],
        faqs=[
            ("Are beach short-term rentals a good investment in 2026?",
             "They can be, though the cost side has changed. Coastal insurance has repriced sharply and association assessments have become a real risk. The markets that still work are the ones where purchase price has not risen as fast as nightly rate, which currently favors value Gulf submarkets over premium Atlantic ones."),
            ("How much does distance to the beach affect nightly rate?",
             "Substantially. A property one block from a beach access point can command 30% or more over an otherwise identical property four blocks back. That gap is permanent because the house cannot be moved, which is why access distance is our first underwriting filter."),
            ("What is the best bedroom count for a beach rental?",
             "Four is the highest-leverage count in most beach markets, because it moves the property from serving one family to serving two families splitting a week. Five works in markets with thin five-bedroom inventory. Above five, the demand pool narrows faster than the rate rises."),
            ("How much should I budget for coastal insurance?",
             "Far more than an inland property of the same value. Wind and flood coverage on Gulf and Atlantic coastal property has repriced sharply, and it should be quoted for the specific address before an offer, not estimated from a percentage rule of thumb."),
        ],
        related=[
            '<a href="/markets/destin/">Destin market analysis</a>',
            '<a href="/markets/panama-city-beach/">Panama City Beach market analysis</a>',
            '<a href="/case-studies/mark-farrah-destin-fl-4br/">Case study: a 4BR Destin beach house at $950,000</a>',
            '<a href="/case-studies/ashley-billy-fort-walton-beach-fl/">Case study: 80 nights booked in 21 days</a>',
            '<a href="/revenue-projections/">How to build a revenue projection you can trust</a>',
        ],
    ),
    dict(
        slug="mountain",
        name="Mountain Cabins",
        eyebrow="Mountain Properties",
        h1="Mountain Cabin Short-Term Rentals: The Smokies Playbook",
        title="Mountain Cabin STR Investing Guide (2026)",
        description="Why the Smokies is the highest-volume STR market in America, how amenity fit beats square footage, and why a $20K peak month is not a $240K year.",
        blurb="Amenity fit over square footage, and why peak-month numbers mislead on seasonal mountain inventory.",
        lead="Mountain cabins produce the biggest headline numbers in short-term rental investing and the most misleading ones. A nine-bedroom Smokies cabin that clears $20,000 in June does not clear $240,000 for the year, and the buyers who get hurt in this asset class are almost always the ones who annualized a peak month.",
        sections=[
            ("Why the Smokies dominates", [
                "Great Smoky Mountains National Park receives more annual visitors than any other national park in the United States, roughly double the second-place park. That single fact explains why the Sevierville, Pigeon Forge and Gatlinburg corridor supports more short-term rental inventory than any comparable region in the country, and why it can absorb new supply that would flood a smaller market.",
                "It is our most-transacted market. Victoria's nine-bedroom at $1,375,000, Vishal's five-bedroom at $1,250,000, Alfredo and Millie's four-bedroom at $865,000 and Adam's four-bedroom at $775,000 are all in the same corridor and all serve different guest brackets.",
                "Tennessee also levies no state income tax on wages. That does not change the federal treatment of the property, but it removes a layer of state-level complexity that a comparable purchase in California or New York would carry.",
            ]),
            ("Amenity fit beats square footage", [
                "In mountain markets the amenity set is close to standardized, and that is exactly why it matters. Hot tub, mountain view, and game room are what the comparable inventory has. A cabin missing any one of them is priced against properties that have all three, and it loses.",
                "An extra 400 square feet moves the nightly rate far less than a hot tub does. When we underwrite a cabin, we price the amenity gap against the actual comparable set and fund it at purchase. Treating it as an optional later upgrade is how a first year underperforms.",
                ("ul", [
                    "<strong>Hot tub.</strong> Effectively mandatory. The single most searched amenity filter in the market.",
                    "<strong>Mountain view.</strong> Cannot be added. Verify it from the actual deck, not from the listing photo angle.",
                    "<strong>Game room.</strong> Pool table, arcade cabinet, theater seating. Drives both rate and length of stay.",
                    "<strong>Fireplace and covered deck.</strong> Extends the usable shoulder season into winter.",
                    "<strong>Reliable road access.</strong> Steep gravel switchbacks lose bookings and generate refund requests in winter.",
                ]),
            ]),
            ("Bedroom count and which calendar you are buying", [
                "Large-bedroom-count cabins produce the highest gross revenue and the narrowest calendar. A nine-bedroom competes for reunions, corporate retreats and multi-family trips, and there are only so many twenty-six-person groups in a given month. When those bookings land, they are enormous. When they do not, the cabin sits.",
                "A four-bedroom serves two families, a small friend group or a couple with in-laws, and that demand exists every week of the season. The revenue ceiling is much lower and the occupancy floor is much higher.",
                "For a first purchase we generally steer toward four and five bedrooms. The steadiness is worth more than the peak, and the acquisition cost and turnover complexity are both dramatically lower.",
                ("table", ["Bedrooms", "Primary guest", "Revenue profile"], [
                    ["3 to 4", "Couples, small families", "Steady occupancy, moderate rate"],
                    ["5 to 6", "Two families, friend groups", "Best balance of rate and consistency"],
                    ["7 to 9", "Reunions, retreats, weddings", "Highest peak, narrowest calendar"],
                ]),
            ]),
            ("Reading a seasonal calendar honestly", [
                "Smokies revenue concentrates between June and October, with a second spike over the winter holidays. January through March is thin. A model built on the annual shape of the market survives that. A model built by multiplying a June figure by twelve does not.",
                "This is the single most common underwriting error we see in mountain markets, and it is usually the seller's proforma that introduces it. Listing packets are routinely assembled from peak-season rates extrapolated across the year, producing a revenue figure the property will never hit.",
                ("warn", "When a seller supplies a proforma, treat it as a marketing document. Underwrite against actual booked-night data for genuinely comparable inventory in the same corridor, not against the seller's spreadsheet."),
            ]),
            ("Location within the corridor", [
                "Sevierville, Pigeon Forge and Gatlinburg are discussed as one market and they are not. Drive time to the Parkway, to Dollywood and to the national park entrance moves nightly rates materially. Two cabins with identical specifications ten minutes apart can sit in different pricing tiers.",
                "Gatlinburg proper is closest to the park entrance and carries the most walkable-town demand. Pigeon Forge is the entertainment core around Dollywood. Sevierville spreads wider, with more land, larger cabins and a lower price per square foot, which is why most of our large-cabin transactions happen there.",
                "Beyond the Smokies, the same principles apply in Broken Bow, Oklahoma, where the top tier is luxury A-frames competing on architecture, and in Big Bear and the Poconos, where ski access adds a winter season the Smokies does not have.",
            ]),
        ],
        faqs=[
            ("Is a peak month representative of a mountain cabin's annual performance?",
             "No, and treating it as one is the most common way buyers overpay. Smokies revenue concentrates between June and October with a holiday spike, and January through March is thin. A $20,000 June is not a $240,000 year."),
            ("What amenities matter most in a Smoky Mountain cabin?",
             "Hot tub, mountain view and game room, in that order, plus a fireplace and reliable road access. The amenity set is close to standardized, so a cabin missing one is priced against properties that have all three."),
            ("How many bedrooms should a first mountain cabin have?",
             "Four or five for most first-time buyers. Large lodges have a higher revenue peak but a much narrower booking calendar, higher acquisition cost and more complex turnover. Four to five bedrooms has demand every week of the season."),
            ("Are Sevierville, Pigeon Forge and Gatlinburg the same market?",
             "No. Drive time to the Parkway, Dollywood and the park entrance moves rates materially. Gatlinburg is closest to the park, Pigeon Forge is the entertainment core, and Sevierville has more land and larger cabins at a lower price per square foot."),
        ],
        related=[
            '<a href="/markets/smoky-mountains/">Smoky Mountains market analysis</a>',
            '<a href="/markets/gatlinburg/">Gatlinburg market analysis</a>',
            '<a href="/case-studies/victoria-sevierville-tn-9br-cabin/">Case study: a 9BR cabin that cleared $20K in a month</a>',
            '<a href="/case-studies/adam-sevierville-tn-4br/">Case study: a 4BR Sevierville cabin at $775,000</a>',
            '<a href="/property-types/ski/">Ski property short-term rentals</a>',
        ],
    ),
    dict(
        slug="lake",
        name="Lake Houses",
        eyebrow="Lake Properties",
        h1="Lake House Short-Term Rentals: Waterfront, Dock Rights and Drive Markets",
        title="Lake House STR Investing Guide (2026)",
        description="What separates a lake house that books from one that does not: dock rights, water frontage versus lake access, drive-market catchment, and the short season problem.",
        blurb="Dock rights, frontage versus access, and why a short season demands a lower purchase basis.",
        lead="Lake houses are the most misunderstood property type in short-term rental investing, because the word lake covers assets that behave nothing like each other. A house on the water with a private dock and a house half a mile from a public boat ramp are described identically in listings and produce completely different revenue.",
        sections=[
            ("Frontage, access, and the difference that decides the deal", [
                "Direct water frontage with a private dock is a different asset class from lake access. Frontage means guests walk out the back door to the water. Access means a shared community launch, a deeded easement, or a short drive. Guests booking a lake house are booking the water, and they pay for immediacy.",
                "Dock rights are the specific item to verify before an offer. Many lakes, particularly those managed by the Army Corps of Engineers or a utility authority, restrict private dock permits, and an existing dock does not always transfer with a sale. A property marketed as having a dock where the permit is non-transferable is worth substantially less than the listing implies.",
                ("ul", [
                    "Confirm the dock permit exists, is current, and transfers on sale.",
                    "Confirm whether the shoreline is privately owned or subject to a flowage easement.",
                    "Check the controlling authority's rules on boat lifts, slips and swim platforms.",
                    "Verify the water level management regime, since drawdown lakes can leave docks dry for part of the year.",
                ]),
            ]),
            ("Drive-market catchment is the demand engine", [
                "Almost no lake market is a fly-to destination. Lake demand is drive-to, which means the size and wealth of the metro within two to four hours is the demand engine, and everything else is detail.",
                "Table Rock Lake near Branson West draws from Kansas City, St. Louis, Tulsa and Northwest Arkansas. Our client Dustin bought an eight-bedroom there at $930,900, and the property benefits from a second demand driver in Branson's entertainment corridor that pure lake markets do not have.",
                "The Poconos work on the same logic at a much larger scale. Roughly thirty million people live within a two-hour drive from New York and Philadelphia. Julie's five-bedroom in Pocono Lake at $880,000 sits inside that radius, which is why the property books groups on three weeks' notice.",
                "Drive-to demand has a specific advantage worth understanding: it holds up when airfare rises or discretionary travel budgets tighten. A family that cancels a flight to Europe still drives three hours to a lake house.",
            ]),
            ("The short season problem", [
                "Most lake markets have a genuinely short season. In the upper Midwest and Northeast, meaningful lake demand runs from Memorial Day to Labor Day, roughly fourteen weeks. A property that earns well for fourteen weeks and nothing for thirty-eight has to be bought at a basis that reflects that.",
                "This is where lake investing goes wrong. Buyers see strong July nightly rates, compare them favorably to a beach market, and pay a price that would only work with a beach market's season length.",
                "Markets that solve the problem have a second driver. Branson has the entertainment corridor. The Poconos have skiing at Camelback and Blue Mountain plus autumn foliage. Lake Tahoe has a full winter ski season that rivals its summer. Smith Mountain Lake and Lake Norman have mild enough climates to extend into spring and autumn shoulders.",
                ("table", ["Lake market", "Second driver", "Effective season"], [
                    ["Poconos, PA", "Ski, foliage, NYC drive", "Close to year round"],
                    ["Lake Tahoe, CA/NV", "Major ski resorts", "Two full seasons"],
                    ["Table Rock / Branson West, MO", "Branson entertainment", "Summer plus autumn groups"],
                    ["Upper Midwest lakes", "None typically", "About 14 weeks"],
                ]),
            ]),
            ("What lake guests actually book", [
                ("ul", [
                    "<strong>Dock and water toys.</strong> Kayaks, paddleboards and a swim platform convert lookers into bookers. Boat storage or a slip is a genuine differentiator.",
                    "<strong>Large gathering space.</strong> Lake trips are group trips. Open kitchen and dining that seats everyone matters more than bedroom luxury.",
                    "<strong>Outdoor cooking and fire pit.</strong> The lake evening is the product. A grill, covered deck and fire pit are consistently mentioned in reviews.",
                    "<strong>Bunk configurations.</strong> Sleeping capacity above bedroom count works at the lake in a way it does not at a premium beach house.",
                    "<strong>Air conditioning.</strong> Older lake cottages frequently lack it, and a hot July week without it produces refund requests.",
                ]),
                ("warn", "Older lake houses often carry deferred maintenance that is invisible in summer photography: septic systems near capacity, well water issues, seawall or bank erosion, and non-permitted additions. These are the properties most likely to look like a bargain and cost the most to bring to rental standard."),
            ]),
        ],
        faqs=[
            ("What is the difference between lake frontage and lake access?",
             "Frontage means the property is on the water, typically with a dock. Access means a shared launch, deeded easement or short drive. Guests book the water and pay for immediacy, so the two are different asset classes even when listings describe them the same way."),
            ("Do dock rights transfer when a lake property sells?",
             "Not always. Many lakes managed by the Army Corps of Engineers or a utility authority restrict private dock permits, and an existing dock does not guarantee a transferable permit. Verify the permit status before writing an offer."),
            ("How long is a typical lake rental season?",
             "In the upper Midwest and Northeast, roughly fourteen weeks from Memorial Day to Labor Day. Markets with a second demand driver such as skiing, foliage or a nearby entertainment corridor run much longer, which is why they support higher purchase prices."),
            ("What makes a drive-to lake market resilient?",
             "The size and wealth of the metro within two to four hours. Drive-to demand books later and shorter than fly-to demand, and it holds up better when airfare rises or travel budgets tighten."),
        ],
        related=[
            '<a href="/markets/poconos/">Poconos market analysis</a>',
            '<a href="/markets/branson/">Branson market analysis</a>',
            '<a href="/case-studies/dustin-branson-west-mo-8br/">Case study: an 8BR Table Rock Lake house</a>',
            '<a href="/case-studies/julie-pocono-lake-pa-5br/">Case study: a 5BR Pocono Lake house</a>',
            '<a href="/property-types/mountain/">Mountain cabin short-term rentals</a>',
        ],
    ),
    dict(
        slug="city",
        name="City STRs",
        eyebrow="Urban Properties",
        h1="City Short-Term Rentals: Permits, Compression Nights and the Long-Term Rental Floor",
        title="Urban Short-Term Rental Investing Guide (2026)",
        description="Why urban STR permits are the asset, how compression nights drive city revenue, and why every city property needs a long-term rental floor in the model.",
        blurb="The permit is the asset. Model the long-term rental floor before you buy.",
        lead="Urban short-term rentals invert the usual risk profile. The operating economics are better than a vacation market in almost every respect: higher occupancy, a flatter annual curve, and demand that comes from business, medical, event and family travel rather than leisure alone. The risk is entirely regulatory, and it is concentrated rather than gradual.",
        sections=[
            ("The permit is the asset", [
                "In a well-regulated city, the permit is worth more than the property's features. Nashville separates owner-occupied from non-owner-occupied permits and caps non-owner-occupied permits by zoning district. That constraint is not a burden on the investment, it is the entire investment thesis.",
                "In an unregulated market, a strong year invites new supply, new supply compresses rates, and the returns that attracted capital disappear within two seasons. A permit cap prevents exactly that dynamic. Operators holding a valid permit in a restricted district are protected from the competition that would otherwise arrive.",
                "Two of our clients bought into this thesis in Nashville. Mahmoud and, separately, Krystin and Michael each purchased four-bedroom properties targeting the group travel segment that permitted whole-house rentals serve.",
                ("ul", [
                    "Verify the permit exists and is currently valid for the specific parcel.",
                    "Verify whether it transfers to a new owner or must be re-applied for.",
                    "Verify the zoning district permits non-owner-occupied operation.",
                    "Check whether the city caps permits per block, per district, or by density ratio.",
                    "Read the condo or HOA declaration separately. A city permit does not override a private covenant.",
                ]),
            ]),
            ("Compression nights and why dynamic pricing matters more here", [
                "City revenue is driven disproportionately by compression nights, dates where a convention, a festival, a playoff game or a graduation pushes citywide demand past hotel capacity and rates run several times baseline.",
                "Nashville is a clear example. CMA Fest, the NFL and NHL seasons, Music City Center conventions and a continuous stream of Broadway weekends produce dozens of these nights a year. Capturing them requires pricing that is actually watching the event calendar, not a static weekend uplift.",
                "An operator who prices a city property on a flat weekday and weekend schedule will leave a large share of the year's profit on the table. This is the single largest performance gap between well-run and poorly-run urban listings, and it is bigger than the gap in vacation markets, where seasonality is more predictable.",
            ]),
            ("The long-term rental floor", [
                "Every urban short-term rental should be underwritten against what it is worth as a long-term rental if the permit regime tightens. That number is the floor, and the deal has to be acceptable at the floor, not only at the short-term projection.",
                "In Nashville the long-term rental market is strong enough that the floor is a real one. In some tourist-dependent cities it is not, and a property bought purely on short-term economics in a market with weak long-term rents is an unhedged regulatory bet.",
                "This discipline also protects against a subtler risk: a permit regime that stays intact but tightens operationally, adding occupancy caps, quiet hours, parking requirements or minimum stay floors that shrink the revenue without eliminating it.",
                ("warn", "Permit rules are political and can change in a single council session. A property that only works under the current ordinance is not a real estate investment, it is a policy bet with a mortgage attached."),
            ]),
            ("How urban operations differ", [
                "City guests turn over more frequently, expect faster response times, and are far more likely to raise complaints about noise, parking or neighbors. Cleaning and management systems adequate for a weekly beach turnover are not adequate for a market where a house turns three times in one week.",
                "Neighbor relations are an operating requirement rather than a courtesy. Most city short-term rental enforcement actions begin with a neighbor complaint. Noise monitoring devices, explicit quiet hours, clear parking instructions, and a local contact who answers the phone are what keep a permitted property out of the enforcement pipeline.",
                "Guest screening also matters more. The party-house problem is concentrated in urban markets, and a single incident can generate an enforcement action, an insurance claim and a permanent reputation problem with the neighborhood.",
                ("ul", [
                    "Noise monitoring in main living areas, disclosed in the listing.",
                    "Minimum stay floors on high-risk weekends.",
                    "Explicit parking assignments with photographs in the guest guide.",
                    "A local contact reachable within thirty minutes.",
                    "Clear, enforced occupancy limits written into the house rules.",
                ]),
            ]),
        ],
        faqs=[
            ("Why are permit-restricted cities good markets for STR investing?",
             "Because a permit cap limits new supply. In unregulated markets a strong year attracts competition that compresses rates within two seasons. A valid permit in a restricted district protects an operator from exactly that dynamic."),
            ("Do short-term rental permits transfer when a property sells?",
             "It depends entirely on the city. Some transfer with the property, some must be re-applied for by the new owner, and some are non-transferable by design. This has to be verified for the specific parcel before an offer, not assumed."),
            ("What is a long-term rental floor and why does it matter?",
             "It is what the property is worth as a conventional rental if the short-term permit regime tightens. Every urban STR should be acceptable at that floor, because permit rules are political and can change quickly."),
            ("What are compression nights?",
             "Dates when a convention, festival, playoff game or graduation pushes citywide demand past hotel capacity and nightly rates run several times baseline. City revenue depends disproportionately on capturing them, which requires pricing tied to the actual event calendar."),
        ],
        related=[
            '<a href="/markets/nashville/">Nashville market analysis</a>',
            '<a href="/markets/austin/">Austin market analysis</a>',
            '<a href="/regulations/">Short-term rental rules by state</a>',
            '<a href="/case-studies/mahmoud-nashville-tn-4br/">Case study: a 4BR Nashville permitted STR</a>',
            '<a href="/management/">Property management for short-term rentals</a>',
        ],
    ),
    dict(
        slug="ski",
        name="Ski STRs",
        eyebrow="Ski Properties",
        h1="Ski Short-Term Rentals: Lift Proximity, Two Seasons and Snow Risk",
        title="Ski Property STR Investing Guide (2026)",
        description="How ski STRs price on lift proximity, why a summer season decides whether the asset works, and how to underwrite a bad snow year before you buy.",
        blurb="Ski-in access, the summer season that carries the year, and underwriting a bad snow year.",
        lead="Ski properties have the highest peak nightly rates in short-term rental investing and the most concentrated risk. A great snow year and a poor one differ by more than any other weather variable in any other market, and the properties that survive a poor one are the ones with a real summer season.",
        sections=[
            ("Lift proximity is the pricing spine", [
                "Ski markets price on distance to the lift with a precision that no other property type matches. Ski-in ski-out commands an enormous premium. Walking distance to a base area is the next tier. Shuttle-accessible is a meaningful step down, and drive-and-park is a different asset entirely.",
                "The tiers are discontinuous rather than gradual. A property that is a four-minute walk to a lift and a property that is a twelve-minute walk are not 8% apart in rate, they are in different pricing brackets, because the guest is deciding whether they can carry skis and children to the lift without a vehicle.",
                "Verify the claim physically. Listings routinely describe shuttle-accessible properties as ski-in ski-out, and marketing distance is measured optimistically. Walk it, in winter conditions if possible.",
            ]),
            ("The summer season decides whether the asset works", [
                "A ski property that only earns in winter is carrying twelve months of mortgage, insurance and property tax on roughly sixteen weeks of revenue. That can work at the right basis, but it is fragile, and one bad snow year produces a genuinely painful set of statements.",
                "The mountain markets that hold up have a real second season. Park City has an established summer of hiking, biking, the Sundance ecosystem and festival traffic. Lake Tahoe has a full summer lake market that rivals its winter. Big Bear has summer lake and hiking demand from Los Angeles. The Poconos have summer lake demand plus autumn foliage.",
                "When we underwrite ski inventory, the summer number carries more weight than the winter number, because the winter number is what everyone already believes and the summer number is what decides whether a poor snow year is survivable.",
                ("table", ["Ski market", "Summer driver", "Season profile"], [
                    ["Park City, UT", "Hiking, biking, festivals", "Two strong seasons"],
                    ["Lake Tahoe, CA/NV", "Full summer lake market", "Two strong seasons"],
                    ["Big Bear, CA", "Lake and hiking, LA drive", "Two seasons, LA-fed"],
                    ["Poconos, PA", "Lake, foliage, NYC drive", "Close to year round"],
                ]),
            ]),
            ("Underwriting a bad snow year", [
                "Snow variability is the defining risk of the asset class and the one most commonly left out of the model. Build the projection with a poor winter, not an average one, and confirm the property still services its debt.",
                "Resorts with substantial snowmaking capacity and high base elevation are materially less exposed than low-elevation resorts dependent on natural snowfall. That difference belongs in the market selection, not just in the property selection.",
                ("ul", [
                    "Model a winter at roughly 70% of average revenue and confirm debt service still clears.",
                    "Favor resorts with heavy snowmaking coverage and high base elevation.",
                    "Weight the summer season heavily in the annual model.",
                    "Confirm insurance covers ice dam, freeze and burst pipe damage, which are the common winter claims.",
                    "Budget for snow removal, which is a real recurring line item, not an incidental.",
                ]),
                ("warn", "Freeze damage is the most expensive avoidable loss in ski markets. A property left unheated between bookings in a cold snap can produce a burst-pipe claim that costs more than a season of profit. Remote temperature monitoring is cheap insurance."),
            ]),
            ("What ski guests pay for", [
                ("ul", [
                    "<strong>Hot tub.</strong> As close to mandatory in ski markets as in the Smokies, and heavily filtered on.",
                    "<strong>Boot and gear storage with drying.</strong> A heated mudroom or boot dryer is mentioned constantly in reviews and costs very little.",
                    "<strong>Garage or covered parking.</strong> Genuinely valuable in snow country, and a differentiator in older base-area inventory.",
                    "<strong>Sleeping capacity above bedroom count.</strong> Ski trips are group trips splitting cost, so bunk rooms perform well.",
                    "<strong>Reliable heat and a fireplace.</strong> Both an amenity and a risk control.",
                ]),
                "Homeowner association rules deserve particular attention in ski markets, because much of the desirable base-area inventory is condominium or townhome product, and a substantial share of it prohibits short-term rentals outright or imposes minimum stays that break the economics. This is separate from any municipal rule and it is not always disclosed prominently.",
            ]),
        ],
        faqs=[
            ("How much does ski-in ski-out access affect rates?",
             "Substantially, and the tiers are discontinuous rather than gradual. Ski-in ski-out, walking distance to a base area, shuttle-accessible and drive-and-park sit in distinct pricing brackets, because the guest is deciding whether they can reach the lift without a vehicle."),
            ("Do ski properties need a summer season?",
             "In practice yes. A winter-only property carries twelve months of costs on about sixteen weeks of revenue, which is fragile in a poor snow year. Markets like Park City, Tahoe and Big Bear work because summer demand is real."),
            ("How should I underwrite snow risk?",
             "Model a winter at roughly 70% of average revenue and confirm the property still services its debt. Favor resorts with heavy snowmaking coverage and high base elevation, which are far less exposed to natural snowfall variability."),
            ("What is the most common expensive problem in ski markets?",
             "Freeze and burst pipe damage in properties left unheated between bookings. Remote temperature monitoring is inexpensive relative to a claim that can cost more than a season of profit."),
        ],
        related=[
            '<a href="/markets/park-city/">Park City market analysis</a>',
            '<a href="/markets/lake-tahoe/">Lake Tahoe market analysis</a>',
            '<a href="/markets/big-bear/">Big Bear market analysis</a>',
            '<a href="/property-types/mountain/">Mountain cabin short-term rentals</a>',
            '<a href="/revenue-projections/">Building a revenue projection you can trust</a>',
        ],
    ),
    dict(
        slug="desert",
        name="Desert STRs",
        eyebrow="Desert Properties",
        h1="Desert Short-Term Rentals: Pools, Inverted Seasons and Event Compression",
        title="Desert Short-Term Rental Investing Guide (2026)",
        description="Why desert STRs peak in winter, what a heated pool is actually worth in Scottsdale and Palm Springs, and how event weeks carry the annual number.",
        blurb="Winter peaks, mandatory pools, and event weeks that carry a quarter of the year.",
        lead="Desert markets run the calendar backwards. Scottsdale, Phoenix, Palm Springs and Joshua Tree earn their money between October and April and spend July and August nearly empty. Underwriting one on a conventional seasonal assumption produces a model that is wrong in both directions at once.",
        sections=[
            ("The inverted season", [
                "Peak demand in the Southwest runs roughly October through April. January through March is the strongest stretch, driven by snowbirds, spring training, golf and event traffic. June through August is the trough, when daytime temperatures make outdoor activity impractical and demand collapses.",
                "This inversion is an advantage for a portfolio. A desert property pairs naturally with a mountain or lake property, because the two peak at opposite ends of the year. A portfolio of two summer-peaking properties has one revenue season. A desert plus mountain pair has two.",
                "It also means the summer trough must be budgeted, not discovered. Some operators drop rates to near cost in July and August to cover carry rather than sitting empty. Others accept low occupancy and use the window for maintenance and refresh work. Either is defensible. Assuming summer revenue that will not arrive is not.",
            ]),
            ("A heated pool is not optional", [
                "In Scottsdale, Phoenix, Palm Springs and the surrounding markets, a private pool is close to mandatory above the entry tier. Properties without one compete on price against properties with one and lose.",
                "Heating specifically matters, and buyers routinely miss this. Desert winter days are warm and desert winter nights are cold. An unheated pool is unusable in January and February, which is exactly when demand peaks. A pool heater is the difference between an amenity that books the property and a decorative water feature.",
                ("ul", [
                    "<strong>Heated private pool.</strong> The single highest-return amenity in the market.",
                    "<strong>Shade structure and misters.</strong> Extends usable outdoor hours in shoulder months.",
                    "<strong>Outdoor living and fire feature.</strong> Desert evenings are the product; a fire pit gets used most of the year.",
                    "<strong>Genuinely capable air conditioning.</strong> An undersized system generates refunds in the shoulder season.",
                    "<strong>Golf proximity.</strong> In Scottsdale and Palm Springs this is a primary booking driver, not a nice-to-have.",
                ]),
            ]),
            ("Event compression carries the year", [
                "Desert markets have some of the most extreme event compression in the country. Scottsdale during the WM Phoenix Open and spring training, Palm Springs during Coachella and Stagecoach, and Joshua Tree during festival weekends produce nightly rates several times baseline.",
                "A handful of those weeks can represent a substantial share of annual profit. Capturing them requires pricing tied to the actual event calendar, minimum stay requirements set well in advance, and a booking window strategy that does not let a compression week fill at baseline rates six months out.",
                "The corresponding risk is over-reliance. A model that assumes premium event pricing every year is exposed if a festival moves, shrinks or is cancelled. Underwrite the base calendar so the property works without the compression, and treat event weeks as upside.",
                ("table", ["Market", "Peak drivers", "Trough"], [
                    ["Scottsdale, AZ", "Spring training, golf, WM Open", "July to August"],
                    ["Phoenix / Mesa, AZ", "Snowbirds, spring training", "July to August"],
                    ["Palm Springs, CA", "Coachella, Stagecoach, winter sun", "July to August"],
                    ["Joshua Tree, CA", "Festivals, park season, LA drive", "Deep summer"],
                    ["Sedona, AZ", "Spring and autumn hiking, red rock", "Milder trough"],
                ]),
            ]),
            ("Regulation and operating costs", [
                "Arizona state law substantially preempts municipal short-term rental bans, which has made Phoenix, Mesa, Scottsdale and Sedona unusually stable places to operate compared with California desert markets. Cities can impose licensing, noise and safety requirements but cannot prohibit outright.",
                "California is the opposite. Palm Springs operates a permit cap with a waiting list, and Joshua Tree and the surrounding San Bernardino County areas have tightened repeatedly. In California desert markets the permit position is the first thing to verify and the largest single risk to the investment.",
                "Operating costs skew differently here than in other markets. Pool service and heating are significant recurring lines. Summer cooling loads are heavy even at low occupancy, because a vacant house in Phoenix still has to be kept below the temperature at which furnishings and finishes degrade. Landscaping is cheap; water is not always.",
                ("warn", "In California desert markets, verify the permit and any cap or waiting list before writing an offer. A property that cannot obtain a permit is worth its long-term rental value, not its short-term rental proforma."),
            ]),
        ],
        faqs=[
            ("When is peak season in desert short-term rental markets?",
             "Roughly October through April, with January through March strongest, driven by snowbirds, golf, spring training and events. June through August is the trough, when heat suppresses demand almost entirely."),
            ("Does a desert short-term rental need a pool?",
             "Above the entry tier, effectively yes, and it needs to be heated. Desert winter nights are cold, so an unheated pool is unusable in January and February, which is exactly when demand peaks."),
            ("How much do events matter in desert markets?",
             "A great deal. Spring training and the WM Phoenix Open in Scottsdale, and Coachella and Stagecoach in Palm Springs, produce rates several times baseline. Underwrite the base calendar so the property works without them and treat event weeks as upside."),
            ("Is Arizona or California better for desert STR regulation?",
             "Arizona. State law substantially preempts municipal bans, so cities can license and regulate but not prohibit. California desert markets like Palm Springs run permit caps with waiting lists, which makes the permit position the largest single risk."),
        ],
        related=[
            '<a href="/markets/scottsdale/">Scottsdale market analysis</a>',
            '<a href="/markets/phoenix-mesa/">Phoenix and Mesa market analysis</a>',
            '<a href="/markets/joshua-tree/">Joshua Tree market analysis</a>',
            '<a href="/markets/sedona/">Sedona market analysis</a>',
            '<a href="/regulations/arizona/">Arizona short-term rental rules</a>',
        ],
    ),
]


def main():
    for t in TYPES:
        write(f"{P}{t['slug']}/", guide(
            slug=t["slug"], parent=P, parent_name="Property Types",
            title=t["title"], h1=t["h1"], eyebrow=t["eyebrow"],
            description=t["description"], lead=t["lead"],
            sections=t["sections"], faqs=t["faqs"], related=t["related"],
            section_name="Property Type Guides",
        ))

    write(P, hub(
        path=P,
        title="STR Property Types: Beach, Mountain, Lake, City, Ski, Desert (2026)",
        h1="Which property type actually fits what you are trying to do",
        eyebrow="Property Types",
        description="Six property type guides covering beach, mountain, lake, city, ski and desert short-term rentals: what drives revenue, what breaks, and what each one really costs to run.",
        sub="A beach house, a Smokies cabin and a permitted Nashville rental are three different businesses that happen to use the same booking platform. These guides cover what actually drives revenue in each, and what goes wrong.",
        cards=[(f"{P}{t['slug']}/", t["name"], t["blurb"]) for t in TYPES],
        sections=[
            ("How to choose between them", [
                "Most first-time buyers pick a property type emotionally, based on somewhere they like to visit. That is not automatically wrong, since you will care more about a property you understand, but it should not be the deciding factor. The deciding factors are season length, regulatory stability and how much operational attention the asset needs.",
                ("table", ["Type", "Season", "Regulatory risk", "Operating intensity"], [
                    ["Beach", "Long on the Gulf, shorter on the Atlantic", "Low to moderate", "High turnover, high wear"],
                    ["Mountain cabin", "Concentrated June to October plus holidays", "Generally low", "Moderate"],
                    ["Lake", "Short unless a second driver exists", "Low", "Moderate, seasonal"],
                    ["City", "Flat and year round", "High, permit dependent", "High, frequent turnover"],
                    ["Ski", "Winter plus whatever summer exists", "Moderate, HOA heavy", "High, weather exposed"],
                    ["Desert", "October to April, empty summer", "Low in AZ, high in CA", "Moderate, pool intensive"],
                ]),
                "A useful pairing rule for anyone planning more than one property: buy your second in a market whose peak season is opposite your first. A desert property plus a mountain cabin gives a portfolio two revenue seasons. Two summer-peaking properties give it one, twice.",
            ]),
        ],
        faqs=[
            ("Which short-term rental property type performs best?",
             "There is no single answer, because the types differ on season length, regulatory risk and operating intensity rather than on a simple return ranking. Gulf beach and Smokies mountain inventory are our most-transacted categories; permitted city rentals have the flattest annual curve; desert properties pair well with summer-peaking markets."),
            ("Should my second property be in the same market as my first?",
             "Generally no. Concentrating in one submarket means one regulatory change, one storm season or one supply glut affects the whole portfolio. Our clients who own multiple properties typically span markets with different seasons and different guest catchments."),
            ("Which property type is easiest to operate?",
             "Mountain cabins and lake houses, because stays are longer and turnover is less frequent than in city or beach markets. City rentals are the most operationally demanding, with the fastest turnover and the tightest guest response expectations."),
        ],
        related=[
            '<a href="/markets/">All market analyses</a>',
            '<a href="/case-studies/">Client case studies by market</a>',
            '<a href="/revenue-projections/">How to build a revenue projection</a>',
            '<a href="/regulations/">Short-term rental rules by state</a>',
        ],
        list_name="Short-Term Rental Property Type Guides",
    ))
    print(f"property types: {len(TYPES)} pages + hub")


if __name__ == "__main__":
    main()
