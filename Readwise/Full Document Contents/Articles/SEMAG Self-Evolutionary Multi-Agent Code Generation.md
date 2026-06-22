# SEMAG: Self-Evolutionary Multi-Agent Code Generation

![rw-book-cover](https://static.arxiv.org/static/browse/0.3.4/images/icons/favicon.ico)

## Metadata
- Author: [[arxiv.org]]
- Full Title: SEMAG: Self-Evolutionary Multi-Agent Code Generation
- Category: #articles
- Summary: SEMAG is a new multi-agent system that improves code generation by using self-evolution and teamwork among agents. It achieves top accuracy on seven programming benchmarks, outperforming previous methods like GPT-4o. SEMAG also reduces computing costs while solving complex coding tasks effectively.
- URL: https://arxiv.org/html/2603.15707v1

## Full Document
### SEMAG: Self-Evolutionary Multi-Agent Code Generation

 Yulin Peng 1, Haowen Hou2, Xinxin Zhu 1, 2,   

Ying Tiffany He 1, F. Richard Yu 3   

1College of Computer Science and Software Engineering, Shenzhen University, China   

2Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), China   

3School of Information Technology, Carleton University, Canada

###### Abstract

Large Language Models (LLMs) have made significant progress in handling complex programming tasks. However, current methods rely on manual model selection and fixed workflows, which limit their ability to adapt to changing task complexities. To address this, we propose SEMAG, a Self-Evolutionary Multi-Agent code Generation framework that mimics human coding practices. It decomposes programming tasks into stages, including planning, coding, debugging, and discussion, while adapting workflows to task difficulty. Its self-evolutionary agents can access the latest models in real time and automatically upgrade the backbone model. SEMAG sets new state-of-the-art Pass@1 accuracy across benchmarks. Using identical backbone models, SEMAG outperforms prior methods by 3.3% on CodeContests. When augmented with self-evolutionary model selection that automatically identifies optimal backbones, SEMAG reaches 52.6%, showcasing both framework effectiveness and adaptability to evolving LLM capabilities.

SEMAG: Self-Evolutionary Multi-Agent Code Generation

 Yulin Peng 1, Haowen Hou2, Xinxin Zhu 1, 2, Ying Tiffany He 1, F. Richard Yu 3 1College of Computer Science and Software Engineering, Shenzhen University, China 2Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), China 3School of Information Technology, Carleton University, Canada 

####  1 Introduction

Large Language Models (LLMs) have demonstrated substantial progress in code generation and completion, driven by large-scale pretraining on diverse codebases. The GPT series Achiam et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib2)); Hurst et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib28)), CodeLLaMA-2 Roziere et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib3)), Qwen2.5-Coder Hui et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib46)), and DeepSeek-v3 Liu et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib45)) exhibit strong coding capabilities, unlocking new avenues for automated software development. In parallel, multi-agent frameworks and debugging-enhanced methodologies—such as planning-centric workflows Lei et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib36)), self-debugging paradigms Chen et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib52)), and collaborative agent systems Zhong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib35))—have shown promising performance on standard benchmarks. Nonetheless, real-world scenarios present open-ended tasks, constrained computational budgets, and evolving specifications, revealing critical limitations in current approaches.

First, frameworks such as Self-Debugging Chen et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib52)), LDB Zhong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib35)) typically adopt a fixed reasoning depth. On simple tasks, they introduce unnecessarily complex workflows, leading to redundant computation and excessive token usage, while on difficult tasks, the shallow reasoning depth results in poor success rates. Although hierarchical prompting has been shown to mitigate unnecessary reasoning Budagam et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib54)), these approaches still lack a principled mechanism to adapt reasoning depth dynamically to task complexity.

