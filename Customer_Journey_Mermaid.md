---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---
# Advisor-Customer Journey - Mermaid Diagrams

## 1. HIGH-LEVEL OVERVIEW - Complete Journey

```mermaid
graph TD
    Start([Customer/Prospect]) --> Discovery[Phase 1: Prospecting & Lead Identification]

    Discovery --> DiscoveryOptions{Lead Source}
    DiscoveryOptions -->|Internal Cross-Sell| LPAdvisor["L&P Advisor identifies<br/>customer with wealth >1M"]
    DiscoveryOptions -->|External Prospecting| ExtProspect["Business Dev sources<br/>external prospects"]
    DiscoveryOptions -->|Existing Customer| Review["Advisor reviews existing<br/>customer base"]

    LPAdvisor --> Qualify[Phase 2: Lead Qualification & Pipeline]
    ExtProspect --> Qualify
    Review --> Qualify

    Qualify --> QualifyProcess["Track in Excel/Salesforce<br/>Pipeline stages:<br/>Lead → Prospect → Opportunity<br/>→ In Progress → Won"]
    QualifyProcess --> Decision1{Qualified?}
    Decision1 -->|No| Reject["Close Opportunity<br/>Mark as Lost"]
    Decision1 -->|Yes| Prepare[Phase 3: Pre-Meeting Preparation]

    Prepare --> PrepareDetails["Assemble 360° view:<br/>- Customer profile<br/>- Holdings across systems<br/>- Relationship history<br/>- Risk profile"]
    PrepareDetails --> Meeting[Phase 4: Advisor-Customer Meeting]

    Meeting --> MeetingType{Meeting Type}
    MeetingType -->|Initial| Initial["Needs assessment<br/>Fact gathering<br/>Service introduction"]
    MeetingType -->|Follow-up| FollowUp["Present proposal<br/>Q&A and concerns<br/>Decision collection"]
    MeetingType -->|Annual Review| Review2["Portfolio review<br/>Identify opportunities<br/>Rebalancing"]

    Initial --> Decision2{Interest?}
    FollowUp --> Decision2
    Review2 --> Decision3{Action Needed?}

    Decision2 -->|Not Interested| Reject
    Decision2 -->|Yes| Segment[Phase 5: Segmentation &<br/>Advisor Assignment]
    Decision3 -->|New Product| Segment
    Decision3 -->|Increase Amount| Onboard[Phase 6: Onboarding/Setup]

    Segment --> SegmentTypes["Wealth Level:<br/><500K: MSA Platform<br/>500K-1M: L&P/CRT<br/>1-3M: L&P or PB<br/>3M+: Private Banker"]
    SegmentTypes --> Handoff{Advisor Change?}
    Handoff -->|Yes| Coordination["Formal handshake<br/>between teams"]
    Handoff -->|No| Onboard

    Coordination --> Onboard

    Onboard --> OnboardProcess["Phase 6: Onboarding<br/>- KYC verification in ALVI<br/>- Account setup<br/>- Investment proposal<br/>- Execute orders<br/>- Portal access setup"]
    OnboardProcess --> Confirm["Customer Onboarded<br/>Account Active"]

    Confirm --> Ongoing[Phase 7: Ongoing Relationship<br/>Management]

    Ongoing --> OngoingActivities["- Portfolio reviews<br/>- Annual meetings<br/>- 360° view monitoring<br/>- Cross-sell identification<br/>- Warm referrals"]
    OngoingActivities --> Growth["Customer Lifetime Value<br/>Growth & Retention"]

    Reject --> End1([Lost Lead])
    Growth --> End2([Active Customer])

    style Start fill:#e1f5ff
    style Discovery fill:#fff9c4
    style Qualify fill:#fff9c4
    style Prepare fill:#f3e5f5
    style Meeting fill:#f3e5f5
    style Segment fill:#e0f2f1
    style Onboard fill:#ffe0b2
    style Ongoing fill:#c8e6c9
    style End1 fill:#ffcdd2
    style End2 fill:#c8e6c9
```

