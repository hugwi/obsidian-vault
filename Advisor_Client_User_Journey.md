---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---
# Advisor-Client User Journey: How Advisors Work with Clients and Customers

## Overview
This document outlines the complete journey of how advisors (Life & Pension, Private Banking, and P&C advisors) work with clients and customers in Max Wealth Management. The journey spans from prospecting and lead identification through client onboarding, advisory meetings, and ongoing relationship management.

---

## 1. PROSPECTING & LEAD IDENTIFICATION

### 1.1 Internal Cross-Sell Opportunities
**Actors:** Life & Pension (L&P) advisors, Private Banking advisors
**Goal:** Identify high-net-worth clients for private banking opportunities

**Process:**
- L&P advisor meets with a customer during fact-gathering sessions
- During meeting, advisor discusses free savings opportunities
- If customer has **>1 million SEK in free savings**, advisor identifies as potential private banking client
- L&P advisor creates lead record and initiates handshake with private banking team
- Lead information documented (name, personal number, email, estimated wealth)

**Data Points Gathered:**
- Current financial position
- Savings/investment capacity
- Financial goals and risk profile
- Existing products held

### 1.2 External Prospecting
**Actors:** Central private banking team, business development
**Goal:** Source and qualify external prospects

**Process:**
- Business development team identifies external prospect lists (e.g., small business owners from Retriever)
- Qualifying criteria: owner-led companies, estimated wealth levels
- Prospects targeted through:
  - Direct calls for meeting booking
  - Seminar invitations
  - One-on-one private meetings
- Lead captured in Excel pipeline (currently manual)

**Information Tracked:**
- Lead source (Retriever, purchased lists, events, etc.)
- Contact details
- Estimated wealth/potential
- Meeting scheduled date

### 1.3 Existing Customer Base Review
**Actors:** Private banking advisors, L&P advisors
**Goal:** Identify upsell and cross-sell opportunities within current portfolio

**Process:**
- Advisor reviews existing clients in system
- Checks for gaps in product offerings across business areas:
  - Private savings products not held
  - Insurance gaps
  - Pension products
- Uses 360-degree view to identify opportunities
- Prioritizes clients based on wealth level and growth potential

---

## 2. LEAD QUALIFICATION & PIPELINE MANAGEMENT

### 2.1 Pipeline Tracking
**Current State:** Manual Excel tracking
**Future State:** Salesforce CRM

**Pipeline Stages:**
1. **Lead** - Initial prospect identified
2. **Prospect** - Initial meeting scheduled
3. **Opportunity** - Meeting completed, proposal made
4. **In Progress** - Proposal submitted, awaiting response
5. **Won/Closed** - Account opened

**Information Captured:**
- Lead/Prospect name
- Contact details
- Lead source (L&P, external, P&C referral)
- Estimated wealth/capital
- Meeting date(s)
- Outcome of meetings
- Next steps/follow-up actions
- Pipeline owner (advisor name)
- Probability of close
- Expected commission/value

### 2.2 Lead Sources Classification
**Internal Cross-Sell:**
- L&P customer hand-off
- P&C opportunity identification
- Existing customer upsell

**External Prospecting:**
- Cold outreach (Retriever lists, purchased lists)
- Event attendees
- Referrals
- Other (TBD/fill in as needed)

---

## 3. PRE-MEETING PREPARATION

### 3.1 Customer Information Assembly
**Timeline:** Before advisor meeting
**Actors:** Advisor (primary), support staff (secondary)

**Required Information:**
- **Customer Profile:**
  - Name, contact details, personal/company number
  - Risk profile and financial situation
  - Existing relationship history

- **360-Degree View of Holdings:**
  - Private banking products held (currently in Privat Service, Max Fonder)
  - L&P products (pension, insurance - in existing systems)
  - P&C products and coverage
  - Free savings accounts and investments
  - Capital in Max Fonder (discretionary mandates, mutual funds, savings products)

- **Relationship Information:**
  - Previous meetings and outcomes
  - Key decision-makers and influencers
  - Communication preferences
  - Trust level indicators

### 3.2 System Access Requirements
**Actors:** Advisor
**Challenge:** Multiple systems requiring separate logins

**Current Systems & Access:**
- **ALVI:** Back-office platform for private banking (administration, contracts)
  - Viewing access for accounts
  - Cannot buy/sell directly (must use Max Fonder)
  - Onboarding new customers
  - Documentation

- **Max Fonder:** Trading and fund platform
  - Only place advisors can buy/sell
  - View holdings and portfolio composition
  - Requires separate login from ALVI

- **Max View:** Viewing platform
  - See if customer has Max Fonder account
  - View portfolio holdings and account structure
  - Limited visibility into investment details
  - Single sign-on available from ALVI

