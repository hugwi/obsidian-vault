# Ethira Architecture Diagram

## 5-Layer Architecture

```mermaid
graph TD
    A["<b>Entry point</b><br/>Clear<br/>Action<br/>External API/WebSocket<br/>Entry point"]
    
    B["<b>Orchestration — Routing</b><br/>Request path, end to end<br/>Message composition<br/>AI coordination"]
    
    C1["<b>Text-Agent +<br/>LLM Agent</b>"]
    C2["<b>Specialized<br/>Processor Agent</b>"]
    C3["<b>Context<br/>Management</b>"]
    C4["<b>Tool/Action<br/>Execution</b>"]
    C5["<b>Chat State<br/>Machine</b>"]
    
    D1["<b>Business Logic<br/>Implementation</b>"]
    D2["<b>State<br/>Management</b>"]
    D3["<b>Tool Execution<br/>Framework</b>"]
    D4["<b>Document<br/>Extraction</b>"]
    
    E["<b>Infrastructure Layer</b><br/>LLM Integration | Workspace Data | External Systems<br/>Database | Queue | WebSocket"]
    
    A -->|"message"| B
    
    B -->|dispatch| C1
    B -->|dispatch| C2
    B -->|dispatch| C3
    B -->|dispatch| C4
    B -->|state| C5
    
    C1 -->|results| D1
    C2 -->|results| D2
    C3 -->|context| D3
    C4 -->|actions| D4
    C5 -->|updates| D1
    
    D1 --> E
    D2 --> E
    D3 --> E
    D4 --> E
    
    style A fill:#fff9e6,stroke:#cc9900,stroke-width:2px,color:#000
    style B fill:#ffe6e6,stroke:#cc6666,stroke-width:2px,color:#000
    style C1 fill:#e6f2ff,stroke:#6699cc,stroke-width:2px,color:#000
    style C2 fill:#e6f2ff,stroke:#6699cc,stroke-width:2px,color:#000
    style C3 fill:#e6f2ff,stroke:#6699cc,stroke-width:2px,color:#000
    style C4 fill:#e6f2ff,stroke:#6699cc,stroke-width:2px,color:#000
    style C5 fill:#e6f2ff,stroke:#6699cc,stroke-width:2px,color:#000
    style D1 fill:#e6ffe6,stroke:#66cc66,stroke-width:2px,color:#000
    style D2 fill:#e6ffe6,stroke:#66cc66,stroke-width:2px,color:#000
    style D3 fill:#e6ffe6,stroke:#66cc66,stroke-width:2px,color:#000
    style D4 fill:#e6ffe6,stroke:#66cc66,stroke-width:2px,color:#000
    style E fill:#f0e6ff,stroke:#9966cc,stroke-width:2px,color:#000
```

## Layer Description

| Layer | Components | Responsibility |
|-------|------------|-----------------|
| **Entry Point** (Yellow) | Clear, Action, External API/WebSocket | User interface entry & message reception |
| **Orchestration** (Pink) | Request routing, Message composition, AI coordination | Route messages to appropriate agents |
| **Agents** (Blue) | Text-Agent, LLM-Agent, Specialized Processor, Context Mgmt, Tool/Action Execution, Chat State Machine | Execute specialized logic & agent tasks |
| **Domain Logic** (Green) | Business Logic, State Management, Tool Execution Framework, Document Extraction | Apply business rules & process data |
| **Infrastructure** (Purple) | LLM Integration, Workspace Data, Database, Queue, WebSocket | Persistence & external system integration |