---

## 2. DETAILED - PROSPECTING & LEAD IDENTIFICATION (Phase 1)

```mermaid
graph TD
    A["Phase 1: Prospecting & Lead Identification"] --> B{Lead Source}

    B -->|Internal: L&P Cross-Sell| C["L&P Advisor<br/>meets with customer"]
    B -->|Internal: Existing Customer| D["Advisor reviews<br/>existing customer base"]
    B -->|External| E["Business Development<br/>identifies prospects"]
    B -->|P&C Channel| F["P&C Advisor identifies<br/>potential PB opportunity"]

    C --> C1["During fact-gathering session,<br/>discuss free savings"]
    C1 --> C2{Wealth > 1M?}
    C2 -->|Yes| C3["✓ Potential PB Client<br/>Initiate handshake"]
    C2 -->|No| C4["Close conversation<br/>Not qualified"]

    D --> D1["Search for:<br/>- No PB products<br/>- Wealth >1M<br/>- Growth potential"]
    D1 --> D2["Identify gaps in<br/>product holdings"]
    D2 --> D3["✓ Opportunity Found<br/>Schedule contact"]

    E --> E1["Use Retriever or<br/>purchased prospect lists"]
    E1 --> E2["Filter by criteria:<br/>- Owner-led companies<br/>- Estimated wealth<br/>- Industry fit"]
    E2 --> E3["Contact methods:<br/>- Cold calls<br/>- Seminar invitations<br/>- Direct meetings"]
    E3 --> E4["✓ Meeting Scheduled<br/>Add to pipeline"]

    F --> F1["Insurance customer review<br/>identifies wealth indicators"]
    F1 --> F2["Warm handoff to<br/>Private Banking"]
    F2 --> F3["✓ Qualified Lead<br/>PB advisor follows up"]

    C3 --> G["Lead Details Captured:<br/>- Name & contact<br/>- Estimated wealth<br/>- Lead source<br/>- L&P advisor contact"]
    D3 --> G
    E4 --> G
    F3 --> G

    C4 --> H["Not Qualified<br/>Archive"]

    G --> I["MOVE TO PHASE 2<br/>Lead Qualification"]
    H --> END1([End])

    I --> END2([Continue Journey])

    style A fill:#fff9c4
    style C3 fill:#c8e6c9
    style D3 fill:#c8e6c9
    style E4 fill:#c8e6c9
    style F3 fill:#c8e6c9
    style END2 fill:#4caf50
```

---

## 3. DETAILED - LEAD QUALIFICATION & PIPELINE (Phase 2)