- **Private Services (Privat Tjänsten):** Customer-facing portal
  - See if customer has private banking account (ISK, capital insurance)
  - Cannot view account details or holdings (old API limitation)
  - Restricted data access

- **Salesforce (Future):** CRM system
  - Centralized customer view
  - Pipeline and opportunity tracking
  - 360-degree customer information
  - Integration with other business areas

### 3.3 Information Gaps Advisor Identifies
**Pain Point:** Advisors must manually piece together customer view from multiple systems

- Missing integration between Max Fonder and back-office system
- Poor API quality preventing real-time data updates
- Cannot see complete account status (e.g., new accounts with uninvested funds)
- Broker code inconsistencies causing data mismatches

---

## 4. ADVISOR-CUSTOMER MEETING

### 4.1 Meeting Types

#### Initial Meeting (New Prospect)
**Purpose:** Introduce services, understand needs, build relationship

**Typical Flow:**
1. Advisor uses pre-assembled customer information
2. Presents Max Wealth Management services
3. Conducts needs assessment interview
4. Gathers fact-finding information:
   - Financial situation
   - Income and assets
   - Investment experience
   - Financial goals (5-10 year horizon)
   - Risk tolerance
   - Life circumstances and plans

**Outcome Options:**
- Interest → Schedule follow-up meeting
- Investment proposal prepared
- Not interested → Close opportunity

#### Follow-up Meeting (Decision)
**Purpose:** Present investment proposal, answer questions, collect decision

**Meeting Content:**
- Review of fact-finding summary
- Investment recommendation aligned to goals/risk
- Proposal presentation
  - Suggested allocation across products
  - Expected returns and risk level
  - Fee structure and commission
  - Max Fonder fund selection (house view options)
- Q&A addressing concerns

**Outcome Options:**
- Accept proposal → Onboarding process
- Request modifications → Schedule next meeting
- Decline → Close opportunity

#### Ongoing Relationship Meetings (Existing Customers)
**Purpose:** Annual review, portfolio rebalancing, cross-sell opportunities

**Meeting Content:**
- Portfolio performance review
- Asset allocation assessment
- Life changes that might impact strategy
- Identify additional product opportunities
- Risk reassessment

### 4.2 Meeting Preparation Checklist

**What Advisor Needs to Know:**
- [ ] Complete financial picture (all holdings across business areas)
- [ ] Previous recommendations and outcomes
- [ ] Savings capacity and liquidity needs
- [ ] Tax situation and relevant structures (ISK, pension accounts, etc.)
- [ ] Family/business situation changes
- [ ] Risk tolerance profile
- [ ] Previous meetings with other advisors/teams

**Critical Success Factor:** Advisor must appear knowledgeable and prepared. Customers have high expectations that advisor has reviewed their situation in advance.

**Risk if Unprepared:**
- Advisor looks uninformed
- Customer loses confidence
- Sale lost to competitor
- Relationship damaged

---

## 5. CLIENT SEGMENTATION & ADVISOR ASSIGNMENT

### 5.1 Wealth-Based Segmentation

| Wealth Level | Primary Advisor | Advisory Model | Products Focus |
|---|---|---|---|
| <500K SEK | MSA Platform | Self-service / Automated | Free savings |
| 500K-1M SEK | L&P Advisors or CRT | Advisory with capacity constraints | Free savings, some pension |
| 1-3M SEK | L&P Advisors or Private Bankers | Full advisory | Holistic (pension + savings) |
| >3M SEK | Private Bankers | Dedicated advisory | Full wealth management |
| Established PB Customers | Private Bankers | Relationship-based | All products/services |

### 5.2 Advisor Types & Collaboration

**L&P Advisors (Life & Pension):**
- Primary advisors for pension and life insurance
- Identify and source private banking leads
- May handle free savings for customers <1M
- 6 integrated private bankers also handle their own private banking customers
- Other L&P advisors must coordinate with private banking team

**Private Banking Advisors:**
- Dedicated to high-net-worth clients (>1M typically)
- 6 integrated advisors (embedded in L&P teams)
- 11 standalone advisors (central team with open market prospecting)
- Build relationships for discretionary mandates and multiple asset classes

**Central Advisory Team (L&P):**
- Specialized team handling clients 500K-1M
- Funnel customers into private banking when wealth exceeds 1M
- More junior/cost-effective than private bankers
- High throughput model

**P&C Advisors:**
- Insurance and property coverage specialists
- Identify potential private banking prospects
- Source leads through company databases

### 5.3 Cross-Team Handoff Process

**Handoff Triggers:**
- Customer wealth exceeds segmentation threshold
- New product area identified as needed
- Existing customer requests more comprehensive service

