---
title: "A Comprehensive Overview of Large Language Models"
source: "https://arxiv.org/pdf/2307.06435.pdf"
author: "Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad"
published: 2023-07-12
created: 2023-08-29
description: "Large Language Models (LLMs) have recently demonstrated remarkable"
tags:
  - to-process
  - llm-foundations
---

‌A Comprehensive Overview of Large Language Models

18 Aug 2023

Humza Naveed, Asad Ullah Khan\*, Shi Qiu\*, Muhammad Saqib\*, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, Ajmal Mian

  


Abstract—

arXiv:2307.06435v2

[cs.CL]

## Large Language Models (LLMs) have recently demonstrated remarkable capabilities in natural language processing tasks and beyond. This success of LLMs has led to a large influx of research contributions in this direction. These works encompass diverse topics such as architectural innovations of the underlying neural networks, context length improvements, model alignment, training datasets, benchmarking, efficiency and more. With the rapid development of techniques and regular breakthroughs in LLM research, it has become considerably challenging to perceive the bigger picture of the advances in this direction. Considering the rapidly emerging plethora of literature on LLMs, it is imperative that the research community is able to benefit from a concise yet comprehensive overview of the recent developments in this field. This article provides that overview to the research community. It not only focuses on a systematic treatment of the existing literature on a broad range of LLM related concept, but also pays special attention to providing comprehensive summaries with extensive details about the individual existing models, datasets and major insights. We also pay heed to aligning our overview with the emerging outlook of this research direction by accounting for the other recently materializing reviews of the broader research direction of LLMs. Our self-contained comprehensive overview of LLMs discusses relevant background concepts along with covering the advanced topics at the frontier of this research direction. This review article is intended to not only provide a systematic survey, but also a quick comprehensive reference for the researchers and practitioners to draw insights from extensive informative summaries of the existing works to advance the LLM research direction.

Index Terms—

## Large Language Models, LLMs, chatGPT, LLM training, LLM Benchmarking

  


1. Introduction