```mermaid
graph TD
    A["Phase 2: Lead Qualification<br/>& Pipeline Management"] --> B["Lead Status: NEW"]

    B --> C["Enter in Pipeline System<br/>(Currently: Excel → Future: Salesforce)"]

    C --> D["Pipeline Stage 1: LEAD"]
    D --> D1["Track information:<br/>- Lead source<br/>- Contact details<br/>- Estimated wealth<br/>- Initial notes"]
    D1 --> E["Pipeline Stage 2: PROSPECT"]

    E --> E1["Initial Contact Attempt:<br/>- Phone call<br/>- Email<br/>- Meeting invitation"]
    E1 --> E2{Contact Successful?}
    E2 -->|No| E3["Follow up in 1 week<br/>Max 3 attempts"]
    E3 --> E4{Success?}
    E4 -->|No| LOST1["Archive Lead<br/>Mark as Lost"]
    E4 -->|Yes| E5["Schedule Meeting"]
    E2 -->|Yes| E5

    E5 --> F["Pipeline Stage 3: OPPORTUNITY"]
    F --> F1["Meeting Scheduled<br/>- Date confirmed<br/>- Time & location<br/>- Attendees noted"]
    F1 --> G["Pre-Meeting Phase<br/>(See Phase 3)"]

    G --> H["MEETING CONDUCTED"]

    H --> I{"Meeting<br/>Outcome"}
    I -->|Not Interested| LOST2["Stage: LOST<br/>Close Opportunity<br/>Document reason"]
    I -->|Interested| J["Stage: IN PROGRESS"]

    J --> J1["Action Items:<br/>- Proposal being prepared<br/>- Follow-up meeting scheduled<br/>- Customer questionnaire sent"]
    J1 --> K["2nd Meeting: Proposal"]

    K --> L{"Customer<br/>Decision"}
    L -->|Decline| LOST3["Stage: LOST<br/>Closed Opportunity"]
    L -->|Modify Terms| J
    L -->|Accept| M["Stage: WON"]

    M --> M1["Stage: WON<br/>✓ Close Opportunity<br/>Create Account Record<br/>Move to Phase 6: Onboarding"]

    LOST1 --> END1([End - Not Qualified])
    LOST2 --> END2([End - Declined])
    LOST3 --> END3([End - Declined])
    M1 --> END4([Continue to Onboarding])

    D1 --> TRACK["📊 Tracked Metrics:<br/>- Lead source<br/>- Meeting dates<br/>- Outcome<br/>- Days in pipeline<br/>- Conversion rate"]

    style A fill:#fff9c4
    style M1 fill:#c8e6c9
    style TRACK fill:#e3f2fd
```

---

## 4. DETAILED - PRE-MEETING PREPARATION (Phase 3)

```mermaid
graph TD
    A["Phase 3: Pre-Meeting Preparation<br/>Timeline: 2-3 days before meeting"] --> B["Advisor Login to Systems"]

    B --> C["System 1: Max View"]
    C --> C1["Check if customer has<br/>Max Fonder account"]
    C1 --> C2["View portfolio holdings<br/>(read-only)"]

    B --> D["System 2: Private Services"]
    D --> D1["Check ISK &<br/>Capital Insurance accounts"]
    D1 --> D2["Limited visibility:<br/>Cannot see uninvested cash<br/>API limitation"]

    B --> E["System 3: L&P Systems"]
    E --> E1["View pension products"]
    E1 --> E2["View insurance coverage"]

    B --> F["System 4: ALVI"]
    F --> F1["View existing<br/>private banking accounts"]
    F1 --> F2["Review contract history"]

    B --> G["System 5: Manual/Notes"]
    G --> G1["Search CRM for<br/>previous meeting notes"]
    G1 --> G2["Review relationship history<br/>with customer"]

    C2 --> H["360° Customer View<br/>Assembled"]
    D2 --> H
    E2 --> H
    F2 --> H
    G2 --> H

    H --> I["Information Collected:<br/>📋 Demographics<br/>- Name, contact details<br/>- Personal/company number<br/>- Risk profile"]

    I --> J["💰 Financial Picture<br/>- Existing holdings in each system<br/>- Total estimated wealth<br/>- Free savings vs managed<br/>- Pension/insurance coverage"]

    J --> K["📈 Relationship Info<br/>- Previous advisor interactions<br/>- Key contact person<br/>- Communication preferences<br/>- Trust indicators"]

    K --> L["⚠️ Data Quality Issues"]

    L --> L1["Issue 1: Multiple logins<br/>required for complete view"]
    L1 --> L2["Issue 2: Cannot see uninvested<br/>cash in Max Fonder"]
    L2 --> L3["Issue 3: Broker code<br/>inconsistencies"]
    L3 --> L4["Issue 4: Fragmented data<br/>across 5+ systems"]

    L4 --> M["PREPARATION COMPLETE"]

    M --> N["✓ Advisor Ready for Meeting<br/>✓ Appears knowledgeable<br/>✓ Customer confidence high"]

    N --> O["→ Move to Phase 4<br/>Advisor-Customer Meeting"]

    style A fill:#f3e5f5
    style H fill:#c8e6c9
    style L fill:#ffcdd2
    style M fill:#c8e6c9
    style O fill:#81c784
```