**Handoff Process:**
1. Identifying advisor initiates "handshake" with receiving team
2. Formal agreement to transfer relationship/contact
3. Transfer customer record and account information
4. Receiving advisor takes ownership
5. Communication with customer about new advisor assignment

**Key Rules:**
- Private bankers cannot randomly contact L&P team's customers (trust/relationship risk)
- Must have formal handshake/approval before outreach
- Except: Private bankers can contact existing customers if criteria met (wealth >1M, no recent L&P contact)
- Commission share arrangements apply during handoff period

---

## 6. ONBOARDING NEW CLIENTS

### 6.1 KYC & Account Setup

**System:** Primarily in ALVI (back-office system)

**Steps:**
1. **Customer Verification (KYC):**
   - Collect identification
   - Verify beneficial ownership
   - Assess source of funds
   - Document compliance requirements

2. **Account Creation:**
   - Open primary account in ALVI
   - Link to Max Fonder systems
   - Set up access and permissions
   - Link to existing products (pension, insurance, etc.)

3. **Customer Portal Access:**
   - Private Services access for account viewing
   - Can integrate with other product areas
   - Single sign-on capability

### 6.2 Investment Proposal & Orders

**Process:**
1. Advisor prepares investment proposal in ALVI
2. Customer reviews proposal
3. Customer logs into same system to review details
4. Orders placed for:
   - Mutual fund purchases
   - Discretionary mandate setup
   - Transfer of existing investments
5. Execution and confirmation

**Challenge:** Customer must log in with Bank ID separately to finalize some transactions in Max Fonder

---

## 7. ONGOING RELATIONSHIP MANAGEMENT

### 7.1 Opportunity Tracking

**Types of Opportunities:**
- **Upsell:** Increase investment amount with existing advisor
- **Cross-Sell:** New product area (e.g., insurance to investment customer)
- **Product Upsell:** Additional products within same category (e.g., ISK to existing Max Fonder customer)

### 7.2 360-Degree View Usage

**For Existing Private Banking Customers:**
- Advisor sees all holdings: private banking, L&P products, P&C coverage
- Identifies gaps in product coverage
- Proposes holistic investment strategy
- Can warm-refer to specialist in other area (e.g., insurance advisor)

**Value to Advisor:**
- Better quality advice (complete financial picture)
- Efficiency (see opportunities immediately)
- Commission opportunities (multiple products)

**Value to Customer:**
- Holistic wealth management advice
- Coordinated financial strategy across products
- Better outcomes through comprehensive planning

### 7.3 Commission & Incentive Structure

**Commission Sources:**
- Performance-based on customer capital managed
- Amount varies by fund/product
- Tied to Max Fonder fund selection (commission on assets under management)
- Team-based commission pools

**Incentives for Leads:**
- L&P advisors receive KPI credit for leads shared to private banking
- Bonus pool structure encourages lead generation
- Leaderboards show meeting activity (competitive element)

**Potential Conflicts:**
- Advisors hesitant to share customers (protecting commission)
- Incentive structures being redesigned to encourage collaboration
- Commission still largely tied to individual/team revenue

---

## 8. PAIN POINTS & SYSTEM CHALLENGES

### 8.1 Data & System Integration Issues

**Fragmented Systems:**
- Customer information scattered across ALVI, Max Fonder, Private Services, Max View
- No single integrated view for advisor
- Multiple logins required for full picture
- APIs between systems are poor quality/incomplete

**Specific Gaps:**
- Cannot see uninvested cash in Max Fonder accounts (API limitation)
- Broker code inconsistencies (not auto-updated)
- Old API prevents real-time account status updates
- Incomplete MaxFonder holdings visibility from all advisor systems

**Impact:**
- Advisors unprepared for meetings despite best efforts
- Missed cross-sell opportunities
- Reduced advice quality
- Customer perception of disorganization

### 8.2 Process & Workflow Issues

**Missing Integration Points:**
- L&P advisory tool lacks Max Fonder integration
- Private banking has no formalized prospecting process
- Excel-based pipeline tracking is manual and error-prone
- No automated lead distribution from fact-gathering to private banking

**Prospecting Challenges:**
- Manual sourcing from external lists
- Unclear rules for advisor lead access
- No transparent process for prospect assignment
- Central mailbox leads not tracked consistently

**Communication & Trust Issues:**
- Team/advisor silos create trust concerns
- Customers surprised by contact from different advisor (lack of coordination)
- Commission-based incentives create reluctance to share customers
- Relationship continuity breaks during handoffs

### 8.3 Missing Functionality

- No unified CRM showing all advisor activity
- Cannot track first contact date vs. follow-up timing
- No visibility into which advisor owns prospect relationship
- No enforcement mechanism for engagement rules across business areas
- Limited automation of lead routing and assignment

