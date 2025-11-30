---
name: real-estate-listing-analyzer
description: Analyzes property listings to extract key data, generate comparisons, identify insights, and create professional real estate documentation for agents and investors.
license: Apache-2.0
---

# Real Estate Property Listing Analyzer

A specialized skill for analyzing residential and commercial property listings, extracting structured data, generating comparative market analyses, and creating professional real estate documentation.

## Purpose

This skill helps real estate professionals, investors, and agents:
- Extract and structure data from property listings (text, PDFs, images)
- Generate comparative market analyses (CMAs)
- Identify key selling points and red flags
- Create professional property summaries and factsheets
- Analyze pricing relative to market conditions
- Generate investment analysis reports

## Capabilities

### 1. Property Data Extraction
Extract structured information from listings:
- **Basic Details**: Address, price, square footage, beds/baths, lot size, year built
- **Features**: Amenities, upgrades, condition, appliances, parking
- **Financial**: HOA fees, taxes, price per sqft, financing options
- **Location**: School district, neighborhood, nearby amenities
- **Images**: Count, quality assessment, virtual tour availability

### 2. Comparative Market Analysis (CMA)
Generate professional CMAs:
- Compare up to 10 properties simultaneously
- Identify pricing outliers and value opportunities
- Calculate price per square foot trends
- Analyze days on market patterns
- Generate visual comparison tables

### 3. Investment Analysis
Evaluate properties for investment potential:
- Calculate cap rates and ROI estimates
- Analyze rental income potential
- Identify value-add opportunities
- Flag potential issues (foundation, roof, systems)
- Compare against investment criteria

### 4. Professional Documentation
Create real estate documents:
- Property factsheets with key highlights
- Buyer presentation summaries
- Listing comparison matrices
- Market analysis reports
- Investment opportunity briefs

## Input Formats Accepted

- **Text**: Copy-pasted listing descriptions
- **URLs**: Zillow, Realtor.com, Redfin, MLS listings
- **PDFs**: Listing sheets, disclosure documents
- **Images**: Property photos with OCR for signage/flyers
- **Spreadsheets**: Multiple listings for batch analysis

## Usage Examples

### Example 1: Single Property Analysis
```
User: Analyze this listing: [paste listing text or URL]

Claude:
# Property Analysis: 123 Main Street

## Key Details
- Price: $450,000 | $225/sqft
- Beds/Baths: 3 bed, 2.5 bath
- Square Footage: 2,000 sqft
- Lot Size: 0.25 acres
- Year Built: 2005

## Highlights
✓ Recently renovated kitchen (2023)
✓ New HVAC system (2022)
✓ Walking distance to top-rated schools
✓ Low HOA ($50/month)

## Considerations
⚠ Roof is 18 years old (may need replacement soon)
⚠ No garage (carport only)
⚠ Busy street location

## Market Position
- Priced 3% below neighborhood average ($232/sqft)
- 47 days on market (neighborhood avg: 32 days)
- Price reduced once (-$10k on Day 30)

## Investment Potential
- Rental estimate: $2,400-$2,600/month
- Gross yield: ~6.4%
- Value-add: Garage addition could increase value $30-40k
```

### Example 2: Comparative Analysis
```
User: Compare these 5 properties for my client looking in the $400-500k range

Claude: [Creates detailed comparison table with:]
- Side-by-side specs
- Price per sqft analysis
- Location scoring
- Condition assessment
- Best value recommendation
- Pros/cons for each property
```

### Example 3: Market Trend Analysis
```
User: Analyze the 3-bedroom market in the Riverside neighborhood

Claude:
# Riverside 3-Bedroom Market Analysis

## Current Inventory
- Active listings: 12 properties
- Price range: $380k - $575k
- Avg price/sqft: $218
- Avg DOM: 38 days

## Pricing Trends
- Median price: $465k (down 2% from last quarter)
- Properties under $450k selling in 21 days avg
- Properties over $500k sitting 52 days avg

## Buyer Recommendations
- Sweet spot: $420-470k range
- High demand for move-in ready
- Updated kitchens command 8-12% premium
```

## Analysis Framework

When analyzing properties, follow this structured approach:

### Step 1: Data Extraction
Extract all available data points into structured format