---

## 5. DETAILED - ADVISOR-CUSTOMER MEETING (Phase 4)

```mermaid
graph TD
    A["Phase 4: Advisor-Customer Meeting"] --> B{Meeting Type}

    B -->|Initial Meeting| C["INITIAL MEETING<br/>New Prospect"]
    B -->|Follow-up Meeting| D["FOLLOW-UP MEETING<br/>Proposal & Decision"]
    B -->|Annual Review| E["ONGOING MEETING<br/>Annual Review & Opportunities"]

    C --> C1["Meeting Objectives:<br/>✓ Build relationship<br/>✓ Understand needs<br/>✓ Introduce services"]
    C1 --> C2["Meeting Flow:<br/>1. Opening & rapport<br/>2. Fact-finding interview<br/>3. Financial situation review<br/>4. Goals & risk profile<br/>5. Next steps discussion"]
    C2 --> C3["Information Gathered:<br/>📋 Income & assets<br/>📋 Investment experience<br/>📋 Financial goals (5-10yr)<br/>📋 Risk tolerance<br/>📋 Life circumstances"]
    C3 --> C4{Meeting Outcome}
    C4 -->|Not Interested| C5["Document Objections<br/>Archive Opportunity<br/>LOST"]
    C4 -->|Schedule 2nd Meeting| C6["Follow-up meeting<br/>scheduled for proposal"]

    D --> D1["Meeting Objectives:<br/>✓ Present proposal<br/>✓ Answer concerns<br/>✓ Collect decision"]
    D1 --> D2["Meeting Flow:<br/>1. Fact-finding review<br/>2. Recommendation<br/>3. Proposal presentation<br/>4. Fee & commission explanation<br/>5. Q&A & objection handling"]
    D2 --> D3["Proposal Includes:<br/>💼 Allocation strategy<br/>💼 Fund selection (Max Fonder)<br/>💼 Expected returns<br/>💼 Risk assessment<br/>💼 Fee structure"]
    D3 --> D4{Customer Decision}
    D4 -->|Decline| D5["Document reasons<br/>Close opportunity<br/>LOST"]
    D4 -->|Request Changes| D6["Schedule 3rd meeting<br/>Modify proposal<br/>Resubmit"]
    D4 -->|Accept| D7["✓ Proposal Accepted<br/>→ Move to Onboarding"]

    E --> E1["Meeting Objectives:<br/>✓ Portfolio review<br/>✓ Performance assessment<br/>✓ Identify opportunities"]
    E1 --> E2["Meeting Flow:<br/>1. Performance review<br/>2. Asset allocation check<br/>3. Life changes discussion<br/>4. Risk reassessment<br/>5. Opportunity discussion"]
    E2 --> E3["Key Focus:<br/>🎯 Use 360° view<br/>🎯 Check all business areas<br/>🎯 Identify gaps<br/>🎯 Cross-sell opportunities"]
    E3 --> E4{New Opportunities?}
    E4 -->|No| E5["Schedule next review<br/>Thank you meeting"]
    E4 -->|Yes| E6["Discuss new products<br/>Prepare new proposal"]

    C5 --> END1([Lost])
    C6 --> D
    D5 --> END2([Lost])
    D6 --> D
    D7 --> PHASE5["Phase 5:<br/>Segmentation"]
    E5 --> END3([Ongoing])
    E6 --> PHASE5

    style A fill:#f3e5f5
    style C1 fill:#e3f2fd
    style D1 fill:#e3f2fd
    style E1 fill:#e3f2fd
    style D7 fill:#c8e6c9
    style PHASE5 fill:#81c784
```

---

