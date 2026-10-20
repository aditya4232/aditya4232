<!-- Profile content refreshed from the October 2026 resume. -->
<p align="center">
  <img src="./assets/neural-core.svg" width="1200" alt="Aditya Shenvi — AI/ML and Cloud Engineer. Animated neural network; Junior AI Cloud Engineer, Hyderabad." />
</p>

<p align="center">
  <a href="https://linkedin.com/in/adityashenvi"><img src="https://img.shields.io/badge/LinkedIn-CONNECT-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="Connect on LinkedIn" /></a>
  <a href="https://adityacuz.dev"><img src="https://img.shields.io/badge/Portfolio-EXPLORE-0891B2?style=for-the-badge&amp;logo=googlechrome&amp;logoColor=white" alt="Explore my portfolio" /></a>
  <a href="mailto:adityashenvi2050@gmail.com"><img src="https://img.shields.io/badge/Email-SAY_HELLO-7C3AED?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" alt="Email Aditya" /></a>
</p>

<p align="center"><b>I build LLM applications that retrieve knowledge, use tools, and connect to real workflows.</b><br/>Python at the core. FastAPI at the boundary. AWS in the cloud.</p>

<p align="center"><a href="#01--profile">Profile</a> · <a href="#03--selected-engineering">Projects</a> · <a href="#04--engineering-toolkit">Stack</a> · <a href="#05--professional-experience">Experience</a></p>

## `01` / Profile

I'm **Aditya**, an **AI/ML & Cloud Engineer** based in **Hyderabad, India**, currently working as a **Junior AI Cloud Engineer**. I build AI-powered features, authenticated serverless APIs, and enterprise knowledge-source integrations. My earlier work includes document-grounded assistants and offline-capable operations dashboards.

My work spans the full path from **chunking and embeddings** to **agent orchestration**, **streaming APIs**, and **deployment troubleshooting**. I also build in the open: local agents, text-to-app experiments, and accessible model fine-tuning.

<table>
<tr>
<td width="33%" valign="top"><b>RETRIEVE</b><br/><br/>Document ingestion, semantic search, and answers grounded in source material.</td>
<td width="33%" valign="top"><b>ORCHESTRATE</b><br/><br/>Agent workflows, tool calling, structured outputs, and streaming responses.</td>
<td width="33%" valign="top"><b>SHIP</b><br/><br/>Serverless APIs, authenticated integrations, infrastructure as code, and runtime monitoring.</td>
</tr>
</table>

## `02` / Systems thinking

```mermaid
flowchart LR
    A[Documents & enterprise sources] --> B[Ingest & chunk]
    B --> C[Embeddings & retrieval]
    C --> D[LLM & agent orchestration]
    D --> E[Source-cited answers & tool actions]
    F[Authentication & access controls] -.-> A
    F -.-> D
    D -.-> G[Evaluation & observability]
    style A fill:#0d1526,stroke:#38bdf8,color:#e2e8f0
    style B fill:#0d1526,stroke:#38bdf8,color:#e2e8f0
    style C fill:#0d1526,stroke:#a78bfa,color:#e2e8f0
    style D fill:#17203b,stroke:#a78bfa,color:#e2e8f0
    style E fill:#0d2527,stroke:#34d399,color:#e2e8f0
    style F fill:#0d1526,stroke:#64748b,color:#cbd5e1
    style G fill:#0d1526,stroke:#64748b,color:#cbd5e1
```

*The systems I enjoy building: grounded retrieval, deliberate tool use, and observable cloud services.*

## `03` / Selected engineering

**Local-first agents → multi-agent generation → model customization**<br/>
Three complementary directions in my open-source work: running assistants locally, coordinating agents to build applications, and adapting small models on consumer hardware.