### Step 2: Context Assessment
- Neighborhood characteristics
- School ratings
- Proximity to amenities
- Market conditions (buyer's/seller's market)

### Step 3: Value Analysis
- Compare price to neighborhood comps
- Calculate price per square foot
- Assess condition vs. price
- Identify undervalued or overpriced indicators

### Step 4: Risk Assessment
- Age of major systems (roof, HVAC, water heater)
- Deferred maintenance indicators
- Location concerns (busy roads, flood zones)
- HOA restrictions or financial health

### Step 5: Opportunity Identification
- Value-add potential (renovations, additions)
- Rental income potential
- Market appreciation trends
- Unique features or advantages

### Step 6: Documentation
Generate appropriate output format:
- Quick summary for busy agents
- Detailed analysis for serious buyers
- Investment report for investors
- Comparison matrix for multiple properties

## Output Formats

### Standard Property Summary
- Executive summary (2-3 sentences)
- Key metrics table
- Highlights (3-5 bullet points)
- Considerations (3-5 bullet points)
- Market position analysis
- Recommendation

### Comparison Matrix
- Table format with all properties
- Color-coded value indicators
- Ranking by criteria
- Best match recommendation

### Investment Analysis Report
- Financial projections
- ROI calculations
- Risk assessment
- Exit strategy options
- Action items

### Professional Factsheet
- One-page formatted document
- Property photos integration
- Key stats prominently displayed
- Agent contact information
- QR code for virtual tour

## Best Practices

1. **Always verify square footage** - Check if it includes garage, basement, or just living space
2. **Calculate price per sqft consistently** - Use same methodology across comparisons
3. **Consider location context** - $200/sqft in one neighborhood ≠ $200/sqft in another
4. **Flag missing information** - Note what data is unavailable
5. **Use relative comparisons** - "15% above neighborhood average" vs absolute numbers
6. **Highlight timeframes** - "Renovated in 2022" is more valuable than "recently renovated"
7. **Quantify when possible** - "$30k under market" vs "good deal"

## Data Sources & Integration

Works with data from:
- Zillow
- Realtor.com
- Redfin
- MLS listings
- Property disclosure documents
- Tax assessor records
- School rating websites
- Neighborhood statistics

## Limitations

- Market data accuracy depends on source currency
- Cannot access private MLS data without user providing it
- Rental estimates are based on comparable analysis, not guaranteed
- Investment calculations are projections, not guarantees
- Physical inspections cannot be replaced by document analysis

## Real Estate Compliance Note

This skill provides analytical tools for real estate professionals. All analysis should be:
- Verified with licensed appraisers for official valuations
- Reviewed for local market accuracy
- Used as decision support, not sole decision basis
- Compliant with fair housing regulations
- Accompanied by appropriate disclosures

## Integration with AgentLabs AI Toolkit

This skill is designed to complement the SnoopLabs AgentLabs AI Toolkit:
- Use with **Notes Generator** for property showing notes
- Feed into **Factsheet Generator** for listing sheets
- Support **Sales Offer Generator** with market data
- Enhance **Project Comparator** with property comparisons
- Provide data for **Presentation Builder** slides

## Advanced Features

### Batch Processing
Process multiple listings simultaneously:
- Upload CSV/Excel with listing URLs or data
- Generate comparison matrix
- Identify top 3-5 best matches based on criteria
- Create presentation-ready output

### Criteria-Based Filtering
Filter properties by:
- Price range
- Location radius
- Minimum beds/baths
- Square footage range
- Age of property
- Specific amenities
- Investment criteria (cap rate, cash flow)

### Market Insights
- Identify pricing trends
- Spot seasonal patterns
- Detect neighborhood appreciation
- Flag upcoming development impacts

## Technical Implementation Notes

When processing listings:
1. Prioritize extracting numerical data accurately
2. Maintain consistent units (sqft not sq ft, not square feet)
3. Handle missing data gracefully (note "Not disclosed")
4. Preserve source links for verification
5. Format currency consistently ($450,000 not $450K)
6. Use tables for multi-property comparisons
7. Include data source and extraction timestamp

## Updates & Version History

- v1.0 (2025-01) - Initial release
- Designed for SnoopLabs AgentLabs AI Toolkit integration
- Optimized for residential real estate (single-family, condos, townhomes)
- Commercial real estate support planned for future version