## 6. DETAILED - SEGMENTATION & ADVISOR ASSIGNMENT (Phase 5)

```mermaid
graph TD
    A["Phase 5: Segmentation &<br/>Advisor Assignment"] --> B["Customer Wealth Identified<br/>in Onboarding Process"]

    B --> C{Wealth Level}

    C -->|< 500K| D["Segment: SELF-SERVICE<br/>Platform: MSA"]
    D --> D1["Advisor: N/A (Automated)<br/>Model: Self-directed<br/>Products: Free savings only<br/>Commission: Volume-based"]

    C -->|500K - 1M| E["Segment: ADVISORY<br/>WITH CAPACITY"]
    E --> E1["Advisor: L&P Advisor or<br/>Central Advisory Team<br/>Model: Advisory<br/>Products: Free savings + Pension<br/>Commission: Per transaction"]

    C -->|1M - 3M| F["Segment: FULL ADVISORY<br/>Shared Model"]
    F --> F1["Advisor: L&P Advisors OR<br/>Private Bankers (both can serve)<br/>Model: Full wealth advisory<br/>Products: All (holistic)<br/>Commission: AUM-based"]

    C -->|> 3M| G["Segment: DEDICATED<br/>PRIVATE BANKING"]
    G --> G1["Advisor: Private Banker<br/>Model: Dedicated relationship<br/>Products: Full wealth management<br/>Commission: AUM + performance"]

    D1 --> H{Advisor<br/>Change?}
    E1 --> H
    F1 --> H
    G1 --> H

    H -->|NEW CUSTOMER| I["Direct assignment<br/>to identified segment"]
    I --> ONBOARD["Move to Phase 6<br/>Onboarding"]

    H -->|EXISTING CUSTOMER<br/>UPSELL| J["Stay with current advisor"]
    J --> ONBOARD

    H -->|WEALTH MIGRATION| K["Need Handoff<br/>Example: 500K→1M<br/>L&P needs to introduce PB"]
    K --> K1["HANDOFF PROCESS:<br/>1. Advisor recognizes wealth<br/>2. Initiates handshake<br/>3. Formal introduction<br/>4. Transfer documentation<br/>5. Receiving advisor takes lead"]
    K1 --> K2{"Team<br/>Rules"}
    K2 -->|Integrated PB| K3["PB embedded in L&P team<br/>✓ Can contact freely<br/>✓ Revenue shared"]
    K2 -->|Standalone PB| K4["PB in central team<br/>⚠️ Must have handshake first<br/>⚠️ Cannot cold contact<br/>⚠️ Commission negotiation"]

    K3 --> K5["Relationship transition<br/>Customer retains both advisors<br/>or PB takes lead"]
    K4 --> K5
    K5 --> ONBOARD

    style A fill:#e0f2f1
    style D fill:#fff9c4
    style E fill:#ffe0b2
    style F fill:#ffccbc
    style G fill:#ff7043
    style K fill:#ffcdd2
    style ONBOARD fill:#81c784
```

---

## 7. DETAILED - ONBOARDING (Phase 6)