[Language plays a fundamental role in facilitating commu- nication and self-expression for humans, and likewise, com- munication holds paramount importance for machines in their interactions with humans and other systems. Large Language Models (LLMs) have emerged as cutting-edge artificial intel- ligence systems designed to process and generate text, aiming to communicate coherently [](#bookmark56)1]. The need for LLMs stems from the growing demand for machines to handle complex lan- guage tasks, including translation, summarization, information retrieval, and conversational interactions. Recently, significant breakthroughs have been witnessed in language models, pri- marily attributed to deep learning techniques, advancements in

Version: 01 (update on July 10, 2023).

[GitHub link:](https://github.com/humza909/LLM_Survey.git) <https://github.com/humza909/LLM_Survey.git>

\* is for equal contribution.

[Contact e-mail: humza\_naveed@yahoo.com](mailto:humza_naveed@yahoo.com)

  


![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/dyNIN4uJ4DRHiMA_EDjB4RdP5iSIKNp58dodTJock_A-Image_001.jpg)

  


‌Fig. 1: The trends in the number of LLM models introduced over the years.

  


[neural architectures like transformers, increased computational capabilities, and the accessibility of training data extracted from the internet [](#bookmark57)2[]. These developments have brought about a revolutionary transformation by enabling the creation of Large Language Models (LLMs) that can approximate human- level performance on certain evaluation benchmarks [](#bookmark58)3[], [](#bookmark59)4].

[LLMs, particularly pre-trained language models (PLM), have shown tremendous generalization abilities for text under- standing and generation tasks while trained in a self-supervised setting on a large corpus of text [](#bookmark60)5[], [](#bookmark61)6[], [](#bookmark62)7]. The performance of pre-trained language models (PLMs) improves significantly when fine-tuned for downstream tasks, surpassing the perfor- mance of models trained from scratch. These characteristics of language models motivated researchers to train larger PLMs on even bigger datasets and found that scaling model and dataset size further improve the generalization abilities.

[Now modern LLMs are capable of performing various tasks like code generation, text generation, tool manipulation, rea- soning, and understanding in zero-shot and few-shot settings in diverse domains, even without requiring any fine-tuning on downstream tasks [](#bookmark63)8[], [](#bookmark64)9[], [](#bookmark65)10[]. Such generalization was previously unattainable with smaller models, marking a signif- icant advancement in language modeling. This development has sparked enthusiasm and excitement within the research community for the enhancement of LLM architectures and training strategies, leading to the development of numerous LLMs [](#bookmark66)11[], [](#bookmark67)12[], [](#bookmark68)13[], [](#bookmark63)8[], [](#bookmark64)9[], [](#bookmark65)10[], [](#bookmark69)14].

[The graph presented in Fig](#bookmark1) 1 depicts an increasing trend

  


![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/JpqK8Q7vQHoReTmbe4PlrOAl26hsqw3MvYsSKNZDFx0-Image_002.jpg)

  


‌Fig. 2: The progressive introduction of LLM models demonstrates advances in natural language processing explicitly adapted to various fields and provides increased research, analysis, and application capabilities.‌

  


[in the number of released LLMs, including open-source and closed-source models, over the years. Furthermore, Fig](#bookmark2) 2 [highlights the names of significant releases of various LLMs and Fig](#bookmark4) 3 provides a broader overview of LLMs.

[During the early days of Large Language Models (LLMs), many research efforts focused on developing models for transfer learning to downstream tasks [](#bookmark66)11[], [](#bookmark67)12[], [](#bookmark70)15[] until the emergence of models like GPT-3 [](#bookmark63)8[], which demonstrated impressive performance even without fine-tuning. Due to the closed-source nature of GPT-3, there was a demand for open- source alternatives, leading to the development of various models [](#bookmark64)9[], [](#bookmark65)10[] operating at the scale of GPT-3 and trained on extensive web-based datasets [](#bookmark71)16[], [](#bookmark72)17[], [](#bookmark73)18[], [](#bookmark74)19[]. Subse- quently, researchers proposed several architectural designs and training strategies that showed superior performance compared to GPT-3 across various tasks [](#bookmark70)15[], [](#bookmark69)14[], [](#bookmark75)20[], [](#bookmark76)21].

[The performance of LLMs improves further with instruc- tion fine-tuning, outperforming pre-trained LLMs on various benchmarks [](#bookmark77)22[], [](#bookmark78)23]. Instruction fine-tuning of LLMs refers to a specific training approach by incorporating additional prompts or instructions during the fine-tuning phase to guide the output and thus enable the users to have more fine- grained control over the outputs of LLMs. These prompts can be natural language instructions or example demonstrations based on the task’s requirement. In the literature, different

[datasets have been curated for instruction fine-tuning. These datasets include more instances and tasks that further improve the performance over baselines [](#bookmark79)24[], [](#bookmark78)23[], [](#bookmark80)25[], [](#bookmark81)26[]. When performing instruction fine-tuning, all the model parameters need to be updated. However, parameter-efficient fine-tuning takes a different approach by updating only a small number of parameters while still maintaining good performance. This method keeps the original model frozen and adds a few extra parameters at different locations within the model [](#bookmark82)27[], [](#bookmark83)28[], [](#bookmark84)29[], [](#bookmark85)30[], [](#bookmark86)31]. This approach helps achieve efficient fine- tuning while minimizing the impact on the model’s overall performance.

[Due to the success of LLMs on a wide variety of tasks, the research literature has recently experienced a large influx of LLM related contributions. Naturally, the research community has started the effort of organizing this literature as survey articles. For instance, Zhou et al. [](#bookmark87)32[] presented an overview of the foundation models. An impressive effort is recently made by Zhou et al. [](#bookmark88)33[] in their survey that also discusses aspects related to model architectures, fine-tuning, emergent abilities, and more. Another recent survey on augmented lan- guage models provides a historical account of the foundation models [](#bookmark89)34]. In contrast to these surveys, our contribution focuses on providing a comprehensive yet concise overview of the general direction of LLM research. On one hand, this

  


![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/GjpGJEYzxAtUFloA4Wmn28W9Ah1Wnz1CLM4ML2SVpcw-Image_003.gif)

‌Fig. 3: A broader overview of LLMs, dividing LLMs into four branches: 1. Training 2. Inference 3. Applications 4. Challenges‌

  


article summarizes more details of the individual models as compared to the existing efforts. On the other, it also covers more models in providing their summaries. It also delves into the details of model development, architectures, training datasets, and other related concepts to provide a self-contained comprehensive overview of this direction. Hence, this article addresses an important gap of providing a concise yet compre- hensive overview of the rapidly developing general direction of LLM research. Our key contributions are summarized as follows.


	* We present the first survey on the developments in LLM research with the specific aim of providing concise yet comprehensive overview of the direction. We present extensive summaries that include fine-grained details of the reviewed contributions.
	* In this self-contained article, we cover a range of concepts to comprehend the general direction of LLMs, including background concepts, popular models, crucial discover- ies, related datasets and evaluation details etc.
	* Besides paying special attention to the chronological order of LLMs throughout the article, we also summarize major findings of the popular contributions, and provide detailed discussion on the key design and deploymentaspects of LLMs to help practitioners to effectively leverage this technology.

[It is noteworthy that although this article is the first contri- bution in its own right in terms of providing a concise yet comprehensive overview of LLMs, our work complements the recent (and emerging) surveys of this direction, e.g., [](#bookmark88)33[], [](#bookmark87)32[]. Infrequently, we also loosely follow the existing terminologies to ensure providing a more standardized outlook of this research direction. For instance, following [](#bookmark88)33], our survey considers a language model to be *large* [if it has 10B parameters or more. Hence, we discuss such models in detail in this survey. We refer the readers interested in smaller models to [](#bookmark90)35[], [](#bookmark91)36[], [](#bookmark87)32].

[The organization of this paper is as follows. Section](#bookmark6) II [dis- cusses the background of LLMs. Section](#bookmark16) III [focuses on LLMs overview, architectures, and training pipelines and strategies. Section](#bookmark39) IV [presents the key findings derived from each LLM. Section](#bookmark40) V [highlights the configuration and parameters that play a crucial role in the functioning of these models. The LLM training and evaluation benchmarks are discussed in sec- tion](#bookmark41) VI, followed by concluding remarks and future direction in the conclusion section.
2. ‌BACKGROUND‌

We provide the relevant background to understand the key concepts related to LLM in this section. Aligned with our objective of providing a comprehensive overview of this di- rection, this section offers a comprehensive yet concise outline of the fundamental concepts. In natural language processing literature, these concepts are of standard nature. Hence, we focus more on the intuitive aspects and refer the readers interested in details to the original works we cite in our discussion.

  



	1. Tokenization
	
	[LLMs are trained on text to predict text, and similar to other natural language processing systems, they use tokeniza- tion [](#bookmark92)37[] as the essential preprocessing step. It aims to parse the text into non-decomposing units called tokens. Tokens can be characters, subwords [](#bookmark93)38[], symbols [](#bookmark94)39[], or words, depending on the size and type of the model. Some of the commonly used tokenization schemes in LLMs are briefed here. Readers are encouraged to refer to [](#bookmark95)40] for a detailed survey.
	
	
		1. [WordPiece [](#bookmark96)41]: [It was introduced in [](#bookmark96)41] as a novel text
		
		segmentation technique for Japanese and Korean languages to improve the language model for voice search systems. Word- Piece selects tokens that increase the likelihood of an n-gram- based language model trained on the vocabulary composed of tokens.
		2. [BPE [](#bookmark94)39]: Byte Pair Encoding (BPE) has its origin in compression algorithms. It is an iterative process of generating tokens where pairs of adjacent symbols are replaced by a new symbol, and the occurrences of the most occurring symbols in the input text are merged together.
		3. [UnigramLM [](#bookmark93)38]: In this tokenization, a simple unigram language model (LM) is trained using an initial vocabulary of subword units. The vocabulary is pruned iteratively by removing the lowest-probability items from the list, which are the worst performing on the unigram LM.
	2. Attention
	
	Attention, particularly *selective attention*[, has been widely studied under perception, psychophysics and psychology. Se- lective attention can be conceived as “the programming by the O of which stimuli will be processed or encoded and in what order this will occur” [](#bookmark97)42]. While this definition has its roots in visual perception, it has uncanny similarities with the recently formulated *attention* [[](#bookmark98)43[], [](#bookmark99)44] (which stimuli will be processed) and *positional encoding* [(in what order this will occur) [](#bookmark99)44[] in LLMs. We discuss both in sections](#bookmark8) II-C [and](#bookmark9) II-D, respectively.
	3. ‌Attention in LLMs
	
	The attention mechanism computes a representation of the input sequences by relating different positions (*tokens*) of these sequences. There are various approaches to calculating and implementing attention, out of which some famous types are given below.
	
	
		1. [Self-Attention [](#bookmark99)44*]:* The self-attention is also known as intra-attention since all the queries, keys and values come from the same block (encoder or decoder). The self-attention layer connects all the sequence positions to each other with O(1) space complexity which is highly desirable for learning long- range dependencies in the input.
		2. Cross Attention: In encoder-decoder architectures, the outputs of the encoder blocks act as the queries to the intermediate representation of the decoder, which provides the keys and values to calculate a representation of the decoder conditioned on the encoder. This attention is called cross- attention.
		3. Full Attention: The naive implementation of calculating self-attention is known as full attention.
		4. [Sparse Attention [](#bookmark100)45]: The self-attention has a time complexity of O(n2)[, which becomes prohibitive when scaling the LLMs to large context windows. An approximation to the self-attention was proposed in [](#bookmark100)45], which greatly enhanced the capacity of GPT series LLMs to process a greater number of input tokens in a reasonable time.
		5. [Flash Attention [](#bookmark101)46]: The bottleneck for calculating the attention using GPUs lies in the memory access rather than the computational speed. Flash Attention uses the classical input tiling approach in order to process the blocks of the input in GPU on-chip SRAM rather than doing IO for every token from the High Bandwith Memory (HBM). An extension of this approach to sparse attention follows the speed gains of the full attention implementation. This trick allows even greater context-length windows in the LLMs as compared to those LLMs with sparse attention.
	4. ‌Encoding Positions
	
	The *attention* [modules do not consider the order of process- ing by design. Transformer [](#bookmark99)44[] introduced “positional encod- ings” to feed information about the position of the tokens in input sequences. Several variants of positional encoding have been proposed [](#bookmark102)47[], [](#bookmark103)48[]. Interestingly, a recent study [](#bookmark104)49] suggests that adding this information may not matter for the state-of-the-art decoder-only Transformers.
	
	
		1. Absolute: This is the most straightforward approach to adding the sequence order information by assigning a unique identifier to each position of the sequence before passing it to the attention module.
		2. Relative: In order to pass the information of the rel- ative dependencies of different tokens appearing at different locations in the sequence, a relative positional encoding is calculated by some kind of learning. Two famous types of relative encodings are:
		
		# Alibi [[](#bookmark102)
		
		47
		
		] 
		
		In this approach, a scalar bias is subtracted from the attention score calculated using two tokens which increases with the distance between the positions of the tokens. This learned approach effectively favors using recent tokens for attention.
		
		# RoPE [Keys, queries and values are all vectors in the LLMs. RoPE [](#bookmark103)
		
		48
		
		] involves the rotation of the query and key represen- tations at an angle proportional to their absolute positions of the tokens in the input sequence. This step results in a relative
		
		‌positional encoding scheme which decays with the distance where gl [is the gain parameter. RMSNorm [](#bookmark112)57] modifies al
		
		between the tokens.
	5. Activation Functions
	
	[fitting abilities of the neural networks, as proved in [](#bookmark105)50]. The
	
	The activation functions serve a crucial role in the curve-
	
	i
	
	i
	
	RMS(al)
	
	as
	
	  
	
	
	al =
	
	  
	
	
	l , n
	
	a
	
	u 1 Σ
	
	i
	
	n
	
	i gl, where RMS(al) = ,
	
	i
	
	  
	
	
	i
	
	  
	
	
	i
	
	(al )2. (5)
	
	modern activation functions used in LLMs are different from the earlier squashing functions but are critical to the success of LLMs. We discuss these activation functions in this section.
	
	
		1. [ReLU [](#bookmark106)51]: Rectified linear unit (ReLU) is defined as
		
		ReLU (x) = max(0, x) (1)
		2. [GeLU [](#bookmark107)52]: [Gaussian Error Linear Unit (GeLU) is the combination of ReLU, dropout [](#bookmark108)53[] and zoneout [](#bookmark109)54]. It is the most widely used activation function in contemporary LLM literature.
		3. [GLU variants [](#bookmark110)55*]:* [Gated Linear Unit [](#bookmark111)56] is a neural network layer that is an element-wise product (⊗) of a linear transformation and a sigmoid transformed (σ) linear projection of the input given as
		
		GLU (x, W, V, b, c) = (xW + b) ⊗ σ(xV + c), (2)
		
		where X is the input of layer and l, W, b, V and c are learned parameters.
		
		[GLU was modified in [](#bookmark110)55[] to evaluate the effect of different variations in the training and testing of transformers, resulting in better empirical results. Here are the different GLU varia- tions introduced in [](#bookmark110)55] and used in LLMs.
		
		  
		
		
		ReGLU (x, W, V, b, c) = max(0, xW + b)⊗,
		
		GEGLU (x, W, V, b, c) = GELU (xW + b) ⊗ (xV + c),
		
		SwiGLU (x, W, V, b, c, β) = Swishβ(xW + b) ⊗ (xV + c).
	6. Layer Normalization
	
	Layer normalization leads to faster convergence and is a widely used component in transformers. In this section, we provide different normalization techniques widely used in LLM literature.
	
	
		1. LayerNorm: Layer norm computes statistics over all the hidden units in a layer (l) as follows:
		
		
			1. Pre-Norm and Post-Norm: [LLMs use transformer [](#bookmark99)44[] architecture with some variations. The original implementa- tion [](#bookmark99)44] used layer normalization after the residual con- nection, commonly called post-LN, concerning the order of Multihead attention – Residual – LN[. There is another order of the normalization, referred to as pre-LN [](#bookmark113)58] due to the position of the normalization step before the self-attention layer as in LN – Multihead attention – Residual[. Pre-LN is known to provide more stability in the training [](#bookmark114)59].
			2. DeepNorm: [While pre-LN has certain benefits over post- LN training, pre-LN training has an unwanted effect on the gradients [](#bookmark114)59[]. The earlier layers have larger gradients than those at the bottom. DeepNorm [](#bookmark115)60] mitigates these adverse effects on the gradients. It is given asxlf = LN (αxlp + Glp (xlp , θlp ), (6)
		
		where α is a constant and θlp represents the parameters of layer lp. These parameters are scaled by another constant β. Both of these constants depend only on the architecture.
	7. Distributed LLM Training
	
	[This section describes distributed LLM training approaches briefly. More details are available in [](#bookmark64)9[], [](#bookmark116)61[], [](#bookmark117)62[], [](#bookmark118)63].
	
	
		1. Data Parallelism: Data parallelism replicates the model on multiple devices where data in a batch gets divided across devices. At the end of each training iteration weights are synchronized across all devices.
		2. Tensor Parallelism: Tensor parallelism shards a tensor computation across devices. It is also known as horizontal parallelism or intra-layer model parallelism.
		3. Pipeline Parallelism: Pipeline parallelism shards model layers across different devices. This is also known as vertical parallelism.
		4. Model Parallelism: A combination of tensor and pipeline
		
		1 Σ
		
		n
		
		a
		
		ul = l
		
		n i
		
		i
		
		,u 1 Σn
		
		σl = ,
		
		n
		
		i
		
		i
		
		  
		
		
		(al − ul)2, (3)
		
		parallelism is known as model parallelism.
		5. 3D Parallelism: A combination of data, tensor, and model parallelism is known as 3D parallelism.
		6. Optimizer Parallelism: Optimizer parallelism also
		
		i
		
		where n is the number of neurons in the layer l and al is the summed input of the i neuron in layer l. LayerNorm provides
		
		invariance to rescaling of the weights and re-centering of the distribution.
		
		2. RMSNorm: [[](#bookmark112)57] proposed that the invariance properties of LayerNorm are spurious, and we can achieve the same performance benefits as we get from LayerNorm by using a computationally efficient normalization technique that trades off re-centering invariance with speed. LayerNorm gives the
		
		normalized summed input to layer l as follows
		
		![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/tKuVDcsG3TdbbquUL0FoLjXpuJ8PS7dGjDLMc-Kjn1Q-Image_004.png) al − ul
		
		[known as zero redundancy optimizer [](#bookmark116)61] implements opti- mizer state partitioning, gradient partitioning, and parameter partitioning across devices to reduce memory consumption while keeping the communication costs as low as possible.
	8. Libraries[Some commonly used libraries for LLM training are: 1) Transformer [](#bookmark119)64[], 2) DeepSpeed [](#bookmark120)65[], 3) Megatraon-LM [](#bookmark117)62],

[4) JAX [](#bookmark121)66[], 5) Colossal-AI [](#bookmark122)67[], 6) BMTrain [](#bookmark118)63], 7)

[FastMoE [](#bookmark123)68[], and frameworks are 1) MindSpore [](#bookmark124)69], 2)

al =  i      gl

(4)

[PyTorch [](#bookmark125)70[], 3) Tensorflow [](#bookmark126)71[], 4) MXNet [](#bookmark127)72].

i σ i

‌I. Data PreProcessing

This section briefly summarizes data preprocessing tech- niques used in LLMs training.


	1. Quality Filtering: For better results, training data quality
	
	is essential. Some approaches to filtering data are: 1) classifier- based and 2) heuristics-based. Classifier-based approaches train a classifier on high-quality data and predict the quality of text for filtering, whereas heuristics-based employ some rules for filtering like language, metrics, statistics, and keywords.
	2. Data Deduplication: Duplicated data can affect model
	
	performance and increase data memorization; therefore, to train LLMs, data deduplication is one of the preprocessing steps. This can be performed at multiple levels, like sentences, documents, and datasets.
	3. Privacy Reduction: Most of the training data for LLMsis collected through web sources. This data contains private information; therefore, many LLMs employ heuristics-based methods to filter information such as names, addresses, and phone numbers to avoid learning the mentioned information.

J. Architectures

[Here we discuss the variants of the transformer architectures at a higher level which arise due to the difference in the application of the attention and the connection of transformer blocks. An illustration of attention patterns of these architec- tures is shown in Figure](#bookmark12) 4.


	1. Encoder Decoder: Transformers were originally de-
	
	[signed as sequence transduction models and followed other prevalent model architectures for machine translation systems. They selected encoder-decoder architecture to train human language translation tasks. This architecture is adopted by [](#bookmark66)11[], [](#bookmark70)15]. In this architectural scheme, an encoder encodes the input sequences to variable length context vectors, which are then passed to the decoder to maximize a joint objective of minimizing the gap between predicted token labels and the actual target token labels.
	2. Causal Decoder: The underlying objective of an LLM
	
	[is to predict the next token based on the input sequence. While additional information from the encoder binds the prediction strongly to the context, it is found in practice that the LLMs can learn as well absent this encoder [](#bookmark128)73] and adding the context in the decoder. Similar to the original encoder-decoder
	
	architecture’s decoder block, this decoder restricts the flow of information backward, i.e., the predicted token tk only depends on the tokens preceded by and up to tk−1. This is the most widely used variant in the state-of-the-art LLMs.
	3. Prefix Decoder: The causal masked attention is reason-able in the encoder-decoder architectures where the encoder can attend to all the tokens in the sentence from every position using self-attention. This means that the encoder can also attend to tokens tk+1 to tn in addition to the tokens from t1

to tk−1 while calculating the representation for tk . But when

[we drop the encoder and only keep the decoder, we also lose this flexibility in attention. A variation in the decoder-only architectures is by changing the mask from strictly causal to fully visible on a portion of the input sequence, as shown in Figure](#bookmark12) 4. The Prefix decoder is also known as non-causal decoder architecture.

  


![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/PkDMmWTLr-4BZl0MQ6ySS6CyN5u5kGZHzXRQ3MUV57s-Image_005.jpg)

[Fig. 4: An example of attention patterns in language models, image is taken from [](#bookmark129)74].

  


![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/QYYSgyb2Mcg4mIa07N0qGqQ09qb9FEY89OodfIg7YZY-Image_006.jpg)

[Fig. 5: An example of language model training objectives, image from [](#bookmark129)74].

  


K. Pre-Training Objectives

[This section describes LLMs pre-training objectives. For more details see the paper [](#bookmark129)74].


	1. Full Language Modeling: [An autoregressive language modeling objective where the model is asked to predict future tokens given the previous tokens, an example is shown in Figure](#bookmark13) 5.
	2. Prefix Language Modeling: [A non-causal training objec- tive, where a prefix is chosen randomly and only remaining target tokens are used to calculate the loss. An example is shown in Figure](#bookmark13) 5.
	3. Masked Language Modeling: [In this training objective, tokens or spans (a sequence of tokens) are masked randomly and the model is asked to predict masked tokens given the past and future context. An example is shown in Figure](#bookmark13) 5.
	4. Unified Language Modeling: [Unified language model- ing [](#bookmark130)75] is a combination of causal, non-causal, and masked language training objectives. Here in masked language mod- eling, the attention is not bidirectional but unidirectional, attending either left-to-right or right-to-left context.  


L. Model Adaptation

This section discusses various model adaptation techniques, where a model is pre-trained on large data and then adapted for downstream tasks.


	1. Transfer Learning: [Fine-tuning a pre-trained model with data for the downstream task is known as transfer learning. In this type of model adaptation, the model is initialized with pre-trained weights and updated according to the new data. Some of the LLMs employing this technique are [](#bookmark66)11[], [](#bookmark67)12[], [](#bookmark70)15[], [](#bookmark75)20].
	2. Parameter Efficient Learning: The parameter efficient learning fine-tunes a few parameters either by adding new parameters to the model or the existing ones.
	
	# ‌Prompt Tuning: [[](#bookmark85)
	
	30
	
	[], [](#bookmark131)76
	
	] adds trainable prompt token em- beddings as prefixes or free-style to the input token embed- dings. During fine-tuning only these embeddings parameters are trained for the downstream task while keeping the rest of the weights frozen.
	
	# Prefix Tuning: [[](#bookmark86)
	
	31
	
	] adds task-specific trainable prefix vectors to the transformer layers, where only prefix parameters are fine-tuned, and the rest of the model stays frozen. The input sequence tokens can attend prefixes acting as virtual tokens.
	
	# Adapter Tuning: [module is an encoder-decoder architecture that is placed either sequential or parallel to the attention and feed-forward layers in the transformer block [](#bookmark132)
	
	77
	
	[], [](#bookmark83)28
	
	[], [](#bookmark84)29
	
	]. Only these layers are fine-tuned, and the rest of the model is kept frozen.
	3. Instruction Finetuning: [Instruction tuning is an approach to fine-tuning pre-trained models on instruction formatted data. Instructions generally comprise multiple tasks in plain natural language, guiding the model to respond according to the prompt and the input. The training data consists of an instruction and an input-output pair. More details on formatting instruction data and its various styles are available in [](#bookmark88)33].
	4. Alignment Tuning: [Alignment techniques play a crucial role in ensuring large language models (LLMs) operate ac- cording to human intentions and values. These models can generate text and make decisions, making it vital to control their behavior and outputs to avoid undesirable outcomes. Alignment techniques aim to bridge the gap between what humans expect from LLMs and their actual behavior. A model is defined to be an “aligned” model if the model fulfils three criteria’s of helpful, honest and harmless or “HHH” [](#bookmark133)78].
	
	[The researchers investigated alignment techniques from hu- man feedback, specifically emphasizing reinforcement learn- ing from human feedback (RLHF) [](#bookmark134)79].
	
	
		1. Reward modelling: [The RLHF (Reinforcement Learning from Human Feedback) [](#bookmark134)79] encompasses reward modelling and reinforcement learning. During the reward modelling phase, the data collection approach shifts towards comparisons. A dataset is created, starting with an identical prompt, and the task is to create multiple completions using the (Supervised Fine-tuned) SFT model, which human evaluators then rank. Assuming one completion is significantly superior to the others based on the ranking, a binary classification is performed on all possible pairs of completions. This stage is known as reward modelling Training. A token in each row represents the completions generated by the SFT model. An additional special reward readout token is appended at the end of each row. The focus of supervision lies solely on a reward token within the transformer. The transformer predicts a reward value indicating the quality of each completion for a given prompt. The ground truth ranking is available for reference.
		2. Reinforcement Learning: In the previous stage, a re-
		
		ward model assigns a high score to completions, and therefore the associated token in this stage will receive reinforcement, increasing their probabilities for future occurrences. On the other hand, when the reward model assigns a low score will have lower probabilities for the future. This iterative process
		
		  
		
		
		![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/4j6q9e0UuwbaBihTGfwjnBNgUx8p8w3UCuCqMsuSSgc-Image_007.jpg)
		
		[Fig. 6: Unified text-to-text training example, source image from [](#bookmark66)11].
		
		  
		
		
		is repeated across multiple prompts and batches, leading to the development of a policy that generates excellent outputs. This process represents the RLHF (Reinforcement Learning from Human Feedback) pipeline, which culminates in the deploy- ment of a model. For example, ChatGPT is an example of an RLHF model, while models like Vicuna-13B are categorized as SFT (Supervised Fine-Tuning) models.
	5. In-context Learning: [No fine-tuning is involved in this type of model adaptation. The model is shown multiple input-output demonstration pairs to generate a desired input response. This adaptation is similar to a few-shot learning but without requiring any parameter update. More details on formatting demonstrations are available in [](#bookmark135)80[], [](#bookmark88)33].
	6. Chain-of-thought Prompting: [Chain-of-thought prompt- ing (CoT) is a special case of prompting where demonstra- tions contain reasoning information aggregated with inputs and outputs so that the model generates outcomes with rea- sonings. Some examples in literature train LLMs with CoT reasoning, whereas other utilizes LLMs’ CoT abilities without fine-tuning. More details on designing prompts are available in [](#bookmark136)81[], [](#bookmark88)33].
3. ‌LARGE LANGUAGE MODELS

  


This section reviews LLMs, briefly describing their architec- tures, training objectives, pipelines, datasets, and fine-tuning details.

  



	1. Pre-Trained Models
	
	
		1. General Purpose:
		
		
			1. [T5 [](#bookmark66)11]: [An encoder-decoder model trained on the Colossal Clean Crwal Corpus (C4) dataset with a unified text- to-text training for all NLP problems, shown in Figure](#bookmark15) 6[. The model differs from the traditional transformer model [](#bookmark99)44[]. These changes include no bias in layer normalization, using relative positional embedding, and placing layer normalization outside the residual path. The masked language modeling is used as a pre-training objective where spans (consecutive tokens) were replaced with a single mask instead of separate masks for each token. This type of masking speeds up the training as it produces shorter sequences. After pre-training, the model is fine-tuned using adapter layers [](#bookmark132)77] for down- stream tasks.
			
			  
			
			
			![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/2gWDtZX7qB2BOf_O0s-QBaN-v5o3v6I2AJsA065aFfU-Image_008.jpg)
			
			  
			
			
			[Fig. 7: The image is the article of [](#bookmark139)84], showing an example of PanGu-α architecture.‌
			2. [GPT-3 [](#bookmark63)8]: [The architecture of GPT-3 is mostly the same as GPT-2 [](#bookmark137)82[] but with dense and sparse attention in transformer layers similar to the Sparse Transformer [](#bookmark100)45[]. The model is trained on data taken from CommonCrawl, Web- text dataset, books corpora, and English-language Wikipedia. Large models can train on larger batch sizes with a lower learning rate; in order to decide the batch size during training, GPT-3 uses the gradient noise scale as in [](#bookmark138)83]. Overall, GPT-3 increases model parameters to 175B showing that the performance of large language models improves with the scale and is competitive with the fine-tuned models.
			3. [mT5 [](#bookmark67)12]: [A multilingual T5 model [](#bookmark66)11] trained
			
			on the mC4 dataset with 101 languages. The dataset is extracted from the public common crawl scrape. The model uses GeGLU activation and trains with a vocab size of 250,000 to cover multiple languages. To avoid over-fitting or under- fitting for a language, mT5 employs a data sampling procedure to select samples from all languages. The paper suggests using a small amount of pre-training datasets, including all languages when fine-tuning for a task using English language data. This allows the model to generate non-English outputs.
			4. PanGu-α [[](#bookmark139)84]: An autoregressive model trained on
			
			[1.1TB Chinese data collected from Common Crawl, e-Books, encyclopedia, etc. Additional to the standard transformer model, it has a query layer after stacked transformer layers, example shown in Figure](#bookmark17) 7[. The purpose of the query layer is to predict the next token. Its structure is similar to the transformer layer but with an additional embedding for the next position in the attention mechanism, given in Eq.](#bookmark19) 7. The model is trained using MindSpore with five-dimensional parallelism, i.e., data parallelism, op-level model parallelism, pipeline model parallelism, optimizer parallelism, and rema-
			
			terialization.
			
			[sentencepiece tokenizer. The models are trained with knowl- edge inheritance, starting with only the Chinese language in the first stage and then adding English and Chinese data. This trained model gets duplicated multiple times to initialize the 198B MoE model. Moreover, to use the model for downstream tasks, CPM-2 experimented with both complete fine-tuning and prompt fine-tuning as in [](#bookmark82)27] where only prompt-related parameters are updated by inserting prompts at various posi- tions, front, middle, and back. CPM-2 also proposes INFMOE, a memory-efficient framework with a strategy to dynamically offload parameters to the CPU for inference at a 100B scale. It overlaps data movement with inference computation for lower inference time.
			
			
				
					1. [ERNIE 3.0 [](#bookmark141)86]: ERNIE 3.0 takes inspiration from
					
					[multi-task learning to build a modular architecture using Transformer-XL [](#bookmark142)87] as the backbone. The universal repre- sentation module is shared by all the tasks, which serve as the basic block for task-specific representation modules, which are all trained jointly for natural language understanding, natural language generation, and knowledge extraction. This LLM is primarily focused on the Chinese language, claims to train on the largest Chinese text corpora for LLM training, and achieved state-of-the-art in 54 Chinese NLP tasks.
					2. [Jurassic-1 [](#bookmark143)88]: A pair of auto-regressive language
					
					[models, including a 7B-parameter J1-Large model and a 178B- parameter J1-Jumbo model. The Jurassic-1 models are mainly structured on the Transformer decoder module [](#bookmark99)44[], while the architecture modifications proposed by GPT-2 [](#bookmark137)82[] are also incorporated. In particular, the training vocabulary items of Jurassic-1 comprise word pieces, complete words, and multi-word expressions without any word boundaries, where possible out-of-vocabulary instances are interpreted as Uni- code bytes. In practice, data collected from publicly available resources are formed in the GPT-3’s data structure to train the Jurassic-1 models following the conventional self-supervised auto-regressive training objective. Compared to the GPT-3 counterparts, the Jurassic-1 models apply a more balanced depth-to-width self-attention architecture [](#bookmark144)89] and an improved tokenizer for a faster prediction based on broader resources, achieving a comparable performance in zero-shot learning tasks and a superior performance in few-shot learning tasks given the ability to feed more examples as a prompt.
					3. [HyperCLOVA [](#bookmark145)90]: The architecture is the same as
					
					[that of GPT3 [](#bookmark63)8] with morphene aware byte level encoding tokenization step. A large Korean-centric corpus gathered from various sources (see table for details) is trained using Megatron LM. Prompt-based tuning is also applied to enhance perfor- mance on downstream tasks. The main objective of training this model is to see how the non-English language model fares compared to universally found English-based LMs.
					
					‌a = pnWq Wk THT
					
					(7)
					4. [Yuan 1.0 [](#bookmark146)91]: A large singleton language model
					
					h h L
			5. [CPM-2 [](#bookmark68)13]: [Cost-efficient Pre-trained language Models (CPM-2) pre-trains bilingual (English and Chinese) 11B and 198B mixture-of-experts (MoE) models on the Wu- DaoCorpus [](#bookmark140)85] dataset. It has an encoder-decoder architecture with a bidirectional encoder and a unidirectional decoder. The tokenization process removes “\_” white space tokens in the
			
			[with 245B parameters. The Yuan 1.0 is structured as a Trans- former [](#bookmark99)44]. A Chinese corpus with 5TB of high-quality text is created to train Yuan 1.0 model, where the raw data is collected from Internet resources. A Massive Data Filtering System (MDFS) built on Spark is developed to process the raw data via coarse and fine filtering techniques. To speed up the training of Yuan 1.0 with the aim of saving energy expenses and
			
			‌carbon emissions, a collaborative design of model architecture and large-scale distributed training is introduced. In practice, the Yuan 1.0 model performs well on text classification, Winograd Schema, natural language inference, and reading comprehension tasks.
			
			
				
					1. [Gopher [](#bookmark147)92]: It is the largest of six causal decoder
					
					[LLMs trained on the subsets of MassiveWeb, Books, C4, News, GitHub, and Wikipedia samples from high-quality curated MassiveText. The model is a modified version of Transformer architecture used in [](#bookmark137)82]. The Gopher family of models ranges from 44M to 280B parameters in size to study the effect of *scale* [on the LLMs performance. The 280B model beats GPT-3 [](#bookmark63)8[], Jurrasic-1 [](#bookmark143)88[], MT-NLG [](#bookmark76)21], and others on 81% of the evaluated tasks.
					2. [ERNIE 3.0 TITAN [](#bookmark148)93]: ERNIE 3.0 Titan extends
					
					ERNIE 3.0 by training a larger model with 26x the number of parameters of the latter. This bigger model outperformed other state-of-the-art models in 68 NLP tasks. LLMs produce text with incorrect facts. In order to have control of the generated text with factual consistency, ERNIE 3.0 Titan adds another task, *Credible and Controllable Generations*, to its multi- task learning setup. It introduces additional self-supervised adversarial and controllable language modeling losses to the pre-training step, which enables ERNIE 3.0 Titan to beat other LLMs in their manually selected Factual QA task set evaluations.
					3. [GPT-NeoX-20B [](#bookmark149)94]: An auto-regressive model
					
					[that largely follows GPT-3 with a few deviations in architec- ture design, trained on the Pile dataset without any data dedu- plication. GPT-NeoX has parallel attention and feed-forward layers in a transformer block, given in Eq.](#bookmark21) 8[, that increases throughput by 15%. It uses rotary positional embedding [](#bookmark103)48[], applying it to only 25% of embedding vector dimension as in [](#bookmark150)95[]. This reduces the computation without performance degradation. Opposite to GPT-3, which uses dense and sparse layers, GPT-NeoX-20B uses only dense layers. The hyperpa- rameter tuning at this scale is difficult; therefore, the model chooses hyperparameters from the method [](#bookmark63)8] and interpolates values between 13B and 175B models for the 20B model. The model training is distributed among GPUs using both tensor and pipeline parallelism.
					
					‌x + Attn(LN1(x)) + FF (LN2(x)) (8)
					4. [OPT [](#bookmark65)10]: [It is a clone of GPT-3, developed with the intention to open-source a model that replicates GPT-3 performance. The model was trained using RoBERTa, The Pile, and PushShift.io Reddit datasets. Training of OPT employs dynamic loss scaling [](#bookmark151)96] and restarts from an earlier checkpoint with a lower learning rate whenever loss divergence is observed. Overall, the performance of OPT-175B models is comparable to the GPT3-175B model.
					5. [BLOOM [](#bookmark64)9]: A causal decoder model trained on
					
					[ROOTS corpus with the aim of open-sourcing an LLM. The architecture of BLOOM is shown in Figure](#bookmark23) 8[, with differences like ALiBi positional embedding, an additional normalization layer after the embedding layer as suggested by the bitsand- bytes](#bookmark22)1 library. These changes stabilize training with improved
					
					‌1https://github.com/TimDettmers/bitsandbytes
					
					  
					
					
					![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/YHsQN3kWAlQhja6n_kleFFawjXm-kyJz8dTpCjkeeyM-Image_009.jpg)
					
					[Fig. 8: The BLOOM architecture example sourced from [](#bookmark64)9]. downstream performance.
					6. [GLaM [](#bookmark152)97*]:* [Generalist Language Model (GLaM) represents a family of language models using a sparsely ac- tivated mixture-of-experts (MoE) structure [](#bookmark153)98[], [](#bookmark154)99[]. Specif- ically, the architecture of GLaM is derived from a Decoder- only Transformer [](#bookmark99)44]. To gain more model capacity while reducing computation, the experts are sparsely activated where only the best two experts are used to process each input token. The largest GLaM model, GLaM (64B/64E), is about 7× [larger than GPT-3 [](#bookmark63)8], while only a part of the parameters is activated per input token. To effectively compare with GPT-3, the evaluation of GLaM follows the similar zero, one, and few- shot learning protocols as in GPT-3. Specifically, the largest GLaM (64B/64E) model achieves better overall results while consuming only one-third of GPT-3’s training energy.
					7. [MT-NLG [](#bookmark76)21*]:* [A causal decoder transformer trained on two snapshots of Common Crawl along with some other datasets given in table](#bookmark50) VIII. MT-NLG uses 8-way tensor slicing by Megatron for memory efficiency and 35-way pipeline parallelism using DeepSpeed for compute efficiency to train a 530B model, roughly 3× GPT-3 model parameters. This model beats GPT-3 on a number of evaluations.
					8. [Chinchilla [](#bookmark155)100]: [A causal decoder trained on the same dataset as the Gopher [](#bookmark147)92[] but with a little different data sampling distribution (sampled from MassiveText). The model architecture is similar to the one used for Gopher, with the exception of AdamW optimizer instead of Adam. Chinchilla identifies the relationship that model size should be doubled for every doubling of training tokens. Over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens are trained to get the estimates for compute-optimal training under a given budget. The authors train a 70B model with the same compute budget as Gopher (280B) but with 4 times more data. It outperforms Gopher [](#bookmark147)92[], GPT-3 [](#bookmark63)8], and others on various downstream tasks, after fine-tuning.
					9. [AlexaTM [](#bookmark156)101]: [The first multilingual sequence- to-sequence model (20B parameter) is capable of in-context learning. The pre-training data is collected from Wikipedia and mC4 dataset [](#bookmark67)12] covering 12 programming languages. To enable the AlexaTM 20B model to perform on both spoken and written cases, all data is converted into spoken format via a written-to-spoken formatter. In addition to pre-training on the denoising task, an extra Causal Language Modeling (CLM)
					
					‌task is performed for 20% of the time to help the model with efficient in-context learning. In practice, the model is asked to continue the input instead of denoising the input once a special CLM token is attached to the beginning of the input.
					10. PaLM: [A causal decoder model trained on a dataset of 780B tokens collected from webpages, books, Wikipedia, news, and others, given in Table](#bookmark50) VIII[. The PaLM has parallel attention and feed-forward layers similar to Eq.](#bookmark21) 8, speeding up training 15 times faster. Additional changes to the conven- tional transformer model include SwiGLU activation, RoPE embeddings, multi-query attention that saves computation cost during decoding, and shared input-output embeddings. During training, loss spiking was observed, and to fix it, model training was restarted from a 100 steps earlier checkpoint by skipping 200-500 batches around the spike. Moreover, the model was found to memorize around 2.4% of the training data at the 540B model scale, whereas this number was lower for smaller models.
					11. [U-PaLM [](#bookmark75)20]: [This method trains PaLM for 0.1% additional compute with UL2 (also named as UL2Restore) objective [](#bookmark70)15] using the same dataset and outperforms baseline significantly on various NLP tasks, including zero-shot, few- shot, commonsense reasoning, CoT, etc. Training with UL2R involves converting a causal decoder PaLM to a non-causal decoder PaLM and employing 50% sequential denoising, 25% regular denoising, and 25% extreme denoising loss functions.
					12. [UL2 [](#bookmark70)15]: An encoder-decoder architecture trained
					
					using a mixture of denoisers (MoD) objectives. Denoisers include 1) R-Denoiser: a regular span masking, 2) S-Denoiser: which corrupts consecutive tokens of a large sequence and
					
					3) X-Denoiser: which corrupts a large number of tokens randomly. During pre-training, UL2 includes a denoiser token from R, S, X to represent a denoising setup. It helps improve fine-tuning performance for downstream tasks that bind the task to one of the upstream training modes. This MoD style of training outperforms the T5 model on many benchmarks.
					13. [GLM-130B [](#bookmark157)102]: [GLM-130B is a bilingual (En- glish and Chinese) model trained using an auto-regressive mask infilling pre-training objective similar to the GLM [](#bookmark158)103]. This training style makes the model bidirectional as compared to GPT-3, which is unidirectional. Opposite to the GLM, the training of GLM-130B includes a small amount of multi-task instruction pre-training data (5% of the total data) along with the self-supervised mask infilling. To stabilize the training, it applies embedding layer gradient shrink.
					14. [LLaMA [](#bookmark159)104]: [A set of foundation language models varying from 7B to 65B parameters. The overall architec- ture of LLaMA follows the Transformer [](#bookmark99)44[], while a few subsequently proposed improvements of normalization [](#bookmark112)57[], activation [](#bookmark110)55[], and positional embedding [](#bookmark103)48[] operations are incorporated for better performances. About 67% of LLaMA’s pre-training data is collected from English CommonCrawl following the CCNet method [](#bookmark160)105]. LLaMA and the asso- ciated variants are widely used for parameter-efficient tuning, especially for instruction following tasks.
					15. PanGu-Σ [[](#bookmark161)106]: An autoregressive model with parameters copied from PanGu-α and extended to a trillion scale with Random Routed Experts (RRE), the architectural[diagram is shown in Figure](#bookmark28) 9. RRE is similar to the MoE architecture, with distinctions at the second level, where tokens are randomly routed to experts in a domain instead of using a learnable gating method. The model has bottom layers densely activated and shared across all domains, whereas top layers are sparsely activated according to the domain. This training style allows extracting task-specific models and reduces catastrophic forgetting effects in case of continual learning.
		2. Coding:
		
		
			1. [CodeGen [](#bookmark162)107]: [CodeGen has similar architecture to the PaLM [](#bookmark69)14], i.e., parallel attention, MLP layers, and RoPE embeddings. The model is trained on both natural language and programming language data sequentially (trained on the first dataset, then the second and so on) on the following datasets 1) PILE, 2) BIGQUERY and 3) BIGPYTHON. Code- Gen proposed a multi-step approach to synthesizing code. The purpose is to simplify the generation of long sequences where the previous prompt and generated code are given as input with the next prompt to generate the next code sequence. CodeGen opensource a Multi-Turn Programming Benchmark (MTPB) to evaluate multi-step program synthesis.
			2. [Codex [](#bookmark163)108]: [This LLM is trained on a subset of public Python Github repositories to generate code from docstrings. Computer programming is an iterative process where the programs are often debugged and updated before fulfilling the requirements. Similarly to this, Codex generates 100 versions of a program by repetitive sampling for a given description, which produces a working solution for 77.5% of the problems passing unit tests. Its powerful version powers Github Copilot](#bookmark25)2.
			3. [AlphaCode [](#bookmark164)109]: [A set of large language models designed for competition-level code generation tasks. Ba- sically, the AlphaCode models follow an encoder-decoder transformer architecture [](#bookmark99)44[] ranging from 300M to 41B parameters. Moreover, the multi-query attention [](#bookmark165)110[] is ap- plied to reduce memory and cache costs. Since competitive programming problems highly require deep reasoning and an understanding of complex natural language algorithms, the AlphaCode models are pre-trained on filtered GitHub code in popular languages and then fine-tuned on a new competitive programming dataset named CodeContests. Particularly, the CodeContests dataset mainly contains problems, solutions, and test cases collected from the Codeforces platform](#bookmark26)3[. In practice, standard language modeling objectives are used for the pre-training on GitHub code data, while GOLD [](#bookmark166)111[] with tempering [](#bookmark167)112] serve as the training objective for the fine- tuning on CodeContests data. To evaluate the performance of AlphaCode, simulated programming competitions are hosted on the Codeforces platform: overall, AlphaCode ranks at the top 54.3% among over 5000 competitors, where its Codeforces rating is within the top 28% of recently participated users.
			4. [CodeT5+ [](#bookmark168)113]: [CodeT5+ is based on CodeT5 [](#bookmark169)114], with shallow encoder and deep decoder, trained in multiple stages initially unimodal data (code) and later bimodal data (text-code pairs). Each training stage has
			
			‌2https://github.com/features/copilot 3https://codeforces.com/‌
			
			‌different training objectives and activates different model blocks encoder, decoder, or both according to the task. The unimodal pre-training includes span denoising and CLM objectives, whereas bimodal pre-training objectives contain contrastive learning, matching, and CLM for text-code pairs. CodeT5+ adds special tokens with the text to enable task modes, for example, [CLS] for contrastive loss, [Match] for text-code matching, etc.
			5. [StarCoder [](#bookmark170)115]: A decoder-only model with San- taCoder architecture, employing Flash attention to scale up the context length to 8k. The StarCoder trains an encoder to filter names, emails, and other personal data from the training data. Its fine-tuned variant outperforms PaLM, LLaMA, and LAMDA on HumanEval and MBPP benchmarks.
		3. Scientific Knowledge:
		
		
			1. [Galactica [](#bookmark171)116]: A large curated corpus of human scientific knowledge with 48 million papers, textbooks, lecture notes, millions of compounds and proteins, scientific websites, encyclopedias, and more are trained using metaseq library3,
			
			[which is built on PyTorch and fairscale [](#bookmark172)117]. The model wraps reasoning datasets with < work > token to provide step-by-step reasoning context to the model, which has been shown to improve the performance on reasoning tasks.
		4. Dialog:
		
		
			1. [LaMDA [](#bookmark173)118]: [A family of Transformer-based neu- ral language models for dialog ranging from 2B to 137B parameters. The model architecture of LaMDA follows a decoder-only Transformer [](#bookmark99)44] language model. LaMDA is pre-trained on public dialog data, public dialog utterances, and public web documents. Particularly, more than 90% of the pre-training data is in English. Particularly, LaMDA aims to produce responses that exhibit high levels of quality, safety, and groundedness. To achieve this, discriminative and gener- ative fine-tuning techniques are incorporated to enhance the model’s safety and quality aspects. As a result, the LaMDA models can be utilized as a general language model performing various tasks.
			2. [Sparrow [](#bookmark174)119]: An information-seeking dialogue
			
			[agent is trained to gain more helpfulness and correctness with less harm. Two additions are proposed to help human raters judge agent behavior: the first is the specific natural language rules that need raters to rate separately, and the second is to make the agent show proof from sources that support factual claims when collecting opinions about the model’s statements. The architecture of the Sparrow models is based on Dialogue Prompted Chinchila 70B [](#bookmark155)100[]. Human data is collected for rule violations and per-turn response preferences, which mainly aims to train preference reward models (preference RMs) and a rule reward model (rule RM). In practice, reinforcement learning with advantage actor-critic (A2C) [](#bookmark175)120] is used to train the initialized Chinchilla model; the rule RM estimated rule violation rate and the prefer- ence RMs estimated per-turn response preferences are jointly optimized. Given experimental data, Sparrow’s evidence can support the sampled response for factual questions 78% of the time. Moreover, Sparrow is highly resistant to human adversarial probing since it only violates the defined rules 8% of the time when probed.
			
			  
			
			
			![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/tKo0-ambb304HpujWj4Gj_pst0LmH3Pi5oA5jwTp-Zk-Image_010.jpg)
			
			Σ
			
			[Fig. 9: This example illustrates the PanGu- architecture, as depicted in the image sourced from [](#bookmark161)106].
		5. Finance:
		
		
			1. [BloombergGPT [](#bookmark176)121]: [A non-causal decoder model trained using both financial ("FINPILE" from the Bloomberg archive) and general-purpose datasets. The model’s architec- ture is similar to the BLOOM [](#bookmark64)9[] and OPT [](#bookmark65)10[]. It allocates 50B parameters to different blocks of the model using the approach [](#bookmark177)122]. For effective training, BloombergGPT packs
			
			documents together with < |endoftext| > to use maximum
			
			sequence length, use warmup batch size starting from 1024 to 2048, and manually reduces the learning rate multiple times during the training.
			2. [Xuan Yuan 2.0 [](#bookmark178)123]: [A Chinese financial chat model with BLOOM’s [](#bookmark64)9] architecture trained on a combina- tion of general purpose, financial, general purpose instructions, and financial institutions datasets. Xuan Yuan 2.0 combined the pre-training and fine-tuning stages to avoid catastrophic forgetting.
	2. Fine-Tuned Models
	
	
		1. Instruction-Tuning with Manually Created Datasets:
		
		
			1. [T0 [](#bookmark77)22]: [Similar to Flan [](#bookmark80)25[], T0 fine-tunes the LM- adapted T5 model [](#bookmark82)27] with multi-task instruction prompts. To train the model, T0 designs various prompt templates to convert different datasets into prompts. The model trained with explicit multi-task prompting improves zero-shot performance, outperforming models 6 to 16 times larger in size.
			2. [WebGPT [](#bookmark181)126]: [A set of fine-tuned GPT-3 [](#bookmark63)8] mod-
			
			[els that can answer long-form questions in a text-based web- browsing environment. During browsing, the models must collect references to support their answers in order to exploit easier human evaluation. In addition to the Q&A data in the ELI5 dataset [](#bookmark184)129], two more types of data, *demonstrations* of humans and *comparisons* between two model-generated answers, are collected for training. Using human labelers’ feedback on whether the retrieved information is useful to answer the given inputs, the data is tested with four usages: behavior cloning, reward modeling, reinforcement learning, and rejection sampling. Practically, the combination of be- havior cloning and rejection sampling contributes to the best-
			
			‌TABLE I: Noteworthy findings and insights from *pre-trained* Large Language Model.‌
			
			  
			
			
			Models Findings & Insights
			
			
				* Encoder and decoder with shared parameters perform equivalently when parameters are not shared
				
				T5 • Fine-tuning model layers (adapter layers) work better than the conventional way of training on only classification layers
				
				GPT-3 • Few-shot performance of LLMs is better than the zero-shot, suggesting that LLMs are meta-learners
				* Large multi-lingual models perform equivalently to single language models on downstream tasks. However, smaller multi-
				
				mT5 lingual models perform worse
				
				PanGu-α • LLMs are good at a few shot capabilities
				* Prompt fine-tuning requires updating very few parameters while achieving performance comparable to full model fine-tuning
				* Prompt fine-tuning takes more time to converge as compared to full model fine-tuning
				* Inserting prompt tokens in-between sentences can allow the model to understand relations between sentences and long
				
				CPM-2
				
				  
				
				
				Codex
				
				  
				
				
				ERNIE 3.0
				
				  
				
				
				Jurassic-1
				
				HyperCLOVA Yuan 1.0
				
				sequences
				
				
					+ In an analysis, CPM-2 finds that prompts work as a provider (additional context) and aggregator (aggregate information with the input text) for the model
					+ This LLM focuses on code evaluations and introduces a novel way of selecting the best code samples.
					+ The results indicate it is possible to accurately select code samples using heuristic ranking in lieu of a detailed evaluation of each sample, which may not be feasible or feasible in some situations.
					+ ERNIE 3.0 shows that a modular LLM architecture with a universal representation module and task-specific representation module helps in finetuning phase.
					+ Optimizing the parameters of a task-specific representation network during the fine-tuning phase is an efficient way to take advantage of the powerful pretrained model.
					+ The performance of an LLM is highly related to the network size.
					+ To improve runtime performance, more operations can be performed in parallel (width) rather than sequentially (depth).
					+ To efficiently represent and fit more text in the same context length, the model uses a larger vocabulary to train a SentencePiece tokenizer without restricting it to word boundaries. This tokenizer improvement can further benefit few-shot learning tasks.
					+ By employing prompt-based tuning, the performances of models can be improved, often surpassing those of state-of-the-art models when the backward gradients of inputs are accessible.
					+ The model architecture that excels in pre-training and fine-tuning cases may exhibit contrasting behavior in zero-shot and few-shot learning.
					
					  
					
					
					Gopher • Relative encodings enable models to be evaluated for longer sequences than those on which it was trained.
					
					
						- This LLM builds on top of ERNIE 3.0 and add a self-supervised adversarial loss to distinguish whether a text is generated
						
						ERNIE 3.0 Titan
						
						  
						
						
						GPT-NeoX-20B
						
						  
						
						
						OPT
						
						or the original one.
					+ This distinction ability between real and generate text improves the LLM’s performance as compared to ERNIE 3.0.
					+ Parallel attention + FF layers speed-up training 15% with the same performance as with cascaded layers
					+ [Initializing feed-forward output layers before residuals with scheme in [](#bookmark179)124] avoids activations from growing with increasing depth and width
					+ Training on Pile outperforms GPT-3 on five-shot
					+ Restart training from an earlier checkpoint with a lower learning rate if loss diverges
					+ Model is prone to generate repetitive text and stuck in a loop
					
					  
					
					
					BLOOM • None
					
					
						- Galactica’s performance has continued to improve across validation set, in-domain, and out-of-domain benchmarks, even with multiple repetitions of the corpus, which is superior to existing research on LLMs.
						
						Galactica
						
						  
						
						
						GLaM
					+ A working memory token approach can achieve strong performance over existing methods on mathematical MMLU and MATH benchmarks. It sets a new state-of-the-art on several downstream tasks such as PubMedQA (77.6%) and MedMCQA dev (52.9%).
					+ The feed-forward component of each Transformer layer can be replaced with a mixture-of-experts (MoE) module consisting of a set of independent feed-forward networks (*i.e.*, the ‘experts’). By sparsely activating these experts, the model capacity can be maintained while much computation is saved.
					+ By leveraging sparsity, we can make significant strides toward developing high-quality NLP models while simultaneously reducing energy consumption. Consequently, MoE emerges as a robust candidate for future scaling endeavors.
					+ The model trained on filtered data shows consistently better performances on both NLG and NLU tasks, where the effect of filtering is more significant on the former tasks.
					+ Filtered pretraining corpora plays a crucial role in the generation capability of LLMs, especially for the downstream tasks.
					+ The scaling of GLaM MoE models can be achieved by increasing the size or number of experts in the MoE layer. Given a fixed budget of computation, more experts contribute to better predictions.
					
					  
					
					
					LaMDA • The model can be fine-tuned to learn to call different external information resources and tools. MT-NLG • None.
					
					
						- For higher effectiveness and efficiency, a transformer model can be asymmetrically constructed with a shallower encoder and a deeper decoder.
						- To achieve better performances, it is necessary to employ strategies such as massively scaling up sampling, followed by the
						
						AlphaCode
						
						filtering and clustering of samples into a compact set.
					+ The utilization of novel sampling-efficient transformer architectures designed to facilitate large-scale sampling is crucial.
					+ Simplifying problem descriptions can effectively improve the model’s performance.
					
					  
					
					
					Table Continued on Next Page
					
					  
					
					
					‌Models Findings & Insights
					
					  
					
					
					Chinchilla
					
					  
					
					
					PaLM
					
					  
					
					
					AlexaTM
					
					  
					
					
					Sparrow
					
					  
					
					
					U-PaLM UL2
					+ The experiments that culminated in the development of Chinchilla determined that for optimal computation during training,
					
					the model size and the number of training tokens should be scaled proportionately: for each doubling of the model size, the number of training tokens should be doubled as well.
					+ English-centric models produce better translations when translating to English as compared to non-English
					+ Generalized models can have equivalent performance for language translation to specialized small models
					+ Larger models have a higher percentage of training data memorization
					+ Performance has not yet saturated even at 540B scale, which means larger models are likely to perform better
					+ Compared to commonly used Decoder-only Transformer models, seq2seq architecture is more suitable for training generative LLMs given stronger bidirectional attention to the context.
					+ An extra Causal Language Modeling (CLM) task can be added to benefit the model with a more efficient in-context learning, especially for few-shot learning tasks.
					+ The key to training powerful seq2seq-based LLMs lies in mixed pre-training, rather than additional multitask training.
					+ Placing layernorms at the beginning of each transformer layer can improve the training stability of large models.
					+ Reinforcement learning from multi-objective human feedback can be leveraged to train the models, in order to maximize preference rates and minimize rule violations.
					+ The judgments of labelers and the alignments with defined rules can help the model generate better responses.
					+ Good dialogue goals can be broken down into detailed natural language rules for the agent and the raters.
					+ Constructing useful and reliable agents from generative models requires a combination of width and depth: the width aspect enables addressing the complexities of goals and topics; while the depth aspect ensures accurate handling of them.
					+ The combination of reinforcement learning (RL) with reranking yields optimal performance in terms of preference win rates and resilience against adversarial probing.
					+ Training with a mixture of denoisers outperforms PaLM when trained further for a few more FLOPs
					+ Training with a mixture of denoisers improves the infilling ability and open-ended text generation diversity
					+ Mode switching training enables better performance on downstream tasks
					+ CoT prompting outperforms standard prompting for UL2
					
					  
					
					
					GLM-130B • Pre-training data with a small proportion of multi-task instruction data improves the overall model performance CodeGen • Multi-step prompting for code synthesis leads to a better user intent understanding and code generation
					
					
						- LLaMA is open-source and can be fine-tuned or continually pre-trained to develop new models or instruction-based tools.
						- A few optimizations are proposed to improve the training efficiency of LLaMA, such as efficient implementation of multi-head self-attention and a reduced amount of activations during back-propagation.
						
						LLaMA
						
						  
						
						
						PanGu-Σ
					+ Training exclusively on public data can also achieve state-of-the-art performance.
					+ A constant performance improvement is gained when scaling the model.
					+ Smaller models can also realize good performances using more training data and time.
					+ Sparse models provide the benefits of large models at a lower computation cost
					+ Randomly Routed Experts reduces catastrophic forgetting effects which in turn is essential for continual learning
					+ Randomly Routed Experts allow extracting a domain-specific sub-model in deployment which is cost-efficient while maintaining a performance similar to the original
					
					  
					
					
					BloombergGPT • Pre-training with general-purpose and task-specific data improves task performance without hurting other model capabilities XuanYuan 2.0 • Combining pre-training and fine-tuning stages in single training avoids catastrophic forgetting
					
					
						- Causal LM is crucial for a model’s generation capability in encoder-decoder architectures
						
						CodeT5+ • Multiple training objectives like span corruption, Causal LM, matching, etc complement each other for better performance
						
						StarCoder • HHH prompt by Anthropic allows the model to follow instructions without fine-tuning
						
						  
						
						
						[performing model containing 175B parameters. To evaluate the performance of the WebGPT model, the model’s answers are compared with the human demonstrators’ written ones, the highest-voted answers in ELI5 [](#bookmark184)129[], and the adversarial short- form questions and answers in the TruthfulQA [](#bookmark185)130] dataset.
			3. [Tk-INSTRUCT [](#bookmark81)26]: Tk-INSTRUCT instruction fine-tunes T5 model on self-proposed SUPER- NATURALINSTRUCTIONS dataset of 1616 different NLP tasks. To analyze the generalization capabilities of Tk-INSTRUCT, the model is evaluated on unseen tasks with a few examples as ground-truth in-context instructions. The model outperforms GPT-3 and Instruct-GPT by large margins, although it is smaller in size 11B, opposite to 175B.
			4. [mT0 and BLOOMZ [](#bookmark78)23]: This method fine-tunes BLOOM and T0 using a multilingual multi-task prompt dataset. It creates a new dataset named xP3, adding 46 different language datasets with new tasks not present previously in P3.
			
			Training with this dataset improves zero-shot generalization for both English and non-English. This also leads to better generalization on held-out tasks.
			5. [OPT-IML [](#bookmark79)24*]:* [An instruction-tuned OPT model, trained on instruction meta-learning benchmark of 2000 NLP tasks that is a combination of 8 meta-datasets including, Super-NaturalInstructions, PromptSource, FLAN, and others as given in Table](#bookmark50) VIII. For computational efficiency, OPT- IML utilizes the maximum sequence length of 2048 tokens by packing multiple instances together, separated by the < eos > token during training. It employs a masking mechanism to separate instances in a sequence to avoid attending tokens from different instances. Overall, OPT-IML outperforms baseline model OPT with instruction-finetuning on zero and few-shot generalization abilities.
			6. [Flan [](#bookmark80)25]: Fine-tuning language models (Flan), fine- tunes T5, PaLM, and UPaLM with 1836 instruction tasks
			
			‌TABLE II: Key insights and findings from the study of *instruction-tuned* Large Language Models.‌
			
			  
			
			
			Models Findings & Insights
			
			T0
			
			  
			
			
			WebGPT
			
			  
			
			
			Tk-INSTRUCT
			
			  
			
			
			mT0 and BLOOMZ
			
			  
			
			
			OPT-IML
			
			  
			
			
			Flan
			
			
				* Multi-task prompting enables zero-shot generalization and outperforms baselines
				* Even a single prompt per dataset task is enough to improve performance
				* The answer quality of LLMs can be further improved with human feedback.
				* To aid the model in effectively filtering and utilizing relevant information, human labelers play a crucial role in answering questions regarding the usefulness of the retrieved documents.
				* Interacting a fine-tuned language model with a text-based web-browsing environment can improve end-to-end retrieval and synthesis via imitation learning and reinforcement learning.
				* Generating answers with references can make labelers easily judge the factual accuracy of answers.
				* Instruction tuning leads to a stronger generalization of unseen tasks
				* More tasks improve generalization whereas only increasing task instances does not help
				* Supervised trained models are better than generalized models
				* Models pre-trained with instructions and examples perform well for different types of inputs
				* Instruction tuning enables zero-shot generalization to the tasks never seen before
				* Multi-lingual training leads to even better zero-shot generalization for both English and non-English
				* Training on machine-translated prompts improves performance for held-out tasks with non-English prompts
				* English only fine-tuning on multilingual pre-trained language model is enough to generalize to other pre-trained language tasks
				* Task size sampling to create a batch with most of the task examples is important for better performance
				* Only example proportional sampling is not enough, training datasets/benchmarks should also be proportional for better generalization/performance
				* Fully held-out and partially supervised tasks performance improves by scaling tasks or categories whereas fully supervised tasks have no effect
				* Including small amounts i.e. 5% of pretraining data during fine-tuning is effective
				* Only 1% reasoning data improves the performance, adding more deteriorates performance
				* Adding dialogue data makes the performance worse
				* Finetuning with CoT improves performance on held-out tasks
				* Fine-tuning along with CoT data improves reasoning abilities
				* CoT tuning improves zero-shot reasoning
				* Performance improves with more tasks
				* Instruction fine-tuning improves usability which otherwise is challenging for pre-trained models
				* Improving the model’s performance with instruction tuning is compute efficient
				* Multitask prompting enables zero-shot generalization abilities in LLM  
			
			
			WizardCoder • Fine-tuning with re-written instruction-tuning data into a complex set improves the performance significantly
			
			  
			
			
			  
			
			
			![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/SaWyWaMs42dGhRZOE7ZiL_9Mtx-6gIn3ko2vGuf9pMI-Image_011.jpg)
			
			[Fig. 10: An example image shows an instance of the Flan training paradigm, taken from [](#bookmark80)25].
			
			  
			
			
			[taken from Muffin (80 tasks), T0-SF (193 tasks), NIV2 (1554 tasks), and CoT (taken from nine datasets), as shown in Figure](#bookmark34) 10. Instruction fine-tuning improves the model perfor- mance significantly with minimal computing, only 0.2% of the total pre-training compute in the case of PaLM 540B. Flan also suggests that adding more instruction fine-tuning tasks with CoT reasoning data will likely improve the performance further.
		2. Instruction-Tuning with LLMs Generated Datasets: Generating an instruction-tuning dataset requires carefully writing instructions and input-output pairs, which are often
		
		[written by humans, smaller in size, and less diverse. To overcome this, self-instruct [](#bookmark186)131[] proposed an approach to prompt available LLMs to generate instruction-tuning datasets. Self-instruct outperformed models trained on manually created dataset SUPER-NATURALINSTRUCTIONS (a dataset with 1600+ tasks) [](#bookmark81)26[] by 33%. It starts with a seed of 175 tasks, 1 instruction, and 1 sample per task and iteratively generates new instructions (52k) and instances (82k input-output pairs) using GPT-3 [](#bookmark63)8[]. Contrary to this, Dynosaur [](#bookmark187)132] uses the meta- data of datasets on Huggingface to prompt LLMs to generate multiple task instruction-tuning datasets.
		
		# LLaMA Tuned
		
		Various models in literature instruction-tune
		
		[LLaMA [](#bookmark188)133[] with GPT-3 [](#bookmark63)8[] or GPT-4 [](#bookmark189)134[] generated datasets. Among these, Alpaca, Vicuna, and LLaMA-GPT-4 are a few general-purpose fine-tuned models, where Alpaca is trained on 52k samples from text-davinci-003, Vicuna on 70k samples from ShareGPT.com, and LLaMA-GPT-4 by re- creating Alpaca instructions from GPT-4. Goat [](#bookmark190)135[] fine- tunes LLaMA for arithmetic tasks (1 million samples) by generating data from ChatGPT and outperforms GPT-4, PaLM, BLOOM, OPT, etc, attributing its success to the LLaMA’s consistent tokenization of numbers. HuaTuo [](#bookmark191)136] is a medical knowledge model, fine-tuned with a generated QA dataset of 8k instructions.
		
		# Complex Instructions [Evol-Instruct [](#bookmark192)
		
		137
		
		[], [](#bookmark183)128
		
		] prompts LLMs to convert given instructions into a more complex
		
		‌TABLE III: Summary of pre-trained LLMs. Only the LLMs discussed individually in the previous sections are summarized. “Data/Tokens” is the model’s pre-training data which is either the number of tokens or data size. “Data Cleaning” indicates whether the data cleaning is performed or not. This includes heuristics (Heur), deduplication (Dedup), quality filtering (QF), and privacy filtering (PF), “Cost” is the calculated training cost obtained by multiplying the GPUs/TPUs hourly rate with the number of GPUs and the training time. The actual cost may vary due to many reasons such as using in-house GPUs or getting a discounted rate, re-training, number of employees working on the problem, etc. “Training Parallelism” indicates distributed training using data parallelism (D), tensor parallelism (T), pipeline parallelism (P), model parallelism (M), optimizer parallelism (OP), and rematerialization (R), where for “Library” column, “DS” is a short form for Deep Speed. In column “Commercial Use”, we assumed a model is for non-commercial purposes if its license is not available.‌
		
		  
		
		
		Models Publication
		
		  
		
		
		#### License
		
		  
		
		
		#### Model
		
		  
		
		
		#### No. of
		
		  
		
		
		#### Commercial
		
		  
		
		
		#### Steps
		
		  
		
		
		#### Data/
		
		  
		
		
		#### Data
		
		  
		
		
		#### No. of
		
		  
		
		
		#### Processing Training Calculated
		
		  
		
		
		#### Training
		
		#### Venue
		
		#### Type
		
		#### Creators Purpose
		
		#### Params
		
		#### Use
		
		#### Trained Tokens
		
		#### Cleaning
		
		#### Processing Units Unit Type
		
		#### Time
		
		#### Train. Cost Parallelism Library
		
		[T5 [](#bookmark66)[11](#bookmark66)] JMLR'20 Apache-2.0 Google General 11B ✓ [1M 1T Heur+Dedup 1024 TPU v3 - - D+M Mesh TensorFlow GPT-3 [](#bookmark63)[8](#bookmark63)] NeurIPS'20 - OpenAI General 175B *×* - 300B Dedup+QF - V100 - - M -
		
		[mT5 [](#bookmark67)[12](#bookmark67)] NAACL'21 Apache-2.0 Google General 13B ✓ 1M 1T - - - - - - - PanGu-α [[](#bookmark139)[84](#bookmark139)] arXiv'21 Apache-2.0 Huawei General 200B ✓ [260k 1.1TB Heur+Dedup 2048 Ascend 910 - - D+OP+P+O+R MindSpore CPM-2 [](#bookmark68)[13](#bookmark68)] AI Open'21 MIT Tsinghua General 198B ✓ [1M 2.6TB Dedup - - - - D+M JAXFormer Codex [](#bookmark163)[108](#bookmark163)] arXiv'21 - OpenAI Coding 12B *×* - 100B Heur - - - - - -
		
		[ERNIE 3.0 [](#bookmark141)[86](#bookmark141)] arXiv'21 - Baidu General 10B *×* 120k∗ 375B Heur+Dedup 384 V100 - - M∗ PaddlePaddle
		
		[Jurassic-1 [](#bookmark143)[88](#bookmark143)] White-Paper'21 Apache-2.0 AI21 General 178B ✓ [- 300B - 800 GPU - - D+M+P Megatron+DS HyperCLOVA [](#bookmark145)[90](#bookmark145)] EMNLP'21 - Naver General 82B *×* [- 300B Clf+Dedup+PF 1024 A100 321h 1.32 Mil M Megatron Yuan 1.0 [](#bookmark146)[91](#bookmark146)] arXiv'21 Apache-2.0 - General 245B ✓ 26k∗ 180B Heur+Clf+Dedup 2128 GPU - - D+T+P -
		
		[Gopher [](#bookmark147)[92](#bookmark147)] arXiv'21 - Google General 280B *×* [- 300B QF+Dedup 4096 TPU v3 920h 13.19 Mil D+M JAX+Haiku ERNIE 3.0 Titan [](#bookmark148)[93](#bookmark148)] arXiv'21 - Baidu General 260B *×* - 300B Heur+Dedup - Ascend 910 - - D+M+P+D\* PaddlePaddle
		
		[GPT-NeoX-20B [](#bookmark180)[125](#bookmark180)] BigScience'22 Apache-2.0 EleutherAI General 20B ✓ [150k 825GB None 96 40G A100 - - M Megatron+DS+PyTorch OPT [](#bookmark65)[10](#bookmark65)] arXiv'22 MIT Meta General 175B ✓ [150k 180B Dedup 992 80G A100 - - D+T Megatron BLOOM [](#bookmark64)[9](#bookmark64)] arXiv'22 RAIL-1.0 BigScience General 176B ✓ [- 366B Dedup+PR 384 80G A100 2520h 3.87 Mil D+T+P Megatron+DS Galactica [](#bookmark171)[116](#bookmark171)] arXiv'22 Apache-2.0 Meta Science 120B *×* 225k 106B Dedup 128 80GB A100 - - - Metaseq
		
		[GLaM [](#bookmark152)[97](#bookmark152)] ICML'22 - Google General 1.2T *×* 600k∗ 600B Clf 1024 TPU v4 - - M GSPMD
		
		[LaMDA [](#bookmark173)[118](#bookmark173)] arXiv'22 - Google Dialog 137B *×* [3M 2.81T Filtered 1024 TPU v3 1384h 4.96 Mil D+M Lingvo MT-NLG [](#bookmark76)[21](#bookmark76)] arXiv'22 Apache-v2.0 MS.+Nvidia General 530B *×* [- 270B - 4480 80G A100 - - D+T+P Megatron+DS AlphaCode [](#bookmark164)[109](#bookmark164)] Science'22 Apache-v2.0 Google Coding 41B ✓ [205k 967B Heur+Dedup - TPU v4 - - M JAX+Haiku Chinchilla [](#bookmark155)[100](#bookmark155)] arXiv'22 - Google General 70B *×* [- 1.4T QF+Dedup - TPUv4 - - - JAX+Haiku PaLM [](#bookmark69)[14](#bookmark69)] arXiv'22 - Google General 540B *×* [255k 780B Heur 6144 TPU v4 - - D+M JAX+T5X AlexaTM [](#bookmark156)[101](#bookmark156)] arXiv'22 Apache v2.0 Amazon General 20B *×* [500k 1.1T Filtered 128 A100 2880h 1.47 Mil M DS Sparrow [](#bookmark174)[119](#bookmark174)] arXiv'22 - Google Dialog 70B *×* - - - 64 TPU v3 - - M -
		
		[U-PaLM [](#bookmark75)[20](#bookmark75)] arXiv'22 - Google General 540B *×* [20k - - 512 TPU v4 120h 0.25 Mil - - UL2 [](#bookmark70)[15](#bookmark70)] ICLR'23 Apache-2.0 Google General 20B ✓ [2M 1T - 512 TPU v4 - - M JAX+T5X GLM [](#bookmark157)[102](#bookmark157)] ICLR'23 Apache-2.0 Multiple General 130B *×* - 400B - 768 40G A100 1440h 3.37 Mil M -
		
		[CodeGen [](#bookmark162)[107](#bookmark162)] ICLR'23 Apache-2.0 Salesforce Coding 16B ✓ [650k 577B Heur+Dedup - TPU v4 - - D+M JAXFormer LLaMA [](#bookmark159)[104](#bookmark159)] arXiv'23 - Meta General 65B *×* 350k 1.4T Clf+Heur+Dedup 2048 80G A100 504h 4.12 Mil D+M xFormers PanGuΣ [[](#bookmark161)[106](#bookmark161)] arXiv'23 - Huawei General 1.085T *×* [- 329B - 512 Ascend 910 2400h - D+OP+P+O+R MindSpore BloombergGPT [](#bookmark176)[121](#bookmark176)] arXiv23 - Bloomberg Finance 50B *×* [139k 569B Dedup 512 40G A100 1272h 1.97 Mil M PyTorch Xuan Yuan 2.0 [](#bookmark178)[123](#bookmark178)] arXiv23 RAIL-1.0 Du Xiaoman Finance 176B ✓ [- 366B Filtered 80GB A100 - - P DS CodeT5+ [](#bookmark168)[113](#bookmark168)] arXiv'23 BSD-3 Salesforce Coding 16B ✓ [110k 51.5B Dedup 16 40G A100 - - - DS StarCoder [](#bookmark170)[115](#bookmark170)] arXiv'23 OpenRAIL-M BigCode Coding 15.5B ✓ 250k 1T Dedup+QF+PF 512 80G A100 624h 1.28 Mil D+T+P Megatron-LM
		
		  
		
		
		[TABLE IV: Summary of instruction tuned LLMs. All abbreviations are the same as Table](#bookmark35) III. Entries in “Data/Tokens” starting with “S-” represents the number of training samples.
		
		  
		
		
		
		
		|  |
		| --- |
		| Models Publication License Model No. of Commercial Pre-trained Steps Data/ No. of Processing Train. Calculated Train.Venue Type Creators Purpose Params Use Models Trained Tokens Processing Units Unit Type Time Train. Cost Parallelism Library |
		| [WebGPT [](#bookmark181)[126](#bookmark181)] arXiv'21 - OpenAI | General 175B | × | GPT-3 | - | - | - | - - | - | - | - |
		| [T0 [](#bookmark77)[22](#bookmark77)] ICLR'22 Apache-2.0 BigScience | General 11B | ✓ | T5 | - | 250B | 512 | TPU v3 270h | 0.48 Mil | - | - |
		| [Tk-Instruct [](#bookmark81)[26](#bookmark81)] EMNLP'22 MIT AI2+ | General 11B | ✓ | T5 | 1000 | - | 256 | TPU v3 4h | 0.0036 Mil | - | Google T5 |
		| [OPT-IML [](#bookmark79)[24](#bookmark79)] arXiv'22 - Meta | General 175B | × | OPT | 8k | 2B | 128 | 40G A100 - | - | D+T | Megatron |
		| [Flan-U-PaLM [](#bookmark80)[25](#bookmark80)] ICLR'22 Apache-2.0 Google | General 540B | ✓ | U-PaLM | 30k | - | 512 | TPU v4 - | - | - | JAX+T5X |
		|  |  |  |  |  |  |  |  |  |  |  |
		| [mT0 [](#bookmark182)[127](#bookmark182)] ACL'23 Apache-2.0 HuggingFace+ General 13B | ✓ | mT5 | - | - | - - - | - - - |
		| [WizardCoder [](#bookmark183)[128](#bookmark183)] arXiv'23 Apache-2.0 HK Bapt. Coding 15B | × | StarCoder | 200 | S-78k | - - - | - - - |
		
		  
		
		
		[set. The instructions are iteratively evolved with re-writing instructions in complex wording and creating new instruc- tions. With this style of automated instruction generation, WizardLM [](#bookmark192)137[] (fine-tuned LLaMA on 250k instructions), outperforms Vicuna and Alpaca, and WizardCoder [](#bookmark183)128] (fine- tuned StarCoder) beats Claude-Plus, Bard, and others.
		
		# Self-Alignment
		
		Aligning LLMs with human feedback is slow
		
		[and costly. The literature suggests a semi-automated process to align LLMs by prompting LLMs to generate helpful, honest, and ethical responses to the queries, and fine-tuning using the newly created dataset. Constitutional AI [](#bookmark193)138[] replaces human feedback in RLHF with AI, naming RF from AI feedback (RLAIF). Self-Align [](#bookmark194)139] prompts the LLM with ICL examples, instructing LLM about what the response should contain to be considered useful and ethical. The same LLM is later fine-tuned with the new dataset.
	3. Robotics[LLMs have been rapidly adopted across various domains in the scientific community due to their multipurpose capabili- ties [](#bookmark88)33[]. In robotics research, the LLMs have very promising applications as well, such as enhancing human-robot inter- action [](#bookmark195)140[], [](#bookmark196)141[], [](#bookmark197)142[], [](#bookmark198)143[], task planning [](#bookmark199)144[], [](#bookmark200)145],

[[](#bookmark201)146[], navigation [](#bookmark202)147[], [](#bookmark203)148[], and learning [](#bookmark204)149[], [](#bookmark205)150]. They can enable robots to understand and generate natural language, aiding in instruction following, data annotation, and collaborative problem-solving. They can facilitate continuous learning by allowing robots to access and integrate information from a wide range of sources. This can help robots acquire new skills, adapt to changes, and refine their performance based on real-time data.

LLMs have also started assisting in simulating environments for testing and offer potential for innovative research in robotics, despite challenges like bias mitigation and integration

[complexity. The work in [](#bookmark206)151[] focuses on personalizing robot household cleanup tasks. By combining language-based plan- ning and perception with LLMs, such that having users provide object placement examples, which the LLM summarizes to generate generalized preferences, they show that robots can generalize user preferences from a few examples. An embod- ied LLM is introduced in [](#bookmark207)152], which employs a Transformer- based language model where sensor inputs are embedded alongside language tokens, enabling joint processing to en- hance decision-making in real-world scenarios. The model is trained end-to-end for various embodied tasks, achieving positive transfer from diverse training across language and vision domains. LLMs have also been explored as zero-shot human models for enhancing human-robot interaction.

[The study in [](#bookmark195)140] demonstrates that LLMs, trained on vast

[text data, can serve as effective human models for certain HRI tasks, achieving predictive performance comparable to specialized machine-learning models. However, limitations were identified, such as sensitivity to prompts and difficulties with spatial/numerical reasoning. In another study [](#bookmark208)153], the authors enable LLMs to reason over sources of natural lan- guage feedback, forming an “inner monologue” that enhances their ability to process and plan actions in robotic control scenarios. They combine LLMs with various forms of textual feedback, allowing the LLMs to incorporate conclusions into their decision-making process for improving the execution of user instructions in different domains, including simulated and real-world robotic tasks involving tabletop rearrangement and mobile manipulation. All of these studies employ LLMs as the core mechanism for assimilating everyday intuitive knowledge into the functionality of robotic systems.
4. ‌FINDINGS & INSIGHTS

[Training a billion-scale model is difficult as compared to a smaller model. LLMs are prone to various instabilities during training, such as hardware failure and instability. Other than this, LLMs exhibit different behaviors such as emergent abilities, improved zero-shot, few-shot, and reasoning abilities. Researchers report these essential details in their papers for results reproduction and field progress. We identify critical information in Table](#bookmark29) I [and](#bookmark32) II [such as architecture, training strategies, and pipelines that improve LLMs’ performance or other abilities acquired because of changes mentioned in section](#bookmark16) III.
5. ‌MODEL CONFIGURATIONS

[We provide different statistics of pre-trained and instruction- tuned models in this section. This includes information such as publication venue, license type, model creators, steps trained, parallelism, etc in Table](#bookmark35) III [and Table](#bookmark37) IV[. Architecture details of pre-trained LLMs are available in Table](#bookmark42) V[. Providing these details for instruction-tuned models is unnecessary because it fine-tunes pre-trained models for instruction datasets. Hence, architectural details are the same as the baselines. Moreover, optimization settings for various LLMs are available in Table](#bookmark43) VI [and Table](#bookmark44) VII[. We do not include details on precision, warmup, and weight decay in Table](#bookmark44) VII.

Neither of these details are important as others to mention for instruction-tuned models nor provided by the papers.
6. ‌DATASETS AND EVALUATION

[LLMs are known to require a huge amount of data for training. Hence, datasets for training and benchmarking these models are currently a topic of key importance. In Fig.](#bookmark46) 11[, we show the distribution of datasets currently available for benchmarking language models for a variety of natural lan- guage processing tasks. It is noteworthy that this distribution is restricted to only the tasks for which at least 20 datasets have already been proposed in the literature. LLMs can directly benefit from these dataset for training and evaluation. In general, the performance of LLMs greatly depends on the training dataset. A model trained on a good-quality data is likely to perform better on evaluation benchmarks. Specific training and evaluation datasets used by LLMs are summarized in Table](#bookmark50) VIII [and](#bookmark53) IX.

  



	1. Evaluation Tasks
	
	The evaluation of LLMs is a critical step in gauging their proficiency and identifying their limitations. This process provides a measure of the model’s ability to comprehend, gen- erate, and interact with human language across a spectrum of tasks. For Natural Language Understanding (NLU), these tasks encompass sentiment analysis, natural language inference, semantic understanding, closed book question answering, and reading comprehension, among others. In contrast, Natural Language Generation (NLG) tasks include text summarization, translation, and more. These tasks form part of established benchmarks that facilitate the comparison of different models.
	2. Evaluation Datasets
	
	[The role of specific datasets, particularly those commonly used, is fundamental in the evaluation of Large Language Models. These datasets, each with its unique design and set of challenges, serve as the basis for assessing the capabilities of LLMs. They offer a comprehensive measure of performance across a variety of tasks, providing insights into the models’ proficiency. In the following discussion, we provide a concise overview of a selection of these key datasets. While the Tables](#bookmark50) VIII [and](#bookmark53) IX include a larger set of datasets, we focus on the most commonly used ones in the evaluation of LLMs. Each dataset description encapsulates the core aspects it evaluates in an LLM, offering a snapshot of the model’s potential strengths and limitations.
	
	
		1. [HellaSwag [](#bookmark209)154]: A dataset that challenges models to
		
		pick the best ending to a context uses Adversarial Filtering to create a ‘Goldilocks’ zone of complexity, where generated text is absurd to humans but often misclassified by models.
		2. [PIQA [](#bookmark210)155]: A dataset that probes the physical knowl- edge of models, aiming to understand how well they are learning about the real world.
		3. [TriviaQA [](#bookmark211)156]: A dataset that tests models on reading comprehension and open domain question answering (QA) tasks, with a focus on Information Retrieval (IR)-style QA.
		
		  
		
		
		
		
		|  |  |  |  |  |  |  |  |  |  |  |  |
		| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
		|  |  |  |  |  |  |  |  |  |  |  |  |
		| Models | Type | Training | Vocab | Tokenizer | Norm | PE | Activation | Bias | nL | nH | HS |
		| T5 (11B) | Enc-Dec | Span Corruption | 32k | SentencePiece | Pre-RMS | Relative | ReLU | × | 24 | 128 | 1024 |
		| GPT3 (175B) | Causal-Dec | Next Token | - | - | Layer | Learned | GeLU |  | 96 | 96 | 12288 |
		| mT5 (13B) | Enc-Dec | Span Corruption | 250k | SentencePiece | Pre-RMS | Relative | ReLU | - | - | - | - |
		| PanGu-α (200B) | Causal-Dec | Next Token | 40k | BPE | Layer | - | - | - | 64 | 128 | 16384 |
		| CPM-2 (198B) | Enc-Dec | Span Corruption | 250k | SentencePiece | Pre-RMS | Relative | ReLU | - | 24 | 64 | - |
		| Codex (12B) | Causal-Dec | Next Token | - | BPE+ | Pre-Layer | Learned | GeLU | - | 96 | 96 | 12288 |
		| ERNIE 3.0 (10B) | Causal-Dec | Next Token | - | WordPiece | Post-Layer | Relative | GeLU | - | 48 | 64 | 4096 |
		| Jurassic-1 (178B) | Causal-Dec | Next Token | 256k | SentencePiece∗ | Pre-Layer | Learned | GeLU |  | 76 | 96 | 13824 |
		| HyperCLOVA (82B) | Causal-Dec | Next Token | - | BPE\* | Pre-Layer | Learned | GeLU | - | 64 | 80 | 10240 |
		| Yuan 1.0 (245B) | Causal-Dec | Next Token | - | - | - | - | - | - | 76 | - | 16384 |
		| Gopher (280B) | Causal-Dec | Next Token | 32k | SentencePiece | Pre-RMS | Relative | GeLU |  | 80 | 128 | 16384 |
		| ERNIE 3.0 Titan (260B) | Causal-Dec | Next Token | - | WordPiece | Post-Layer | Relative | GeLU | - | 48 | 192 | 12288 |
		| GPT-NeoX-20B | Causal-Dec | Next Token | 50k | BPE | Layer | Rotary | GeLU |  | 44 | 64 | - |
		| OPT (175B) | Causal-Dec | Next Token | - | BPE | - | - | ReLU |  | 96 | 96 | - |
		| BLOOM (176B) | Causal-Dec | Next Token | 250k | BPE | Layer | ALiBi | GeLU |  | 70 | 112 | 14336 |
		| Galactica (120B) | Causal-Dec | Next Token | 50k | BPE+custom | Layer | Learned | GeLU | × | 96 | 80 | 10240 |
		| GLaM (1.2T) | MoE-Dec | Next Token | 256k | SentencePiece | Layer | Relative | GeLU |  | 64 | 128 | 32768 |
		| LaMDA (137B) | Causal-Dec | Next Token | 32k | BPE | Layer | Relative | GeGLU | - | 64 | 128 | 8192 |
		| MT-NLG (530B) | Causal-Dec | Next Token | 50k | BPE | Pre-Layer | Learned | GeLU |  | 105 | 128 | 20480 |
		| AlphaCode (41B) | Enc-Dec | Next Token | 8k | SentencePiece | - | - | - | - | 64 | 128 | 6144 |
		| Chinchilla (70B) | Causal-Dec | Next Token | 32k | SentencePiece-NFKC | Pre-RMS | Relative | GeLU |  | 80 | 64 | 8192 |
		| PaLM (540B) | Causal-Dec | Next Token | 256k | SentencePiece | Layer | RoPE | SwiGLU | × | 118 | 48 | 18432 |
		| AlexaTM (20B) | Enc-Dec | Denoising | 150k | SentencePiece | Pre-Layer | Learned | GeLU |  | 78 | 32 | 4096 |
		| Sparrow (70B) | Causal-Dec | Pref.&Rule RM | 32k | SentencePiece-NFKC | Pre-RMS | Relative | GeLU |  | 16∗ | 64 | 8192 |
		| U-PaLM (540B) | Non-Causal-Dec | MoD | 256k | SentencePiece | Layer | RoPE | SwiGLU | × | 118 | 48 | 18432 |
		| UL2 (20B) | Enc-Dec | MoD | 32k | SentencePiece | - | - | - | - | 64 | 16 | 4096 |
		| GLM (130B) | Non-Causal-Dec | AR Blank Infilling | 130k | SentencePiece | Deep | RoPE | GeGLU |  | 70 | 96 | 12288 |
		| CodeGen (16B) | Causal-Dec | Next Token | - | BPE | Layer | RoPE | - | - | 34 | 24 | - |
		| LLaMA (65B) | Causal-Dec | Next Token | 32k | BPE | Pre-RMS | RoPE | SwiGLU | - | 80 | 64 | 8192 |
		| PanGu-Σ (1085B) | Causal-Dec | Next Token | - | BPE | Fused Layer | - | FastGeLU | - | 40 | 40 | 5120 |
		| BloombergGPT (50B) | Causal-Dec | Next Token | 131k | Unigram | Layer | ALiBi | GeLU |  | 70 | 40 | 7680 |
		| Xuan Yuan 2.0 (176B) | Causal-Dec | Next Token | 250k | BPE | Layer | ALiBi | GeLU |  | 70 | 112 | 14336 |
		| CodeT5+ (16B) | Enc-Dec | SC+NT+Cont.+Match | - | Code-Specific | - | - | - | - | - | - | - |
		| StarCoder (15.5B) | Causal-Dec | FIM | 49k | BPE | - | Learned | - | - | 40 | 48 | 6144 |
		
		
			*
			*
			*
			*
			*
			*
			*
			*
			*
			*
			*
			*
			*
			*‌TABLE V: Architecture details of LLMs. Here, “PE” is the positional embedding, “nL” is the number of layers, “nH” is the number of attention heads, “HS” is the size of hidden states
		
		  
		
		
		### Objective
		
		  
		
		
		‌TABLE VI: Summary of optimization settings used for pre-trained LLMs. The values for weight decay, gradient clipping, and dropout are 0.1, 1.0, and 0.1, respectively, for most of the LLMs.
		
		  
		
		
		  
		
		
		
		
		|  |  |  |  |  |  |  |  |  |  |  |
		| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
		|  |  | Sequence |  |  | LR | Optimizers | Precision | Weight | Grad |  |
		| Models | Batch Size | Length | LR | Warmup | Decay | AdaFactor Adam AdamW | FP16 BF16 Mixed | Decay | Clip | Dropout |
		
		  
		
		
		
		
		|  |  |  |  |  |  |  |  |
		| --- | --- | --- | --- | --- | --- | --- | --- |
		| T5 (11B) | 211 | 512 | 0.01 | × inverse square root | ✓ | - | - - ✓ |
		| GPT3 (175B) | 32K | - | 6e-5 |  |  |  | ✓ ✓ - |
		| mT5 (13B) | 1024 | 1024 | 0.01 | - inverse square root | ✓ | - | - - ✓ |
		| PanGu-α (200B) | - | 1024 | 2e-5 | - - | - | - |  |  | - |
		| CPM-2 (198B) | 1024 | 1024 | 0.001 | - - |  | - | - - ✓ |
		| Codex (12B) | - | - | 6e-5 |  |  |  |  |
		| ERNIE 3.0 (12B) | 6144 | 512 | 1e-4 |  |  | - |  |
		| Jurassic-1 (178B) | 3.2M | 2048 | 6e-5 |  |  |  | ✓ ✓ - |
		| HyperCLOVA (82B) | 1024 | - | 6e-5 | - cosine | ✓ | - |  |
		| Yuan 1.0 (245B) | <10M | 2048 | 1.6e-4 |  |  | - |  |
		| Gopher (280B) | 3M | 2048 | 4e-5 |  |  |  | - ✓ - |
		| ERNIE 3.0 Titan (260B) | - | 512 | 1e-4 |  |  |  | ✓ ✓ - |
		| GPT-NeoX-20B | 1538 | 2048 | 0.97e-5 |  |  |  | ✓ ✓ × |
		| OPT (175B) | 2M | 2048 | 1.2e-4 | - linear | ✓ | ✓ | ✓ ✓ ✓ |
		| BLOOM (176B) | 2048 | 2048 | 6e-5 |  |  |  | ✓ ✓ × |
		| Galactica (120B) | 2M | 2048 | 7e-6 |  |  | - | ✓ ✓ ✓ |
		| GLaM (1.2T) | 1M | 1024 | 0.01 | - inverse square root | ✓ | FP32 + ✓ | - ✓ *×* |
		| LaMDA (137B) | 256K | - | - | - - | - | - | - | - | - | - | - - - |
		| MT-NLG (530B) | 1920 | 2048 | 5e-5 |  |  |  | ✓ ✓ - |
		| AlphaCode (41B) | 2048 | 1536+768 | 1e-4 |  |  |  | ✓ ✓ - |
		| Chinchilla (70B) | 1.5M | 2048 | 1e-4 |  |  |  | - - - |
		| PaLM (540B) | 2048 | 2048 | 0.01 | - inverse square root | ✓ | - | ✓ ✓ × |
		| AlexaTM (20B) | 2M | 1024 | 1e-4 | - linear decay to 5% | ✓ | ✓ | ✓ - ✓ |
		| Sparrow (70B) | RM: 8+16, RL:16 | - | 2e-6 |  |  |  |  |  | - ✓ *×* |
		| U-PaLM (540B) | 32 | 2048 | 1e-4 | - cosine | ✓ | - | - - - |
		| UL2 (20B) | 1024 | 1024 | - | - inverse square root | - | - | - | - | - | - | × |
		| GLM (130B) | 4224 | 2048 | 8e-5 |  |  |  | ✓ ✓ ✓ |
		| CodeGen (16B) | 2M | 2048 | 5e-5 |  |  | - | ✓ ✓ - |
		| LLaMA (65B) | 4M | 2048 | 1.5e-4 |  |  | - | ✓ ✓ - |
		| PanGu-Σ (1.085T) | 512 | 1024 | 2e-5 |  |  |  | - - - |
		| BloombergGPT (50B) | 2048 | 2048 | 6e-5 |  |  |  | ✓ ✓ × |
		| Xuan Yuan 2.0 (176B) | 2048 | 2048 | 6e-5 |  |  |  | ✓ ✓ - |
		| CodeT5+ (16B) | 2048 | 1024 | 2e-4 | - linear | ✓ | ✓ |  |
		| StarCoder (15.5B) | 512 | 8k | 3e-4 |  |  |  |  |
		
		
			* cosine
			*
			*
			* -
			*
			* cosine
			*
			*
			* - -
			* linear
			*
			* - -
			* cosine
			*
			*
			* - -
			* cosine decay to 10%
			*
			* - -
			* cosine decay to 10%
			*
			*
			* linear
			*
			*
			* cosine
			*
			*
			* cosine
			*
			*
			* linear decay to 10%
			*
			* cosine decay to 10%
			*
			*
			* cosine decay to 10%
			*
			*
			* cosine decay to 10%
			*
			*
			* cosine decay to 10%
			*
			*
			*
			* cosine
			*
			*
			* cosine
			*
			* cosine decay to 10%
			*
			* -
			*
			*
			* cosine
			*
			*
			* cosine
			*
			*
			* - -
			* cosine
			*
			*
			* - -‌TABLE VII: Summary of optimization settings used for instruction-tuned LLMs. Values for gradient clipping and dropout are the same as the pre-trained models, while no model is using weight decay for instruction tuning.‌
		
		  
		
		
		  
		
		
		
		
		|  |  |  |  |  |  |  |  |  |
		| --- | --- | --- | --- | --- | --- | --- | --- | --- |
		|  |  | Sequence |  |  |  | Optimizer | Grad |  |
		| Models | Batch Size | Length | LR | Warmup | LR\_Decay | AdaFactor Adam | Clip | Dropout |
		
		  
		
		
		
		
		|  |  |  |  |  |  |  |  |
		| --- | --- | --- | --- | --- | --- | --- | --- |
		| WebGPT (175B) | BC:512, RM:32 | - | 6e-5 | - - |  | - | - |
		| T0 (11B) | 1024 | 1280 | 1e-3 | - - |  | - ✓ |
		| Tk-Instruct (11B) | 1024 | - | 1e-5 | - constant | - | - | - | - |
		| OPT-IML (175B) | 128 | 2048 | 5e-5 | × linear | ✓ | ✓ | ✓ |
		| Flan-U-PaLM (540B) | 32 | - | 1e-3 | - constant | ✓ | - ✓ |
		| WizardCoder (15B) | 512 | 2048 | 2e-5 |  | - | - | - | - |
		
		
			*
			*
			* cosine  
		
		
		![image](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/84862860/xkKrqBwU1CBAWMErZ7P1vTDgj4j3zKMm398TnZCDG_o-Image_012.jpg)
		
		‌Fig. 11: Distribution of benchmark datasets available for different natural language processing tasks. We include only the tasks for which at least 20 datasets have already been proposed.
		4. [LAMBADA [](#bookmark212)157]: This dataset evaluates contextual text understanding through a word prediction task. Models must predict the last word of a passage, which is easy for humans when given the whole passage, but not when given only the last sentence.
		5. [WinoGrande [](#bookmark213)158]: [A large-scale dataset inspired by the original Winograd [](#bookmark214)159] Schema Challenge tests models on their ability to resolve pronoun ambiguity and encourages the development of models that understand the broad context in natural language text.
		6. [MMLU [](#bookmark215)160]: A benchmark that measures the knowl- edge acquired by models during pretraining and evaluates models in zero-shot and few-shot settings across 57 subjects, testing both world knowledge and problem-solving ability.
		7. [SuperGLUE [](#bookmark58)3]: [A more challenging and diverse suc- cessor to the GLUE [](#bookmark216)161] benchmark, SuperGLUE includes a variety of language understanding tasks, such as question answering, natural language inference, and coreference reso- lution. It is designed to provide a rigorous test of language understanding and requires significant progress in areas like sample-efficient, transfer, multitasking, and unsupervised or self-supervised learning.
		8. [StoryCloze [](#bookmark217)162]: It introduces a new “StoryCloze Test”, a commonsense reasoning framework for evaluating story understanding, generation, and script learning. It considers a model’s ability to understand and generate coherent and sensible stories.
		9. [BoolQ [](#bookmark218)163]: A dataset derived from Google search queries, BoolQ challenges models to answer binary (yes/no) questions. The questions are naturally occurring and are paired with a paragraph from a Wikipedia article containing the answer. It’s a test of reading comprehension and reasoning.
		10. [RACE-High [](#bookmark219)164]: [A subset of the RACE [](#bookmark219)164] dataset, RACE-High consists of high school-level English exam questions. It is designed to evaluate the comprehension ability of models in a more academic and challenging context.
		11. [RACE-Middle [](#bookmark219)164]: [Another subset of the RACE [](#bookmark219)164] dataset, RACE-Middle, contains middle school-level English exam questions. It offers a slightly less challenging but academically oriented evaluation of a model’s comprehension skills.
		12. [Truthful-QA [](#bookmark185)130]: A unique benchmark that measures a language model’s truthfulness when generating answers. The dataset includes questions across various categories like health, law, and politics, some of which are designed to test the model against common human misconceptions.
		13. [ANLI [](#bookmark220)165]: A large-scale dataset designed to test the robustness of machine learning models in Natural Language Inference (NLI) is created through an iterative, adversarial process where humans try to generate examples that models cannot correctly classify.
		14. [ARC-Challenge [](#bookmark221)166]: A rigorous question-answering dataset, ARC-Challenge includes complex, grade-school level questions that demand reasoning beyond simple retrieval, testing the true comprehension capabilities of models.
		15. [XNLI [](#bookmark222)167]: [A cross-lingual benchmark, XNLI extends the MultiNLI [](#bookmark223)168] corpus to 15 languages, including low- resource ones like Urdu. It tests models on cross-lingual sentence understanding, with 112,500 annotated pairs across three categories: entailment, contradiction, and neutral.
		16. [PAWS-X [](#bookmark224)169]: [PAWS-X, or Cross-lingual Paraphrase Adversaries from Word Scrambling, is a multilingual version of the PAWS [](#bookmark225)170] dataset for paraphrase identification. It includes examples in seven languages and is designed to eval-
		
		‌uate the performance of cross-lingual paraphrase identification models.
		17. [ARC [](#bookmark221)166]: A larger version of the ARC-Challenge, this dataset contains both easy and challenging grade-school level, multiple-choice science questions. It’s a comprehensive test of a model’s ability to understand and answer complex questions.
		18. [ARC-Easy [](#bookmark221)166]: A subset of the ARC dataset, ARC- Easy, contains questions that are answered correctly by either a retrieval-based algorithm or a word co-occurrence algorithm. It’s a great starting point for models beginning to explore advanced question-answering.
		19. [CoQA [](#bookmark226)171]: A conversational question-answering dataset, CoQA challenges models with questions that rely on conversation history and require free-form text answers. Its diverse content from seven domains makes it a rigorous test for models’ ability to handle a wide range of topics and conversational contexts.
		20. [DROP [](#bookmark227)172]: DROP, or Discrete Reasoning Over the content of Paragraphs, is designed to test a model’s ability to understand a wide variety of reading phenomena. It encourages comprehensive and reliable evaluation of reading comprehen- sion capabilities.
		21. [RTE [](#bookmark228)173]: The Recognizing Textual Entailment (RTE) datasets come from a series of annual competitions on textual entailment, predicting whether a given sentence logically fol- lows from another and evaluating a model’s understanding of logical relationships in a text.
		22. [BIG-bench [](#bookmark229)174]: The BIG-bench (Behavior of Intel- ligent Generative Models Benchmark) is a large-scale bench- mark designed to test the abilities of LLMs across a wide range of tasks, including reasoning, creativity, ethics, and understanding of specific domains.
		23. [SQUADv2 [](#bookmark230)175]: [The Stanford Question Answering Dataset (SQuAD) [](#bookmark231)176] is a collection of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text from the corresponding reading passage. SQuADv2 combines the original SQuAD1.1 dataset with over 50,000 unanswerable questions. The aim is to evaluate a model’s ability to understand and answer questions based on a given context and to determine when a question is unanswerable.
		24. [GSM8K [](#bookmark232)177]: A dataset of diverse grade school math word problems, testing a model’s ability to perform multi-step mathematical reasoning.
		25. [WiC [](#bookmark233)178]: This dataset assesses a model’s ability to discern word meanings based on context, aiding in tasks related to Word Sense Disambiguation.
		26. [Math23k [](#bookmark234)179]: This one challenges a model’s ability to understand and solve mathematical word problems. It con- tains 23,000 Chinese arithmetic word problems that require models to perform reasoning and computation based on the problem description.
		27. [LCQMC [](#bookmark235)180]: The Large-scale Chinese Question Matching Corpus (LCQMC) is a dataset for evaluating the performance of models in semantic matching tasks. It contains pairs of questions in Chinese and their matching status,
		
		making it a valuable resource for research in Chinese language understanding.
		28. [MATH [](#bookmark236)181]: This dataset is a platform for evaluating the mathematical problem-solving abilities of AI models. It contains a diverse set of math problems, ranging from arith- metic to calculus, and is designed to test the model’s ability to understand and solve complex mathematical problems.
		29. [ETHOS [](#bookmark237)182]: ETHOS is a hate speech detection dataset built from YouTube and Reddit comments. It’s a tool in the fight against online hate speech, offering binary and multi-label variants for robust content moderation.
		30. [StereoSet [](#bookmark238)183]: StereoSet is a comprehensive dataset designed to measure and evaluate the presence of stereotypical biases in language models. It focuses on four key domains: gender, profession, race, and religion. By contrasting stereo- typical bias against language modeling ability, it provides a valuable tool for understanding and mitigating biases in large language models.
		31. [HumanEval [](#bookmark239)184]: A dataset for the problem-solving ability of AI models, which includes a diverse set of tasks that require various cognitive abilities, makes it a comprehensive tool for assessing general intelligence in AI.
		32. [WebQA [](#bookmark240)185]: A dataset for open-domain question answering, WebQA offers a large collection of web-based question-answer pairs. It is designed to assess the ability of AI models to understand and answer questions based on web content.
		33. [CMRC2018 [](#bookmark241)186]: This dataset is a test of Chinese language models’ ability to reason comprehensively and is designed with a challenging span-extraction format that pushes the boundaries of machine performance.
		34. [Wikitext103 [](#bookmark242)187]: With over 100 million tokens from Wikipedia’s top articles, this dataset is a rich resource for tasks that require understanding long-term dependencies, such as language modeling and translation.
		35. [PG19 [](#bookmark243)188]: This is a digital library of diverse books from Project Gutenberg. It’s specifically designed to facilitate research in unsupervised learning and language modeling, with a special focus on long-form content.
		36. [C4 [](#bookmark66)11]: A clean, multilingual dataset, C4 offers bil- lions of tokens from web-crawled data. It’s a comprehensive resource for training advanced Transformer models on various languages.
		37. [QuAC [](#bookmark244)189]: This dataset simulates an information- seeking dialog between students and teachers using hidden Wikipedia text. It introduces unique challenges not found in machine comprehension datasets, making it a valuable resource for advancing dialog systems.
		38. [COPA [](#bookmark245)190]: This dataset evaluates a model’s progress in open-domain commonsense causal reasoning. Each question comprises a premise and two alternatives, and the model must select the more plausible alternative, testing a model’s ability to understand and reason about cause and effect.
		39. [WSC [](#bookmark214)159]: The Winograd Schema Challenge (WSC) is a reading comprehension task in which a system must resolve references in a text, often requiring world knowledge and reasoning about the text.
		40. [RACE [](#bookmark219)164]: The RACE is a reading comprehension dataset collected from English examinations in China, which benchmarks AI models for understanding and answering ques- tions on long and complex passages, simulating the challenge of a real-world examination.
		41. [StrategyQA [](#bookmark246)191]: A question-answering dataset that requires reasoning over multiple pieces of evidence to evaluate the strategic reasoning ability of AI models, pushing the boundaries of what machines can understand and answer.
		42. [CSQA [](#bookmark247)192]: The CommonsenseQA is a question- answering dataset that requires commonsense knowledge to answer the ability of AI models to understand and answer questions that require commonsense reasoning.
		43. [GLUE [](#bookmark216)161]: The General Language Understanding Evaluation (GLUE) benchmark is a collection of resources for training, evaluating, and analyzing natural language under- standing systems. It includes a variety of tasks that test a wide range of linguistic phenomena, making it a comprehensive tool for evaluating language understanding in AI.
7. ‌SUMMARY AND DISCUSSION


	1. Architecture
	
	Due to the gigantic scale of LLMs, minor changes in architecture and training strategies have a big impact on performance and stability. Here, we summarize key architectural modules used in various LLMs, leading to better performance, reduced training time and memory, and better training stability.
	
	# Layer Normalization
	
	is found to have a significant effect on the performance and training stability of LLMs. Pre-norm,
	
	[that is normalizing inputs rather than outputs, is more common among LLMs stabilizing the training [](#bookmark63)8[], [](#bookmark159)104[], [](#bookmark139)84[]. BLOOM [](#bookmark64)9[] and AlexaTM [](#bookmark156)101[] utilize an additional layer normalization before embedding layer to stabilize the training of large-scale models, while the model’s zero- shot generalization ability can be negatively impacted [](#bookmark64)9[]. However, another study [](#bookmark157)102[] finds that pre-norm degrades fine-tuned model performance as compared to post-norm, and there are no stability benefits of pre-norm beyond the 100B scale. Therefore, GLM-130B [](#bookmark157)102] used deep-norm which is a variant of post-norm for better downstream task performance after fine-tuning.
	
	# Positional Encoding
	
	effect performance and training stability
	
	[of LLMs like other building blocks of a model. BLOOM [](#bookmark64)9[] finds ALiBi outperforming learned and rotary positional encodings. Contrary to this, GLM-130B [](#bookmark157)102] identifies rotary positional encoding better than ALiBi. So, there is no conclusion in literature about the positional encodings yet.
	
	# Parallel Attention [where attention and feed-forward layers are parallel to each other rather than sequential in transformer block has shown to reduce training time by 15%. There is no evidence of performance drop due to this change in literature and used by the models PaLM [](#bookmark69)
	
	14
	
	[], GPT-NeoX [](#bookmark149)94
	
	[], and CodeGen [](#bookmark162)107
	
	].
	
	# Multi-Query Attention
	
	has shared key and value attention
	
	[up sampling in autoregressive decoding. No performance degradation has been observed with this change and makes the training efficient allowing larger batch sizes. Multi-query attention is used in [](#bookmark69)14[], [](#bookmark164)109].
	
	# Mixture of Experts [allows easily scaling model to trillion of parameters [](#bookmark161)
	
	106
	
	[], [](#bookmark152)97
	
	]. Only a few experts are activated during the computation making them compute-efficient. The performance of MoE models is better than the dense models
	
	[for the same amount of data and requires less computation during fine-tuning to achieve performance similar to the dense models as discussed in [](#bookmark152)97[]. MoE architectures are less prone to catastrophic forgetting, therefore are more suited for continual learning [](#bookmark161)106[]. Extracting smaller sub-models for downstream tasks is possible without losing any performance, making MoE architecture hardware-friendly [](#bookmark161)106].
	
	Σ
	
	# Sparse vs Dense Activated [GPT-3 [](#bookmark63)
	
	8
	
	] uses sparse
	
	[transformers [](#bookmark100)45[] whereas GLaM [](#bookmark152)97[] and PanGu- [](#bookmark161)106[] use MoE [](#bookmark153)98[] architecture to lower computational costs and increase the model size and capacity. According to the literature, sparse modules do not degrade the model’s performance [](#bookmark100)45]. However, more experiments are required to verify this statement.
	2. Training Strategies
	
	Training models at a huge scale require some tricks to reduce training costs, avoid loss divergence and achieve better performance. We summarize and discuss some of these key tricks used in different LLMs.
	
	# Mixed Precision [is a famous method for LLMs to reduce memory usage and improve training efficiency. In mixed precision, forward and backward passes are performed in FP16 format whereas optimizer states and master weights are kept in FP32 format [](#bookmark350)
	
	295
	
	]. A drawback associated with this format
	
	[change is training instability due to a smaller value range resulting in loss spikes [](#bookmark157)102[]. An alternative to FP16 is BF16 which has a comparatively larger range and performs some precision-sensitive operations like gradient accumulation and softmax in FP32 [](#bookmark64)9]. BF16 has better performance and training stability but uses more memory and is supported on specific hardware, for example, A100 GPUs. Therefore, its adoption in LLMs is limited.
	
	# Training Instability
	
	is a common issue in LLMs where loss
	
	[divergence or spiking is observed multiple times during train- ing. This happens in the presence of gradient clipping [](#bookmark69)14[]. To mitigate this problem, many approaches suggest restarting training from an earlier checkpoint [](#bookmark69)14[], [](#bookmark157)102[], [](#bookmark152)97[], skipping 200-500 earlier data batches at the point of divergence in [](#bookmark69)14[] and re-shuffling batches in [](#bookmark152)97[]. The embedding layer gradient shrink proves to further stabilize the training as its gradient norm is significantly larger than the other layers [](#bookmark157)102]. Another suggestion to improve training stability for larger models is not to use **biases** [in dense and norm layers as in [](#bookmark69)14].
	
	# Weight Initialization
	
	plays a significant role in model conver-
	
	[gence and training stability. GPT-NeoX [](#bookmark149)94] initializes feed-
	
	heads in a transformer block while query attention heads are
	
	forward layers before residuals with 2
	
	√
	
	L d
	
	[as in [](#bookmark179)124] and
	
	[projected as usual. This reduces memory usage and speeds other layers with small initialization scheme [](#bookmark351)296]. This avoids
	
	‌TABLE VIII: Training and evaluation dataset for pre-trained LLMs. Here,“D” denotes Dialogue, “QA” denotes question answering, “CR” is for commonsense reasoning, “CoT” is for chain-of-thought, “RC” for reading comprehension, “LU” for language understanding, “IRC” for in-context reading comprehension, “NLI” for natural language inference, “WT” for winograd-style tasks, “SC” for sentence completion, “WSD” for word sense disambiguation, “CorefR” for coreference resolution.‌
	
	  
	
	
	
	
	|  |  |  |
	| --- | --- | --- |
	| Models | Training Dataset | Evaluation Dataset |
	| T5 | [C4 [](#bookmark66)[11](#bookmark66)[]](#bookmark66) | [GLUE [](#bookmark216)161[], CNNDM, SQuAD [](#bookmark231)176[], SuperGLUE [](#bookmark58)3[], EnDe, ENFr, EnRo, QQP [](#bookmark248)193[], MNLI-m [](#bookmark249)194[], MNLI-mm [](#bookmark249)194[], QNLI [](#bookmark231)176],[WNLI [](#bookmark214)159[], CB [](#bookmark250)195],[WiC [](#bookmark233)178[], WMT [](#bookmark251)196], CNN/DM |
	| GPT-3 | Common Crawl, WebText, Books Corpora, Wikipedia | QA: NaturalQS, WebQS, TriviaQA, ARC, CoQA, DROPSuperGLUE, WMT, LAMBADA, StoryCloze, HellaSwag |
	| mT5 | [mC4 [](#bookmark67)[12](#bookmark67)[]](#bookmark67) | [SP: XNLI [](#bookmark222)167[], PAWS-X [](#bookmark224)[169](#bookmark224)[] S: WikiAnn NER [](#bookmark252)[197](#bookmark252)[]](#bookmark252)[QA: MLQA [](#bookmark253)198[], TyDiQA-GoldP [](#bookmark254)[199](#bookmark254)[]](#bookmark254) |
	| PanGu-α | 1.1TB Chinese Text Corpus | - |
	| CPM-2 | [WuDaoCorpus [](#bookmark140)[85](#bookmark140)[]](#bookmark140) | [CCPM [](#bookmark255)200], C3 [[](#bookmark256)201], Sogou-Log,[WMT20 [](#bookmark257)202[], Math23k [](#bookmark234)179[], LCSTS [](#bookmark258)203],[LCQMC [](#bookmark235)180[], AdGen [](#bookmark259)204[], CUGE [](#bookmark260)[205](#bookmark260)[]](#bookmark260) |
	| Codex | 54 million public software repositories hosted on GitHubcontaining python files under 1MB | [HumanEval [](#bookmark239)184],64 original programming problems with unit test |
	| ERNIE3.0 | Chinese text corpora, Baidu Search, Web text, QA-long, QA-short, Poetry & CoupletDomain-specific data from medical, law and financial area Baidu knowledge graph with more than 50 million facts | NLU: NLPCC2014-SC, SE-ABSA16\_PHNS, SE-ABSA16\_CAME,[BDCI2019, COTE-BD [](#bookmark261)206[], COTE-DP [](#bookmark261)206[], COTE-MFW [](#bookmark261)206],[XNLI [](#bookmark222)167[], OCNLI [](#bookmark262)207[], CMNLI [](#bookmark262)207[], CLUEWSC2020 [](#bookmark262)207],[FinRE [](#bookmark263)208[], SanWen [](#bookmark264)209[], CCKS2020, AFQMC [](#bookmark262)207],[LCQMC [](#bookmark235)180[], CSL [](#bookmark262)207[], PAWS-X [](#bookmark224)169[], BQ Corpus [](#bookmark265)210],[TNEWS, IFLYTEK [](#bookmark266)211[], THUCNEWS, CNSE [](#bookmark267)212[], CNSS [](#bookmark267)212[], NLPCC-DBQA, CHIP2019, cMedQA [](#bookmark268)213],[cMedQA2 [](#bookmark269)214[], CKBQA 13 [](#bookmark270)215[], WebQA [](#bookmark240)185],[CLUENER [](#bookmark262)207[], Weibo [](#bookmark271)216[], OntoNotes [](#bookmark272)217], CCKS2019,[CMRC 2018 [](#bookmark241)186[], CMRC2019 [](#bookmark273)218[], DRCD [](#bookmark274)219],[DuReader [](#bookmark275)220], Dureaderrobust [[](#bookmark276)221], Dureaderchecklist, Dureaderyesno, C3 [[](#bookmark256)201[], CHID [](#bookmark277)222[], CAIL2018-Task1 & Task2 [](#bookmark278)223],[DogWhistle Insider & Outsider [](#bookmark279)224[], Sogou-log [](#bookmark280)225[]; NLG: LCSTS [](#bookmark258)203[], KBQG, DuReader-QG [](#bookmark275)220],Dureaderrobust[-QG [](#bookmark276)221[], MATINF-QA [](#bookmark281)226[], Math23KMath23k [](#bookmark234)179],[AdGen [](#bookmark259)204[], WMT20-enzh [](#bookmark257)202[], KdConv [](#bookmark282)[227](#bookmark282)[]](#bookmark282) |
	| Jurassic-1 | [Wikipedia, OWT, Books, C4 [](#bookmark66)11[], PileCC [](#bookmark283)228], arXiv, GitHub | [ARC-Challenge [](#bookmark221)166[], ARC-Easy [](#bookmark221)166[], BoolQ [](#bookmark218)163],[HellaSwag [](#bookmark209)154[], PIQA [](#bookmark210)155],[RACE-high [](#bookmark219)164[], RACE-middle [](#bookmark219)164],[RTE [](#bookmark228)173[], StoryCloze [](#bookmark217)162[], WinoGrande [](#bookmark213)[158](#bookmark213)[]](#bookmark213) |
	| HyperCLOVA | Korean blogs, Community sites, News, KiNKorean Wikipedia, Wikipedia (English and Japanese); Modu-Corpus: Messenger, News,Spoken and written language corpus, Web corpus | NSMC: a movie review dataset from NAVER movies;[KorQuAD 1.0 [](#bookmark284)229[], Korean ML dataset AI Hub Korean-English, YNAT [](#bookmark285)230],[KLUE-TC [](#bookmark285)230[], KLUE-STS [](#bookmark285)[230](#bookmark285)[]](#bookmark285) |
	| Yuan 1.0 | Common Crawl, SogouT, Sogou News,Baidu Baike, Wikipedia, Books | [FewCLUE [](#bookmark286)231[], ZeroCLUE [](#bookmark262)207],[CMRC2018 [](#bookmark241)186[], WebQA [](#bookmark240)[185](#bookmark240)[]](#bookmark240) |
	| Gopher | [subsets of MassiveWeb [](#bookmark147)[92](#bookmark147)[] Books, C4 [](#bookmark66)11], News, GitHub and[Wikipedia samples from MassiveText [](#bookmark147)[92](#bookmark147)[]](#bookmark147) | [LM: Pile [](#bookmark283)228[], LAMBADA [](#bookmark212)157],[Wikitext103 [](#bookmark242)187[], PG-19 [](#bookmark243)188[], C4 [](#bookmark66)11];[LU: MMLU [](#bookmark215)160[], BIG-bench [](#bookmark229)174];[RC: RACE-middle [](#bookmark219)164[], RACE-high [](#bookmark219)[164](#bookmark219)[]](#bookmark219)[QA: TriviaQA [](#bookmark211)156[], TruthfulQA [](#bookmark185)130[], Natural Questions [](#bookmark287)232[]; Fact Checking on Fever [](#bookmark288)233[], MultiFC [](#bookmark289)234];[HellaSwag [](#bookmark209)154[], PIQA [](#bookmark210)155[], WinoGrande [](#bookmark213)158[], SIQA [](#bookmark290)235];[RealToxicityPrompts [](#bookmark291)236[], Twitter Dataset [](#bookmark292)237],[CivilComments toxicity classification [](#bookmark293)[238](#bookmark293)[]](#bookmark293) |
	| ERNIE3.0 TITAN | Chinese text corpora, Baidu Search, Web text, QA-long, QA-short, Poetry & CoupletDomain-specific data from medical, law and financial area Baidu knowledge graph with more than 50 million facts ERNIE 3.0 adversarial dataset, ERNIE 3.0 controllable dataset | NLU: NLPCC2014-SC, SE-ABSA16\_PHNS, SE-ABSA16\_CAME,[BDCI2019, EPRSTMT [](#bookmark286)231[], COTE-BD [](#bookmark261)206[], COTE-MFW [](#bookmark261)206],[OCNLI [](#bookmark262)207[], CMNLI [](#bookmark262)207[], OCNLI-FC [](#bookmark286)231[], CLUEWSC [](#bookmark262)[207](#bookmark262)[]](#bookmark262)[CLUEWSC-FC [](#bookmark286)231[], FinRE [](#bookmark263)208[], SanWen [](#bookmark264)209[], AFQMC [](#bookmark262)207],[LCQMC [](#bookmark235)180[], PAWS-X [](#bookmark224)169[], BQ Corpus [](#bookmark265)210[], CSL [](#bookmark262)[207](#bookmark262)[]](#bookmark262)[CSL-FC [](#bookmark286)231[], BUSTM, TNEWS, TNEWS-FC [](#bookmark286)231[], IFLYTEK [](#bookmark266)211], IFLYTEK-FC[THUCNEWS, CNSE [](#bookmark267)212[], CNSS [](#bookmark267)212[], CSLDCP NLPCC-DBQA, CHIP2019, cMedQA [](#bookmark268)213[], cMedQA2 [](#bookmark269)214[], CKBQA 13 [](#bookmark270)215[], WebQA [](#bookmark240)185],[PD&CFT, CMRC2017 [](#bookmark294)239[], CMRC2019 [](#bookmark273)[218](#bookmark273)[]](#bookmark273)[CHID [](#bookmark277)222[], CHID-FC [](#bookmark286)231[], WPLC, DRCD [](#bookmark274)219],[DuReader [](#bookmark275)220], Dureaderrobust [[](#bookmark276)221], Dureaderchecklist, Dureaderyesno, C3 [[](#bookmark256)201[], CMRC 2018 [](#bookmark241)186[], CAIL2018-Task1 & Task2 [](#bookmark278)[223](#bookmark278)[]](#bookmark278)[DogWhistle Insider & Outsider [](#bookmark279)[224](#bookmark279)[]](#bookmark279) |
	| GPT-NeoX-20B | [Pile [](#bookmark283)[228](#bookmark283)[]](#bookmark283) | [ANLI [](#bookmark220)165[], ARC [](#bookmark221)166[], HeadQA [](#bookmark295)240[], HellaSwag [](#bookmark209)154],[LAMBADA [](#bookmark212)157[], LogiQA [](#bookmark296)241[], OpenBookQA [](#bookmark297)242[], PIQA [](#bookmark210)155],[PROST [](#bookmark298)243[], QA4MRE [](#bookmark299)244[], SciQ [](#bookmark300)245[], TriviaQA [](#bookmark211)156],[WinoGrande [](#bookmark213)158[], SuperGLUE [](#bookmark58)3[], MATH [](#bookmark236)181],Advanced Knowledge-Based Tasks |
	| OPT | [RoBERTa [](#bookmark301)246[], Pile [](#bookmark283)228],[PushShift.io Reddit [](#bookmark302)[247](#bookmark302)[]](#bookmark302) | [HellaSwag [](#bookmark209)154[], StoryCloze [](#bookmark217)162[], PIQA [](#bookmark210)155],[ARC-Easy [](#bookmark221)166[], ARC-Challenge [](#bookmark221)166[], OpenBookQA [](#bookmark297)242],[WinoGrad [](#bookmark214)159[], WinoGrande [](#bookmark213)158[], SuperGLUE [](#bookmark58)3[], Wizard of Wikipedia [](#bookmark303)248[], Empathetic Dialogues [](#bookmark304)249],[ConvAI2 [](#bookmark305)250[], Blended Skill Talk [](#bookmark306)251[], Wizard of Internet [](#bookmark307)[252](#bookmark307)[] ETHOS [](#bookmark237)182[], CrowS-Pairs [](#bookmark308)253[], StereoSet [](#bookmark238)183],[RealToxicPrompts [](#bookmark291)236], Dialogue Responsible AI evaluations |
	
	Table Continued on Next Page
	
	  
	
	
	
	
	|  |  |  |
	| --- | --- | --- |
	| ‌Models | Training Dataset | Evaluation Dataset |
	| BLOOM | [ROOTS [](#bookmark309)[254](#bookmark309)[]](#bookmark309) | - |
	| Galactica | arXiv, PMC, Semantic ScholarWikipedia, StackExchange, LibreText, Open Textbooks RefSeq Genome, OEIS, LIPID MAPS, NASAExoplanet Common Crawl, ScientificCC, AcademicCCGitHub repositories[Khan Problems [](#bookmark310)255[], GSM8K [](#bookmark232)177], OneSmallStep | Knowledge probes, Latex equations,[AminoProbe [](#bookmark171)116[], BioLAMA [](#bookmark171)116[], Chemical Reactions [](#bookmark171)116],[Galaxy Clusters [](#bookmark171)116[], Mineral Groups [](#bookmark171)[116](#bookmark171)[]](#bookmark171) |
	| GLaM | Filtered Webpages, Social media conversations Wikipedia, Forums, Books, News | [NLG: TriviaQA [](#bookmark211)156[], NQS, WebQS, SQuADv2 [](#bookmark230)175],[LAMBADA [](#bookmark212)157[], DROP [](#bookmark227)172[], QuAC [](#bookmark244)189[], CoQA [](#bookmark226)171];[NLU: HellaSwag [](#bookmark209)154[], StoryCloze [](#bookmark217)162[], WinoGrad [](#bookmark214)159],[WinoGrande [](#bookmark213)158[], RACE-middle [](#bookmark219)164[], RACE-high [](#bookmark219)164[], PIQA [](#bookmark210)155],[ARC-Challenge [](#bookmark221)166[], ARC-Easy [](#bookmark221)166[], OpenbookQA [](#bookmark297)242],[BoolQ [](#bookmark218)163[], COPA [](#bookmark311)256[], RTE [](#bookmark228)173[], WiC [](#bookmark233)178],[MultiRC [](#bookmark312)257[], WSC [](#bookmark214)159[], ReCoRD [](#bookmark313)258[], CB [](#bookmark250)195],[ANLI R1 [](#bookmark220)165[], ANLI R2 [](#bookmark220)165[], ANLI R3 [](#bookmark220)[165](#bookmark220)[]](#bookmark220) |
	| LaMDA | [Infiniset [](#bookmark173)118]: Public documents, Dialogs, Utterances | [Mini-Turing Benchmark (MTB) [](#bookmark59)4];Self-collected dialogs with turns by asking crowdworkers to interact with LaMDA;[Wizard of Wikipedia [](#bookmark303)[248](#bookmark303)[]](#bookmark303) |
	| MT-NLG | Twosnapshots of Common Crawl and Books3,[OpenWebText2, Stack Exchange, PubMed Abstracts, Wikipedia, PG-19 [](#bookmark243)188], BookCorpus2, NIH ExPorter,[PileCC [](#bookmark283)228[], CC-Stories [](#bookmark314)259[], RealNews [](#bookmark315)[260](#bookmark315)[]](#bookmark315) | [Completionprediction: LAMBADA [](#bookmark212)[157](#bookmark212)[]](#bookmark212)[RC: RACE [](#bookmark219)164[], BoolQ [](#bookmark218)[163](#bookmark218)[]](#bookmark218)[CR:PiQA [](#bookmark210)[155](#bookmark210)[]](#bookmark210)[NaturalLanguage Interface: ANLI [](#bookmark220)165[], HANS [](#bookmark316)[261](#bookmark316)[]](#bookmark316) |
	| AlphaCode | Selected GitHub repositories[CodeContests [](#bookmark164)109[]: Codeforces [](#bookmark317)262],[Description2Code [](#bookmark318)263[], CodeNet [](#bookmark319)[264](#bookmark319)[]](#bookmark319) | [Codeforces competitions, CodeContests [](#bookmark164)109[], APPS [](#bookmark236)[181](#bookmark236)[]](#bookmark236) |
	| Chinchilla | [MassiveWeb [](#bookmark147)92[], MassiveText [](#bookmark147)[92](#bookmark147)[] Books, C4 [](#bookmark66)11], News, GitHub, Wikipedia | [LM: Pile [](#bookmark283)228[], LAMBADA [](#bookmark212)157],[Wikitext103 [](#bookmark242)187[], PG-19 [](#bookmark243)188[], C4 [](#bookmark66)11];[LU: 57 MMLU [](#bookmark215)[160](#bookmark215)[] tasks, 62 BIG-bench [](#bookmark229)[174](#bookmark229)] tasks;[QA: TriviaQA [](#bookmark211)156[], Natural Questions [](#bookmark287)232];[RC: RACE-middle [](#bookmark219)164[], RACE-high [](#bookmark219)164];[HellaSwag [](#bookmark209)154[], PIQA [](#bookmark210)155[], WinoGrande [](#bookmark213)158],[SIQA [](#bookmark290)235[], BoolQ [](#bookmark218)163[], TruthfulQA [](#bookmark185)[130](#bookmark185)[]](#bookmark185) |
	| PaLM | webpages, books, wikipedia, news, articles, source code, social media conversations | [QA: TriviaQA [](#bookmark211)156[], Natural Questions [](#bookmark287)232[], Web Questions [](#bookmark320)265],[TyDiQA-GoldP [](#bookmark254)199[]; CR: PIQA [](#bookmark210)155[], ARC [](#bookmark221)166[], OpenBookQA [](#bookmark297)242];[IRC: DROP [](#bookmark227)172[], CoQA [](#bookmark226)171[], QuAC [](#bookmark244)189[], SQuADv2 [](#bookmark230)175[], RACE [](#bookmark219)164];[NLI: ANLI [](#bookmark220)165[]; WT: WinoGrad [](#bookmark214)159[], WinoGrande [](#bookmark213)158];[CoT: GSM8K [](#bookmark232)177[], StrategyQA [](#bookmark246)191[], CSQA [](#bookmark247)192],[SVAMP [](#bookmark321)266[], MAWPS [](#bookmark322)267[], AQuA [](#bookmark323)268];[LU: MMLU [](#bookmark215)[160](#bookmark215)[] SuperGLUE [](#bookmark58)3[], LAMBADA [](#bookmark212)157],[HellaSwag [](#bookmark209)154[], StoryCloze [](#bookmark217)162[], BIG-bench [](#bookmark229)174], WMT language pairs |
	| AlexaTM | [Wikipedia, mC4 [](#bookmark67)[12](#bookmark67)[]](#bookmark67) | [NLG: MLSum [](#bookmark324)269[], XSum [](#bookmark325)270[], E2E [](#bookmark326)271[], WebNLG [](#bookmark327)272];[Machine Translation: Flores-101 [](#bookmark328)273[], English-German WMT’16, English-French WMT’14, German-French WMT’19 [](#bookmark329)274];[NLP: XNLI [](#bookmark222)167[], XCOPA [](#bookmark245)190[], PAWS-X [](#bookmark224)169[], XWinograd [](#bookmark330)275],[SuperGLUE [](#bookmark58)3[], SQUADv2 [](#bookmark230)175[], MultiArith [](#bookmark331)[276](#bookmark331)[]](#bookmark331) |
	| Sparrow | Human data for rule violations and per-turn response preferences,[Self-play data accumulated through training, GopherCite FilteredELI5 [](#bookmark332)[277](#bookmark332)[]](#bookmark332) | Per-turn response preference and adversarial probing,[Multi-turn dialogues, Information-seeking dialogues, Chinchilla-generated [](#bookmark155)[100](#bookmark155)[] conversational questions, GopherCite [](#bookmark332)[277](#bookmark332)] human evaluation interface,[FilteredELI5 [](#bookmark332)[277](#bookmark332)[] “Free” dialogues, DPC-generated [](#bookmark155)[100](#bookmark155)[] dialogues WinoGender [](#bookmark333)278[], Winobias [](#bookmark334)279[], BBQ [](#bookmark335)280],[Natural Questions [](#bookmark287)232[], Quiz Bowl [](#bookmark336)281[], TriviaQA [](#bookmark211)[156](#bookmark211)[]](#bookmark211) |
	| U-PaLM | Same as PaLM | [MMLU [](#bookmark215)160],[QA: TriviaQA [](#bookmark211)156[], Natural Questions [](#bookmark287)232[], TydiQA [](#bookmark254)199];[RC: LAMBADA [](#bookmark212)157];[CR: BoolQ [](#bookmark218)163[], PIQA [](#bookmark210)155[], HellaSwag [](#bookmark209)154[], WinoGrande [](#bookmark213)158];[CoT: GSM8K [](#bookmark232)177[], BBH [](#bookmark229)174[], StrategyQA [](#bookmark246)191[], CSQA [](#bookmark247)192];[LU: MMLU [](#bookmark215)[160](#bookmark215)[] SuperGLUE [](#bookmark58)3[], MGSM [](#bookmark337)[282](#bookmark337)[]](#bookmark337) |
	| UL2 | - | [SuperGLUE [](#bookmark58)3[], GSM8K [](#bookmark232)177[], SVAMP [](#bookmark321)266[], ASDiv [](#bookmark338)283],[MAWPS [](#bookmark322)267[], AQuA [](#bookmark323)[268](#bookmark323)[]](#bookmark323) |
	| GLM-130B | - | [LAMBADA [](#bookmark212)157[], Pile [](#bookmark283)228[], MMLU [](#bookmark215)160],[CLUE [](#bookmark262)207[], CrowS-Pairs [](#bookmark308)253[], StereoSet [](#bookmark238)183],[ETHOS [](#bookmark237)182[], RealToxicPrompts [](#bookmark291)[236](#bookmark291)[]](#bookmark291) |
	| CodeGen | [Pile [](#bookmark283)228[], BigQuery, BigPython [](#bookmark162)[107](#bookmark162)[]](#bookmark162) | Mostly Basic Python Problems |
	| LLaMA | [CommonCrawl, C4 [](#bookmark66)11], Github, Wikipedia, Books, arXiv, StackExchange | [CR: BoolQ [](#bookmark218)163[], PIQA [](#bookmark210)155[], SIQA [](#bookmark290)235[], HellaSwag [](#bookmark209)154],[WinoGrande [](#bookmark213)158[], ARC-Challenge [](#bookmark221)166[], OpenBookQA [](#bookmark297)242];[QA: TriviaQA [](#bookmark211)156[], Natural Questions [](#bookmark287)232];[RC: RACE-middle [](#bookmark219)164[], RACE-high [](#bookmark219)164];[Mathematical Reasoning: MATH [](#bookmark236)181[], GSM8K [](#bookmark232)177];[Code Generation: HumanEval [](#bookmark239)184[], MBPP [](#bookmark339)284];[MMLU [](#bookmark215)160[], RealToxicityPrompts [](#bookmark291)236],[CrowS-Pairs [](#bookmark308)253[], WinoGender [](#bookmark333)278[], TruthfulQA [](#bookmark185)[130](#bookmark185)[]](#bookmark185) |
	| PanGUΣ | [WuDaoCorpora [](#bookmark140)85[], CLUE [](#bookmark262)207[], Pile [](#bookmark283)228[], C4 [](#bookmark66)11], and Python code | - |
	| BloombergGPT | [FinPile [](#bookmark176)121[], The Pile [](#bookmark283)228[], C4 [](#bookmark66)11[], Wikipedia [](#bookmark72)[17](#bookmark72)[]](#bookmark72) | [Financial Data, BIG-bench [](#bookmark229)174[], MMLU [](#bookmark215)160[], ARC, PiQA [](#bookmark210)155],[CommonsenseQA [](#bookmark247)192[], BoolQ [](#bookmark218)163[], OpenBookQA [](#bookmark297)242[], RACE [](#bookmark219)164[], MultiRC [](#bookmark312)257],[ReCoRD [](#bookmark313)258[], ANLI [](#bookmark220)165[], RTE [](#bookmark228)173[], COPA [](#bookmark245)190[], WIC [](#bookmark233)178[], WinoGrad [](#bookmark214)159],[WinoGrande [](#bookmark213)158[], HellaSWAG [](#bookmark209)154[], StoryCloze [](#bookmark217)[162](#bookmark217)[]](#bookmark217) |
	| XuanYuan 2.0 | Internet | - |
	| CodeT5+ | [CodeSearchNet [](#bookmark340)285], Github Code | [HumanEval [](#bookmark239)184[], MathQA [](#bookmark341)286[], GSM8K [](#bookmark232)[177](#bookmark232)[]](#bookmark232) |
	| StarCoder | [The Stack v1.2 [](#bookmark342)[287](#bookmark342)[]](#bookmark342) | [HumanEval [](#bookmark239)184[], MBPP [](#bookmark339)284[], DS-1000 [](#bookmark343)288[], HELM [](#bookmark344)289],[Multi-Language Evaluation, GSM8K [](#bookmark232)177[], MMLU [](#bookmark215)160[], CoQA [](#bookmark226)[171](#bookmark226)[]](#bookmark226) |
	
	[TABLE IX: Training and evaluation datasets for instruction-tuned LLMs. All the abbreviations are the same as Table](#bookmark50) [VIII](#bookmark50)‌
	
	  
	
	
	
	
	|  |  |  |
	| --- | --- | --- |
	| Models | Training Datasets | Evaluation Datasets |
	| T0 | - | [NLI: ANLI [](#bookmark220)165[], CB [](#bookmark250)195[], RTE [](#bookmark228)173];[SC: COPA [](#bookmark311)256[], HellaSwag [](#bookmark209)154[] StoryCloze [](#bookmark217)162];[WSD: WiC [](#bookmark233)178[]; CorefR: WSC [](#bookmark214)159[], Wino (XL) [](#bookmark213)158] |
	| WebGPT | [ELI5 [](#bookmark184)129[], ELI5 fact-check [](#bookmark181)126[], TriviaQA [](#bookmark211)156],[ARC-Challenge [](#bookmark221)166[], ARC-Easy [](#bookmark221)166], Hand-written data, Demonstrations of humans,Comparisons between model-generated answers | [ELI5 [](#bookmark184)129[], TruthfulQA [](#bookmark185)130[], TriviaQA [](#bookmark211)156] |
	| Tk-INSTRUCT | [SUP-NATINST [](#bookmark81)26] | [SUP-NATINST [](#bookmark81)26] |
	| mT0 | [xP3 [](#bookmark182)127] | - |
	| OPT-IML | [PromptSource [](#bookmark77)22[], FLAN [](#bookmark80)25],[Super-NaturalInstructions [](#bookmark345)290],[UnifiedSKG [](#bookmark346)291[], CrossFit [](#bookmark347)292],[ExMix [](#bookmark348)293[], T5 [](#bookmark66)11], Reasoning | [PromptSource [](#bookmark77)22[], FLAN [](#bookmark80)25[], Super-NaturalInstructions [](#bookmark345)290],[UnifiedSKG [](#bookmark346)291[], CrossFit [](#bookmark347)292[], ExMix [](#bookmark348)293[], T5 [](#bookmark66)11],[Reasoning, MMLU [](#bookmark215)160[], BBH [](#bookmark229)174[], RAFT [](#bookmark349)294] |
	| Flan | Muffin, T0-SF, NIv2, CoT | [MMLU [](#bookmark215)160[], BBH [](#bookmark229)174[], TyDiQA [](#bookmark254)199[], MGSM [](#bookmark337)282] |
	| WizardCoder | Code Alpaca | [HumanEval [](#bookmark239)184[], MBPP [](#bookmark339)284[], DS-1000 [](#bookmark343)288] |
	
	  
	
	
	[activations growing exponentially with the increasing depth. MT-NLG [](#bookmark76)21[] found higher variance for weight initialization leads to unstable training, hence validating small initialization scheme [](#bookmark351)296[]. Various models perform random weight ini- tialization which can cause bad initialization, Galactica [](#bookmark171)116] suggests a longer warmup to negate the effect.
	
	# Learning Rate [is important for stable training. It is suggested to use a lower value [](#bookmark64)
	
	9
	
	[], [](#bookmark69)14
	
	[], [](#bookmark75)20
	
	] with warmup and decay
	
	(cosine or linear). Usually, the learning rate is within the range 1e−4 to 8e−4[. Moreover, MT-NLG (530B) [](#bookmark76)21[] and GPT-NeoX (20B) [](#bookmark149)94[] suggest interpolating learning rates based on the model size using the GPT-3 [](#bookmark63)8] models ranging
	
	between 13B and 175B. This avoids tuning the learning rate hyperparameter.
	
	***Training Parallelism*** [3D parallelism, a combination of data, pipeline and tensor parallelism, is the most utilized training parallelism approach in LLMs [](#bookmark157)102[], [](#bookmark69)14[], [](#bookmark65)10[], [](#bookmark64)9[], [](#bookmark76)21[], [](#bookmark146)91[], [](#bookmark143)88[]. In addition to the 3D parallelism, BLOOM [](#bookmark64)9[] uses zero optimizer [](#bookmark116)61] to shard optimizer states. PanGu-α [[](#bookmark139)84] and PanGu-Σ [[](#bookmark161)106] go beyond the 3D parallelism and apply 5D parallelism which additionally contains optimizer parallelism and rematerialization.
	
	# Mode Switching [adds task-related tokens at the beginning of the text during training. These tokens refer to the natural language understanding and natural language generation tasks which are shown to improve the downstream task performance in [](#bookmark70)
	
	15
	
	[], [](#bookmark75)20
	
	[], [](#bookmark156)101
	
	]. During fine-tuning and inference, tokens are appended based on the downstream tasks.
	
	# Controllable Text Generation
	
	Generating credible and con- trolled text from a pre-trained model is challenging. GPT-
	
	[3 [](#bookmark63)8[] and other LLMs use in-context learning to control generated text. While in-context learning helps in controlling the generated text, ERNIE 3.0 Titan [](#bookmark148)93] suggests using adversarial loss to rank its generated text for credibility and soft prompts such as genre, topic, keywords, sentiment, and length for better control on generated text.
	
	# Alignment using human feedback[. Utilizing human prefer- ence in Large Language Models (LLMs) offers a significant advantage in addressing misalignment issues and ensuring accurate outputs. Reinforcement Learning from Human Feed- back (RLHF) [](#bookmark134)
	
	79
	
	] uses human feedback as a reward to guide model learning naturally, such as ranking and rating, reducing
	
	manual effort and annotation costs, enhancing model perfor- mance, and aligning with human values for ethical decision- making.
	
	[On the other hand, human involvement makes data col- lection time-consuming and resource-intensive. Designing a suitable reward function demands domain expertise, and com- plex labelling tasks may lead to ambiguous results. The growing data diversity poses scalability challenges for human annotators. Additionally, there’s a risk of unintentionally trans- ferring biases from human feedback to the model’s behav- ior [](#bookmark352)297[]. Lastly, the subjectivity in "HHH" evaluation criteria requires careful definition and implementation for effective alignment [](#bookmark133)78[]. Recently Reinforcement Learning from AI Feedback (RLAIF) and context distillation, use labels without human annotations, while enhancing reward modeling (RM) by generating synthetic comparison data from different-sized vanilla LLMs and prompts leading to an improved model for alignment [](#bookmark353)298[], [](#bookmark354)299[], [](#bookmark355)300[], [](#bookmark356)301].
	3. Pre-Training vs Instruction Tuning
	
	[While pre-training is important for the generalization of LLMs, instruction-tuning improves the performance of LLMs further and makes them useable. Therefore, it is suggested to perform instruction fine-tuning of pre-trained LLMs to use them effectively [](#bookmark80)25[], [](#bookmark81)26[], [](#bookmark357)302[], [](#bookmark79)24[], [](#bookmark181)126].
	4. Supervised Models vs Generalized Models
	
	[Although generalized models are capable of performing diverse tasks with good performance they have not yet outper- formed models trained in supervised settings. The supervised trained models are still state-of-the-art in various NLP tasks by a large margin as shown in [](#bookmark63)8[], [](#bookmark69)14[], [](#bookmark81)26].
	5. Zero-Shot vs Few-Shot
	
	[LLMs perform well in zero-shot and few-shot settings. But the performance difference between zero-shot and few-shot is large for pre-trained models [](#bookmark63)8[], [](#bookmark69)14[], naming LLMs as meta-learners [](#bookmark63)8[]. LLMs zero-shot evaluations underperform unsupervised methods in neural machine translation [](#bookmark63)8]. The
	
	[literature shows pre-training is not enough for good zero- shot performance [](#bookmark69)14[], [](#bookmark80)25[]. To improve the zero-shot per- formance the literature suggests using instruction fine-tuning that improves the zero-shot performance significantly and outperforms baselines. Instruction fine-tuning has also been shown to improve zero-shot generalization to unseen tasks. Another model Flan-PaLM [](#bookmark80)25] unlocks zero-shot reasoning with CoT training.
	6. Encoder vs Decoder vs Encoder-Decoder[Traditionally, these architectures perform well for different tasks, for example, encoder-only for NLU tasks, decoder- only for NLG, and encoder-decoder for sequence2sequence modeling. Encoder-only models are famous for smaller models such as Bert [](#bookmark60)5[], RoBERTa [](#bookmark358)303[], etc, whereas LLMs are either decoder-only [](#bookmark63)8[], [](#bookmark149)94[], [](#bookmark64)9[] or encoder-decoder [](#bookmark66)11[], [](#bookmark67)12[], [](#bookmark156)101[]. While decoder-only models are good at NLG tasks, various LLMs, PaLM [](#bookmark69)14[], OPT [](#bookmark65)10[], GPT-3 [](#bookmark63)8[], BLOOM [](#bookmark64)9[], LLaMA [](#bookmark188)133[], are decoder-only models with significant performance gains on both NLU and NLG tasks. In contradiction to this, T5 [](#bookmark66)11[] and UL2 [](#bookmark70)15[] identify encoder- decoder models out-performing decoder-only models. In an- other study, PaLM [](#bookmark69)14] finds increasing the size of decoder- only models can reduce the performance gap between decoder- only and encoder-decoder architectures.

Although decoder-only architectures have become a trend for

[LLMs, many recently proposed approaches [](#bookmark70)15[], [](#bookmark156)101[] use mode-switching tokens in text with encoder-decoder architec- tures to enable task-specific modes. Similarly, CodeT5+ [](#bookmark168)113] uses an encoder-decoder architecture with multiple training objectives for different tasks, activating the encoder, decoder, or both according to the tasks. These variations in architecture and training objectives allow a model to perform well in differ- ent settings. Because of this dynamic configuration, the future of LLMs can be attributed to encoder-decoder architectures.
8. Conclusion

This paper has reviewed various LLMs, discussing the pros and cons of multiple models. Our review concluded significant findings and provided a detailed analysis of the design aspects of each LLM, including architecture, datasets, and training pipelines. We have identified crucial architectural compo- nents and training strategies employed by different LLMs and presented a summary and discussion. Moreover, we have compared the performance of LLMs in zero-shot and few-shot settings, explored the impact of fine-tuning, and compared supervised vs generalized models, and encoder vs decoder vs encoder-decoder architectures. This paper will serve as a valuable resource for researchers, offering insights into the recent advancements in LLMs and providing fundamental concepts and details to develop improved LLMs.
9. Versioning

We keep track of the versions of this paper we release as the content updates.

# Version 1.0:

We covered 30 pre-trained models and 6 instruction-tuned models, including their overview, findings,

training, and evaluation datasets, and discussed important architectural and training tricks by various LLMs.

***Version 1.1:*** [Further pre-trained LLMs added along with discussion on on self-instruct LLMs. Categorized LLMs ac- cording to the application, provided descriptions of widely used evaluation datasets, added a section on robotics, and extended discussion in section](#bookmark49) VII. Tables have been updated. **Note:** If you find any mistakes, or have issues and conflicts with the writing in this paper, please email us. We welcome suggestions to improve this paper.

References


	1. ‌B. A. y Arcas, “Do large language models understand us?” *Daedalus*[, vol. 151, no. 2, pp. 183–197, 2022.](#bookmark0) [1](#bookmark0)‌
	2. ‌A. Chernyavskiy, D. Ilvovsky, and P. Nakov, “Transformers:“the end of history” for natural language processing?” in *Machine Learning and Knowledge Discovery in Databases. Research Track: European Conference, ECML PKDD 2021, Bilbao, Spain, September 13–17, 2021, Proceedings, Part III 21*[. Springer, 2021, pp. 677–693.](#bookmark0) [1](#bookmark0)
	3. A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill,
	
	‌O. Levy, and S. Bowman, “Superglue: A stickier benchmark for general-purpose language understanding systems,” *Advances in neural information processing systems*[, vol. 32, 2019.](#bookmark0) 1[,](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
	4. ‌D. Adiwardana, M.-T. Luong, D. R. So, J. Hall, N. Fiedel, R. Thop- pilan, Z. Yang, A. Kulshreshtha, G. Nemade, Y. Lu *et al.*, “Towards a human-like open-domain chatbot,” *arXiv preprint arXiv:2001.09977*[, 2020.](#bookmark0) 1[,](#bookmark52) [22](#bookmark52)
	5. ‌J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transformers for language understanding,” *arXiv preprint arXiv:1810.04805*[, 2018.](#bookmark0) 1[,](#bookmark55) [24](#bookmark55)
	6. ‌M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, and L. Zettlemoyer, “Deep contextualized word representations,” in *NAACL-HLT*[. Association for Computational Linguistics, 2018, pp. 2227–2237.](#bookmark0) [1](#bookmark0)
	7. M. Lewis, Y. Liu, N. Goyal, M. Ghazvininejad, A. Mohamed, O. Levy,
	
	‌V. Stoyanov, and L. Zettlemoyer, “Bart: Denoising sequence-to- sequence pre-training for natural language generation, translation, and comprehension,” *arXiv preprint arXiv:1910.13461*[, 2019.](#bookmark0) [1](#bookmark0)
	8. T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,
	
	A. Neelakantan, P. Shyam, G. Sastry, A. Askell *et al.*, “Language mod- els are few-shot learners,” *Advances in neural information processing systems*[, vol. 33, pp. 1877–1901, 2020.](#bookmark0) 1[,](#bookmark3) 2[,](#bookmark18) 8[,](#bookmark20) 9[,](#bookmark27) 11[,](#bookmark33) 14[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) 23,
	
	[24](#bookmark55)
	9. T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ilic´, D. Hesslow,
	
	‌R. Castagné, A. S. Luccioni, F. Yvon, M. Gallé *et al.*, “Bloom: A 176b- parameter open-access multilingual language model,” *arXiv preprint arXiv:2211.05100*[, 2022.](#bookmark0) 1[,](#bookmark3) 2[,](#bookmark10) 5[,](#bookmark20) 9[,](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
	10. S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen,
	
	‌C. Dewan, M. Diab, X. Li, X. V. Lin *et al.*, “Opt: Open pre-trained transformer language models,” *arXiv preprint arXiv:2205.01068*[, 2022.](#bookmark0) 1[,](#bookmark3) 2[,](#bookmark20) 9[,](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
	11. C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena,
	
	Y. Zhou, W. Li, and P. J. Liu, “Exploring the limits of transfer learn- ing with a unified text-to-text transformer,” *The Journal of Machine Learning Research*[, vol. 21, no. 1, pp. 5485–5551, 2020.](#bookmark0) 1[,](#bookmark3) 2[,](#bookmark11) 6[,](#bookmark14) 7[,](#bookmark18) 8,
	
	‌15[,](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
	12. L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant,
	
	A. Barua, and C. Raffel, “mt5: A massively multilingual pre-trained text-to-text transformer,” *arXiv preprint arXiv:2010.11934*[, 2020.](#bookmark0) 1[,](#bookmark3) 2,
	
	‌6[,](#bookmark18) 8[,](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark55) [24](#bookmark55)
	13. Z. Zhang, Y. Gu, X. Han, S. Chen, C. Xiao, Z. Sun, Y. Yao, F. Qi,
	
	‌J. Guan, P. Ke *et al.*, “Cpm-2: Large-scale cost-effective pre-trained language models,” *AI Open*[, vol. 2, pp. 216–224, 2021.](#bookmark0) 1[,](#bookmark18) 8[,](#bookmark36) [15](#bookmark36)
	14. A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts,
	
	‌P. Barham, H. W. Chung, C. Sutton, S. Gehrmann *et al.*, “Palm: Scaling language modeling with pathways,” *arXiv preprint arXiv:2204.02311*[, 2022.](#bookmark0) 1[,](#bookmark3) 2[,](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
	15. ‌Y. Tay, M. Dehghani, V. Q. Tran, X. Garcia, J. Wei, X. Wang, H. W. Chung, D. Bahri, T. Schuster, S. Zheng *et al.*, “Ul2: Unifying language learning paradigms,” in *The Eleventh International Conference on Learning Representations*[, 2022.](#bookmark3) 2[,](#bookmark11) 6[,](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
	16. [“Common crawl.” [Online]. Available:](https://commoncrawl.org/) [https://commoncrawl.org/](#bookmark3) [2](#bookmark3)
	17. [“Wikipedia.” [Online]. Available:](https://en.wikipedia.org/wiki/Main_Page) [https://en.wikipedia.org/wiki/Main\_](https://en.wikipedia.org/wiki/Main_Page) [Page](#bookmark3) 2[,](#bookmark52) [22](#bookmark52)
	18. [“Openwebtext corpus.” [Online]. Available:](http://Skylion007.github.io/OpenWebTextCorpus) [http://Skylion007.github.](http://Skylion007.github.io/OpenWebTextCorpus) [io/OpenWebTextCorpus](#bookmark3) [2](#bookmark3)
	19. [“Bigquery dataset.” [Online]. Available:](https://cloud.google.com/bigquery?hl=zh-cn) [https://cloud.google.com/](https://cloud.google.com/bigquery?hl=zh-cn) [bigquery?hl=zh-cn](#bookmark3) [2](#bookmark3)
	20. ‌Y. Tay, J. Wei, H. W. Chung, V. Q. Tran, D. R. So, S. Shakeri, X. Gar- cia, H. S. Zheng, J. Rao, A. Chowdhery *et al.*, “Transcending scaling laws with 0.1% extra compute,” *arXiv preprint arXiv:2210.11399*[, 2022.](#bookmark3) 2[,](#bookmark11) 6[,](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
	21. S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari,
	
	J. Casper, Z. Liu, S. Prabhumoye, G. Zerveas, V. Korthikanti *et al.*, “Us- ing deepspeed and megatron to train megatron-turing nlg 530b, a large- scale generative language model,” *arXiv preprint arXiv:2201.11990*[, 2022.](#bookmark3) 2[,](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
	22. ‌V. Sanh, A. Webson, C. Raffel, S. H. Bach, L. Sutawika, Z. Alyafeai,
	
	‌A. Chaffin, A. Stiegler, T. L. Scao, A. Raja *et al.*, “Multitask prompted training enables zero-shot task generalization,” *arXiv preprint arXiv:2110.08207*[, 2021.](#bookmark3) 2[,](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
	23. N. Muennighoff, T. Wang, L. Sutawika, A. Roberts, S. Biderman,
	
	T. L. Scao, M. S. Bari, S. Shen, Z.-X. Yong, H. Schoelkopf *et al.*, “Crosslingual generalization through multitask finetuning,” *arXiv preprint arXiv:2211.01786*[, 2022.](#bookmark3) 2[,](#bookmark31) [13](#bookmark31)
	24. ‌S. Iyer, X. V. Lin, R. Pasunuru, T. Mihaylov, D. Simig, P. Yu, K. Shus- ter, T. Wang, Q. Liu, P. S. Koura *et al.*, “Opt-iml: Scaling language model instruction meta learning through the lens of generalization,” *arXiv preprint arXiv:2212.12017*[, 2022.](#bookmark3) 2[,](#bookmark31) 13[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
	25. ‌H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y. Tay, W. Fedus, E. Li,
10. Wang, M. Dehghani, S. Brahma *et al.*, “Scaling instruction-finetuned language models,” *arXiv preprint arXiv:2210.11416*[, 2022.](#bookmark3) 2[,](#bookmark27) 11[,](#bookmark31) 13,

‌14[,](#bookmark36) 15[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)

1. Y. Wang, S. Mishra, P. Alipoormolabashi, Y. Kordi, A. Mirzaei,

‌A. Naik, A. Ashok, A. S. Dhanasekaran, A. Arunkumar, D. Stap *et al.*, “Super-naturalinstructions: Generalization via declarative instructions on 1600+ nlp tasks,” in *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*[, 2022, pp. 5085– 5109.](#bookmark3) 2[,](#bookmark31) 13[,](#bookmark33) 14[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
2. ‌B. Lester, R. Al-Rfou, and N. Constant, “The power of scale for parameter-efficient prompt tuning,” *arXiv preprint arXiv:2104.08691*[, 2021.](#bookmark3) 2[,](#bookmark18) 8[,](#bookmark27) [11](#bookmark27)
3. ‌J. He, C. Zhou, X. Ma, T. Berg-Kirkpatrick, and G. Neubig, “Towards a unified view of parameter-efficient transfer learning,” *arXiv preprint arXiv:2110.04366*[, 2021.](#bookmark3) 2[,](#bookmark14) [7](#bookmark14)
4. Z. Hu, Y. Lan, L. Wang, W. Xu, E.-P. Lim, R. K.-W. Lee, L. Bing, and

‌S. Poria, “Llm-adapters: An adapter family for parameter-efficient fine- tuning of large language models,” *arXiv preprint arXiv:2304.01933*[, 2023.](#bookmark3) 2[,](#bookmark14) [7](#bookmark14)
5. ‌B. Lester, R. Al-Rfou, and N. Constant, “The power of scale for parameter-efficient prompt tuning,” *arXiv preprint arXiv:2104.08691*[, 2021.](#bookmark3) 2[,](#bookmark14) [7](#bookmark14)
6. X. L. Li and P. Liang, “Prefix-tuning: Optimizing continuous prompts for generation,” *arXiv preprint arXiv:2101.00190*[, 2021.](#bookmark3) 2[,](#bookmark14) [7](#bookmark14)
7. ‌C. Zhou, Q. Li, C. Li, J. Yu, Y. Liu, G. Wang, K. Zhang, C. Ji, Q. Yan,

‌L. He *et al.*, “A comprehensive survey on pretrained foundation models: A history from bert to chatgpt,” *arXiv preprint arXiv:2302.09419*[, 2023.](#bookmark3) 2[,](#bookmark5) [3](#bookmark5)
8. W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min,

B. Zhang, J. Zhang, Z. Dong *et al.*, “A survey of large language models,” *arXiv preprint arXiv:2303.18223*[, 2023.](#bookmark3) 2[,](#bookmark5) 3[,](#bookmark14) 7[,](#bookmark36) [15](#bookmark36)
9. ‌G. Mialon, R. Dessì, M. Lomeli, C. Nalmpantis, R. Pasunuru,

‌R. Raileanu, B. Rozière, T. Schick, J. Dwivedi-Yu, A. Celikyil- maz *et al.*, “Augmented language models: a survey,” *arXiv preprint arXiv:2302.07842*[, 2023.](#bookmark3) [2](#bookmark3)
10. ‌U. Naseem, I. Razzak, S. K. Khan, and M. Prasad, “A comprehensive survey on word representation models: From classical to state-of-the- art word representation language models,” *Transactions on Asian and Low-Resource Language Information Processing*[, vol. 20, no. 5, pp. 1–35, 2021.](#bookmark5) [3](#bookmark5)
11. B. Min, H. Ross, E. Sulem, A. P. B. Veyseh, T. H. Nguyen, O. Sainz,

E. Agirre, I. Heinz, and D. Roth, “Recent advances in natural language processing via large pre-trained language models: A survey,” *arXiv preprint arXiv:2111.01243*[, 2021.](#bookmark5) [3](#bookmark5)
12. ‌J. J. Webster and C. Kit, “Tokenization as the initial phase in nlp,” in *COLING 1992 volume 4: The 14th international conference on computational linguistics*[, 1992.](#bookmark7) [4](#bookmark7)
13. ‌T. Kudo, “Subword regularization: Improving neural network transla- tion models with multiple subword candidates,” in *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*[, 2018, pp. 66–75.](#bookmark7) [4](#bookmark7)
14. ‌R. Sennrich, B. Haddow, and A. Birch, “Neural machine translation of rare words with subword units,” in *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1:*

Long Papers)[, 2016, pp. 1715–1725.](#bookmark7) [4](#bookmark7)
15. ‌S. J. Mielke, Z. Alyafeai, E. Salesky, C. Raffel, M. Dey, M. Gallé,

A. Raja, C. Si, W. Y. Lee, B. Sagot *et al.*, “Between words and char- acters: A brief history of open-vocabulary modeling and tokenization in nlp,” *arXiv preprint arXiv:2112.10508*[, 2021.](#bookmark7) [4](#bookmark7)
16. ‌M. Schuster and K. Nakajima, “Japanese and korean voice search,” in *2012 IEEE international conference on acoustics, speech and signal processing (ICASSP)*[. IEEE, 2012, pp. 5149–5152.](#bookmark7) [4](#bookmark7)
17. ‌C. W. Eriksen and J. E. Hoffman, “Some characteristics of selective attention in visual perception determined by vocal reaction time,”

‌Perception & Psychophysics[, vol. 11, no. 2, pp. 169–171, 1972.](#bookmark7) [4](#bookmark7)
18. ‌D. Bahdanau, K. Cho, and Y. Bengio, “Neural machine translation by jointly learning to align and translate,” *arXiv preprint arXiv:1409.0473*[, 2014.](#bookmark7) [4](#bookmark7)
19. ‌A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” *Advances in neural information processing systems*[, vol. 30, 2017.](#bookmark7) 4[,](#bookmark10) 5[,](#bookmark14) 7[,](#bookmark18) 8[,](#bookmark20) 9[,](#bookmark24) 10[,](#bookmark27) [11](#bookmark27)
20. ‌R. Child, S. Gray, A. Radford, and I. Sutskever, “Generating long sequences with sparse transformers,” *arXiv preprint arXiv:1904.10509*[, 2019.](#bookmark7) 4[,](#bookmark18) 8[,](#bookmark48) [20](#bookmark48)
21. T. Dao, D. Fu, S. Ermon, A. Rudra, and C. Ré, “Flashattention: Fast and memory-efficient exact attention with io-awareness,” *Advances in Neural Information Processing Systems*, vol. 35, pp. 16 344–16 359,

[2022.](#bookmark7) [4](#bookmark7)
22. ‌O. Press, N. Smith, and M. Lewis, “Train short, test long: Attention with linear biases enables input length extrapolation,” in *International Conference on Learning Representations*[, 2022. [Online]. Available:](https://openreview.net/forum?id=R8sQPpGCv0) [https://openreview.net/forum?id=R8sQPpGCv0](#bookmark7) [4](#bookmark7)
23. ‌J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu, “Roformer: Enhanced transformer with rotary position embedding,” *arXiv preprint arXiv:2104.09864*[, 2021.](#bookmark7) 4[,](#bookmark20) 9[,](#bookmark24) [10](#bookmark24)
24. ‌A. Kazemnejad, I. Padhi, K. N. Ramamurthy, P. Das, and S. Reddy, “The impact of positional encoding on length generalization in trans- formers,” *arXiv preprint arXiv:2305.19466*[, 2023.](#bookmark7) [4](#bookmark7)
25. K. Hornik, M. Stinchcombe, and H. White, “Multilayer feedforward networks are universal approximators,” *Neural networks*, vol. 2, no. 5,

[pp. 359–366, 1989.](#bookmark10) [5](#bookmark10)
26. ‌V. Nair and G. E. Hinton, “Rectified linear units improve restricted boltzmann machines,” in *Proceedings of the 27th international confer- ence on machine learning (ICML-10)*[, 2010, pp. 807–814.](#bookmark10) [5](#bookmark10)
27. D. Hendrycks and K. Gimpel, “Gaussian error linear units (gelus),”

‌arXiv preprint arXiv:1606.08415[, 2016.](#bookmark10) [5](#bookmark10)
28. N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhut- dinov, “Dropout: a simple way to prevent neural networks from overfitting,” *The journal of machine learning research*, vol. 15, no. 1,

[pp. 1929–1958, 2014.](#bookmark10) [5](#bookmark10)
29. D. Krueger, T. Maharaj, J. Kramár, M. Pezeshki, N. Ballas, N. R. Ke,

‌A. Goyal, Y. Bengio, A. Courville, and C. Pal, “Zoneout: Regulariz- ing rnns by randomly preserving hidden activations,” *arXiv preprint arXiv:1606.01305*[, 2016.](#bookmark10) [5](#bookmark10)
30. ‌N. Shazeer, “Glu variants improve transformer,” *arXiv preprint arXiv:2002.05202*[, 2020.](#bookmark10) 5[,](#bookmark24) [10](#bookmark24)
31. ‌Y. N. Dauphin, A. Fan, M. Auli, and D. Grangier, “Language modeling with gated convolutional networks,” in *International conference on machine learning*[. PMLR, 2017, pp. 933–941.](#bookmark10) [5](#bookmark10)
32. ‌B. Zhang and R. Sennrich, “Root mean square layer normalization,” *Advances in Neural Information Processing Systems*[, vol. 32, 2019.](#bookmark10) 5[,](#bookmark24) [10](#bookmark24)
33. ‌A. Baevski and M. Auli, “Adaptive input representations for neural language modeling,” *arXiv preprint arXiv:1809.10853*[, 2018.](#bookmark10) [5](#bookmark10)
34. ‌S. Shleifer, J. Weston, and M. Ott, “Normformer: Improved transformer pretraining with extra normalization,” *arXiv preprint arXiv:2110.09456*[, 2021.](#bookmark10) [5](#bookmark10)
35. ‌H. Wang, S. Ma, L. Dong, S. Huang, D. Zhang, and F. Wei, “Deepnet: Scaling transformers to 1,000 layers,” *arXiv preprint arXiv:2203.00555*[, 2022.](#bookmark10) [5](#bookmark10)
36. S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He, “Zero: Memory optimizations toward training trillion parameter models,” in *SC20: In- ternational Conference for High Performance Computing, Networking,*

‌Storage and Analysis[. IEEE, 2020, pp. 1–16.](#bookmark10) 5[,](#bookmark54) [23](#bookmark54)
37. ‌M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and B. Catan- zaro, “Megatron-lm: Training multi-billion parameter language models using model parallelism,” *arXiv preprint arXiv:1909.08053*[, 2019.](#bookmark10) [5](#bookmark10)
38. [“"bmtrain: Efficient training for big models.".” [Online]. Available:](https://github.com/OpenBMB/BMTrain) [https://github.com/OpenBMB/BMTrain](#bookmark10) [5](#bookmark10)
39. T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi,

‌P. Cistac, T. Rault, R. Louf, M. Funtowicz *et al.*, “Transformers: State-of-the-art natural language processing,” in *Proceedings of the 2020 conference on empirical methods in natural language processing: system demonstrations*[, 2020, pp. 38–45.](#bookmark10) [5](#bookmark10)
40. J. Rasley, S. Rajbhandari, O. Ruwase, and Y. He, “Deepspeed: Sys- tem optimizations enable training deep learning models with over 100 billion parameters,” in *Proceedings of the 26th ACM SIGKDD*

  


‌International Conference on Knowledge Discovery & Data Mining[, 2020, pp. 3505–3506.](#bookmark10) [5](#bookmark10)
41. J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary,

‌D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman- Milne *et al.*[, “Jax: composable transformations of python+ numpy programs,” 2018.](#bookmark10) [5](#bookmark10)
42. S. Li, J. Fang, Z. Bian, H. Liu, Y. Liu, H. Huang, B. Wang, and

‌Y. You, “Colossal-ai: A unified deep learning system for large-scale parallel training,” *arXiv preprint arXiv:2110.14883*[, 2021.](#bookmark10) [5](#bookmark10)
43. ‌J. He, J. Qiu, A. Zeng, Z. Yang, J. Zhai, and J. Tang, “Fastmoe: A fast mixture-of-expert training system,” *arXiv preprint arXiv:2103.13262*[, 2021.](#bookmark10) [5](#bookmark10)
44. ‌L. Huawei Technologies Co., “Huawei mindspore ai development framework,” in *Artificial Intelligence Technology*[. Springer, 2022, pp. 137–162.](#bookmark10) [5](#bookmark10)
45. A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,

‌T. Killeen, Z. Lin, N. Gimelshein, L. Antiga *et al.*, “Pytorch: An imperative style, high-performance deep learning library,” *Advances in neural information processing systems*[, vol. 32, 2019.](#bookmark10) [5](#bookmark10)
46. M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin,

S. Ghemawat, G. Irving, M. Isard *et al.*, “Tensorflow: a system for large-scale machine learning.” in *Osdi*, vol. 16, no. 2016. Savannah,

[GA, USA, 2016, pp. 265–283.](#bookmark10) [5](#bookmark10)
47. T. Chen, M. Li, Y. Li, M. Lin, N. Wang, M. Wang, T. Xiao, B. Xu,

‌C. Zhang, and Z. Zhang, “Mxnet: A flexible and efficient machine learning library for heterogeneous distributed systems,” *arXiv preprint arXiv:1512.01274*[, 2015.](#bookmark10) [5](#bookmark10)
48. P. J. Liu\*, M. Saleh\*, E. Pot, B. Goodrich, R. Sepassi, L. Kaiser, and

‌N. Shazeer, “Generating wikipedia by summarizing long sequences,” in *International Conference on Learning Representations*[, 2018. [Online]. Available:](https://openreview.net/forum?id=Hyg0vbWC-) [https://openreview.net/forum?id=Hyg0vbWC-](#bookmark11) [6](#bookmark11)
49. T. Wang, A. Roberts, D. Hesslow, T. Le Scao, H. W. Chung, I. Beltagy,

‌J. Launay, and C. Raffel, “What language model architecture and pretraining objective works best for zero-shot generalization?” in *International Conference on Machine Learning*[. PMLR, 2022, pp. 22 964–22 984.](#bookmark11) [6](#bookmark11)
50. L. Dong, N. Yang, W. Wang, F. Wei, X. Liu, Y. Wang, J. Gao,

‌M. Zhou, and H.-W. Hon, “Unified language model pre-training for natural language understanding and generation,” *Advances in neural information processing systems*[, vol. 32, 2019.](#bookmark11) [6](#bookmark11)
51. ‌X. Liu, Y. Zheng, Z. Du, M. Ding, Y. Qian, Z. Yang, and J. Tang, “Gpt understands, too,” *arXiv preprint arXiv:2103.10385*[, 2021.](#bookmark14) [7](#bookmark14)
52. N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. De Laroussilhe,

A. Gesmundo, M. Attariyan, and S. Gelly, “Parameter-efficient transfer learning for nlp,” in *International Conference on Machine Learning*.

[PMLR, 2019, pp. 2790–2799.](#bookmark14) [7](#bookmark14)
53. A. Askell, Y. Bai, A. Chen, D. Drain, D. Ganguli, T. Henighan,

‌A. Jones, N. Joseph, B. Mann, N. DasSarma *et al.*, “A general language assistant as a laboratory for alignment,” *arXiv preprint arXiv:2112.00861*[, 2021.](#bookmark14) 7[,](#bookmark54) [23](#bookmark54)
54. D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford,

‌D. Amodei, P. Christiano, and G. Irving, “Fine-tuning language models from human preferences,” *arXiv preprint arXiv:1909.08593*[, 2019.](#bookmark14) 7[,](#bookmark54) [23](#bookmark54)
55. Q. Dong, L. Li, D. Dai, C. Zheng, Z. Wu, B. Chang, X. Sun,

‌J. Xu, and Z. Sui, “A survey for in-context learning,” *arXiv preprint arXiv:2301.00234*[, 2022.](#bookmark14) [7](#bookmark14)
56. ‌J. Huang and K. C.-C. Chang, “Towards reasoning in large language models: A survey,” *arXiv preprint arXiv:2212.10403*[, 2022.](#bookmark14) [7](#bookmark14)
57. ‌A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever *et al.*, “Language models are unsupervised multitask learners,” *OpenAI blog*[, vol. 1, no. 8, p. 9, 2019.](#bookmark18) 8[,](#bookmark20) [9](#bookmark20)
58. ‌S. McCandlish, J. Kaplan, D. Amodei, and O. D. Team, “An empirical model of large-batch training,” *arXiv preprint arXiv:1812.06162*[, 2018.](#bookmark18) [8](#bookmark18)
59. W. Zeng, X. Ren, T. Su, H. Wang, Y. Liao, Z. Wang, X. Jiang, Z. Yang,

‌K. Wang, X. Zhang *et al.*, “Pangu-α : Large-scale autoregressive pretrained chinese language models with auto-parallel computation,” *arXiv preprint arXiv:2104.12369*[, 2021.](#bookmark18) 8[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) [23](#bookmark54)
60. S. Yuan, H. Zhao, Z. Du, M. Ding, X. Liu, Y. Cen, X. Zou, Z. Yang, and J. Tang, “Wudaocorpora: A super large-scale chinese corpora for pre-training language models,” *AI Open*[, vol. 2, pp. 65–68, 2021.](#bookmark18) 8,

‌21[,](#bookmark52) [22](#bookmark52)
61. Y. Sun, S. Wang, S. Feng, S. Ding, C. Pang, J. Shang, J. Liu, X. Chen,

Y. Zhao, Y. Lu *et al.*, “Ernie 3.0: Large-scale knowledge enhanced pre-training for language understanding and generation,” *arXiv preprint arXiv:2107.02137*[, 2021.](#bookmark18) 8[,](#bookmark36) [15](#bookmark36)
62. ‌Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. V. Le, and R. Salakhutdinov, “Transformer-xl: Attentive language models beyond a fixed-length context,” *arXiv preprint arXiv:1901.02860*[, 2019.](#bookmark18) [8](#bookmark18)‌
63. O. Lieber, O. Sharir, B. Lenz, and Y. Shoham, “Jurassic-1: Technical details and evaluation,” *White Paper. AI21 Labs*[, vol. 1, 2021.](#bookmark18) 8[,](#bookmark20) 9[,](#bookmark36) 15,

[23](#bookmark54)
64. ‌Y. Levine, N. Wies, O. Sharir, H. Bata, and A. Shashua, “Limits to depth efficiencies of self-attention,” *Advances in Neural Information Processing Systems*[, vol. 33, pp. 22 640–22 651, 2020.](#bookmark18) [8](#bookmark18)
65. B. Kim, H. Kim, S.-W. Lee, G. Lee, D. Kwak, D. H. Jeon, S. Park,

‌S. Kim, S. Kim, D. Seo *et al.*, “What changes can large-scale language models bring? intensive study on hyperclova: Billions-scale korean generative pretrained transformers,” *arXiv preprint arXiv:2109.04650*[, 2021.](#bookmark18) 8[,](#bookmark36) [15](#bookmark36)
66. S. Wu, X. Zhao, T. Yu, R. Zhang, C. Shen, H. Liu, F. Li, H. Zhu,

‌J. Luo, L. Xu *et al.*, “Yuan 1.0: Large-scale pre-trained language model in zero-shot and few-shot learning,” *arXiv preprint arXiv:2110.04725*[, 2021.](#bookmark18) 8[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
67. J. W. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, F. Song,

‌J. Aslanides, S. Henderson, R. Ring, S. Young *et al.*, “Scaling language models: Methods, analysis & insights from training gopher,” *arXiv preprint arXiv:2112.11446*[, 2021.](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
68. S. Wang, Y. Sun, Y. Xiang, Z. Wu, S. Ding, W. Gong, S. Feng,

‌J. Shang, Y. Zhao, C. Pang *et al.*, “Ernie 3.0 titan: Exploring larger- scale knowledge enhanced pre-training for language understanding and generation,” *arXiv preprint arXiv:2112.12731*[, 2021.](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
69. ‌S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Gold- ing, H. He, C. Leahy, K. McDonell, J. Phang *et al.*, “Gpt-neox- 20b: An open-source autoregressive language model,” *arXiv preprint arXiv:2204.06745*[, 2022.](#bookmark20) 9[,](#bookmark48) 20[,](#bookmark54) 23[,](#bookmark55) [24](#bookmark55)
70. [W. Ben and K. Aran, “Gpt-j-6b: A 6 billion parameter autoregressive language model,” 2021.](#bookmark20) [9](#bookmark20)
71. P. Micikevicius, S. Narang, J. Alben, G. Diamos, E. Elsen, D. Garcia,

‌B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh *et al.*, “Mixed precision training,” *arXiv preprint arXiv:1710.03740*[, 2017.](#bookmark20) [9](#bookmark20)
72. N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun,

‌Y. Zhou, A. W. Yu, O. Firat *et al.*, “Glam: Efficient scaling of language models with mixture-of-experts,” in *International Conference on Machine Learning*[. PMLR, 2022, pp. 5547–5569.](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark48) [20](#bookmark48)
73. ‌N. Shazeer, A. Mirhoseini, K. Maziarz, A. Davis, Q. Le, G. Hinton, and J. Dean, “Outrageously large neural networks: The sparsely-gated mixture-of-experts layer,” *arXiv preprint arXiv:1701.06538*[, 2017.](#bookmark20) 9[,](#bookmark48) [20](#bookmark48)
74. ‌W. Fedus, B. Zoph, and N. Shazeer, “Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity,” *The Journal of Machine Learning Research*[, vol. 23, no. 1, pp. 5232–5270, 2022.](#bookmark20) [9](#bookmark20)
75. J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai,

‌E. Rutherford, D. d. L. Casas, L. A. Hendricks, J. Welbl, A. Clark *et al.*, “Training compute-optimal large language models,” *arXiv preprint arXiv:2203.15556*[, 2022.](#bookmark20) 9[,](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark52) [22](#bookmark52)
76. S. Soltan, S. Ananthakrishnan, J. FitzGerald, R. Gupta, W. Hamza,

H. Khan, C. Peris, S. Rawls, A. Rosenbaum, A. Rumshisky *et al.*, “Alexatm 20b: Few-shot learning using a large-scale multilingual seq2seq model,” *arXiv preprint arXiv:2208.01448*[, 2022.](#bookmark20) 9[,](#bookmark36) 15[,](#bookmark48) 20,

‌23[,](#bookmark55) [24](#bookmark55)
77. A. Zeng, X. Liu, Z. Du, Z. Wang, H. Lai, M. Ding, Z. Yang, Y. Xu,

‌W. Zheng, X. Xia *et al.*, “Glm-130b: An open bilingual pre-trained model,” *arXiv preprint arXiv:2210.02414*[, 2022.](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) [23](#bookmark54)
78. Z. Du, Y. Qian, X. Liu, M. Ding, J. Qiu, Z. Yang, and J. Tang, “Glm: General language model pretraining with autoregressive blank infilling,” in *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 2022, pp. 320–

[335.](#bookmark24) [10](#bookmark24)
79. H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,

‌T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar *et al.*, “Llama: Open and efficient foundation language models,” *arXiv preprint arXiv:2302.13971*[, 2023.](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark48) [20](#bookmark48)
80. G. Wenzek, M.-A. Lachaux, A. Conneau, V. Chaudhary, F. Guzmán,

‌A. Joulin, and E. Grave, “Ccnet: Extracting high quality monolingual datasets from web crawl data,” *arXiv preprint arXiv:1911.00359*[, 2019.](#bookmark24) [10](#bookmark24)

Σ
81. X. Ren, P. Zhou, X. Meng, X. Huang, Y. Wang, W. Wang, P. Li,

X. Zhang, A. Podolskiy, G. Arshinov *et al.*, “Pangu- : Towards trillion parameter language model with sparse heterogeneous computing,” *arXiv preprint arXiv:2303.10845*[, 2023.](#bookmark24) 10[,](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark54) [23](#bookmark54)
82. ‌E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang, Y. Zhou,

‌S. Savarese, and C. Xiong, “Codegen: An open large language model for code with multi-turn program synthesis,” *arXiv preprint arXiv:2203.13474*[, 2022.](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark52) [22](#bookmark52)
83. M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan,

‌H. Edwards, Y. Burda, N. Joseph, G. Brockman *et al.*, “Evaluating large language models trained on code,” *arXiv preprint arXiv:2107.03374*[, 2021.](#bookmark24) 10[,](#bookmark36) [15](#bookmark36)
84. Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond,

‌T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago *et al.*, “Competition- level code generation with alphacode,” *Science*[, vol. 378, no. 6624, pp. 1092–1097, 2022.](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark48) 20[,](#bookmark52) [22](#bookmark52)
85. ‌N. Shazeer, “Fast transformer decoding: One write-head is all you need,” *arXiv preprint arXiv:1911.02150*[, 2019.](#bookmark24) [10](#bookmark24)
86. ‌R. Y. Pang and H. He, “Text generation by learning from demonstra- tions,” *arXiv preprint arXiv:2009.07839*[, 2020.](#bookmark24) [10](#bookmark24)
87. ‌R. Dabre and A. Fujita, “Softmax tempering for training neural machine translation models,” *arXiv preprint arXiv:2009.09372*[, 2020.](#bookmark24) [10](#bookmark24)
88. ‌Y. Wang, H. Le, A. D. Gotmare, N. D. Bui, J. Li, and S. C. Hoi, “Codet5+: Open code large language models for code understanding and generation,” *arXiv preprint arXiv:2305.07922*[, 2023.](#bookmark24) 10[,](#bookmark36) 15[,](#bookmark55) [24](#bookmark55)
89. ‌Y. Wang, W. Wang, S. Joty, and S. C. Hoi, “Codet5: Identifier-aware unified pre-trained encoder-decoder models for code understanding and generation,” *arXiv preprint arXiv:2109.00859*[, 2021.](#bookmark24) [10](#bookmark24)
90. R. Li, L. B. Allal, Y. Zi, N. Muennighoff, D. Kocetkov, C. Mou,

‌M. Marone, C. Akiki, J. Li, J. Chim *et al.*, “Starcoder: may the source be with you!” *arXiv preprint arXiv:2305.06161*[, 2023.](#bookmark27) 11[,](#bookmark36) [15](#bookmark36)
91. ‌R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Sar- avia, A. Poulton, V. Kerkez, and R. Stojnic, “Galactica: A large language model for science,” *arXiv preprint arXiv:2211.09085*[, 2022.](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
92. [FairScale authors, “Fairscale: A general purpose modular pytorch library for high performance and large scale training,”](https://github.com/facebookresearch/fairscale) [https://github.](https://github.com/facebookresearch/fairscale) com/facebookresearch/fairscale[, 2021.](#bookmark27) [11](#bookmark27)
93. ‌R. Thoppilan, D. De Freitas, J. Hall, N. Shazeer, A. Kulshreshtha, H.-T. Cheng, A. Jin, T. Bos, L. Baker, Y. Du *et al.*, “Lamda: Language models for dialog applications,” *arXiv preprint arXiv:2201.08239*[, 2022.](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark52) [22](#bookmark52)
94. A. Glaese, N. McAleese, M. Tre˛bacz, J. Aslanides, V. Firoiu, T. Ewalds,

‌M. Rauh, L. Weidinger, M. Chadwick, P. Thacker *et al.*, “Improving alignment of dialogue agents via targeted human judgements,” *arXiv preprint arXiv:2209.14375*[, 2022.](#bookmark27) 11[,](#bookmark36) [15](#bookmark36)
95. V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley,

D. Silver, and K. Kavukcuoglu, “Asynchronous methods for deep rein- forcement learning,” in *International conference on machine learning*.

[PMLR, 2016, pp. 1928–1937.](#bookmark27) [11](#bookmark27)
96. S. Wu, O. Irsoy, S. Lu, V. Dabravolski, M. Dredze, S. Gehrmann,

‌P. Kambadur, D. Rosenberg, and G. Mann, “Bloomberggpt: A large language model for finance,” *arXiv preprint arXiv:2303.17564*[, 2023.](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark52) [22](#bookmark52)
97. ‌Y. Levine, N. Wies, O. Sharir, H. Bata, and A. Shashua, “Limits to depth efficiencies of self-attention,” *Advances in Neural Information Processing Systems*[, vol. 33, pp. 22 640–22 651, 2020.](#bookmark27) [11](#bookmark27)
98. ‌X. Zhang, Q. Yang, and D. Xu, “Xuanyuan 2.0: A large chinese financial chat model with hundreds of billions parameters,” *arXiv preprint arXiv:2305.12002*[, 2023.](#bookmark27) 11[,](#bookmark36) [15](#bookmark36)
99. [W. Ben, “Mesh-transformer-jax: Model-parallel implementation of transformer language model with jax,” 2021.](#bookmark30) 12[,](#bookmark48) [20](#bookmark48)
100. ‌S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Gold- ing, H. He, C. Leahy, K. McDonell, J. Phang *et al.*, “Gpt-neox- 20b: An open-source autoregressive language model,” *arXiv preprint arXiv:2204.06745*[, 2022.](#bookmark36) [15](#bookmark36)
101. R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim,

‌C. Hesse, S. Jain, V. Kosaraju, W. Saunders *et al.*, “Webgpt: Browser- assisted question-answering with human feedback,” *arXiv preprint arXiv:2112.09332*[, 2021.](#bookmark27) 11[,](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
102. N. Muennighoff, T. Wang, L. Sutawika, A. Roberts, S. Biderman,

‌T. L. Scao, M. S. Bari, S. Shen, Z.-X. Yong, H. Schoelkopf *et al.*, “Crosslingual generalization through multitask finetuning,” *arXiv preprint arXiv:2211.01786*[, 2022.](#bookmark36) 15[,](#bookmark54) [23](#bookmark54)
103. Z. Luo, C. Xu, P. Zhao, Q. Sun, X. Geng, W. Hu, C. Tao, J. Ma, Q. Lin,

‌and D. Jiang, “Wizardcoder: Empowering code large language models with evol-instruct,” *arXiv preprint arXiv:2306.08568*[, 2023.](#bookmark33) 14[,](#bookmark36) [15](#bookmark36)
104. A. Fan, Y. Jernite, E. Perez, D. Grangier, J. Weston, and M. Auli, “Eli5: Long form question answering,” *arXiv preprint arXiv:1907.09190*[, 2019.](#bookmark27) 11[,](#bookmark31) 13[,](#bookmark54) [23](#bookmark54)
105. ‌S. Lin, J. Hilton, and O. Evans, “Truthfulqa: Measuring how models mimic human falsehoods,” *arXiv preprint arXiv:2109.07958*[, 2021.](#bookmark31) 13[,](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)‌
106. ‌Y. Wang, Y. Kordi, S. Mishra, A. Liu, N. A. Smith, D. Khashabi, and H. Hajishirzi, “Self-instruct: Aligning language model with self generated instructions,” *arXiv preprint arXiv:2212.10560*[, 2022.](#bookmark33) [14](#bookmark33)
107. ‌D. Yin, X. Liu, F. Yin, M. Zhong, H. Bansal, J. Han, and K.-W. Chang, “Dynosaur: A dynamic growth paradigm for instruction-tuning data curation,” *arXiv preprint arXiv:2305.14327*[, 2023.](#bookmark33) [14](#bookmark33)
108. P. Gao, J. Han, R. Zhang, Z. Lin, S. Geng, A. Zhou, W. Zhang, P. Lu,

‌C. He, X. Yue *et al.*, “Llama-adapter v2: Parameter-efficient visual instruction model,” *arXiv preprint arXiv:2304.15010*[, 2023.](#bookmark33) 14[,](#bookmark55) [24](#bookmark55)
109. [“Openai. gpt-4 technical report,” 2023.](#bookmark33) [14](#bookmark33)
110. ‌T. Liu and B. K. H. Low, “Goat: Fine-tuned llama outperforms gpt-4 on arithmetic tasks,” *arXiv preprint arXiv:2305.14201*[, 2023.](#bookmark33) [14](#bookmark33)
111. ‌H. Wang, C. Liu, N. Xi, Z. Qiang, S. Zhao, B. Qin, and T. Liu, “Huatuo: Tuning llama model with chinese medical knowledge,” *arXiv preprint arXiv:2304.06975*[, 2023.](#bookmark33) [14](#bookmark33)
112. C. Xu, Q. Sun, K. Zheng, X. Geng, P. Zhao, J. Feng, C. Tao, and

‌D. Jiang, “Wizardlm: Empowering large language models to follow complex instructions,” *arXiv preprint arXiv:2304.12244*[, 2023.](#bookmark33) 14[,](#bookmark36) [15](#bookmark36)
113. Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones,

‌A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon *et al.*, “Constitutional ai: Harmlessness from ai feedback,” *arXiv preprint arXiv:2212.08073*[, 2022.](#bookmark36) [15](#bookmark36)
114. ‌Z. Sun, Y. Shen, Q. Zhou, H. Zhang, Z. Chen, D. Cox, Y. Yang, and C. Gan, “Principle-driven self-alignment of language mod- els from scratch with minimal human supervision,” *arXiv preprint arXiv:2305.03047*[, 2023.](#bookmark36) [15](#bookmark36)
115. ‌B. Zhang and H. Soh, “Large language models as zero-shot human models for human-robot interaction,” *arXiv preprint arXiv:2303.03548*[, 2023.](#bookmark36) 15[,](#bookmark38) [16](#bookmark38)
116. ‌A. Lykov and D. Tsetserukou, “Llm-brain: Ai-driven fast generation of robot behaviour tree based on large language model,” *arXiv preprint arXiv:2305.19352*[, 2023.](#bookmark36) [15](#bookmark36)
117. ‌E. Billing, J. Rosén, and M. Lamb, “Language models for human-robot interaction,” in *ACM/IEEE International Conference on Human-Robot Interaction, March 13–16, 2023, Stockholm, Sweden*[. ACM Digital Library, 2023, pp. 905–906.](#bookmark36) [15](#bookmark36)
118. ‌Y. Ye, H. You, and J. Du, “Improved trust in human-robot collaboration with chatgpt,” *IEEE Access*[, 2023.](#bookmark36) [15](#bookmark36)
119. I. Singh, V. Blukis, A. Mousavian, A. Goyal, D. Xu, J. Tremblay,

D. Fox, J. Thomason, and A. Garg, “Progprompt: Generating situated robot task plans using large language models,” in *2023 IEEE Interna- tional Conference on Robotics and Automation (ICRA)*. IEEE, 2023,

[pp. 11 523–11 530.](#bookmark36) [15](#bookmark36)
120. ‌Y. Zhen, S. Bi, L. Xing-tong, P. Wei-qin, S. Hai-peng, C. Zi-rui, and F. Yi-shu, “Robot task planning based on large language model representing knowledge with directed graph structures,” *arXiv preprint arXiv:2306.05171*[, 2023.](#bookmark36) [15](#bookmark36)
121. ‌W. Huang, P. Abbeel, D. Pathak, and I. Mordatch, “Language models as zero-shot planners: Extracting actionable knowledge for embodied agents,” in *International Conference on Machine Learning*[. PMLR, 2022, pp. 9118–9147.](#bookmark36) [15](#bookmark36)
122. ‌Y. Ding, X. Zhang, C. Paxton, and S. Zhang, “Task and motion planning with large language models for object rearrangement,” *arXiv preprint arXiv:2303.06247*[, 2023.](#bookmark36) [15](#bookmark36)
123. ‌——, “Leveraging commonsense knowledge from large language mod- els for task and motion planning,” in *RSS 2023 Workshop on Learning for Task and Motion Planning*[, 2023.](#bookmark36) [15](#bookmark36)
124. ‌Y. Ge, W. Hua, J. Ji, J. Tan, S. Xu, and Y. Zhang, “Openagi: When llm meets domain experts,” *arXiv preprint arXiv:2304.04370*[, 2023.](#bookmark36) [15](#bookmark36)
125. T. Zhong, Y. Wei, L. Yang, Z. Wu, Z. Liu, X. Wei, W. Li, J. Yao,

‌C. Ma, X. Li *et al.*, “Chatabl: Abductive learning via natural language interaction with chatgpt,” *arXiv preprint arXiv:2304.11107*[, 2023.](#bookmark36) [15](#bookmark36)
126. J. Wu, R. Antonova, A. Kan, M. Lepert, A. Zeng, S. Song, J. Bohg,

‌S. Rusinkiewicz, and T. Funkhouser, “Tidybot: Personalized robot as- sistance with large language models,” *arXiv preprint arXiv:2305.05658*[, 2023.](#bookmark38) [16](#bookmark38)
127. D. Driess, F. Xia, M. S. Sajjadi, C. Lynch, A. Chowdhery, B. Ichter,

‌A. Wahid, J. Tompson, Q. Vuong, T. Yu *et al.*, “Palm-e: An embodied multimodal language model,” *arXiv preprint arXiv:2303.03378*[, 2023.](#bookmark38) [16](#bookmark38)
128. W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang, P. Florence, A. Zeng,

J. Tompson, I. Mordatch, Y. Chebotar, P. Sermanet, T. Jackson,

N. Brown, L. Luu, S. Levine, K. Hausman, and brian ichter, “Inner monologue: Embodied reasoning through planning with language

  


‌models,” in *6th Annual Conference on Robot Learning*[, 2022. [Online]. Available:](https://openreview.net/forum?id=3R3Pz5i0tye) [https://openreview.net/forum?id=3R3Pz5i0tye](#bookmark38) [16](#bookmark38)
129. ‌R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi, “Hel- laswag: Can a machine really finish your sentence?” *arXiv preprint arXiv:1905.07830*[, 2019.](#bookmark38) 16[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
130. ‌Y. Bisk, R. Zellers, J. Gao, Y. Choi *et al.*, “Piqa: Reasoning about physical commonsense in natural language,” in *Proceedings of the AAAI conference on artificial intelligence*[, vol. 34, no. 05, 2020, pp. 7432–7439.](#bookmark38) 16[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
131. ‌M. Joshi, E. Choi, D. S. Weld, and L. Zettlemoyer, “Triviaqa: A large scale distantly supervised challenge dataset for reading comprehen- sion,” *arXiv preprint arXiv:1705.03551*[, 2017.](#bookmark38) 16[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
132. D. Paperno, G. Kruszewski, A. Lazaridou, Q. N. Pham, R. Bernardi,

‌S. Pezzelle, M. Baroni, G. Boleda, and R. Fernández, “The lambada dataset: Word prediction requiring a broad discourse context,” *arXiv preprint arXiv:1606.06031*[, 2016.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
133. ‌K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi, “Winogrande: An adversarial winograd schema challenge at scale,” *Communications of the ACM*[, vol. 64, no. 9, pp. 99–106, 2021.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
134. ‌H. Levesque, E. Davis, and L. Morgenstern, “The winograd schema challenge,” in *Thirteenth international conference on the principles of knowledge representation and reasoning*[, 2012.](#bookmark45) 18[,](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
135. D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and

J. Steinhardt, “Measuring massive multitask language understanding,”

‌arXiv preprint arXiv:2009.03300[, 2020.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
136. ‌A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman, “Glue: A multi-task benchmark and analysis platform for natural language understanding,” *arXiv preprint arXiv:1804.07461*[, 2018.](#bookmark45) 18[,](#bookmark48) 20[,](#bookmark51) [21](#bookmark51)
137. ‌N. Mostafazadeh, N. Chambers, X. He, D. Parikh, D. Batra, L. Van- derwende, P. Kohli, and J. Allen, “A corpus and evaluation framework for deeper understanding of commonsense stories,” *arXiv preprint arXiv:1604.01696*[, 2016.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
138. C. Clark, K. Lee, M.-W. Chang, T. Kwiatkowski, M. Collins, and

‌K. Toutanova, “Boolq: Exploring the surprising difficulty of natural yes/no questions,” *arXiv preprint arXiv:1905.10044*[, 2019.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
139. ‌G. Lai, Q. Xie, H. Liu, Y. Yang, and E. Hovy, “Race: Large-scale reading comprehension dataset from examinations,” *arXiv preprint arXiv:1704.04683*[, 2017.](#bookmark45) 18[,](#bookmark48) 20[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
140. ‌Y. Nie, A. Williams, E. Dinan, M. Bansal, J. Weston, and D. Kiela, “Adversarial nli: A new benchmark for natural language understand- ing,” *arXiv preprint arXiv:1910.14599*[, 2019.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
141. ‌P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord, “Think you have solved question answering? try arc, the ai2 reasoning challenge,” *arXiv preprint arXiv:1803.05457*[, 2018.](#bookmark45) 18[,](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
142. A. Conneau, G. Lample, R. Rinott, A. Williams, S. R. Bowman,

‌H. Schwenk, and V. Stoyanov, “Xnli: Evaluating cross-lingual sentence representations,” *arXiv preprint arXiv:1809.05053*[, 2018.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
143. ‌A. Williams, N. Nangia, and S. Bowman, “A broad-coverage challenge corpus for sentence understanding through inference,” in *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)*[. New Orleans, Louisiana: Association for Computational Linguistics, Jun. 2018, pp. 1112–1122. [Online]. Available:](https://aclanthology.org/N18-1101) [https://aclanthology.org/N18-1101](#bookmark45) [18](#bookmark45)
144. ‌Y. Yang, Y. Zhang, C. Tar, and J. Baldridge, “Paws-x: A cross- lingual adversarial dataset for paraphrase identification,” *arXiv preprint arXiv:1908.11828*[, 2019.](#bookmark45) 18[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
145. Y. Zhang, J. Baldridge, and L. He, “PAWS: Paraphrase adversaries from word scrambling,” in *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*[. Minneapolis, Minnesota: Association for Computational Linguistics, Jun. 2019, pp. 1298–1308. [Online]. Available:](https://aclanthology.org/N19-1131) [https:](https://aclanthology.org/N19-1131)

[//aclanthology.org/N19-1131](#bookmark45) [18](#bookmark45)
146. ‌S. Reddy, D. Chen, and C. D. Manning, “Coqa: A conversational question answering challenge,” *Transactions of the Association for Computational Linguistics*[, vol. 7, pp. 249–266, 2019.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
147. ‌D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner, “Drop: A reading comprehension benchmark requiring discrete rea- soning over paragraphs,” *arXiv preprint arXiv:1903.00161*[, 2019.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
148. I. Dagan, O. Glickman, and B. Magnini, “The pascal recognising tex- tual entailment challenge,” in *Machine learning challenges workshop*[. Springer, 2005, pp. 177–190.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
149. ‌A. Srivastava, A. Rastogi, A. Rao, A. A. M. Shoeb, A. Abid, A. Fisch,

A. R. Brown, A. Santoro, A. Gupta, A. Garriga-Alonso *et al.*, “Beyond the imitation game: Quantifying and extrapolating the capabilities of language models,” *arXiv preprint arXiv:2206.04615*[, 2022.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22,

[23](#bookmark54)
150. ‌P. Rajpurkar, R. Jia, and P. Liang, “Know what you don’t know: Unanswerable questions for squad,” *arXiv preprint arXiv:1806.03822*[, 2018.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
151. ‌P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang, “Squad: 100,000+ questions for machine comprehension of text,” *arXiv preprint arXiv:1606.05250*[, 2016.](#bookmark47) 19[,](#bookmark51) [21](#bookmark51)
152. K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser,

‌M. Plappert, J. Tworek, J. Hilton, R. Nakano *et al.*, “Training verifiers to solve math word problems,” *arXiv preprint arXiv:2110.14168*[, 2021.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
153. ‌M. T. Pilehvar and J. Camacho-Collados, “Wic: 10,000 example pairs for evaluating context-sensitive representations,” *arXiv preprint arXiv:1808.09121*[, vol. 6, 2018.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
154. ‌Y. Wang, X. Liu, and S. Shi, “Deep neural solver for math word problems,” in *Proceedings of the 2017 conference on empirical methods in natural language processing*[, 2017, pp. 845–854.](#bookmark47) 19[,](#bookmark51) [21](#bookmark51)
155. ‌X. Liu, Q. Chen, C. Deng, H. Zeng, J. Chen, D. Li, and B. Tang, “Lcqmc: A large-scale chinese question matching corpus,” in *Proceed- ings of the 27th international conference on computational linguistics*[, 2018, pp. 1952–1962.](#bookmark47) 19[,](#bookmark51) [21](#bookmark51)
156. D. Hendrycks, S. Basart, S. Kadavath, M. Mazeika, A. Arora, E. Guo,

‌C. Burns, S. Puranik, H. He, D. Song *et al.*, “Measuring coding challenge competence with apps,” *arXiv preprint arXiv:2105.09938*[, 2021.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
157. ‌I. Mollas, Z. Chrysopoulou, S. Karlos, and G. Tsoumakas, “Ethos: an online hate speech detection dataset,” *arXiv preprint arXiv:2006.08328*[, 2020.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
158. ‌M. Nadeem, A. Bethke, and S. Reddy, “Stereoset: Measuring stereotypical bias in pretrained language models,” *arXiv preprint arXiv:2004.09456*[, 2020.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
159. M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan,

‌H. Edwards, Y. Burda, N. Joseph, G. Brockman *et al.*, “Evaluating large language models trained on code,” *arXiv preprint arXiv:2107.03374*[, 2021.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
160. ‌Y. Chang, M. Narang, H. Suzuki, G. Cao, J. Gao, and Y. Bisk, “We- bqa: Multihop and multimodal qa,” in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*[, 2022, pp. 16 495–16 504.](#bookmark47) 19[,](#bookmark51) [21](#bookmark51)
161. ‌Y. Cui, T. Liu, W. Che, L. Xiao, Z. Chen, W. Ma, S. Wang, and G. Hu, “A span-extraction dataset for chinese machine reading comprehen- sion,” *arXiv preprint arXiv:1810.07366*[, 2018.](#bookmark47) 19[,](#bookmark51) [21](#bookmark51)
162. ‌S. Merity, C. Xiong, J. Bradbury, and R. Socher, “Pointer sentinel mixture models,” *arXiv preprint arXiv:1609.07843*[, 2016.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
163. ‌J. W. Rae, A. Potapenko, S. M. Jayakumar, and T. P. Lillicrap, “Compressive transformers for long-range sequence modelling,” *arXiv preprint arXiv:1911.05507*[, 2019.](#bookmark47) 19[,](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
164. E. Choi, H. He, M. Iyyer, M. Yatskar, W.-t. Yih, Y. Choi, P. Liang, and

‌L. Zettlemoyer, “Quac: Question answering in context,” *arXiv preprint arXiv:1808.07036*[, 2018.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
165. ‌E. M. Ponti, G. Glavaš, O. Majewska, Q. Liu, I. Vulic´, and A. Korho- nen, “Xcopa: A multilingual dataset for causal commonsense reason- ing,” *arXiv preprint arXiv:2005.00333*[, 2020.](#bookmark47) 19[,](#bookmark52) [22](#bookmark52)
166. ‌M. Geva, D. Khashabi, E. Segal, T. Khot, D. Roth, and J. Berant, “Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies,” *Transactions of the Association for Computational Linguistics*[, vol. 9, pp. 346–361, 2021.](#bookmark48) 20[,](#bookmark52) [22](#bookmark52)
167. ‌A. Talmor, J. Herzig, N. Lourie, and J. Berant, “Commonsenseqa: A question answering challenge targeting commonsense knowledge,” *arXiv preprint arXiv:1811.00937*[, 2018.](#bookmark48) 20[,](#bookmark52) [22](#bookmark52)
168. [S. Iyer, N. Dandekar, and K. Csernai, “First quora dataset release: Question pairs,”](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs) [https://quoradata.quora.com/](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs) First-Quora-Dataset-Release-Question-Pairs[.](#bookmark51) [21](#bookmark51)
169. ‌A. Williams, N. Nangia, and S. R. Bowman, “A broad-coverage challenge corpus for sentence understanding through inference,” *arXiv preprint arXiv:1704.05426*[, 2017.](#bookmark51) [21](#bookmark51)
170. M.-C. De Marneffe, M. Simons, and J. Tonhauser, “The commit- mentbank: Investigating projection in naturally occurring discourse,” in *proceedings of Sinn und Bedeutung*, vol. 23, no. 2, 2019, pp. 107–

[124.](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
171. O. Bojar, R. Chatterjee, C. Federmann, Y. Graham, B. Haddow,

M. Huck, A. J. Yepes, P. Koehn, V. Logacheva, C. Monz *et al.*, “Find- ings of the 2016 conference on machine translation,” in *Proceedings of*

  


the First Conference on Machine Translation: Volume 2, Shared Task Papers[, 2016, pp. 131–198.](#bookmark51) [21](#bookmark51)
172. ‌X. Pan, B. Zhang, J. May, J. Nothman, K. Knight, and H. Ji, “Cross- lingual name tagging and linking for 282 languages,” in *Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*[, 2017, pp. 1946–1958.](#bookmark51) [21](#bookmark51)
173. ‌P. Lewis, B. Og˘uz, R. Rinott, S. Riedel, and H. Schwenk, “Mlqa: Evaluating cross-lingual extractive question answering,” *arXiv preprint arXiv:1910.07475*[, 2019.](#bookmark51) [21](#bookmark51)‌
174. ‌J. H. Clark, E. Choi, M. Collins, D. Garrette, T. Kwiatkowski, V. Niko- laev, and J. Palomaki, “Tydi qa: A benchmark for information-seeking question answering in typologically diverse languages,” *Transactions of the Association for Computational Linguistics*[, vol. 8, pp. 454–470, 2020.](#bookmark51) 21[,](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
175. W. Li, F. Qi, M. Sun, X. Yi, and J. Zhang, “Ccpm: A chinese classical poetry matching dataset,” *arXiv preprint arXiv:2106.01979*[, 2021.](#bookmark51) [21](#bookmark51)
176. ‌K. Sun, D. Yu, D. Yu, and C. Cardie, “Investigating prior knowledge for challenging chinese machine reading comprehension,” *Transactions of the Association for Computational Linguistics*[, vol. 8, pp. 141–155, 2020.](#bookmark51) [21](#bookmark51)‌
177. B. Loïc, B. Magdalena, B. Ondˇrej, F. Christian, G. Yvette, G. Roman,

H. Barry, H. Matthias, J. Eric, K. Tom *et al.*, “Findings of the 2020 conference on machine translation (wmt20),” in *Proceedings of the Fifth Conference on Machine Translation*[. Association for Computational Linguistics„ 2020, pp. 1–55.](#bookmark51) [21](#bookmark51)
178. ‌B. Hu, Q. Chen, and F. Zhu, “Lcsts: A large scale chinese short text summarization dataset,” *arXiv preprint arXiv:1506.05865*[, 2015.](#bookmark51) [21](#bookmark51)
179. ‌Z. Shao, M. Huang, J. Wen, W. Xu, and X. Zhu, “Long and diverse text generation with planning-based hierarchical variational model,” *arXiv preprint arXiv:1908.06605*[, 2019.](#bookmark51) [21](#bookmark51)
180. ‌Y. Yao, Q. Dong, J. Guan, B. Cao, Z. Zhang, C. Xiao, X. Wang, F. Qi,

‌J. Bao, J. Nie *et al.*, “Cuge: A chinese language understanding and generation evaluation benchmark,” *arXiv preprint arXiv:2112.13610*[, 2021.](#bookmark51) [21](#bookmark51)
181. Y. Li, T. Liu, D. Li, Q. Li, J. Shi, and Y. Wang, “Character-based bilstm-crf incorporating pos and dictionaries for chinese opinion target extraction,” in *Asian Conference on Machine Learning*. PMLR, 2018,

[pp. 518–533.](#bookmark51) [21](#bookmark51)
182. ‌L. Xu, H. Hu, X. Zhang, L. Li, C. Cao, Y. Li, Y. Xu, K. Sun, D. Yu,

C. Yu *et al.*, “Clue: A chinese language understanding evaluation benchmark,” *arXiv preprint arXiv:2004.05986*[, 2020.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
183. ‌Z. Li, N. Ding, Z. Liu, H. Zheng, and Y. Shen, “Chinese relation extrac- tion with multi-grained information and external linguistic knowledge,” in *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*[, 2019, pp. 4377–4386.](#bookmark51) [21](#bookmark51)
184. ‌J. Xu, J. Wen, X. Sun, and Q. Su, “A discourse-level named entity recognition and relation extraction dataset for chinese literature text,” *arXiv preprint arXiv:1711.07010*[, 2017.](#bookmark51) [21](#bookmark51)
185. ‌J. Chen, Q. Chen, X. Liu, H. Yang, D. Lu, and B. Tang, “The bq corpus: A large-scale domain-specific chinese corpus for sentence semantic equivalence identification,” in *Proceedings of the 2018 conference on empirical methods in natural language processing*[, 2018, pp. 4946– 4951.](#bookmark51) [21](#bookmark51)‌
186. [L. CO, “Iflytek: a multiple categories chinese text classifier. competi- tion official website,” 2019.](#bookmark51) [21](#bookmark51)
187. B. Liu, D. Niu, H. Wei, J. Lin, Y. He, K. Lai, and Y. Xu, “Matching article pairs with graphical decomposition and convolutions,” *arXiv preprint arXiv:1802.07459*[, 2018.](#bookmark51) [21](#bookmark51)
188. ‌S. Zhang, X. Zhang, H. Wang, J. Cheng, P. Li, and Z. Ding, “Chinese medical question answer matching using end-to-end character-level multi-scale cnns,” *Applied Sciences*[, vol. 7, no. 8, p. 767, 2017.](#bookmark51) [21](#bookmark51)
189. ‌S. Zhang, X. Zhang, H. Wang, L. Guo, and S. Liu, “Multi-scale attentive interaction networks for chinese medical question answer selection,” *IEEE Access*[, vol. 6, pp. 74 061–74 071, 2018.](#bookmark51) [21](#bookmark51)
190. ‌P. Li, W. Li, Z. He, X. Wang, Y. Cao, J. Zhou, and W. Xu, “Dataset and neural recurrent sequence labeling model for open-domain factoid question answering,” *arXiv preprint arXiv:1607.06275*[, 2016.](#bookmark51) [21](#bookmark51)
191. ‌N. Peng and M. Dredze, “Named entity recognition for chinese social media with jointly trained embeddings,” in *Proceedings of the 2015 conference on empirical methods in natural language processing*, 2015,

[pp. 548–554.](#bookmark51) [21](#bookmark51)
192. ‌R. Weischedel, S. Pradhan, L. Ramshaw, M. Palmer, N. Xue, M. Mar- cus, A. Taylor, C. Greenberg, E. Hovy, R. Belvin *et al.*, “Ontonotes release 4.0,” *LDC2011T03, Philadelphia, Penn.: Linguistic Data Con- sortium*[, 2011.](#bookmark51) [21](#bookmark51)
193. ‌Y. Cui, T. Liu, Z. Yang, Z. Chen, W. Ma, W. Che, S. Wang, and G. Hu, “A sentence cloze dataset for chinese machine reading comprehension,” *arXiv preprint arXiv:2004.03116*[, 2020.](#bookmark51) [21](#bookmark51)‌
194. ‌C. C. Shao, T. Liu, Y. Lai, Y. Tseng, and S. Tsai, “Drcd: A chinese machine reading comprehension dataset,” *arXiv preprint arXiv:1806.00920*[, 2018.](#bookmark51) [21](#bookmark51)
195. W. He, K. Liu, J. Liu, Y. Lyu, S. Zhao, X. Xiao, Y. Liu, Y. Wang,

‌H. Wu, Q. She *et al.*, “Dureader: a chinese machine reading comprehension dataset from real-world applications,” *arXiv preprint arXiv:1711.05073*[, 2017.](#bookmark51) [21](#bookmark51)
196. ‌H. Tang, J. Liu, H. Li, Y. Hong, H. Wu, and H. Wang, “Dureaderrobust: A chinese dataset towards evaluating the robustness of machine reading comprehension models,” *arXiv preprint arXiv:2004.11142*[, 2020.](#bookmark51) [21](#bookmark51)
197. ‌C. Zheng, M. Huang, and A. Sun, “Chid: A large-scale chinese idiom dataset for cloze test,” *arXiv preprint arXiv:1906.01265*[, 2019.](#bookmark51) [21](#bookmark51)
198. C. Xiao, H. Zhong, Z. Guo, C. Tu, Z. Liu, M. Sun, Y. Feng, X. Han,

‌Z. Hu, H. Wang *et al.*, “Cail2018: A large-scale legal dataset for judgment prediction,” *arXiv preprint arXiv:1807.02478*[, 2018.](#bookmark51) [21](#bookmark51)
199. ‌C. Xu, W. Zhou, T. Ge, K. Xu, J. McAuley, and F. Wei, “Blow the dog whistle: A chinese dataset for cant understanding with common sense and world knowledge,” *arXiv preprint arXiv:2104.02704*[, 2021.](#bookmark51) [21](#bookmark51)
200. ‌C. Xiong, Z. Dai, J. Callan, Z. Liu, and R. Power, “End-to-end neural ad-hoc ranking with kernel pooling,” in *Proceedings of the 40th International ACM SIGIR conference on research and development in information retrieval*[, 2017, pp. 55–64.](#bookmark51) [21](#bookmark51)
201. ‌C. Xu, J. Pei, H. Wu, Y. Liu, and C. Li, “Matinf: A jointly labeled large- scale dataset for classification, question answering and summarization,” *arXiv preprint arXiv:2004.12302*[, 2020.](#bookmark51) [21](#bookmark51)
202. ‌H. Zhou, C. Zheng, K. Huang, M. Huang, and X. Zhu, “Kdconv: A chinese multi-domain dialogue dataset towards multi-turn knowledge- driven conversation,” *arXiv preprint arXiv:2004.04100*[, 2020.](#bookmark51) [21](#bookmark51)
203. L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster,

‌J. Phang, H. He, A. Thite, N. Nabeshima *et al.*, “The pile: An 800gb dataset of diverse text for language modeling,” *arXiv preprint arXiv:2101.00027*[, 2020.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
204. ‌S. Lim, M. Kim, and J. Lee, “Korquad1. 0: Korean qa dataset for machine reading comprehension,” *arXiv preprint arXiv:1909.07005*[, 2019.](#bookmark51) [21](#bookmark51)
205. S. Park, J. Moon, S. Kim, W. I. Cho, J. Han, J. Park, C. Song,

‌J. Kim, Y. Song, T. Oh *et al.*, “Klue: Korean language understanding evaluation,” *arXiv preprint arXiv:2105.09680*[, 2021.](#bookmark51) [21](#bookmark51)
206. L. Xu, X. Lu, C. Yuan, X. Zhang, H. Xu, H. Yuan, G. Wei, X. Pan,

‌X. Tian, L. Qin *et al.*, “Fewclue: A chinese few-shot learning evaluation benchmark,” *arXiv preprint arXiv:2107.07498*[, 2021.](#bookmark51) [21](#bookmark51)
207. T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh,

‌C. Alberti, D. Epstein, I. Polosukhin, J. Devlin, K. Lee *et al.*, “Natural questions: a benchmark for question answering research,” *Transactions of the Association for Computational Linguistics*[, vol. 7, pp. 453–466, 2019.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
208. ‌J. Thorne, A. Vlachos, C. Christodoulopoulos, and A. Mittal, “Fever: a large-scale dataset for fact extraction and verification,” *arXiv preprint arXiv:1803.05355*[, 2018.](#bookmark51) [21](#bookmark51)
209. I. Augenstein, C. Lioma, D. Wang, L. C. Lima, C. Hansen,

‌C. Hansen, and J. G. Simonsen, “Multifc: A real-world multi-domain dataset for evidence-based fact checking of claims,” *arXiv preprint arXiv:1909.03242*[, 2019.](#bookmark51) [21](#bookmark51)
210. ‌M. Sap, H. Rashkin, D. Chen, R. LeBras, and Y. Choi, “Socialiqa: Commonsense reasoning about social interactions,” *arXiv preprint arXiv:1904.09728*[, 2019.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
211. ‌S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith, “Realtoxicityprompts: Evaluating neural toxic degeneration in language models,” *arXiv preprint arXiv:2009.11462*[, 2020.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
212. ‌S. L. Blodgett, L. Green, and B. O’Connor, “Demographic dialectal variation in social media: A case study of african-american english,” *arXiv preprint arXiv:1608.08868*[, 2016.](#bookmark51) [21](#bookmark51)
213. ‌D. Borkan, L. Dixon, J. Sorensen, N. Thain, and L. Vasserman, “Nuanced metrics for measuring unintended bias with real data for text classification,” in *Companion proceedings of the 2019 world wide web conference*[, 2019, pp. 491–500.](#bookmark51) [21](#bookmark51)
214. ‌Y. Cui, T. Liu, Z. Chen, W. Ma, S. Wang, and G. Hu, “Dataset for the first evaluation on chinese machine reading comprehension,” *arXiv preprint arXiv:1709.08299*[, 2017.](#bookmark51) [21](#bookmark51)
215. ‌D. Vilares and C. Gómez-Rodríguez, “Head-qa: A healthcare dataset for complex reasoning,” *arXiv preprint arXiv:1906.04701*[, 2019.](#bookmark51) [21](#bookmark51)
216. J. Liu, L. Cui, H. Liu, D. Huang, Y. Wang, and Y. Zhang, “Logiqa: A challenge dataset for machine reading comprehension with logical reasoning,” *arXiv preprint arXiv:2007.08124*[, 2020.](#bookmark51) [21](#bookmark51)
217. ‌T. Mihaylov, P. Clark, T. Khot, and A. Sabharwal, “Can a suit of armor conduct electricity? a new dataset for open book question answering,” *arXiv preprint arXiv:1809.02789*[, 2018.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)‌
218. ‌S. Aroca-Ouellette, C. Paik, A. Roncone, and K. Kann, “Prost: Phys- ical reasoning of objects through space and time,” *arXiv preprint arXiv:2106.03634*[, 2021.](#bookmark51) [21](#bookmark51)
219. A. Peñas, E. Hovy, P. Forner, Á. Rodrigo, R. Sutcliffe, and R. Morante, “Qa4mre 2011-2013: Overview of question answering for machine reading evaluation,” in *Information Access Evaluation. Multilinguality, Multimodality, and Visualization: 4th International Conference of the CLEF Initiative, CLEF 2013, Valencia, Spain, September 23-26, 2013.*

‌Proceedings 4[. Springer, 2013, pp. 303–320.](#bookmark51) [21](#bookmark51)
220. ‌J. Welbl, N. F. Liu, and M. Gardner, “Crowdsourcing multiple choice science questions,” *arXiv preprint arXiv:1707.06209*[, 2017.](#bookmark51) [21](#bookmark51)
221. Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis,

‌L. Zettlemoyer, and V. Stoyanov, “Roberta: A robustly optimized bert pretraining approach,” *arXiv preprint arXiv:1907.11692*[, 2019.](#bookmark51) [21](#bookmark51)
222. ‌J. Baumgartner, S. Zannettou, B. Keegan, M. Squire, and J. Blackburn, “The pushshift reddit dataset,” in *Proceedings of the international AAAI conference on web and social media*[, vol. 14, 2020, pp. 830–839.](#bookmark51) [21](#bookmark51)
223. ‌E. Dinan, S. Roller, K. Shuster, A. Fan, M. Auli, and J. Weston, “Wizard of wikipedia: Knowledge-powered conversational agents,” *arXiv preprint arXiv:1811.01241*[, 2018.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
224. ‌H. Rashkin, E. M. Smith, M. Li, and Y.-L. Boureau, “Towards empathetic open-domain conversation models: A new benchmark and dataset,” *arXiv preprint arXiv:1811.00207*[, 2018.](#bookmark51) [21](#bookmark51)
225. E. Dinan, V. Logacheva, V. Malykh, A. Miller, K. Shuster, J. Ur- banek, D. Kiela, A. Szlam, I. Serban, R. Lowe *et al.*, “The second conversational intelligence challenge (convai2),” in *The NeurIPS’18 Competition: From Machine Learning to Intelligent Conversations*.

[Springer, 2020, pp. 187–208.](#bookmark51) [21](#bookmark51)
226. ‌E. M. Smith, M. Williamson, K. Shuster, J. Weston, and Y.-L. Boureau, “Can you put it all together: Evaluating conversational agents’ ability to blend skills,” *arXiv preprint arXiv:2004.08449*[, 2020.](#bookmark51) [21](#bookmark51)
227. ‌M. Komeili, K. Shuster, and J. Weston, “Internet-augmented dialogue generation,” *arXiv preprint arXiv:2107.07566*[, 2021.](#bookmark51) [21](#bookmark51)
228. ‌N. Nangia, C. Vania, R. Bhalerao, and S. R. Bowman, “Crows-pairs: A challenge dataset for measuring social biases in masked language models,” *arXiv preprint arXiv:2010.00133*[, 2020.](#bookmark51) 21[,](#bookmark52) [22](#bookmark52)
229. H. Laurençon, L. Saulnier, T. Wang, C. Akiki, A. Villanova del Moral,

T. Le Scao, L. Von Werra, C. Mou, E. González Ponferrada, H. Nguyen *et al.*, “The bigscience roots corpus: A 1.6 tb composite multilingual dataset,” *Advances in Neural Information Processing Systems*, vol. 35,

[pp. 31 809–31 826, 2022.](#bookmark52) [22](#bookmark52)
230. D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang,

‌D. Song, and J. Steinhardt, “Measuring mathematical problem solving with the math dataset,” *arXiv preprint arXiv:2103.03874*[, 2021.](#bookmark52) [22](#bookmark52)
231. ‌M. Roemmele, C. A. Bejan, and A. S. Gordon, “Choice of plausible alternatives: An evaluation of commonsense causal reasoning.” in *AAAI spring symposium: logical formalizations of commonsense reasoning*[, 2011, pp. 90–95.](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
232. ‌D. Khashabi, S. Chaturvedi, M. Roth, S. Upadhyay, and D. Roth, “Looking beyond the surface: A challenge set for reading comprehen- sion over multiple sentences,” in *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)*[, 2018, pp. 252–262.](#bookmark52) [22](#bookmark52)
233. ‌S. Zhang, X. Liu, J. Liu, J. Gao, K. Duh, and B. Van Durme, “Record: Bridging the gap between human and machine commonsense reading comprehension,” *arXiv preprint arXiv:1810.12885*[, 2018.](#bookmark52) [22](#bookmark52)
234. ‌T. H. Trinh and Q. V. Le, “A simple method for commonsense reasoning,” *arXiv preprint arXiv:1806.02847*[, 2018.](#bookmark52) [22](#bookmark52)
235. ‌R. Zellers, A. Holtzman, H. Rashkin, Y. Bisk, A. Farhadi, F. Roesner, and Y. Choi, “Defending against neural fake news,” *Advances in neural information processing systems*[, vol. 32, 2019.](#bookmark52) [22](#bookmark52)
236. ‌R. T. McCoy, E. Pavlick, and T. Linzen, “Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference,” *arXiv preprint arXiv:1902.01007*[, 2019.](#bookmark52) [22](#bookmark52)
237. [M. Mirzayanov, “Codeforces: Results of 2020,”](https://codeforces.com/blog/entry/89502) [https://codeforces.com/](https://codeforces.com/blog/entry/89502) blog/entry/89502[.](#bookmark52) [22](#bookmark52)
238. E. Caballero, . OpenAI, and I. Sutskever, “Description2Code Dataset,”

[8 2016. [Online]. Available:](https://github.com/ethancaballero/description2code) [https://github.com/ethancaballero/](https://github.com/ethancaballero/description2code)

[description2code](#bookmark52) [22](#bookmark52)
239. R. Puri, D. S. Kung, G. Janssen, W. Zhang, G. Domeniconi, V. Zolotov,

J. Dolby, J. Chen, M. Choudhury, L. Decker *et al.*, “Codenet: A large- scale ai for code dataset for learning a diversity of coding tasks,” *arXiv preprint arXiv:2105.12655*[, 2021.](#bookmark52) [22](#bookmark52)
240. ‌J. Berant, A. Chou, R. Frostig, and P. Liang, “Semantic parsing on freebase from question-answer pairs,” in *Proceedings of the 2013 conference on empirical methods in natural language processing*, 2013,

[pp. 1533–1544.](#bookmark52) [22](#bookmark52)
241. ‌A. Patel, S. Bhattamishra, and N. Goyal, “Are nlp models really able to solve simple math word problems?” *arXiv preprint arXiv:2103.07191*[, 2021.](#bookmark52) [22](#bookmark52)
242. ‌R. Koncel-Kedziorski, S. Roy, A. Amini, N. Kushman, and H. Ha- jishirzi, “Mawps: A math word problem repository,” in *Proceedings of the 2016 conference of the north american chapter of the association for computational linguistics: human language technologies*[, 2016, pp. 1152–1157.](#bookmark52) [22](#bookmark52)
243. ‌W. Ling, D. Yogatama, C. Dyer, and P. Blunsom, “Program induction by rationale generation: Learning to solve and explain algebraic word problems,” *arXiv preprint arXiv:1705.04146*[, 2017.](#bookmark52) [22](#bookmark52)
244. ‌T. Scialom, P.-A. Dray, S. Lamprier, B. Piwowarski, and J. Sta- iano, “Mlsum: The multilingual summarization corpus,” *arXiv preprint arXiv:2004.14900*[, 2020.](#bookmark52) [22](#bookmark52)
245. ‌S. Narayan, S. B. Cohen, and M. Lapata, “Don’t give me the details, just the summary!” *Topic-Aware Convolutional Neural Networks for Extreme Summarization. ArXiv, abs*[, 1808.](#bookmark52) [22](#bookmark52)
246. ‌J. Novikova, O. Dušek, and V. Rieser, “The e2e dataset: New challenges for end-to-end generation,” *arXiv preprint arXiv:1706.09254*[, 2017.](#bookmark52) [22](#bookmark52)
247. T. C. Ferreira, C. Gardent, N. Ilinykh, C. Van Der Lee, S. Mille,

‌D. Moussallem, and A. Shimorina, “The 2020 bilingual, bi-directional webnlg+ shared task overview and evaluation results (webnlg+ 2020),” in *Proceedings of the 3rd International Workshop on Natural Language Generation from the Semantic Web (WebNLG+)*[, 2020.](#bookmark52) [22](#bookmark52)
248. N. Goyal, C. Gao, V. Chaudhary, P.-J. Chen, G. Wenzek, D. Ju, S. Kr- ishnan, M. Ranzato, F. Guzmán, and A. Fan, “The flores-101 evaluation benchmark for low-resource and multilingual machine translation,” *Transactions of the Association for Computational Linguistics*, vol. 10,

[pp. 522–538, 2022.](#bookmark52) [22](#bookmark52)
249. Y. Xia, X. Tan, F. Tian, F. Gao, W. Chen, Y. Fan, L. Gong, Y. Leng,

R. Luo, Y. Wang *et al.*, “Microsoft research asia’s systems for wmt19,”

‌arXiv preprint arXiv:1911.06191[, 2019.](#bookmark52) [22](#bookmark52)
250. ‌A. Tikhonov and M. Ryabinin, “It’s all in the heads: Using attention heads as a baseline for cross-lingual transfer in commonsense reason- ing,” *arXiv preprint arXiv:2106.12066*[, 2021.](#bookmark52) [22](#bookmark52)
251. ‌S. Roy and D. Roth, “Solving general arithmetic word problems,” *arXiv preprint arXiv:1608.01413*[, 2016.](#bookmark52) [22](#bookmark52)
252. J. Menick, M. Trebacz, V. Mikulik, J. Aslanides, F. Song, M. Chadwick,

‌M. Glaese, S. Young, L. Campbell-Gillingham, G. Irving *et al.*, “Teaching language models to support answers with verified quotes,” *arXiv preprint arXiv:2203.11147*[, 2022.](#bookmark52) [22](#bookmark52)
253. ‌R. Rudinger, J. Naradowsky, B. Leonard, and B. Van Durme, “Gender bias in coreference resolution,” *arXiv preprint arXiv:1804.09301*[, 2018.](#bookmark52) [22](#bookmark52)
254. ‌J. Zhao, T. Wang, M. Yatskar, V. Ordonez, and K.-W. Chang, “Gender bias in coreference resolution: Evaluation and debiasing methods,” *arXiv preprint arXiv:1804.06876*[, 2018.](#bookmark52) [22](#bookmark52)
255. ‌A. Parrish, A. Chen, N. Nangia, V. Padmakumar, J. Phang, J. Thomp- son, P. M. Htut, and S. R. Bowman, “Bbq: A hand-built bias benchmark for question answering,” *arXiv preprint arXiv:2110.08193*[, 2021.](#bookmark52) [22](#bookmark52)
256. ‌J. Boyd-Graber, B. Satinoff, H. He, and H. Daumé III, “Besting the quiz master: Crowdsourcing incremental classification games,” in *Proceedings of the 2012 joint conference on empirical methods in natural language processing and computational natural language learning*[, 2012, pp. 1290–1301.](#bookmark52) [22](#bookmark52)
257. ‌F. Shi, M. Suzgun, M. Freitag, X. Wang, S. Srivats, S. Vosoughi, H. W. Chung, Y. Tay, S. Ruder, D. Zhou *et al.*, “Language models are multi- lingual chain-of-thought reasoners,” *arXiv preprint arXiv:2210.03057*[, 2022.](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
258. ‌S.-Y. Miao, C.-C. Liang, and K.-Y. Su, “A diverse corpus for evaluating and developing english math word problem solvers,” *arXiv preprint arXiv:2106.15772*[, 2021.](#bookmark52) [22](#bookmark52)
259. J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan,

‌E. Jiang, C. Cai, M. Terry, Q. Le *et al.*, “Program synthesis with large language models,” *arXiv preprint arXiv:2108.07732*[, 2021.](#bookmark52) 22[,](#bookmark54) [23](#bookmark54)
260. ‌H. Husain, H. Wu, T. Gazit, M. Allamanis, and M. Brockschmidt, “Codesearchnet challenge: Evaluating the state of semantic code search,” *CoRR*[, vol. abs/1909.09436, 2019.](#bookmark52) [22](#bookmark52)
261. J. Austin, A. Odena, M. I. Nye, M. Bosma, H. Michalewski, D. Dohan,

E. Jiang, C. J. Cai, M. Terry, Q. V. Le, and C. Sutton, “Program synthesis with large language models,” *CoRR*[, vol. abs/2108.07732, 2021.](#bookmark52) [22](#bookmark52)
262. ‌D. Kocetkov, R. Li, L. B. Allal, J. Li, C. Mou, C. M. Ferrandis,

‌Y. Jernite, M. Mitchell, S. Hughes, T. Wolf *et al.*, “The stack: 3 tb of permissively licensed source code,” *arXiv preprint arXiv:2211.15533*[, 2022.](#bookmark52) [22](#bookmark52)
263. Y. Lai, C. Li, Y. Wang, T. Zhang, R. Zhong, L. Zettlemoyer, W.-

t. Yih, D. Fried, S. Wang, and T. Yu, “Ds-1000: A natural and reliable benchmark for data science code generation,” in *International Conference on Machine Learning*. PMLR, 2023, pp. 18 319–18 345.

‌22[,](#bookmark54) [23](#bookmark54)
264. P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga,

‌Y. Zhang, D. Narayanan, Y. Wu, A. Kumar *et al.*, “Holistic evaluation of language models,” *arXiv preprint arXiv:2211.09110*[, 2022.](#bookmark52) [22](#bookmark52)
265. Y. Wang, S. Mishra, P. Alipoormolabashi, Y. Kordi, A. Mirzaei,

‌A. Arunkumar, A. Ashok, A. S. Dhanasekaran, A. Naik, D. Stap *et al.*, “Benchmarking generalization via in-context instructions on 1,600+ language tasks,” *arXiv preprint arXiv:2204.07705*[, 2022.](#bookmark54) [23](#bookmark54)
266. T. Xie, C. H. Wu, P. Shi, R. Zhong, T. Scholak, M. Yasunaga, C.-

‌S. Wu, M. Zhong, P. Yin, S. I. Wang *et al.*, “Unifiedskg: Unifying and multi-tasking structured knowledge grounding with text-to-text language models,” *arXiv preprint arXiv:2201.05966*[, 2022.](#bookmark54) [23](#bookmark54)
267. ‌Q. Ye, B. Y. Lin, and X. Ren, “Crossfit: A few-shot learning challenge for cross-task generalization in nlp,” *arXiv preprint arXiv:2104.08835*[, 2021.](#bookmark54) [23](#bookmark54)
268. ‌V. Aribandi, Y. Tay, T. Schuster, J. Rao, H. S. Zheng, S. V. Mehta, H. Zhuang, V. Q. Tran, D. Bahri, J. Ni *et al.*, “Ext5: To- wards extreme multi-task scaling for transfer learning,” *arXiv preprint arXiv:2111.10952*[, 2021.](#bookmark54) [23](#bookmark54)
269. ‌N. Alex, E. Lifland, L. Tunstall, A. Thakur, P. Maham, C. J. Riedel, E. Hine, C. Ashurst, P. Sedille, A. Carlier *et al.*, “Raft: A real-world few-shot text classification benchmark,” *arXiv preprint arXiv:2109.14076*[, 2021.](#bookmark54) [23](#bookmark54)
270. P. Micikevicius, S. Narang, J. Alben, G. Diamos, E. Elsen, D. Garcia,

‌B. Ginsburg, M. Houston, O. Kuchaiev, G. Venkatesh *et al.*, “Mixed precision training,” *arXiv preprint arXiv:1710.03740*[, 2017.](#bookmark48) [20](#bookmark48)
271. ‌T. Q. Nguyen and J. Salazar, “Transformers without tears: Improving the normalization of self-attention,” *CoRR*[, vol. abs/1910.05895, 2019.](#bookmark48) 20[,](#bookmark54) [23](#bookmark54)
272. ‌Y. Wolf, N. Wies, Y. Levine, and A. Shashua, “Fundamental lim- itations of alignment in large language models,” *arXiv preprint arXiv:2304.11082*[, 2023.](#bookmark54) [23](#bookmark54)
273. Y. Dubois, X. Li, R. Taori, T. Zhang, I. Gulrajani, J. Ba, C. Guestrin,

‌P. Liang, and T. B. Hashimoto, “Alpacafarm: A simulation frame- work for methods that learn from human feedback,” *arXiv preprint arXiv:2305.14387*[, 2023.](#bookmark54) [23](#bookmark54)
274. ‌S. Kim, S. Bae, J. Shin, S. Kang, D. Kwak, K. M. Yoo, and M. Seo, “Aligning large language models through synthetic feedback,” *arXiv preprint arXiv:2305.13735*[, 2023.](#bookmark54) [23](#bookmark54)
275. ‌Z. Sun, Y. Shen, Q. Zhou, H. Zhang, Z. Chen, D. Cox, Y. Yang, and C. Gan, “Principle-driven self-alignment of language mod- els from scratch with minimal human supervision,” *arXiv preprint arXiv:2305.03047*[, 2023.](#bookmark54) [23](#bookmark54)
276. ‌K. Yang, D. Klein, A. Celikyilmaz, N. Peng, and Y. Tian, “Rlcd: Reinforcement learning from contrast distillation for language model alignment,” *arXiv preprint arXiv:2307.12950*[, 2023.](#bookmark54) [23](#bookmark54)
277. L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin,

C. Zhang, S. Agarwal, K. Slama, A. Ray *et al.*, “Training language models to follow instructions with human feedback,” *Advances in Neural Information Processing Systems*, vol. 35, pp. 27 730–27 744,

[2022.](#bookmark54) [23](#bookmark54)
278. Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis,

L. Zettlemoyer, and V. Stoyanov, “Roberta: A robustly optimized bert pretraining approach,” *arXiv preprint arXiv:1907.11692*[, 2019.](#bookmark55) [24](#bookmark55)