---

## 9. FUTURE STATE VISION (Planned Improvements)

### 9.1 Salesforce CRM Integration

**Benefits:**
- Unified platform for all advisor activity
- 360-degree customer view in one system
- Visible pipeline and opportunity tracking
- Historical record of all touchpoints

**Capabilities:**
- Identify customers without specific products
- Automated lead routing based on criteria
- Track advisor engagement (who looked at customer, when)
- Enforce rules of engagement (logging contact attempts)
- Create accountability through transparent activity tracking

### 9.2 Data Architecture Improvements

**Master Data Management (MDM):**
- Single source of truth for customer records
- Clear ownership of each data element
- Reconciliation between systems
- Automated data updates via APIs

**API Enhancements:**
- Improved PartnerWeb API quality
- Real-time data flow from back-office to Salesforce
- Better integration with private services
- Complete Max Fonder holdings visibility

**Data Warehouse Integration:**
- Centralized reporting analytics
- Performance dashboards for teams and individuals
- Lead source and conversion tracking
- Commission and KPI calculations

### 9.3 Process Standardization

**Formalized Prospecting Process:**
- Clear definitions of prospect vs. customer vs. opportunity
- Standard prospecting pipeline for all business areas
- Defined rules of engagement
- Transparent lead ownership and assignment

**Enhanced Collaboration:**
- Defined handoff procedures between business areas
- Transparent access to customer information
- Activity tracking prevents duplicate contact
- Warm referrals between advisors

**Incentive Redesign:**
- Team-based KPIs and bonuses
- Lead-sharing incentives
- Collaboration metrics tracked
- Commission adjustments to encourage cross-sell

---

## 10. KEY METRICS & SUCCESS FACTORS

### 10.1 Advisor Productivity Metrics

- Number of meetings per week
- Pipeline value ($)
- Conversion rate (leads to customers)
- Average deal size
- Commission/revenue per advisor
- Cross-sell attachment rate

### 10.2 Customer Experience Metrics

- Customer satisfaction with advisor preparation
- Time to first meeting
- Customer retention rate
- Product adoption rate
- Net Promoter Score

### 10.3 Business Development Metrics

- Lead volume by source
- Time from lead to first meeting
- Handoff success rate (customer retention)
- Cross-product adoption rate
- Private banking customer growth

---

## 11. SUMMARY: TYPICAL ADVISOR JOURNEY

### New Private Banking Customer - Timeline

**Phase 1: Discovery (Weeks 1-2)**
- L&P advisor identifies customer with wealth >1M during fact-gathering
- Creates lead in system and initiates handshake
- Information shared with private banking team

**Phase 2: Preparation (Days before meeting)**
- Private banker assembles customer information from multiple systems
- Reviews existing holdings, wealth, risk profile
- Prepares presentation materials
- Researches Max Fonder fund recommendations

**Phase 3: Initial Meeting (Week 2-3)**
- Private banker meets with customer
- Reviews customer's financial situation
- Discusses goals and preferences
- Gathers additional fact-finding information
- Discusses proposed private banking relationship

**Phase 4: Proposal Development (Week 3-4)**
- Private banker prepares investment proposal
- Selects specific Max Fonder funds aligned to profile
- Calculates fees and expected outcomes
- Prepares documentation

**Phase 5: Decision Meeting (Week 4-5)**
- Present proposal to customer
- Answer questions and address concerns
- Collect customer decision

**Phase 6: Onboarding (Week 5-6)**
- Complete KYC in ALVI
- Set up accounts and access
- Execute orders
- Link to Private Services portal
- Customer begins managing portfolio

**Phase 7: Ongoing Management**
- Regular portfolio reviews
- Annual meetings with customer
- Identification of additional opportunities
- Cross-sell to other business areas
- Quarterly/annual performance reporting

---

## Appendix: System Glossary

| System | Purpose | User | Key Features |
|---|---|---|---|
| **ALVI** | Back-office administration | Private bankers, admin staff | Account setup, contracts, KYC, documentation |
| **Max Fonder** | Trading & fund platform | Advisors, customers | Buy/sell funds, discretionary mandates, manage portfolio |
| **Max View** | Viewing platform | Advisors | View customer accounts in Max Fonder (read-only) |
| **Private Services** | Customer portal | Customers, advisors (view) | See accounts, view portfolio, manage investments |
| **Salesforce (Future)** | CRM | All advisors | Customer records, pipeline, opportunities, activity tracking |
| **Data Warehouse (Future)** | Reporting & Analytics | Management, reporting | Performance metrics, dashboards, business intelligence |
| **Partner Web** | Data source | Admin, IT | API for customer and commission data |

---

*Document prepared based on meeting recordings and business process discussions from November-December 2024*