```mermaid
graph TD
    A["Phase 6: Onboarding & Account Setup"] --> B["Proposal Accepted<br/>Customer Ready to Open Account"]

    B --> C["Step 1: KYC & Compliance<br/>Location: ALVI System"]
    C --> C1["Collect Documentation:<br/>📄 Government ID<br/>📄 Proof of address<br/>📄 Source of funds<br/>📄 Tax information"]
    C1 --> C2["Verification Process:<br/>✓ Identity verification<br/>✓ Beneficial ownership<br/>✓ PEP screening<br/>✓ Sanctions check"]
    C2 --> C3["✓ KYC APPROVED"]

    C3 --> D["Step 2: Account Creation<br/>Location: ALVI System"]
    D --> D1["Create Primary Account:<br/>- Account type selection<br/>- Currency preference<br/>- Discretionary mandate setup<br/>- Initial deposit info"]
    D1 --> D2["Link to Systems:<br/>- Connect to Max Fonder<br/>- Enable trading access<br/>- Set permissions"]
    D2 --> D3["✓ ACCOUNT CREATED"]

    D3 --> E["Step 3: Investment Setup<br/>Location: ALVI + Max Fonder"]
    E --> E1["Review Investment Proposal:<br/>🎯 Fund allocation %<br/>🎯 Max Fonder fund selection<br/>🎯 Risk level<br/>🎯 Expected returns<br/>🎯 Management fees"]
    E1 --> E2["Execute Orders:<br/>- Buy mutual funds<br/>- Set up discretionary mandate<br/>- Transfer existing investments<br/>- Configure auto-rebalancing"]
    E2 --> E3["✓ ORDERS EXECUTED"]

    E3 --> F["Step 4: Portal Access<br/>Location: Private Services"]
    F --> F1["Set Up Customer Portal:<br/>🔑 Bank ID login enabled<br/>🔑 Two-factor auth configured<br/>🔑 Account access granted"]
    F1 --> F2["Permissions:<br/>- View account holdings<br/>- See transaction history<br/>- View performance reports<br/>- Optional: auto-trading setup"]
    F2 --> F3["✓ PORTAL ACCESS ENABLED"]

    F3 --> G["Step 5: Documentation & Agreements"]
    G --> G1["Customer Review & Sign:<br/>📋 Account agreement<br/>📋 Fund prospectus<br/>📋 Risk disclosure<br/>📋 Fee agreement"]
    G1 --> G2["Advisor delivers:<br/>- Digital via Private Services<br/>- Paper copies<br/>- Signature collection"]
    G2 --> G3["✓ ALL AGREEMENTS SIGNED"]

    G3 --> H["Step 6: Account Activation"]
    H --> H1["Final Checks:<br/>✓ All documents complete<br/>✓ Funds received<br/>✓ Orders confirmed<br/>✓ Access verified"]
    H1 --> H2["Send Welcome Package:<br/>📧 Welcome email<br/>📧 Account summary<br/>📧 Access instructions<br/>📧 First report"]
    H2 --> H3["✓ ACCOUNT LIVE"]

    H3 --> I["✓✓✓ ONBOARDING COMPLETE ✓✓✓"]
    I --> J["Move to Phase 7<br/>Ongoing Relationship Management"]

    J --> END["🎉 Customer Active<br/>Ready for Portfolio Management"]

    style A fill:#ffe0b2
    style C3 fill:#c8e6c9
    style D3 fill:#c8e6c9
    style E3 fill:#c8e6c9
    style F3 fill:#c8e6c9
    style G3 fill:#c8e6c9
    style H3 fill:#c8e6c9
    style I fill:#4caf50
    style END fill:#81c784
```

---

## 8. DETAILED - ONGOING RELATIONSHIP MANAGEMENT (Phase 7)