| Project | What I built | Engineering focus |
| :--- | :--- | :--- |
| **[ALD-01](https://github.com/aditya4232/ALD-01)** | Local AI agent system with **5 specialized agents**, **10+ LLM integrations**, provider failover, and a streaming dashboard. Published on npm and PyPI. | `Python` `FastAPI` `Ollama` `LangChain` |
| **[CodeGenesis](https://github.com/aditya4232/CodeGenesis)** | Multi-agent text-to-app platform that generates full-stack application code from natural-language prompts. | `LangChain` `LangGraph` `OpenRouter` `FastAPI` |
| **[FineTuneLite](https://github.com/aditya4232/FineTuneLite)** | Local fine-tuning studio for **small language models**, with CPU-based PEFT/LoRA training and chat. | `Python` `PEFT` `LoRA` `Transformers` |
| **[Intelligent Document System](https://github.com/aditya4232/Intelligent-document-system)** | Document Q&A for consulting and staffing workflows, with source citations and confidence scores. | `RAG` `Embeddings` `Document Q&A` |
| **[DYSC-Agent](https://github.com/aditya4232/DYSC-Agent)** | Security analysis CLI combining static analysis, AI-assisted fix suggestions, and an interactive tool-calling REPL. | `Node.js` `CLI` `Static analysis` |
| **[SafeBite](https://github.com/aditya4232/SafeBite-V1)** | Food-analysis platform with Gemini nutrition insights, OCR label scanning, Firebase authentication, and real-time sync. | `Flask` `Node.js` `MongoDB` `Firebase` |

<p align="right"><a href="https://github.com/aditya4232?tab=repositories">Explore all repositories →</a></p>

## `04` / Engineering toolkit

| Layer | Tools & concepts |
| :--- | :--- |
| **Intelligence** | LangChain · LangGraph · CrewAI · RAG · MCP · tool calling · structured outputs · RAG evaluation |
| **Models & data science** | PyTorch · scikit-learn · Hugging Face Transformers · SentenceTransformers · PEFT/LoRA · Ollama · Pandas · NumPy |
| **Services & data** | Python · FastAPI · Flask · Node.js · REST · WebSockets · PostgreSQL · MongoDB · SQL Server · FAISS · ChromaDB |
| **AWS** | Lambda · S3 · EC2 · Cognito · Amplify · SQS · CloudWatch · SAM · CloudFormation |
| **Delivery & security** | GitHub Actions · CI/CD · Docker · infrastructure as code · OAuth 2.0 · JWT · RBAC |
| **Languages & tooling** | Java · JavaScript · Git · Postman · npm · PyPI · GCP & Kubernetes fundamentals |

## `05` / Professional experience

**Junior AI Cloud Engineer**<br/>
`Sep 2026 → Present`

- Deploy AI-powered features on AWS and implement Cognito sessions, OAuth integrations, and authenticated serverless APIs.
- Implement Slack connection flows and support history ingestion with **Lambda, SQS, and S3**.
- Troubleshoot **SAM/CloudFormation** deployments, monitor runtime health in **CloudWatch**, and maintain release checks and technical documentation.

**AI Engineer Intern**<br/>
`Jan 2026 → Jun 2026`

- Built a RAG chatbot over **100+ enterprise documents** using LangChain, Ollama, FAISS/ChromaDB, and FastAPI, with source-cited answers.
- Developed document-processing workflows and **Talent Radar**, a candidate-matching dashboard.
- Integrated LLM providers with structured output parsing and streaming responses.

**Full Stack Developer Intern**<br/>
`Jul 2025 → Sep 2025`

- Built an operations dashboard with **Node.js and MongoDB**, supporting offline field workflows through Service Workers.
- Implemented multi-user authentication, **RBAC**, and real-time data synchronization.

<details>
<summary><b>Earlier experience</b></summary>

**Software Engineering Intern** · `Apr 2025 → Jun 2025`<br/>
Built enterprise HRMS APIs with VB.NET and SQL Server; worked on query optimization and bulk CSV/Excel processing.

</details>

<details>
<summary><b>Engineering priorities</b></summary>

- **Grounded answers:** preserve source context and make citations useful.
- **Explicit interfaces:** use structured outputs and clear tool contracts.
- **Secure integrations:** verify authentication and scope access to the workflow.
- **Operable services:** make failures visible through logs, monitoring, and release checks.

</details>

## `06` / Foundations & milestones

**B.Tech · Computer Science Engineering**<br/>
ICFAI Foundation for Higher Education, Hyderabad · **Jul 2022 – Sep 2026**

- **Google AI Essentials** · 2026
- **AWS Machine Learning Foundations** · 2025
- **AWS Cloud 101** · 2025
- **Introduction to Kubernetes (LFS158)** · Linux Foundation · 2025
- **Smart India Hackathon 2024** · National Certificate
- **ISRO Space Technology Training** · 2024

---

<p align="center"><img src="./assets/signal-line.svg" width="1200" alt="Animated cyan and violet signal line" /></p>

<p align="center"><b>Let's build useful AI, from retrieval to deployment.</b><br/><br/>
<a href="https://linkedin.com/in/adityashenvi">LinkedIn</a> · <a href="https://adityacuz.dev">Portfolio</a> · <a href="mailto:adityashenvi2050@gmail.com">Let's build something useful</a></p>
