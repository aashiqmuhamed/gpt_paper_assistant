# Personalized Daily Arxiv Papers 10/29/2026
Total relevant papers: 15

Paper selection prompt and criteria at the bottom

Table of contents with paper titles:

0. [Beyond the Readout: A Latent Numerical Frame Shared Across Modality and Operation](#link0)
**Authors:** Oriol Juan Sabater, Alex Ferrando de las Morenas, Pau Rodr\'iguez, Xavier Suau

1. [Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards](#link1)
**Authors:** Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang

2. [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](#link2)
**Authors:** Azim Ospanov, Zijin Feng, Ding Ding, Chengwu Liu, Haoli Bai, Jiacheng Sun, Lifeng Shang, Farzan Farnia

3. [LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets](#link3)
**Authors:** Shenghui Li, Thiemo voigt

4. [ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time](#link4)
**Authors:** Emma Andrews, Konstantinos Kontras, Keane Ong, Maarten De Vos, Gianmarco Mengaldo

5. [The uneven rise of AI-generated web content](#link5)
**Authors:** Adam Visokay, Soumyakanti Pan, Molly Griston, Polina Iasakova, Mark Nepf, Denis Peskoff, Riya Sinha, Jikai Sun, Isabelle Thiara, Letao Wang, Yiwei Wu, Lauren Yan, Tyler H. McCormick

6. [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](#link6)
**Authors:** Chang Su, Bin Wu, Emine Yilmaz, Yao Lu

7. [Proactive Memory for Event-Driven LLM Agents](#link7)
**Authors:** Jinyang Li, Zichuan Fu, Xian Wu, Wenlin Zhang, Yimin Deng, Kaifeng Guo, Guojing Li, Junjia QI, Xiangyu Zhao

8. [RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport](#link8)
**Authors:** Dongyue Li, Zebang Cheng, Zhongyi Deng, Hongboxu, Yi Bin, Fei Ma

9. [Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles](#link9)
**Authors:** Yezhou Cheng, Charles Ling

10. [When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](#link10)
**Authors:** Chiming Duan, Tong Jia, Yingxi Chen, Minghua He, Lingzhe Zhang, Ying Li

11. [Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](#link11)
**Authors:** Jiawei Zhou, Bo Peng, Yuxuan Huang, Ming Zhang, Youbang Sun, Xiang Wang, Chaochao Lu

12. [Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](#link12)
**Authors:** Jialin Zhang, Lakshya A Agrawal, Shangyin Tan, Donghyun Lee, Lutfi Eren Erdogan, Dan Klein, Koushik Sen, Alex Dimakis, Matei Zaharia

13. [SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](#link13)
**Authors:** Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler, Cahit Berkay Kazangirler

14. [Prospector: learning a compact graph traversal policy for scientific reasoning](#link14)
**Authors:** Haiqian Yang, Markus J. Buehler

---
## 0. [Beyond the Readout: A Latent Numerical Frame Shared Across Modality and Operation](https://arxiv.org/abs/2610.37422) <a id="link0"></a>
**ArXiv ID:** 2610.37422
**Authors:** Oriol Juan Sabater, Alex Ferrando de las Morenas, Pau Rodr\'iguez, Xavier Suau

**Abstract:** arXiv:2610.37422v1 Announce Type: new  Abstract: When a multimodal model computes 17+35 from text or 91-39 from a rendered image, it produces the same answer, 52. Does it use one internal concept of number for both, or separate machinery for each path? Similarity metrics such as RSA or CKA cannot settle this question. They give the same score to identical and to rotated directions, and two representations can look alike only because both prepare the same output digits. We therefore use causal interventions. For four conditions (text or image, addition or subtraction), we learn a small subspace of Gemma4-12B-it's residual stream in which swapping coordinates swaps the model's answer. The subspaces answer three questions. First, do the conditions write numbers along the same directions? They do not. Reusing a subspace from text in an image on the same operation recovers only 53.2% of its causal effect. A single rotation and rescaling maps one subspace onto the other and raises recovery to 91.4%, so the conditions share one geometry expressed in different coordinates. Second, does this shared geometry only reflect the digit the model is about to print? To test this, we split each subspace into 9 directions that the output layer reads to choose the next digit and 13 directions that it cannot see. The 13 hidden directions still carry the number, yet changing them barely alters the digit being written. Third, what are these hidden directions for? A model must emit a multi-digit answer one digit at a time, so it can compute the full result early and keep it in reserve. When two numbers share their first digit, swapping the number in the hidden directions leaves the digit being written intact and redirects the next digit in 77.6% of cases. The model thus forms an abstract numerical concept upstream and unfolds it across time: multimodal representations share meaning through relational geometry across distinct coordinate frames.

**Comment:** Matches criterion 8 closely: uses causal interventions to analyze internal representations of numerical concepts in a multimodal model, revealing mechanistic interpretability insights about shared latent numerical frames across modalities and operations.
**Relevance:** 8
**Novelty:** 8

---

## 1. [Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.37041) <a id="link1"></a>
**ArXiv ID:** 2610.37041
**Authors:** Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang

**Abstract:** arXiv:2610.37041v1 Announce Type: new  Abstract: Reinforcement learning with verifiable rewards (RLVR) has shown strong empirical gains in improving the reasoning ability of large language models (LLMs) on tasks such as mathematics and programming. However, recent studies have shown that RLVR rollouts often collapse onto a narrow set of reasoning trajectories, limiting the explored reasoning space. Motivated by findings that thinking tokens at critical steps serve as critical structural elements in LLM reasoning pathways, we propose Guided-RLVR, a novel approach that augments RLVR with a lightweight controller. The controller strategically injects semantically meaningful steering tokens into the sampling distribution, encouraging the model to approach problems from multiple reasoning perspectives and thereby expanding the exploration space. Experiments on mathematical reasoning and code generation benchmarks show that Guided-RLVR consistently outperforms existing RLVR methods while producing more diverse reasoning trajectories.

**Comment:** Matches criterion 1 closely: proposes a novel method Guided-RLVR that improves reinforcement learning with verifiable rewards (RLVR) for LLMs, enhancing instruction-following and reasoning diversity via a lightweight controller injecting steering tokens.
**Relevance:** 9
**Novelty:** 7

---

## 2. [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](https://arxiv.org/abs/2610.36767) <a id="link2"></a>
**ArXiv ID:** 2610.36767
**Authors:** Azim Ospanov, Zijin Feng, Ding Ding, Chengwu Liu, Haoli Bai, Jiacheng Sun, Lifeng Shang, Farzan Farnia

**Abstract:** arXiv:2610.36767v1 Announce Type: new  Abstract: Large Language Models (LLMs) have made remarkable progress on solving competition-level mathematics, yet their ability to verify natural-language mathematical proofs remains relatively underexplored. This gap is especially pronounced for Olympiad-level proofs, which require meticulous assessment of each claim in a long reasoning chain. Current proof verification thus primarily relies on expert inspection, which is costly to scale. In this paper, we present a systematic study of LLM-based verification in this setting. Specifically, we introduce a human-curated dataset of USAMO 2025 candidate solutions with expert grading, and conduct a broad evaluation of existing LLM verifiers across frontier models. We also propose TROJAN, an iterative self-critique pipeline for generating high-fidelity adversarial proofs at scale. Our comprehensive evaluation covers 20 models spanning seven metrics, two prompt styles, three inference methods, and three prompt templates, showing that state-of-the-art models still leave considerable room for improvement. To narrow this gap, we propose MABGrader, a Multi-Armed Bandit framework that reframes grading as arm selection over the discrete score space. MABGrader outperforms the SOTA ProofGrader by 26.4% in Quadratic Weighted Kappa and reduces grading error by 14%. Code and dataset are available at https://github.com/aziksh-ospanov/TROJAN.

**Comment:** Matches criterion 12 closely: studies LLM reasoning capabilities and verification of complex reasoning chains in mathematical proofs, proposing a novel Multi-Armed Bandit framework (MABGrader) to improve grading accuracy, which relates to reasoning and evaluation of LLM outputs.
**Relevance:** 7
**Novelty:** 6

---

## 3. [LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets](https://arxiv.org/abs/2610.36386) <a id="link3"></a>
**ArXiv ID:** 2610.36386
**Authors:** Shenghui Li, Thiemo voigt

**Abstract:** arXiv:2610.36386v1 Announce Type: new  Abstract: Low-Rank Adaptation (LoRA) has become a key mechanism for efficiently specializing foundation models into many task- and user-specific variants. Serving many LoRA adapters under a shared resource budget turns post-hoc compression into a two-level allocation problem: rank must be distributed across layers within each adapter and across adapters within the fleet. Although trained LoRAs contain substantial spectral redundancy, spectral reconstruction alone does not determine how much compression an adapter can functionally tolerate. We formulate fleet compression through a functional rank-distortion frontier for each adapter, followed by fleet-level minimax allocation under a shared rank budget. Given exact frontiers, this decomposition is equivalent to joint optimization over all layer ranks. We introduce Functional Rank Allocation (FRA), an unlabeled method for constructing practical frontiers. FRA measures isolated module truncations end to end, uses these measurements as an additive search surrogate solved by dynamic programming, remeasures every complete candidate, and takes the lower-risk envelope with a complementary spectral proposal before exact minimax allocation over the constructed frontiers. Across 78 adapters from three public fleets, FRA improves worst-case and tail utility over uniform spectral compression in constrained-budget regimes. Fixed-budget probes show that isolated costs rank candidates well, but their calibration shifts across proposal shapes; end-to-end verification and the spectral proposal therefore limit functional-search error.

**Comment:** Related to criterion 1: The paper proposes a new method (Functional Rank Allocation) for post-hoc compression of LoRA adapters, which is a fine-tuning related technique improving efficient adaptation of language models.
**Relevance:** 6
**Novelty:** 7

---

## 4. [ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time](https://arxiv.org/abs/2610.36536) <a id="link4"></a>
**ArXiv ID:** 2610.36536
**Authors:** Emma Andrews, Konstantinos Kontras, Keane Ong, Maarten De Vos, Gianmarco Mengaldo

**Abstract:** arXiv:2610.36536v1 Announce Type: new  Abstract: When one time series informs another, the delay at which that information arrives determines if models can utilize this relationship effectively. A source may be strongly predictive at one delay but uninformative at neighboring lags. Therefore, fixed input windows may obscure this structure by bundling informative and irrelevant history together. Transfer entropy (TE) can recover these delays by measuring how much a source's past tells us about a target beyond the target's own history. However, existing TE estimators require separate fits across source and conditioning depths, with further estimation on local windows to track delays over time. We introduce ATEMPO, a diffusion-based transfer entropy estimator amortized over lags and time. ATEMPO samples source and conditioning depths during training and conditions explicitly on temporal position, allowing a single score network to estimate the full TE surface without refitting. Differencing this surface recovers when information arrives. Across synthetic datasets with ground-truth TE, ATEMPO achieves the lowest mean relative error among baselines, and on datasets with known lags, ATEMPO achieves $0.98\pm0.04$ lag-detection accuracy. ATEMPO requires a single fit across source depths $K=6$ and target depths $L=3$, whereas existing estimators require 18 separate fits to evaluate the same $K \times L$ grid. On three systems with time-varying lag, ATEMPO is the only estimator to maintain perfect lag-detection accuracy across all evaluated window lengths. These recovered delays improve downstream forecasting: ATEMPO-selected inputs reduce MSE on WEATHER-5K by 7.25%, while 120 selected inputs outperform the benchmark's 240-feature default by 4.6%. Across three brain-computer interface tasks, using ATEMPO-selected lags achieves the highest or equal-best $R^2$, improving mean $R^2$ by 4.1% relative to the strongest competing baseline.

**Comment:** Criterion 2: The paper introduces ATEMPO, a diffusion-based transfer entropy estimator amortized over lags and time, which is a novel statistical method related to time series information flow estimation. While not directly about language models, it presents a clever statistical method involving diffusion models and estimation that could be relevant to contamination detection or membership inference in principle.
**Relevance:** 5
**Novelty:** 7

---

## 5. [The uneven rise of AI-generated web content](https://arxiv.org/abs/2610.36631) <a id="link5"></a>
**ArXiv ID:** 2610.36631
**Authors:** Adam Visokay, Soumyakanti Pan, Molly Griston, Polina Iasakova, Mark Nepf, Denis Peskoff, Riya Sinha, Jikai Sun, Isabelle Thiara, Letao Wang, Yiwei Wu, Lauren Yan, Tyler H. McCormick

**Abstract:** arXiv:2610.36631v1 Announce Type: new  Abstract: In less than five years, generative artificial intelligence (AI) has dramatically reshaped the public-facing web. Using a sample of more than 5 million crawlable webpages, we demonstrate that the share containing AI-generated text has increased precipitously, but unevenly. Our analyses reveal substantial differences in AI composition across language and domain categories (e.g., .edu, .com, or .gov). A higher fraction of English-language webpages contain AI-generated text compared to pages in other languages, and prevalence is substantially lower on .gov and .edu domains compared to .com. These distinctions persist even after accounting for compositional effects. We also find heterogeneity based on a page's position in the connectivity structure of the web. AI-generated text is most common and has increased most rapidly in pages that are the least central in the graph, which drives much of the overall growth in AI-generated text. A slower increase has taken place for more central pages, with the most central tier emerging as the least likely to contain AI-generated text. Methodologically, we use multiple AI detection tools, and generate estimates using a Bayesian hierarchical model that incorporates corrections for the detectors' statistical properties (both false positives and false negatives) and allows for different detector performance across groups, while propagating uncertainty in detector error rates into prevalence estimates. Our work suggests that AI is a prominent, but varied, contributor to public information and internet-based communication.

**Comment:** Related to criterion 5: The paper provides a large-scale empirical survey and Bayesian modeling of AI-generated web content prevalence, offering new data on real-world usage of generative AI.
**Relevance:** 5
**Novelty:** 6

---

## 6. [What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models](https://arxiv.org/abs/2610.37631) <a id="link6"></a>
**ArXiv ID:** 2610.37631
**Authors:** Chang Su, Bin Wu, Emine Yilmaz, Yao Lu

**Abstract:** arXiv:2610.37631v1 Announce Type: new  Abstract: Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood across models. A higher score suggests that the knowledge may be less consistently represented across years of web text. We evaluate six benchmarks covering diverse topics using six models from multiple open-source model families. We find that low- and high-TVS items are learned similarly early in training, but high-TVS items improve faster later on. At the end of the pretraining run, high-TVS items outperform low-TVS items in 34 of 36 model-benchmark settings, with an average advantage of 7.3 points of chance-normalized accuracy. This pattern is most robust on knowledge-intensive tasks, even when comparing items of similar difficulty. Our findings reveal differences in how knowledge is learned over the course of pretraining, with temporal variability providing a diagnostic of these learning dynamics beyond aggregate benchmark scores.

**Comment:** Related to criterion 2: The paper proposes a temporal variability score to analyze knowledge acquisition dynamics in pretrained language models, which is a novel statistical diagnostic potentially useful for understanding test set contamination or knowledge memorization patterns.
**Relevance:** 5
**Novelty:** 6

---

## 7. [Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967) <a id="link7"></a>
**ArXiv ID:** 2610.36967
**Authors:** Jinyang Li, Zichuan Fu, Xian Wu, Wenlin Zhang, Yimin Deng, Kaifeng Guo, Guojing Li, Junjia QI, Xiangyu Zhao

**Abstract:** arXiv:2610.36967v1 Announce Type: new  Abstract: Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal trajectories, and behavioral regularities. Trajectory facts are checked against source events, and regularities are assessed through historical replay before being matched to current conditions. We also construct ProactiveStream, a longitudinal benchmark covering three application scopes, where agents process isolated event streams chronologically under episode-aware opportunity labels. On ProactiveStream, ProactMem achieves an overall effectiveness (F1) of 52.6%, a 21.4% relative improvement over the strongest of five external baselines. Code is available at: https://anonymous.4open.science/r/ProactMem-5351/.

**Comment:** Does not match any criteria related to RLHF, contamination, diffusion LMs, or interpretability; proposes Proactive Memory for LLM agents to anticipate events, focusing on memory organization and event streams rather than instruction-following or contamination.
**Relevance:** 3
**Novelty:** 6

---

## 8. [RPSD: Retrieval-Privileged On-Policy Self-Distillation with Optimal Transport](https://arxiv.org/abs/2610.37281) <a id="link8"></a>
**ArXiv ID:** 2610.37281
**Authors:** Dongyue Li, Zebang Cheng, Zhongyi Deng, Hongboxu, Yi Bin, Fei Ma

**Abstract:** arXiv:2610.37281v1 Announce Type: new  Abstract: Sequential recommendation predicts a user's next interaction from historical behavior. Recent LLM-based methods recast this task as generative recommendation and increasingly adopt reinforcement learning such as GRPO for post-training. However, these methods suffer from two limitations, namely credit-blind optimization, where a sequence-level reward is shared across all generated tokens, and collaborative-blind supervision, where each training signal is derived from a single user and ignores behavioral patterns shared across similar users. To address both issues, we propose Retrieval-Privileged on-policy Self-Distillation (RPSD). For credit-blind optimization, we introduce on-policy self-distillation (OPSD), in which a teacher with privileged knowledge re-evaluates the student's on-policy response, and the token-level confidence difference between the student and teacher reshapes the shared sequence-level advantage into token-specific credit. However, the privileged knowledge in vanilla OPSD is still derived from a single user, leaving collaborative-blind supervision unresolved. We therefore ground the teacher in collaborative behavioral evidence from similar users. Specifically, we use temporally aware optimal transport (OT) to compare interaction trajectories across users by jointly considering item similarity and temporal structure, and further apply diversity-aware selection to retain complementary trajectories as privileged evidence. In this way, on-policy self-distillation provides fine-grained token-level credit, while OT enriches the teacher with structured cross-user evidence. To the best of our knowledge, this is the first work to bring on-policy self-distillation to sequential recommendation and to use cross-user behavior as its privileged signal. Extensive experiments across multiple real-world datasets demonstrate that RPSD achieves state-of-the-art performance.

**Comment:** No direct match to any specific criterion. The paper proposes a method for sequential recommendation using on-policy self-distillation and optimal transport, which is an application of RL and distillation but not specifically about RLHF or instruction-following fine-tuning for language models.
**Relevance:** 3
**Novelty:** 6

---

## 9. [Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles](https://arxiv.org/abs/2610.36415) <a id="link9"></a>
**ArXiv ID:** 2610.36415
**Authors:** Yezhou Cheng, Charles Ling

**Abstract:** arXiv:2610.36415v1 Announce Type: new  Abstract: Tool-assisted planning success can reflect external search and verification, leaving a model's unaided planning ability unresolved. We isolate innate planning through complete plans generated in one response without tools or execution feedback. We propose a verifiable framework that decomposes success-weighted plan efficiency as $\mathrm{SPE}=R\times Q\times E$: execution reliability, planning coordination among legal plans, and action economy among completed plans. Trajectory replay and certified optima verify these factors; the joint score includes unsuccessful attempts. We evaluate 8,400 full-plan outputs from seven model conditions on $4\times4$ sliding puzzles, controlling exact horizon and obstacle count in the primary cohort. Models that complete every trial still become less economical at longer horizons, while higher efficiency among completed plans can coexist with poor goal attainment. SPE separates the overall capability hierarchy, while its factors distinguish coordination failure from inefficient completion. The framework makes long-horizon limitations in unaided planning quantitatively verifiable.

**Comment:** No direct match to any criteria. Studies innate planning ability of LLMs on sliding puzzles with a verifiable efficiency metric, but this is about planning performance evaluation rather than new paradigms for open-ended text generation evaluation or reasoning transparency.
**Relevance:** 3
**Novelty:** 5

---

## 10. [When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents](https://arxiv.org/abs/2610.36471) <a id="link10"></a>
**ArXiv ID:** 2610.36471
**Authors:** Chiming Duan, Tong Jia, Yingxi Chen, Minghua He, Lingzhe Zhang, Ying Li

**Abstract:** arXiv:2610.36471v1 Announce Type: new  Abstract: LLM agents interact with Web services to perform tasks on users' behalf. Errors during these interactions can disrupt execution and prevent task completion, motivating external intervention. However, agents may self-recover through continued execution, raising the question of when to intervene and when to wait for self-recovery. We present an empirical study of errors and self-recovery in LLM agents. We construct ReInBench, a dataset containing 1,259 agent traces and 1,403 error events across computer-use and Web tasks. Our study examines how often and how quickly agents self-recover, how self-recovery relates to subsequent execution and task completion, and whether self-recovery can be predicted when an error occurs. We find that 725 error events self-recover, often within a few steps, with self-recovery performance differing across Execution LLMs. Self-recovery can also help agents recover from subsequent errors of the same type and support overall task completion. Intervention should therefore prioritize errors unlikely to self-recover, while allowing agents to continue when self-recovery is likely. Building on these empirical findings, we propose ReCoF, a method that predicts whether an error will self-recover to inform whether additional intervention is needed. ReCoF achieves an average relative improvement of 9.02% in Macro-F1 over the strongest baseline on ReInBench. Our code and data can be found at https://method-notes.github.io/ReCoF/.

**Comment:** Does not match criteria related to RLHF, contamination, diffusion LMs, or interpretability; studies error self-recovery in LLM agents and intervention timing, which is an empirical study of agent behavior rather than methodological improvements or contamination detection.
**Relevance:** 3
**Novelty:** 5

---

## 11. [Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](https://arxiv.org/abs/2610.37201) <a id="link11"></a>
**ArXiv ID:** 2610.37201
**Authors:** Jiawei Zhou, Bo Peng, Yuxuan Huang, Ming Zhang, Youbang Sun, Xiang Wang, Chaochao Lu

**Abstract:** arXiv:2610.37201v1 Announce Type: new  Abstract: Skill optimizers adapt an agent to long-horizon tasks, such as repairing a terminal environment, by rewriting its skill, a natural-language procedure in its context, and keeping the edits that raise success on a small dev set. On such tasks success is noisy, so a gain on a small dev set does not show that an edit helps, and a success score does not show what the edit costs. We introduce BiPA, which replays an optimizer's acceptance rule on candidates identical to its seed to measure what selection alone reports, and records each episode as a bipartite graph of turns and the text they read to trace extra input tokens to the behavior behind them. Across three optimizers, three agentic benchmarks and two models, the learned skills succeed about as often as their hand-written seed, 0.1 points higher on average. Their dev gains vanish on test: keeping the best of several candidates on at most 30 tasks reports gains this large even when none changed. They read about 16% more input tokens: the optimizers almost always add rules, half to re-check work and some to act one call at a time, and the agent follows them as extra turns, each re-sending the whole conversation. Four principles follow: accept an edit only if its gain exceeds what selection alone reports; charge it for the turns it adds, not for its length; let the editor delete and merge rules; show it what earlier rules cost. Code is available at https://github.com/valleysprings/BiPA.git.

**Comment:** Does not match any specific criterion related to RLHF, contamination, diffusion LMs, or interpretability; focuses on skill optimization and agentic tasks with bipartite attribution, which is more about agent skill editing and evaluation.
**Relevance:** 3
**Novelty:** 5

---

## 12. [Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](https://arxiv.org/abs/2610.36774) <a id="link12"></a>
**ArXiv ID:** 2610.36774
**Authors:** Jialin Zhang, Lakshya A Agrawal, Shangyin Tan, Donghyun Lee, Lutfi Eren Erdogan, Dan Klein, Koushik Sen, Alex Dimakis, Matei Zaharia

**Abstract:** arXiv:2610.36774v1 Announce Type: new  Abstract: Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on each optimization step instead of one candidate at a time. In our sweep on two tasks, most batched runs finished in half the wall-clock time or less, and the fastest in about a quarter to a third. Batched settings also achieved higher held-out test scores, from 68.9% to 72.1% on LiveBench-Math (with $2\times2$) and from 49.0% to 60.0% on HoVer (with $8\times1$). A simple runtime model explains the measured speedups under a finite worker pool, and batched settings also spend their metric-call and dollar budgets more efficiently. We frame the axes along which a reflective optimization step can scale in parallel, a first look at allocating a fixed optimization budget across them.

**Comment:** No direct match to any specific criterion. The paper improves efficiency of reflective optimization loops for text generation but does not address RLHF fine-tuning methods, contamination, diffusion LMs, or evaluation paradigms explicitly.
**Relevance:** 3
**Novelty:** 5

---

## 13. [SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.36991) <a id="link13"></a>
**ArXiv ID:** 2610.36991
**Authors:** Zafer Sahinoglu, Abdulazeez Mohammed, Buse Yaren Kazangirler, Cahit Berkay Kazangirler

**Abstract:** arXiv:2610.36991v1 Announce Type: new  Abstract: Retrieval-augmented generation (RAG) systems ground large language models (LLMs) by retrieving external evidence and conditioning generation on the retrieved context. Although dense retrieval is effective for local semantic matching, independently ranked retrieval can return redundant passages, miss cross-chunk dependencies, and provide incomplete evidence for multi-hop reasoning. We propose SpectRAG, a spectral graph-augmented retrieval framework that combines hybrid candidate seeding, weighted chunk graph construction, graph-based expansion, spectral relevance propagation, and token-budgeted context selection. Document chunks are represented by dense semantic embeddings and graph-spectral coordinates derived from a weighted chunk graph whose edges encode semantic similarity, document adjacency, section hierarchy, shared entities, citation links, and similarity between LLM-generated utility questions. At query time, SpectRAG builds a high-recall seed set using exact inner-product search and hybrid relevance signals, expands it over the chunk graph, re-scores candidates using graph proximity and spectral information, and assembles the final context under a fixed token budget. The goal is not merely to retrieve individually similar chunks, but to construct a context that is relevant, diverse, structurally connected, and sufficient for grounded reasoning. Experiments on MultiHopRAG, UltraDomain, and long-document question-answering settings show that SpectRAG improves broad evidence recovery and achieves competitive generation quality against dense, hybrid, HyDE, LightRAG, and NaiveRAG baselines. The results further indicate that graph-spectral structure is particularly useful for inference-oriented and cross-document retrieval, while highlighting trade-offs in early precision, computational cost, and domain-dependent performance.

**Comment:** No direct match to any specific criterion. The paper proposes a graph-augmented retrieval method for multi-hop retrieval-augmented generation, which is an application-focused improvement in retrieval for LLMs, not about RLHF, contamination, diffusion LMs, or evaluation paradigms.
**Relevance:** 3
**Novelty:** 5

---

## 14. [Prospector: learning a compact graph traversal policy for scientific reasoning](https://arxiv.org/abs/2610.37121) <a id="link14"></a>
**ArXiv ID:** 2610.37121
**Authors:** Haiqian Yang, Markus J. Buehler

**Abstract:** arXiv:2610.37121v1 Announce Type: new  Abstract: Scientific reasoning in specialized engineering fields depends on knowledge scattered across the literature, often proprietary and absent from frontier LLM training data. In such domains, frontier models tend to give generic answers. Knowledge graphs (KGs) can ground LLM reasoning. Because a graph is too large to provide in full, typical LLM+KG systems preselect a portion, deciding relevance before reasoning begins. Here we train a compact model, Prospector, to reason over a domain knowledge graph by traversing it step by step, seeking evidence in light of what it has already found. Prospector calls a small set of tools one at a time to progressively build its context, and answers with a chain of evidence that can be checked edge by edge against what its tools retrieved from the graph. On a knowledge graph built from the semiconductor-manufacturing literature, Prospector approaches the strongest off-the-shelf models given the same graph and tools, and it far exceeds off-the-shelf models answering closed-book or from a pre-selected portion of the graph. Although trained only on the semiconductor graph, Prospector transfers to unseen knowledge graphs from three other distinct fields: bio-inspired materials, per- and polyfluoroalkyl substances (PFAS) and materials properties. Served on a single GPU, Prospector answers faster and at a fraction of the cost of a hosted service, while keeping proprietary data on the owner's hardware. We find that the policy's latent state is indicative of its next move on both seen and unseen graphs, and modulating the latent state can steer the policy from one behavior mode to another. These results suggest a practical LLM + KG paradigm for scientific and engineering reasoning over private data, in which a compact model trained on a graph from published literature transfers its traversal to unseen graphs that stay with their owners.

**Comment:** No direct match to any specific criterion. The paper focuses on a compact graph traversal policy for scientific reasoning over knowledge graphs, which is an application of LLM+KG systems rather than methodological improvements to RLHF or instruction-following, or other listed criteria.
**Relevance:** 3
**Novelty:** 4

---


---

## Paper selection prompt
 1. New methodological improvements to RLHF or instruction-following which are specific fine-tuning steps that are taken to make language models better at following user instructions across a range of tasks.
    - Relevant: papers that discuss specific methods like RLHF, or instruction-tuning datasets, improving these methods, or analyzing them. Usually these papers will explicitly mention RLHF, instruction-following or instruction-tuning.
    - Not relevant: papers about adaptation to some task. Simply following instructions or inputs are not sufficient.
 2. Shows new powerful test set contamination or membership inference methods for language models. Test set contamination is the phenomenon where a language model observes a benchmark dataset during pretraining.
    - Relevant: test statistics that can detect contamination of benchmarks in language models. statistics that can provide guarantees are more interesting. membership inference methods that are general enough to apply to language models are also relevant.
    - Not relevant: any papers that do not consider language models, or that do not consider test set contamination.
 3. Shows a significant advance in the performance of diffusion language models.
    - Relevant: papers that study language models that are also diffusion models. Continuous diffusions are even more relevant, while discrete diffusions are less so.
    - Not relevant: papers about image diffusions like DALL-E or Stable Diffusion, or papers that do not explicitly mention language models or applications to text.
 4. Describes new paradigms to evaluating open-ended text generation. Evaluating the outputs of language models is hard, especially in open-ended settings like for chatbots.
    - Relevant: papers that fundamentally rethink language model evaluation -- especially by accounting for subjectivity or using adversaries.
    - Not relevant: specific evaluations for specific tasks, identifying new properties or flaws of language models, or simply collecting new data.
 5. Conducts surveys or provides data into real-world usage and safety properties of language models.
    - Relevant: papers that create new datasets or surveys on real-world usage of language models.
    - Not relevant: papers that apply language models to new real-world tasks.
 6. Studies 'scaling laws' in the context of neural networks. Scaling laws refer to the very clear power-law relationship between the size or computational power used to train a model and the performance of that model.
    - Relevant: theoretical or conceptual explanation behind scaling laws for language models.
    - Not relevant: papers that have experiments at different model scales (but do not explicitly fit a scaling law) or papers that mention scaling laws, but the scaling laws are not the central subject of the paper
 7. Presents new methods or improvements for sparse autoencoders in neural network interpretability. Sparse autoencoders are unsupervised learning techniques that learn sparse representations of neural network activations to understand what features networks detect.
    - Relevant: papers that explicitly mention sparse autoencoders, sparse coding, or sparse feature extraction applied to understanding neural networks, language models, or other AI systems.
    - Not relevant: papers about general autoencoders without sparsity constraints, or sparse methods not applied to interpretability.
 8. Demonstrates new mechanistic interpretability techniques or discoveries about how neural networks work internally. Mechanistic interpretability seeks to understand the algorithms and circuits that neural networks learn.
    - Relevant: papers about circuit analysis, feature visualization, activation patching, causal interventions on neural networks, or reverse-engineering specific algorithms learned by models.
    - Not relevant: papers that only do black-box analysis or correlation studies without mechanistic understanding.
 9. Shows advances in machine unlearning techniques for removing specific knowledge or behaviors from trained models.
    - Relevant: papers on forgetting specific data, removing harmful capabilities, or selectively editing model knowledge while preserving other capabilities.
    - Not relevant: papers about general model editing or fine-tuning without specific unlearning focus.
 10. Presents methods for tamper resistance, robustness against adversarial modifications, or secure AI systems.
    - Relevant: papers on preventing model poisoning, backdoor attacks, or making AI systems resistant to tampering or manipulation.
    - Not relevant: papers only about general adversarial robustness without security/tamper resistance focus.
 11. Studies AI alignment techniques, value learning, or methods to ensure AI systems behave according to human values and intentions.
    - Relevant: papers on reward modeling, constitutional AI, value alignment, or techniques to make AI systems more aligned with human preferences.
    - Not relevant: papers focused only on performance improvement without alignment considerations.
 12. Advances in LLM reasoning capabilities, chain-of-thought reasoning, or understanding how language models perform complex reasoning tasks.
    - Relevant: papers on step-by-step reasoning, logical inference in LLMs, reasoning chain analysis, or methods to improve reasoning capabilities.
    - Not relevant: papers about reasoning in non-LLM contexts or that don't focus on reasoning mechanisms.
 13. Presents new methods for AI control, oversight, or monitoring of AI system behavior during deployment.
    - Relevant: papers on AI governance techniques, monitoring systems, control mechanisms, or methods to maintain oversight of deployed AI systems.
    - Not relevant: papers focused only on training-time controls without deployment considerations.
 14. Shows advances in chain-of-thought monitoring, reasoning transparency, or methods to understand AI decision-making processes.
    - Relevant: papers on monitoring reasoning chains, making AI reasoning more transparent, or techniques to track how models arrive at conclusions.
    - Not relevant: papers about general explainability without specific focus on reasoning processes.
 15. Studies ControlArena, Inspect framework, or similar evaluation platforms for AI safety and control.
    - Relevant: papers using or extending these evaluation frameworks, comparative studies using these platforms, or methodological improvements to these tools.
    - Not relevant: papers that mention these tools only in passing without substantial use or analysis.
 16. Advances in latent reasoning, implicit reasoning processes, or understanding hidden computational processes in neural networks.
    - Relevant: papers on uncovering implicit reasoning, analyzing hidden computational steps, or methods to make latent reasoning processes more explicit.
    - Not relevant: papers about explicit reasoning without focus on hidden or latent processes.
 17. Studies data poisoning attacks or defenses in machine learning systems.
    - Relevant: papers on poisoning training data to manipulate model behavior, detecting poisoned data, or defending against data poisoning attacks.
    - Not relevant: papers about general adversarial examples at inference time without training data manipulation.
 18. Advances in data-centric AI approaches that focus on improving data quality, curation, or data-driven methods for ML.
    - Relevant: papers on data quality assessment, data selection, data augmentation strategies, curriculum learning based on data properties, or systematic approaches to dataset creation and curation.
    - Not relevant: papers that simply use standard datasets without focusing on data-centric methodology.
 19. Studies security of LLMs and methods to protect language models from attacks or exploitation.
    - Relevant: papers on prompt injection defenses, jailbreak prevention, securing LLM deployments, protecting against extraction attacks, or hardening LLM systems against adversarial users.
    - Not relevant: papers about using LLMs for security applications, or general robustness without security focus.

 In suggesting papers to your friend, remember that he enjoys papers on statistical machine learning, and generative modeling in natural language processing.
 Your friend also likes learning about surprising empirical results in language models, as well as clever statistical tricks.
 He does not want to read papers that are about primarily applications of methods to specific domains.