```mermaid
graph TD
    A["Phase 7: Ongoing Relationship<br/>Management"] --> B["Customer Account Active<br/>Relationship Begins"]

    B --> C["Primary Focus: 360° View<br/>& Opportunity Management"]

    C --> D["Activity 1: Regular Contact"]
    D --> D1["Monthly/Quarterly:<br/>- Portfolio performance updates<br/>- Market commentary<br/>- Opportunity alerts<br/>- Product changes"]
    D1 --> D2["Channel:<br/>📧 Email updates<br/>📞 Phone check-ins<br/>📊 Portal notifications<br/>📋 Periodic reports"]

    C --> E["Activity 2: Portfolio Reviews"]
    E --> E1["Quarterly Reviews:<br/>- Asset allocation check<br/>- Rebalancing assessment<br/>- Performance vs. benchmark<br/>- Risk profile assessment"]
    E1 --> E2["Annual Deep Review:<br/>- Life changes discussion<br/>- Goal progress update<br/>- Tax planning review<br/>- Strategy adjustment"]

    C --> F["Activity 3: 360° View Monitoring"]
    F --> F1["Check Holdings Across<br/>All Business Areas:"]
    F1 --> F2["✓ Private Banking accounts<br/>✓ L&P pension products<br/>✓ Insurance coverage<br/>✓ Free savings in other systems<br/>✓ External investments"]
    F2 --> F3["Identify Gaps:<br/>⚠️ Missing product areas<br/>⚠️ Underutilized funds<br/>⚠️ Coverage gaps<br/>⚠️ Tax inefficiencies"]

    F3 --> G["Activity 4: Cross-Sell<br/>Opportunities"]
    G --> G1["Identify Opportunities:<br/>💼 New private banking products<br/>💼 Insurance products (via P&C)<br/>💼 Pension optimization<br/>💼 Tax strategies"]
    G1 --> G2["Approach Options:<br/>Approach 1️⃣: Advisor advises directly<br/>Approach 2️⃣: Warm referral to specialist<br/>Approach 3️⃣: Colleague introduction<br/>Approach 4️⃣: No action (customer not interested)"]

    G2 --> G3["Track Outcomes:<br/>📊 Opportunities identified<br/>📊 Actions recommended<br/>📊 Customer acceptance rate<br/>📊 New products added"]

    G3 --> H["Activity 5: Commission &<br/>Performance Tracking"]
    H --> H1["Advisor Metrics:<br/>💰 AUM per customer<br/>💰 Commission earned<br/>💰 Cross-sell rate<br/>💰 Customer retention"]
    H1 --> H2["Team Metrics:<br/>📈 Portfolio growth<br/>📈 Lead generation<br/>📈 Conversion rates<br/>📈 Customer lifetime value"]

    H2 --> I["Activity 6: Relationship<br/>Quality Management"]
    I --> I1["Maintain Trust:<br/>✓ Regular communication<br/>✓ Transparent advice<br/>✓ Conflict avoidance<br/>✓ Reliability"]
    I1 --> I2["Build Loyalty:<br/>🤝 VIP treatment for large clients<br/>🤝 Event invitations<br/>🤝 Priority access<br/>🤝 Personalized service"]

    I2 --> J["Life Cycle Events"]

    J --> J1{Trigger Event}
    J1 -->|Customer Wealthy| J2["Upsell: More sophisticated<br/>products, dedicated service"]
    J1 -->|Life Change| J3["Reassess: Update goals,<br/>strategy, products"]
    J1 -->|Market Change| J4["Review: Risk profile,<br/>asset allocation, tax impact"]
    J1 -->|Time Elapsed| J5["Annual Review:<br/>Standard check-in cycle"]

    J2 --> K["Generate Action"]
    J3 --> K
    J4 --> K
    J5 --> K

    K --> L{Action<br/>Needed?}
    L -->|Portfolio Adjustment| M["Execute rebalancing<br/>Update allocation"]
    L -->|New Product| N["Proposal development<br/>New opportunity"]
    L -->|No Change| O["Continue monitoring<br/>Schedule next review"]

    M --> P["ONGOING CYCLE<br/>Continuous Management"]
    N --> P
    O --> P

    P --> Q["🔄 REPEAT:<br/>Regular contact,<br/>Portfolio monitoring,<br/>Opportunity identification,<br/>Commission growth"]

    Q --> R{Customer<br/>Outcome}
    R -->|Active| S["✓ Retained Customer<br/>Growing relationship"]
    R -->|Churned| T["✗ Lost Customer<br/>Investigate reason"]
    R -->|Migrated| U["↗️ Moved to higher segment<br/>More dedicated service"]

    S --> END1["📈 Long-term Value"]
    T --> END2["📉 Learning opportunity"]
    U --> END3["🚀 Growth opportunity"]

    style A fill:#c8e6c9
    style C fill:#81c784
    style D fill:#e3f2fd
    style E fill:#e3f2fd
    style F fill:#e3f2fd
    style G fill:#fff9c4
    style H fill:#ffe0b2
    style P fill:#c8e6c9
    style END1 fill:#4caf50
```