![Refer to caption](https://2603.15707v1/x1.png)Figure 2: Overview of SEMAG. (1) Self-Evolve: Agents dynamically select optimal backbone LLMs per task requirements. (2) Plan: Planning Agent creates solution plans validated by Plan Verifying Agent through I/O simulation. (3) Debug: Coding Agent generates code; upon failure, specialized agents (Embedding Trace, Code Explaining, Suggesting, Debugging) collaboratively refine using trace logs. (4) Debate: When debugging stalls, Debating Agents propose alternatives with Discriminating Agent selecting the optimal configuration.
![Refer to caption](https://2603.15707v1/x2.png)Figure 2: Overview of SEMAG. (1) Self-Evolve: Agents dynamically select optimal backbone LLMs per task requirements. (2) Plan: Planning Agent creates solution plans validated by Plan Verifying Agent through I/O simulation. (3) Debug: Coding Agent generates code; upon failure, specialized agents (Embedding Trace, Code Explaining, Suggesting, Debugging) collaboratively refine using trace logs. (4) Debate: When debugging stalls, Debating Agents propose alternatives with Discriminating Agent selecting the optimal configuration.
Second, current pipelines utilize a single debugging iteration. When initial outputs diverge significantly from the target, systems are prone to local minima. Though advanced reasoning paradigms such as Chain-of-Thought Wei et al. ([2022](https://arxiv.org/html/2603.15707v1/#bib.bib50)), Tree-of-Thoughts Yao et al. ([2023a](https://arxiv.org/html/2603.15707v1/#bib.bib51)), and parallel candidate exploration Li et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib55)) enhance complex reasoning, they lack explicit discussion–decision phases that aggregate diverse reasoning trajectories for improved synthesis.

Third, most systems are tightly coupled to a single backbone model. Frameworks built on GPT Achiam et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib2)); Hurst et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib28)), Gemini Team et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib30), [2024](https://arxiv.org/html/2603.15707v1/#bib.bib31)), or Claude Anthropic ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib13)) typically depend on a static model throughout execution. As task characteristics shift or new models emerge, backbone switching often requires manual intervention, limiting adaptability and scalability.

To address these challenges, we propose SEMAG, a Self-Evolutionary Multi-Agent code Generation framework. Our contributions are summarized as follows:

* • Adaptive hierarchical prompting: We propose a dynamic strategy that adjusts reasoning depth based on task complexity.
* • Collaborative self-evolution: We introduce discussion–decision module enabling escape from local optima and adaptive backbone switching.
* • Empirical gains: Achieves state-of-the-art performance on seven benchmarks. With controlled backbone comparison, SEMAG improves 3.3% over the previous best method on CodeContests; with self-evolutionary model selection, it further reaches 52.6%.

We evaluate SEMAG across seven text-to-code benchmarks, including four foundational datasets (HumanEval, MBPP, HumanEval-ET, MBPP-ET) and three competition-level benchmarks (APPS, LiveCode, CodeContests). Experimental results show that SEMAG achieves new state-of-the-art performance, including 98.8% Pass@1Chen et al. ([2021](https://arxiv.org/html/2603.15707v1/#bib.bib7)); Dong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib37)) on HumanEval, 87.6% on MBPP, and 65.0% on LiveCode. Most notably, on the most challenging dataset CodeContests, SEMAG achieves 38.0% Pass@1 accuracy with GPT-4o (3.3% improvement over LPW under the same backbone). When augmented with self-evolutionary model selection that automatically identifies the optimal backbone, SEMAG further reaches 52.6%. These results demonstrate that SEMAG achieves superior performance and resource efficiency, while offering strong adaptability to evolving programming tasks.

####  2 Related Work

#####  2.1 Traditional Approaches to Program Synthesis

Program synthesis has a long-standing research foundation in artificial intelligence Waldinger and Lee ([1969](https://arxiv.org/html/2603.15707v1/#bib.bib38)); Manna and Waldinger ([1971](https://arxiv.org/html/2603.15707v1/#bib.bib39)). Traditional methods leverage search strategies and data flow analysis McCarthy ([1978](https://arxiv.org/html/2603.15707v1/#bib.bib40)). Early efforts aimed to advance automatic programming and to identify viable approaches BALZER ([1985](https://arxiv.org/html/2603.15707v1/#bib.bib41)); Soloway ([1986](https://arxiv.org/html/2603.15707v1/#bib.bib42)) or explore large program spaces through domain-specific languages Mernik et al. ([2005](https://arxiv.org/html/2603.15707v1/#bib.bib43)); Gu et al. ([2021](https://arxiv.org/html/2603.15707v1/#bib.bib44)). These approaches struggle with generalization and scalability due to search space complexity.

#####  2.2 Large Language Models for Code Synthesis

Pretrained language models have enhanced code synthesis, with specialized models such as Qwen2.5-Coder Hui et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib46)), CodeLLaMA-2 Roziere et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib3)), Mistral Jiang et al. ([2024a](https://arxiv.org/html/2603.15707v1/#bib.bib47)), and DeepSeek-v3 Liu et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib45)) excelling in programming tasks. General-purpose models, including GPT Achiam et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib2)); Hurst et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib28)), Gemini Team et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib30), [2024](https://arxiv.org/html/2603.15707v1/#bib.bib31)), and Claude Anthropic ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib13)), also demonstrate robust code generation capabilities. However, these models still face challenges related to syntactic correctness, semantic alignment, generation robustness, and version conflicts. As a result, more refined control and evaluation mechanisms for code generation are necessary.

#####  2.3 Prompting and Debugging Techniques

Researchers have proposed various prompting and debugging techniques to improve code generation. Prompting strategies generally fall into three categories: retrieval-based Islam et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib21)), planning-based Yao et al. ([2023b](https://arxiv.org/html/2603.15707v1/#bib.bib15)), and debugging-based Chen et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib52)) approaches. These aim to guide LLMs in decomposing complex tasks into manageable parts through step-by-step reasoning. Techniques such as Chain-of-Thought Wei et al. ([2022](https://arxiv.org/html/2603.15707v1/#bib.bib50)), Tree-of-Thoughts Yao et al. ([2023a](https://arxiv.org/html/2603.15707v1/#bib.bib51)), and cumulative reasoning mimic human problem-solving paths, significantly enhancing model performance on complex tasks Zhou et al. ([2022](https://arxiv.org/html/2603.15707v1/#bib.bib49)); Zhang et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib53)). More advanced methods simulate the software development process by constructing multiple candidate programs and exploring the solution space in parallel Li et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib55)); Antoniades et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib56)).

Debugging systems such as Self-Debugging Chen et al. ([2023](https://arxiv.org/html/2603.15707v1/#bib.bib52)) and LDB Zhong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib35)) iteratively refine code using model explanations, execution, and human feedback. However, their effectiveness decreases when the initial code diverges from the intended function. To improve generation quality with limited supervision, some methods break down the coding task by incorporating visible test cases, step-by-step verification Hu et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib57)); Li and Yuan ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib58)); Mathews and Nagappan ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib59)), and natural language instructions to improve controllability and alignment.

Previous methods either fix reasoning depth—wasting compute on simple tasks and underperforming on hard ones—or rely on a single LLM, limiting recovery from failures. SEMAG tackles both with three mechanisms: a hierarchical controller that scales from one-shot to multi-step planning based on feedback; a discussion–decision phase where agents critique and merge solutions to avoid local optima; and an automatic model selector that switches to a more capable backbone, boosting Pass@1 accuracy as difficulty rises.

####  3 Method

We present a hierarchical multi-agent framework for code synthesis that adapts to task complexity through progressive refinement levels, coupled with a self-evolution mechanism for dynamic model selection. The overview of SEMAG is shown in Figure [2](https://arxiv.org/html/2603.15707v1/#S1.F2).

#####  3.1 Problem Formulation

We define a code generation task as 𝒯=(P,S,𝒞)\mathcal{T}=(P,S,\mathcal{C}) where P∈𝒫P\in\mathcal{P} is problem description, S={(xi,yi)}i=1nS=\{(x\_{i},y\_{i})\}\_{i=1}^{n} are input-output examples, and 𝒞\mathcal{C} is the program space. The core agent operations are:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CODER:𝒫×𝒮×Π×Θ→𝒞,PLANNER:𝒫×𝒮→Π,VERIFIER:Π×𝒫×𝒮→0,1×Π×ℒ,DEBUGGER:𝒞×Σ→𝒞\begin{split}\text{CODER}&:\mathcal{P}\times\mathcal{S}\times\Pi\times\Theta\rightarrow\mathcal{C},\\ \text{PLANNER}&:\mathcal{P}\times\mathcal{S}\rightarrow\Pi,\\ \text{VERIFIER}&:\Pi\times\mathcal{P}\times\mathcal{S}\rightarrow{0,1}\times\Pi\times\mathcal{L},\\ \text{DEBUGGER}&:\mathcal{C}\times\Sigma\rightarrow\mathcal{C}\end{split} |  | (1) |

where Π\Pi is the plan space, Θ\Theta parameters, ℒ\mathcal{L} logs, and Σ\Sigma suggestions. Additional agents include EMBEDTRACE (𝒞→𝒯\mathcal{C}\rightarrow\mathcal{T}), EXPLAINER (𝒞×𝒫→ℰ\mathcal{C}\times\mathcal{P}\rightarrow\mathcal{E}), and SUGGESTOR (𝒯×ℒ×ℰ→Σ\mathcal{T}\times\mathcal{L}\times\mathcal{E}\rightarrow\Sigma).

#####  3.2 Hierarchical Code Synthesis Framework

Our framework employs a four-level hierarchical architecture that progressively increases computational effort based on task complexity.

Level 1 (Direct Generation): The system initially attempts direct code synthesis using minimal prompting:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=CODER​(P,S,∅,∅),Y=\text{CODER}(P,S,\varnothing,\varnothing), |  | (2) |

where ∅\varnothing indicates no plan or parameters.

Level 2 (Planning and Verification): Upon Level 1 failure, the system generates and iteratively refines a structured solution plan. The planning process operates as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π0=PLANNER​(P,S),\pi\_{0}=\text{PLANNER}(P,S), |  | (3) |

followed by iterative verification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (νi,πi,ℓi)=VERIFIER​(πi−1,P,S),i∈[1,Mplan].\begin{split}(\nu\_{i},\pi\_{i},\ell\_{i})=\text{VERIFIER}(\pi\_{i-1},P,S),\\ &i\in[1,M\_{\text{plan}}].\end{split} |  | (4) |

where νi∈{0,1}\nu\_{i}\in\{0,1\} indicates verification status, πi\pi\_{i} is the refined plan, and ℓi\ell\_{i} contains verification logs. The process terminates when νi=1\nu\_{i}=1 or i=Mplani=M\_{\text{plan}}, with the final plan π∗\pi^{\*} guiding code generation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y=CODER​(P,S,π∗,∅).Y=\text{CODER}(P,S,\pi^{\*},\varnothing). |  | (5) |

Algorithm 1 Hierarchical workflow of SEMAGInput: Problem PP, examples SS   
Output: Program YY

1:⊳\triangleright Level 1 2:ifthenreturn3:endif4:⊳\triangleright Level 2 5:fordo6:7:ifthenbreak8:endif9:endfor10:11:ifthenreturn12:endif13:fordo⊳\triangleright Level 3 14:15:fordo16:17:18:19:ifthenreturn20:endif21:ifthenbreak22:endif23:24:endfor25:⊳\triangleright Level 4 26:27:ifthenreturn28:endif29:endfor30:return
Level 3 (Trace-Guided Debugging): When Level 2 fails, the system enters an iterative debugging phase with KpassK\_{\text{pass}} passes and MtryM\_{\text{try}} attempts per pass. For each attempt, the debugging process consists of:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ=EMBEDTRACE​(Y),ϵ=EXPLAINER​(Y,P),σ=SUGGESTOR​(τ,ℓ∗,ϵ),Y′=DEBUGGER​(Y,σ).\begin{split}\tau=\text{EMBEDTRACE}(Y),\\ \qquad\epsilon=\text{EXPLAINER}(Y,P),\\ \sigma=\text{SUGGESTOR}(\tau,\ell^{\*},\epsilon),\\ \qquad Y^{\prime}=\text{DEBUGGER}(Y,\sigma).\end{split} |  | (6) |

This process repeats for MdebugM\_{\text{debug}} iterations, where τ\tau captures runtime variable states, ϵ\epsilon provides semantic analysis, and σ\sigma synthesizes targeted modifications.

Level 4 (Multi-Agent Collaborative Refinement): When iterative debugging stalls, the system employs collaborative multi-agent discussion. Each of NdebaterN\_{\text{debater}} agents generates proposals incorporating discussion history:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dj=DEBATERj​(P,τ,Y,Hj−1),j∈[1,Ndebater].\begin{split}d\_{j}=\text{DEBATER}\_{j}(P,\tau,Y,H\_{j-1}),\\ j&\in[1,N\_{\text{debater}}].\end{split} |  | (7) |

where Hj−1={d1,…,dj−1}H\_{j-1}=\{d\_{1},...,d\_{j-1}\} represents accumulated discussion history. The decision aggregation employs weighted consensus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (α∗,θ∗)=arg⁡max(α,θ)​∑j=1Ndebaterwj⋅ϕ​(dj,α,θ),wj=exp⁡(ηj/τw)∑kexp⁡(ηk/τw).\begin{split}(\alpha^{\*},\theta^{\*})=\arg\max\_{(\alpha,\theta)}\sum\_{j=1}^{N\_{\text{debater}}}w\_{j}\cdot\phi(d\_{j},\alpha,\theta),\\ w\_{j}=\frac{\exp(\eta\_{j}/\tau\_{w})}{\sum\_{k}\exp(\eta\_{k}/\tau\_{w})}.\end{split} |  | (8) |

where ηj\eta\_{j} represents historical performance and ϕ\phi evaluates proposal alignment.

| Model | Method | HumanEval | MBPP | HumanEval-ET | MBPP-ET |
| --- | --- | --- | --- | --- | --- |
| GPT-3.5 | Direct | 72.0% ±\pm 1.2% | 55.2% ±\pm 0.8% | 62.8% ±\pm 0.6% | 45.6% ±\pm 0.6% |
| Self-Planning | 77.4% ±\pm 1.8% | 69.2% ±\pm 0.4% | 69.5% ±\pm 0.6% | 52.4% ±\pm 1.0% |
| MapCoder | 77.4% ±\pm 0.6% | 72.0% ±\pm 0.6% | 66.5% ±\pm 1.2% | 56.6% ±\pm 0.8% |
| LDB | 81.1% ±\pm 0.6% | 72.4% ±\pm 0.2% | 72.6% ±\pm 1.8% | 55.6% ±\pm 0.4% |
| LPW | 89.0% ±\pm 0.8% | 76.0% ±\pm 0.2% | 77.4% ±\pm 0.8% | 57.6% ±\pm 0.2% |
| SEMAG (Ours) | 91.5% ±\pm 1.8% | 76.2% ±\pm 0.8% | 79.9% ±\pm 0.6% | 64.4% ±\pm 0.4% |
| (+27.1%) | (+38.0%) | (+27.2%) | (+41.2%) |

Table 1: Pass@1 accuracy comparison of different methods using GPT-3.5 on code generation benchmarks. The values enclosed in parentheses represent the improvement over the Direct Prompting approach. The standard deviation (±\pm) is calculated based on the results of three independent runs and applies to the data analysis of subsequent experiments.
#####  3.3 Adaptive Level Transition Mechanism

Rather than using fixed iteration thresholds, we employ an adaptive transition mechanism based on execution trace similarity. The transition decision is formulated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Transition​(t)={True,if ​ρ​(τt,τt−1)>δ​(t,𝒯)False,otherwise\text{Transition}(t)=\begin{cases}\text{True},\text{if }\rho(\tau\_{t},\tau\_{t-1})>\delta(t,\mathcal{T})\\ \text{False},\text{otherwise}\end{cases} |  | (9) |

where ρ\rho measures trace similarity using normalized edit distance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(τt,τt−1)=1−EditDist​(τt,τt−1)max⁡(|τt|,|τt−1|)\rho(\tau\_{t},\tau\_{t-1})=1-\frac{\text{EditDist}(\tau\_{t},\tau\_{t-1})}{\max(|\tau\_{t}|,|\tau\_{t-1}|)} |  | (10) |

The adaptive threshold δ​(t,𝒯)\delta(t,\mathcal{T}) adjusts based on task complexity and iteration count:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​(t,𝒯)=δ0⋅exp⁡(−λ⋅tTmax⋅complexity​(𝒯))\delta(t,\mathcal{T})=\delta\_{0}\cdot\exp\left(-\lambda\cdot\frac{t}{T\_{\max}}\cdot\text{complexity}(\mathcal{T})\right) |  | (11) |

where δ0=0.85\delta\_{0}=0.85 is the initial threshold, λ=0.5\lambda=0.5 is the decay rate, t∈[1,Tmax]t\in[1,T\_{\max}] is the current iteration count within the active level, and TmaxT\_{\max} represents the maximum iterations before mandatory level transition.

#####  3.4 Self-Evolution Mechanism

To enable dynamic adaptation to evolving LLMs, we propose an automated model selection framework employing NselectorsN\_{\text{selectors}} parallel agents. Each selector ii performs four operations: First, it generates task-specific keywords κi=KEYWORDGEN​(T,context)\kappa\_{i}=\text{KEYWORDGEN}(T,\text{context}) and retrieves recent information Li=SEARCH​(κi)L\_{i}=\text{SEARCH}(\kappa\_{i}) by searching tools. Then, relevant links are filtered and summarized:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Li′={l∈Li:relevance​(l,T)>θr},\quad L^{\prime}\_{i}=\{l\in L\_{i}:\text{relevance}(l,T)>\theta\_{r}\}, |  | (12) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci=⋃ℓ∈Li′SUMMARIZE​(ℓ).C\_{i}=\bigcup\_{\ell\in L^{\prime}\_{i}}\text{SUMMARIZE}(\ell). |  | (13) |

Third, each selector proposes models mim\_{i} with confidence score:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (mi,ri,si)=SELECTOR​(Ci,Perf​(mi,Tsample)),(m\_{i},r\_{i},s\_{i})=\text{SELECTOR}(C\_{i},\text{Perf}(m\_{i},T\_{\text{sample}})), |  | (14) |

where sis\_{i} reflects sampled performance on task subset TsampleT\_{\text{sample}}. Finally, consensus is achieved through weighted voting:

|  |  |  |  |
| --- | --- | --- | --- |
|  | m∗=arg⁡maxm∈M​∑i=1Nselectorssi⋅𝕀​[mi=m].m^{\*}=\arg\max\_{m\in M}\sum\_{i=1}^{N\_{\text{selectors}}}s\_{i}\cdot\mathbb{I}[m\_{i}=m]. |  | (15) |

This mechanism ensures optimal model selection without manual intervention while maintaining adaptability to emerging LLMs.

| Model | Method | HumanEval | MBPP | HumanEval-ET | MBPP-ET |
| --- | --- | --- | --- | --- | --- |
| GPT-4o | Direct | 91.5% ±\pm 1.8% | 62.8% ±\pm 0.4% | 79.3% ±\pm 1.2% | 51.0% ±\pm 0.2% |
| LDB | 92.1% ±\pm 1.2% | 82.4% ±\pm 0.8% | 81.7% ±\pm 1.8% | 65.4% ±\pm 1.0% |
| LPW | 98.2% ±\pm 0.6% | 84.8% ±\pm 0.6% | 84.8% ±\pm 1.2% | 65.8% ±\pm 0.8% |
| SEMAG (Ours) | 98.8% ±\pm 0.6% | 87.6% ±\pm 0.4% | 86.6% ±\pm 0.6% | 71.8% ±\pm 0.2% |
| (+8.0%) | (+38.9%) | (+9.2%) | (+40.8%) |

| Model | Method | APPS | LiveCode | CodeContests | Overall Avg. |
| --- | --- | --- | --- | --- | --- |
| GPT-4o | Direct | 47.5% ±\pm 0.3% | 46.4% ±\pm 0.8% | 24.6% ±\pm 1.3% | 57.6% |
| LDB | 53.2% ±\pm 0.7% | 54.3% ±\pm 0.7% | 29.3% ±\pm 0.7% | 65.5% |
| LPW | 62.6% ±\pm 0.3% | 59.3% ±\pm 1.4% | 34.7% ±\pm 0.7% | 70.0% |
| SEMAG (Ours) | 67.6% ±\pm 0.8% | 65.0% ±\pm 0.7% | 38.0% ±\pm 1.3% | 73.6% |
| (+42.3%) | (+40.1%) | (+54.5%) | (+27.7%) |

Table 2: Pass@1 accuracy comparison of different methods using GPT-4o (2024-05-13) across multiple benchmarks. The values enclosed in parentheses represent the improvement over the Direct Prompting approach.

| Level | Benchmark |
| --- | --- |
| HumanEval | MBPP | HumanEval-ET | MBPP-ET | APPS | LiveCode | CodeContests |
| Level 1 | 148 | 314 | 130 | 255 | 66 | 65 | 37 |
| Level 2 | 8 | 18 | 6 | 10 | 9 | 16 | 6 |
| Level 3 | 4 | 48 | 2 | 46 | 7 | 4 | 5 |
| Level 4 | 4 | 120 | 26 | 189 | 57 | 55 | 102 |

Table 3: Distribution of prompt difficulty levels across multiple benchmarks using GPT-4o (2024-05-13).
####  4 Experiments

#####  4.1 Experimental Setup

Evaluation Datasets. We evaluate SEMAG on seven text-to-code benchmarks across two categories. The foundational datasets include HumanEval Chen et al. ([2021](https://arxiv.org/html/2603.15707v1/#bib.bib7)) and HumanEval-ET (164 problems each), and MBPP Austin et al. ([2021](https://arxiv.org/html/2603.15707v1/#bib.bib23)) and MBPP-ET (500 problems each). The ET variants Dong et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib24)) extend their counterparts with additional edge test cases. For MBPP/MBPP-ET, which lack sample input-output pairs, we follow previous work Zhong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib35)); Lei et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib36)) by randomly selecting one test case from the hidden test set as a sample (excluded from evaluation). The competition-level datasets consist of APPS Hendrycks et al. ([2021](https://arxiv.org/html/2603.15707v1/#bib.bib33)) (139 problems), LiveCode Jain et al. ([2025](https://arxiv.org/html/2603.15707v1/#bib.bib32)) (140 problems), and CodeContests Li et al. ([2022](https://arxiv.org/html/2603.15707v1/#bib.bib34)) (150 problems). LiveCode, released after the LLM training cutoff, ensures uncontaminated evaluation.

Baseline Methods. We compare SEMAG against several baseline approaches: Direct inputs tasks directly into an LLM; Self-Planning Jiang et al. ([2024b](https://arxiv.org/html/2603.15707v1/#bib.bib61)) decomposes tasks into subgoals; MapCoder Islam et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib21)) employs four agents for retrieval, planning, execution, and debugging; LDB Zhong et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib35)) utilizes control flow diagrams for programme decomposition and error localization; and LPW Lei et al. ([2024](https://arxiv.org/html/2603.15707v1/#bib.bib36)), the state-of-the-art approach, verifies plans step-by-step and uses print statements for debugging.

#####  4.2 Main Results

Comparison with Baselines. Tables [1](https://arxiv.org/html/2603.15707v1/#S3.T1) and [2](https://arxiv.org/html/2603.15707v1/#S3.T2) present results using GPT-3.5 and GPT-4o as backbone models. With GPT-3.5, SEMAG achieves the highest Pass@1 accuracy across all benchmarks, outperforming the strongest baseline LPW by 2.5%, 0.2%, 2.5%, and 6.8% on HumanEval, MBPP, HumanEval-ET, and MBPP-ET respectively.

Using GPT-4o, SEMAG establishes new state-of-the-art results across all seven benchmarks, achieving 98.8% accuracy on HumanEval (solving 162/164 problems). Compared to LPW, SEMAG demonstrates consistent improvements of 1.8-6.0% on foundational benchmarks and 3.3-5.7% on competition-level benchmarks, with particularly significant gains of 40-54% over Direct prompting.

![Refer to caption](https://2603.15707v1/x3.png)Figure 3: Pass@1 accuracy on CodeContests using GPT-4o(2024-05-13), GPT-4.1(2025-04-14), DeepSeek-v3(2025-03-24) and Claude-3.7-Sonnet(2025-02-19). 
Self-Evolution Agents in Code Task. To evaluate self-evolution capability, we deploy agents on the CodeContests benchmark to select optimal LLMs autonomously. Agents analyze real-time information to identify three candidate models: Claude-3.7-Sonnet, GPT-4.1, and DeepSeek-v3. Figure [3](https://arxiv.org/html/2603.15707v1/#S4.F3) shows that Claude-3.7-Sonnet achieves 52.6% Pass@1 accuracy, establishing a new state-of-the-art and significantly outperforming GPT-4o’s 38.0%. GPT-4.1 and DeepSeek-v3 both achieve 48.7%, demonstrating that the self-evolution mechanism effectively identifies and evaluates task-optimized models for continuous improvement.

#####  4.3 Ablations Studies and Analyses

Token Efficiency Analysis. Table [3](https://arxiv.org/html/2603.15707v1/#S3.T3) presents the distribution of prompt difficulty levels (1–4, indicating increasing complexity) across benchmarks using GPT-4o. Simpler datasets (HumanEval, MBPP) predominantly use Level 1 prompts (90.2% and 62.8%, respectively), while complex datasets (APPS, CodeContests) require more Level 3–4 prompts (46.0% and 71.3%, respectively). Figure [4](https://arxiv.org/html/2603.15707v1/#S4.F4) compares token consumption between LPW and SEMAG. Our hierarchical prompt strategy reduces token usage while improving accuracy across all datasets. On simpler tasks (HumanEval, MBPP), SEMAG achieves 19.3% and 15.5% token reduction compared to LPW, respectively. For complex tasks (APPS, CodeContests), where Level 4 prompts dominate, token reduction is 9.3% and 5.1%, respectively, constrained by inherent task complexity. This demonstrates SEMAG’s hierarchical decomposition effectively optimizes both performance and efficiency.

![Refer to caption](https://2603.15707v1/x4.png)Figure 4: Comparison of Pass@1 accuracy and average token count per question for LPW and SEMAG across benchmarks, using GPT-4o as the LLM backbone. Here, K = 10 3 K=10^{3} . 
Impact of Different Agents. We conduct an ablation study on HumanEval using GPT-3.5 to evaluate each agent’s contribution. As shown in Table [4](https://arxiv.org/html/2603.15707v1/#S4.T4), excluding any component reduces Pass@1 accuracy. Individual agents achieve limited improvements: Plan Verification alone reaches 77.4% (+5.5% from baseline 71.9%), Refine Suggestion 80.5%, and Discussion and Decision 81.7%. Dual-agent configurations perform better (82.9%-83.5%) but remain 8.7%-9.4% below the full implementation. The complete SEMAG achieves 91.5% Pass@1, demonstrating the synergistic importance of all three components.

| Plan | Refine | Discussion and | Pass@1 |
| --- | --- | --- | --- |
| Verification | Suggestion | Decision | accuracy |
| ×\times | ×\times | ×\times | 71.9% (-21.4%) |
| ✓\checkmark | ×\times | ×\times | 77.4% (-15.4%) |
| ×\times | ✓\checkmark | ×\times | 80.5% (-12.0%) |
| ×\times | ×\times | ✓\checkmark | 81.7% (-10.7%) |
| ×\times | ✓\checkmark | ✓\checkmark | 83.5% (-8.7%) |
| ✓\checkmark | ×\times | ✓\checkmark | 83.5% (-8.7%) |
| ✓\checkmark | ✓\checkmark | ×\times | 82.9% (-9.4%) |
| ✓\checkmark | ✓\checkmark | ✓\checkmark | 91.5% |

Table 4: Pass@1 accuracy of different component combinations in SEMAG, showing relative decreases from the full implementation (91.5% baseline). Results obtained using GPT-3.5 on the HumanEval benchmark.
Impact of Tool Using. In the planning stage, the planning agent can choose to utilise external tools, such as search engines, to enhance decision-making. We conduct an experiment on the HumanEval benchmark with GPT-3.5. Table [5](https://arxiv.org/html/2603.15707v1/#S4.T5) shows that when the planning agent uses tools, SEMAG achieves a Pass@1 accuracy of 91.5%. Without tools, the accuracy decreases to 87.8%. This 3.7% decline emphasizes the importance of external tools in planning. The results demonstrate that these tools help the planning agent access more relevant information, improving the quality of plans and SEMAG’s overall performance.

|  |  |
| --- | --- |
| With Tool Using | Without Tool Using |
| 91.5% | 87.8% |

Table 5: Pass@1 accuracy of SEMAG with and without tool usage in the planning stage. Results are obtained using GPT-3.5 on the HumanEval benchmark.
Analysis of Self-Evolution Agents. To calibrate the crawler depth of self-evolution agents, we vary the number of returned pages, Nlinks∈{10,15,20,25,30}N\_{\text{links}}\in\{10,15,20,25,30\}, while fixing all other variables (five random seeds, identical search prompts, temperature =0.1=0.1). After summarizing the first NN URLs (published ≤30\leq 30 days ago), the agents ranked the evidence and proposed 3 candidate LLMs for the given code task. Table [6](https://arxiv.org/html/2603.15707v1/#S4.T6) reports (i) the probability that Claude-3.7-Sonnet appears in the Top-3 list, (ii) average token consumption during summarization & reasoning, and (iii) end-to-end selection latency, all averaged over the five seeds.

| NlinksN\_{\text{links}} |  Pr(%)\Pr(\%) ↑\uparrow  | Tokens (KK) ↓\downarrow  | Latency (min) ↓\downarrow  |
| --- | --- | --- | --- |
| 10 | 40.0 | 30.4 | 3.5 |
| 15 | 60.0 | 39.1 | 4.6 |
| 20 | 80.0 | 45.9 | 6.0 |
| 25 | 80.0 | 65.2 | 7.8 |
| 30 | 80.0 | 78.3 | 9.2 |

Table 6: Impact of crawl depth on the probability (%) of discovering Claude-3.7-Sonnet in Top-3 and associated resource costs (averaged over five runs, 30-day window).
The results show that shallower crawls with 10–15 pages often miss key benchmark posts, yielding a lower than 70% probability of identifying Claude-3.7-Sonnet and defaulting to weaker models, albeit at lower cost. Scaling to Nlinks=20N\_{\text{links}}=20 achieves perfect discovery (probability 80%) with modest overhead (45k tokens, 6 minutes). Further increases add little value but inflate costs by 30–55%.

This highlights uncertainties in search-dependent model selection: online information may be incomplete or biased due to search algorithms, recency effects, or uneven coverage. In our experiments, insufficient depth (Nlinks≤15N\_{\text{links}}\leq 15) omitted Claude-3.7-Sonnet in up to 60% of runs, risking suboptimal choices. Thus, Nlinks=20N\_{\text{links}}=20 balances reliability and efficiency, ensuring top performers are captured while minimizing resources.

Parameters Details. We experiment on how different temperatures of LLM influence the accuracy of SEMAG. Figure [5](https://arxiv.org/html/2603.15707v1/#S4.F5) shows the variation in Pass@1 accuracy on the HumanEval benchmark using GPT-3.5. The highest mean Pass@1 accuracy (91.1%) is achieved at T=0.1T=0.1 and T=0.8T=0.8, with T=0.1T=0.1 exhibiting the lowest variance. To improve the reproducibility and consistency of our experimental results, we maintain a constant temperature of T=0.1T=0.1 throughout all stages of SEMAG.

![Refer to caption](https://2603.15707v1/x5.png)Figure 5: Pass@1 accuracy (right y-axis) and its variance (left y-axis, scaled by × 10 − 4 \times 10^{-4} ) on the HumanEval benchmark using GPT-3.5 as the backbone, measured over three independent runs for each temperature setting (0.1 to 1.0). 
![Refer to caption](https://2603.15707v1/x6.png)Figure 6: Pass@1 accuracy on the HumanEval benchmark with GPT-3.5 as the backbone, evaluated under different combinations of M t ​ r ​ y M\_{try} and M d ​ e ​ b ​ u ​ g M\_{debug} values. Each cell represents the mean Pass@1 accuracy for a specific parameter pair. 
To further quantify the influence of the number of candidate generations (Mt​r​yM\_{try}) and debugging iterations (Md​e​b​u​gM\_{debug}), we conduct a grid search over (Mt​r​y,Md​e​b​u​g)∈{0,1,…,6}2(M\_{try},M\_{debug})\in\{0,1,\dots,6\}^{2}. Figure [6](https://arxiv.org/html/2603.15707v1/#S4.F6) shows the variation in Pass@1 accuracy on the HumanEval benchmark using GPT-3.5. Increasing either Mt​r​yM\_{try} or Md​e​b​u​gM\_{debug} consistently improves performance. Starting from (0,0)(0,0), where only 71.3% accuracy is achieved, the Pass@1 accuracy increases steadily with higher values of both parameters. The performance begins to plateau near (Mt​r​y=5,Md​e​b​u​g=4)(M\_{try}=5,M\_{debug}=4), where SEMAG reaches 91.5%, representing a near-optimal balance between solution diversity and iterative refinement. Although the highest accuracy observed (92.1%) occurs at (5,6)(5,6), the gain over (5,4)(5,4) is minimal and comes with increased inference costs. As a result, we set Mt​r​y=5M\_{try}=5 and Md​e​b​u​g=4M\_{debug}=4 for all subsequent experiments, as these values have been empirically shown to optimize SEMAG’s performance.

####  5 Conclusion

We introduce SEMAG, a Self-Evolutionary Multi-Agent framework designed for code generation. By employing a division of labour with hierarchical prompting mechanisms, the coding agents of SEMAG significantly enhance the performance of LLMs across diverse programming tasks. The self-evolutionary agents of SEMAG feature self-evolving capabilities, enabling them to access the latest models in real-time and automatically upgrade the backbone model. The coding agents of SEMAG achieve state-of-the-art Pass@1 accuracy across seven benchmarks, including 98.8% on HumanEval, 87.6% on MBPP, and 38.0% on CodeContests, while substantially reducing computational resource overhead and token consumption. With controlled backbone, SEMAG improves 3.3% over LPW on CodeContests. With self-evolutionary model selection, it further reaches 52.6%, demonstrating the benefit of adaptive backbone switching. Future work will explore finer-grained decomposition, cross-modal collaboration, and efficient model selection strategies.

####  6 Limitations

Among the limitations of our work, firstly, SEMAG involves inference-time hyperparameters (MtryM\_{\text{try}} and MdebugM\_{\text{debug}}) that affect the trade-off between accuracy and cost; however, our experiments in Section 4.3 identify a stable configuration that generalizes across benchmarks, and adaptive tuning strategies are left for future work. Secondly, the hierarchical multi-agent design invests more computation on challenging problems through iterative refinement, which may increase latency in time-sensitive scenarios; our adaptive level transition mechanism partially addresses this by reducing token consumption by 15–20% on simpler tasks compared to fixed-depth baselines. Thirdly, the self-evolutionary model selection component relies on real-time information retrieval to identify optimal backbones; we note that this module is optional—the core framework operates independently with any fixed model as shown in Table [1](https://arxiv.org/html/2603.15707v1/#S3.T1) and Table [2](https://arxiv.org/html/2603.15707v1/#S3.T2). Offline model recommendation could be explored in future work. Finally, as with any system executing machine-generated code, running outputs inside a sandbox environment is advisable to mitigate potential security risks.

#### References

* J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023) Gpt-4 technical report. External Links: 2303.08774 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§1](https://arxiv.org/html/2603.15707v1/#S1.p4.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* Anthropic (2024) Introducing the next generation of claude. Note: <https://www.anthropic.com/news/claude-3-family>Accessed: 2024-03-04 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p4.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* A. Antoniades, A. Örwall, K. Zhang, Y. Xie, A. Goyal, and W. Wang (2025) SWE-search: enhancing software agents with monte carlo tree search and iterative refinement. In International Conference on Representation Learning, Vol. 2025, pp. 64485–64515. External Links: [Link](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1e6783e4d739196cad3336f12d402bf-Paper-Conference.pdf) Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. (2021) Program synthesis with large language models. External Links: 2108.07732 Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* R. BALZER (1985) A 15 year perspective on automatic programming. IEEE transactions on software engineering 11 (11), pp. 1257–1268. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* D. Budagam, A. Kumar, M. Khoshnoodi, S. KJ, V. Jain, and A. Chadha (2025) Hierarchical prompting taxonomy: a universal evaluation framework for large language models aligned with human cognitive principles. In First International KDD Workshop on Prompt Optimization, 2025, External Links: [Link](https://openreview.net/forum?id=0myKAuHN3M) Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p2.1).
* M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. (2021) Evaluating large language models trained on code. External Links: 2107.03374 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p6.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* X. Chen, M. Lin, N. Schärli, and D. Zhou (2023) Teaching large language models to self-debug. External Links: 2304.05128 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§1](https://arxiv.org/html/2603.15707v1/#S1.p2.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p2.1).
* Y. Dong, J. Ding, X. Jiang, G. Li, Z. Li, and Z. Jin (2025) Codescore: evaluating code generation by learning code execution. ACM Transactions on Software Engineering and Methodology 34 (3), pp. 1–22. Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* Y. Dong, X. Jiang, Z. Jin, and G. Li (2024) Self-collaboration code generation via chatgpt. ACM Transactions on Software Engineering and Methodology 33 (7), pp. 1–38. Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p6.1).
* Y. Gu, R. Tinn, H. Cheng, M. Lucas, N. Usuyama, X. Liu, T. Naumann, J. Gao, and H. Poon (2021) Domain-specific language model pretraining for biomedical natural language processing. ACM Transactions on Computing for Healthcare (HEALTH) 3 (1), pp. 1–23. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* D. Hendrycks, S. Basart, S. Kadavath, M. Mazeika, A. Arora, E. Guo, C. Burns, S. Puranik, H. He, D. Song, and J. Steinhardt (2021) Measuring coding challenge competence with apps. In Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks, Vol. 1. Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* Y. Hu, Q. Zhou, Q. Chen, X. Li, L. Liu, D. Zhang, A. Kachroo, T. Oz, and O. Tripp (2025) QualityFlow: an agentic workflow for program synthesis controlled by llm quality checks. External Links: 2501.17167 Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p2.1).
* B. Hui, J. Yang, Z. Cui, J. Yang, D. Liu, L. Zhang, T. Liu, J. Zhang, B. Yu, K. Lu, et al. (2024) Qwen2. 5-coder technical report. External Links: 2409.12186 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024) Gpt-4o system card. External Links: 2410.21276 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§1](https://arxiv.org/html/2603.15707v1/#S1.p4.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* M. A. Islam, M. E. Ali, and M. R. Parvez (2024) Mapcoder: multi-agent code generation for competitive problem solving. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 4912–4944. External Links: [Link](https://aclanthology.org/2024.acl-long.269/), [Document](https://dx.doi.org/10.18653/v1/2024.acl-long.269) Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p2.1).
* N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica (2025) Livecodebench: holistic and contamination free evaluation of large language models for code. In International Conference on Representation Learning, pp. 58791–58831. Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* A. Q. Jiang, A. Sablayrolles, A. Roux, A. Mensch, B. Savary, C. Bamford, D. S. Chaplot, D. d. l. Casas, E. B. Hanna, F. Bressand, et al. (2024a) Mixtral of experts. External Links: 2401.04088 Cited by: [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* X. Jiang, Y. Dong, L. Wang, Z. Fang, Q. Shang, G. Li, Z. Jin, and W. Jiao (2024b) Self-planning code generation with large language models. ACM Transactions on Software Engineering and Methodology 33 (7), pp. 1–30. Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p2.1).
* C. Lei, Y. Chang, N. Lipovetzky, and K. A. Ehinger (2024) Planning-driven programming: a large language model programming workflow. External Links: 2411.14503 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p2.1).
* D. Li, S. Cao, C. Cao, X. Li, S. Tan, K. Keutzer, J. Xing, J. E. Gonzalez, and I. Stoica (2025) S\*: test time scaling for code generation. External Links: 2502.14382 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p3.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* K. Li and Y. Yuan (2024) Large language models as test case generators: performance evaluation and enhancement. External Links: 2404.13340 Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p2.1).
* Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al. (2022) Competition-level code generation with alphacode. Science 378 (6624), pp. 1092–1097. Cited by: [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1).
* A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, et al. (2024) Deepseek-v3 technical report. External Links: 2412.19437 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* Z. Manna and R. J. Waldinger (1971) Toward automatic program synthesis. Communications of the ACM 14 (3), pp. 151–165. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* N. S. Mathews and M. Nagappan (2024) Test-driven development for code generation. External Links: 2402.13521 Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p2.1).
* J. McCarthy (1978) History of lisp. SIGPLAN Not. 13 (8), pp. 217–223. External Links: ISSN 0362-1340 Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* M. Mernik, J. Heering, and A. M. Sloane (2005) When and how to develop domain-specific languages. ACM computing surveys (CSUR) 37 (4), pp. 316–344. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* B. Roziere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan, Y. Adi, J. Liu, R. Sauvestre, T. Remez, et al. (2023) Code llama: open foundation models for code. External Links: 2308.12950 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* E. Soloway (1986) Learning to program == learning to construct mechanisms and explanations. Communications of the ACM 29 (9), pp. 850–858. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* G. Team, R. Anil, S. Borgeaud, J. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican, et al. (2023) Gemini: a family of highly capable multimodal models. External Links: 2312.11805 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p4.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* G. Team, P. Georgiev, V. I. Lei, R. Burnell, L. Bai, A. Gulati, G. Tanzer, D. Vincent, Z. Pan, S. Wang, et al. (2024) Gemini 1.5: unlocking multimodal understanding across millions of tokens of context. External Links: 2403.05530 Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p4.1), [§2.2](https://arxiv.org/html/2603.15707v1/#S2.SS2.p1.1).
* R. J. Waldinger and R. C. Lee (1969) PROW: a step toward automatic program writing. In Proceedings of the 1st international joint conference on Artificial intelligence, pp. 241–252. Cited by: [§2.1](https://arxiv.org/html/2603.15707v1/#S2.SS1.p1.1).
* J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. (2022) Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems 35, pp. 24824–24837. Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p3.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and K. Narasimhan (2023a) Tree of thoughts: deliberate problem solving with large language models. Advances in neural information processing systems 36, pp. 11809–11822. Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p3.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2023b) React: synergizing reasoning and acting in language models. In International Conference on Representation Learning, Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* Y. Zhang, J. Yang, Y. Yuan, and A. C. Yao (2023) Cumulative reasoning with large language models. External Links: 2308.04371 Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).
* L. Zhong, Z. Wang, and J. Shang (2024) Debug like a human: a large language model debugger via verifying runtime execution step by step. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 851–870. External Links: [Link](https://aclanthology.org/2024.findings-acl.49/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-acl.49) Cited by: [§1](https://arxiv.org/html/2603.15707v1/#S1.p1.1), [§1](https://arxiv.org/html/2603.15707v1/#S1.p2.1), [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p2.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p1.1), [§4.1](https://arxiv.org/html/2603.15707v1/#S4.SS1.p2.1).
* D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang, D. Schuurmans, C. Cui, O. Bousquet, Q. Le, et al. (2022) Least-to-most prompting enables complex reasoning in large language models. External Links: 2205.10625 Cited by: [§2.3](https://arxiv.org/html/2603.15707v1/#S2.SS3.p1.1).

####  Appendix A Analysis of Solving Different Levels

#####  A.1 APPS

APPS is a well-established dataset for evaluating algorithmic problem-solving capabilities, categorising programming problems into three distinct difficulty levels: Introductory, Interview, and Competition. These levels range from basic coding exercises to advanced competitive programming challenges, providing a structured framework to assess the performance of LLM-based methods across varying complexities.

![Refer to caption](https://2603.15707v1/x7.png)Figure 7: Pass@1 accuracy on the APPS benchmark across different difficulty levels, Introductory , Interview , and Competition , of Direct, LDB, LPW and SEMAG, when using GPT-4o as the LLM backbone. 
Figure [7](https://arxiv.org/html/2603.15707v1/#A1.F7) compares accuracy on the APPS benchmark across different levels of problems. SEMAG demonstrates superior performance in Introductory and Interview levels, achieving 89.4% and 80.4% respectively, which represents a significant margin over existing approaches. Specifically, SEMAG surpasses the next-best LPW approach by 2.2% in the Introductory level and establishes a notable 15.2% advantage in the Interview level. However, in competitive environments, SEMAG (32.6%) shows slightly reduced effectiveness compared to LPW’s 34.8%, suggesting potential areas for optimization in Competition level. The hierarchical prompting strategy affects model performance, resulting in success in visible tests but failure in hidden tests. The baseline Direct exhibits fundamental limitations, particularly in competition contexts (13%), while LDB demonstrates moderate improvements in Interview (52.2%) and Competition (28.3%) levels compared to Direct. These results collectively highlight SEMAG’s exceptional capability in the initial engagement and interpersonal evaluation phases.

#####  A.2 LiveCode

LiveCode benchmark focuses on real-time coding scenarios reflective of practical software development tasks. Its problems are classified into Easy, Medium, and Hard levels, capturing varying degrees of complexity encountered in applied settings.

![Refer to caption](https://2603.15707v1/x8.png)Figure 8: Pass@1 accuracy on the LiveCode benchmark across different difficulty levels, Easy , Medium , and Hard , of Direct, LDB, LPW and SEMAG, when using GPT-4o as the LLM backbone. 
Figure [8](https://arxiv.org/html/2603.15707v1/#A1.F8) compares accuracy on the LiveCode benchmark across different levels of problems. In the Easy level, both SEMAG and LPW achieve the highest accuracy of 86.7%, which is 6.7% higher than the Direct prompting approach (80.0%). This indicates that both methods possess effective representation capabilities in low-complexity scenarios. In the Medium level, SEMAG demonstrates a significant advantage, achieving an accuracy of 60.0%, which surpasses the second-best method, LPW (47.3%), by 12.7%. In the most challenging Hard level, SEMAG continues to lead with an accuracy of 47.5%, outperforming LPW (40.0%) and LDB (35.0%). This validates the strong robustness of SEMAG in extremely complex problems.

####  Appendix B Prompt of SEMAG

Here, we list the prompts of SEMAG in detail as follows.

![Refer to caption](https://2603.15707v1/x9.png)Figure 9: The prompt of Planning Agent. 
![Refer to caption](https://2603.15707v1/x10.png)Figure 10: The prompt of Plan verifying Agent. 
![Refer to caption](https://2603.15707v1/x11.png)Figure 11: The prompt of Coding Agent. 
![Refer to caption](https://2603.15707v1/x12.png)Figure 12: The prompt of Adding Trace Agent. 
![Refer to caption](https://2603.15707v1/x13.png)Figure 13: The prompt of Code Explaining Agent. 
![Refer to caption](https://2603.15707v1/x14.png)Figure 14: The prompt of Suggesting Agent. 
![Refer to caption](https://2603.15707v1/x15.png)Figure 15: The prompt of Debugging Agent. 
![Refer to caption](https://2603.15707v1/x16.png)Figure 16: The prompt of Discussing Agent. 
![Refer to caption](https://2603.15707v1/x17.png)Figure 17: The prompt of Discriminating Agent. 
![Refer to caption](https://2603.15707v1/x18.png)Figure 18: The prompt of Code Refining Agent. 
####  Appendix C Prompt of Self-Evolution Agent

Here, we list the prompt of the Self-Evolution agent as follows.

![Refer to caption](https://2603.15707v1/x19.png)Figure 19: The prompt of LLM Selecting Agent. 
![Refer to caption](https://2603.15707v1/x20.png)Figure 20: The prompt of Link Selecting Agent. 
![Refer to caption](https://2603.15707v1/x21.png)Figure 21: The prompt of Content Summarizing Agent. 
![Refer to caption](https://2603.15707v1/x22.png)Figure 22: The prompt of LLM Deciding Agent. 
![Refer to caption](https://2603.15707v1/x23.png)Figure 23: The prompt of Model Matching Agent. 
####  Appendix D Example Problem

Here, we show how SEMAG works on an example problem(51st problem) from the HumanEval benchmark. The detailed prompts and responses are given as follows.

![Refer to caption](https://2603.15707v1/x24.png)Figure 24: An example of Planning Agent. 
![Refer to caption](https://2603.15707v1/x25.png)Figure 25: An example of Plan Verifying Agent. 
![Refer to caption](https://2603.15707v1/x26.png)Figure 26: An example of Coding Agent. 
![Refer to caption](https://2603.15707v1/x27.png)Figure 27: An example of Embedding Trace Statement Agent. 
![Refer to caption](https://2603.15707v1/x28.png)Figure 28: An example of Code Explaining Agent. 
![Refer to caption](https://2603.15707v1/x29.png)Figure 29: An example of Suggesting Agent. 
![Refer to caption](https://2603.15707v1/x30.png)Figure 30: An example of Debugging Agent. 
![Refer to caption](https://2603.15707v1/x31.png)Figure 31: An example of Debating Agent. 
![Refer to caption](https://2603.15707v1/x32.png)Figure 32: An example of Debating Agent, following Figure [31](https://arxiv.org/html/2603.15707v1/#A4.F31).
![Refer to caption](https://2603.15707v1/x33.png)Figure 33: An example of Discriminating Agent. 
![Refer to caption](https://2603.15707v1/x34.png)Figure 34: An example of Coding Agent (Refine stage).