---

## 9. TIMELINE VISUALIZATION - Complete Customer Journey Duration

```mermaid
graph LR
    subgraph "Phase 1: Discovery (1-2 weeks)"
        A["Lead<br/>Identified"]
    end

    subgraph "Phase 2: Qualification (1-3 weeks)"
        B["Prospect<br/>Contact"]
        C["Meeting<br/>Scheduled"]
    end

    subgraph "Phase 3: Preparation (2-3 days before meeting)"
        D["360° View<br/>Assembled"]
    end

    subgraph "Phase 4: Meeting (1-2 weeks)"
        E["Initial<br/>Meeting"]
        F["Proposal<br/>Meeting"]
    end

    subgraph "Phase 5: Segmentation (1-2 days)"
        G["Advisor<br/>Assignment"]
    end

    subgraph "Phase 6: Onboarding (1-2 weeks)"
        H["KYC &<br/>Setup"]
        I["Account<br/>Live"]
    end

    subgraph "Phase 7: Ongoing (Annual)"
        J["Reviews &<br/>Monitoring"]
    end

    A --> B --> C --> D --> E --> F --> G --> H --> I --> J

    style A fill:#fff9c4
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#f3e5f5
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style G fill:#e0f2f1
    style H fill:#ffe0b2
    style I fill:#ffe0b2
    style J fill:#c8e6c9
```

---

## 10. SYSTEM INTERACTIONS DURING JOURNEY

```mermaid
graph TD
    Phase["Advisor-Customer Journey"]

    Phase -->|Phase 1-2: Prospecting| S1["Excel<br/>Pipeline"]
    Phase -->|Phase 3: Prep| S2["Max View"]
    Phase -->|Phase 3: Prep| S3["Private Services"]
    Phase -->|Phase 3: Prep| S4["L&P Systems"]
    Phase -->|Phase 3: Prep| S5["ALVI"]

    Phase -->|Phase 4: Meeting| S6["CRM/Notes"]

    Phase -->|Phase 5: Assignment| S7["Salesforce"]

    Phase -->|Phase 6: Onboarding| S8["ALVI<br/>KYC & Setup"]
    Phase -->|Phase 6: Onboarding| S9["Max Fonder<br/>Trading"]
    Phase -->|Phase 6: Onboarding| S10["Private Services<br/>Portal"]

    Phase -->|Phase 7: Ongoing| S11["Salesforce<br/>CRM"]
    Phase -->|Phase 7: Ongoing| S12["Data Warehouse<br/>Reporting"]
    Phase -->|Phase 7: Ongoing| S13["Max Fonder<br/>Portfolio"]

    S1 -->|Future| Future["Consolidated to<br/>Salesforce CRM"]
    S2 -->|Challenge| Challenge1["Multiple logins<br/>Fragmented data"]
    S3 -->|Challenge| Challenge1
    S4 -->|Challenge| Challenge1
    S5 -->|Challenge| Challenge1

    Future --> Vision["360° View<br/>in One System<br/>Better Integration<br/>API Improvements"]

    style Phase fill:#2196f3
    style S1 fill:#ffccbc
    style S2 fill:#ffccbc
    style S3 fill:#ffccbc
    style S4 fill:#ffccbc
    style S5 fill:#ffccbc
    style S8 fill:#ffe0b2
    style S9 fill:#ffe0b2
    style S10 fill:#ffe0b2
    style S11 fill:#c8e6c9
    style S12 fill:#c8e6c9
    style S13 fill:#c8e6c9
    style Challenge1 fill:#ffcdd2
    style Vision fill:#81c784
```

