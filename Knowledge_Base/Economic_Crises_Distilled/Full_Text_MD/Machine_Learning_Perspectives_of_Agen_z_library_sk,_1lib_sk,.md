Pedro Campos
Anand Rao
Joaquim Margarido Editors
Machine Learning
Perspectives
of Agent-Based
Models
Practical Applications to Economic
Crises and Pandemics with Python, R,
Netlogo and Julia

Machine Learning Perspectives of Agent-Based
Models

Pedro Campos • Anand Rao . Joaquim Margarido
Editors
Machine Learning
Perspectives of Agent-Based
Models
Practical Applications to Economic Crises
and Pandemics with Python, R, Netlogo
and Julia

Editors
Pedro Campos Anand Rao
University of Porto, FEP, LIAAD-INESC Heinz College of Information Systems and
TEC Public Policy
Porto, Portugal Carnegie Mellon University
Pittsburgh, PA, USA
Joaquim Margarido
ISEP
Porto, Portugal
ISBN 978-3-031-73353-6 ISBN 978-3-031-73354-3 (eBook)
https://doi.org/10.1007/978-3-031-73354-3
© The Editor(s) (if applicable) and The Author(s), under exclusive license to Springer Nature Switzerland
AG 2025
This work is subject to copyright. All rights are solely and exclusively licensed by the Publisher, whether
the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse
of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and
transmission or information storage and retrieval, electronic adaptation, computer software, or by similar
or dissimilar methodology now known or hereafter developed.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication
does not imply, even in the absence of a specific statement, that such names are exempt from the relevant
protective laws and regulations and therefore free for general use.
The publisher, the authors and the editors are safe to assume that the advice and information in this book
are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or
the editors give a warranty, expressed or implied, with respect to the material contained herein or for any
errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional
claims in published maps and institutional affiliations.
This Springer imprint is published by the registered company Springer Nature Switzerland AG
The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland
If disposing of this product, please recycle the paper.

This book is dedicated to all our students and
researchers who believe that it is possible to
significantly improve our understanding of
complex social and economic systems with
agent-based models and machine learning.

Editor’s Preface
Machine Learning and Agent-based models have been around for decades, arguably
since the early days of the Artificial Intelligence (AI) endeavor. As the fields of
AI and computational modeling continue to evolve, the integration of these two
methodologies has become increasingly significant for advancing both research and
practical applications.
Machine Learning (ML) has been primarily concerned about learning patterns
from large amounts of data and predicting outcomes or classifying information. For
example, early applications of ML included decision tree algorithms used in medical
diagnosis. Agent-based models (ABM), on the other hand, have been primarily used
to model and simulate the behavior of autonomous entities called agents and how
they interact with each other. Agent-based models have been used extensively for
capturing and analyzing emergent behavior.
Machine Learning has grown significantly over the past three decades and
has found a broad range of applications across several sectors like financial ser-
vices, healthcare, media and entertainment, retail, manufacturing, agriculture, etc.
Advances in deep learning, specifically around embeddings, attention mechanisms,
and quantization have revolutionized the development of multi-modal foundation
models. The number of ML algorithms and foundation models has expanded
with literally hundreds or even thousands of distinct algorithms and hundreds of
proprietary and open-source foundation models. The basis of ML algorithms has
also evolved from statistical models to neural network models in deep learning,
becoming increasingly larger and more sophisticated, typically now running into
billions of parameters.
Agent-based models on the other hand have also grown over the decades
becoming increasingly sophisticated in capturing complex interactions and behav-
iors. They have been widely used in social sciences to analyze, simulate, and
intervene in individual and group behaviors. Agents have evolved from modeling
emergent behaviors seen in the physical world to acting as digital twins with a
two-way near real-time interaction between the physical and digital to the more
recent conversational LLM-based agents. A fundamental characteristic underlying
all these different types of agents is the fact that these agents are embedded in an
vii

viii Editor’sPreface
environment, continuously interacting with it and with other agents, and carrying
out tasks or fulfilling goals on behalf of others.
Machine Learning acknowledges agents when it comes to reinforcement learn-
ing. Reinforcement learning is one of the best-known techniques for agents
embedded in an environment to learn based on environmental feedback in terms of
rewards or penalties. Over time, reinforcement learning has evolved, significantly
impacting areas such as robotics and autonomous systems. The more recent usage
of the word “agents” within the deep learning and Large Language Model (LLM)
community is to enable conversational entities to access external tools, take actions,
and communicate with other agents.
Agent-based models recognize Machine Learning, especially reinforcement
learning as one type of learning behavior. However, Agent-based models have
typically looked at analyzing and modeling a variety of behaviors including collab-
orative or adversarial behaviors, programmed or emergent behaviors, negotiation,
and counterfactual analysis. For example, an ABM study might simulate a market
where agents learn to trade through reinforcement learning, enhancing the realism
of economic models. More recently machine learning is being used as a technique
for calibrating sophisticated agent-based models.
As someone who has worked in both these areas over the past 35 years, I find
it strange that there are very few books or collection of papers that bring these two
areas closer together. The lack of integrated research has posed significant chal-
lenges, often resulting in missed opportunities for leveraging combined strengths.
This book addresses these gaps by providing a comprehensive examination of the
overlap between these fields. With the increasing adoption of both Agent-based
models and Machine Learning it makes sense to look at the overlap between these
two fields. As a result, this collection of papers brought together on “Machine
Learning Perspectives of Agent-Based Models” is a very timely publication.
The particular focus of this collection is on bringing together ABM and ML
to analyze, predict, and intervene during crisis. While COVID-19 was the most
traumatic event of the current century, it did bring to fore both Agent-based
modeling (a typical text-book example to study the spread of epidemics is agent-
based modeling), and machine learning that was able to exploit the large volumes of
data that was available from the pandemic. Detailed methodologies and case studies
within this collection illustrate how these tools were pivotal in understanding and
managing the crisis.
This collection goes beyond the COVID-19 pandemic, demonstrating applica-
tions in modeling financial crisis, organizational learning, strategic alliances, and
automotive industry. It demonstrates the benefits of integrating Machine Learning
with Agent-based models to gather deeper insights and more meaningful behavioral
interventions. Chapters dedicated to financial market simulations and conflict
scenarios provide a broad view of the utility of these models.
Finally, this collection also addresses some of the ethical and transparency
considerations as we move into the widespread adoption and application of these
models into larger AI systems. Verification and validation of simulations are more
challenging than predictions and more sophisticated ML techniques can go a long

Editor’sPreface ix
way in improving the state of the art in validation and calibration of Agent-based
models. The book emphasizes robust validation techniques to ensure the reliability
of simulations and predictions, fostering trust and acceptance among stakeholders.
In conclusion, “Machine Learning Perspectives of Agent-Based Models” is a
groundbreaking and timely publication that bridges the gap between two rapidly
growing research areas that is finding widespread commercial application. It is
an invaluable resource for researchers, practitioners, and policymakers aiming to
leverage the combined strengths of ML and ABM to address complex societal
issues. I sincerely hope that this collection would be the first of many to bring
researchers, practitioners, and policymakers together to address important crises and
solve societal problems.
Distinguished Professor of Applied Data Science Prof. Anand S. Rao
and AI, Heinz College of Information Systems
and Public Policy
Carnegie Mellon University
Pittsburgh, PA, USA
June 2024

Preface
Agent-Based Models (ABM) provide a promising alternative for understanding
economic processes. ABMs are microscale models that simulate the interactions
of heterogeneous agents based on simple rules. Unlike traditional models, ABMs
consider factors like limited information, bounded rationality, and market disequi-
librium, making them more suitable for capturing the complexity of real-world
economic systems. “A Machine Learning perspective of Agent-Based Models:
Applications to Economic Crises and Pandemics” explores the synergy between
ABMs and Machine Learning, showcasing practical examples in different lan-
guages. The text advocates for a shift toward more dynamic and realistic modeling
approaches, such as ABMs, to better understand and address the complexities of
economic crises. It also highlights the potential of incorporating Machine Learning
techniques to enhance the capabilities of these models. This integration could aid in
not only enhancing the interpretability of ABMs but also in refining the predictive
capabilities of the models, especially when dealing with the dynamic and uncertain
nature of economic crises and pandemics.
This book discusses the challenges of dealing with uncertainty and instability
in the global economy, particularly in the context of frequent crises like the
COVID-19 pandemic, financial crises, and wars and it highlights the limitations
of traditional economic models, especially the neoclassical approach, in explaining
complex economic phenomena. We discuss how ABMs can be applied to study
the effects of the COVID-19 pandemic on healthcare systems and economic
stability. Furthermore, the text introduces the integration of Machine Learning (ML)
and deep-learning models into ABMs to enhance interpretability and prediction
capabilities. The discussion highlights the challenges of interpreting predictions
from complex ML models and underscores the importance of ethical considerations,
transparency, and model validation in the context of complex simulations.
The book aims to simplify the presentation of models for undergraduate students,
using programming languages such as Python, R, NetLogo, and Julia.1 The idea is
1 Program codes are available in: https://ml4agents.free.nf
xi

xii Preface
to be able to function as a guide for creating agent-based models from the scratch
using game theory (such as the Ultimatum game, or a simple currency exchange
game), and machine learning as a paradigm. It emphasizes the importance of a
learning-by-programming approach and includes practical examples of economic
and management phenomena modeled through ABMs.
Divided into four parts, the book covers foundational concepts, explores diverse
applications in crises, develops an economic game from the scratch, and concludes
with case studies and extensions.
This book comes at a time when generative AI is emerging. Generative AI
plays a significant role in science and society, and it can also contribute to the
creation and understanding of complex simulations, such as Data Augmentation,
Scenario Exploitation, and Human-AI Collaboration, since Generative AI tools can
facilitate collaboration between human modelers and AI systems. By generating
suggestions for model adjustments or proposing alternative scenarios, generative AI
supports the iterative development of ABMs. This collaborative approach enhances
the model-building process, leveraging the strengths of both human expertise and
AI capabilities.
But these aspects will be left open for a future edition!
Pittsburgh, PA, USA Anand Rao
Porto, Portugal Pedro Campos
Porto, Portugal Joaquim Margarido
June 2024

Acknowledgments
We thank the collaboration of the authors of this book: Ali R. Vahdati, Ana
Nogueira, Arit Kumar Bishwas, Conceição Rocha, Friederike Wall, Inês Ferreira,
Jeremy Pitt, José Matos, Joseph Voyles, Margarida Silva, Mark Paich, Marta
Moraes, Pavel Brazdil, Rosaldo J. F. Rossetti, Sindy Ma, Sonia Teixeira, and Zafeiris
Kokkinogenis.
xiii

Contents
1 Introduction ................................................................. 1
Pedro Campos
Part I Agent-Based Modelling and Machine Learning
2 Agent-Based Modeling and Learning in Economics: An Overview... 9
Pedro Campos, Anand Rao, and Pavel Brazdil
Part II Agent-Based Models in the Context of COVID19
3 Epidemiology Modelling................................................... 51
Arit Kumar Bishwas and Anand Rao
4 Agent-Based Behavioral Models: Modeling COVID19 Behavior ..... 77
Anand Rao and Arit Kumar Bishwas
5 COVID-19 Epidemiological, Behavioral, and Economic Model....... 99
Anand Rao, Sindy Ma, Mark Paich, and Joseph Voyles
Part III Creating Agent-Based Models of Crisis in Python, and R
6 MyWealth: A Simple Model of Economic Exchange in Python ....... 129
Joaquim Margarido and Pedro Campos
7 The Ultimatum Game as a Paradigm for Learning Agents:
A Python Adventure........................................................ 147
Joaquim Margarido and Pedro Campos
8 Alternative Machine Learning Approaches for an
Agent-Based Model of the Ultimatum Game Using R.................. 189
Pedro Campos, José Matos, and Joaquim Margarido
xv

xvi Contents
Part IV Case Studies: Agent-Based Learning and Crisis Using R,
Netlogo, and Julia
9 An Agent-Based Epidemic Modeling in Julia ........................... 227
Ali R. Vahdati
10 Portfolio Management and Crises: A Multi-Armed Bandit
Approach .................................................................... 251
Inês Ferreira and Marta Moraes
11 Organizational Learning from Crises with Machine
Learning and Agent-Based Models ....................................... 269
Friederike Wall and Pedro Campos
12 Strategic Alliances in NetLogo: A Flocking Algorithm with
Reinforcement Learning................................................... 287
Sónia Teixeira and Pedro Campos
13 Exploring the Efficiency vs. Fairness Behavioural Spectrum
in Multi-Agent Deep Reinforcement Learning.......................... 307
Margarida Silva, Zafeiris Kokkinogenis, Jeremy Pitt, and Rosaldo
J. F. Rossetti
14 Resilient Agent-Based Networks in the Automotive Industry ......... 341
Ana Nogueira, Conceição Rocha, and Pedro Campos

Contributors
Arit Kumar Bishwas PricewaterhouseCoopers, Fremont, CA, USA
Pavel Brazdil University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
Pedro Campos University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
Inês Ferreira University of Porto, FEP, Porto, Portugal
Zafeiris Kokkinogenis University of Porto, LIACC, Porto, Portugal
Sindy Ma PricewaterhouseCoopers, London, London
Joaquim Margarido ISEP, Porto, Portugal
José Matos University of Porto, FEP, Porto, Portugal
Marta Moraes University of Porto, FEP, Porto, Portugal
Ana Nogueira University of Porto, FEP, Porto, Portugal
Mark Paich PricewaterhouseCoopers, London, UK
Jeremy Pitt Imperial College London, London, UK
Anand Rao Heinz College of Information Systems and Public Policy, Carnegie
Mellon University, Pittsburgh, PA, USA
Conceicao Rocha CPES-INESC TEC, Porto, Portugal
Rosaldo J. F. Rossetti University of Porto, FEUP-DEI, Porto, Portugal
Margarida Silva University of Porto, FEUP-MIEIC, Porto, Portugal
Sónia Teixeira University of Porto, LIAAD-INESC TEC, Porto, Portugal
University of Zurich, Zurich, Switzerland
Joseph Voyles PricewaterhouseCoopers, London, UK
Friederike Wall Department for Management Control and Strategic Management,
University of Klagenfurt, Klagenfurt, Austria
xvii

Lists of Abbreviations
AAA Artificial Adaptive Agents
ABM Agent-Based Models
ACE Agent-Based Computational Economics
ACO Ant Colony Optimization
ACS Agent-Based Computational Sociology
AI Artificial Intelligence
ANFIS Adaptive Neuro-Fuzzy Inference System
ANN Artificial Neural Networks
ASHIA Analytically Solvable Heterogeneous Interacting Agent Models
AV Autonomous Vehicles
BERT Bidirectional Encoder Representations from Transformers
CE Computational Equivalence
CI Computational Intelligence
CNN Convolutional Neural Networks
COVID-19 Coronavirus Disease 2019
COVID-EBE Coronavirus Disease (Epidemiological, Behavioral, and Economic)
C-S Cucker and Smale Algorithm
CV Coefficient of Variation
DP Dynamic Programming
DSGE Dynamic Stochastic General Equilibrium Models
DTN Disruption-Tolerant Networking
EES Evolutionary Stable Strategy
ETF Exchange-Traded Fund
GA Genetic Algorithm
GABMs Generative Agent-Based Models
GDP Gross Domestic Product
iGSS Inverse Generative Social Science
LLM Large Language Model
LSTM Long Short-Term Memory
MAB Multi-Armed Bandit
MADRL Multi-Agent Deep Reinforcement Learning
xix

xx ListsofAbbreviations
MARL Multi-Agent Reinforcement Learning
MAS Multi-Agent Systems
MC Monte Carlo Methods
MDP Markov Decision Process
ML Machine Learning
NN Neural Networks
POMDP Partially Observable Markov Decision Process
PPS Project Portfolio Selection
PRS Procedural Reasoning System
PSO Particle Swarm Optimization
RL Reinforcement Learning
SARS-CoV-2 Severe Acute Respiratory Syndrome Coronavirus 2
SEIRD Susceptible, Exposed, Infected, Recovered, and Dead
SIR Susceptible-Infected-Recovered
SCN Supply Chain Network
SCM Supply Chain Management
SWF Social Welfare Function
TD Temporal Difference Method
UCB Upper Confidence Bounds Algorithm
VOA Virus Optimization Algorithm

Chapter 1
Introduction
Pedro Campos
We reside in an era marked by continual crises that directly affect the real economy.
The recent COVID-19 pandemic represented one of the most significant challenges
since World War II. Financial turmoil and continuous conflicts highlight the
world’s instability, prompting questions like: how do we handle such widespread
uncertainty? Can we still make forecasts amidst this instability?”
Economics and Management sciences focus on the complex behaviour and inter-
actions of economic agents dealing with production, distribution and consumption
of goods and services, resource allocation, public policy, strategic management,
micro and macroeconomics, among others. But because of this complexity, it is
often difficult to understand how certain effects may result from the combination of
certain causes.
The neoclassical approach is not well suited to encompass and explain all the
complex details of economic life, such as the Global Financial Crisis of 2008 and
the Great Recession that followed [1]. Joseph Schumpeter, for example, rejected
the kind of economic thought that mainly favours deductive methods of inquiry.
Taking into account the evolution of Economics as a science, the need for a deep
epistemological change has already been pointed out by outstanding economists.
Dynamic Stochastic General Equilibrium (DSGE) models, the standard tool for
macroeconomic analysis, have been deeply challenged by the Global Financial
Crisis and the Great Recession. In DSGE models there is no causal link between
a boom and a bust by construction, except for small self-correcting deviations from
the deterministic steady state, so the stable period can be understood as separate
from the unstable period. DSGE models attempt to integrate macroeconomics with
microeconomics by providing microeconomic foundations for macroeconomics [4].
P. Campos (@)
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 1
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_1

2 P.Campos
Economy is as a complex system of heterogeneous interacting agents charac-
terised by limited information and bounded rationality. Crises are macroscopic
phenomena which spontaneously emerge from the web of microscopic interactions
[1]. Agent Based Models (ABM) are microscale models that use simulation in order
to search for explanatory insights into the collective behaviour of agents obeying
simple rules. ABM constitute a bottom-up approach that allows us to analyze the
effect of interactions of agents as a whole. They characterize economic processes
as dynamical systems of heterogeneous agents, explicitly accounting for agent
heterogeneity, bounded rationality, and market disequilibrium. These models are
a promising research tool for understanding the situations and problems emerged
with the recent crisis. As an example, [1] argue that a Central Bank has to prevent a
systems’ financial collapse, or the spreading of a financial crisis, rather than looking
at the “average” risk of bankruptcy using the latter as a measure of the stability
of the system by means of a network analysis. Therefore, the economy can be
analyzed in terms of different interacting sub-systems and local intervention can
be recommended to prevent failures and their spread . The interaction of agents that
belong to the network structure between firms and banks can play a significant role
in determining the emergence, the depth and the diffusion of a crises.
Axtell and Farmer [2] have provided an overview of the usefulness of Agent-
Based Modeling (ABM) in Economics and Finance. Also Matteo Richiardi [3] in
the Institute for New Economic Thinking employed experimentation and simulation
with diverse behavioral assumptions, ranging from choice heuristics to learning and
expectation formation, to establish a solid basis for the modeling assumptions used.
The acknowledgment that a new direction is needed to further study the link
between the causes and effects of crises, and that ABM may provide that link has
been made by Hamill and Gilbert [4]. Agent based models potentially present a
way to model the financial economy as a complex system, as John Maynard Keynes
attempted to do, while taking human adaptation and learning into account, as Lucas
advocated [5].
There are many situations where the effects of crises can be handled with
ABM. Flaminio Squazzoni and other authors [6], worried by the effects that the
COVID-19 pandemic were causing on the sustainability of the health care systems,
and threatening an economic meltdown, drew attention to the understanding that
pandemic requires fine-grained data representing specific local conditions and the
social reactions of individuals. They argue that current mainstream research do not
cover the full behavioural and social complexity of societies under pandemic crisis.
The insurance industry has been studied by Owadally et al. [7], and the authors
concluded that heterogeneity and interaction at a microlevel must be understood
if cycles and crises are to be managed and prevented. An ABM has been used by
Garrido et al. [8] to understand how propagation of failures in a banking network
system occurs in a very short run analysis. For this purpose, an outside credit shock
on one of the banks was triggered and the cascade effect of failures was simulated. In
another work, an ABM has been combined with network analysis by Namatame and
Chen [9] to shed light on how a failure in a firm propagates through dynamic credit
networks and leads to a cascade of bankruptcies. Gallegati and Kirman used Agent-

1 Introduction 3
Based Computational Economics (ACE) and Analytically Solvable Heterogeneous
Interacting Agent (ASHIA) models based on statistical physics or Markov chains to
deal with economies in which direct interaction between agents is important [10].
The concepts of adaptive learning, and Machine Learning, are drawing inspi-
ration from thought leaders like Herbert Simon [11], John Holland [12], Melanie
Mitchell [13], Peter Todd [14], and Richard Belew [15]. These influential figures
anticipated and supported the idea of incorporating learning principles into agent-
based models. However, Machine learning and deep-learning models, with their
intricate structures, pose challenges in interpretability despite their complexity.
In the era of Large Language Models, and Generative AI, these can also help
to program and develop Agent-Based models, and must be used thoughtfully,
considering the specific needs and goals of the agent-based modeling process.
Ethical considerations, transparency, and validation of model outputs remain crucial
aspects of incorporating language models in complex simulations.
The book “A Machine Learning perspective of Agent-Based Models—
Applications to Economic Crises and Pandemics, with practical examples in
Python, R, Netlogo and Julia” uses the ABM paradigm for economic crisis and
pandemics, and Artificial Intelligence (AI) and Machine Learning (ML) models are
used to support description and prediction tasks. ML methods are used to better
interpret and understand the relation between the parameters of the ABM and the
results in the simulations [16]. However, interpretability of predictions produced
by ML models is far from straightforward. Deep-learning models in particular are
enormously complex, often containing hundreds of layers of neurons adding up to
tens of millions of parameters. Recent advances and concerns have been devoted to
the interpretability of ML models.
In addition, ML models are also used by agents to learn during the process of
interactions with other agents and with the environment. Multiple ML methods
for ABM emulation have been compared by Angione et al. [17] to determine
the approaches best-suited to replicating the complex and non-linear behaviour of
ABMs.
One of the innovative aspects of this book is the simplicity of how models
are presented to undergraduate students. We use this approach to convey concepts
and teach how to create models to reproduce some economics and management
phenomena.
The Ultimatum game, a game-theoretical approach is described with detail along
the book and, at some point, the effect of learning is introduced. Forms of learning
such as Reinforcement Learning and other models are considered. At the same
time, machine learning-based data analysis techniques are also used to handle data
generated by agent-based models. Also covered are Social Network Analysis and
Agent Based Models of Network Science.
We follow the perspective of Learning by Programming, which consists of using
simple programming techniques to build models, such as the Microeconomic Model
of crisis, or a Virus on a Network Spread Model, that are taught and learned step by
step throughout the book using several different tools. Python is the main language
in the book, due to its popularity, but R, NetLogo and Julia are also used. Python

4 P.Campos
has become a very popular programming language in the last few years, especially
in the area of data science and has been used in very important projects like Google,
Quora, Youtube, Reddit and Dropbox, to name a few.
Some packages exist in Python for Agent-Based Modeling, such as Janus for
Land Use and Land Cover Change, and MESA, a modular framework for building,
analyzing and visualizing the outputs. Furthermore, Python is also very suitable for
implementing Machine Learning models and some people even argue that Python
is the most popular language for all Data Scientists.
The book contains four parts.
In Part I—Agent-Based Modelling and Machine Learning, we cover the founda-
tional concepts of ABM, and the integration of learning and evolution. We introduce
different perspectives of Machine Learning in ABM, such as the ones of Yoav
Shoham, Melanie Mitchell, Rosaria Conte, Thomas Brenner, Shu Heng-Chen, and
Chung-Ching Tai, among others.
In Part II we explore different applications of ABM in crises, namely, in the
context of COVID19: Epidemiology modelling, modelling COVID behaviour, and
COVID 19 Epidemiological, Behavioral, and Economic Models. We show how
ABM, traditionally used as an exemplar for ‘disease progression’ was adapted,
enhanced, and put to the test during the COVID19 pandemic. The interplay between
the epidemiological factors, consumer behavior and their impact on the economy is
demonstrated with the help of ABM.
Part III contains a step-by-step development of a simple economic exchange
model (MyWealth) with a learning component that is created from the scratch in
Python, simulating simplified economies, aiding in teaching economic concepts
and agent-based modeling principles. Another step-by-step implementation of the
Ultimatum Game is made by setting up a baseline model with proposers using
either fair or unfair split strategies. A Fictitious Play is introduced, which reduces
responder rejections, and Reinforcement Learning to refine action policies through
sequential decisions, culminating in a crisis midway through the iterations. We
also demonstrate the potential of different types of agent-based learning within the
Ultimatum Game where agents engage in repeated game iterations, following prede-
fined rules and utilizing Machine Learning to optimize their earnings. Specifically,
we implement Fictitious Play, Reinforcement Learning, and decision tree-based
Classifier systems in R to enable agents to learn from past interactions and apply
prior knowledge.
Finally, in Part IV, case studies and extensions exploring dynamic environments
and the use of different tools and languages like Julia for ABM implementation are
developed. From Industry-Based Resilient Networks in the Automotive Industry,
to Organizational Learning, Portfolio Management or the study of Fairness in
traffic Light Control problems using deep learning, and R, JULIA or Netlogo
implementations.

1 Introduction 5
References
1. D.D. Gatti, G. Fagiolo, M. Gallegati, M. Richiardi, A. Russo (eds.), Agent-Based Models
(Cambridge University Press, Cambridge, 2018)
2. R.L. Axtell, J.D. Farmer, Agent-based modeling in economics and finance: past, present, and
future. INET Oxford Working Papers 2022-10. Institute for New Economic Thinking at the
Oxford Martin School, University of Oxford (2022)
3. M. Richiardi, The future of agent-based modelling. Working Paper 2015-W06, Economics
Group, Nuffield College, University of Oxford (2015)
4. L. Hamill, N. Gilbert, Agent-Based Modelling in Economics (Wiley, Hoboken, 2015)
5. J.D. Farmer, D. Foley, The economy needs agent-based modelling. Nature 460(7256), 685–686
(2009)
6. F. Squazzoni, J.G. Polhill, B. Edmonds, P. Ahrweiler, P. Antosz, G. Scholz, E. Chappin, M.
Borit, H. Verhagen, F. Giardini, N. Gilbert, Computational models that matter during a global
pandemic outbreak: a call to action. J. Art. Soc. Soc. Simul. 23(2), 10 (2020)
7. I. Owadally, F. Zhou, D. Wright, The insurance industry as a complex social system:
competition, cycles and crises. J. Artif. Soc. Soc. Simul. 21(4), 1–2 (2018)
8. P. Garrido, P. Campos, A. Dias, Balance sheet analysis of credit and debt networks. Adv.
Complex Syst. 18(5–6), 1550025 (2015)
9. A. Namatame, S.H. Chen, Agent-Based Modeling and Network Dynamics (Oxford University
Press, Oxford, 2015)
10. M. Gallegati, A. Kirman, Reconstructing economics. Complex. Econ. 1(1), 5–31 (2012)
11. H. Simon, A behavioral model of rational choice. Quart. J. Econ. 1, 99–118 (1955)
12. J. Holland, Adaptation in Natural and Artificial Systems: An Introductory Analysis with
Applications to Biology, Control and Artificial Intelligence (The MIT Press, Cambridge, 2001)
13. M. Mitchell, Artificial Intelligence: A Guide for Thinking Humans, 1st edn. (Farrar, Strausand,
Giroux, New York, 2019)
14. P. Todd, The causes and effects of evolutionary simulation in the behavioural sciences, in
Adaptive Individuals in Evolving Populations: Models and Algorithms, ed. by R. Belew, M.
Mitchell (Santa Fe Institute in the Sciences of Complexity/Addison Wesley, Santa Fe/Boston,
1996), pp. 211–231
15. R.K. Belew, M. Mitchell, Adaptive Individuals in Evolving Populations (Addison-Wesley,
Reading, 1996)
16. M. Pereda,J.Santos, J.M. Galan,Abriefintroduction tothe use ofmachine learningtechniques
in the analysis of agent-based models (2015). https://ssrn.com/abstract=2689676. https://doi.
org/10.2139/ssrn.2689676
17. C. Angione, E. Silverman, E. Yaneske, Using machine learning as a surrogate model for agent-
based simulations. PLoS One 17(2), e0263150 (2022)

Part  I
| Agent-Based  | Modelling  | and  Machine  |
| ------------ | ---------- | ------------- |
Learning

Chapter 2
Agent-Based Modeling and Learning in
Economics: An Overview
Pedro Campos, Anand Rao, and Pavel Brazdil
The fields of Agent-Based Modelling (ABM) and Multi-Agent Systems (MAS) have
attracted the attention of many researchers over the last two or three decades, as they
model how our society is organised. So, developing such complex systems could
help us to advance not only the general understanding, but also be used to help
to guide decisions. In addition, crises have followed one another, from financial
crises to pandemics and wars, with significant economic and social impacts. The
question therefore arises as to how these ABM and MAS can be developed. In
this chapter we reflect on the role of learning, and in particular, machine learning,
in multi-agent systems (MAS) and also the effects of crises. The study of agent
learning is addressed in different areas, such as Artificial Intelligence (AI) and game
theory, with applications in engineering, economics, and other social sciences. The
AI literature takes an approach to agent learning that distinguishes it from the game
theoretic literature. As stated by Shoham et al. [1], commonalities between these
two fields are greater than the differences and together with the area of mechanism
design, and perhaps the computational questions regarding concepts such as the
Nash equilibrium, multi-agent learning is one of the most fruitful interaction fields
between computer science and game theory as we are going to see in this Chapter.
The structure of the Chapter is the following: Sect. 2 provides an overview of the
evolution and key concepts in agent-based modeling (ABM) within economics,
highlighting its role in simulating complex adaptive systems (2.1). The discussion
then moves to the notions of adaptation and learning in multi-agent systems (2.2),
P. Campos (@) · P. Brazdil
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt; pbrazdil@fep.up.pt
A. Rao
Heinz College of Information Systems and Public Policy, Carnegie Mellon University, Pittsburgh,
PA, USA
e-mail: anandr2@andrew.cmu.edu
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 9
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_2

10 P.Camposetal.
followed by a review of learning mechanisms inspired by evolutionary dynamics
(2.3). Section 2.4 explores efforts to integrate cognitive and social dimensions in
agent-based models. Next, major approaches to agent learning are categorized and
analyzed (2.5). Section 2.6 introduces the intersection between machine learning
and ABM. The emerging role of Large Language Models (LLMs) in agent-based
research is examined in Sect. 2.7, followed by strategies for integrating LLMs into
ABM frameworks (2.8). Section 2.9 introduces Generative Agent-Based Models
(GABMs), a novel paradigm blending generative AI and agent-based simulations.
Finally, Sect. 2.10 offers concluding remarks and final considerations regarding
future research directions.
2.1 Agent-Based Models in Economics
Agent-based models or modelling (ABM), is a class of computational models
aiming at studying systems composed of interacting agents and exhibiting emergent
properties arising from the interactions of the agents that cannot be deduced from the
properties of the agents themselves [2]. These agents engage in varied behaviours
encoded in a set of decision rules that drive their actions in response to behavioural,
environmental and social change [3]. In 1991, John Holland and John Miller
had already addressed the role of Artificial Adaptive Agents (AAA) in Economic
Theory [4]. The topic of learning in agent-based modelling has been dealt with
much insistence in recent times, due to the need to understand how it is possible
for agents to develop methods to adapt their behavior to new situations, which
can be seen as learning mechanisms. In the last decade, multi-agent learning has
achieved great success in games which were once considered impossible for AI to
conquer [5]. The formal connection between ABM and machine learning started
around 1990 with the rise of topics like reinforcement learning. Stone and Veloso
[6] defined general multi-agent scenarios from a machine learning perspective and
presented a survey using robotic soccer as an appropriate test-bed for agents. Agent-
based models are particularly appealing for their ability to study the interactions of
heterogeneous agents, characterized by learning and bounded rationality [7]. Axtell
[8] supported a close connection between agent computing in the positive social
sciences and distributed computation in computer science. Distributed computation,
as well as distributed artificial intelligence involves computations performed by
distinct software agents. The growing attention devoted to ABM in the study of
economic phenomena is due, to a great extent, to the inadequacy demonstrated by
the prevailing theoretical frameworks for economic analysis, during and after the
global financial crisis of 2007–2008 [9].

2 ABL 11
2.1.1 Neoclassics, Evolutionary and Crises
Agent-based Models have been commonly used within the evolutionary economics
perspective, which provides much more realistic settings than neoclassic economics
by allowing the consideration of learning agents acting in a context of disequi-
librium and bounded-rationality [9]. Indeed, the analysis of interactions at the
individual level, only, may lead to misunderstandings. Usually, economists assume
that the market is in equilibrium and that the individual preferences are constant.
Dynamic Stochastic General Equilibrium Models (DSGE) models are standard tools
for macroeconomic analysis. There are examples where this assumption does not
hold and the interaction between different levels of analysis is crucial for the real
understanding of a given situation. Thus, the analysis of mixed levels (individual
cognitive level and social level) may constitute the answer to some of these
problems. Indeed, a growing number of leading economists identify the limitations
of the dominant economic theory as a significant aspect of the economic crisis,
including Paul Krugman, and Joseph Stiglitz, among others [10]. These limitations
include assumptions of rational expectations, representative agents and perfect
markets. More recently, Polyzos et al. [11] studied the effects of the governments
responses to crisis caused by the COVID 19 pandemics, and introduces several
other financial crisis, rare events, and disasters such as World Wars, the Great
Depression or even the Asian financial crisis (late 1990s) and other similar events
and argues that a framework for measurement of the financial consequences of
such events is necessary. In the context of financial crisis, several researchers such
as [10], [11], [12], and [13], argue that Dynamic Stochastic General Equilibrium
Models (DSGE) may carry disadvantages in describing complex economic systems.
Therefore, the use of agent-based modelling and learning is a good fit for crisis-task
predictions. In neoclassical conception, learning is typically modeled as rational
adaptation through individual or fictitious play, while more realistic approaches
draw on AI and behavioral science [14]. In fact, unlike DSGE models, it features a
bottom-up approach, by simulating the behaviour of each individual agent and then
aggregating the results. In that sense, during the COVID-19 pandemic, Squazzoni
et al. [15] called on the scientific community to improve the transparency, access,
and rigour of the models. The importance of a model is that if micro-specifications
are theoretically plausible, the simulation will become stable and robust against
simulation parameters.
2.1.2 Agent-Based Computational Economics
Multi-Agent Systems are often used to model economies and organizations. Accord-
ing to [16], there are several reasons why economies should be modelled by
MAS: economies are complex systems encompassing micro behaviours, interaction
patterns, and global regularities. The MAS allows a “two-way feedback between

12 P.Camposetal.
microstructure and macro regularities mediated by agent interactions”. Whether
partial or general in scope, studies of economic systems should consider how
to handle difficult real-world aspects such as asymmetric information, imperfect
competition, strategic interaction, collective learning and possibility of multiple
equilibria. Multi-Agent Systems are a way of “growing economies from the bottom
up” [17]. The field of Agent-Based Computational Economics (ACE) is inspired,
includes or may be complementary to other fields such as: Experimental Economics,
Complex Adaptive Systems, Computational Modelling of Social Dynamics, Net-
work Economics, Agent Modelling in Economics and Finance, etc. ACE have been
assumed as a relevant and promising alternative framework for economic analysis
and have been extensively used as a “laboratory” for policy design, in addition
to being widely successful in explaining micro and macro stylized facts [10]. An
illustrative example of the ambitious steps being taken in the field of ACE is the
development of EURACE, an attempt to construct an agent-based model of the
European economy [18].
In a large part of the studies of ACE, game theory is used. Game theory provides
us with the mathematical tools to understand the possible strategies that utility-
maximizing agents might use when making a choice. It is mostly concerned with
modeling the decision process of rational humans, a fact that should be kept in mind
as we consider its applicability to multiagent systems. One of the most important
aspects in modelling in economics is the way how the system is conceptualized
and then implemented by the modeller. According to [16], the modeller constructs
a virtual economic world populated by various agent types (economic, social,
biological, physical) and sets the initial world conditions. Next, he/she steps back to
observe how the virtual world develops over time. The events in this virtual world
are driven by agent interactions. The key characteristics of an organizational agent,
the “firm” agent should contain the following characteristics:
• Profit-seeking agent with strategic reasoning and learning capability;
• Profit gains by producing and selling products;
• Can adjust production and price levels in every trading period;
• Can also invest profits to expand its production capacity.
One of most important contributions of ACE to mainstream economic theory is
that it enriches our exploration of economic dynamics [19]. It calls our attention
to the fact that the established economic theory may not be robust to learning
algorithms. In that sense, Shu Heng-Chen [19] states that economists are able to
realize the relevance of laboratory experiments (based on game theory, for example),
psychology, cognitive sciences and neural sciences to economics. In fact, agent-
based simulation can help game theorists ponder on the sensitivity of their analysis
to various learning schemes and Reinforcement Learning is one of this learning
types that may be used in ACE. Furthermore, [19] argues that within the area of
economics itself, ACE matches well with experimental economics and behavioral
economics as models of human agents. It has recently been noticed that models of
software agents and human agents should not be separate entities. ABM and mostly
ACE are composed of Agents (usually active objects), Objects (the other elements

2 ABL 13
Fig. 2.1 Sample of an agent-based model
not agents), Relationships (interaction agent-agent and agent-object, that promotes
communication between the various elements of the model) and Environment—the
framework where the agents and objects are embedded—see Fig.2.1.
According to [20], the standard model of economic decision-making, rests on a
set of hypotheses that may be typified in the following propositions:
1. Agents are fully informed about the environment;
2. Agents are consistent, in the sense that between two alternatives they choose the
best one (according to some criterion);
3. Deciding agents encounter no limit of time and computational power
2.1.3 Interaction and Cooperation
Epstein and Axtell [21], in their pioneering work “Growing Artificial Societies”,
demonstrated how fundamental collective behaviour can emerge from the interac-
tion of individual agents and between agents and the environment. And an important
output of interaction is related to learning from others.
The idea of learning in dynamic environments contrasts with classical non-
cooperative game theory that analyzes how rational players will behave through
static solution concepts such as the Nash equilibrium. In Nash equilibrium, no
individual has a unilateral incentive to change his or her behavior [22]. Interaction
is a natural process in the real world, resulting from the relationship between an
individual and the world where he or she lives. For these interactions to happen,
individuals have to be capable of developing communication (not just transmitting
information), but more importantly, to provoke some specific behaviour in others
[23]. Those interactions may consist, for instance, of attraction, combat, mating,
communication, trade, partnership or rivalry [24]. Cooperation is the primary
form of interaction studied in Multi-Agent Systems, although cooperation usually
lies outside the Nash equilibrium in simple, one-shot games. Cooperation is a
mechanism of complex interaction, where agents have to coordinate their actions

14 P.Camposetal.
in the search for synergies that offer advantages of pooled skills [23]. The level of
commitment is low and there is no sharing of goals.
2.1.4 Generative and Inverse Generative Social Science
With Growing Artificial Societies, Epstein and Axtell [21] proposed a generative
program for the social sciences. Generative social science is primarily concerned
with building computational models or simulations that generate social phenomena
through the interaction of individual agents. Many Agent-Based Models work under
the generative approach that has been systematised by Joshua Epstein [25], in the
following steps:
1. Situate an initial population of autonomous heterogeneous agents in a relevant
spatial environment;
2. Allow them to interact according to simple local rules, and thereby generate—or
‘grow’—the macroscopic regularity from the bottom up [ ...].
.
In turn, [20] point out that four main issues need to be addressed to build an
Agent-Based Model,: (i) the nature of the agents; (ii) the list of variables describing
their state; (iii) the list of the actions the agents can perform; (iv) the structure of their
interaction with other agents. Both these computational approaches working “from
the bottom-up” allow for a generative research program to be pursued with unprece-
dented scope and vigour. Therefore, those micro-specifications in question are said
to satisfy the criterion of ‘generative sufficiency’ with regard to the social outcome
that we are studying. The concept of generative sufficiency was approached by
Medina in 2017 [26], in which the author proposed several conceptual alternatives
and identified collective challenges that the analytics community should consider to
remain aligned with its objectives.
More recently, in 2023, Epstein [27], developed the concept of Inverse Generative
Science (iGSS) where, instead of manually creating fully-formed agents to achieve
a specific target, as in the forward problem, iGSS begins with the macro-target
and evolves micro-agents that produce it. In this process, only basic agent-rule
components and allowable combinators are specified. One important aspect of
this perspective is the link with Fisher’s (1930) Fundamental Theorem of Natural
Selection [28]: the rate of growth of a population, in terms of fitness, is proportional
to phenotypic variance. By driving up the variance in generative agent phenotypes,
iGSS can likewise accelerate the evolution of social science.
Generative social science is a specific approach within social science with a focus
on the interactions of individual agents. Emergence, on the other hand, is a broader
concept that describes the spontaneous formation of complex patterns in various
complex systems, including but not limited to social systems, and, of course, they
are connected.

2 ABL 15
2.1.5 Individual and Aggregate Levels: Emergence
Relationships among the elements of ABM are crucial. And communication is the
basis for interactions within social organization [29]; it is expressed as a form of
interaction in which the dynamic relationship between agents is expressed through
the intermediary of mediators or signals, which once interpreted, will affect the other
agents. In this scope, the field of agent-based organizational simulation (ABOS) has
been fruitful, as it allows researchers to recreate interactions between individuals
in an organization or between organizations in a market. See, for example, the
surveys made by Wall [30] and Gómez-Cruz et al. [29]. Agent-based models in
organizations can also incorporate learning. In 2023, Wall developed a model that
helps understand the adaptive processes of managers based on experiential learning
and backward-looking search behavior [31]. One important feature of the agents
is behaviour. Behaviour characterizes all the properties that the agent manifests
itself in its environment. Belew and Mitchell [32] describe behaviour, as something
that “closes the loop” between an organism and its environment. We will devote
some attention to behaviour in the next chapters of this book, as the modelling of
behaviour is very important in Agent-Based Models.
Another important aspect of ABM is the individual and aggregate levels of
analyses. The connection between these levels is sometimes referred to as emer-
gence. According to [24], the large-effects of complex locally interacting individuals
endorse the appearance of emergent properties at the level of the population.
Emergence is maybe one of the hallmarks of complexity in both physical and socioe-
conomic systems. Emergence is the casual relationship between the complexity of
macro dynamics and the complexity of micro dynamics [33]. Batten [34] addresses
several forms of emergent cooperative behaviour, such as those represented by the
prisoner’s dilemma or the trading agent. In the basis of emergence, there is the
interaction of individual agents. Techniques that produce such results are known by
several names including Agent-Based Modelling, bottom-up modelling and artificial
social systems [24].
The bottom-up approach is widely used in teaching and learning ABM through
cellular-automata. Cellular automata are cells located in a regular grid where the
behaviour of an individual cell is determined by a set of rules which specify how
that state depends on the previous state of that cell and the states of its neighbours.
In the following we will look at some examples of this approach and how they can
provide us with important insights into real problems.
2.1.6 The Game of Life
One of the famous examples of cellular automata is the Conway’s Game of Life
[35]. The rules in this game are simple: a cell can only survive if there are either
two or three other living cells in its immediate neighbourhood (the eight cells
surrounding it). If these conditions are not satisfied it will die either from the effect

16 P.Camposetal.
of overcrowding (if it has too many living neighbours) or from loneliness (if it has
too few living neighbours).
Cellular automata are an idealized version of a complex system [36]. Conway
was trying to find rules that originated interesting pattern behaviours in the agents.
And indeed various interesting patterns can emerge in this game. But what is
emergence and can it be observed here?
The emerging properties of this model appear when black cells do not actually
’move’, but the pattern of black squares are seen by an observer as a glider
travelling across the grid. Besides, other complex patterns spontaneously emerge
such as, oscillators (patterns that repeat over time), and stable structures (still lifes).
These behaviors are not explicitly programmed—they emerge purely from the local
interactions over time.
Algorithm 1 Conway’s Game of Life
1: Initialize a 2D grid of cells (each cell is either Alive or Dead)
2: for each generation do
3: Create a new empty grid (next state)
4: for each cell(x,y).in the grid do
5: Count the number of Alive neighbors around(x,y).
6: if cell(x,y).is Alive then
7: if Alive neighbors =2.or =3.then
8: Cell(x,y). stays Alive in the new grid
9: else
10: Cell(x,y).becomes Dead (underpopulation or overpopulation)
11: end if
12: else
13: if Alive neighbors =3.then
14: Cell(x,y).becomes Alive (reproduction)
15: end if
16: end if
17: end for
18: Replace the current grid with the new grid
19: end for
2.1.7 Schelling’s Segregation Model
Another two-dimensional cellular automata popular example of emergence was
developed by Thomas Schelling in the early 1970s [37],1 who was interested in
studying the macro behaviour that emerged from micro decisions. The Schelling
1 There are several different implementations of the Schelling’s segregation game. See for example:
Agent-Based Computational Economics, (Leigh Tesfatsion’s page): http://www2.econ.iastate.
edu/tesfatsi/demos/schelling/schellhp.htm Simulating Complexity: https://simulatingcomplexity.

2 ABL 17
model illustrates how individual tendencies regarding neighbors can lead to seg-
regation [3 8 ]. The rules are simple: there are two ethnic groups of agents: each
agent aims to reside within a neighborhood where the fraction of people of the same
group is sufficiently high. With this model, Schelling demonstrated that the in-group
preference favours a higher segregated society.
In a possible implementation of this game, agents are initially placed at random
locations in a40×40cell grid and can move to an empty location in case they are not
.
satisfied with the current location. In this game, agents have rules of satisfaction (the
fraction F of people of the same group). We can assume that the level of satisfaction
is the same for all individuals. We developed the pseudocode and a sample code for
this game, using R. In this program, we simulated 10 thousands attempts of agents
moving, based on the premises defined above.
| Shelling Segregation model |     | (R  | code)2  |     |
| -------------------------- | --- | --- | ------- | --- |
for (i in 1:10000) {
#place agents at random locations
#Choose randomly from those that are unhappy
#(they must come from a non-occupied cell)
#go is a flag to go
#iteration is a flag to limit the iterations
go<-0;iteration<-0
while (go==0 & iteration<100) {
mover_X<-round(runif(1, 1, 40))
mover_Y<-round(runif(1, 1, 40))
if (world[mover_X, mover_Y]==1 | world[mover_X, mover_Y]==2 )
{#see if it’s unhappy
ifelse(get_neighbours(mover_X, mover_Y,
world[mover_X,mover_Y])<0.3,go<-1,
{go<-0;iteration<-iteration+1})
}
}
| ethnic_group<-world[mover_X, |             |                 | mover_Y]    |              |
| ---------------------------- | ----------- | --------------- | ----------- | ------------ |
| if (iteration                | <100)       | {world[mover_X, |             | mover_Y]<-0} |
| #choose                      | destination | agents’         | coordinates | randomly     |
| #it must                     | go to an    | empty cell      |             |              |
| #vague is                    | a flag      |                 |             |              |
| #iteration                   | is a        | flag to limit   | the         | # iterations |
vague<-1
| if (iteration<100)            |                 | iteration<-0     |       |                            |
| ----------------------------- | --------------- | ---------------- | ----- | -------------------------- |
| while (vague==1               |                 | & iteration<100) |       | {                          |
| dest_X<-round(runif(1,        |                 | 1,               | 40))  |                            |
| dest_Y<-round(runif(1,        |                 | 1,               | 40))  |                            |
| if (world[dest_X,             |                 | dest_Y]==0)      |       |                            |
| {#see                         | the destination |                  | makes | it happy                   |
| ifelse(get_neighbours(dest_X, |                 |                  |       | dest_Y, ethnic_group)>0.3, |
wordpress.com/2016/01/06/building-a-schelling-segregation-model-in-r/  R  Bloggers:  https://
www.r-bloggers.com/2012/04/animating-schellings-segregation-model/.
2 Program codes are avaialable in: http://ml4agents.free.nf/.

18 P.Camposetal.
vague<-0, {vague<-1;iteration<-iteration+1})
}
}
if (iteration <100) {world[dest_X, dest_Y]<-ethnic_group;
move<-move+1}
print(i)
}
To detect the satisfaction of the agents, function get_neighbours returns the
fraction of people of the same ethnic group in the neighborhood.
get_neighbours<-function(x, y,a) {
#a<-world[x,y]
if (x == 1) x<-39
if (x == 40) x<-2
if (y == 1) y<-39
if (y == 40) y<-2
n1<-world[x,y-1 ]; n2<-world[x+1, y-1];
n3<-world[x+1, y ]; n4<-world[x+1, y+1];
n5<-world[ x,y+1 ]; n6<-world[x-1,y+1 ];
n7<-world[ x-1,y ]; n8<-world[ x-1,y-1]
n<-c(n1,n2,n3,n4,n5,n6,n7,n8);table(n)
return(table(n)[a+1]/8) }
After 10,000 runs, we can see what happened in terms of changes in the pattern
of the distribution of the two ethnic groups—see Fig.2.2.
But what is maybe more interesting in this dynamics is that the behaviour in
Shelling’s model is contingent, that is, the behaviour of some depends on what the
others are doing. In Schelling’s model, a small change in class consciousness (the
fraction of people of the same ethnic group) can result in a large change in the
number of moves [34]. There is a small range over which the degree of segregation
is by no means obvious. Once class consciousness exceeds a critical threshold,
however, a highly segregated pattern appears immediately
Sometimes, like in the Schelling’s example above, emergence occurs as a natural
phenomenon. Can we see this as an individual process of adaptation?
In the following we will revisit the origins of Adaptation as a computational
concept.
Fig. 2.2 Distribution of two
ethnic groups (blues and reds)
after running 10,000
iterations of the Shelling
Segregation model (see R
code)

2 ABL 19
2.2 Adaptation and Learning
2.2.1 The Origins
Adaptation is the capacity to adjust to change. Richard Belew and Melanie Mitchell
[32] defined Adaptation as “the capacity for change and the additional requirement
that this change signifies an improvement of fit”. And change implies adopting
new behaviors that allow to cope with change. Jean Piaget described behavior as
the adaptation to the environment which is controlled through mental organizations
called schemes that the individual uses to represent the world and designate action.
Piaget believed that people learn new information slowly by attaching the new
information with meanings from prior experiences [39].
Adaptation of an individual depends on the way it gets and assimilates the
information from the environment. Information is subject to error and, also, it is
the result of the agent’s perception of the environment. Agents having this capacity
of being able to call into question a fact develop the basis of our cognitive adaptation
and therefore the accommodating of our cognitive system to a world of perpetual
evolution [23].
Learning is adapting to the constantly changing environment. This work is
focused essentially on the ability of agents to learn and how learning can be crucial
to create important models that allow us to better understand and explore economic
dynamics. This ability leads us to the machine learning perspective of Agent-
Based Models. Learning models are used by agents to learn during the process of
interactions with other agents and with the environment, in order to improve their
actions in response to behavioural, environmental and social change.
Machine Learning and Deep-learning models, in particular, are enormously
complex, often containing hundreds of layers of neurons adding up to tens of
millions of parameters. Because of that, interpretability of predictions produced
by Machine Learning models, for example, is far from straightforward. We will
devote some special focus to Machine Learning later on, but it is important to start
with the concept of Adaptive learning, and Adaptation, based on the thoughts of
Herbert Simon [40], John Holland [41], Melanie Mitchell [42], Peter Todd [43], and
Richard Belew [44], among others, that somewhat anticipated and advocated the
idea of Learning in Agent-Based Models.
In 1991, Holland and Miller developed the concept of artificial adaptive agents
(AAA), [4]. According to the authors, an agent is called adaptive if it satisfies two
criteria: (i) the actions of the agent in its environment can be assigned a value
representing, for instance, performance, utility, payoff or fitness, etc., and (ii) the
agent behaves so as to increase this value over time.
Later on, Peter Todd pointed out that the behavioural sciences have focused on
the ways in which the behaviour of organisms changes over time at different time
scales [43]. And he focused on four type of changes: moment to moment decision
making, long-term alterations of strategies, lifetime developmental adjustments and
across life-time changes. These processes are all adaptive, as they involve a change

20 P.Camposetal.
in the behaviour of the individual. However, adaptation requires more than a change
in the behaviour, motivated by the environment or by other individuals.
Belew and Mitchell [32], defined Adaptation as “the capacity for change and
the additional requirement that this change signifies an improvement of fit”.
Furthermore, changes associated with this improvement of fit (sometimes called
fitness) must be accumulated and replicated over time [43]. The measurement of
these improvements is a difficult issue, but some proposals about how to resolve this
problem exist in some sciences, such as Economics or Management. Adaptation is
actually strictly linked to cognitive systems. Herbert Simon in 1955 [40] argued that
adaptation is a sine qua non for any cognitive system and that cognitive science is
a fundamental set of common concerns shared by different disciplines concerned
with systems that are adaptive.
Adaptive individuals or agents are not irrational. Young [45] argues that agents
adapt but they are not also Hyper-rational: “They look around them, they gather
information, and they act fairly sensibly on the basis of their information most of
the time”, Young [45, p. 5]. The rationality of economic agents is a very important
question in economic science. Simon [40] developed a behavioural model of rational
choice where he replaces the global rationality assumed previously in some work
in economics by a “kind of rational behaviour that is compatible with the access
to information and the computational capacities that are processed by organisms,
including man, in the kinds of environments in which such organisms exist”. Simon
compares the psychological concept of “aspiration level” of the individuals with
the economic concept of the “opportunity cost” in the payoff values. He also
discusses the difficulty of humans in being truly rational when all alternatives are
evaluated before a choice is made. The author [40] simplifies what he calls the
“classical” concept of rationality where there is some hyper-rationality involving the
computation of all possible payoffs involving all alternatives in a decision making
process. The author argues that “there is a complete lack of evidence that, in actual
human choice situations of any complexity, these computations can be, or are in
fact, performed.” This approach uses some concepts from Psychology to solve the
apparent paradox of the economic theory where there is the attempt to deal with
human behaviour in situations in which that behaviour is at least “intendedly”
rational.
The definition of Holland’s artificial adaptive agents discussed earlier was
applied to economic theory too. Holland and Miller in 1991 [4] argued that
“economic analysis has largely avoided questions about the way which economic
agents make choices when confronted by a perpetually novel and evolving world”.
So, an economy can be viewed as an adaptive system, where adaptive agents
aggregate. A complex adaptive system, as defined by Holland and Miller [4] is “a
complex system that contains adaptive agents, networked so that the environment of
each adaptive agent includes other agents in the system”.
Coming from the fields of Artificial Intelligence and particularly Machine
Learning, the theory of complex adaptive systems made it possible to develop well
defined and flexible models that exhibit emergent behaviour. The work of Holland

2 ABL 21
regarding Genetic Algorithms, based on biological metaphors, [46] introduced a
formal framework for the adaptation process.
In this framework, there are three associated objects in the centre of the study:
the environment, E, an adaptive plan, P (which determines successive structural
modifications in response to the environment), and M, a measure of the performance
of the structures in the environment. Some authors used Holland’s framework and
other’s to represent their adaptive systems. For example, [47], and [45], examined
adaptation in organizations of intelligent artificial agents. Holland [46] concludes
that concurrent learning mechanisms generate the ability to learn strategies which
can be either adaptive or maladaptive. Therefore, performance and form of organi-
zations depend on several characteristics, such as environmental change, agent and
structural learning, and the emergence of institutionalized strategies.
2.2.2 Computational Equivalence
Chen and Tai [33] use the concept of Computational Equivalence (see also [48],
and more recently [49]), that makes a bridge between human intelligence and
computational intelligence. The authors take up the general description of the
agents’ properties (Autonomy, Social ability, Reactivity, and Pro-activeness) that
apply well to the economic literature, to describe how agent (and specially) agent
algorithms can be considered adaptive. They start by referring to the Lucas criterion,
where a comparison of the behavior of adaptive schemes with behavior observed in
laboratory experiments involving human subjects (used in Experimental Economics
and Behavioral Economics) can facilitate the choice of a particular adaptive scheme.
But, on the other hand, [33] explore, as an alternative, the concept of agent
engineering and suggest computational equivalence as something that contributes
to complex adaptive economic systems.
Computational Equivalence (CE) has been introduced firstly by Herbert Simon
[48], and it provides a competing explanation for the failure of some adaptive
schemes to replicate the experimental results. The question behind the idea of CE is
the following: “what will happen when the participating human agents are equipped
with computational intelligence tools in a complex adaptive environment? This is
the principle of CE: the capacity of human agents to behave by choosing exactly
the same form of agent engineering. (a kind of digital twin between human and
software/artificial agents?)
However, CE is hard to implement in human beings. Limited time and computa-
tional constraints makes it impossible for the humans to carry out computationally-
intensive adaptive schemes, at least nowadays. Chen and Tai [33] propose the CE
lab framework, where human agents have access to computers. This is a kind of
augmented intelligence given by CI (computational intelligence). Human agents are
therefore equipped with CI tools in a complex adaptive environment to solve specific
problems using fuzzy logic, neural networks, and genetic algorithms.

22 P.Camposetal.
But do agents need to understand the CI methods they use? For example, in
Internet auctions, artificial software agents support human bidders with routine tasks
to improve performance precision (see [33])
This is the main issue in Computational Equivalence: can we think of CE as
a digital twin of a human agent? This discussion can be deepened further by
measuring the impacts of the inclusion of artificial agents on an already-existing
society composed of only human agents artificial agents? And vice-versa. In other
words, we may ask if artificial agents do influence human behavior? [50].
2.3 Learning and Evolution
Agents adapt their behaviour in response to others’ behaviour and to the environ-
ment, in an interactive decision making process where learning plays an important
role. According to [23] we can view the problem of the adaptation of a group
of agents in two different ways: either as an individual characteristic of the
agents—learning—or as a collective process bringing reproductive mechanisms into
play—evolution. It is possible, though, to build an overall view of an adaptation
process which is simultaneously individual and collective.
The issues connecting adaptation, learning and evolution have been studied by
several scientists in Biology an Zoology including Darwin [51], Lamarck [52],
Baldwin [53], Hinton and Nowlan [54] and many others. Their research areas are
very diverse. Indeed, Psychology and Biology were, latu sensu, the original fields of
inspiration of those who studied adaptation, but up to date the concepts of adaptive
learning and evolution have spread into other fields of knowledge and can be found
in almost every subject, from Chemistry and Physics to Economy, Marketing and
Computer Science.
Several adaptive mechanisms of learning have been systematized by Young [45]
in the Economic and Social Sciences:
• Natural Selection Individuals that present higher levels of fitness (well adapted
individuals) are at a reproductive advantage compared to individuals that present
lower levels of fitness (maladapted individuals).
• Imitation Individuals copy the behaviour of others, especially behaviour that is
popular or appears to yield higher payoffs;
• Reinforcement learning Individuals tend to adopt actions that yielded high
payoffs in the past, and avoid actions that have yielded low payoffs. This is the
standard learning model in behavioural psychology and it has gained the attention
of economists. As in imitative models, payoffs describe choice behaviours but it
is “one’s own past payoffs that matter, not the payoffs of others” [45];
• Instance-Based learning Individuals use actual information about the envi-
ronment and other individuals. When a new action has to be adopted by an
individual, a set of similar related actions is retrieved from memory and used
to decide about the new action to adopt.

2 ABL 23
It is difficult to say what the best model of learning is. It would be desirable to
have a model of learning that incorporates elements of all these models.
Previous section introduced the importance of adaptation and individual
behaviour and how interactions at this micro level could maintain the whole system
working. If we see the interactions in the system as playing a game, a question
arises as to whether the game is always played in the same way. In other words, do
individuals evolve their strategies? Are they adaptive? Is there any kind of learning
behaviour?
Some research focused on game dynamics aiming at finding the patterns of
evolution in games and players [22]. In game dynamics it is possible to model
how individuals or populations change their strategy over time based on payoff
comparison—these game dynamics assume that strategies with higher payoff
perform better.
One of the most important game dynamics is the replicator equation defined
for a single species by Taylor and Jonker [55]. The replicator equation captures
the essence of selection. This equation emerges from individuals making rational
decisions on how to imitate observed strategies that currently receive higher payoff.
It is a simple model of evolution and prestige-biased learning in games, where
players are born with their own strategy and then imitate others’ strategies. An early
success of evolutionary game theory is then the result that an evolutionarily stable
strategy (ESS) is dynamically stable for the single species replicator equation.
In 1973, Smith and Price [56] defined Evolutionary Stable Strategy (ESS) for
a single population game in terms of the current state s and a perturbed version
s0=Ex+(1−E)swhere s is the perturbed population, mostly “contaminated” with
. 0.
x, and s is the original resident strategy (majority). The quantity x is the invading
(mutant) strategy,andEis a small number representing the fraction of mutants. The
.
perturbed version is referred to as a (E−) small invasion of (x−) mutants. For a
. .
single population the formal definition is as follows: The current state s is an ESS if
f(s,s0)>f(x,s0)for allx =s and for allE >0sufficiently small.
. . .
Some research regarding game dynamics and the replicator equation applies
to social sciences and particularly to economics. Cooperation and evolutionary
dynamics have been studied by Cressman et al. [57] in the public goods game, a
standard experimental game in economics where subjects secretly choose how many
of their private tokens are put into a public pot. Authors conclude that stability of all
these equilibria under standard evolutionary dynamics (i.e. the replicator equation
and the canonical equation of adaptive dynamics) is characterized.
Friedman [58], uses evolutionary game models of financial markets to explore
the way how players adapt according to the primary characteristics that embody the
mottoes “survival of the fittest,” “evolution not revolution,’ and “natural selection”.
The author introduces several types of learning models, such as adaptive learning
(where traders systematically change their actions in response to personal experi-
ence). Learning variants include: observational learning in response to other traders’
experience, direct imitation of more successful traders’ actions, and active learning
by trying actions more for their informativeness than for their direct profitability.
Emerging strategies have been studied by Saha and Kavitha [59] when dif-
ferent types of replicator dynamics capture inter-agent interactions in financial

24 P.Camposetal.
environments. The authors created a network where agents connect through credit
instruments borrowed from each other or through direct lending. They considered a
large population in which the agents adapt one of the two available strategies, risky
or risk-free investments and in these scenarios the replicator dynamics converges to
an equilibrium at which the expected returns of both the populations are equal.
2.4 Integrating Cognitive and Social Levels: A History of
ABM
The notion of ’intelligent agents’ or ’software agents’ has been an area of study
within Artificial Intelligence at least since the late 1960s and early 1970s [60–63].
Some of the early roots of this study can be traced back to the work on robotics
and planning [62, 63]. Shakey, the robot, was conceived by SRI International in
1965 to integrate the different areas of AI at that time, including representation
and reasoning, planning, machine learning, computer vision, natural language
understanding and speech understanding. See Kuipers et al. [63] for a fascinating
history of Shakey and the generation of robots that were inspired by Shakey. The
notion of ’agents’ as autonomous entities that sensed their environment through their
sensors and were able to take appropriate actions through their effectors emerged
from this work. Simple reflex agents that could execute simple condition-action
rules emerged from this early notion of agents. Early reflex agents had no concept
of a state. Having a state and taking actions that were conditional upon the state
of the agent (e.g., situation-action rules or state-action rules) became an important
property of agents leading to state-based agents or model-based agents. Next, agents
were designed to achieve a certain goal using a process (i.e., sequence of tasks or
plan) and were called goal-based agents.Firby[64, 65] introduced the notion of an
Reactive Action Package (RAP) that can be categorized as a behavior to achieve the
goal.
This was followed by the Procedural Reasoning System (PRS) [66, 67] that
combined both deliberative and reactive planning. In addition, the state of the agent
was now a complex mental state consisting of beliefs, desires, plans, and intentions,
and was called a rational agent [68]or cognitive agent. Beliefs represent the agent’s
information about itself, its environment and other agents in the environment.
Desires are goals or objectives (i.e. what the agent desires as the final state of
the system) corresponding to the motivation of the agent. Both desires and goals
play important roles in practical decision making. Desires may be viewed as
motivational forces inside agents, and goals as desirable states that the agents try
to reach. Intentions are commitments to achieving particular goals. They represent
the currently chosen course of actions intended to be taken to achieve the desires.
In other words, intentions can be seen as a sequence of actions that the agent
takes in order to achieve its desires. Intentions play an important role in practical
reasoning and can not be reduced to beliefs and desires. Desires capture the
deliberative component of the agent [68]. So, the BDI architecture [69] views an
agent as someone that is rational and has mental attitudes of Belief, Desire and

2 ABL 25
Intention representing, respectively, the informational, motivational and deliberative
conditions of the agent.
The work on the Procedural Reasoning System led to the theoretical underpin-
nings of the BDI architecture for agents and was inspired by the work of Michael
Bratman on Practical Reasoning [70]. The study of rational agents included sym-
bolic reasoning as well as probabilistic and utility-maximizing agents, often referred
to as utility-based agents. The mid-1980s also saw the emergence of reinforcement
learning [71, 72] as a mechanism for agents embedded in an environment to learn
from their actions leading to learning agents.
The early references to agents were largely in the area of planning. Russell
and Norvig [73] in their seminal textbook recast the field of AI as the study of
intelligent agents—both the engineering discipline of building intelligent agents
that can sense, think, and act to achieve goals as well as the theoretical foundation
that helps us understand artificial intelligence. In the late 1980s and 1990s the
field expanded from designing and building single agents to designing and building
multiple agents leading to multi-agent systems. A series of workshops on Modeling
Autonomous Agents in a Multi-Agent World (MAAMAW) [74, 75], forerunner
to today’s international conferences on Modeling Autonomous Agents and Multi-
agent Systems) (AAMAS) [76, 77], addressed the design and implementation of
multi-agent systems. While the multi-agent systems community approached the
interaction of rational agents, another group of researchers were studying the
evolution of life and the emergence of complex properties from simple agents.
Artificial Life and complex adaptive systems [78, 79] researchers were studying
how very simple rules in agents led to surprisingly complex emergent behaviors
(e.g., a flock of birds flying in a formation). Central to the study of artificial life
was the notion of emergent properties and also an environment to simulate simple
agents. This led to the birth of Netlogo [80], a popular platform for exploring
emergent behaviors and studying the interaction of multiple agents. The popularity
of individual and multi-agent systems led to the call of using this as a paradigm
for programming, called agent-based programming [81]. A number of agent-based
languages and virtual machine architectures were built to realize these programming
paradigms [82, 83].
Single agent systems and multi-agent systems were used in a variety of appli-
cations including robotics, air-traffic management [84], space shuttle diagnosis
[85], air-combat modeling [86], telecommunications network management, medical
diagnosis, etc. A number of commercial tools to build these multi-agent systems
emerged during this time along with agent-oriented methodologies to assist devel-
opers in defining, building, and testing such systems. This also led to agent-oriented
methodologies that improved upon the object-oriented methodologies [87]. Some
of these methodologies have now been re-architected for cloud deployment.
Several researchers extended the role of rational or cognitive models in social
simulation. Gilbert [88] suggested that “it is possible to distinguish at least a
biological, a cognitive and a social level [of analysis], in which the characteristics
of phenomena at one level are emergent from the behaviour of phenomena at
levels below” [88]. In 2023 Wall explored explores cognition in organizational

26 P.Camposetal.
learning by suggesting an algorithm that captures key elements of Simon’s concept
of satisficing which received considerable support in behavioral experiments [31].
BDI architectures were extended with social commitment and team plans to address
social behaviors and applied to interesting problems, such as air-combat modeling.
The BDI architecture has been criticised by many researchers, including Rao and
Georgeff [69]. Some say that it is very reductive: sociologists and scientists from
Distributed Artificial Intelligence argue that there are other cognitive aspects that
should be introduced in the model. On the other hand, classical decision theorists
question the necessity of having all these three attitudes. Other authors argue that it
is hard to find a mechanism that permits an efficient implementation of the mental
attitudes: beliefs, desires and intentions. However, the BDI-architecture has been
used in many applications as described above and it seems to be adequate in dealing
with many situations. Furthermore, the concepts of beliefs, desires and intentions
are easy to understand and the BDI–architecture has the advantage that it is intuitive
and relatively simple to identify the process of decision-making and how to perform
it [89].
2.5 Agent Learning Approaches
Alongside the area of mechanism design, and perhaps the computational questions
surrounding solution concepts such as the Nash equilibrium, Multi-agent learning
(MAL) is today arguably one of the most fertile interaction grounds between
computer science and game theory, and the next generation of LLMs (Large
Language Models) will probably not be isolated models, but multi-agent systems
where LLMs learn, reason, and act strategically in the presence of other intelligent
models.
Until now we were referring only to agents, which may represent intelligent
entities (people, animals, companies, institutions), that we want to simulate based
on Agent-Based Models, as in the perspective of ACE (Agent-Based Computational
Economics). But agent-based learning approaches look at agents also as pieces of
software that help a system learn, and the goal is not exactly (and not always)
to simulate an intelligent entity, but to be able to solve other problems, such as
segmenting the customer market, or predicting the weather for a month from now.
Consequently, the task of agent learning has an important role here. According to
[14], learning can be individual (agents adapt based on their environment), social
(agents learn from or about others strategically), or group-based (agents coordinate
for collective benefit).
We will focus on different taxonomies of learning by combining the machine
learning perspective, and the game theoretical perspective. In the vision of Bogner
et al. [90], machine learning is mainly used in ABM for two main purposes: (i)
the modelling of adaptive agents equipped with experience learning and, (ii) the
analysis of outcomes produced by a given ABM. This latter purpose is related to
the analysis of the simulation output: handling the model, understanding the exact
model behavior and extracting meaningful insights from simulation results. In the
following, we will introduce different perspectives of agent learning approaches.

2 ABL 27
2.5.1 Game Theoretical Learning and Artificial Intelligence
Some authors such as Shoham et al. [1] and recently Mitchell [91], consider two
fundamental perspectives of learning in the literature: the AI literature and the game
theoretic literature, even though the shared aims are greater than the differences.The
example of simple game with two-players’, (like in the prisoner’s dilemma), is used
by Shoham et al. [1] to demonstrate Single Agent and Multi Agent Learning. In this
game, the row player teaches the column player to play in a way that benefits both.
For that reason, the authors say, that “it might be more appropriate to speak more
neutrally about multi-agent adaptation rather than learning”.
The learning building blocks in [1] are depicted in Fig.2.3, where a distinction
is made between two different perspectives of agent-based learning: the game’s
theoretical perspective and the theories of Multi-Agent learning. The former are
focused on the types of games agents use to learn (repeated versus stochastic), while
the latter address the perspective of researchers (descriptive versus prescriptive).
Mitchell’s perspective [91] is different, and follows the ideas of Rosaria Conte
[92], where learning can be seen outside the scope of game theory. In that sense,
the human-like learning is confronted with the not-human like learning. The
human-like learning corresponds to symbolic AI, a collection of methods that are
based on human-readable representations of problems, logic and search. Although
the symbolic approach has been the dominant approach for years, the symbolic
approach may eventually be abandoned in favor of subsymbolic AI approach, due
mainly to technical limitations of the algorithms. In the early 2000’s, attention was
drown [92] to the explainability of symbolic AI (such as learning classifier systems),
and the lack of such explainability in subsymbolic learning when dealing with neural
networks, for example (Fig.2.4).
Most work in artificial intelligence concerns the learning performed by an indi-
vidual agent [93]. Individual agents learn to function successfully in an environment
that is unknown and potentially also changes as the agent is learning. However, in
Multi-Agent learning, environment contains other agents and the learning of the
Fig. 2.3 Shoham’s building
blocks [1] for learning in
MAS
’

28 P.Camposetal.
Fig. 2.4 Mitchell’s [91] building blocks for learning in MAS
other agents will be impacted by the learning performed by our agent protagonist.
This is why sometimes the challenging is not the way how agents learn, but also
how agents are taught by other agents.
2.5.2 Non-conscious Learning, Routine-Based Learning and
Belief Learning
According to Thomas Brenner [94], there are essentially three ways of learning in
economic literature (see Fig.2.5): Non-conscious learning, Routine-based learning
and Belief learning. Reinforcement learning may be seen in the perspective of a
non-conscious learning type, since it has been studied in Psychology with different
kinds of animals and corresponds to the situation where actions leading to negative
outcomes (a punishment), will be avoided in the future, while actions with positive
outcome (a reward) will reoccur. Routine-Based Learning is the type of learning
where imitation plays an important role, such as in a child’s perspective, or the rule
to imitate local people whilst in a foreign country for the first time. In this way one
quickly learns about the traditions there and adapts behaviour.
On the other hand, in belief learning we are able to understand the mechanisms
that govern our surrounding and life. Nowadays, this is mainly studied in psychol-
ogy under the label of learning and is referred to as cognitive learning, where mental
models and belief learning play important roles. Belief Learning focuses on how
agents update and revise these beliefs over time as they gather new information or
interact with the environment.
Following this perspective, John Duffy [95] recalled that there are also ‘zero
intelligence’ agents with rationally minimal intelligence that produce higher per-
formance than real human agents in structured market institutions; Besides these
(i) Zero intelligence agents, there are also (ii) inductive learning trading models,
that have been used to identify learning mechanisms undertaken by human agents

2 ABL 29
Fig. 2.5 Brenner [94] building blocks for learning in MAS
in complex market situations; and (iii). Evolutionary trading models, where genetic
algorithms and other computational models are used.
2.5.3 A Combination of Methods
The problem of agent-based learning has been posed differently by Vidal [96], but
with a similar perspective: machine learning algorithms are developed and applied
that increase the ability of an agent to match a set of inputs to their corresponding
outputs. In other words, a large, sometimes infinite, set of examples E is assumed.
Each examplee ∈ E is a paire = a,bwherea ∈ Arepresents the input the agent
. . .
receives andb∈Bis the output the agent should produce when receiving this input.
.
Therefore, the goal of the agent is to find a function f which mapsA → B for as
.
many examples of A as possible.
The use of Machine Learning approaches in agent-based modelling have been
used for two main applications [3, 90]: (i) modelling adaptive agents that can learn
from experience through reinforcement learning approaches; and (ii) analysing and
post-processing the (often large-scale) outcomes of running a given ABM.
We will discuss these types of learning in more detail and introduce machine
learning as a possible form of agents learning. The field of Machine Learning is con-
cerned with the question of how to construct computer programs that automatically
improve with experience [97]. Machine Learning draws on concepts and results
from many fields, including statistics, artificial intelligence, philosophy, information
theory, biology, cognitive science, computational complexity, and control theory.
Chen and Tai [33] considers that Multi-Agent Systems can be seen a combination of
computational intelligent methods, drawn from Machine Learning methods. These

30 P.Camposetal.
computational intelligent methods are a way of solving the paradigm of Rober
Lucas who suggested using laboratories with human agents, known as Experimental
Economics. However, since the laboratories were not computationally equipped
to meet the demands of the selection tasks of human behaviours in economics,
the authors establishing a laboratory where human subjects are equipped with
the computational power that satisfies the computational equivalence condition.
Therefore, following [33] three great groups of methods are identified to meet
this computational intelligence capability: Fuzzy Logic, Neural Networks and
Evolutionary computation. However, human agents may combine several different
computational intelligent tools into a hybrid system to learn and adapt (Fig.2.6).
And there is still the possibility of combining different CI methods, as hybrid
systems, in which many tools work synergetically together as a Multi-Agent System.
This may be compared to a type of metalearning, where agents can compare
different adaptive schemes and choose a combination of them.
2.6 Machine Learning
Let us briefly consider what distinguishes Machine Learning (ML) from multi-agent
learning. We start with single agent learning and proceed with other approaches.
From the perspective of Machine Learning there are mainly three types of learning
approaches depending on the nature of the target variable or “feedback” available to
the learning system:
• Supervised Learning
Learning with a target or label. The agent is supervised in every way in
advance (ex. Neural Networks, Support Vector Machines, Random Forests, etc.)
Fig. 2.6 Chen and Tai’s [33]
building blocks for learning
in MAS

2 ABL 31
• Unsupervised learning
Learning without a label. The answers to the problems are not available with
the agent in advance (Association Rules, Clustering, etc.)
• Reinforcement Learning (RL)
There is no explicit target, but a goal to optimize. In RL the agent is given
some reward occasionally for completing any task. The goal is to build a system
that improves the performance through interactions with the environment [98,99]
Machine Learning models have been used by Angione et al. [3], as these can
facilitate more robust sensitivity analyses for the ABM while also reducing CPU
time consumption when calibrating and analysing the simulations. In this approach,
Machine Learning methods are used to generate statistical models that replicate
the behaviour of the original ABM to a high degree of accuracy. The ‘Linked
Lives’ model of social care provision in the UK, which models the interaction
between supply and demand of informal social care has been used to present a useful
comparison of methods for generating surrogate ABMs. Once the simulation runs
were completed, the authors chose a selection of the most commonly used machine
learning methods to evaluate as possible means for creating surrogate models of the
ABM:
• Neural Networks
• Support Vector Machines
• Random Forests
• Linear Regression
• Gradient Boosted Trees
• K-NN
• Gaussian Processes
• Decision Trees.
All these different Machine Learning methods were implemented to attempt
to replicate the behaviour of the ABM, and Neural networks were the strongest
performers overall. Gradient-boosted trees and non-linear SVM have generally a
slightly higher error, but considerably faster runtime.
This vision is in line with [90], for whom machine learning may be used in ABM
for the analysis of outcomes produced by a given ABM, namely handling the model,
understanding the exact model behavior and extracting meaningful insights from
simulation results. The authors establish a classification where they combine ABM
steps, overall goals and machine learning methods.
As the area of machine learning covers many different approaches, let us now
limit our attention just to supervised learning. The tasks in this area require a set of
training examples (these include the values of the target variable) characterizing a
given source task and a learning method (e.g., decision tree, neural network, etc.)
to learn a model (trained decision tree, neural network, etc.). This process may,
in addition, include other knowledge (meta-knowledge), that helps to guide the
learning process. It may indicate, which learning method is useful for with type
of task. The learned model is then applied to the target task, which in the context of

32 P.Camposetal.
supervised learning, would predict the value of the target variable. In early works
in the area machine learning is was assumed that the source and the target tasks are
rather similar to facilitate the process.
Later, this assumption was dropped, and the researchers were interested to
enhance the methodology so that the learned model could be adapted to new settings
associated with the target task. In this context, the term transfer learning was often
used to refer to this process. In approaches that involve deep neural networks, the
idea of transfer learning attained a special importance, as it served as a relatively
easy way to adapt a pre-trained model to new settings by so-called fine-tuning. As
fine-tuning required only a few examples, it is sometimes referred to as few-shot
learning.
So, to summarize, Machine Learning requires certain information to learn, which
is normally provided by the user, although some works use also data acquired by
from other sources (e.g., observation of the environment). If we consider the user
as an agent, we see that the scheme of single-agent learning can be transformed
into two-agent learning. The user can, in this context, be regarded as the teaching
agent, who has the role of teaching the learning system to resolve certain tasks.
The learning system acquires a trained model as a result. This process is sometimes
referred to as inter-agent transfer learning (TL) [100, 101], to distinguish it from the
transfer learning discussed afterwards, when the agent is trying to adapt the learned
model to a new context (i.e., intra-agent transfer learning). In the following we
will use the term transfer learning instead of the longer version inter-agent transfer
learning.
More details about transfer learning between two agents are given below. We
will distinguish between two somewhat different transfer learning tasks. The first
one involves simple supervised tasks that require the application of a supervised
machine learning method, such as classification or regression. The second group
involves more complex tasks that typically involve an application of a sequence of
actions (policy) to achieve some given goal state. The focus on transfer learning (TL)
is motivated by the observation that the traditional approach that uses reinforcement
learning (RL) where so called Q-values are attributed to states does not really scale
up to more complex problems. So, we need effective ways to reuse the existing
knowledge that is around.
The final section is dedicated to situations that include multiple agents, whose
aim is to resolve a set of given problems. In this setting the solution can be improved
not only by individual learning (e.g., learning of one of the agents), but by adopting
a different policy.

2 ABL 33
2.6.1 Transfer Learning Between Two Agents
2.6.1.1 Transfer Learning in Simple Supervised Tasks
In this section we consider how can one agent (teacher) aid another (learner) to learn
a simple supervised task, such as classification of regression. This can be done by
supplying the learner agent with the following transferable knowledge sources:
1. training data
2. learning bias,
3. trained model or system (e.g., a trained decision tree, deep neural network, etc.)
So, supplying training data to the learning system is an important aspect in
transfer learning. The assumption here is that the recipient has the capacity to
learn, by invoking some of its learning subsystems (e.g., decision tree, deep neural
network, etc.) that could be trained. Another aspect that affects the outcome of
learning is so-called learning bias that affects the learning process. In other words,
the outcome depends on how the learning process is configured. Different options
constitute the so-called configuration space [102]. Many studies carried out in the
past were concerned with the question of which features are important and how
these should be organized (e.g., a flat list, hierarchy, etc.). Others have studied which
classifiers (or other ML algorithms) should be used in the experiments for a given
task. These studies often explore the experimental results of different classifiers (or
other ML algorithms) on past problems. The issue of which hyperparameters affect
most the performance and which values should be tried out when dealing with a
particular task was investigated by many researchers. All these aspects affect the
configuration space that is then explored by the respective learning subsystem(s).
The term meta-knowledge is often used to refer to the different aspects of learning
setup. In the area of Machine Learning that does not involve agents, these aspects
were normally determined by the user. In multi-agent setting it would be useful
to have a way to transmit this knowledge from one agent to another, enabling the
recipient agent to learn more effectively. The transferable knowledge source (3)
mentioned above involves passing the outcome of learning, namely the trained
model or system (e.g., a trained decision tree, deep neural network, etc.). This
option is viable if the recipient agent (learning agent) can interpret the format of
the model passed by the teacher agent (e.g., a decision tree, or deep neural network,
etc.). One alternative of this kind was contemplated by Brazdil et al. [103], where
different agents were able to construct individual models in the form of rules, which
were then merged into a single combined rule set. The authors have shown that
the final rule set had superior performance when compared to the rules obtained
by a single agent. The outcome of learning can be exploited in different ways. One
example involves the so-called word embedding that can be extracted from deep
neural networks after processing large quantities of texts (e.g., Wikipedia articles).
These can capture the contextual information accompanying a given word. They can

34 P.Camposetal.
be exploited in various tasks, such as, determining similarity between words within
a given context, or whether one term implies another.
2.6.2 Transfer Learning in More Complex Tasks
Let us now consider the more complex tasks that require an application of a
sequence of actions (policy) to achieve a given goal state. As the user is normally
used to label the attempts as successful or not, this area is often referred to as
reinforcement learning. The user’s feedback regarding the success of a particular
sequence of actions reinforces the system to explore the more promising paths.
Although this area was rather popular for many years, the fact that the methods
did not really scale up to more complex applications, led various researchers to
reflect about the causes and suggest alternative ways to address the problem. Here
we consider the following approaches that were suggested before that mitigate this
problem:
• Separating tasks into subtasks and carrying out off-line training
• Learning from demonstrations and imitation
More recently, [104] proposes a multitask-based training framework termed
MTT in cooperative MARL (Multi-Agent Reinforcement Learning), which aims
to learn shared collaborative knowledge across multiple tasks simultaneously.
2.6.2.1 Separating Tasks Into Subtasks and Carrying Out Offline
Training
When the chain of operations is rather long, reinforcement learning may not be
very effective [105]. An alternative to this is training the agent offline on a shorter
sequence of tasks/actions, as this is often done in human learning (e.g., training the
service in the game of tennis) and exploit supervised learning. In some situations,
the generation of the training examples can be done with the recourse to a random
process. Also, labeling the outcome of agent’s operations/actions can be done by the
same agent involved in the learning process.
2.6.2.2 Learning from Demonstrations and Imitation
This mode involves a teacher and learner agents. Demonstrations can be given by
providing a partial information about state/action pairs. The partial information can
be in different forms, i.e., include a subset of state/action pairs, or only information
about some states to be visited while trying to attain the goal. A good overview
of the works in this area is provided by Da Silva and Costa [101]. However, many
authors have contributed to this area before, and we review some of the early works

2 ABL 35
here. One important task in this area is the so-called pole-balancing problem, which
was studied by Michie and Chambers [106]. The objective of this problem is to
balance a pole (an inverted pendulum) that is connected by a ball-baring pivot to
a cart driven by a motor. The movement of the cart is restricted to the horizontal
axis by a track, and the pole is free to move about the horizontal axis of the pivot.
The objective is to control the cart so that the pole would continue to be balanced.
An approach called BOXES has been used by Michie and Chambers [106] for
controlling the cart. They partitioned (pre-processed) into discrete regions called
“boxes” to make the problem manageable. The authors were inspired by the way
humans dealt with this problem. Data from past experiments was used to update the
control variables. In the subsequent years many different approaches were used to
obtain the controller, including adjusting a linear solution, training a neural network
or by evolutionary approaches. The area of learning by demonstration had many
followers in the subsequent years. System ELM [107, 108] could learn to solve
arithmetic and algebraic problems. The given rules (clauses) were reformulated, as
a result of learning. Many operations involved could be described as specializations.
The system searched for a solution by expanding the search space. The system was
given a “trace”, consisting of a sub-sequence of states to be visited on the way to
reach the goal state. These states were in the form of valid arithmetic or algebraic
expressions. This provided a useful help in the search, but if enough computing
power were available, the system could reach the required next state without it.
Various researchers (e.g., [109] and [110]) investigated one application in the
area of behavioral cloning. The aim of these works was to synthesize artificial
controllers that are robust and comprehensible to human understanding. This area
is sometimes also referred to as reverse engineering of human control skills. In
the work of [110] the methodology involved the following steps. It starts by
characterizing of the system being controlled as a set of state and control variables,
representing the system status and decisions made by the human controller. This
is followed by the definition of a task plan as a temporal sequence of stages. Then
each control task is executed by the human controller following the task plan. While
performing the control task the system’s state and control variables are recorded at
regular intervals, generating the behavioral traces. These are then pre-processed to
produce datasets to be used by ML tools to induce an artificial controller for each
stage. Finally, different components for each stage are assembled into an artificial
controller. Different ML tools have been used by Camacho and Brazdil [110] in
this process, but preference was given to those that give intelligible output. The
controllers synthesized by Cart in the form of multivariate decision and regression
trees revealed to be the most robust.
The area of learning by imitation is similar to the area of learning by demonstra-
tion. The distinguishing feature is that it does not involve an act of demonstrating a
certain sequence of actions, but rather observing someone performing these actions.

36 P.Camposetal.
2.6.3 Tasks That Involve a Group of Agents
This scenario involves a set of tasks that is attributed to a group of agents to
carry out. The aim of the system is to define an effective policy (plan) for each
agent, determining which methods, algorithms or primitive operations (together
with their hyper-parameter settings) should be executed and when. This would
normally be done by a planner (scheduler), although retrieval of suitable past plans
and possibly their revision/adaptation to the current task can also be considered.
Both centralized and distributed solutions to this task are discussed by Ferber
[23]. Planning (scheduling) requires that the given subtasks, methods and agents
are characterized, enabling to determine, for instance, which agents can execute
which methods, or which agents or methods should be allocated to which tasks,
while optimizing certain criteria and respecting certain restrictions. In general, this
requires that the agents coordinate their plans and refine their own plans, while
negotiating over resources [111, 112].
The area of metalearning developed ways to characterize the performance of
algorithms on past tasks using the performance metaknowledge. These techniques
could be useful in the process of characterizing subtasks, methods and agents and
hence facilitate the process of assigning the given methods and agents to the given
subtasks.
We note that a particular set of plans or policies associated with each agent can
be analyzed and often improved further leading to improved overall performance,
as judged by certain measures, such as total time to reach the goal state or the total
consumption of resources by all agents. Certain indicators, such as conflict over
given resources, can be used a signal indicating that it may be possible to improve
the given performance measures. If it is indeed possible to improve the set of plans
or policies, the outside observer may be lead to think that the system has “learned
to do things better”, as a result. The learning in this case is achieved by a better
organization of who does what, akin to what happens in the area of ant colony
optimization.
More recently, deep learning methods start appearing to solve real life problems,
as they outperform not only classical methods, but also human benchmarks in
various tasks like image classification or face recognition. Deep learning is a subset
of machine learning, which is essentially a neural network with three or more layers.
These methods are somewhat new in Economics. According to [113], Economics
have not yet benefited from the developments, and therefore now is the right time
to apply Deep Learning and multi-layer neural nets to Agent-Based Models in
economics. Indeed, dealing with millions of interaction and generating Big data
make the target models large-scale agent-based models. The advantage of such
large-scale, high-resolution, high-fidelity agent-based models is that they can be
used as virtual laboratories, or as laboratory “in silico”, such as suggested by
Tesfatsion [16], also in line with the perspective of the computational intelligence
perspective of [33]. Examples of such models that are useful to be tested with big
amounts of data and that may be not tested in reality include [113] problems to deal

2 ABL 37
with what happens when the biggest banks go bankrupt, or: what happens when a
Euro member leaves the Euro.
2.6.4 Systemic Learning: Learning as a Whole?
Systemic learning draws on the five disciplines of the learning organization as
outlined by Senge [114]. This holistic view supports cause-and-effect relationships
between data and people and enhances individual and collective decision making
by considering an integrated approach to learning. Later in this book we describe in
more detail the way how this approach is integrated, where learning is assumed to
be decentralized and different learning agents are heterogeneous. These agents act
as components of a system that functions as a whole, and each component can have
different functions in this system. The five disciplines are:
1. Personal mastery: This discipline is associated with continuous developing of the
agent’s personal vision, proficiency and seeing reality objectively. According to
Peter Senge, agents need vision (the future that they desire, based on a purpose),
goals, and objectives to help achieving the vision. Agents also need creative
tension, commitment to truth and other characteristics.
2. Mental models: Agents may be capable of building their own mental models as
an abstraction of its environment and deepening their individual vision. Mental
models can be seen as personal algorithms. Mental models involves individuals
actively using data to test their interpretations and conclusions, so we need data to
be able to build these mental models and endow them with learning capabilities.
3. Building a shared vision: Agents can perform learning by doing individually, that
involves voluntary and non-hierarchical meetings to solve problems, but they can
also learn from each other in a proactive manner.
4. Team learning: This discipline has to do with “thinking together”
5. Systems Thinking (the fifth discipline): this is a holistic view that helps decision
makers understand the cause-and-effect relationships among data and people. It
expands individual and collective thinking skills and improves individual and
collective decision making.
More recently Muntongi and Rigava [115] applied the System’s Thinking to the
City of Harare as a case study in the application of Peter Senge’s fifth discipline to
foster the learning city concept.
2.7 Large Language Models (LLM)
This is the age of Large Language Models (LLM), a type of machine learning
that recognizes and generates text. LLMs can be seen as foundational technologies
behind AI chatbots and can be incorporated as agents within an ABM, where each

38 P.Camposetal.
agent has a specific role and behavior governed by language-based reasoning and
decision-making. These LLM agents can process and interpret unstructured data
(e.g., economic reports, news articles) to make informed decisions, interact with
other agents, and learn from the environment.
LLMs have learning capacities. These can be embedded by integrating LLMs
with Machine Learning techniques like reinforcement learning (RL), where agents
continuously improve their decision-making based on past interactions and feedback
from the simulation environment. The integration of Large Language Models
(LLMs) into Agent-Based Models (ABMs) holds significant potential for under-
standing and preventing economic crises.
One of the key strengths of LLMs is their ability to handle real-time data and
continuously update predictions based on new information. For economic crises,
LLMs can be used to process live streams of economic data, news, and social media
sentiment, allowing the agents within the model to adapt their behaviors in response
to emerging signals. This real-time adaptability makes it possible to identify early
warning signs of a crisis, such as sudden shifts in market confidence, and model
how these signals could lead to broader economic disruptions.
Some authors have already started to develop literature and applications of
LLM with agents in the economy, including financial crises. In [116], the authors
conduct a comprehensive analysis of how large language models can be applied
to Agent-Based Models, including identifying potential challenges and exploring
promising avenues for future research. The work of [117] investigates structures
and techniques for creating LLM-enhanced social simulations and determined that
combining LLMs with agent-based simulations gives researchers and scientists a
strong set of tools.
In the area of Finance, [118] demonstrate GPT-4’s ability to follow natural
language instructions across various financial tasks. Applications include evaluating
sentiment in financial news and predicting stock movements. A practical survey
focused on key aspects of utilizing LLMs for financial tasks is provided by Li et
al. [119]: the authors review current approaches, including leveraging pretrained
models via zero-shot or few-shot learning, fine-tuning on domain-specific data, and
training custom LLMs from scratch.
Four key questions are posed by Ash and Hansen [120] that are central to
assessing LLM value for economic research: (1) replicability of results, (2) adapting
models to economic-specific domains, (3) the trade-off between transparency and
predictive success, and (4) performance evaluation. The reliance on large datasets
raises concerns about data transparency and potential biases, which may affect
research outcomes. On the other hand, the complexity of LLMs poses issues with
interpretability, making it difficult for researchers to understand how the models
generate their results. There is also a risk that increased automation might replace
the role of expert judgment, leading to over-reliance on models without adequate
human oversight. Finally, economists will need to acquire new technical skills, such
as programming and machine learning, to fully harness the potential of LLMs in
economic research.

2 ABL 39
2.8 Integrating LLMs with Agent-Based Models
Agents in an ABM as decision-making entities with learning capabilities can be
enhanced by LLMs [121]. The agents interact within an environment and learn
over time using reinforcement learning (RL) techniques. LLMs provide cognitive
reasoning and natural language processing for each agent’s decision-making, and
the RL mechanism helps agents improve based on feedback from their interactions.
Core components of such system may include:
• Agent Layer (LLM-based agents)—each agent in the ABM is modeled as a
distinct entity equipped with an LLM for decision-making and interaction.
Agents can learn with reinforcement learning from the consequences of their
actions. Agents can interact with each other and the environment.
• Environment Layer—This layer defines the economic system, market conditions,
and social settings in which agents operate. It generates signals and feedback
based on the agents’ actions, simulating market dynamics, economic shocks, or
regulatory changes.
• Knowledge and Data Integration Layer—This layer integrates external data into
the system, allowing LLMs to analyze information from real-world sources
(news articles, market reports, or economic data) that influence the agents’
decision-making processes.
It is possible to integrate learning techniques into LLM-based Agent-Based Models
(ABMs). For example, it is possible to integrate transfer learning and enhance the
learning capabilities of agents by allowing them to leverage pre-trained knowledge
and apply to new, related economic scenarios. LLMs, initially trained on broad
economic datasets, can be fine-tuned to specific crisis scenarios, providing agents
with a more robust starting point. This significantly reduces the learning curve,
enabling agents to perform better right from the initialization phase in simulations.
Transfer learning also enables the sharing of learned strategies between agents in
different scenarios or across domains. Agents that have learned successful behaviors
in one crisis (e.g., the 2008 financial crisis) can transfer that knowledge to agents
operating in new or evolving environments. This knowledge-sharing mechanism
accelerates the learning process across agents and improves overall system perfor-
mance in ABM simulations of economic crises. In combination with reinforcement
learning, agents not only transfer knowledge but also continuously adapt and refine
their behaviors based on feedback from the environment. This approach makes it
easier to model complex economic systems and design simulations that respond
dynamically to new shocks or crises.
2.9 Generative Agent Based Models (GABMs)
The rise of Large Language Models (LLMs) has profoundly impacted both the natu-
ral and social sciences. Generative Agent-Based Models (GABMs), which integrate
LLMs as proxies for human participants, are gaining notable attention. Insights into

40 P.Camposetal.
how LLMs are revolutionizing research in complex systems and behavioral sciences
are provided by Lu et al. [122], who analyze recent developments across various
areas of complex systems, including network science, evolutionary game theory,
social dynamics, and epidemic modeling.
In the work of [123] the authors discuss the emerging use of GABMs and present
a case study where human behavior is incorporated into a simulation of social norm
diffusion within an organization, combining a mechanistic model of interactions
with a pre-trained LLM. The model, designed to be simple for educational purposes,
explores various scenarios and evaluates how changing prompts affect the results.
The proposed GABM framework integrates a LLM and a Mechanistic Model to
simulate human decision-making and interactions in social systems. This model
processes information about each agent and the system’s state, helping to generate
decisions. The mechanistic model simulates the interactions between agents within
the system. This dynamic interaction aims to model complex social behaviors using
a combination of data-driven decision-making and structured agent interactions.
2.10 Conclusions and Final Considerations
This Chapter positions ABM as a key tool in Agent-Based Computational Eco-
nomics (ACE), a framework that views economies as complex systems composed of
interacting agents. ACE has gained traction as an alternative to traditional economic
analysis, especially for studying non-linear dynamics and micro-to-macro linkages
that are not well-captured by Dynamic Stochastic General Equilibrium (DSGE)
models.
The work underscores the bottom-up nature of ACE, where individual agents’
behaviors aggregate into larger economic patterns, allowing researchers to explore
emergent phenomena like market bubbles, systemic risk, and innovation diffusion.
ACE also serves as a “laboratory” for testing economic policies and theories in
controlled, simulated environments. The versatility of ABM in capturing both
microeconomic and macroeconomic phenomena makes it an invaluable tool for
modern economic analysis.
2.10.1 Emergence and Bounded Rationality
One of the central themes of the chapter is the concept of emergence—the idea
that complex, macro-level patterns arise from local interactions among individual
agents. This principle is crucial to understanding phenomena that cannot be easily
predicted by looking at individual behaviors in isolation. For example, models
like the Schelling Segregation Model demonstrate how individual preferences
for being surrounded by similar neighbors can lead to large-scale patterns of
racial or economic segregation. These emergent patterns occur without any central

2 ABL 41
coordination, purely from local interactions. The chapter also discusses how agents
adapt both individually and collectively, a dynamic process central to agent-based
systems. Adaptive agents adjust their behavior in response to their environment,
drawing on cognitive science and machine learning principles to refine their
decision-making processes over time. This capacity for adaptation is a cornerstone
of ABM’s potential to model complex social and economic systems. Our overview
chapter integrates insights from behavioral economics and psychology into the
modeling of agents in economic systems. Unlike traditional models of rational
agents, Agent-Based Models often incorporate bounded rationality, recognizing that
individuals have cognitive limitations and access to incomplete information. This
work discusses how ABM allows for the modeling of diverse decision-making
processes, from satisficing (making decisions that are “good enough” rather than
optimal) to reinforcement learning where agents learn from past experiences and
adjust future behavior based on rewards and punishments. This approach contrasts
with the hyper-rationality assumed in classical economic models. By embedding
agents with realistic cognitive constraints, the models provide richer, more accurate
simulations of human behavior and economic decision-making processes.
2.10.2 Agent-Based Modeling and Learning
We explored the role of learning in ABM, particularly in Multi-Agent Systems
(MAS), and underscored the increasing relevance of machine learning (ML)
techniques in enabling agents to adapt and evolve based on their environment.
Multi-agent learning is seen as one of the most productive intersections between
game theory, computer science, and mechanism design. The chapter highlights
how adaptive agents use learning algorithms—such as reinforcement learning and
others—to adjust their behavior in response to other agents and changing external
conditions. This is especially important for modeling economic behavior where
agents face incomplete information and need to adapt dynamically. This ability to
model bounded rationality and learning in disequilibrium is crucial to understanding
real-world economics.
We identify different learning approaches of agents. Shoham et al. [1] propose a
distinction between two different perspectives of agent-based learning: the game’s
theoretical perspective and the theories of Multi-Agent learning (Fictitious play,
Rational learning, and Bayesian learning), and the theories of Multi-Agent learning
with Reinforcement Learning.
On the other hand, [91], introduced a taxonomy of agent learning approaches,
categorized along two dimensions: Human-like (referring to symbolic AI, which
is more interpretable by humans) vs. Not Human-like learning (that encompasses
subsymbolic AI, such as neural networks) and Games vs. Beyond Games. Within
the “Games” category, methods like Reinforcement Learning and Deep Q-learning
(using convolutional neural networks) are applied to game-like environments, where
agents learn optimal strategies based on rewards and penalties. In contrast, “Beyond

42 P.Camposetal.
Games” includes approaches like Transfer Learning, which allows knowledge from
one task or environment to be applied to others, facilitating learning in more general
contexts.
A different topology of learning was introduced by Brenner [94] with three
different ways of learning: Non-conscious learning, Routine-based learning and
Belief learning. Finally, [33] consider a combination of computational intelligent
methods, drawn from Machine Learning methods: Fuzzy Logic, Neural Networks,
and Evolutionary Computation.
2.10.3 Application to Crises
One of the key applications of ABM discussed in this work is its use in simulating
responses to economic and financial crises, caused by pandemics, and wars.
Traditional economic models often struggle to account for the complexity and
unpredictability of these crises due to their reliance on equilibrium assumptions and
representative agents. ABM, by contrast, uses a bottom-up approach, simulating
the behaviors of individual agents to understand how local decisions lead to larger
systemic outcomes. Systemic risk in financial markets can be quantified through
network-based analysis of interbank liabilities, and a proposed Systemic Risk
Tax—proportional to each transaction’s marginal contribution to systemic risk—
can, according to agent-based modeling and empirical data, restructure financial
networks to be nearly free of systemic risk [124]. In this chapter we cite several
examples where ABM has been used to analyze the impact of government inter-
ventions, such as the 2007–2008 financial crisis and the COVID-19 pandemic.
These models provide a virtual laboratory for testing policy responses, offering
insights into the likely effects of various interventions and helping to inform
decisions in real-time. ABM’s ability to model complex systems and incorporate
heterogeneous agents makes it particularly well-suited for crisis management and
long-term economic forecasting.
2.10.4 Generative AI as a Promising Tool
This work also emphasizes the importance of agent-based modeling (ABM) within
social sciences, particularly through a generative approach, which seeks to “grow”
social phenomena from the bottom up. This approach situates autonomous, het-
erogeneous agents in a defined environment and allows their interactions to
produce emergent social behaviors. A key innovation introduced in this work is the
concept of Inverse Generative Social Science (iGSS). Unlike traditional generative
approaches where micro-level agents are created to observe macro-level outcomes,
iGSS works backward by setting a macro-target (such as a specific economic or
social outcome) and evolving agents that lead to that target. This shifts the focus

2 ABL 43
from designing detailed agents to specifying key macro-level outcomes and letting
agents naturally evolve to produce them, driven by basic rules.
Finally, the integration of Large Language Models (LLMs) into Generative
Agent-Based Models (GABMs) is revolutionizing research in complex systems
and behavioral sciences by simulating human decision-making and interactions, as
shown in recent studies by Lu et al. [122] and Ghaffarzadegan et al. [123], which
highlight the application of LLMs in modeling social norm diffusion and other
social dynamics.
We believe this work contributes to the continued development and application
of ABM and agent learning techniques to address complex economic and social
challenges. By simulating interactions at both micro and macro levels, ABM
offers powerful tools for understanding emergent behavior, learning processes, and
adaptive responses to crises. This makes it a promising approach for studying
everything from market dynamics to public policy in a rapidly changing world.
References
1. Y. Shoham, R. Powers, T. Grenager, If multi-agent learning is the answer, what is the
question? Artif. Intell. 171(7), 365–377 (2007)
2. R. Axelrod, L. Tesfatsion, A guide for newcomers to agent-based modeling in the social
sciences, in Handbook of Computational Economics, ed. by L. Tesfatsion, K. Judd, vol. 2
(Elsevier, Amsterdam, 2005), pp. 1647–1659
3. C. Angione, E. Silverman, E. Yaneske, Using machine learning as a surrogate model for
agent-based simulations. PLoS One 17(2), e0263150 (2022)
4. J.H. Holland, J. Miller, Artificial adaptive agents in economic theory. Am. Econ. Rev. 81,
365–370 (1991)
5. Y. Lu, K. Yan, Algorithms in multi-agent systems: a holistic perspective from reinforcement1
learning and game theory (2020). arXiv:2001.06487v3, https://doi.org/10.48550/arXiv.2001.
06487
6. P. Stone, M. Veloso, Multiagent systems: a survey from a machine learning perspective.
Auton. Robot. 8, 345–383 (2000)
7. K. Safarzyýska, J.C.J.M. van den Bergh, Evolutionary models in economics: a survey of
methods and building blocks. J. Evol. Econ. 20(3), 329–373 (2010)
8. R.L. Axtell, The new coevolution of information science and social science: From software
agents to artificial societies and back or how more computing became different computing.
Technical Report.
9. F. Neves, P. Campos, S. Silva, Innovation and employment: an agent-based approach. J. Artif.
Soc. Soc. Simul. 22(1), 8 (2019)
10. G. Fagiolo, A. Roventini, Macroeconomic policy in dsge and agent-based models redux: new
developments and challenges ahead. J. Artif. Soc. Soc. Simul. 20(1), 1 (2017)
11. S. Polyzos, A. Samitas, I. Kampouris, Economic stimulus through bank regulation: govern-
ment responses to the COVID-19 crisis. J. Int. Financ. Markets Inst. Money75, 101444 (2021)
12. R. Calvert Jump, C. Hommes, P. Levine, Learning, heterogeneity, and complexity in the new
keynesian model. J. Econ. Behav. Org. 166, 446–470 (2019)
13. S. Calimani, G.H. laj, D. Z˙ochowski, Simulating fire sales in a system of banks and asset
managers. J. Bank. Finan. 138, 105707 (2022)

44 P.Camposetal.
14. R.L. Axtell, J.D. Farmer, Agent-based modeling in economics and finance: past, present, and
future. INET Oxford Working Papers 2022-10, Institute for New Economic Thinking at the
Oxford Martin School, University of Oxford (2022)
15. F. Squazzoni, J.G. Polhill, B. Edmonds, P. Ahrweiler, P. Antosz, G. Scholz, E. Chappin, M.
Borit, H. Verhagen, F. Giardini, N. Gilbert, Computational models that matter during a global
pandemic outbreak: a call to action. J. Artif. Soc. Soc. Simul. 23(2), 10 (2020)
16. L. Tesfatsion, Chapter 16 agent-based computational economics: a constructive approach to
economic theory, in Handbook of Computational Economics, vol. 2 (Elsevier, Amsterdam,
2006), pp. 831–880
17. L. Tesfatsion, Agent-based computational economics: growing economies from the bottom
up. Artif. Life 8(1), 55–82 (2002). https://doi.org/10.1162/106454602753694765
18. C. Deissenberg, S. van Der Hoog, H. Dawid, EURACE: a massively parallel agent-based
model of the European economy. Working Paper halshs-00339756, HAL (2008)
19. S.-H. Chen, Computationally intelligent agents in economics and finance. Inf. Sci. 177(5),
1153–1168 (2007). Including: The 3rd International Workshop on Computational Intelligence
in Economics and Finance (CIEF’2003)
20. D. Delli Gatti, G. Fagiolo, M. Gallegati, M. Richiardi, A. Russo (eds.), Agent-Based Models
(Cambridge University Press, Cambridge, 2018)
21. J.M. Epstein, R. Axtell, Growing Artificial Societies: Social Science from the Bottom Up
(Brookings Institution Press; The MIT Press, Cambridge, 1996)
22. R. Cressman, Y. Tao, The replicator equation and other game dynamics. Proc. Natl. Acad.
Sci. 111(3), 10810–10817 (2014). Edited by Brian Skyrms, University of California, Irvine,
CA, and approved March 27, 2014 (received for review February 4, 2014)
23. J. Ferber, Multi-Agent Systems: An Introduction to Distributed Artificial Intelligence
(Addison-Wesley Longman, 1999)
24. R. Axelrod, The Complexity of Cooperation (Princeton University Press, Princeton, 1977)
25. J.M. Epstein, Generative Social Science: Studies in Agent-Based Computational Modeling,
stu-student edition (Princeton University Press, Princeton, 2006)
26. F.J. León-Medina, Analytical sociology and agent-based modeling: is generative sufficiency
sufficient? Soc. Theory 35(3), 157–178 (2017)
27. J.M. Epstein, Inverse generative social science: backward to the future. J. Artif. Soc. Soc.
Simul. 26(2), 9 (2023)
28. R.A. Fisher, The Genetical Theory of Natural Selection (Clarendon Press, Oxford, 1930)
29. N.A. Gómez-Cruz, I. Loaiza Saa, F.F. Ortega Hurtado, Agent-based simulation in manage-
ment and organizational studies: a survey. Eur. J. Manage. Bus. Econ. 26(3), 313–328 (2017)
30. F. Wall, Agent-based modeling in managerial science: an illustrative survey and study. Rev.
Manage. Sci. 10(1), 135–193 (2016)
31. F. Wall, Modeling managerial search behavior based on Simon’s concept of satisficing.
Comput. Math. Org. Theory 29, 265–299 (2023)
32. R.K. Belew, M. Mitchell (eds.), Adaptive Individuals in Evolving Populations-Models and
Algorithms (Routledge, Milton Park, 1996)
33. S.-H. Chen, C.-C. Tai, Republication: on the selection of adaptive algorithms in ABM: a
computational-equivalence approach. Comput. Econ. 28, 313–331 (2006)
34. D.F. Batten, Discovering Artificial Economics: How Agents Learn and Economies Evolve
(Routledge, Milton Park, 2000)
35. M. Gardner, Mathematical games: on cellular automata, self-reproduction, the garden of Eden
and the game ’life’. Sci. Am. 223, 120–123 (1970)
36. M. Mitchell, Complexity: A Guided Tour, 1st edn. (Oxford University Press, Oxford, 2009)
37. T.C. Schelling, Dynamic models of segregation. J. Math. Soc. 1(2), 143–186 (1971)
38. E. Hatna, I. Benenson, The schelling model of ethnic residential dynamics: beyond the
integrated-segregated dichotomy of patterns. J. Artif. Soc. Soc. Simul. 15(1), 1–6 (2012)
39. M.C. Almy, C. Genishi, Ways of Studying Children: An Observation Manual for Early
Childhood Teachers, rev. edn. (Teachers College Press, Williston, 1979)
40. H. Simon, A behavioral model of rational choice. Quart. J. Econ. 1, 99–118 (1955)

2 ABL 45
41. J. Holland, Adaptation in Natural and Artificial Systems: An Introductory Analysis with
Applications to Biology, Control and Artificial Intelligence (The MIT Press, Cambridge,
2001)
42. M. Mitchell, Artificial Intelligence: A Guide for Thinking Humans, 1st edn. (Farrar, Strausand,
Giroux, New York, 2019)
43. P. Todd, The causes and effects of evolutionary simulation in the behavioural sciences, in
Adaptive Individuals in Evolving Populations: Models and Algorithms, ed. by R. Belew, M.
Mitchell (Santa Fe Institute in the Sciences of Complexity/Addison Wesley, Santa Fe/Boston,
1996), pp. 211–231
44. R.K. Belew, M. Mitchell, Adaptive Individuals in Evolving Populations (Addison-Wesley,
Reading, 1996)
45. H.P. Young, Individual Strategy and Social Structure: An Evolutionary Theory of Institutions
(Princeton University Press, Princeton, 1998)
46. J. Holland, Adaptation in Natural and Artificial Systems: An Introductory Analysis with
Applications to Biology, Control and Artificial Intelligence, 6th edn. (The MIT Press,
Cambridge, 2001)
47. K.M. Carley, V. Hill, Structural change and learning within organizations, in Dynamics of
Organizations: Computational Models and Organizational Theories, ed. by A. Lomi, E.R.
Larsen (AAAI Press/The MIT Press, Menlo Park, 2001), pp. 63–92
48. H.A. Simon, Search and reasoning in problem solving. Artif. Intell. 1, 7–29 (1983)
49. D. Waszek, Informational equivalence but computational differences? Herbert Simon on
representations in scientific practice. Minds Mach. 34, 93–116 (2024)
50. C. Schmidt, J. Grossklags, Interaction of human and artificial agents on double auction
markets-simulations and laboratory experiments. Papers on strategic interaction, Max Planck
Institute of Economics, Strategic Interaction Group (2004)
51. C. Darwin, On the Origin of Species by Means of Natural Selection, or the Preservation of
Favoured Races in the Struggle for Life, 1st edn. (John Murray, London, 1859)
52. J.B. Lamarck, Zoological Philosophy. National Museum of Natural History (1809)
53. M.J. Baldwin, A new factor in evolution. Am. Natural. 30(354), 441–451 (1896)
54. G. Hinton, S. Nowlan, How learning can guide evolution. Complex Syst. 1, 495–502 (1987)
55. P.D. Taylor, L. Jonker, Evolutionarily stable strategies and game dynamics. Math. Biosci. 40,
145–156 (1978)
56. J. Smith, G. Price, The logic of animal conflict. Nature 246, 15–18 (1973)
57. R. Cressman, J. Song, B.-Y. Zhang, Y. Tao, Cooperation and evolutionary dynamics in the
public goods game with institutional incentives. J. Theor. Biol. 299, 144–151 (2012). Epub
2011 Aug 11
58. D. Friedman, Towards evolutionary game models of financial markets. Quant. Finance 1(1),
177–185 (2001)
59. I. Saha, V. Kavitha, Financial replicator dynamics: emergence of systemic-risk-averting
strategies, in International Conference on Network Games, Control and Optimization (2020)
60. M. Wooldridge, N.R. Jennings, Intelligent agents: theory and practice. Knowl. Eng. Rev. 10,
115–152 (1995)
61. A.S. Rao, M. Wooldridge, Foundations of Rational Agency (Springer, Dordrecht, 1999), pp.
1–10
62. N.J. Nilsson, Shakey the robot (1984)
63. B. Kuipers, E.A. Feigenbaum, P.E. Hart, N.J. Nilsson, Shakey: from conception to history. AI
Mag. 38, 88–103 (2017)
64. R.J. Firby, An investigation into reactive planning in complex domains, in Proceedings of
the Sixth National Conference on Artificial Intelligence-volume 1, AAAI’87 (AAAI Press,
Washington, 1987), pp. 202–206
65. R.J. Firby, R.E. Kahn, P.N. Prokopowicz, M.J. Swain, An architecture for vision and action,
in Proceedings of the 14th International Joint Conference on Artificial Intelligence-Volume
1, IJCAI’95, San Francisco (Morgan Kaufmann, Burlington, 1995), pp. 72–79
66. M.P. Georgeff, Reasoning about procedural knowledge (1985)

46 P.Camposetal.
67. M.P. Georgeff, F. Ingrand, Decision-making in an embedded reasoning system, in Interna-
tional Joint Conference on Artificial Intelligence (IJCAI) (1989)
68. A.S. Rao, M.P. Georgeff, An abstract architecture for rational agents, in Proceedings
of knowledge representation and reasoning (KR&R-92) (Scientific Research Publishing,
Cambridge, 1992), pp. 439–449
69. A.S. Rao, M.P. Georgeff, BDI agents: from theory to practice, in Proceedings of First
International Conference on Multiagent Systems (ICMAS) (1995)
70. M. Bratman, Intention, Plans, and Practical Reason (Harvard University Press, Cambridge
1987)
71. R.S. Sutton, Temporal credit assignment in reinforcement learning. Ph.D. Thesis (1984).
AAI8410337
72. R.S. Sutton, A.G. Barto, Introduction to reinforcement learning (1998)
73. S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, 3rd edn. (Prentice Hall
Press, Upper Saddle River, 2009)
74. C. Castelfranchi, E. Werner (Eds.), Artificial Social Systems, 4th European Workshop on
Modelling Autonomous Agents in a Multi-Agent World, MAAMAW’92, S. Martino al Cimino,
Italy, July 29–31, 1992, Selected Papers. Lecture Notes in Computer Science, vol. 830
(Springer, Berlin, 1994)
75. F.J.Garijo,M.Boman(Eds.),Multi Agent System Engineering, 9th European Workshop on
Modelling Autonomous Agents in a Multi-Agent World, MAAMAW’99, Valencia, June 30–July
2, 1999, Proceedings. Lecture Notes in Computer Science, vol. 1647 (Springer, Berlin, 1999)
76. Proceedings of the First International Joint Conference on Autonomous Agents and Multia-
gent Systems: Part 1 (AAMAS’02) (Association for Computing Machinery, New York, 2002)
77. Proceedings of the 21st International Conference on Autonomous Agents and Multiagent
Systems (AAMAS’22) (International Foundation for Autonomous Agents and Multiagent
Systems, Richland, 2022)
78. C.G. Langton, Artificial life: an overview (1995)
79. C.G. Langton, C.E. Taylor, J.D. Farmer, S. Rasmussen, Artificial life II (1991)
80. U. Wilensky, W. Rand, An introduction to agent-based modeling: modeling natural, social,
and engineered complex systems with netlogo (2015)
81. Y. Shoham, Agent-oriented programming. Artif. Intell. 60, 51–92 (1993)
82. A.S. Rao, Agentspeak(l): BDI agents speak out in a logical computable language, in
Proceedings of Modelling Autonomous Agents in a Multi-Agent World (MAAMAW) (1996)
83. R.H. Bordini, J.F. Hübner, M. Wooldridge, The jason agent programming language (2007)
84. A. Lucas, M. Ljungberg, R. Evertsz, G. Tidhar, R.S. Goldie, P. Maisano, New techniques for
air traffic management for single and multiple airports (1994)
85. F. Ingrand, M.P. Georgeff, A.S. Rao, An architecture for real-time reasoning and system
control. IEEE Expert 7, 34–44 (1992)
86. A. Rao, A. Lucas, D. Morley, M. Selvestrel, G. Murray, Agent-oriented architecture for air
combat simulation (1993)
87. D. Kinny, M.P. Georgeff, A.S. Rao, A methodology and modelling technique for systems
of BDI agents, in Proceedings of Modelling Autonomous Agents in a Multi-Agent World
(MAAMAW) (1996)
88. N. Gilbert, When does social simulation need cognitive models? in Cognition and Multi-
Agent Interaction: From Cognitive Modelling to Social Simulation, ed. by R. Sun (Cambridge
University Press, Cambridge, 2005)
89. J. Corchado, J. Pavón, E. Corchado, L. Castillo, Development of CBR-BDI agents: a tourist
guide application. Lect Notes Comput. Sci. 3155, 547–559 (2004)
90. K. Bogner, M. Müller, A. Pyka, B. Ebersberger, T. Berger, J. Dahlke, Is the juice worth the
squeeze? Machine learning in and for agent-based modelling a preprint. Technical Report
(2020)
91. M. Mitchell, Artificial Intelligence: A Guide for Thinking Humans (1st edn.) (Farrar, Straus
and Giroux, New York, 2019)
92. R. Conte, M. Paolucci, Intelligent social learning. J. Artif. Soc. Soc. Simul. 4(1), U61–U82
(2001)

2 ABL 47
93. H. Aziz, Multiagent systems: algorithmic, game-theoretic, and logical foundations by y.
shoham and k. leyton-brown cambridge university press, 2008. SIGACT News 41(1), 34–37
(2010)
94. T. Brenner, Chapter 18 agent learning representation: advice on modelling economic learning,
in Handbook of Computational Economics, vol. 2 (Elsevier, Amsterdam, 2006), pp. 895–947
95. J. Duffy, Agent-based Models and Human Subject Experiments. Computational Economics
(University Library of Munich, Munich, 2004)
96. J.M. Vidal, Learning in multiagent systems: an introduction from a game-theoretic perspec-
tive, in Adaptive Agents and Multi-Agent Systems, ed. by E. Alonso, D. Kudenko, D. Kazakov.
Lecture Notes in Computer Science, vol. 2636 (Springer, Berlin, 2003)
97. T. Mitchell, Machine Learning (McGraw Hill, Singapore, 1997)
98. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, 2nd edn. (MIT Press,
Cambridge, 2018)
99. G. Ciaburro, Hands-on reinforcement learning with R: get up to speed with building self-
learning systems using R 3.x
100. F. Leno da Silva, G. Warnell, Agents teaching agents: a survey on inter-agent transfer learning.
Auton. Agents Multi-Agent Syst. 34(1), 9 (2019)
101. F.L. Da Silva, A.H.R. Costa, A survey on transfer learning for multiagent reinforcement
learning systems. J. Artif. Intell. Res. 64, 645–703 (2019)
102. P.B. Brazdil, J.N. van Rijn, C. Soares, J. Vanschoren, Metalearning: Applications to Auto-
mated Machine Learning and Data Mining, 2nd edn. (Springer, Berlin, 2022)
103. P. Brazdil, M. Gams, S.W. Sian, L. Torgo, W. Van de Velde, Learning in distributed systems
and multi-agent environments, in Machine Learning-EWSL-91, ed. by Y. Kodratoff. Lecture
Notes in Artificial Intelligence, vol. 482 (Springer, Berlin, 1991), pp. 412–423
104. C. Hu, C. Wang, W. Luo, C. Yang, L. Xiang, Z. He, A multitask-based transfer framework
for cooperative multi-agent reinforcement learning. Appl. Sci. 15(4), 2216 (2025). https://doi.
org/10.3390/app15042216
105. P. Stone, Layered Learning in Multiagent Systems: A Winning Approach to Robotic Soccer
(MIT Press, Cambridge, 2000)
106. D. Michie, R.A. Chambers, Boxes: an experiment in adaptive control, in Machine Intelli-
gence, ed. by E. Dale, D. Michie, vol. 2 (Oliver and Boyd, Edinburgh, 1968)
107. P. Brazdil, Model of error detection and correction. Ph.D. Thesis, University of Edinburgh
(1981)
108. P. Brazdil, Use of derivation trees in discrimination, in ECAI 1984-proceedings of 6th Euro-
pean Conference on Artificial Intelligence, ed. by T. O’Shea (North-Holland, Amsterdam,
1984), pp. 239–244
109. M. Bain, C. Sammut, A framework for behavioural cloning. Technical report, Department of
AI, University of New South Wales, Sydney (2001)
110. R. Camacho, P. Brazdil, Improving the robustness and encoding complexity of behavioural
clones, in Machine Learning: ECML 2001 (2001), pp. 37–48
111. E.H. Durfee, Distributed Problem Solving and Planning (Springer, Berlin, 2001), pp. 118–
149
112. Y. Shoham, K. Leyton-Brown, Multiagent Systems: Algorithmic, Game-Theoretic, and
Logical Foundations (Cambridge University Press, New York, 2009)
113. S. van der Hoog, Deep learning in (and of) agent-based models: a prospectus (2017)
114. P.M. Senge, The Fifth Discipline: The Art and Practice of the Learning Organization
(Doubleday, New York, 1990)
115. C. Mutongi, B. Rigava, The application of the fifth discipline strategies in the learning city
concept, in 2024 IEEE 3rd International Conference on AI in Cybersecurity (ICAIC), Houston
(2024), pp. 1–7. https://doi.org/10.1109/ICAIC60265.2024.10433847
116. C. Gao, X. Lan, N. Li, Y. Yuan, J. Ding, Z. Zhou, F. Xu, Y. Li, Large language models
empowered agent-based modeling and simulation: a survey and perspectives (2023). arXiv,
abs/2312.11970

48 P.Camposetal.
117. Ö. Gürcan, LLM-augmented agent-based modelling for social simulations: challenges and
opportunities, in HHAI 2024: Hybrid Human AI Systems for the Social Good (2024), pp.
134–144
118. H. Zhao, Z. Liu, Z. Wu, Y. Li, T. Yang, P. Shu, S. Xu, H. Dai, L. Zhao, G. Mai, N. Liu, T.
Liu, Revolutionizing finance with LLMs: an overview of applications and insights (2024).
arXiv:2401.11641
119. Y. Li, S. Wang, H. Ding, H. Chen, Large language models in finance: a survey, in Proceedings
of the Fourth ACM International Conference on AI in Finance (ICAIF’23) (Association for
Computing Machinery, New York, 2023), pp. 374–382
120. E. Ash, S. Hansen, Large language models for economic research: four key questions. CEPR
VoxEU (2023). https://cepr.org/voxeu/columns/large-language-models-economic-research-
four-key-questions
121. Gao, X. Lan, N. Li, et al., Large language models empowered agent-based modeling and
simulation: a survey and perspectives. Humanit. Soc. Sci. Commun. 11, 1259 (2024). https://
doi.org/10.1057/s41599-024-03611-3
122. Y. Lu, A. Aleta, C. Du, L. Shi, Y. Moreno, Generative agent-based models for complex
systems research: a review (2024). arXiv:2408.09175. https://arxiv.org/abs/2408.09175
123. N. Ghaffarzadegan, A. Majumdar, R. Williams, N. Hosseinichimeh, Generative agent-based
modeling: an introduction and tutorial. Syst. Dyn. Rev. 40(1), e1761 (2024)
124. S. Poledna, S. Thurner, Elimination of systemic risk in financial networks by means of a
systemic risk transaction tax. Quant. Finance 16, 1599 (2016)

Part  II
| Agent-Based  | Models  | in  the  Context  |
| ------------ | ------- | ----------------- |
of  COVID19

Chapter 3
Epidemiology Modelling
Arit Kumar Bishwas and Anand Rao
3.1 Introduction
The whole world is going through a tough time in dealing with the ongoing
COVID-19 (Coronavirus disease 2019) which is a transmissible disease instigated
by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). This was first
acknowledged inWuhan,China,inDecember2019[1].Thediseasehassincespread
across the world and led to an enduring pandemic. Investigating such a complex
disease to track down the connected dots of the initialization of spreads within the
chain and controlling it is extremely complicated. The total cases by Worldometer
[2] ares hown in Fi g.3.1 demonstrates the super spread nature of COVID-19.
Governments around the world are sharing the COVID-19 data for its spreading
rates, death rates, and recovery rates. Most of the data is publicly available
to conduct research and understand the nature of the virus and determine the
probable actions required to control the spreading among the population and help in
developing policies around it to reduce the effect and restrict the outbreaks.
It is extremely essential to be able to comprehend the COVID-19 spread with
the help of a computational model. An appropriate designed model can help to
determine the actions and policies which will have the best impact in controlling
the outbreaks and prevent further spread by demolishing the spreading chain. In
2010, Olsen et al. [3] used an agent-based model to determine the cost-effectiveness
ratio for HPV vaccinations. They have demonstrated that in the longer term the
A. K. Bishwas
PricewaterhouseCoopers, Fremont, CA, USA
e-mail: aritkumar.official@gmail.com
A. Rao (@)
Heinz College of Information Systems and Public Policy, Carnegie Mellon University, Pittsburgh,
PA, USA
e-mail: anandr2@andrew.cmu.edu
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 51
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_3

52 A.K.BishwasandA.Rao
Fig. 3.1 Total COVID-19 cases across the world (till 9th Feb 2022)
vaccinations save on overall treatment costs and improve the survival rate, although
the preliminary costing for the vaccination program may have heavy investments
the demonstrated longer benefits justify the initial investments.
3.1.1 World at Halt!
This is the first of its kind of situation in the world where the whole world got halted
for almost two years. The impact Covid-19 deployed is devastating on many fronts.
3.1.1.1 Impact on Human Life
Based on one of the investigated reports in 2020 [4], around the world, millions of
human lives have severely been impacted and tens of millions of them are at risk of
falling into poverty, the estimated 690 million undernourished population in 2020
may probably jump by 132 million by the end year. COVID-19 impacted the way
humans used to live, it affected the human livelihoods, health and food system.
3.1.1.2 The Impact on the Economy
COVID-19 has obstructed the economic growth of the entire world. Although, we
can not exactly estimate the economic damages from the COVID-19 pandemic
that have been inaugurated the world economy, based on the economic experts the
impact is severe negative [5]. Based on the report, the majority of the economies
will face a loss of at least 2.9% of the gross domestic product over 2020, and we are

3 EpidemiologyModelling 53
witnessingtheprobable impacts atpresent timein2022. Thisestimationwasalready
paraphrased to a 3.4% loss on the GDP side [5]. From a supportive factual aspect, in
2020, around 84.54 trillion U.S. dollars were estimated as the global GDP and 2.96
trillion U.S. dollars of lost economic output with a predicted 4.5% drop in economic
growth outcomes. The report from The World Bank [6], although discussed the
situation with some improvement hints.
3.1.1.3 The Impact on Education
The impact of COVID-19 on the education system is very distressing. The schools
and colleges around the world were shut down and the children missed the schooling
and college culture. This is not only the effect on cultural experiences education
and the lack of human interactions for them but also deployed a psychological
consequence on them. This causes many dropouts, more interaction with digital
artefacts, and high digital screening time with mobile, laptops etc. for children
which can influence their health. But on the other hand, it changed the way we
used to experience the education process, it opened a lot of new opportunities in the
digital market and new ways of teaching methods [7].
Throughout the recorded history, we witnessed the periodic epidemics and
pandemics in the world which has caused uncontrolled deaths, disrupted impacts on
societies,andeconomical disasters.Theepidemiology modellinghelpsinmitigating
the effects by predicting the progression of its outbreak, which we have discussed
in detail in the next section.
3.2 Epidemiology Modelling
Epidemiology is the study of disease occurrence which can help in comparing
the effect of control and prevention. An epidemic is the rapid spread of disease
to a large number of hosts in a given population within a short period of time.
So, it is maybe not only how many people are affected, but also how fast the
disease spreads that defines “epidemic”. Apart from transmission mode, agents
causing infectious, duration of spread, susceptibilities, confrontation, the epidemic
also involves other factors such as geography, economy, and demography etc. By
modellingtheepidemiology,wemeantoinvestigateallthefactorsthatdeterminethe
presence, absence and related disorders. If we go back in history, a great physician,
Hippocrates is considered the first epidemiologist. He wrote the following famous
books: “Epidemic—I”, “Epidemic—III”, and “On Airs waters and places” [8].
Later between 1620 and 1674 [9], John Graunt started a deep investigation of
the infectious disease and wrote the book “Natural and Political Observations
Made upon the Bills of Mortality” [10]. Between 1700 and 1732, Daniel Bernoulli
demonstrated the first mathematical model against smallpox, and we can say that

54 A.K.BishwasandA.Rao
he is the first person who put the stepping stone for analysing epidemiology using
mathematical models [11].
Modelling an epidemic requires a detailed understanding of the nature and dif-
ferent associated and affected factors of the disease spreading. The epidemiological
models help in understanding the nature of the disease spreading and developing
the related policies. No model is perfect, and mostly associated with limitations but
sometimes a model can demonstrate superior capabilities by finding the appropriate
combination of the parameters which can lead to an answer to an interesting
question.
We are now going to comprehend the following terms often used to understand
the specific technical applications in the study of epidemiological modelling:
3.2.1 Vertical Transmission
In case, the disease is transmitted down from the mother to the child, causing a
child born with an infected disease, is known as vertical transmission. For example,
in AIDS and Hepatitis B, recently many vertical transmission cases have been also
found for COVID-19 cases. In a recent investigation on infected pregnant women
for the COVID-19 vertical transmission, the investigation team reported that there
are only 3.2% positive cases [12, 13].
Based on [12] and some other recent investigations [14–17], we conclude that
there is no adequate evidence to reject the possibility of vertical transmission for
COVID-19basedontheanalysisoftheavailabledataatthetimeoftheinvestigation.
3.2.2 Vector Transmission
When the disease is transmitted among humans indirectly through any other
medium is known as vector transmission. The current literatures suggest that
SARS-CoV-2 virus, which causes COVID-19 disease, is transmitted among the
human population via aerosols to a lesser extent, and mainly through respiratory
droplets [18, 19]. Based on the recent investigations, there are no proper shreds of
evidence of COVID-19 vector transmission, although the transmission seems to be
exaggerated by humidity, temperature, air currents, precipitation, pH, and radiation
in the ambient environment [19].
3.2.3 Deterministic Epidemic Models
The deterministic model is very useful when the population size is sufficiently large.
To be more precise, these models are based on different compartments, where each

3 EpidemiologyModelling 55
of the compartments represents a set of individuals relative to a specific stage of the
epidemic. We mathematical express the rate of transitions among the compartments
with derivatives, and hence a system of differential equations formulates a model. A
very important property of the deterministic model is to consider that the population
size in a compartment is differentiable with respect to time [20].
3.2.4 Stochastic Epidemic Models
There are some mathematical models where we allow random variations in inputs
over time for approximating probability distributions of likely outcomes, which are
known as stochastic epidemic models. These kinds of models depend on the casual
variations in sickness dynamics, disease, and exposure risk [21].
3.2.5 Contact Rate and Adequate Contact Rate
At a given unit time an infectious individual contacts the total number of individuals
isknownasthecontact rate.Adequate contact ratehelpsindeterminingtheinfection
strength of the infectives. It is defined as the product of the probability of infection
by each contact and contact rate. Mathematically, we can express an adequate
contact rate as p C(N), where p is the probability of infection by each contact,
c . c.
and C(N) is the contact rate with population size N.
3.2.6 Infection Rate
Infection rate (aka incident rate) is the probability of infection in the population N
under consideration. It helps in measuring the occurrence frequency of the infection
in a population N under observation within a specific period. Mathematically, we
can describe the infection rate as:
I
I =K N (3.1)
. R
N
risk
where, I is the infection rate, I is the number of infections,N is the population
R. N. risk.
at risk, K is a constant factor which can have values as 100,1000,10000 etc. The
value of K represents a standard population and period for interpretation of the
rate. For example, with K = 100, the formulation gives an infection rate that can
be articulated as a percentage [22].

56 A.K.BishwasandA.Rao
3.2.7 Incident (Bilinear Incident or Mass Action, Standard
Incident)
We express the incident as the number of new infectious cases during some specific
time period. More technically, it is a measurement of the occurrence’s probability
of infection in a population within a specific period.
3.2.8 Basic Reproduction Number
The basic reproduction number, R , is the expected number of infectious cases
0.
caused by an individual in a susceptible to infection population. The values of R
0.
are generally estimated from mathematical models and are model dependent and
influenced by different parameter values. The estimated value also depends on many
other factors such as the behavioural pattern of the population under consideration
and environmental aspects [23].
3.3 Agent-Based Models
Modelling is a mathematical way to describe how individuals are interacting
with each other within a population. An agent-based model is a computational
model which is used to understand the behaviour of a system and associated
governess of the consequences by simulating an agent’s action and interactions in
the system. Agent-based models have intrinsic nature to capture highly complex
relations between aspects that emergent outcomes based on agent’s decisions within
the model that other types of models cannot. We use Monte Carlo methods to
understand the stochasticity of these kinds of models.
3.3.1 Compartmental Based Modelling
Within a population, we categorize different sets of people and use a nomenclature
for the representation purpose based on the characteristics of the sets. Susceptible,
Exposed, Infected, Recovery, and Dead are some of the standard naming conven-
tions used in literature. Each of these sets is also known as the compartment. Within
each compartment, we assume that each individual possesses similar characteristics,
and these compartments are mutually exclusive.

3 EpidemiologyModelling 57
3.3.1.1 SI Model
The first model we are discussing is the basic SI mode [24]. In this kind of model,
there are only two types of compartments involved—Susceptible (S) and Infected
(I). The following Fig.3.2 represents a basic SI model, where S, I and β are the
.
parameters. These parameters are used to represent the rate of flow and interactions
rates between the compartments. βis the rate of interaction between the Susceptible
.
and Infected individuals from the compartments.
Similarly, Fig.3.3 shows a model when the individuals got treated and becomes
susceptible from infected, where δis the rate of interaction between the infected and
.
susceptible individuals.
3.3.1.2 SIR Model Without Vital Dynamics
In 1927, Kermack et al. [25] introduced a simple but very effective model known
as the SIR model shown in Fig.3.4, which is based on susceptible, infected, and
recovered compartments. The three compartments are mutually exclusive. The
population of the Susceptible (S) compartment comprises those individuals who can
indenture the infection and make the compartment infective. The population of the
Infective (I) compartment contains the pollution of individuals who can transmit the
disease to the susceptible compartment. The Removed (R) compartment contains the
population where the individual can be at one of the states [25]:
• got infected
• either has died
• recovered fully from the disease
• have been quarantined
Fig. 3.2 Basic SI model
Fig. 3.3 SI model with rate
of interaction δ.
Fig. 3.4 SIR model

58 A.K.BishwasandA.Rao
Mathematically, we can explain the model with the following system of differen-
tial equations:
dS βSI
=− (3.2)
.
dt N
dI βSI
= −γI (3.3)
.
dt N
dR
=γI (3.4)
.
dt
where t is the time, S is the susceptible population, I is the infected population,
and R is the recovered population. γ and β are the rates of recovery and infection
. .
respectively, and N is the sum of S, I, and R. The following are some popular
variations of the SIR models:
3.3.1.2.1 SIRS Model
In this type of SIR model [26], the individuals from the recovery compartment go
to the susceptible compartment too as shown in Fig.3.5.
3.3.1.2.2 SIRI Model
The model where the individuals from the recovery compartment also go to the
infected compartment as shown in Fig.3.6, is known as the SIRI model [27].
Fig. 3.5 SIRS model
Fig. 3.6 SIRI model

3 EpidemiologyModelling 59
3.3.1.2.3 SIRD Model
SIRD is another kind of variation of the SIR model, known as the Susceptible-
Infectious-Recovered-Deceased model, where we also consider the diseased case
as a compartment apart from the susceptible, infectious, and recovered. The SIRD
model is shown in Fig.3.7 [28].
The following system of differential equations represents the SIRD model, where
β, γ and μare the infection, recovery and death rates respectively:
. . .
dS βSI
=− (3.5)
.
dt N
dI βSI
= −γI −μI (3.6)
.
dt N
dR
=γI (3.7)
.
dt
dD
=μI (3.8)
.
dt
3.3.1.2.4 SIRV Model
When we took the vaccination case as a compartment into account in the SIR
model, we define the SIRV model, known as the Susceptible-Infectious-Recovered-
Vaccinated model as shown in Fig.3.8 [29].
Fig. 3.7 SIRD model
Fig. 3.8 SIRV model

60 A.K.BishwasandA.Rao
The following system of differential equations describes the SIRV model, where
ν . is the rate of vaccination:
dS βSI
| =−     | −νS | (3.9)  |
| ------ | --- | ------ |
| . dt N |     |        |
dI βSI
| = −γI |     |         |
| ----- | --- | ------- |
| .     |     | (3.10)  |
dt N
dR
=γI
| .   |     | (3.11)  |
| --- | --- | ------- |
dt
dV
| =νS |     | (3.12)  |
| --- | --- | ------- |
.
dt
3.3.1.2.5  SEIS Model
There are cases where the immunity is not achieved at the end and so the individuals
are taken back to the susceptible compartment from the infectious compartment as
shown in Fig.3.9 [30].
We  define  the  SEIS  model  in  the  following  way  by  using  the  system  of
differential equations:
| dS βSI |     |         |
| ------ | --- | ------- |
| =^−μS− | +γI | (3.13)  |
.
| dt  | N   |     |
| --- | --- | --- |
dE βSI
| = −(μ+α)E |     | (3.14)  |
| --------- | --- | ------- |
. dt N
dI
| =αE−(γ | +μ)I, | (3.15)  |
| ------ | ----- | ------- |
.
dt
where ^and μare the birth and death rates respectively.
. .
Fig. 3.9  SEIS model

3 EpidemiologyModelling 61
3.3.1.2.6 SEIR Model Without Vital Dynamics
In case when an individual is exposed to the infected environment, we considered an
exposed compartment to put these kinds of individuals. To handle such situations,
we consider the Susceptible-Exposed-Infectious-Recovered (SEIR) model, as shown
in Fig.3.10 [31].
We represent the model by using the following system of differential equations,
where, α is the latency period during which an individual is infected but not yet
.
infectious:
dS βSI
=μN −μS− (3.16)
.
dt N
dE βSI
= −(μ+α)E (3.17)
.
dt N
dI
=αE−(γ +μ)I (3.18)
.
dt
dR
=γI −μR (3.19)
.
dt
SEIRS (Susceptible-Exposed-Infectious-Recovered-Susceptible)is a variation of
the SEIR model, where recovered individuals are kept back in the susceptible
compartment as shown in Fig.3.11 [32].
Fig. 3.10 SEIR model without vital dynamics
Fig. 3.11 SEIRS model

62 A.K.BishwasandA.Rao
3.3.1.3 SIR Model with Vital Dynamics
In this kind of model, the population is characterized by some relevant and vital
dynamics such as death and birth rates during a communicable disease is spreading.
The following Fig.3.12 shows the SIR model with vital dynamics [33, 34].
We define the model as follows:
dS βSI
=^−μS−S− (3.20)
.
dt N
dI βSI
= −(μ+γ)I (3.21)
.
dt N
dR
=γI −μR, (3.22)
.
dt
where ^and μare the birth and death rates respectively.
. .
3.3.2 Agent-Based Modelling
In Agent-based modelling, we define a model to simulate a system composed
of a collection of agents. An agent-based model is composed of the following
three elements: autonomous agents—which is an interacting component in a large
complex system, interactions—this is a phenomenon of the agent’s communication
mechanism, and the environment—where the agents interact within. Here, an agent,
which is an autonomous decision-making entity, can be an individual, any organiza-
tion, or body. An agent takes an action based on some set of defined rules. An agent
can also have the capability to evolve and consent unforeseen behaviours to emerge.
Some advance agent-based systems also integrate machine learning techniques and
evolutionary algorithms from the aspects of realistic learning adaptation.
In the previous sections, we discussed the compartmental based approaches
which are based on traditional differential equations. Each of the approaches has
some weaknesses and strengths. Compartmental based models assume homogeneity
Fig. 3.12 SIR model with vital dynamics

3 EpidemiologyModelling 63
Fig. 3.13 Rules for an agent of a day activity
and attempt perfection in mixing within compartments, on the other hand, agent-
based models can target heterogeneous attributes across individuals and in the
associated network of interactions among them [35], where heterogeneity empha-
sises the classification of individuals with different roles associated with specified
different actions and responses in the system under consideration and allow for the
agent’s dynamics across space and time [36–38]. ABM modelling is a costly affair
from the computational power and cognitive point of view. The following Fig.3.13
demonstrates the agent’s rules for a day activity.
Compartmental models follow a “top-down” structure as compared to agent-
based models. Although the compartmental models are very effective in analysing
epidemiological situations, it is challenging to fit various intervention strategies
reasonably into one compartmental based model to quantify the effectiveness
[38–41]. Adding more parameters seems to be a solution but it may increase
the complexities of the compartmental model without gaining much validity and
accuracy while making decisions [42]. Agent-based models, on the flip side, apply
a “bottom-up” structure. In an agent-based model, each individual interacts with the
other based on a specified or selected set of rules [35, 36, 43, 44]. Although, these
specific rules can be changed by the application of different intervention strategies.
The user can analyse the outcomes by manipulating the different parameters in the
ABM simulation which confer the infectious probability and spread on different
intervention strategical aspects. As compared to the compartmental or equation-
based model, in the agent-based model, the transmission of the virus affects the
strategy on an individual level [35, 36, 43, 45].

64 A.K.BishwasandA.Rao
3.3.3 Machine Learning-Based Modelling
Machine learning (ML) is a branch of artificial intelligence that helps in performing
some of the most interesting tasks like classification, clustering, object detections,
dimension reduction, natural language processing etc. Machine learning promises
to provide a model which helps in finding the unknown hidden patterns, functions,
dependencies, or relations among the data from the given data set under consider-
ation. The trained machine learning models support predicting the outcome based
on the given inputs. Machine learning, in general, can be categorised into three
parts—supervised learning, unsupervised learning, and reinforcement learning. The
following Fig.3.14 shows the types of machine learning and related tasks [46–49].
Deep learning (aka deep structured learning) is a sub-branch of machine learning
that imitates the way humans pursue a certain type of information, which is based
on the artificial neural networks with multiple layers for processing the information
to extract progressively higher-dimensional features from the given input data. With
deep learning, learning can be supervised, unsupervised, and reinforcement learning
following the same categorization of ML.
Some of the popular deep learning algorithms such as convolutional neural
networks (CNN) [46], long short-term memory (LSTM) [47], bidirectional encoder
representations from the transformers (BERT) [48], deep reinforcement learning
[49] have been applied many different fields including computer vision [50], natural
languageprocessing[51],speechrecognition[52],drugdesign[53],thevirusspread
analysis in pandemic [54], etc.
Fig. 3.14 Machine learning types, tasks, and related algorithms

3 EpidemiologyModelling 65
3.4 COVID-19 Epidemiological Modelling
Due to the flexible nature of the agent-based model, it has a very wider application
area to different situational scenarios areas such as hospitals [55], facilities [38], and
university campuses [56]. An agent-based model (ABM) can capture the spatial,
heterogeneous, interactive, and local features of the epidemic spreading [57] which
makestheABMaverypopular andinterestingmethodforvisualizingandinforming
a complex dynamic system [58].
3.4.1 Covid-19 Epidemiological Analysis with ABM
During COVID-19, ABM played a vital role in analysing the COVID-19 epidemi-
ological circumstance to understand the spread and control it. Many attempts have
been made to understand the nature of its spreading which helped in controlling the
disastrous impact of the situation. In this section, we explore some of the important
and interesting research in this direction.
3.4.1.1 Recent Investigation 1
In [59], the authors have discussed their investigation regarding the COVID-19
situation in France. When the COVID-19 hit the whole world and many European
countries implemented nationwide lockdown and protection measurement, so, did
France too. They analysed the potential impact of the post-lockdown measures
and the protection measurements like mask-wearing, and physical distances. They
examined the outcomes of the investigation in terms of the intensive care unit-
bed occupancies and cumulative mortality and disease incidences. The researchers
used a stochastic agent-based model to investigate the COVID-19 epidemic in
France. For this purpose, they generated a realistic synthetic population with
the help of demographic characteristics and household structure representative of
the population under consideration. They also take into account the co-location
probability and duration by establishing a day-wise geo-localized activity sequence
based communal interaction network among the individuals, and a disease model,
which outputs the infection probability of the edge over the day from the edge
weights in the communal interaction network. Within a heterogeneous population,
the proposed framework can capture an emergent phenomenon with complex
interactions between individuals. The framework can help the policymakers and
epidemiologists define the measurement at the societal and individual level, by
unfolding the disease microorganism’s characteristics and simulating the evolution
of the disease microorganism with a realistic synthetic population. The model is
comprised of 194 parameters, which include 140, 33, and 21 parameters for French
population characteristics, communal interaction, and SARS-CoV-2 characteristics
respectively. The source code of the model can be found on GitHub [60].

66 A.K.BishwasandA.Rao
3.4.1.2 Recent Investigation 2
Like other nations, Tokyo was also suffering very hoarsely from COVID-19. Sun
et al. [61] analysed the spread of COVID-19, involving data assimilation (aka
particle filter approach), in the metropolis of Tokyo by using an agent-based model
with a particle filter approach. Their research helps in evaluating the effective
reproduction number. In their approach, the particle filter approach involves two
interesting steps: (a) Based on the present model’s state, produce a prediction
for the model’s state on the subsequent step, and passage the time step forward;
(b) and, based on the observations on the present time step, update the model’s
state, where they use one day as one time step in our model because every
day new COVID-19 related data was available. They considered simultaneously
numerous independent simulations and consequently estimated some quantities,
such as unknown populations and unknown medical parameters, of interest with
a probability distribution. Figure 3.15 demonstrates the evaluation of the effective
reproduction number for Tokyo, considering from 6th March 2020 to 14th August
2021
In the context of their agent-based model approach, the method consists of an
extension of the SEIR model, which is based on seven compartments as shown in
Fig.3.16.
Where S is the compartment of all susceptible agents, E represents the exposed
agents, I represents the infectious agents, I indicates the infectious agents
a. s.
who are having clear symptoms and taking all necessary precautions, H signifies
Fig. 3.15 Evaluation of the effective reproduction number. Here, the black curve represents the
mean value; the light and dark coloured regions correspond to the 90 and 68% confidence intervals,
respectively. Grey regions indicate the states of emergency (Image Source: [61])

3 EpidemiologyModelling 67
Fig. 3.16 The compartments and their path probabilities (Image Source: [61])
the hospitalized agents who all are getting treatments, D is the compartment
for deceased agents, and R characterizes the recovered agents. Although their
agent-based model with particle filter approach constitutes a simple method for
investigating the epidemic evolution, the assumptions, for example, the number of
agents in the susceptible S compartment is much larger than the cumulative number
of agents who got infected, the method considers might satisfy in Tokyo only with
specified population size. Based on the situation, by adjusting the S compartment
size limit, the approach can serve much wider interests.
3.4.1.3 Recent Investigation 3
Wang et al. [62] investigated the transmission of the virus in the real world by
simulating the situation with an agent-based model and discussed the prevention
strategy for the spread of the virus. Their simulated model is based on a stochastic
epidemic transmission model, developed by Hoertel et al. [63]. They used a
game engine Unity version 2019.4.18f1c1, developed by Unity Technologies [64],
for implementing the simulation. Where each individual has been represented as
a collidable sphere object and represented different health status conditions by
painting the spheres with different colours. They used the following colour coding:
green, orange, red and blue for “healthy”, “infected”, “detected” and “recovered”
respectively.
The simulation follows a simple societal model based on the following three
different types of building structures—workplaces, individuals’ residences, and
hospitals. They assume the scenario where the individuals leave their residences
between 6.00 a.m. to 7.00 a.m., march towards their workplaces, and come back
to their residences from the workplaces at some point of time during 6.00 p.m.
and 7.00 p.m. Each individual follows a random route out of many random routes
based on the map for their trips between building structures. The individual can
move in one of the following directions, “left”, “right”, “up” or “down” on the
map. The individuals are allowed to collide while they are travelling, although the
collision will not change the original moving direction. The simulation applied an
hourly based cap parameter on the number of valid collisions in a day an individual
can encounter based on the consideration of real-life situations. Out of many
interesting parameters, one can tune a parameter in the discussed simulation, known
as “Transmission possibility per contact”, which can determine the possibility

68 A.K.BishwasandA.Rao
of disease transmissions during the collisions. Other important parameters the
simulation is equipped with are a “pre-set incubation time”, “average cure time”,
and “fatality rate”. From the point of simplicity, the model assumes that the
recovered people will neither get infected again nor infect other healthy individuals.
The model is designed based on two strategies—the “Put on masks” order and
the “Stay-at-home” order, but during any stage of the simulation, the user can
change the public health strategies based on the requirements, so the model is highly
customizable. They did some experiments on the simulation with seven students,
aged between 16 to 21 years, tuning with different reproduction numbers which is
nothing but the expected number of cases that are directly generated by one case in
a certain population [62].
3.4.1.4 Recent Investigation 4
Krivorotko et al. [65] analysed the epidemic spread and compared the epidemio-
logical situations in the UK and the New York State (USA) using an agent-based
model, known as Covasim. They started their study by analysing the region-based
epidemiological data such as diagnoses, critical cases, hospitalizations, deaths, and
numbers of people tested. They used the data which was categorized based on
seasonality, stationarity, and dependency spaces. They also used machine learning
techniques to extrapolate the data for stipulating the unknown epidemiological
model’s parameters. They determined the model’s unknown parameters by using
the tree Parzen estimation method, for minimizing the objective function, [66] based
Optuna optimizer [67].
They validated the model with historical data for the year 2020. In their analysis,
the output of the model concludes that the COVID-19 spread with positive cases
remains same during the March of 2021 in New York but reduced in the UK if one
preserved the containment measures and the level of testing. For details of their
studies regarding the COVID-19 spread in New York (USA) and UK, please refer
[63, 65].
3.4.1.5 Some Other Interesting Studies
Walker et al. [68] used an age-structured stochastic “susceptible, exposed, infec-
tious, recovered” (SEIR) model to determine the effects of various social distancing
interventions and the global impact of COVID-19. F. Lorig et al. investigated the
COVID-19 transmission dynamics [69] with agent-based simulated models. Read
et al. [70] studied an SEIR model to evaluate the basic reproduction number and
early estimation of epidemiological parameters in Wuhan.
Bouchnita and Jebrane [71] used a hybrid multi-scale model of COVID-19
transmission dynamics and considered relaxed and regulator measures in a close
region of 250 individuals. Keeling et al. [72] demonstrated the efficacy of contact
tracing as a containment measure;

3 EpidemiologyModelling 69
Silva et al. [73] investigated different situations of social distancing interven-
tions by deploying economic and epidemiological effects. They contemplated an
approach by combining the use of partial isolation and face masks. In some
of the recent investigations, Giordano et al. [74] and Zhao and Chen [75], the
investigators have more shade in simulating progression through different disease
statesandanalysedtheeffectsofnumerouspopulation-wideinterventionslikesocial
distancing and testing on Covid-19. Dehning et al. [76] analysed by quantifying the
impact of intervention measures in Germany using a SIR model.
Chang et al. [77] proposed a mobility network model of Covid-19 using a
metapopulation susceptible–exposed–infectious–removed (SEIR) model to simu-
late the spread, the model integrates fine-grained, dynamic mobility networks. They
used the largest ten US metropolitan areas for the investigation. They used the
mobile phone data of 98 million people and mapped their hourly based movements.
They demonstrated that the SEIR model fits the real case scenario well.
Kastalskiy et al. [78] proposed a system of models for Covid-19. In their
approach, they considered the social stress dynamics with classical epidemic
models, where they defined social stress by the socio-physics tools. They combined
a dynamic SIR model with the classical group of stages of the alarm-resistance-
exhaustion and general adaption syndrome with 13 countries’ statistical data which
demonstrated optimal fitness of the model.
Martin et al. [79] discussed the modelling of SARS-CoV-2 in Germany, where
they designed the model with a graph-based SIR model concentrating on commuter
testing. They assess the efficacy of the different intervention strategies after one
month by conducting numerical simulations. They observed that the virus dynamics
in the counties under consideration are initialized randomly with 75–150 new cases
occurrences per week per 100,000 red zone populations or below 10 cases in green
zones, and consider randomly distributed 25 red zone’s different initial scenarios
while considering 2 to 20% of all counties. They consider an ensemble set of 500
Monte Carlo runs for each scenario to account for ambiguity. In their investigation,
they found that it is very important to favour the lockdown in the out-of-control
regions to avoid the spread of the virus into other neighbouring regions. In recent
times, apart from the ABM, researchers are also using machine learning techniques
for Covid-19 epidemiological analysis and producing many interesting outputs. We
are now going to discuss some of the very interesting investigations on Covid-19
which use machine learning-based techniques.
3.4.2 Covid-19 Epidemiological Analysis with Machine
Learning
After the COVID-19 impact throughout the world, many researchers used machine
learning to analyse the situation and helped in policy-making decisions to under-
stand and control the spread of the virus. In this section, we have discussed some of
the recent interesting research in this domain.

70 A.K.BishwasandA.Rao
3.4.2.1 Recent Investigation 1
Zoabi et al. [80] used a gradient-boosting machine learning model built with
decision-tree base-learners [81] to develop a prediction model. Gradient-boosting
is a very popular machine learning algorithm for text prediction tasks with tabular
data.
The machine learning model predicts the COVID-19 positive/negative cases
using the following 8 binary features: (1) Sex (male or female), (2) age ≥60 years
.
(True or False), (3) Cough (True or False), (4) Fever (True or False), (5) Sore throat
(TrueorFalse),(6)Shortnessofbreath(TrueorFalse),(7)Headache (TrueorFalse),
and (8) Known contact with an individual confirmed to have COVID-19 (True or
False). The training and validation data set consisted of 51, 831 tested individuals
(where 4769 were COVID-19 positive cases), captured from 22nd March 2020 to
31st March 2020. The training-validation data set is divided at a ratio of 4:1. The
test data set consisted of 47, 401 tested individuals, where 3624 are COVID-19
positive cases. The test data was captured between 1st April 2020 to 7th April 2020.
The data set used has been publicly released by the Israeli Ministry of Health of
individuals who were tested for SARS-CoV-2 via RT-PCR. The performance of the
trained model on a test set with only balanced features in terms of ROC curves is
shown in [80]. They reported that if the model is trained and tested with filtered high
biased data, they observed an auROC of 0.862.
As per their study, they also found some issues with the released data like
missing feature values, biased, and some conditionally affected data sets. They tried
to mitigate the issues by assessing the model’s performance in real scenarios like
situations, such as selecting randomly negative reports of all the five symptoms
(Cough, Fever, Sore throat, Shortness of breath, Headache) at a time, and removing
them. The model still demonstrated hopeful outcomes, refer to [80].
3.4.2.2 Recent Investigation 2
The present world is a world of social media, where people demonstrate their
thoughts, opinions, their activities, feelings, emotions etc. Twitter is one of the
most popular social media platforms. Recent COVID-19 hit human life in such
a way that never has been experienced before. People have been using Twitter to
express their thoughts/opinions about COVID-19, and also keep on discussing the
vaccinations’ effectiveness and safety. Jalil et al. [82] studied the COVID-19 related
sentiment analysis using machine learning and deep learning on Twitter’s tweets,
refer to Fig.3.17 [82] for their approach. They collected such tweets from February
2020 to March 2020 and analysed their related sentiments and classified them
based on positive, negative, and neutral thoughts. The early detection of COVID-
19 sentiments helped them understand the situation and handle the pandemic. They
evaluated the model’s performance using accuracy, precision, recall, and F1 scores.

3 EpidemiologyModelling 71
Fig. 3.17 Overview of the overall approach (Image Source: [82])
Figure 3.17 overviews their overall approach. They first did a pre-processing
of the collected tweets by handling the noisy and heterogeneous data, then they
performed keyword trend analysis on the pre-processed corpus to identify the
most frequent words. Later, they used feature extraction techniques such as count
vectorizer, TF-IDF, and word embeddings to extract the features. In the end, they
trained the model with “eXtreme Gradient Boosting”, “LSTM based architectures”,
and “Multi-depth DistilBERT transformation”, and analysed their performances
on test data. They reported that the highest accuracy they achieved with the
transformer-based language classifier (96.66%), for the detailed results and analysis,
please refer to [82].
3.4.2.3 Recent Investigation 3
Recently, many different machine learning techniques have been applied to analyse
COVID-19 situations, Ghafouri-Fard et al. have compiled and discussed many
such techniques in [83]. We have discussed some of their interesting compilations
here. Using virus optimization algorithm (VOA) and adaptive neuro-fuzzy inference
system (ANFIS) [84], Behnood et al. [85] investigated the impact of population
density and numerous climate-associated parameters on COVID-19 spread. They
have demonstrated the influence of population density on the model’s performance
and highlighted the importance of social distancing in controlling the COVID-19
rate of infection. Pinter et al. [86] used a hybrid technique with ANFIS and MLP-
ICA (MLP imperialist competitive algorithm) to investigate the prediction of the
COVID-19 cases time series and mortality rate. Recently, an LSTM based approach

72 A.K.BishwasandA.Rao
has been used by Aora et al. [87] to forecast the COVID-19 positive cases in Indian
patients’ datasets. Kim et al. [88] have used a neural network-based approach, Hi-
COVIDNet, to study the infection risk to the target country among distant countries.
Using different regression analysis-based methods (each with a different polynomial
degree), Yadav et al. [89] analysed the COVID-19 cases. They claim that the sixth-
degree polynomial regression showed the best performance.
3.5 Conclusion
COVID-19 has employed devastating impacts on the world which triggered the
research communities to involve themselves in an investigation of the possible
causes, potential rate of impact, rate of spread, and the way of controlling the
virus’ blown-out effects etc. Research around the world is trying to use different
tools like compartmental modelling, agent-based modelling, and machine learning
to study COVID-19 and the way to control it, and helps in developing the decision
policies concerning the COVID-19 situation. We discussed how different tools have
been used to study the specific and situational depended COVID-19 cases. Each
tool has its pros and con and should be used based on detailed studies of the
circumstances. We also discussed some of the recent research investigations on
COVID-19 conducted with different tools.
References
1. Wikipedia, Covid-19 (2019). https://en.wikipedia.org/wiki/COVID-19. Accessed 11 Nov 2021
2. Worldometers, Coronavirus worldwide graphs (2022). https://www.worldometers.info/
coronavirus/worldwide-graphs/. Accessed 11 Feb 2021
3. J. Olsen, R.M. Jepsen, Human papillomavirus transmission and cost-effectiveness of intro-
ducing quadrivalent HPV vaccination in Denmark. Int. J. Technol. Assess. Health Care 26(2),
183–91 (2010)
4. IFAD Joint Statement by ILO, FAO and 13 October 2020 [Online]. WHO. Impact of covid-19
on people’s livelihoods, their health and our food systems. https://www.who.int/news/item/13-
10-2020-impact-of-covid-19-on-people’s-livelihoods-their-health-and-our-food-systems#:.
Accessed 02 Feb 2022
5. M. Szmigiera, Impact of the coronavirus pandemic on the global economy-Statistics & facts.
Statista. Retrieved in January 2023, from Statista website (2021)
6. https://www.worldbank.org/en/news/feature/2021/06/08/the-global-economy-on-track-for-
strong-but-uneven-growth-as-covid-19-still-weighs
7. https://home.kpmg/in/en/home/insights/2021/10/nep-covid-19-school-education-
assessments.html#:
8. Hippocrates, Ancient Medicine. Airs, Waters, Places. Epidemics 1 and 3. The Oath. Precepts.
Nutriment (P. Potter, Trans.) (Harvard University Press, Cambridge, 2022) (Loeb Classical
Library, Vol.147)
9. D.V. Glass, John graunt and his natural and political observations. Proc. R. Soc. Lond.
159(974), 2–37 (1963)

3 EpidemiologyModelling 73
10. J. Graunt, Natural and political observations mentioned in a following index, and made upon
the bills of mortality by john graunt ....; with reference to the government, religion, trade,
growth, ayre, diseases, and the several changes of the said city. The University of Michigan
Library provides access to these keyboarded and encoded editions of the works for educational
and research purposes (2022), pp. 1620–1674
11. D. Bernoulli, Exposition of a new theory on the measurement of risk. Econ. Soc. 22(1), 23–36
(1954)
12. J. Yuan, H. Qian, S. Cao, B. Dong, X. Yan, S. Luo, M. Zhou, S. Zhou, B. Ning, L. Zhao, Is
there possibility of vertical transmission of covid-19: a systematic review. Transl. Pediatr. 10,
2 (2021)
13. A.M. Kotlyar, O. Grechukhina, A. Chen, S. Popkhadze, A. Grimshaw, O. Tal, H.S. Taylor,
R. Tal, Vertical transmission of coronavirus disease 2019: a systematic review and meta-
analysis. Am. J. Obstetr. Gynecol. 224(1), 35–53 (2021)
14. C. Fenizia, M. Biasin, I. Cetin, et al., Analysis of SARS-CoV-2 vertical transmission during
pregnancy. Nat. Commun. 11, 5128 (2020)
15. M. Beesley, J. Davidson, F. Panariello, S. Shibuya, D. Scaglioni, B. Jones, K. Maksym,
O. Ogunbiyi, N. Sebire, D. Cacchiarelli,A. David, P. De Coppi, M. Gerli, Covid-19 and vertical
transmission: assessing the expression of ACE2/TMPRSS2 in the human fetus and placenta to
assess the risk of SARS-CoV-2 infection. BJOG Int. J. Obstetr. Gynaecol. 129(2), 256–266
(2021)
16. I. Chaubey, R. Vignesh, H. Babu, I. Wagoner, S. Govindaraj, V. Velu, SARS-CoV-2 in pregnant
women: consequences of vertical transmission. Front. Cell. Infect. Microbiol. 11, 717104
(2021)
17. A. AbdelMassih, R. Fouda, et al., Covid-19 during pregnancy should we really worry from
vertical transmission or rather from fetal hypoxia and placental insufficiency? Egypt. Pediatric
Assoc. Gaz. 69, 12 (2021)
18. W.H. Seto, D. Tsang, et al., Effectiveness of precautions against droplets and contact in
prevention of nosocomial transmission of severe acute respiratory syndrome (SARS). Lancet
361(9368), 1519–1520 (2003)
19. L.Zhou,S.Ayeh,V.Chidambaram,etal.,ModesoftransmissionofSARS-CoV-2andevidence
for preventive behavioral interventions. BMC Infect. Dis. 21, 496 (2021)
20. F. Brauer, C. Castillo-Chávez, Mathematical Models in Population Biology and Epidemiology
(Springer, Berlin, 2001)
21. G.M. Nakamura, G.C. Cardoso, A.S. Martinez, Improved susceptible–infectious–susceptible
epidemic equations based on uncertainties and autocorrelation functions. R. Soc. Open Sci. 7,
2 (2020)
22. https://healthcentricadvisors.org/wp-content/uploads/2017/03/Cal_Inf_Rates.pdf
23. P. Delamater, E. Street, T. Leslie, Y. Yang, K. Jacobsen, Complexity of the basic reproduction
number (r0). Emerg. Infect. Diseases 25, 1 (2019)
24. https://docs.idmod.org/projects/emod-generic/en/latest/model-si.html
25. W.O. Kermack, A.G. McKendrick, A contribution to the mathematical theory of epidemics, in
Proceedings of the Royal Society A (1927)
26. X. Wang, An SIRS epidemic model with vital dynamics and a ratio-dependent saturation
incidence rate, in Discrete Dynamics in Nature and Society (Wiley, Hoboken, 2015)
27. P. Guo, X. Yang, Z. Yang, Dynamical behaviors of an SIRI epidemic model with nonlinear
incidence and latent period. Adv. Differ. Equ. 2014, 164 (2014)
28. N.T.J. Bailey, The Mathematical Theory of Infectious Diseases and its Applications (2nd edn.)
(Griffin, London, 1975). 85264-231-8
29. R. Schlickeiser, M. Kr"oger, Analytical modeling of the temporal evolution of epidemics
outbreaks accounting for vaccinations. Physics 3, 2 (2021)
30. H. Zhang, L. Yingqi, X. Wenxiong, Global stability of an seis epidemic model with general
saturation incidence, in International Scholarly Research Notices (Wiley, Hoboken, 2013)
31. https://sites.me.ucsb.edu/

74 A.K.BishwasandA.Rao
32. O. Bjørnstad, K. Shea, M. Krzywinski, et al., The SEIRS model for infectious disease
dynamics. Nat. Methods 17, 557–558 (2020)
33. R. Beckley, C. Weatherspoon, M. Alexander, M. Chandler, A. Johnson, G. Bhatt, Modeling
epidemics with differential equations (pdf). Tennessee State University Internal Report, 2013
(2020)
34. G.A. Mu noz-Fernández, J.M. Seoane, J.B. Seoane-Sepúlveda, A SIR-type model describing
the successive waves of covid-19. Chaos Solitons Fract. 144, 110682 (2021)
35. H. Rahmandad, J. Sterman, Heterogeneity and network structure in the dynamics of diffusion:
comparing agent-based and differential equation models. Manage. Sci. 54(5), 998–1014 (2008)
36. O.M. Cliff, N. Harding, M. Piraveenan, E.Y. Erten, M. Gambhir, M. Prokopenko, Investigating
spatiotemporal dynamics and synchrony of influenza epidemics in australia: an agent-based
modelling approach. Simul. Model. Pract. Theory 87, 412–431 (2018)
37. T. Perkins, R.R einer, G. Espa na, Q. TenBosch, A. Verma, K. Liebman, et al., An agent-based
model of dengue virus transmission shows how uncertainty about breakthrough infections
influences vaccination impactprojections.PlosComput.Biol.15,3(2019)
38. E. Cuevas, An agent-based model to evaluate the covid-19 transmission risks in facilities.
Comput. Biol. Med. 121, 103827 (2020)
39. P.E. Lekone, B.F. Finkenst"adt, Statistical inference in a stochastic epidemic SEIR model with
control intervention: Ebola as a case study. Biometrics 62(4), 1170–1177 (2006)
40. M.H.A. Biswas, l.T. Paiva, M.D. Pinho, A SEIR model for control of infectious diseases with
constraints. Math. Biosci. Eng. 11(4), 761–784 (2014)
41. J. Rockl"ov, H. Sj"odin, A. Wilder-Smith, Covid-19 outbreak on the diamond princess cruise
ship: estimating the epidemic potential and effectiveness of public health countermeasures. J.
Travel Med. 27, 3 (2020)
42. W.C. Roda, M.B. Varughese, D. Han, M.Y Li, Why is it difficult to accurately predict the
covid-19 epidemic? Infect. Dis. Model 5, 271–281 (2020)
43. S. Eubank, H. Guclu, V.A. Kumar, M. Marathe, A. Srinivasan, Z. Toroczkai, et al., Modelling
disease outbreaks in realistic urban social networks. Nature 429(6988), 180–184 (2004)
44. M. Chinazzi, J. Davis, M. Ajelli, C. Gioannini, M. Litvinova, S. Merler, et al., The effect of
travel restrictions on the spread of the 2019 novel coronavirus (covid-19) outbreak. Science
368(6489), 395–400 (2020)
45. N. Hoertel, M. Blachier, C. Blanco, M. Olfson, M. Massetti, M.S. Rico, et al., A stochastic
agent-based model of the SARS-CoV-2 epidemic in france. Nat. Med. 26, 1417–1421 (2020)
46. I.Goodfellow, Y.Bengio,A.Courville,Deep Learning, vol. 326(MIT Press, Cambridge,2016)
47. S. Hochreiter, J. Schmidhuber, Long short-term memory. Neural Comput. 9(8), 1735–1780
(1997)
48. J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: pre-training of deep bidirectional
transformers for language understanding [cs. L] (2018)
49. V. Francois-Lavet, P. Henderson, R. Islam, M.G. Bellemare, J. Pineau, An introduction to deep
reinforcement learning. Found. Trends Mach. Learn. 11(3–4), 219–354 (2018)
50. D.H. Ballard, C.M. Brown, Computer Vision (Prentice Hall, Upper Sadle, 1982). 0-13-165316-
0
51. G. Guida, G. Mauri, Evaluation of natural language processing systems: issues and approaches.
Proc. IEEE 74(7), 1026–1035 (1986)
52. Speaker Independent, Connected speech recognition-fifth generation computer corporation,
fifthgen.com. Archived from the original (2013)
53. C. Reynolds, K. Merz, D. Ringe, Drug Design: Structure-and Ligand-Based Approaches, 1st
edn. (Cambridge University Press, Cambridge, 2010).-0521887236
54. W. Zhao, W. Jiang, X. Qiu, Deep learning for covid-19 detection based on CT images. Sci.
Rep. 11, 14353 (2021)
55. Q. Huang, A. Mondal, M. Ann Horn, F. Fan, P. Fu, X. Wang, H. Zhao, M. Ndeffo-Mbah,
D. Gurarie, SARS-CoV-2 transmission and control in a hospital setting: an individual-based
modelling study. R. Soc. Open Sci. 8, 3 (2021)

3 EpidemiologyModelling 75
56. National Bureau of Statistics of China, China Statistical Yearbook 2019 (China Statistics Press,
Beijing, 2019)
57. G. Chowell, L. Sattenspiel, S. Bansal, C. Viboud, Mathematical models to characterize early
epidemic growth: a review. Phys. Life Rev. 18, 66–97 (2016)
58. C.C. Kerr, R.M. Stuart, D. Mistry, R.G. Abeysuriya, K. Rosenfeld, G.R. Hart, et all., Covasim:
an agent-based model of covid-19 dynamics and interventions. Plos Comput. Biol. 2 (2021)
59. N. Hoertel, M. Blachier, C. Blanco, M. Olfson, M. Massetti, M. Sánchez Rico, F. Limosin,
H. Leleu, A stochastic agent-based model of the SARS-CoV-2 epidemic in France. Natl. Lib.
Med. 26(9), 1417–1421 (2020)
60. https://github.com/henrileleu/covid19
61. C. Sun, S. Richard, T. Miyoshi, Agent-based model and data assimilation: analysis of COVID-
19 in Tokyo (2021, Preprint). arXiv. https://doi.org/10.48550/arXiv.2109.00258
62. Y. Wang, H. Xiong, S. Liu, A. Jung, T. Stone, L. Chukoskie, Simulation agent-based model
to demonstrate the transmission of COVID-19 and effectiveness of different public health
strategies. Front. Comput. Sci. (2021)
63. N. Hoertel, M. Blachier, C. Blanco, M. Olfson, M. Massetti, M. Sánchez Rico, F. Limosin,
H. Leleu, A stochastic agent-based model of the SARS-CoV-2 epidemic in France. Nat. Med.
26, 1417–1421 (2020)
64. https://unity.com/
65. O. Krivorotko, M. Sosnovskaia, I. Vashchenko, C. Kerr, D. Lesnic, Agent-based modeling of
covid-19 outbreaks for new york state and UK: parameter identification algorithm. Sci. Direct
7(1), 30–44 (2022)
66. J. Bergstra, R. Bardenet, Y. Bengio, et al., Algorithms for hyper-parameter optimization, in
Advances in Neural Information Processing Systems, vol. 24 (2011)
67. https://optuna.readthedocs.io/en/stable/
68. P.G.T. Walker, C. Whittaker, O.J. Watson, et al., The impact of covid-19 and strategies for
mitigation and suppression in low-and middle-income countries. Science 369(6502), 413–422
(2020)
69. F. Lorig, E. Johansson, P. Davidsson, Agent-based social simulation of the covid-19pandemic:
a systematic review. J. Artif. Soc. Soc. Simul. 24, 3 (2021)
70. J.M. Read, J.R.E. Bridgen, D.A.T. Cummings, A. Ho, C.P. Jewell, Novel coronavirus
2019-nCoV (COVID-19): early estimation of epidemiological parameters and epidemic size
estimates. Philos. Trans. R. Soc. Lond. B Biol. Sci. 376, 1829 (2021)
71. A. Bouchnita, A. Jebrane, A hybrid multi-scale model of covid-19 transmission dynamics to
assess the potential of non-pharmaceutical interventions. Chaos Solitons Fract. 138(10994), 1
(2020)
72. M.J. Keeling, T.D. Hollingsworth, J.M. Read, Efficacy of contact tracing for the containment
of the 2019 novel coronavirus (covid-19). J. Epidemiol. Commun. Health 74(10), 861–866
(2020)
73. P.C.L. Silva, P.V.C. Batista, H.S. Lima, M.A. Alves, F.G. Guimara¯es, R.C.P. Silva, Covid-abs:
an agent-based model of covid-19 epidemic to simulate health and economic effects of social
distancing interventions. Chaos Solitons Fract. 139(11008), 8 (2020)
74. G. Giordano, F. Blanchini, R. Bruno, et al., Modelling the covid-19 epidemic and implementa-
tion of population-wide interventions in Italy. Nat. Med. 26, 855–860 (2020)
75. S. Zhao, H. Chen, Modeling the epidemic dynamics and control of covid-19 outbreak in China.
Quant. Biol. 8(1), 11–19 (2020)
76. J. Dehning, J. Zierenberg, F. Spitzner, M. Wibral, J. Neto, M. Wilczek, et al., Inferring change
points in the spread of covid-19 reveals the effectiveness of interventions. Science 369, 6500
(2020)
77. S. Chang, E. Pierson, P. Koh, et al., Mobility network models of covid-19 explain inequities
and inform reopening. Nature 589, 82–87 (2021)
78. I. Kastalskiy, E. Pankratova, E. Mirkes, et al., Social stress drives the multi-wave dynamics of
covid-19 outbreaks. Sci. Rep. 11, 22497 (2021)

76 A.K.BishwasandA.Rao
79. M.J. K"uhn, D. Abele, S. Binder, et al., Regional opening strategies with commuter testing and
containment of new SARS-CoV-2 variants in germany. BMC Infect. Dis. 22(1), 333 (2022)
80. Y. Zoabi, S. Deri-Rozov, N. Shomron, Machine learning-based prediction of covid-19 diagno-
sis based on symptoms. NPJ Digit. Med. 4, 3 (2021)
81. T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining,
Inference, and Prediction, ed. by T. Hastie, R. Tibshirani, J. Friedman (Springer, Berlin, 2009)
82. Z. Jalil, A. Abbasi, A.R. Javed, M.B. Khan, M.H.A. Hasanat, K.M. Malik, A.K.J. Saudagar,
COVID-19 Related Sentiment Analysis Using state-of-the-art Machine Learning and Deep
Learning Techniques (Frontiers Public Health, Lausanne, 2022)
83. S. Ghafouri-Fard, H. Mohammad-Rahimi, P. Motie, M.A.S. Minabi, M. Taheri, S. Nateghinia,
Application of machine learning in the prediction of covid-19 daily new cases: a scoping
review. Sci. Direct 7, 10 (2021)
84. M.A.A. Al-Qaness, A.A. Ewees, H. Fan, L. Abualigah, M.A. Elaziz, Marine predators
algorithm for forecasting confirmed cases of covid-19 in Italy, USA, Iran and Korea. Int. J.
Environ. Res. Public Health 17, 10 (2020)
85. A. Behnood, E.M. Golafshani, S.M. Hosseini, Determinants of the infection rate of the covid-
19 in the U.S. using ANFIS and virus optimization algorithm (VOA). Chaos Solitons Fract.
139, 110051 (2020)
86. G. Pinter, I. Felde, A. Mosavi, P. Ghamisi, R. Gloaguen, Covid-19 pandemic prediction for
hungary; a hybrid machine learning approach. Mathematics 8, 6 (2020)
87. P. Arora, H. Kumar, B.K. Panigrahi, Prediction and analysis of covid-19 positive cases using
deep learning models: a descriptive case study of India. Chaos Solitons Fract. 139, 110017
(2020)
88. M. Kim, J. Kang, D. Kim, H. Song, H. Min, Y. Nam, D. Park, J. Lee, Hi-covidnet: deep learning
approach to predict inbound covid-19 patients and case study in South Korea, in 26th ACM
SIGKDD International Conference on Knowledge Discovery and Data Mining, Virtual Event
(Association for Computing Machinery, New York, 2020)
89. R.S. Yadav, Data analysis of covid-2019 epidemic using machine learning methods: a case
study of India. Int. J. Inf. Technol. 12(4), 1321–1330 (2020)

Chapter 4
Agent-Based Behavioral Models:
Modeling COVID19 Behavior
Anand Rao and Arit Kumar Bishwas
4.1 Introduction
4.1.1 About This Chapter
Agent-based models have been extensively used in modeling individual behaviors,
collective behaviors, and social behaviors [1–3]. There is a close connection
between these behaviors and how individuals are organized and interact with each
other and within the overall structure and norms of society. Agent-based models
are being used extensively to study coupled human and natural systems (CHANS)
in ecological modeling as well as more broadly in sociological and behavioral
modeling. In the first section of this chapter, we will describe behaviors—individual,
collective, and social and examine the close connection between behaviors and
social structures—how individuals are organized and interact with each other. We
will review a number of applications of these concepts in psychology, sociology,
and management sciences.
Behavior modeling with agent-based models has been an active area of research
and application before the pandemic. With the COVID19 pandemic, the epidemi-
ological models discussed in the previous chapter have been extended to cover
a variety of individual and social behaviors during the pandemic. The dynamics
of the COVID19 pandemic was largely dictated by the behavior of the people
to the disease progression and the government interventions that were imposed
A. Rao (@)
Heinz College of Information Systems and Public Policy, Carnegie Mellon University, Pittsburgh,
PA, USA
e-mail: anandr2@andrew.cmu.edu
A. K. Bishwas
PricewaterhouseCoopers, Fremont, CA, USA
e-mail: aritkumar.official@gmail.com
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 77
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_4

78 A.RaoandA.K.Bishwas
to control the disease. In second section of this chapter, we describe how agent-
based modeling has been used to model the pandemic behavior of individuals,
including their mobility, social distancing, propensity to wear masks, pandemic
fear, pandemic fatigue, and a number of other behaviors. We will also examine the
interplay between these behaviors and the different government restrictions, such
as, stay-at-home order, bar closure, restaurant closure, ban on large gatherings, etc.
In the final section of this chapter, we take the epidemiological agent-based
model described in the previous chapter and demonstrate how we can model
the mobility and social distancing behaviors of individuals. We also illustrate the
interplay between individual behaviors and the overall disease progression and the
impact of government restrictions, cultural and geographic differences on individual
behaviors.
4.1.2 Objectives
This chapter is targeted at students learning the foundational concepts of agent-
based behavioral modeling, business users who want to apply the techniques in
a variety of advanced applications, policy makers who want to explore different
interventions to improve public safety, and researchers who are keen on advancing
the techniques and applications of this area. The primary objectives include
. The student will be able to model individual and collections of agents, their
structure and interactions, and evaluate individual and emergent behaviors;
. The business user will be able to identify the individual and social behaviors that
are of importance to their problem and their impact on business decisions;
. The policy maker will be able to identify the key interventions that need to
be evaluated and the likely behaviors expected from individuals in different
geographies and socio-demographic settings;
. The researcher will be able to identify key methodological, technical, and
performance issues related to building and calibrating agent-based behavioral
models.
4.2 Behavior Modeling: Framework and Concepts
4.2.1 What Is Behavior Modeling
Behavior is defined as the way a person or entity acts. For example, John throwing
a ball is a behavior; his dog jumping up to catch the ball is a behavior; a flock
of birds flying in the air is a behavior; cars stranded on a highway is behavior;
stock market rising 2% points today is a behavior. All these statements capture
an entity—a person, a dog, a bird, a car, a stock—acting in a certain manner—

4 ABBM 79
throwing, jumping, flying, stationary, or rising respectively. Some of these behaviors
are individual behaviors e.g., John, dog and others are collective behaviors e.g.,
collection of birds or cars or stocks. When this collective behavior is long-lived and
is based on the interaction between members of the same group it is called a social
behavior.
4.2.1.1 Types of Individual Behaviors
Each agent in an agent-based model can exhibit individual behaviors [4–12]. Let’s
start with an agent being an individual human and model human decision making.
Under these situations individual behaviors can be broadly categorized as follows:
Spatial Behaviors Agents are situated in space and time. Hence, a geographic
location or a point in space in a 2-dimensional or 3-dimensional grid is a natural
way to reason about an individual agent [7]. A spatial behavior then becomes an act
(or sequence of acts) to move from one location to another or the decision to remain
at the current location. Capturing spatial behaviors requires one to reason with either
absolute or relative distance between locations. For example, agent-based predator-
prey models are often situated in a two-dimensional space and have spatial behaviors
that help predators hunt their preys or the preys avoid their predators.
Temporal Behaviors Agents invariably have to reason about time leading to
temporal behaviors [7]. Movement across space as discussed above does not happen
instantaneously but happens over a period of time. Similar to spatial behaviors
an agent may reason with time in an absolute or relative sense. For example, an
automated social-media agent might send a New Year greetings to all your friends
at midnight on New Years day (absolute time); similarly your automated social-
media agent might be programmed to thank your follower immediately after they
decide to follow your channel (relative time or event-based).
Cognitive Behaviors In addition to reasoning about time and space, agents also
reason about their cognitive or mental states. Cognitive behaviors can span a broad
spectrum starting from simple stimulus-response rules to complex reasoning on the
beliefs, desires, and intentions of the agents and other agents it is interacting with
[2, 10, 13, 14]. For example, a robotic vacuum cleaner can sense an obstruction on
its path and stop immediately (stimulus-response behavior) and also execute a plan
to cover the entire floor area in the most efficient manner without hitting stationary
objects (optimized route planning behavior). We shall see later a rich variety of
techniques from rule-based programs, heuristics, statistical learning, deep neural
nets, genetic programming, etc., can be used to demonstrate a range of cognitive
behaviors.
As discussed above, agents in agent-based models are typically individuals or
entities (e.g., social-media agent or robotic vacuum cleaner) that are trying to mimic
human behaviors. Agents in agent-based models can also be used to model different
simpler entities, such as birds or fish or more complex entities such as corporations,

80 A.RaoandA.K.Bishwas
governments etc. In all of these cases the ‘individual behavior’ is reflective of the
individual agent that is being modeled—which can be a human, an animal or a
complex entity such as a corporation.
4.2.1.2 Types of Collective Behavior
When individuals interact with each other within a collective the individual
behaviors can interact with each other to produce collective behavior. When these
individual entities are living entities they are also referred to as populations and
the behaviors are referred to as population-level behaviors. For example, as we saw
earlier a flock of birds flying is a collective or population-level behavior.
Collective behaviors can be divided into two broad categories—planned behav-
iors and emergent behaviors.
Planned Behaviors When the interactions between multiple agents is explicitly
planned we have planned behaviors. The individual behaviors can be any of the
different types mentioned above. In the theory of planned behavior [15] attitudes,
subjective norms, and perceived behavior control drive intentions which influence
social behavior. For example, in an agent-based simulation of autonomous vehicles
(AV) multiple agents coordinating their movement across a geographic area to
optimize the pick-up of passengers at different location is an example of a
collective planned behavior. In planned behaviors there is an explicit or implicit
communication and coordination of individual actions.
Emergent Behaviors When the interactions between multiple agents emerges
from the collective, without any explicit planning we have emergent behaviors [16].
For example, agent-based models in ecology study the emergent movement of fish
schools, where each individual fish tends to keep a certain physical distance with
other fish and move parallel to other fish when they are in a certain range. Such
individual behaviors result in an emergent collective behavior of a school of fish.
Such emergent collective behaviors need not be restricted to animals such as fish or
birds but are also common amongst humans. Herd behavior amongst investors and
viral social media patterns are great examples of emergent behaviors that are widely
studied in economics and sociology.
4.2.1.3 Types of Social Behavior
When a collection of agents within a social structure interact with each other we
have social behaviors [7, 17–21]. The social behaviors go beyond the collective
behaviors we studied before as the social structure influences the individual and
collective behaviors and they in turn influence of the social structure. A social
structure is a collection of individuals as well as relationships between these
individuals [22]. For example, societal norms influence when and how agents
within a collection cooperate with each other or defect from the collective as

4 ABBM 81
observed in the study of flocking of birds. Similarly, individual behaviors can also
change the social structure. For example, the famous Schelling’s Segregation Model,
demonstrates how individual movement within a community can have a cascading
effect leading to segregation of individuals.
Social behaviors can be divided into four broad categories: cooperative behavior,
competitive behavior, herd behavior, and defection behavior.
Cooperative Behaviors When two agents within a social structure interact with
each other and perform actions that benefit the other it is called a cooperative
behavior. For example, agent-based models of Prisoner’s Dilemma evaluate when
individuals will cooperate, reciprocate, or defect based on the overall social
structure.
Competitive Behaviors When agents within a social structure perform actions that
benefit themselves or the group that they belong to and at the same time decreasing
the benefits to others we have competitive behavior. For example, agent-based
models of markets typically include both cooperative and competitive behaviors of
different groups [13].
Herd Behaviors When one or more agents imitate the actions of the collective we
have herd behavior [14,23,24]. The term is typically used when the individual agent
is not performing any cost-benefit analysis before deciding to imitate the group and
is ‘blindly’ following the herd. For example, agent-based models of financial system
‘bubbles’ model this type of herd behavior amongst investors.
Defection Behavior When one or more agents performs an action that is contrary
to the action performed by the collective we have defection behavior or contrarian
behavior. For example, agent-based models of investing often model contrarian
behaviors of individuals.
At first glance, collective behaviors and social behaviors may look identical or
very similar. However, what distinguishes a social behavior from a mere collective
behavior is the explicit recognition of social norms and social influence within an
overall social structure of individuals.
4.2.2 Why Build Agent-Based Models for Behavior Modeling
Agent-based models have been used in a variety of scientific, engineering, business,
and economic applications. Before we look at some of these applications of behavior
modeling using ABM we need to understand why we build agent-based models.
One might decide to build an agent-based model for five distinct reasons.
Explain One of the most common reasons for building agent-based models is to
explain observed behavior. In such cases, we either have a lot of data that we want
to use to explain what happened (e.g., inferring customer adoption behavior of a
product based on transactional data) or we have observed behavior that we want

82 A.RaoandA.K.Bishwas
to model to understand how individual agents interact to generate the observed
behavior (e.g., flocking behavior of birds). Building ABMs for this purpose leads
to a nuanced understanding of the problem including the dynamics of the behavior
and the sensitivity of different drivers of the observed behavior.
Predict When one has large volumes of historical data at an individual level ABMs
can be used to not only explain behavior, but also to predict behavior. While
traditional forecasting and predictive models can also be used for this purpose the
advantage of using ABMs is that the predictions are at an individual level and not
at an aggregated level. For example, agent-based models can be used to predict the
next best product for a customer based on historical data of all customer purchases.
Explore In a highly uncertain environment predicting future behavior may not
be feasible, instead ABMs can be used to explore different alternative scenarios.
ABMs in conjunction with scenario planning can result in robust models that can
explore alternative future states or alternative paths to specific future states. For
example, the uncertainty around the progression of COVID-19 during the early days
of the pandemic resulted in the exploration of a number of alternative scenarios e.g.,
V-curve, U-Curve, W-curve etc.
Change Once we build ABMs to explore alternative future scenarios we may want
to change the behavior of individual agents. Building such ABMs require persistent
models where the feedback from the intervention are incorporated into the model.
This requires ABMs to incorporate machine learning at either the individual level
or at the macro-level.
Generate ABMs can also be used to generate behaviors—behaviors that have not
been observed (e.g., different types of shocks to the economy or to individual
behaviors) or behaviors that require collection of data that may be protected or
difficult to collect (e.g., anomalous behavior like anti-money-laundering behavior
where the final determination of the anomalous transaction as to whether it is
fraudulent or not may not be known).
As we move from explanatory models to generative models we typically have
more uncertainty and less data. Also the ability to validate these models diminish as
we go from explanatory to generative models. Nevertheless, generative models can
still be extremely useful in reasoning about the unknown and exploring alternative
actions for unknown scenarios (Fig.4.1).
4.2.3 How to Build Agent-Based Behavior Models
4.2.4 Applications of Agent-Based Behavior Models
ABMs have found a number of applications in science and engineering, business and
economics, and environmental and public sector disciplines [25, 26]. The COVID-
19 pandemic has also highlighted the need to address complex epidemiological and

4 ABBM 83
Fig. 4.1 Purpose of agent-based models
behavioral issues that has brought ABMs to the forefront. As the computational
power has increased the ability to perform simulation on a large number of agents—
typically in the millions—has also increased. The overall move from on-premise to
cloud computing has also eased the availability of data and the ability to utilize on-
demand compute. ABMs are also evolving from one-off explanatory or decision
tools to becoming more persistent and embedded models within the overall IT
environment. We provide an overview of some of the key areas of applications of
ABMs
Science and Engineering ABMs have been extensively applied to problems in the
science and engineering disciplines. In the scientific realm ABMs have been used in
the following areas
. Biology and Medicine: In biology, ABMs have been used for systems biology
[27], ecological and population study of different species including forests,
insects, birds, fish, mammals etc. [7], modeling humans and artificial societies
including human crowds [28], anthropology [29], sociology [30], and psychology
[31]. In medicine, applications of ABMs have included cellular and sub-cellular
behavior [32], cancer growth modeling [33], propagation of pandemics and
epidemics [34, 35].
. Physics and Chemistry: In physics, ABMs have been used to model fluid flows
[36], design of safety critical systems [37], and analysis of failures in distributed
systems [38]. In Chemistry, ABMs have been used for modeling gene and protein
interaction networks [39], complex fluctuations in physiological systems [40],
and design of self-organizing systems [41].
. Engineering: In engineering, ABMs have been used to model air-combat
scenarios, command and control [42], unmanned aerial vehicles, aerospace and
defense systems [43], communication networks, transport networks, construction
and smart cities.

84 A.RaoandA.K.Bishwas
Social and Economic Modeling ABMs have played a central role in modeling
social and economic systems.
. Economic Modeling: Agent-based computational economics (ACE) studies the
emergence of market level behavior from the complex interaction of individual
behaviors [44, 45]. It has been used to model real estate, investing [46], asset
pricing [47], corporate bond trading [48], automated trading [49, 50], and market
meltdowns [51]. Since the 2008 financial crisis, interest in modeling financial
markets and understanding the stability of financial markets has increased [51,
52].
. Social Science: Agent-based computational sociology (ACS) studies the social
interaction between heterogeneous agents. They observe, analyze, and predict the
emergence of aggregate outcomes from individual behaviors. They have been
used to understand cooperation and social norms [53], diffusion [54], social
influence [55], culture dynamics [56], ethnic segregation [57], political coalitions
[58], ecological behavior [59, 60], and collective opinions.
Business and Organizational Modeling ABMs have been extensively used in a
variety of business applications across a number of functional areas. In addition,
ABMs have also been used to study organizational behavior.
. Business Modeling: ABMs have been used in strategic management and
decision making [61], marketing [62], distribution, customer experience [63],
research and development [64], operations and logistics [65], customer service
[66], risk [67], finance [68], and human resource functions [69].
. Organizational Modeling: ABMs have been used to understand organizational
change, organizational learning [70], organizational design [71], and organiza-
tional psychology [72].
We have provided a high-level view of the extensive range of ABM applications
today. A detailed analysis of these are beyond the scope of this book.
4.3 COVID-19 Modeling
In early 2020, as COVID-19 continued to race around the world at a frightening
and ferocious pace—often spreading misinformation along with it—governments,
organizations and people were clamoring for the truth about safeguards, how we
can fight back effectively and how long the nightmare will last. To get these
answers, we needed accurate, comprehensive models. While a number of models
[73] were produced initially with varying levels of infection rates and death rates
the constantly changing numbers caused a great level of consternation and distrust
of these models [74]. This backlash against the modeling community was based
on widespread mis-perception of how models are built and the role they play in
such crisis situations. Let’s examine this interplay between models, behaviors, and
government interventions.

4 ABBM 85
4.3.1 All Models Are Wrong, But Some Are Useful
“All models are wrong, but are some are useful” commented the British statistician
George Box, who later wrote, “All models are approximations.” So, the question we
need to ask is not, “Is the model true?” (It never is.) We need to ask, “Is the model
good enough for this particular application?”
A model, by its very definition, is a representation of a system that highlights
certain components and ignores others. Hence, it can never reflect all aspects of
reality. However, it is still instructive to understand when and why we get models
wrong.
Models are based on assumptions about what needs to be included and excluded
from reality. They are also based on assumptions about how different components
of the model interact. For example, there is a family of epidemiological models
that include some aspects of the disease and ignore others. SIR models look at
Susceptibility, Infection and Recovery (SIR) of individuals, while SIS models look
at Susceptibility, Infection and Susceptibility (SIS) again, as in recurrence of the
common cold. SIRD models add “Deceased” to SIR models, and SEIR models
account for “Exposure” when an infectious disease has an incubation period. SEIR
and SIRD models are the two types commonly being used for COVID-19.
Data is critical to build models and validate their accuracy—and feeding models
inaccurate data will produce inaccurate results. In the case of COVID-19, we need to
feed models the number of cases, hospitalizations and deaths due to the coronavirus
at a national, state and/or county level. We might have incomplete data (e.g., remote
areas may have difficulty collecting and sharing data) or inaccurate data (e.g., in
the early stages of a pandemic, the deaths may be associated with other secondary
conditions and may have been mis-categorized).
Finally, despite our best efforts, there is uncertainty—aspects of the model we
don’t know and may never know with certainty. There is still a lot of uncertainty
around COVID-19’s infection rate, incubation period and recovery rate—all of
which impact the reproduction rate. Furthermore, we still don’t know the impact of
the virus on different segments of the population. In addition to disease uncertainty,
we also have policy and behaviour uncertainty. We cannot say how different
governments and institutions will intervene in this crisis, or how citizens and
employees will behave in these stressful circumstances.
So, if models can be wrong, why build them? What purpose do they serve? As
we saw in Sect.4.2.2 models are built to explain, predict, explore, change, and
generate. COVID-19 models were built for all of these five purposes. One of the
first epidemiological models on COVID-19 was published by the Imperial College
team [73] on March 16, 2020. The model was used to predict potential future
infections and deaths from COVID-19 in UK and US. This model was built based
on understanding the reproduction rate of previous outbreaks of infectious diseases
and the available data from COVID-19 infections in China and South Korea. The
model also explored a number of public health or non-pharmaceutical interventions
to mitigate or suppress the disease. The level of uncertainty was high in the early

86 A.RaoandA.K.Bishwas
months of the pandemic, requiring a range of potential outcomes (e.g., infections,
hospitalizations, and deaths). As we learn more about the virus and our reaction
to it, the uncertainty decreased to some extent. Current COVID-19 models typically
provide a range for the number of cases, hospitalizations and deaths. The COVID-19
models were used to change the attitudes and behaviours of people—health officials,
policymakers, government institutions and citizens. So, while we could argue that
the COVID-19 models are “wrong,” they have still proved useful.
4.3.2 Some Models Are Useful, and a Few Change Behaviours
In just three months after the pandemic started, the behaviours of all segments
of society had changed dramatically, particularly among government officials and
policymakers, as well as citizens.
Health officials and policymakers responded to projections of COVID-19
models—however uncertain they were—by taking remedial measures. The
Coronavirus Government Response Tracker published the Stringency Index, which
examined 13 measures in response to the virus, including school and workplace
closures, cancellation of public events and travel restrictions—measures that would
be considered draconian under any other circumstances [34].
In response to government interventions, citizens largely complied with restric-
tions and changed behaviours. They were traveling less, sheltering at home, social
distancing and being more conscious of disinfection. They had also changed
their purchase behaviour. They were shopping online more rather than going to
physical stores, and they were consuming more bandwidth as social interactions
and entertainment moved online.
These changes in behaviour naturally impacted the key parameters of COVID-
19, thereby changing the data.
4.3.3 When Behaviours Change, New Data Trumps Models
COVID-19 infection, hospitalization and death curves were amplified by the media
in all affected countries as citizens were urged to “shelter at home” and “flatten the
curve.” As a result of behavioural changes, two sets of data started changing.
Case data As more people learned about the virus and received the message
to socially distance, they either ignored or heeded safety warnings, partially or
completely. Individual choices depended on a variety of factors: age, societal
values (deference to authority or libertarian-ism) and economic necessity to work,
among others. And new cases and hospitalizations started dropping in different
countries and US states, which had the intended effect of reducing deaths—but also,
perversely, made the original projections seem unrealistically pessimistic (wrong),
thereby opening up the model developers to criticism.

4 ABBM 87
Unemployment data Interventions such as closing businesses and schools shut
down economic activity and resulted in a massive reduction in the demand for a large
number of goods and services. This also increased unemployment to record levels
in the US and other nations—to numbers not seen since the 1929 Great Depression.
This, in turn, led to a cry to open the economy.
The impact of these interventions is what led Dr. Anthony Fauci, Director of the
National Institute of Allergy and Infectious Diseases, to comment, “When real data
comes in, then data, in my mind, always trumps any model.”
COVID-19 models wee, initially, built with whatever data we had, along
with assumptions about the progression of the disease. These models highlighted
the range of possible outcomes, leading policymakers and citizens to change
behaviour—resulting in the actual number of deaths being significantly lower than
what was originally estimated. So, ultimately the models did serve the purpose of
changing the behavior of citizens and public health authorities, by reducing the
number of deaths, so they should be viewed as successes.
However, after the initial few months and the first wave of infections had
died down pandemic-fatigue set in and there was substantial opposition to various
government interventions, such as, lock-downs, social-distancing, mask wearing,
travel restrictions etc. This opposition was also uneven across countries, regions
of countries, age and socio-economic groups further complicating the tasks of
prediction, exploration, change and containment of COVID-19. With the advent
of vaccinations additional behaviors and outcomes started playing out across the
world. While some parts of the world are well vaccinated the pandemic is by no
means fully controlled offering new strains to emerge and continuing uncertainty.
In the next section, we will look at individual, collective and social behaviors of
the COVID-19 pandemic.
4.3.3.1 COVID-19 Behaviors
Understanding the individual, collective, and social behaviors during the pandemic
has been an important factor in not only projecting the scale and speed of the
COVID-19 pandemic, but also how individuals, businesses, governments, and
society at large react and respond to events and actions. In this section, we describe
some of these behaviors and show how they have been used to explain, predict,
explore, change and generate behaviors. We also look at a number of agent-based
models that have captured and expanded on these behaviors.
Social Distancing Behavior Given that the COVID-19 virus was transmitted
through air one of the key interventions that public safety officials wanted individu-
als to adopt was to maintain a 6ft distance. While this is clearly an individual spatial
behavior the interaction between individuals led to a collective behavior—large
groups of individuals could no longer assemble in restricted spaces like restaurants
or bars and even boarding of aircraft had to be done with care [75]. The collective
behaviors also led to social behavior—for example grocery stores had to restrict

88 A.RaoandA.K.Bishwas
entry to only a certain number of individuals and the rest had to line up outside the
store maintaining the safe social distance of 6ft [76].
Mask Wearing Behavior The second key intervention in reducing and controlling
COVID-19 spread was the mask wearing behavior. Individuals were urged to wear
surgical or N-95 masks when interacting with others outside their home. This
was clearly an individual behavior but impacted other individuals on how they
behaved. The collective behaviors based on individual preferences and political
affiliations started exhibiting patterns of social behaviors. In US, large sections of
the population in the south were against wearing masks and saw it as a violation of
individual liberty, while large sections of the North-East and west coast population
adhered to the mask-wearing mandate and saw it as a demonstration of public good.
Agent-based modeling and simulation was used to determine the efficacy of wearing
masks and its role in reducing infections and potential deaths [77].
Mobility and Transportation Behaviors With each wave of the pandemic indi-
viduals were asked to restrict their movement. Hence, tracking individual mobility
behavior (e.g., spatio-temporal behavior) was key in understanding both adherence
to the guidelines and also the prediction of the spread of the variant within a
given population. As the pandemic progressed it was clear that not all individuals
could restrict their mobility—especially the ones in essential services that spanned
healthcare workers as well as others who needed to make and distribute essential
goods to keep the economy and society functioning. Agent-based simulation was
used to understand the localized movement of people within their census block
groups to predict the spread of COVID-19 [78]. Hence, understanding transportation
behavior of individuals on how they were commuting—by public transport, private
cars, taxis, walking etc. became important [79, 80]. As countries started reopening,
having a reliable spatio-temporal risk score to indicate the risk propensity of
COVID-19 was essential to reduce additional infections [81].
A detailed survey of the agent-based models of COVID-19 can be found in
Alsharhan [34]. These behaviors were modeled within agent-based models to
first understand and explain the infectivity and spread of COVID19, to explore
alternative interventions, and thereby change individual behaviors to reduce the
spread of COVID-19. For example, Zou et al. [82] use AnyLogic to simulate
pedestrian flow in a subway station to understand the impact of social distancing and
mask wearing behaviors on the spread of COVID-19. The analysis led to specific
recommendations and impact of the recommendations on the infectivity and spread
of COVID-19. For example, they were able to demonstrate that 70% mask wearing
behavior had a significant impact on the spread of the disease and social distancing
coupled with mask wearing had a significant complementary impact on the spread
of the disease.
The study of individual mobility patterns for different transport modes before
and during restrictions shed light on how to manage transport networks for safety
and efficiency. This study has been done in ten countries across six continents [83,
84]. A spatio-temporal mobility analysis of citizens at the state level during the

4 ABBM 89
pandemic shows that it takes 14 days for the mobility patterns in a state to adjust to
new situations [85]. The mobility patterns across railway, walking, private cars, and
taxi has changed significantly during the pandemic. By using financial incentives to
trade-off between infection and congestion, one can achieve safety and efficiency of
transportation networks [86]
Contact Tracing Behaviors Many governments and private sector entities have
deployed solutions to extensively trace the contacts that each individual has had
with others and alerting or quarantining individuals once someone in the network
has tested positive for COVID-19. The behavior itself can be categorized as a
government intervention behavior but contact tracing is a collection of interacting
individual contact behaviors leading to isolation or quarantining behavior of
individuals. For example, Freire and Casarin [87] investigate a number of COVID-
19 tracing apps within the European context. Agent-base modeling was used
to understand the disease progression and the effectiveness of contact tracing
interventions [88, 89].
Online Xenophobic Behaviors In addition to the above behaviors directly related
to the spread of the pandemic, there were a number of other behaviors that were
triggered by emotional reactions of people. Online Xenophobic Behavior [90]
against Asians and particularly Chinese has become common during the pandemic.
Hate speech is an individual behavior that impacts the collective behavior of
the group or the online community, provoking more collective behavior against
the individuals and communities. The Network Contagion Research Institute [91]
documented a sharp increase in online hate speech against Chinese during the initial
days of the pandemic.
Pandemic Fatigue Xenophobic behavior was not the only psychological behavior
during the pandemic. The initial fear and anger of the pandemic later grew into
resignation and pandemic fatigue. Agent-based models were used to evaluate the
phenomenon of pandemic fatigue and its impact on disease progression in the
community [92].
Government Intervention Behaviors At the institutional level governments and
enterprises were analyzing specific policy interventions that could have an impact on
reducing the spread of COVID-19. For example, [93] catalog twenty six indicators
of government response based on analyzing the measures of 14 countries. Agent-
based simulation at the city scale helped authorities to visualize disease progression
and evaluate the effectiveness of different interventions on the spread of the disease
[94]. Sophisticated agent-based simulations that incorporate feedback between
government interventions, response by citizens, and the resulting impact on disease
progression were developed using reinforcement learning [95]. Interventions for
specific sectors like education [96, 97] and health-care workers [98] were also
modeled using agent-based modeling.

90 A.RaoandA.K.Bishwas
4.4 How to Build Agent-Based Models?
In this section we describe how to build agent-based models. Agent-based models
have two main components—structure and behavior. The structural component of
the agent-based models specify the types of agents and their attributes. Agents
can be at different levels of granularity and can be connected with other agents
in a social structure. Agents can also communicate with each other. The structural
component captures the static aspects of an agent, while the behaviors capture their
dynamic nature. In this section, we outline a ten-step process for building agent-
based models. In the next Chap.4.5, we provide a concrete case study of building
COVID-19 epidemiological, behavioral and economic model.
The process of building and deploying an agent-based model can be split into
three phases, each with multiple steps.
. Ideate and Scope: This phase includes understanding the scope of the model to
be built, the number and type of agents, their attributes, their behaviors, and the
overall purpose and output of the model. This scoping also allows us to determine
the data requirements for us to build, test, and calibrate the model. The output of
this phase is a detailed ‘paper model’. By a ‘paper model’ what we mean is a
conceptual model of different agents, how they interact with each other and the
relationships between the different entities in the model. A causal-loop diagram
that explicitly captures the reinforcing and balancing feedback loops would be a
critical part of this paper model. See Colleen Lannon [99] for a brief description
of how to draw causal loop diagrams. We will see some examples of causal loop
diagrams in the next chapter in our COVID-19 case study. The key decision to
be made at the end of this phase is to make the decision of whether we want to
build an agent-based model or not. Lack of clarity of what we want to build or
the lack of sufficient data to build the model may be reasons to stop at the ideate
phase without proceeding to the next phase.
. Build and Refine: In this phase we first build a prototype of the model. We
usually start with a small number of agent, entities and their interactions to
simulate the behaviors that we want to observe. Progressively we had complexity
to the model to exhibit additional behaviors. Once we have a basic set of
behaviors we can calibrate the model to historical data. The future projections
made by the agent-based model needs to be calibrated with the real world data.
The deviations from the real world data might result in the further refinement
of the agent-based models. The updated model can then be compared with the
real word data again. This iterative process builds confidence in the output of the
model and progressively improves the original model. Once we have reached a
sufficient level of confidence a decision needs to be made in terms of deploying
the model for production use.
. Deploy and Maintain: In this phase the model we have built is scaled for
production use. We need to determine who and how many people will be using
the system, how often will they be using it, and how frequently the data and
the models need to be refreshed. This will determine the appropriate scaling

4 ABBM 91
and deployment of the prototype to ensure adequate speed and performance of
the system. Deploying large-scale agent-based models will also entail a number
of change management procedures to be in place to make the best use of the
tools. The insights generated by the agent-based models needs to be continuously
monitored and reported to the senior management. Based on the pace of change
of the external environment the agent-based model may need to be refined and
re-calibrated on a periodic basis.
The above description is an overview of the three phases and the key steps within
each phase. Each of these phases produces several design artifacts, code, and outputs
that can be used for operational or strategic decision making. In the next Chapter we
will examine some of these artifacts with the COVID-19 case study.
4.5 Conclusion
This chapter provided an overview and framework for behavior modeling by
examining individual, collective, and social behaviors. We then examined the five
different reasons for building agent-based models and looked at several applications
of agent-based behavior models in science, engineering, business, and economics.
We then examined the types of behaviors that were observed during the pandemic
and the interplay between the epidemiology, individual behaviors, government
interventions and the overall economy. We finally concluded with a brief overview
of how to build complex agent-based models. The primary contributions of this
work include:
. A taxonomy of individual, collective, and social behaviors that provide a
foundation for building a variety of agent-based models;
. A rationale for why and when to use agent-based models and how to build agent-
based models
. A survey of applications of agent-based models
Future work in this area can be targeted at building a robust methodology for
agent-based modeling. While a number of texts on systems thinking and system
dynamic modeling exist [100], the applications of these for agent-based modeling
deserves greater attention. In addition, combining agent-based modeling with the
recent work in reinforcement learning will also yield significantly more powerful
systems. Calibration of agent-based models and the elastic scaling of simulation are
significant technical and engineering challenges to be tacked in the future.
References
1. J. Badham, E. Chattoe-Brown, N. Gilbert, Z. Chalabi, F. Kee, R.F. Hunter, Developing agent-
based models of complex health behaviour. Health & Place 54, 170–177 (2018)
2. M.L. Baptista, C.R. Martinho, F. Lima, P.A. Santos, H. Prendinger, An agent-based model of
consumer behavior based on the BDI architecture and neoclassical theory, in Developments in

92 A.RaoandA.K.Bishwas
Business Simulation and Experiential Learning, vol. 41 (Association for Business Simulation
and Experiential Learning, 2014), pp. 170–178
3. E. Bonabeau, Agent-based modeling: methods and techniques for simulating human systems.
Proc. Natl. Acad. Sci. 99(3), 7280–7287 (2002)
4. N. Brandon, K.L. Dionisio, K. Isaacs, R. Tornero-Velez, D. Kapraun, R.W. Setzer, P.S. Price,
Simulating exposure-related behaviors using agent-based models embedded with needs-based
artificial intelligence. J. Exposure Sci. Environ. Epidemiol. 30(1), 184–193 (2020)
5. C. Bulumulla, L. Padgham, D. Singh, J. Chan, The importance of modelling realistic human
behaviour when planning evacuation schedules, in Proceedings of the 16th International
Conference on Autonomous Agents and Multiagent Systems (AAMAS) ed. by S. Das, E.
Durfee, K. Larson, M. Winikoff (International Foundation for Autonomous Agents and
Multiagent Systems, 2017), pp. 446–454. https://doi.org/10.5555/3091125.3091192
6. V. Cedeno-Mieles, Z. Hu, X. Deng, Y. Ren, A. Adiga, C. Barrett, S. Ekanayake, G. Korkmaz,
C.J. Kuhlman, D. Machi, M.V. Marathe, S.S. Ravi, B.J. Goode, N. Ramakrishnan, P. Saraf,
N. Self, N. Contractor, J.M. Epstein, M.W. Macy, Mechanistic and data-driven agent-based
models to explain human behavior in online networked group anagram games, in Proceedings
of the 2019 IEEE/ACM International Conference on Advances in Social Networks Analysis
and Mining, Vancouver (ACM, New York, 2019), pp. 357–364
7. D.L. DeAngelis, S.G. Diaz, Decision-Making in agent-based modeling: a current review and
future prospectus. Front. Ecol. Evol. 6, 237 (2019)
8. A.H. Dekker, Human behaviour modelling as an emerging disruptive M&S technology, in
Presented at the NATO MSG-111 Multi-Workshop on M&S Support to Transitioning Forces
and Emerged/Emerging Disruptive M&S Technologies, Sydney (2013)
9. J. Dugdale, Human Behaviour Modelling in Complex Socio-Technical Systems: An Agent-
Based Approach (Habilitation à diriger des recherches) (University Joseph Fourier, Grenoble,
2013), p. 85
10. M. Kvassay, P. Krammer, L. Hluchý, B. Schneider, Causal analysis of an agent-based model
of human behaviour. Complexity 2017, 1–18 (2017)
11. L. Nicoletti, A. Padovano, F.P. Vartuli, M. Vetrano, Human behavior modeling: a state of
the art, in Proceedings of the 6th International Defense and Homeland Security Simulation
Workshop (DHSS 2016), MSC-LES (2016), pp. 67–74. https://www.msc-les.org/proceedings/
dhss/2016/DHSS2016.pdf
12. C. Urban, B. Schmidt, PECS–Agent-based modelling of human behaviour, in Deformable
Avatars (IFIP IFIPAICT, ed. by N. Magnenat-Thalmann, D. Thalmann, vol. 68 (Springer,
2001), pp. 206-216. https://doi.org/10.1007/978-0-306-47002-8_18
13. D. Kar, F. Fang, F. Delle Fave, N. Sintov, M. Tambe, “A Game of Thrones”: when human
behavior models compete in repeated Stackelberg security games, in Proceedings of the 14th
International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2015)
(International Foundation for Autonomous Agents and Multiagent Systems, 2015), pp. 1381–
1390. https://doi.org/10.5555/2772879.2773329
14. C. Pahl-Wostl, E. Ebenhöh, Heuristics to characterise human behaviour in agent-based models
(p. 7), in Presented at the 4th International Conference on Environmental Modelling and
Software, Osnabrück, Germany (Brigham Young University, 2004)
15. A. Agarwal, Agent-based model of broadband adoption in unserved and underserved areas
(Master’s thesis). Missouri University of Science and Technology (2021). Retrieved from
https://scholarsmine.mst.edu/masters_theses/7973/
16. J.C. Jackson, D. Rand, K. Lewis, M.I. Norton, K. Gray, Agent-based modeling: a guide for
social psychologists. Soc. Psychol. Personal. Sci. 8(4), 387–395 (2017)
17. F. Bianchi, F. Squazzoni, Agent-based models in sociology: agent-based models in sociology.
Wiley Interdiscipl. Rev. Comput. Stat. 7(4), 284–306 (2015)
18. G.K. Bharathy, B. Silverman, Holistically evaluating agent-based social systems models: a
case study. Simulation 89(1), 102–135 (2013)
19. J.S. Coleman, Foundations of Social Theory (Harvard University Press, Cambridge, 1990)

4 ABBM 93
20. S.C. Marsella, D.V. Pynadath, S.J. Read, PsychSim: agent-based modeling of social interac-
tions and influence (2004), p. 6
21. B.G. Silverman, M. Johns, J. Cornwell, K. O’Brien, Human behavior models for agents in
simulators and games: part i: enabling science with PMFserv. Presence Teleoperator. Virtual
Environ. 15(2), 139–162 (2006)
22. S. Nowak, L. Matthews, A. Parker, A General Agent-Based Model of Social Learning (RAND
Corporation, Santa Monica, 2017)
23. L. Luo, S. Zhou, W. Cai, M.Y.H. Low, F. Tian, Y. Wang, X. Xiao, D. Chen, Agent-based
human behavior modeling for crowd simulation. Comput. Anim. Virtual Worlds 19(3–4),
271–281 (2008)
24. X. Pan, C.S. Han, K. Dauber, K.H. Law, A multi-agent based framework for the simulation of
human and social behaviors during emergency evacuations. AI & Soc. 22(2), 113–132 (2007)
25. R.J. Allan, Survey of agent based modelling and simulation tools (Technical Report DL-
TR-2010-007). Science & Technology Facilities Council, Daresbury Laboratory, Warrington,
(2010, October 7), p. 48. (ePubs-STFC?utm_source=chatgpt.com)
26. B. Heath, R. Hill, F. Ciarallo, A survey of agent-based modeling practices (January 1998 to
July 2008). J. Artif. Soc. Soc. Simul. 12(4), Article 9, 1–9 (2009). https://jasss.soc.surrey.ac.
uk/12/4/9.html
27. A. Montagud, M.P. de Leon, A. Valencia, Systems biology at the giga-scale: large multiscale
models of complex, heterogeneous multicellular systems. Curr. Opin. Syst. Biol. 28, 100385
(2021)
28. M. Okaya, T. Takahashi, Human relationship modeling in agent-based crowd evacuation
simulation, in Agents in Principle, Agents in Practice - 14th International Conference
(PRIMA’2011) (2011)
29. D.F. Adamatti, G.P. Dimuro, H. Coelho (eds.), Interdisciplinary Applications of Agent-Based
Social Simulation and Modeling (IGI Global, 2014)
30. Y. Sato, Does agent-based modeling flourish in sociology? Mind the gap between social
theory and agent-based models, in Reconstruction of the Public Sphere in the Socially
Mediated Age, ed. by K. Endo, S. Kurihara, T. Kamihigashi, F. Toriumi (Springer, Singapore,
2017), pp. 37–46. https://doi.org/10.1007/978-981-10-6138-7_3
31. A.R. Scalco, A. Ceschi, R. Sartori, Application of psychological theories in agent-based
modeling: the case of the theory of planned behavior. Nonlinear Dyn. Psychol. Life Sci. 22(1),
15–33 (2018)
32. M. d’Inverno, J. Prophet, Multidisciplinary investigation into adult stem cell behavior. Trans.
Comput. Syst. Biol. 3, 49–64 (2005)
33. Y. Mansury, M. Kimura, J. Lobo, T.S. Deisboeck, Emerging patterns in tumor systems:
simulating the dynamics of multicellular clusters with an agent-based spatial agglomeration
model. J. Theor. Biol. 219(3), 343–370 (2002)
34. A.M. Alsharhan, Survey of agent-based simulations for modelling COVID-19 pandemic. Adv.
Sci. Technol. Eng. Syst. J. 6(2), 439–447 (2021)
35. K. Bissett, J. Cadena, M. Khan, C. Kuhlman, Agent-based computational epidemiological
modeling. J. Indian Inst. Sci. 101, 303–327 (2021)
36. P. Tranouez, C. Bertelle, D. Olivier, C. Bertelle, D. Olivier, Changing the levels of description
of a fluid flow in an agent-based simulation (2004)
37. P. Dalapati, A. Padhy, B. Mishra, A. Dutta, S. Bhattacharya, Real-time collision handling in
railway transport network: an agent-based modeling and simulation approach. Transp. Lett.
11, 458–468 (2019)
38. E.F. Alsina, G. Cabri, A. Regattieri, An agent-based approach to simulate production,
degradation, repair, replacement and preventive maintenance of manufacturing systems, in
2014 IEEE Symposium on Computational Intelligence in Production and Logistics Systems
(CIPLS) (2014), pp. 24–31
39. L. Zhang, C.A. Athale, T.S. Deisboeck, Development of a three-dimensional multiscale
agent-based tumor model: simulating gene-protein interaction profiles, cell phenotypes and
multicellular patterns in brain cancer. J. Theor. Biol. 244(1), 96–107 (2007)

94 A.RaoandA.K.Bishwas
40. E. Kutumova, I. Kiselev, Ruslan N. Sharipov, G.I. Lifshits, F.A. Kolpakov, Thoroughly
calibrated modular agent-based model of the human cardiovascular and renal systems for
blood pressure regulation in health and disease. Front. Physiol. 12, (2021)
41. Z. Qin, Y. Lu, Multi-agent-based self-organizing manufacturing network towards mass
personalization, in Volume 2: Manufacturing Processes; Manufacturing Systems; Nano/mi-
cro/meso Manufacturing; Quality and Reliability (2021)
42. R.D. Flournoy, Leveraging human behavior modeling technologies to strengthen simulation-
based C2 system acquisition (2000), p. 6
43. R.E. Wray, J.E. Laird, Variability in human behavior modeling for military simulations, in
Presented at the Behavior Representation in Modeling & Simulation (BRIMS) Conference,
Scottsdale (2003), p. 10
44. M. Steinbacher, M. Raddant, F. Karimi, E. Camacho Cuena, S. Alfarano, G. Iori, T. Lux,
Advances in the agent-based modeling of economic and social behavior. SN Bus. Econ. 1(7),
99 (2021)
45. S. Mignot, A. Vignes, The many faces of agent-based computational economics: ecology
of agents, bottom-up approaches and paradigm shift. Œconomia History Methodol. Philos.
10(2), 189–229 (2020). https://doi.org/10.4000/oeconomia.8222
46. M. Taghavi, K. Bakhtiyari, E. Scavino, Agent-based computational investing recommender
system, in Proceedings of the 7th ACM Conference on Recommender Systems, RecSys’13
(Association for Computing Machinery, New York, 2013), pp. 455–458
47. B.-A. Cassell, M.P. Wellman, Agent-based analysis of asset pricing under ambiguous
information, in Proceedings of the 2011 Workshop on Agent-Directed Simulation, ADS’11
(Society for Computer Simulation International, San Diego, 2011), pp. 21–28
48. D.J. Berndt, D. Boogers, J. McCart, Agent-based models of the corporate bond market, in
Proceedings of the Second International Workshop on Data Science for Macro-Modeling,
DSMM’16 (Association for Computing Machinery, New York, 2016)
49. D. Minarsch, M. Favorito, A. Hosseini, J. Ward, Trading agent competition with autonomous
economic agents, in Proceedings of the 19th International Conference on Autonomous Agents
and Multiagent Systems (AAMAS’20) 2020 (International Foundation for Autonomous Agents
and Multiagent Systems, Richland, 2020), pp. 2107–2110
50. E. Sbruzzi, S. Phelps, Testing leverage-based trading strategies under an adaptive-
expectations agent-based model, in Proceedings of the 2013 International Conference on
Autonomous Agents and Multi-Agent Systems, AAMAS’13 (International Foundation for
Autonomous Agents and Multiagent Systems, Richland, 2013), pp. 1161–1162
51. Organisation for Economic Co-operation and Development (OECD), Systemic Financial
Risk: Agent-Based Models to Understand the Leverage Cycle on National Scales and
Its Consequences (Anita Gibson). OECD Review of Risk Management Policies (OECD
Publishing, Paris, 2012) https://doi.org/10.1787/9789264167711
52. J.D. Farmer, D.K. Foley, The economy needs agent-based modelling. Nature 460, 685–686
(2009)
53. A.A.B. Cohen, R. Muneepeerakul, G.A. Kiker, Intra-group decision-making in agent-based
models.Sci.Rep.11, 17709 (2021)
54. W. Rand, C. Stummer, Agent-based modeling of new product market diffusion: an overview
of strengths and criticisms. Ann. Oper. Res. 305, 425–447 (2021)
55. W.K.V. Chan, Agent-based and regression models of social influence, in 2017 Winter
Simulation Conference (WSC) (2017), pp. 1395–1406
56. N. Nguyen, H. Chen, B.W. Jin, W. Quinn, C.C. Tyler, A.S. Landsberg, Cultural dissemination:
an agent-based model with social influence. J. Artif. Soc. Soc. Simul. 24(4), 5 (2021)
57. T.C. Schelling, Micromotives and Macrobehavior (W.W.Norton & Company, New York,
1978)
58. P. Leifeld, Polarization of coalitions in an agent-based model of political discourse. Comput.
Soc. Netw. 1, 1–22 (2014)
59. N.R. Magliocca, Agent-based modeling for integrating human behavior into the food–energy–
water nexus. Land 9(12), 519 (2020)

4 ABBM 95
60. N. Schwarz, G. Dressler, K. Frank, W. Jager, M. Janssen, B. Müller, M. Schlüter, N.
Wijermans, J. Groeneveld, Formalising theories of human decision-making for agent-based
modelling of social-ecological systems: practical lessons learned and ways forward. Socio-
Environ. Syst. Model. 2, 16340 (2020)
61. S. Subramanian, A. Rao, How to build disruptive strategic flywheels. Strategy+Business,
(Issue 96) (2019). Retrieved from https://www.strategy-business.com/article/How-to-build-
disruptive-strategic-flywheels
62. E. Keles¸, F.H. Ergen Keles¸, Agent-based marketing: An inspiring review, in Paper Presented
at the 2nd LCBR European Marketing Conference, Munich (2014). https://doi.org/10.13140/
2.1.3429.5365
63. M. Hassouna, M. Arzoky, Agent based modelling and simulation: toward a new model of
customer retention in the mobile market, in Proceedings of the 2011 Summer Computer
Simulation Conference, SCSC’11 (Society for Modeling & Simulation International, Vista,
2011), pp. 30–35
64. K. Kieckhäfer, G. Walther, J. Axmann, T. Spengler, Integrating agent-based simulation and
system dynamics to support product strategy decisions in the automotive industry, in Winter
Simulation Conference, WSC’09 (2009), pp. 1433–1443
65. P.P. Datta, M. Christopher, P. Allen, Agent based modelling of complex production/distribu-
tion systems to improve resilience. Int. J. Logist. 10, 187–203 (2007)
66. R.B. Lam, Agent-based simulations of service policy decisions, in Proceedings of the 39th
Conference on Winter Simulation: 40 Years! The Best Is Yet to Come, WSC’07 (IEEE Press,
Piscataway, 2007), pp. 2241–2246
67. A.J. Bristor, S.L. Barnes, M.C. Fu, Regulation of systemic risk through contributory
endogenous agent-based modeling, in Proceedings of the 2014 Winter Simulation Conference,
WSC’14 (IEEE Press, Piscataway, 2014), pp. 863–874
68. F. Neri, How to identify investor’s types in real financial markets by means of agent
based simulation, in 2021 6th International Conference on Machine Learning Technologies,
ICMLT’21 (Association for Computing Machinery, New York, 2021), pp. 144–149
69. H.L. Riahi, F. Kebair, L.B. Said, Agent-based modeling and simulation of the emotional
experiences of employees within organizations, in Proceedings of the Conference on Summer
Computer Simulation, SummerSim’15 (Society for Computer Simulation International, San
Diego, 2015), pp. 1–10
70. I.-C. Moon, K.M. Carley, Evolving multi-agent network structure with organizational learn-
ing, in Proceedings of the 2007 Spring Simulation Multiconference-Volume 2, SpringSim’07
(Society for Computer Simulation International, San Diego, 2007), pp. 127–134
71. J. Jiang, B. Huisman, V. Dignum, Agent-based multi-organizational interaction design: a
case study of the dutch railway system, in Proceedings of the the 2012 IEEE/WIC/ACM
International Joint Conferences on Web Intelligence and Intelligent Agent Technology -
Volume 02, WI-IAT’12 (IEEE Computer Society, Washington, 2012), pp. 196–203
72. M. Marin, Y. Zhu, P.T. Meade, M. Sargent, J. Warren, System dynamics and agent-
based simulations for workforce climate, in Proceedings of the 38th Conference on Winter
Simulation, WSC’06 (2006), pp. 667–671
73. N.M. Ferguson, D. Laydon, G. Nedjati-Gilani, N. Imai, K.E. C Ainslie, M. Baguelin, S.
Bhatia, A. Boonyasiri, Z. Cucunubá, G. Cuomo-Dannenburg, A. Dighe, I. Dorigatti, H.
Fu, K.A.M. Gaythorpe, W. Green, A. Hamlet, W. Hinsley, L.C. Okell, S. Elsland, H.A.
Thompson, R. Verity, E. Volz, H. Wang, Y. Wang, P.G.T. Walker, C.E. Walters, P. Winskill,
C. Whittaker, C.A. Donnelly, S. Riley, A.C. Ghani, Report 9: Impact of non-pharmaceutical
interventions (NPIs) to reduce COVID-19 mortality and healthcare demand (2020). https://
doi.org/10.13140/2.1.3429.536510.25561/77482
74. Z. Tufekci, Don’t Believe the COVID-19 Models: That’s not what they’re for, The Atlantic
(2020)
75. B.H.P. Fabrin, D.B. Ferrari, Measuring proximity of individuals during aircraft boarding
process with elderly passengers through agent-based simulation, in Proceedings of the Winter
Simulation Conference, WSC’21 (IEEE Press, Piscataway, 2021)

96 A.RaoandA.K.Bishwas
76. M. Usman, T.-C. Lee, R. Moghe, X. Zhang, P. Faloutsos, M. Kapadia, A social distancing
index: evaluating navigational policies on human proximity using crowd simulations, in
Motion, Interaction and Games, MIG’20 (Association for Computing Machinery, New York,
2020)
77. E. Rosenstrom, J. Ivy, M. Mayorga, J. Swann, B.E. Oruc, P. Keskinocak, N. Hupert, High-
quality masks reduce covid-19 infections and death in the us, in Proceedings of the Winter
Simulation Conference, WSC’21 (IEEE Press, Piscataway, 2021)
78. J. Pesavento, A. Chen, R. Yu, J.-S. Kim, H. Kavak, T. Anderson, A. Züfle, Data-driven
mobility models for covid-19 simulation, in Proceedings of the 3rd ACM SIGSPATIAL
International Workshop on Advances in Resilient and Intelligent Cities, ARIC’20 (Association
for Computing Machinery, New York, 2020), pp. 29–38
79. Q. Hao, L. Chen, F. Xu, Y. Li, Understanding the urban pandemic spreading of covid-19 with
real world mobility data, in Proceedings of the 26th ACM SIGKDD International Conference
on Knowledge Discovery & Data Mining, KDD’20 (Association for Computing Machinery,
New York, 2020 ), pp. 3485–3492
80. N. Ayan, A. Ramesh, A. Seetharam, A.A. de A. Rocha, Hierarchical Models for Detecting
Mobility Clusters During COVID-19 (Association for Computing Machinery, New York,
2021), pp. 43–51
81. S. Rambhatla, S. Zeighami, K. Shahabi, C. Shahabi, Y. Liu, Toward accurate spatiotemporal
covid-19 risk scores using high-resolution real-world mobility data. ACM Trans. Spatial
Algorithms Syst. 8(2), 1–30 (2022)
82. J. Zhou, H.N Koutsopoulos, Virus Transmission risk in urban rail systems: microscopic
simulation-based analysis of spatio-temporal characteristics. J. Transp. Res. Board 2675(10),
120–132 (2021). https://doi.org/10.1177/03611981211010181
83. J. Huang, H. Wang, M. Fan, A. Zhuo, Y. Sun, Y. Li, Understanding the impact of the COVID-
19 pandemic on transportation-related behaviors with human mobility data (Association for
Computing Machinery, New York, 2020), pp. 3443–3450
84. D.M. Barbieri, B. Lou, M. Passavanti, C. Hui, I. Hoff, D.A. Lessa, G. Sikka, K. Chang,
A. Gupta, K. Fang, A. Banerjee, B. Maharaj, L. Lam, N. Ghasemi, B. Naik, F. Wang, A.F.
Mirhosseini, S. Naseri, Z. Liu, Y. Qiao, A. Tucker, K.P. Wijayaratna, P. Peprah, S. Adomako,
L. Yu, S. Goswami, H. Chen, B. Shu, A. Hessami, M.M. Abbas, N. Agarwal, T.H. Rashidi,
Impact of covid-19 pandemic on mobility in ten countries and associated perceived risk for
all transport modes. PLoS ONE 16, e0245886 (2021)
85. S. Wang, K. Wei, L. Lin, W. Li, Spatial-temporal analysis of covid-19’s impact on human
mobility: the case of the united states (2021). ArXiv, abs/2010.03707
86. M. Beliaev, E. Bıyık, D.A. Lazar, W.Z. Wang, D. Sadigh, R. Pedarsani, Incentivizing Routing
Choices for Safe and Efficient Transportation in the Face of the COVID-19 Pandemic
(Association for Computing Machinery, New York, 2021), pp. 187–197
87. M. Freire, J. Casarin, Investigating COVID-19 tracing apps as e-government service in
European context, in 14th International Conference on Theory and Practice of Electronic
Governance (ACM, Athens, 2021), pp. 444–449 .
88. E. Lanzarotti, L. Santi, R. Castro, F. Roslan, L. Groisman, A multi-aspect agent-based
model of covid-19: disease dynamics, contact tracing interventions and shared space-driven
contagions, in Proceedings of the Winter Simulation Conference, WSC’21 (IEEE Press,
Athens, 2021)
89. P. Gupta, T. Maharaj, M. Weiss, N. Rahaman, H. Alsdurf, A. Sharma, N. Minoyan, S. Harnois-
Leblanc, V. Schmidt, P.-L. St-Charles, T. Deleu, A. Williams, A. Patel, M. Qu, O. Bilaniuk,
G.M. Caron, P.L. Carrier, S. Ortiz-Gagné, M.-A. Rousseau, D.L. Buckeridge, J. Ghosn, Y.
Zhang, B. Schölkopf, J. Tang, I. Rish, C.J. Pal, J. Merckx, E.B. Müller, Y. Bengio, Covi-
agentsim: an agent-based model for evaluating methods of digital contact tracing (2020).
ArXiv, abs/2010.16004
90. R.K.-W. Lee, Z. Li, Online xenophobic behavior amid the covid-19 pandemic: a commentary.
Digit. Gov. Res. Pract. 2(1), (2020)

4 ABBM 97
91. S. Zannettou, J. Baumgartner, J. Finkelstein, A. Goldenberg, J. Farmer, J.K. Donohue, P.
Goldenberg, Weaponized Information Outbreak: A Case Study on COVID-19, Bioweapon
Myths, and the Asian Conspiracy Meme, Network Contagion Research Institute (2020)
92. L. Meacci, M. Primicerio, Pandemic fatigue impact on covid-19 spread: a mathematical
modelling answer to the Italian scenario. Results Phys. 31, 104895–104895 (2021)
93. C. Wang, Y. Gao, H. Zhang, Typical patterns of government response measures and trends
for covid-19 pandemic, in Proceedings of the 6th ACM SIGSPATIAL International Workshop
on Emergency Management Using GIS, EM-GIS’20 (Association for Computing Machinery,
New York, 2020)
94. G. Suryawanshi, V. Madhavan, A. Mitra, P.P. Chakrabarti, City-scale simulation of covid-19
pandemic & intervention policies using agent-based modelling, in Proceedings of the Winter
Simulation Conference, WSC’21 (IEEE Press, Piscataway, 2021)
95. R. Capobianco, V. Kompella, J. Ault, G. Sharon, S. Jong, S. Fox, L. Meyers, P.R. Wurman, P.
Stone, Agent-based markov modeling for improved covid-19 mitigation policies. J. Artif. Int.
Res. 71, 953–992 (2021)
96. U.K. Mukherjee, S. Bose, A. Ivanov, S. Souyris, S. Seshadri, P. Sridhar, R. Watkins, Y. Xu,
Evaluation of reopening strategies for educational institutions during covid-19 through agent
based simulation. Sci. Rep. 11, 6264 (2021)
97. J.Panovska-Griffiths,C.C.Kerr,R.M.Stuart,D.Mistry,D.J.Klein,R.M.Viner,C.Bonell,
Determining the optimal strategy for reopening schools, the impact of test and trace
interventions, and the risk of occurrence of a second covid-19 epidemic wave in the UK:
a modelling study. Lancet. Child Adolescent Health 4, 817–827 (2020)
98. C. Neuner, P. Bocciarelli, A. D’Ambrogio, BPMN-based simulation analysis of the covid-
19 impact on emergency departments: a case study in Italy, in Proceedings of the Winter
Simulation Conference, WSC’21 (IEEE Press, Piscataway, 2021)
99. C. Lannon, Causal loop construction: the basics. Syst. Thinker 23, 9 (2012)
100. J. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World
(McGraw-Hill, New York, 2016)

Chapter 5
COVID-19 Epidemiological, Behavioral,
and Economic Model
Anand Rao, Sindy Ma, Mark Paich, and Joseph Voyles
5.1 About This Chapter
Agent-based models have been traditionally used in the study of epidemiology. So
when the COVID-19 pandemic hit in 2020 it was one of the most common ways of
modeling the progression of the disease amongst the wider population both globally
and in specific countries [1–5]. The availability of COVID-19 tracking data and
the global nature of the pandemic facilitated widespread global sharing of data,
code, and models [6–9]. The epidemiological models were continuously updated
and calibrated to new data that was available on a daily basis. Given the substantial
role that behaviors played in the progression of the disease these models also
started capturing the individual behaviors of social distancing, mobility, and mask
wearing as well as behaviors by governments with respect to various restrictions on
movement andgatheringthatwerebeingimposed[9–12].Withtheeconomicimpact
of the pandemic the agent-based models were also extended to address the macro-
economic and sector-specific influences and impacts. The macro-economic impact
on growth and unemployment were factored into the behaviors of individuals,
businesses,andgovernments. Thesemodelswerethentailoredtoindividualindustry
sectors, such as healthcare, financial services, retail, manufacturing etc. evaluate
demand, supply, and production scenarios [5, 13, 14].
In this chapter, we describe an overall conceptual model of how to architect
complex agent-based systems that have multiple, interacting modules. We describe
A. Rao (@)
Heinz College of Information Systems and Public Policy, Carnegie Mellon University, Pittsburgh,
PA, USA
e-mail: anandr2@andrew.cmu.edu
S. Ma· M. Paich· J. Voyles
PricewaterhouseCoopers, New Yor k,NY,USA
e-mail:sindy.y.ma@pwc.com; mark.paich@pwc.com; joseph.voyles@pwc.com
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 99
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_5

100 A.Raoetal.
how to start from a core epidemiological model of an infectious disease such as
COVID-19 and overlay the different behaviors and their interactions. We drive
the design of the agent-based system using systems thinking and specifically use
the technique of causal loop diagrams to illustrate the complex interactions of
agent structures and their behaviors. We present a concrete agent-based architecture
with six different modules that combine epidemiological, behavioral, and economic
factors. Next we describe an agent-based epidemiological model and how it was
developed to project the progression of COVID-19 and how the model was
continuously updated with new data as well as emerging individual behaviors and
government interventions. In the section on the behavioral model we show how
we model individual physical behaviors like social distancing, mobility, and mask-
wearing as well as some of the emotional behaviors like fear and COVID-19 fatigue.
These behaviors play a critical role in modulating the epidemiological model and the
progression of the disease. Finally, we take this behavioral-epidemiological model
and see how it can be used to project demand for specific industry sectors. We take
examples from the healthcare sector with hospital and the retail sector. We conclude
by highlighting the key contributions of this work and directions for future work.
This chapter illustrates how industry-strength agent-based models are being built
and used to make operational, financial, and strategic decisions. It reinforces the
power and practicality of the agent-based approach to capture complex interactions
and make actionable recommendations in uncertain environments.
5.2 Objectives
This chapter demonstrates how large scale, industry strength, agent-based mod-
els are built to make key business decisions in an uncertain environment. The
application used to demonstrate this is the COVID-19 disease progression and the
challenges that individuals, businesses, and governments faced in 2020 in making
operational, financial, and strategic decision in an uncertain environment. This
chapter is targeted at students wanting to learn the practicalities of how to build
agent-based models; business users who are looking for insights on how to make
critical business decisions when uncertainty is very high; and policymakers trying
to understand the complex interplay between the disease progression, behaviors, and
the overall economic impact.
The primary objectives include
1. The student will be able to apply the concepts of agent-based models to build
large, complex systems;
2. The business user will be able to understand and appreciate the power of agent-
based models in making operational, financial, and strategic decisions;
3. The policy maker will be able to understand and evaluate how key policy
decisions and interventions can impact the behaviors of individuals, businesses,
and the overall economy
4. The researcher will be able to identify key engineering challenges in architecting,
running, and deploying large-scale agent-based systems.

5 ABCM-CaseStudy 101
5.3 Conceptual Model
The impact of COVID-19 has been broad, globally and across many facets of life, as
well as deep, impacting lives and our livelihood. Before we start designing an agent-
based model we need to first understand the basic entities of what we trying to model
fromthephysicalworldandthenlookattheirinteractionsandimpacts.Thebestway
to model all of the different aspects of interactions and impacts is to take a systems
level view, and isolate the key systems and the interactions between these systems.
Once we have the macro-level view, we can build more granular micro-level views
of just those systems that are directly relevant to specific behaviors we observe and
the decisions we want to make at the consumer, corporate, or national level. This
will allow us to be resilient—taking into account the key drivers from other related
systems, and also dynamic where we can focus on the immediate decisions at hand.
Figure 5.1 shows the system level view of all the macro and micro factors under
consideration.
At the macro-level four key systems are of interest to us:
• Pandemic progression: Covid19 disease progression is undoubtedly the key
system that influences all the other macro-level systems. A number of pandemic
level uncertainties like—uncertainties around the disease (e.g., infection rates,
incubation time, growth rate, hospitalization rate and fatality rate), testing (e.g.,
diagnostic testing, antibody testing, accuracy), data (e.g., number of hospitaliza-
tions,deaths),andcure(e.g.,therapeuticdrugs—theirefficacyandwhentheywill
be available, vaccines—their efficacy, trials, approval, and availability at scale)
influence the disease progression. These uncertainties are very localized and
Fig. 5.1 Macro-level and Micro-level view of pandemic

102 A.Raoetal.
time-dependent e.g., impact different countries, states, and even neighborhoods
differently at different times.
• Government Interventions: The disease progression undoubtedly influences
the government interventions. State-based social distancing, curtailment and
enablement of economic activity (like opening and closing of schools, bars,
restaurants, etc.), when and for how long a lockdown is imposed or lifted all
have an impact on both the economic activity and the behavior of people [15].
• Citizen behavior: The behavior of people, surprisingly, has turned out to be
one of the most significant macro-level system components of the pandemic—
both the spread of the disease and the ability of the economic activity to
rebound or falter [16]. While some countries and some states in US have
been very successful in enforcing restrictions of movement, with their citizens
complying with the government interventions, other states have either failed
to place restrictions and/or citizens have failed to comply. This macro-level
dynamic makes it extremely important and challenging when we consider its
micro-level impact on companies through consumer demand, workforce safety,
and eventually the financial viability of companies.
• Economy: The economy driven by the government interventions to either inhibit
or enhance economic activity due to the pandemic, the behavior of its citizens,
and the fiscal stimulus by governments to alleviate the economic pain on citizens
and companies is another major macro-level system component.
All four of these macro-level system components interact with the micro-level
system components. Customers, workforce, companies, demand, and supply are
four key micro-level components. Customers and workforce are micro-level variants
of citizens. Citizens within a region or zip code are considered as customers when
they engage in consuming products and services and also act as the workforce when
they are engaged in economic activity working for a company. Companies satisfy
the demand of their consumers and also produce goods or intermediate goods that
become supplies for other companies. Companies also employ the workforce to
produce goods and services. All of these interactions are mediated through cash
which underpins the economy.
At the micro-level, uncertainty in demand (e.g., the significant drop in demand
for some products and services like air travel and tourism or the significant increase
in demand for products like toilet rolls), supply chain disruption, workforce safety,
productivity, and scheduling were major influencers of economic activity. These
combined with the presence or absence of fiscal support from governments resulted
in the financial viability of the companies (i.e., profits, margins, liquidity, and
bankruptcy) and also the purchasing power, income levels and employment status
of individuals.
Making strategic or operational decisions requires one to not only have an
appreciation of the systems level view and the interactions between the components,
but also to understand the key drivers and the nature of these interactions (e.g.,
virtuous or vicious feedback loops). Given the speed at which decisions [17] need

5 ABCM-CaseStudy 103
Fig. 5.2 Epidemiological, behavioral and economic interactions
to be made, executives need to focus on the salient impacts of the pandemic and
how the normal feedback loops are altered by the pandemic [18].
A sample of the high level interactions between epidemiological, behavioral, and
economic factors are highlighted in Fig. 5.2. The epidemiological factors include
COVID-19 disease progression, vaccine effectiveness, and drug effectiveness. We
also saw a wide variety of behavioral changes at the individual, business, and
governmental levels. For example, individuals could stay-at-home, follow social-
distancing, wear masks, get vaccinated or do the exact opposite. Similarly, some
businesses were allowing their workers to work-from home, while others required
them to go to a physical location (e.g., hospital staff or manufacturing labor).
Governments were adopting various intervention strategic from full-to-partial lock-
downs, restrictions on travel, gatherings etc. All these behaviors also changed over
time as the COVID19 disease progressed and the successive waves of infections and
variants swept across the globe. Once vaccines were available the behaviors changed
again with some getting vaccinated and other refusing to get vaccinated changing
the dynamics of disease progression. In addition to the variations of these behaviors
over time, the behaviors also changed with respect to different countries and even
different regions within a country. In US the citizen behavior were sharply divided
between the north-east and the south with greater compliance to early government
restrictions in the north-east compared to the south. Government interventions at the
state and local levels were also different with more stringent gathering and travel
restrictions in the north-east compared to the south.
Examining the causality of these factors with their feedback loops is a powerful
way to understand the interactions and to evaluate alternative scenarios. As an
illustration of this approach we explore the interaction between the Covid19
progression, government interventions, citizen behavior, and economic demand.
Figure 5.3 captures some of the feedback loops. The Growth Loop shows the normal
economic cycle where increased economic activity leads to a greater demand for
goods and services which results in an increase in production that requires more
workers and more economic activity (labelled 1 in the figure). In a pandemic, more

104 A.Raoetal.
Fig. 5.3 Causal loop diagram of impact of COVID19
workers are exposed to the infection, resulting in more infected workers, and more
hospitalized workers. In the case of the “washout loop” the hospitalized workers
recover and start getting back into the economic activity (labelled as 2). However,
in some cases these hospitalized workers could die resulting in reduced economic
activity or the death loop (labelled 3). In addition, both hospitalization and death can
cause fear and panic amongst citizens resulting in them curtailing their movement
and depressing the demand for goods causing the demand suppression loop (labelled
4). The fear and panic due to the pandemic could result in increased government
restrictions that could reduce exposed workers and eventually less deaths from the
disease (labelled 5). However, increased government restrictions could also decrease
economic activity (labelled 6).
The above description is only a partial analysis of the impact of the pandemic.
The reduction in economic activity and the resulting increase in unemployment and
bankruptcies could cause the governments to relax restrictions potentially increasing
economic activity but also increasing the deaths due to the pandemic. Even this
effect might be moderated by some proportion of citizens refusing to participate
in the economic activity, even after the relaxation of restrictions. Understanding
these alternative feedback loops and selecting the ones that are most critical for the
specific managerial decisions are key elements of our computational approach. The
drivers and the feedback loops we discussed so far can be modeled quantitatively
to augment managerial decision making. We address this with examples from the
healthcare and consumer goods sectors.

5 ABCM-CaseStudy 105
5.4 COVID-EBE Architecture
The interactions between the epidemiological, behavioral, and economic factors
varying by time, across all industries, and globally can be extremely complex.
Breaking down these interactions into discrete component models helps us to build
agent-based models that are modular, scalable and easier to calibrate and use. In
this section, we present the overall architecture of the COVID model that we built
between March2020andMay2020fromcomponents ofmodels thatwealreadyhad
built prior to the pandemic. Given the speed at which the pandemic was unwinding,
the overall model was built incrementally and iteratively addressing the specific
questions that needed to be answered for our clients in different sectors. However,
we will present the eventual architecture called COVID-EBE (Epidemiological,
Behavioral, and Economic) model here. The architecture was instantiated for
different industry sectors—healthcare (provider, payer, and pharmaceuticals), retail,
and financial services. We illustrate the instantiation of the COVID-EBE model for
healthcare below.
Before we go into the details of the different modules it is instructive to consider
the types of questions we were trying to answer for clients as it related to COVID19.
The questions can be broadly categorized into three types. The three types in the
order of importance were
• Operational: The questions during the early days of the pandemic were more
tactical and operational questions. How do we keep our operations running?
What safety do we need to provide our staff who have to be physically be present
in a location (e.g., an hospital or manufacturing facility)? How do I ensure that
my staff are productive remotely?
• Financial: What are the short term and long term impacts to my financial
forecasts? How will my cash-flow change based on the increase or decrease in
demand, supply, and staff? How long can the business be viable under current or
projected scenarios? How will the pandemic impact the overall economy and the
ability of consumers to purchase goods? What will be the impact of the pandemic
on businesses and their viability?
• Strategic: How long will the pandemic conditions last? What are the likely
recover scenarios and how can we plan to survive and thrive under the different
scenarios? Will the behaviors of consumers, businesses, and economy get back
to pre-pandemic state or will there be a ‘new normal’? When will the vaccines
be available, how effective will they be, and how will they change the behaviors
and economic outlook?
As is clear from the questions above, answering them requires us to be able
to model the disease progression, understand behaviors of several groups, and
project economic and financial impacts under different scenarios. We envisaged six
models that formed the core of the COVID-EBE architecture that was built on an
existing foundational layer. Figure 5.4 below shows the overall model architecture
of COVID-EBE.

106 A.Raoetal.
Fig. 5.4 Conceptual architecture of COVID-EBE models
The six models fell under two levels—the market level and the business level.
The two market-level models were:
• COVID-19 Zip Code Disease Progression Model: This was the first model
that was developed and was released for use fifteen days after the declaration
of the pandemic by the World Health Organization on March 10, 2020. This
model initially provided the risk propensity of individuals within a US Zip code
to be infected with COVID-19 and the proportion that could then go on to be
hospitalized, would require ICU care, and the proportion that might eventually
die. The model projections were over time, showing the typical curves that
everyone is now familiar with. The simulations were initially done for each US
state and was then extended to counties. Subsequently, the model was enhanced
to evaluate different disease progressions scenarios (e.g., V, U, W), including
recurring waves of infections. We will look at the details of this model in the
next section.
• Economic Simulator: This model took the disease progressions scenarios, such
as the V, U, W curves and applied it to the economic situation. The primary
economic driver that was calculated was employment numbers that were released
on a weekly basis by job category and by county, which gave a good indication
of the economic activity. This was then mapped to the disposable income of
individuals and based on their socio-economic status their financial viability
and distress. This individual level financial status then drove the business level
models on demand for different good and services.
The market level models were interacting with specific industry sector level
models. The industry sectors that were primarily analyzed were healthcare, retail,
and financial services. The four industry level models were:
• Demand and Supply Simulator: In the early days of the pandemic the demand
for various goods were fluctuating widely some increasing substantially (include
reference) while others dropped substantially. While some of the demand was
determined by real need (e.g., ventilators for hospitals) others were driven by fear

5 ABCM-CaseStudy 107
that resulted in hoarding behavior (e.g., toilet paper). In addition to near term
demand, businesses also wanted to understand and prepare for future demand
under different disease progression scenarios. Similar to the demand simulator,
we also needed a supply simulator as international trade took a big hit causing
supply chain bottlenecks. Production and movement of goods within the country
also suffered significantly. We will look at some of the demand simulations for
hospital procedures and retail later in this chapter.
• Workforce planning and resource optimizer: The primary impact of the
pandemic was on individuals and their ability to function productively. Worker
safety, workplace practices to minimize infections, and workplace productivity
were key factors that need to be modeled. Businesses were looking for ways in
whichtheycouldorganize theirworkersinself-contained‘pods’toenablegreater
resiliency of their workforce. In addition, the model was designed to estimate
the infections and hospitalizations based on contact tracing, social distancing
policies, and site based testing.
• Risk and Cost simulator: The risk model translated the COVID19 risk factors,
along with the broader economic impact into the variations of demand and supply
in a specific sector. This was then used to estimate and simulate the change in cost
of goods sold for specific businesses. The scenarios were once again the disease
progression scenarios—V, U, W curves.
• Impact simulator: The final financial impact to a business was calculated by this
model by combining the insights from all of the previous models. The financial
impact could be analyzed for the different disease progression scenarios enabling
businesses to understand their financial and operational viability and determine
their course of action.
The six models were supported by several existing datasets and models. The
foundational datasets included a synthetic data set of US households and individuals
with over 40,000+ variables on the behavioral, socio-demographic, and financial
factors. In addition, a healthcare behavior predictor together with a physiological
model of human metabolism were useful in developing the initial COVID-19 risk
propensities and how they changed over time.
The four business level models explained above needed to be developed for each
of the industry sectors one is modeling. The characteristics of demand, supply,
workforce, and impact needed to be simulated at a more granular to be useful. We
did this by taking the COVID-EBE conceptual model and instantiating it for the
healthcare sector. The primary players we considered were hospital systems (e.g.,
providers) and also health insurance players (e.g., payers). Figure 5.5 shows the six
models but with the flow of key information from one model to the other and also
the external inputs used to analyze the COVID-19 progression, the demand, supply,
workforce considerations, and the economic and financial impact.
It is useful to analyze this diagram with respect to the inputs that we use at
the market level and business level (specifically for payers and providers) before
considering the key outputs that the models produce.

108 A.Raoetal.
Fig. 5.5 Healthcare sector COVID-EBE architecture
• US household and individual data: This is the synthetic dataset of 130 million
US households and the 330 million US individuals with their socio-demographic,
behavioral, health, and financial data. This pre-pandemic dataset was useful in
populating the initial model to consider the progression of the disease selectively
within the US population based on some of the known risk factors.
• COVID-19 tracking data: A couple of weeks into the pandemic daily COVID-
19 tracking data that captured the number of testing, the results of the testing,
number of hospitalizations, number of hospitalizations that were acute requiring
ICU care, and deaths were available at a state level and later on at a county level.
While some of the data was not accurate and sometimes ‘lumpy’ (e.g., some
counties uploaded data in bulk on a weekly basis or when available), the data
was still useful directionally in tracking the progression of the disease and as an
invaluable daily data to calibrate the models.
• Economic and employment data: Macroeconomic data, such as interest rates,
stock-market, growth rates and weekly employment data by state and industry
sector was used to drive the economic model.
• V, U, W Scenarios: A number of analysts started projecting potential scenarios
for economic recovery based on whether the economy would bounce back after
the first wave of infections (i.e., the V curve) or will be in a prolonged period
of stagnation before recovering to pre-pandemic levels (i.e., U curve) or will be
subject to a second wave (and potentially a third and fourth wave) resulting in
a recovery followed by another recession (i.e., W curve). The COVID-19 Zip
code disease progression model and the economic model used these scenarios
for simulation.
• Government interventions: Data around government restrictions on travel,
gatherings, social distancing, mask wearing, test availability, vaccine availability,
and stage of vaccination (e.g., first shot, second shot) across different states and
counties had to be collected.

5 ABCM-CaseStudy 109
• Volume and Urgency of Hospital Procedures: Two critical elements for
the demand and supply simulator were the pre-pandemic volume of hospital
procedures andtheurgency oftheseprocedures. Thesewerethenmodifiedduring
the pandemic based on the disease progression.
• Apprehension of Patients: The demand for non-COVID-19 hospital admission
were very difficult to estimate as it was driven by fear of potentially getting
infected of COVID-19 in the hospital and the urgency of the procedure needed.
This was specifically collected from individual hospitals based on pandemic
bookings and cancellations for different procedures.
Figure also shows a number of intermediate outputs produced by the models that
fed into the other models of the overall architecture. Some of the key intermediate
outputs include
• COVID-19 disease progression: The most important output of the COVID-19
Zip code progression model was to estimate the future infections, hospitaliza-
tions, severe cases and death at a granular (e.g., state or county or city) level and
over 30, 60, 90 day periods.
• COVID-19 economic data: The second most important aspect of the COVID-
19 Zip code progression model was to perform the disease progression across the
different V, U, W, scenarios under different government interventions.
• Member mix by scenario by state: One of the outputs of the economic models
for the healthcare sector was to estimate the employment status and disposable
income of its members by different scenarios and by state. This was critical
in estimating the cost and who will bear the cost (e.g., individual, insurance
company or the State), as well as an input into the workforce, cost, and impact
simulators.
• Demand by procedure by month: One of the key outputs of the demand
simulator was to project the demand of specific procedures by month that was
factored into the workforce planning, cost, and impact simulators.
The key outputs for the healthcare sector—payers and providers helped answer
the operational and financial questions around the procedures that will be scheduled,
the cost, and profitability margins for these procedures. The outputs included
• Scheduled procedures: The list of procedures to be scheduled on a daily basis
in a hospital and aggregate the demand by specific categories to facilitate staff
assignment.
• Cost per procedure: The cost per procedure based on the procedure and
available resources.
• Monthly medical cost and long-term trends: The cost per procedure was used
to calculate the monthly costs as well as the long-term trends based on the
member mix and the economic conditions. Inabilitytopay and long-term medical
loss ratios were also a large concern of payers.
• Profitabilitymargin:Theimpactsimulatorestimatedtheprofitabilitymarginfor
the hospitals and payers were based on the demand, the cost of the procedures,
the payer mix and reimbursements.

110 A.Raoetal.
The details of the data and information flows between the models highlights the
intricate connections between the different macro-level and micro-level views as it
relates to the epidemiological, behavioral and economic factors. In the next three
sections we explore each of these factors in more detail.
5.5 COVID Epidemiological Model
In previous chapters, we looked at several equation-based epidemiological models,
SIR, SIRD, etc. Given the complexity of the COVID-19 Sars-cov-2 virus, especially
the length of the incubation period and the fact that some individuals may be
asymptomatic even after infection, but could still transmit and infect others, we
needed a modified epidemiological model. In addition, the epidemiological model
was required at as granular geographical level as possible—country, state, county,
city, zip code etc. The complex interactions between the disease progression, citizen
behavior and government interventions that we saw in the last chapter and this
chapter meant that the epidemiological model had to be dynamic and was also
changing as the pandemic progressed. Finally, the model predictions had to be
calibrated with the daily data that was available on the disease across different
states and counties. These three factors of the nature of disease, the dynamic nature
of the interaction and continuously available data for model calibration made the
development of the model challenging.
First, we look at the types of agents in the model. The three primary types
of agents are individual agents, government agents, and business agents. The
description of these agents, their attributes, and behaviors are shown in Fig. 5.6.
We are primarily concerned here with the first three types of agents—individuals,
businesses, and governments. As discussed by the feedback loops in earlier sections
there is a rich interaction between these three types of agents.
Let’s now look at how the disease progression takes place within an individual
agent. As shown in Fig. 5.7 an individual agent can be in any one of eight different
states. The model is largely based on the SIRD model that we discussed earlier with
some modifications. The Infected state is expanded to account for the specific nature
of the COVID19-Sars-cov-2 virus. We include both symptomatic and asymptomatic
infections. In addition, the symptomatic state leads to the Hospitalization state
which in some cases could be Severe. The state of immunity could come from
either being Vaccinated or having got the virus and Recovered from the virus.
Lastly, immunity is constrained by time and the appearance of new variants, putting
individuals back into a Susceptible state after a period of time.
The dashboard of the COVID-19 epidemiological model is shown in Fig. 5.8.
The dashboard gives predictions for specific states (e.g., NY and CA) for specific
dates (e.g., April 14, 2020). The total number of infections is shown as new
infections.Newconfirmed cases are actual or predicted numbers based on COVID-
19 test turning positive. The number of hospitalizations and deaths on that day are
shown as new hospitalizations and new deaths. The dashboard also shows the

5 ABCM-CaseStudy 111
Fig. 5.6 Types of agents in the COVID-19 EBE Healthcare Model
Fig. 5.7 State transition diagram for individual agents
cumulative number of hospitalizations and deaths as cumulative hospitalizations
and cumulative deaths.
The primary purpose of the epidemiological model is to estimate the number
of hospitalizations, number of recoveries and deaths over time for each of the
states based on the actual COVID-19 tracking data that was available every day.
By varying different parameters of the model (e.g., contact rate, incubation period)
we can show the range of uncertainty in the future predictions. Figure 5.9 shows the
recoveries and deaths as well as the cumulative recoveries and deaths for New York

112 A.Raoetal.
Fig. 5.8 COVID19-EBE-model-dashboard
Fig. 5.9 COVID-19 model predictions for New York
on April 14, 2020. The peak of the first wave occurred on April 12 with the daily
average deaths reaching 829 [19]. The uncertainty around the predictions is shown
as the gray area for each of the curves. Note that the uncertainty increases as we
move further out in time.
Figure 5.9 illustrates only the model predictions and not the reality of what
happened. In Fig. 5.10, we superimpose the actual hospitalizations and deaths until
April 14, 2020 and the projections of future hospitalizations and deaths by one of
the well known publicly available models—the Institute for Health Metrics and
Evaluation (IHME) at University of Washington [20]. Note that our model tracks
the historical hospitalizations and deaths well, but does not capture the ‘twin peaks’
of the first wave. Also the cumulative number of deaths as predicted by our model
as of April 14, 2020 was much higher than the IHME model.
As discussed earlier the projections of hospitalizations, recovery, and death had
to be computed for every state as the characteristics of the spread of COVID-19 was
different in each of the states. The new and cumulative hospitalizations and deaths
for each of the states as of early April 2020 is shown in Fig. 5.11. Note at that
stage of the pandemic NY and NJ were the two states with the highest number of

5 ABCM-CaseStudy 113
Fig. 5.10 COVID-19 model comparison with IHME predictions
cumulative hospitalizations and deaths. The infections, hospitalizations, and deaths
for some of the southern states of US were still very low. These numbers started
rising for the southern states later in the summer.
5.6 COVID Behavioral Model
In the previous section we described the disease transitions from a purely epi-
demiological perspective—populations were susceptible to infections, some of them
would be infected and may be symptomatic or asymptomatic; some of them would
be hospitalized and then recover; while others may die; those who recover from
the disease may be susceptible in the future based on the immunity they build.
But each one of these states are significantly influenced by individual behaviors,

114 A.Raoetal.
Fig. 5.11 COVID-19 model predictions for different states
business behaviors, and government interventions or behaviors. In this section, we
illustrate these behaviors and how they impact the disease states as well as the other
behaviors. A detailed understanding of these behaviors is critical in explaining how
these models work, why the models overshoot or undercut the original projections,
and finally why this is a good outcome of the modeling as opposed to be viewed as
something undesirable.
Figure 5.3 described a high-level causal model that linked disease progression,
individual behaviors, government interventions and demand. In Fig. 5.12 we go
deeper into the specific behaviors and attitudes. This diagram shows the standard
progression of the disease from infections, to hospitalizations, recovery, and death.
The infections are triggered based on individuals who have a high COVID risk. It
also includes one key behavior of Mobility and two key individual attitudes of Fear
and COVID fatigue. We also look at government interventions and specifically on
Government travel restrictions.

5 ABCM-CaseStudy 115
Fig. 5.12 Causal loop diagram of Mobility and COVID Risk
The best way to understand these causal loop diagrams is to follow through the
different feedback loops. We illustrate our diagram with six major feedback loops.
But before that some basics around feedback loops.
A positive edge means that the source and destination variables move in the same
direction. For example, the variable Mobility has a positive edge to COVID Risk
and this should be read as “All things being equal, an increase in Mobility will cause
and increase in COVID Risk”. Similarly, a negative edge between two variables
means that they move in opposite directions. For example, the variable Fear has
a negative edge to Mobility and this should be read as All things being equal, an
increase in Fear will cause a decrease in Mobility.
A feedback loop is said to be a reinforcing loop if the loop consists of all positive
edges and/or an even number of negative edges. In a reinforcing loop you have
a flywheel effect where a specific variable keeps increasing. A feedback loop is
said to be a balancing loop if the loop consists of an odd numbered of negative
edges. In a balancing loop an increase in one variable is offset by another variable
that decreases it and brings it in balance. Let’s examine a few feedback loops to
understand how different behaviors and attitudes drive them.
• Mobility induced infection fear—Balancing loop An increase in Mobility
results in an increased COVID Risk. This increased risk results in an increase
in the number of Symptomatic Infections. With more infections the Fear
of contracting COVID increases. This increased Fear causes a corresponding

116 A.Raoetal.
decrease in Mobility as more people stay at home. As we went through this
loop, we started with an increase in Mobility and ended up with that behavior
decreasing. In other words, it is a balancing loop and the reader can see that
it has one negative edge and the rest are positive edges. This behavior was
predominant in the early days of the pandemic where the fear of contracting
the disease curtailed mobility [21].
• Recovery induced decrease in fear—Reinforcing loop When we start with an
increase in Mobility, we can see an increase in Symptomatic Infections can
also result in an increase in theRecovery. As more people recover from a COVID
infection it decreases Fear which in turn increases Mobility. This is a reinforcing
loop where with people recovering from COVID-19 infection others get more
confident and increase their mobility. Of course, this then causes the risks and
infectionstoincrease.
• Death induced fear—Balancing loop When we start with an increase in
Mobility, we can see an increase in Symptomatic Infections, Hospitalizations,
Severity of cases, and eventually Death. This increase in Death causes an
increase in Fear which should decrease mobility. Once again this is a balancing
loop and a very powerful one at that.
Notice that the Fear variable is driven by the number of Symptomatic
Infections, number of Recoveries and number of Deaths. TheF ear factor might
differ from individual to individual, might differ based on where the individual is
geographically located influenced by their social circle, and might also vary by
time. This complex interaction is what is captured in the variable Fear .
• Government travel restriction induced indirect COVID Fatigue—Balancing
loop Next we examine an institutional behavior—namely Government travel
Restrictions. With increased Government travel restrictions there will be a
decrease in Mobility; following through the cycle via Symptomatic Infections
we can see that this can cause a decrease in Fear which in turn causes an
increaseCOVIDFatigue. Thisincreaseinfatigueresultsinacallforgovernment
restrictions to be lifted or in the model a decrease in Government travel
restrictions. Once again we end up with a balancing loop. Of course, as
discussed earlier the fear factor will be driven by a number of factors such as
Recoveries and Deaths as discussed earlier, in addition to the Symptomatic
Infections.Thiswasoneofthemostvisibleaspectsofthepandemic asamajority
of countries went through the cycle of enforcing government restrictions, seeing
the situation improve, citizens getting COVID fatigue and demanding the lifting
of restrictions.
• COVID Fatigue induced change in Mobility behavior—Reinforcing loop
Once COVID fatigue sets in people will change their behavior and go back to ‘old
habits’ and resume their normal activity. This is shown by a positive edge from
COVID Fatigue to Mobility. Once again tracing through the different variables
we can see that this becomes a reinforcing loop if we start from Mobility and
trace our path through Fear and COVID Fatigue back to mobility.
• Government travel restrictions induced direct COVID Fatigue—Balancing
loop In addition to the indirect effect of COVID Fatigue from Government

5 ABCM-CaseStudy 117
Fig. 5.13 Causal loop diagram of Mobility and COVID Risk
travel restrictions that we saw earlier, there is also a direct effect. This balancing
loop is shown in the diagram where an increase in travel restrictions causes
an increase in COVID Fatigue which in turn then results in a decrease in
Government travel restrictions.
In all of the above feedback loops we looked at just one of the behaviors—
namely our “mobility” behavior [11]. We can do the same analysis with respect to
the “social distancing” behavior (See Fig. 5.13) and also “mask wearing” behavior.
The behaviors are identical to that of mobility, with the exception that the polarities
are reversed for the factors that lead into “mask wearing” and “social distancing”
[12].
The causal loops above were modeled as two basic mechanisms in the model—
risk reduction and risk reduction fatigue. Risk reduction was modeled as a function
of voluntary reduction and compliance with mandated risk reduction. Examples
of mandated risk reduction include restrictions on mobility, lock-downs, and
mask wearing. Examples of voluntary reduction include non-mandated restrictions
on mobility (e.g. lower recorded levels of mobility during normal hours). The
temporary closure of non-essential businesses is also considered a mandated risk
reduction. When modeling, the ‘compliance’ measured for this type of restriction
will represent the impact the mandated closure had on mobility, as opposed to the
compliance with the closure mandate itself.
There is always some form of voluntary compliance with risk reduction—we call
this the baseline voluntary risk reduction compliance—but in times of great risk,

118 A.Raoetal.
the population increases its voluntary compliance. Assuming we are rational agents,
we can represent this increase as the additional utility to be gained by increasing
risk reduction compliance. We model this utility as a function of the perceived
COVID-19 risk, change in the perceived COVID-19 risk, the type of government
policy, and fatigue. This formulation represents the reasoning that with a worse
perception of the COVID-19 situation, people are likely to voluntarily engage in risk
avoidance. This is amplified when the recent change is great—in both directions.
That is to say, a great increase in cases and deaths will inspire a sharp increase in
risk avoidance whereas a great decrease in cases and deaths will cause a reactionary
loss of caution. The severity of the government intervention will also impact the
compliance of the population. We assume a more severe stance will cause higher
compliance. The strength of the importance of each of these factors is modulated by
calibrated parameters. As previously stated, the parameters are calibrated for each
geographical locale. The resulting risk appetite can vary greatly from one geography
to another.
As we discussed earlier, the relationship between voluntary risk reduction and
perceived danger is a balancing loop, creating endless oscillations. In practical
terms, we observe that cases or deaths rise and people voluntarily lock down.
Cases subsequently come down and people re-enter society. In theory, mandated
risk reduction can dampen this oscillatory behavior. However, there is a powerful
force working against actual risk reduction; we call it the risk reduction fatigue.
Staying in a state of risk reduction leads to risk reduction fatigue. How long
we can stay in this state before the fatigue becomes apparent is difficult to predict.
Searches for the term ‘covid fatigue’ peaked in January of 2022, two years into
the pandemic. Fatigue is produced as a product of prolonged risk reduction and
contributes to how willing the population is to engage in risk reduction. Fatigue
builds over time based on the level of risk avoidance. However, the behavior change
due to fatigue e.g., non-compliance to government restrictions may manifest itself
only after a prolonged period of fatigue.
Following the global pandemic there have been several publications analyzing
the spread and impact of the virus using agent-based modeling.
5.7 COVID Economic Model
In the previous section, we described how individual and government interventions
influence the behaviors of people that eventually impact the progression of the dis-
ease based on the epidemiological model described in Sect. 5.5. In this section, we
illustrate how these behaviors impact demand—a critical element of the economics
of a business and the economy as a whole. Given that COVID-19 impacted the
demand across a range of different goods and services; some of them positively with
an increase in demand (e.g., demand for online services) and some others negatively
with a decrease in demand (e.g., gas or petrol). As we discussed in Sect. 5.5 the
demand and supply need to be modeled at a specific sector. We consider the demand

5 ABCM-CaseStudy 119
for goods and services across two sectors—healthcare and retail. In the case of
healthcare, we look at demand for hospital beds—not just for COVID-19 patients,
but also for other procedures. We describe the ‘Demand and Supply Simulator’ for
hospitals and illustrate how we projected the demand for different procedures that
required hospitalizations and medical staff. In the case of retail, we projected the
demand for store visits and restaurant visits during the pandemic.
5.7.1 Healthcare Demand
The healthcare sector, especially the hospital system, was the ‘eye of the storm’
during the initial days of the pandemic. The hospitals were faced with a variety of
operational, financial, and strategic questions to address. The operational questions
were more near-term, while the strategic questions were more long-term. However,
all three sets of questions were critical to address and influenced each other.
The immediate operational questions was to estimate the demand for beds
for COVID-19 patients and estimate the severity of these patients to estimate
the demand for ICU beds. As we saw in Sect. 5.5, detailed epidemiological
models can be used to predict the demand by state and county for different
future scenarios. Once the ‘wave’ of COVID-19 patients were addressed, patients
requiring hospitalizations for other procedures could be addressed. These ‘other’
procedures were what the hospitals would have handled in the absence of COVID-
19, including Coronary Artery Bypass Graft (CABG), spinal, hip/knee replacement,
endocrinology etc. However, there were two critical parameters in estimating the
demand for these procedures—urgency and apprehension level. The urgency of a
particular procedure was determined by the criticality of the procedure as well as the
patients’ need for the procedure. The urgency level of a particular procedure for a
given patient was not directly influenced by COVID-19. However, the apprehension
level was a factor that was largely determined by the ‘fear’ of the patient potentially
contracting with COVID-19 while in the hospital. This apprehension factor kept
many patients away from the hospital, even when there was enough capacity in
the hospitals to handle such procedures. This was one of three major factors in the
number of ‘excess deaths’ due to COVID-19 [22].
Figure 5.14 shows a conceptual view of how we estimated the apprehension and
urgency levels for each patient for each procedure and then aggregated the demand
for these procedures over time to arrive at the demand curves by procedure for a
hospital. The four levels of the inverted pyramid on the left of the diagram shows
how the demand was calculated. The backlog of patients for different procedures
were calculated first based on historical (pre-pandemic) data and any potential
changes to this demand due to COVID-19 (e.g., lack of socialization leading to
more stress and mental illness in some patients). This baseline of patient need for
procedures did not translate immediately into scheduling an appointment at the
hospital. The prevailing level of government restrictions, the individual fear of the
patients (as discussed in the previous section) potentially contracting COVID-19 in

120 A.Raoetal.
Fig. 5.14 Procedure demand for hospitals
the hospital, and the patients’ own ability to withstand the adverse consequences
of not going through the procedure were all key influencers in the participation
by the patients. This participation then led to a subset of these patients scheduling
appointments for procedures based on the urgency of the procedure, the perceived
risk of not getting the procedure done, and the availability of provider facilities etc.
This realized demand then led to the ongoing demand based on the availability of
hospital staff—physicians, surgeons, care givers etc.
Figure 5.15 shows the demand for eleven major procedures across the country
by state and by zip code. For each of these procedures the demand was projected
by geography (i.e., zip code, county, or state) and by three different scenarios—U,
W, W*. In the case of the ‘U’ scenario the economy came back to normal after a
few months; with W there were two waves of COVID-19; and with W* there were
multiple waves of COVID-19. These projections were being made in mid-2020.
Figure 5.16 shows the demand for CABG procedures for the three different
scenarios. The demand is shown as a % change from January 2020 baseline. The
country was going through a summer COVID-19 wave and the assumption was that
there will be another wave during the winter. With these assumptions notice that the
demand does not get back to the January 2020 baseline until July 2021 for the U
scenario. The recovery is much slower for the W and W* scenarios. The cumulative
lost demand for these procedures are shown on the left.
These immediate operational questions also had a significant impact on the
financial questions. In the US healthcare system, the hospitals were reimbursed for
the procedures and the cost of care based on the insurance status of the individual.
The insurance status was determined by whether the patient was employed or
unemployed and also how old they were to qualify for the government-funded
Medicare and Medicaid benefits. Critical to the viability of the hospital was

5 ABCM-CaseStudy 121
Fig. 5.15 Demand dashboard for eleven procedures across US
Fig. 5.16 Demand curves for CABG procedures for a single county in Michigan
a good estimation of the number of procedures and the cost of care by these
insurance categories. While this is not too difficult to ascertain during normal
times it was a significant challenge to estimate during the pandemic in 2020.
Economic uncertainties around the level of unemployment by sector, the impact
of the government stimulus on the economy, and the availability of a vaccine were
all important determinants in determining the payer mix.
Figure 5.17 shows the total number of booked procedures by the level of
COVID-19 risk, employment status, and insurance status. These demand curves by
payer-mix or insurance type was critical in determining the financial viability of the
hospital and their cash-flow projections.

122 A.Raoetal.
Fig. 5.17 Booked procedures by COVID-19 risk type, payer-mix and employment
The near-term operational questions and medium-term financial questions led
to more long-term strategic questions. COVID-19 made telehealth more popular.
Given the fear factor more patients were willing to consult physicians over the
phone and video chats. For example, the medicare fee-for-service beneficiary
telehealth visits increased 63-fold, 840,000 in 2019 to 52.7 million in 2020 [23].
This phenomena was seen across a number of other insurance categories, including
employer paid insurance [24]. The natural question in mid-2020 was not only
the rate at which telehealth would rise, but also whether this was a temporary
phenomenon and if the trend will decline once we return to the post-pandemic
normal. Some [25] were looking at rethinking the way hospitals work today from a
hospital-centered approach to a patient-centered approach.
In this sub-section, we illustrated a few of the critical elements of integrating
the epidemiological and behavioral models of the previous sections to estimate the
demand for hospital procedures. The impact of demand on the financial viability
of the hospitals and also the impact of economic factors such as unemployment on
the demand, illustrate the interconnections of the epidemiological, behavioral, and
economic models.
5.7.2 Retail Demand
Government restrictions on mobility, mask-wearing and gatherings had a significant
impact on retail demand for restaurants, stores, and super-markets. Similar to
telehealth in the healthcare sector, the demand for online shopping for groceries
and online ordering at restaurants for take-out increased substantially during the

5 ABCM-CaseStudy 123
Fig. 5.18 Estimating retail demand
pandemic. These individual and government behaviors also changed business
behaviors. A number of restaurant chains and grocery chains introduced online
ordering. Given the variable demand and the restricted use of onsite space a number
of businesses also had to rethink their staffing plans and the layout of their space.
Figure 5.18 shows how to model retail sales based on a macro-economic and
micro-economic factors. The key macro-economic indicators that were used to
model retail demand were Gross Domestic Product and Gross State Product,
consumer sentiment, personal consumption expenditures, and unemployment rates.
These indicators were available at the state, county, and zip-code levels at a monthly
and in some cases weekly (e.g., unemployment rates) frequency. In addition,
by mid-2020 a number of data providers had started aggregating a number of
specialized indices to capture individual behaviors at a similar level of granularity
and frequency. These included he stay-at-home index, the mobility index, the dining
visits index, and the grocery visits index [26]. These indices and the resulting
scenarios were used to estimate the demand for visits to retail stores and restaurants.
These two examples should give the reader a good understanding of how the
models were tailored for specific industry sectors and the interconnections of
the epidemiological, behavioral, and economic models. In addition, they also are
illustrative of the constant interplay between individual, business, and government
behaviors. The ability of agent-based models to represent entities at different
levels of granularity (e.g., individuals, businesses, and governments) and capture
their behaviors have been instrumental in building sophisticated simulations of the
COVID-19 disease progression as well as its impact on the economy and broader
society.

124 A.Raoetal.
5.8 Conclusion
This chapter provided a comprehensive description of how to build complex
agent-based systems to evaluate decisions in an uncertain environment. Using the
COVID-19 pandemic as the anchor event this chapter described the architecture, the
complexinteractions,andtheoutputsofmultipleinteractingmodels.Theseincluded
the epidemiological models to project and evaluate the progression of COVID-19
by geography over time; the behavioral models at the individual and governmental
levels that influence the disease progression and also the impact of the disease on
these behaviors; the economic impact of the disease on the demand for different
products and services. The primary contributions of this work include:
• An architecture of multiple agent-based models interacting with each other to
evaluate complex business decisions;
• An epidemiological model of COVID-19 disease progression that is overlay-ed
with individual behaviors and government interventions;
• A behavioral model of COVID-19 that accounts for physical behaviors, such
as social-distancing, mask-wearing, mobility etc., but also captures emotional
behaviors such as fear and COVID-19 fatigue;
• Micro-economic demand models for the hospital and retail sectors that are based
on the epidemiological and behavioral models;
This chapter demonstrates the utility of the overall agent-based architecture
and system by taking two specific industry sectors e.g., hospitals and retail. This
has been done for a variety of different industry sectors including, evaluating
the demand for different types of drugs in the pharmaceutical industry during
the COVID-19 pandemic, the impact of the pandemic on the disposable income
of individuals, the demand for gas at gas stations when government mobility
restrictions are in place [27], the demand for air travel, the supply of manufacturing
staff or the level of absenteeism during the peak COVID-19 pandemic, and the
supply chain bottlenecks and impact on production in a manufacturing facility.
There is an opportunity to describe all of these different applications to provide
a comprehensive view of how agent-based models were used to make a variety of
critical decisions across a range of industry sectors during the pandemic.
The models described in this chapter were built with a view towards rapidly
building and deploying them to ensure that decisions were being made based on the
evaluation of a few uncertain future scenarios. The emphasis of the development
was to get models built and used and not on getting the models perfect. However,
calibrating, refining, refactoring, and sharing these models might be beneficial to
progress the state-of-the-art in building complex agent-based systems.

5 ABCM-CaseStudy 125
References
1. A.M. Alsharhan, Survey of agent-based simulations for modelling COVID-19 pandemic. Adv.
Sci. Technol. Eng. Syst. J. 6(2), 439–447 (2021)
2. O. Al-Abdulla, A. Kallström, C. Valderrama, J. Kauhanen, Simulation of the progression of
the COVID-19 outbreak in Northwest Syria using a basic and adjusted SIR model. Zoonotic
Dis. 2(2), 44–58 (2022)
3. H.S. Zou, H.H. Xia, J.H. Yuan, Anylogic-based model prediction analysis of the impact
of social distance obedience behavior on the spread of epidemics, in Proceedings of the
2nd International Symposium on Artificial Intelligence for Medicine Sciences, Beijing China,
October 2021 (ACM, 2021), pp. 545–550
4. N. Zhang, P. Cheng, W. Jia, C.-H. Dung, L. Liu, W. Chen, H. Lei, C. Kan, X. Han, S. Boni,
S. Xiao, H. Qian, B. Lin, Y. Li, Impact of intervention methods on COVID-19 transmission in
Shenzhen. Build. Environ. 180, 107106 (2020)
5. J. Panovska-Griffiths, C.C. Kerr, R.M. Stuart, D. Mistry, D.J. Klein, R.M. Viner, C. Bonell,
Determining the optimal strategy for reopening schools, the impact of test and trace interven-
tions, and the risk of occurrence of a second COVID-19 epidemic wave in the UK: a modelling
study. Lancet Child Adolesc. Health 4(11), 817–827 (2020)
6. T. Harweg, D. Bachmann, F. Weichert, Agent-based simulation of pedestrian dynamics for
exposure time estimation in epidemic risk assessment. arXiv:2007.04138 [physics] (2020).
arXiv: 2007.04138
7. N.M. Gharakhanlou, N. Hooshangi, Spatio-temporal simulation of the novel coronavirus
(COVID-19) outbreak using the agent-based modeling approach (case study: Urmia, Iran).
Inform. Med. Unlocked 20, 100403 (2020)
8. A. Aleta, D. Martín-Corral, A. Pastore y Piontti, M. Ajelli, M. Litvinova, M. Chinazzi, N.E.
Dean, M. Elizabeth Halloran, I.M. Longini Jr, S. Merler, A. Pentland, A. Vespignani, E. Moro,
Y. Moreno, Modelling the impact of testing, contact tracing and household quarantine on
second waves of COVID-19. Nat. Hum. Behav. 4(9), 964–971 (2020)
9. P.C.L. Silva, P.V.C. Batista, H.S. Lima, M.A. Alves, F.G. Guimarães, R.C.P. Silva, COVID-
ABS: An agent-based model of COVID-19 epidemic to simulate health and economic effects
of social distancing interventions. Chaos Solitons Fractals 139, 110088 (2020)
10. I. Brottier, P. Pipp, COVID-19: The Good, the Bad and the Agent-Based Model, AnyLogic
blog, 5 January 2020
11. J. Valentino-DeVries, D. Lu, G.J.X. Dance, Location data says it all: staying at home during
coronavirus is a luxury. The New York Times, April (2020)
12. J. Katz, M. Sanger-Katz, K. Quealy, A detailed map of who is wearing masks in the U.S. The
New York Times, July (2020)
13. F. Araya, Modeling the spread of COVID-19 on construction workers: An agent-based
approach. Safety Sci. 133, 105022 (2021)
14. C.C. Kerr, R.M. Stuart, D. Mistry, R.G. Abeysuriya, K. Rosenfeld, G.R. Hart, R. C. Núñez,
J.A. Cohen, P. Selvaraj, B. Hagedorn, L. George, M. Jastrze¸bski, A.S. Izzo, G. Fowler, A.
Palmer, D. Delport, N. Scott, S.L. Kelly, C.S. Bennette, B.G. Wagner, S.T. Chang, A.P. Oron,
E.A. Wenger, J. Panovska-Griffiths, M. Famulare, D.J. Klein, Covasim: An agent-based model
of COVID-19 dynamics and interventions. PLOS Comput. Biol. 17(7), e1009149(2021)
15. T. Hale, N. Angrist, R. Goldszmidt, B. Kira, A. Petherick, T. Phillips, S. Webster, E. Cameron-
Blake, L. Hallas, S. Majumdar, H. Tatlow, A global panel database of pandemic policies
(Oxford COVID-19 Government Response Tracker). Nat. Hum. Behav. 5(4), 529–538 (2021)
16. K. Firth-Butterfield, A. Rao, Lessons from COVID-19 modeling: The interplay of data,
models, and behavior. Agenda, World Economic Forum, May (2020)
17. A. Rao, K. Firth-Butterfield, 3 ways COVID-19 is transforming advanced analytics and AI.
Agenda, World Economic Forum, July (2020)
18. A.Rao,Anewwaytothinkaboutmodelingforuncertaintimes,TowardsDataScience,January
28, 2021

126 A.Raoetal.
19. NYC Department of Health, Tracking coronavirus in New York City: Latest map and case
count, NYC.gov (2025)
20. IHME (Institute for Health Metrics and Evaluation), COVID-19 Projections, healthdata.org,
University of Washington (2020)
21. J. Glanz, B. Carey, J. Holder, D. Watkins, J. Valentino-DeVries, R. Rojas, L. Leatherby, Where
America didn’t stay home even as the virus spread. The New York Times, pages April 2 (2020)
22. The Economist, Tracking COVID-19 excess deaths across countries, October 2021
23. L.W. Samson, W. Tarazi, G. Turrini, S. Sheingold, Medicare beneficiaries’ use of telehealth in
2020: trends by beneficiary characteristics and location. ASPE, Office of Health Policy, page
34 (2021)
24. J. Lo, M. Rae, K. Amin, C. Cox, Outpatient telehealth use soared early in the COVID-19
pandemic but has since receded. Peterson-KFF, Health System Tracker, page 14, February
(2022)
25. B. Adibe, Rethinking wellness in health care amid rising COVID-19-associated emotional
distress. JAMA Health Forum 2(1), e201570 (2021)
26. Google LLC, COVID-19 Community Mobility Reports, Google, October 15, 2022
27. S. Hoda, A. Singh, A. Rao, R. Ural, N. Hodson, Consumer demand modeling during COVID-
19 pandemic, in 2020 IEEE International Conference on Bioinformatics and Biomedicine
(BIBM), Seoul, Korea (South), December (IEEE, 2020), pp. 2282–2289

Part  III
| Creating  | Agent-Based  | Models       | of  Crisis  |
| --------- | ------------ | ------------ | ----------- |
|           |              | in  Python,  | and  R      |

Chapter 6
MyWealth: A Simple Model of Economic
Exchange in Python
Joaquim Margarido and Pedro Campos
6.1 Introduction
The growing attention devoted to Agent-Based Models (ABM) in the study of
simple and more complex economic phenomena is due, to a great extent, to the
inadequacy demonstrated by the prevailing theoretical frameworks for economic
analysis, during and after the global financial crisis of 2007–2008 [1]
An illustrative example of the ambitious steps being taken in the field of
Agent-Based Computational Economics (ACE) is the development of EURACE, an
attempt to construct an agent-based model of the European economy [2]. EURACE
was designed to model complex economic systems and simulate the behavior
of agents, such as consumers, firms, and governments, in response to changing
economic conditions and policies.
The downside of complex models, however, is that they require many validations
and are often overfitted relative to the world they are supposed to simulate. Using
simple games to learn agent-based models is an effective way to introduce and
develop an understanding of how agents operate in a complex system. Simple games
are easy to understand, which makes them an ideal tool for beginners. Additionally,
they allow learners to experiment with different strategies and observe the outcomes
of their decisions. This provides an opportunity for learners to practice building and
testing their own agent-based models.
Agent-Based Models combine links between individual and aggregate levels
of analyses. The connection between these levels is sometimes referred to as
J. Margarido (@)
ISEP, Porto, Portugal
P. Campos
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 129
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_6

130 J.MargaridoandP.Campos
emergence. According to [3], the large-effects of complex locally interacting
individuals endorse the appearance of emergent properties at the level of the
population. Aggregate behaviour may be produced by the interaction of individual
agents.
One popular example of emergence was given by Schelling [4], who developed
a simple game that illustrated the macro behaviour that emerged from micro
decisions. Some of these micro decisions are influenced by the system of inter-
action between those individuals and their environment. The kind of behaviour in
Schelling drivers example is contingent, that is, the behaviour of some depends on
what the others are doing. But this notion of behaviour cannot be isolated from
another important concept—the purpose. In general, individuals pursue goals, try
to minimize his/her effort and maximize his/her comfort. The goals, purposes or
objectives relate directly to other individuals and their behaviour.
In this part of the book, we simplify model presentation using languages like
Python, R, NetLogo, and Julia. It serves as a guide to build Agent-Based Models
from scratch—applying game theory (e.g. Ultimatum game or basic currency
exchange) and machine learning as frameworks. In this chapter we introduce
MyWealth, a simple model of economic exchange with a learning component,
developed step-by-step in Python. In this experiment, each agent gives one coin
(ex. one dollar) to one other agent at random if they have any money to give. If
they have no money, they do not give the coin. This model is similar to the “Simple
Economy” model developed by Uri Wilensky and William Rand [5]. Models of this
kind are described in Dragulescu and Yakovenko [6].
The model is designed to simulate the behavior of a simplified economy with a
small number of agents, such as consumers and firms, and a limited set of economic
transactions. In the Simple Economy model, consumers have a fixed budget and
purchase goods from firms based on their preferences and the prices of goods. The
Simple Economy model is useful for exploring basic economic concepts, such as
supply and demand, market equilibrium, and the impact of policy interventions.
It is often used as an educational tool for teaching economics and for introducing
students to the principles of agent-based modeling and simulation. In this work,
we start by introducing the principles of MyWealth game, and then we define he
different functions in Python. Then, in Sect. 6.5. we introduce MESA, and finish
with final considerations in Sect. 6.6.
6.2 The Principles of MyWealth
MyWealth simulates an economic system with a number of agents that interact with
each other in a marketplace. The system is composed of the following elements:
Environment
The environment in MyWealth is represented as a two-dimensional grid (that we call
“stage”) where agents can move around and interact with each other. The grid has a

6 MyWealth:ASimpleModelofEconomicExchangeinPython 131
fixed size that can be adjusted, and it can be populated with patches that represent
resources or obstacles in the environment.
Agents
The agents in the MyWealth Model can move around the grid and interact with each
other.
Relationships
The actions of the agents can impact the overall behavior of the system over time.
• A certain number of agents move to a random position in the stage represented
by a two-dimension array. This two-dimension array represents the cells of a grid
in the memory.
• Every time an agent moves to a cell, if any cell contiguous to that one is occupied,
the agent in that cell has to give a coin to the recently moved agent.
• Each agent’s turn to move is linear, which means the agent has a fixed turn. For
example, the agent number 0 is the first to move, the agent number 1 is the second
and so on.
• Each iteration implies the movement of every agent.
• The process may involve as many iterations as required.
The simulation works only in memory. The main output is the final number of
coins each agent has at the end of the simulation. There are some problems we have
to deal with:
• The size of the stage matters. If the stage is to large, most of the time the agents
will not get near each other and there will be zero or close to zero transactions.
If the stage is too small, at the end of the simulation the agents will have almost
the same wealth as when they started.
• When positioning the agents at the start of the simulation we must ensure that
they are positioned in an unoccupied cell.
• Every time an agent moves, it must move to an unoccupied cell.
• Each agent moves one cell at a time.
• Theagentcanonlymovetoacellaroundhimandnexttohisposition.Thatmeans
up, down, left, right, up-left, up-right, down-left and down-right. We call this a
“von Neumann neighborhood”, which is based a diamond-shaped neighborhood.
The cell movement is calculated randomly.
Let us see now how MyWealth is implement (see Pseudocode of Algorithm 1).
To keep it simple, the simulation is programmed using only two files:
• main.py—where the simulation starts and initial configurations are made
• agent.py—the definition and rules of the agents
The program flow is shown in Fig. 6.1.1
1 Program codes are available in: http://ml4agents.free.nf/

132 J.MargaridoandP.Campos
Algorithm 1 Agent-Based Wealth Exchange Model
1: Initialize parameters: number of agents N, grid size (rows, columns), number of iterations T
2: Create an empty 2D grid of size (rows, columns)
3: for each agent i in 0 to N – 1 do
4: Randomly assign agent i to an unoccupied cell
5: Set agent i’s coin count to 1
6: end for
7: for iteration = 1 to T do
8: for each agent i in order 0 to N – 1 do
9: Identify unoccupied neighboring cells (Moore neighborhood)
10: if there are available cells then
11: Randomly select one unoccupied neighboring cell
12: Move agent i to the selected cell
13: for each occupied neighboring cell after movement do
14: Neighboring agent gives 1 coin to agent i
15: Update coin counts accordingly
16: end for
17: end if
18: end for
19: end for
20: Output final coin count for each agent
Fig. 6.1 Program flow of the
agent based wealth exchange
model in Python
6.3 The main.py File (The Entry Point)
In the entry point (the first code the program runs when starts) we define the first
parameters of the simulation: the number of agents, 50, and the number of iterations,

6 MyWealth:ASimpleModelofEconomicExchangeinPython 133
1000. We also create the stage represented by a grid with 50 columns by 50 rows.
The pseudocode of the Agent-Based Wealth Exchange Model is shown below.
| num_agents  =  50  |          |     |     |
| ------------------ | -------- | --- | --- |
| num_iterations     | =  1000  |     |     |
num_cols  =  50
num_rows  =  50
| agents_list  =    | []      |     |     |
| ----------------- | ------- | --- | --- |
| agents_positions  | =  {}   |     |     |
| num_coins  =  1   |         |     |     |
| #  Creating  the  | agents  |     |     |
#loop
for  id  in  range(num_agents):
| #  instantiating  | an  agent  |            |             |
| ----------------- | ---------- | ---------- | ----------- |
| a  =  agent(id,   | num_cols,  | num_rows,  | num_coins)  |
| #  set  initial   | position   |            |             |
x,  y  =  a.set_start_position(agents_positions)
| # insert the         | positions | in the list |     |
| -------------------- | --------- | ----------- | --- |
| agents_positions[id] |           | = [x, y]    |     |
| # append the         | new agent | to the list |     |
agents_list.append(a)
Listing 6.1  Creating the agents in Python, and adding them to the agents_list list
The  list  agents_list  will  contains  a  list  of  all  the  agents  created  and  used  in  the
simulation.
A list is basically a group of values attributed to one variable, like for instance a
list  of  the  names  of  the  students  in  a  class  like  names=[‘John’,  ‘Michael’,  ‘Mary’,
‘Jennifer’]. If we want to get the second name of the list we use names[1]. We use
[1]  because  the  first  element  in  a  list  has  an  index  of  0,  the  second  1  and  so  on.  If
we want to get the name Jennifer we use names[3]. A list can contain anything like
other list, integers, dictionaries and all of this can exist at the same time in a list.
The  dictionary  agents_positions  will  contain  several  lists  and  each  list  contains
the x and y position of each agent.
A  dictionary,  in  Python,  is  a  container  that  stores  values  referenced  by  keys
like, for instance, grades=‘name’: ‘John’, ‘biology’: 13, ‘english’: 15 where name,
biology and english are keys and John, 13 and 15 are values. If we want to get the
name  of  the  student,  we  use  the  code  grades[‘name’]  or  if  we  want  the  grade  in
biology we use grades[‘biology’] and it will return the name John and 13.
The  dictionary  is  enclosed  in  brackets.  After  each  key,  you  will  find  a  colon.
Also, each pair of keys and values is separated by a comma. The value for a key can
be another dictionary, a list or any other type of value.
Example of the contents in the agents_positions dictionary:
{0: [46,43], 1: [24,35], 2: [14,31], ...}
The numbers 0, 1, and 2 are the numbers of the agents and the values in square
brackets, which are lists, are the x and y positions in the two-dimension grid.
Next, we create the agents and position them randomly within the two-dimension
grid.

134 J.MargaridoandP.Campos
Now, all we have to do is iterate through all of the agents the number of times
defined in the variable num_iterations.
# Iterate
for n in range(num_iterations): # loop for the iterations
for z in range(num_agents): # loop for the number of
C→ agents
x, y = agents_list[z].raw_move(agents_positions) # move
C→ the agent
neighbour1 = give_or_take_coin(x, y, z)
if(neighbour1 >= 0):
coin = agents_list[neighbour1].take_coin ();
if(coin > 0):
agents_list[z].give_coin()
print("Getting coin from agent n.: " + str(neighbour1
C→ ))
Listing 6.2 Iterating through the agents
This small piece of code is a little bit more complex than the instantiation of the
agents and their positioning in the grid.
We have to iterate twice: one for the number of iterations and another for the
number of agents.
This means that we want to move each agent looping through them (for z in
range(num_agents)) the number of times defined in the variable num_iterations (for
n in range(num_iterations)) so the total number of movements is num_agents x
num_iterations.
To make sure that every agent has the same opportunity to move, agents are
moved in a linear way, meaning they move from agent number 0 to agent number
num_agents-1.
The agent’s method raw_move is called, allowing the agent to choose its next
move by selecting new x and y coordinates, ensuring that the selected position is
not already occupied by another agent.
After the agent moves, the stage is going to check if the agent is entitled to get a
reward. This means that if the agent has just moved to a cell next to an occupied one
it has to receive a coin from the occupier of that cell. This is done with the function
give_or_take_coin which ensures that the rule is fulfilled.
The method take_coin has the code that actually gets the coin to give it to the
recently arrived agent. If the agent who has to give the coin does not own any, the
transaction stops here, otherwise he will be decreased a coin and the arriving agent
will be added a coin to his wealth.
There are two functions in the start of the simulation, neighbour and
give_or_take_coin.
As this functions do not belong to a class they don’t have the parameter self as
in the methods that belong to a class. However, they are defined with the keyword
def, too.
The function neighbour has the task of checking whether the agent has moved to
a cell next to an occupied one.

6 MyWealth:ASimpleModelofEconomicExchangeinPython 135
The function give_or_take_coin checks if there will be any transfer of coins and
it  will  only  happen  when  the  agent  has  coins  to  give.  If  he  doesn’t,  the  simulation
will move on.
If the agent has a coin to give, the method give_coin will be called to increase the
wealth of the agent who receives the coin; otherwise, this method won’t be called.
| def  neighbour(x1,  | y1,  x,  y):  |     |
| ------------------- | ------------- | --- |
if(x1  ==  x):
| if(y1  ==         | (y-1)  or  y1  ==     | (y+1)):              |
| ----------------- | --------------------- | -------------------- |
| return            | True                  |                      |
| if(x1  ==  (x+1)  | or  x1  ==  (x-1)):   |                      |
| if(y1  ==         | y  or  y1  ==  (y-1)  | or  y1  ==  (y+1)):  |
| return            | True                  |                      |
return  False
| def  give_or_take_coin(x,  | y,  index):  |     |
| -------------------------- | ------------ | --- |
for  z  in  range(num_agents):
| if (z != | index):                           |       |
| -------- | --------------------------------- | ----- |
| x1,      | y1 = agents_list[z].getPosition() |       |
| n =      | neighbour(x1, y1,                 | x, y) |
| if(n     | == True):                         |       |
return z
return -1
Listing 6.3  The functions neighbour() and give_or_take_coin()
| 6.3.1  The Function  | neighbour()  |     |
| -------------------- | ------------ | --- |
This function receives the values for the x and y position of two agents and check if
they are in contiguous positions.
| 6.3.2  The Function  | give_or_take_coin()  |     |
| -------------------- | -------------------- | --- |
This  function  receives  the  position  of  an  agent  in  the  grid  and  its  index  in  the
list  of  agents,  then  it  iterates  through  all  the  agents  in  the  list  and  compares  their
position with the position of the received agent’s position. If an agent is in a position
contiguous  to  the  received  agent’s  position,  the  function  returns  the  index  of  that
agent so that a coin can be claimed, otherwise the function will return-1 meaning
that all the cells (positions) around the agent are empty.
Now, we will see what is happening in the agent class throughout this process.

| 136                 |       |     |     | J.MargaridoandP.Campos |
| ------------------- | ----- | --- | --- | ---------------------- |
| 6.4  The  agent.py  | File  |     |     |                        |
The library random is imported so that we can generate a random movement of the
agent and define the class agent. A class is a way of grouping data and functionality
under the class agent. To use a class we have to instantiate it which means that we
must reserve space in memory for the code and that instantiation must be attributed
to a variable. Let us suppose we have a class with the name pupil. To instantiate it
we can write some code like this: p=pupil(). The variable p, now, has an instance of
the  class  pupil  and  we  say  that  p  is  an  object.  This  way  we  can  say  that  an  object
is an instantiation of a class and we can instantiate a class the number of times we
want, for instance:
p1=pupil()
p2=pupil()
p3=pupil()
p4=pupil()
p5=pupil()
Now  we  have  5  instances  of  the  class  pupil  and  they  are  all  independent  from
each other and each one has its own piece of memory to live in.
import  random
class  agent:
| Listing 6.4  The class agent  |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- |
In the initializer of the class a few values are passed:
•  num—the id of the agent
•  num_cols—number of columns in the grid
•  num_rows—number of rows in the grid
•  coins—number of initial coins
The  initializer  of  a  class  is  used  to  initialize  some  variables  and  is  called  when
the class is instantiated, in this case the class is instantiated with the code:
| a  =  agent(id,                                | num_cols,  | num_rows  | , coins) |     |
| ---------------------------------------------- | ---------- | --------- | -------- | --- |
| Listing 6.5  Instantiation of the class agent  |            |           |          |     |
We can instantiate a class as many times as we want.
When a class is instantiated the method __init__ is called. Note the name of the
method __init__ (with two underscores before and after the word init) and the word
self  as the first argument of the method.
| def  __init__(self,                                   | num,         | num_cols,  | num_rows,  | coins):  |
| ----------------------------------------------------- | ------------ | ---------- | ---------- | -------- |
| self.num                                              | =  num       |            |            |          |
| self.num_cols                                         | =  num_cols  |            |            |          |
| self.num_rows                                         | = num_rows   |            |            |          |
| self.num_of_coins                                     |              | = coins    |            |          |
| Listing 6.6  The __init__() method of the class agent |              |            |            |          |

6 MyWealth:ASimpleModelofEconomicExchangeinPython 137
The prefix self before the name of a variable makes that variable known to every
method in the class.
The method set_start_position sets the position of the agent when the simulations
start.
The coordinates of the position are created randomly considering the number of
columns and rows in the grid.
Note that the randomly generated position of the agent must be validated before
it is considered effective to avoid having more than one agent in the same cell of
the grid. This is done by testing each generated position against a dictionary with
the id of every agent and its x and y coordinates. If the generated position is already
occupied, new coordinates will be generated until a vacant cell is found. That is
what the following code does.
while self.validate_position(self.x, self.y, agents_positions) ==
C→ False:
self.x = random.randint(0, self.num_cols)
self.y = random.randint(0, self.num_rows)
Listing 6.7 The loop while to validate the position of the agent in the grid
Finally, the method returns the coordinates for this agent.
def validate_position(self, col, row, positions):
for k, v in positions.items():
x = v[0]
y = v[ 1]
if(x == col and y == row):
return False
return True
Listing 6.8 The method validate_position()
The method validate_position() checks if, given the x and y coordinates of a
agent, there is any agent with the same values for the x and y coordinates.
def set_start_position(self, agents_positions):
self.x = random.randint(0, self.num_cols) # random x
C→ position
self.y = random.randint(0, self.num_rows) # random y
C→ position
while self.validate_position(self.x, self.y, agents_positions
C→ ) == False:
self.x = random.randint(0 , self.num_cols)
self.y = random.randint(0, self.num_rows)
return self.x, self.y
Listing 6.9 The method set_start_position() to define a position for the agent
The method set_start_position() generates two random values to position the
agent in the grid, one value for the x and one value for the y. This is done only
once, when the simulation starts.

138 J.MargaridoandP.Campos
Table 6.1 Table of
movement
def raw_move(self, agents_positions):
move = random.randint(0, 7)
x, y = self.get_new_position(move)
while self.validate_position(x, y, agents_positions)
== False:
move = random.randint(0, 7);
x, y = self.get_new_position(move)
self.x = x
self.y = y
return self.x, self.y
Listing 6.10 The method raw_move()
The method raw_move() finds a new position to move the agent.
It generates a random number between 0 and 7 and the agent is moved to the cell
according to Table 6.1:
According to the random number generated, the agent moves to the correspond-
ing cell.
If the number is 0 the agent move up one cell, if the number is 1, the agent moves
up and to the right, if the number is 5, the agent moves down and to the left.
For every possible movement the method validate_position() is called to verify
if the position is empty. This method returns the coordinates (x, y) of an empty cell
when found to update the list of agents’ positions and updates the position of the
agent calling this method.
The method get_new_position() is straightforward; based on a randomly gener-
ated number, it increases or decreases either the x coordinate, the y coordinate, or
both, as shown in the code below.
def get_new_position(self, move):
x = self.x
y = self.y
if(move == 0):

6 MyWealth:ASimpleModelofEconomicExchangeinPython 139
y += 1
elif(move == 1):
x += 1
y += 1
elif(move == 2):
x += 1
elif(move == 3):
x += 1
y -= 1
elif(move == 4):
y -= 1
elif(move == 5):
x -= 1
y -= 1
elif(move == 6):
x -= 1
elif(move == 7):
x -= 1
y += 1
if(x < 0):
x = self.num_cols-1
if(x > self.num_cols - 1):
x = 0
if(y < 0):
y = self.num_rows - 1
if(y > self.num_rows - 1):
y = 0
return x, y
Listing 6.11 The method get_new_position()
The method emphget_new_position() is straightforward; based on a randomly
generated number, it increases or decreases either the x coordinate, the y coordinate,
or both, as shown in the code below.
def take_coin(self):
# give a coin
if(self.num_of_coins > 0):
self.num_of_coins -= 1
return 1
else:
return 0
Listing 6.12 The method take_coin()
The method give_coin() increase the number of coins the agent has.
def give_coin(self):
# accept a coin
self .num_of_coins += 1
Listing 6.13 The method give_coin()

| 140 |     |     | J.MargaridoandP.Campos |
| --- | --- | --- | ---------------------- |
Fig. 6.2  Results of the simulation
Finally, the methods get_position() and get_num_coins() just return the position
of the agent in the grid and the number of coins the agent has, respectively.
def  get_position(self):
| return  self.x,  | self.y  |     |     |
| ---------------- | ------- | --- | --- |
def  get_num_coins(self ):
| return self.num_of_coins                                      |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- |
| Listing 6.14  The methods get_position() and get_num_coins()  |     |     |     |
The simulation is complete; we now need to extract and analyze the results.
In  Fig.  6.2  we  can  see  how  many  coins  each  agent  ends  up  with;  for  instance
agent 5 ended with 1 coin, agent no 11 ended with 3, agent 2 ended with 2 coins and
¯
so on.
| x_axis  =  list(range(1,  | len(agents_list)+1))  |     |     |
| ------------------------- | --------------------- | --- | --- |
| wealth_list  =            | []                    |     |     |
for  n  in  range(len(agents_list)):
| print("Agent  | "  +  str(n)  | +  ":  "  +  str(agents_list[n]. |     |
| ------------- | ------------- | -------------------------------- | --- |
C→
| get_num_coins())  |     | +   |     |
| ----------------- | --- | --- | --- |
"  coins")
wealth_list.append(agents_list[n].get_num_coins())
| plt.ylabel("Number | of coins") | # the y-axis | label |
| ------------------ | ---------- | ------------ | ----- |

6 MyWealth:ASimpleModelofEconomicExchangeinPython 141
| plt.xlabel("Agents") |     | #  the  x-axis  | label  |
| -------------------- | --- | --------------- | ------ |
plt.title("Number  of  coins  per  agent" #  the  title  of  the
C→  graphic
)
| #  creating  the  | graphic       |               |          |
| ----------------- | ------------- | ------------- | -------- |
| plt.bar(x_axis,   | wealth_list , | label="Agents | wealth") |
| # showing the     | graphic       |               |          |
plt.show()
| Listing 6.15  The graphic code  |     |     |     |
| ------------------------------- | --- | --- | --- |
This code is in the main.py file.
For  a  graphical  representation,  first  a  x_axis  list  is  created  which  contains  the
numbers  of  the  agents’  list,  then  a  wealth_list  list  containing  the  number  of  coins
each agent has.
The  plt  variable  is  an  instance  of  the  matplotlib  package  which  is  included  in
beginning of the class code.
Then we define the x-axis and y-axis legends and the title of the graphic.
Finally we create the graphic and show it.
| import  matplotlib.pyplot  | as  | p lt |     |
| -------------------------- | --- | ---- | --- |
Listing 6.16  Importing the matplotlib package and giving it the name plt
A version of this simulation with a graphic interface can be seen in the Youtube
in the address https://www.youtube.com/watch?v=oovLgT2oId4 (Fig. 6.3).
Fig. 6.3  The coin simulation
with a graphic interface

142 J.MargaridoandP.Campos
In  this  simulation  communication  is  the  basis  for  interactions  and  social  orga-
nization; it is expressed as a form of interaction in which the dynamic relationship
between agents is expressed through the intermediary of mediators or signals, which
once interpreted, will affect the other agents. One important features of the Agents
is Behaviour, that characterizes all the properties that the agent manifests itself in its
environment. Belew and Mitchell [7] describe behaviour, as something that “closes
the loop” between an organism and its environment.
According  to  Hamil  and  Gilbert  [8],  agents  shall  contain  the  following  charac-
teristics:
•  Perception (agents can see other agents in their neighbourhood and their environ-
ment);
•  Performance (agents can act, such as moving and communicating);
•  Memory (agents can recall their past states and actions);
•  Policy: agents can have rules that determine what they do next.
6.5  MESA
Mesa is an Apache2 licensed agent-based modeling (or ABM) framework in Python
(https://mesa.readthedocs.io/en/stable/).  Just  out  of  curiosity  we  will  show  a  very
simple demonstration of an Agent-Based Model using Mesa to simulate a version of
MyWealth, where 10 agents start with a random wealth between 0 and 10 monetary
units. Every time an agent plays, a second agent is chosen randomly and a monetary
unit  is  removed  from  it  and  given  to  the  agent  playing.  The  code  is  available  in
Listing 6.17:
| from  MoneyAgent  |                 | import    | MoneyModel  |
| ----------------- | --------------- | --------- | ----------- |
| #  Create         | model           | with  10  | agents      |
| model  =          | MoneyModel(10)  |           |             |
| #  Run  model     | for             | 5  steps  |             |
| for  i  in        | range(5):       |           |             |
model.step()
| #  Print         | final                              | total  wealth  | of  al l agents                 |
| ---------------- | ---------------------------------- | -------------- | ------------------------------- |
| final_wealth     |                                    | = sum(a.wealth | for a in model.schedule.agents) |
| print(f"Final    |                                    | total wealth:  | {final_wealth}")                |
| Listing 6.17     | The entry point of the simulation  |                |                                 |
| from  mesa       | import                             | Agent,         | Model                           |
| from  mesa.time  |                                    | import         | RandomActivation                |
import  random
class  MoneyAgent(Agent):
| """An | agent | with | fixed initial wealth.""" |
| ----- | ----- | ---- | ------------------------ |

6 MyWealth:ASimpleModelofEconomicExchangeinPython 143
| def  __init__(self,          |     | unique_id,         |     | model,  | initial_wealth):  |     |
| ---------------------------- | --- | ------------------ | --- | ------- | ----------------- | --- |
| super().__init__(unique_id,  |     |                    |     | model)  |                   |     |
| self.wealth                  |     | =  initial_wealth  |     |         |                   |     |
def  step(self):
| if  | self.wealth  | ==  0:  |     |     |     |     |
| --- | ------------ | ------- | --- | --- | --- | --- |
return
| other_agent         |     | =  random.choice(self.model.schedule.agents)  |        |     |     |     |
| ------------------- | --- | --------------------------------------------- | ------ | --- | --- | --- |
| other_agent.wealth  |     |                                               | +=  1  |     |     |     |
| self.wealth         |     | -=  1                                         |        |     |     |     |
def  __str__(self):
| return  | f"Agent  | {self.unique_id}  |     |     | wealth:  {self.wealth}"  |     |
| ------- | -------- | ----------------- | --- | --- | ------------------------ | --- |
class  MoneyModel(Model):
| """A                 | model  with          | some  number               |         | of  agents."""     |         |       |
| -------------------- | -------------------- | -------------------------- | ------- | ------------------ | ------- | ----- |
| def  __init__(self,  |                      | N):                        |         |                    |         |       |
| self.num_agents      |                      | =  N                       |         |                    |         |       |
| self.schedule        |                      | =  RandomActivation(self)  |         |                    |         |       |
| #                    | Create               | agents  with               | random  | initial            | wealth  |       |
| for                  | i  in                | range(self.num_agents):    |         |                    |         |       |
|                      | a  =  MoneyAgent(i,  |                            | self,   | random.randint(0,  |         | 10))  |
self.schedule.add(a)
def  step(self):
self .schedule.step()
| #            | Output     | agent wealth             | at   | each                     | step         |          |
| ------------ | ---------- | ------------------------ | ---- | ------------------------ | ------------ | -------- |
| print(f"Step |            | {self.schedule.steps}:   |      |                          | Total wealth | = {sum(a |
|              | C→ .wealth | for                      | a in | self.schedule.agents)}") |              |          |
| for          | agent      | in self.schedule.agents: |      |                          |              |          |
print(agent)
print()
Listing 6.18  Classes MoneyAgent and MoneyModel
| Step  1:  Total    | wealth  | =  45  |     |     |     |     |
| ------------------ | ------- | ------ | --- | --- | --- | --- |
| Agent  0  wealth:  | 8       |        |     |     |     |     |
| Agent  1  wealth:  | 4       |        |     |     |     |     |
| Agent  2  wealth:  | 4       |        |     |     |     |     |
| Agent  3  wealth:  | 7       |        |     |     |     |     |
| Agent  4  wealth:  | 1       |        |     |     |     |     |
| Agent  5  wealth:  | 6       |        |     |     |     |     |
| Agent  6  wealth:  | 5       |        |     |     |     |     |
| Agent  7  wealth:  | 0       |        |     |     |     |     |
| Agent  8  wealth:  | 6       |        |     |     |     |     |
| Agent 9 wealth:    | 4       |        |     |     |     |     |
| Step 2: Total      | wealth  | = 45   |     |     |     |     |
| Agent 0 wealth:    | 7       |        |     |     |     |     |
| Agent 1 wealth:    | 5       |        |     |     |     |     |
| Agent 2 wealth:    | 3       |        |     |     |     |     |
| Agent 3 wealth:    | 7       |        |     |     |     |     |
| Agent 4 wealth:    | 0       |        |     |     |     |     |

144 J.MargaridoandP.Campos
Agent 5 wealth: 5
Agent 6 wealth: 5
Agent 7 wealth: 1
Agent 8 wealth: 6
Agent 9 wealth: 6
Step 3: Total wealth = 45
Agent 0 wealth: 6
Agent 1 wealth: 6
Agent 2 wealth: 4
Agent 3 wealth: 6
Agent 4 wealth: 2
Agent 5 wealth: 5
Agent 6 wealth: 5
Agent 7 wealth: 1
Agent 8 wealth: 5
Agent 9 wealth: 5
Step 4: Total wealth = 45
Agent 0 wealth: 6
Agent 1 wealth: 6
Agent 2 wealth: 5
Agent 3 wealth: 7
Agent 4 wealth: 1
Agent 5 wealth: 4
Agent 6 wealth: 6
Agent 7 wealth: 0
Agent 8 wealth: 6
Agent 9 wealth: 4
Step 5: Total wealth = 45
Agent 0 wealth: 6
Agent 1 wealth: 6
Agent 2 wealth: 4
Agent 3 wealth: 7
Agent 4 wealth: 1
Agent 5 wealth: 4
Agent 6 wealth: 6
Agent 7 wealth: 0
Agent 8 wealth: 7
Agent 9 wealth: 4
Final total wealth: 45
Listing 6.19 Possible set of results after running the simulation
6.6 Final Considerations
MyWealth is an economic simulation model featuring agents interacting in a
marketplace within a two-dimensional grid environment. The agents move and

6 MyWealth:ASimpleModelofEconomicExchangeinPython 145
interact, and relationships are defined as consumer-producer interactions. Agent
actions influence system behavior, with specific rules dictating their movements and
transactions. Agents move randomly, receiving a coin from an adjacent agent upon
occupying an occupied cell. The simulation involves linear agent turns, iterating
over all agents’ movements. The outcome, the final wealth of each agent, is
recorded. However, challenges include grid size impact on transactions, ensuring
initial agent positions are unoccupied, and managing agent movements within the
grid’s constraints. The simulation operates solely in memory, emphasizing the final
wealth distribution as the primary output. Future developments include adjusting
grid size to balance agent proximity and avoiding excessive transactions or limited
interactions. Initial agent positioning must prevent overlap, and agent movements
adhere to a von Neumann neighborhood, allowing movement in eight directions.
MyWealth serves as a valuable tool for teaching how to simulate economic
exchange dynamics and studying wealth distribution patterns in agent-based mod-
els. This is a prototype that can be used pedagogically as a first agent-based model
developed in Python, in which agents interact with very simple rules and new
patterns can emerge. In the next chapters we will add more complexity, through
a new game with the possibility of learning and the introduction of crises.
References
1. F. Neves, P. Campos, S. Silva, Innovation and employment: An agent-based approach. J. Artif.
Soc. Soc. Simul. 22(1), 8 (2019). https://doi.org/10.18564/jasss.3933. http://jasss.soc.surrey.ac.
uk/22/1/8.html
2. C. Deissenberg, S. van der Hoog, H. Dawid, Eurace: A massively parallel agent-based model of
the european economy. Appl. Math. Comput. 204, 541–552 (2008)
3. Axelrod, R. (1997), The Complexity of Cooperation, Princeton, Princeton University Press
4. T.C. Schelling, Dynamic models of segregation. J. Math. Sociol. 1(2), 143–186 (1971)
5. U. Wilensky, W. Rand, Introduction to Agent-Based Modeling: Modeling Natural, Social and
Engineered Complex Systems with NetLogo (MIT Press, Cambridge, MA, 2015)
6. A. Dragulescu, V. Yakovenko, Statistical mechanics of money. European Physical Journal B
17, 723–729 (2000)
7. R.K. Belew, M. Mitchell, Adaptive Individuals in Evolving Populations (Addison-Wesley,
Reading, MA, 1996)
8. L. Hamill, N. Gilbert, Agent-Based Modelling in Economics (Wiley, Hoboken, NJ, 2015)

Chapter 7
The Ultimatum Game as a Paradigm for
Learning Agents: A Python Adventure
Joaquim Margarido and Pedro Campos
7.1 Introduction
Agent-Based Models (ABM) consist of various components, encompassing active
agents (typically), objects (comprising elements other than agents), relationships
(facilitating interactions between agents and objects, promoting communication
within the model’s elements), and the environment (the overarching framework
embedding both agents and objects).
Game Theory is considered an important and valuable tool in Agent-Based
Models, as they can help to understand and study the interactions among self-
interested agents in the real world [1].
This chapter uses the ABM paradigm for economic crisis and pandemics, with
a machine learning approach to help in the description and prediction tasks. This
is done in a pedagogical way and following a methodology that allows students
and teachers to follow the various steps for creating Python code (program codes
are available in: https://ml4agents.free.nf). Indeed, a growing number of leading
economists identify the limitations of the dominant economic theory as a significant
aspect of the economic crisis [2]. In this game, a crisis will be simply introduced in
the model.
In this part of the book, we will be using the Ultimatum game as a paradigm for
learning agents. In the Ultimatum game there are two different agents, the proposer
and the responder, that communicate by announcing their decisions. The rules for
this game are very simple: the proposer is forced to choose how to split a certain
J. Margarido (@)
ISEP, Porto, Portugal
P. Campos
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 147
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_7

148 J.MargaridoandP.Campos
amount with another agent, the responder. The responder must choose between
accepting or refusing the offered amount. If the responder accepts, both win the
amounts corresponding to the proposer’s offer. Otherwise, neither player wins any
reward. Both players know in advance the consequences of the responder accepting
or rejecting the offer. The game has simple rules that we will implement in Python,
step by step. We will implement our own version of the game to illustrate how a very
simple game can be created from scratch, using an Agent-Based Model paradigm.
The implementation is made in different steps: first, we will run a baseline model,
where the proposer may repeatedly use one of two different strategies: offering a fair
split (50% or more), or else, offering an unfair split (less than 50%). In this initial
experiment there is no memory for both agents, i.e., the agents make their decisions
regardless of the opponent’s last move (see also [3]).
In a further step, we will apply two learning strategies: Fictitious Play, where
agents minimize the possibility of rejection from the responders; and Reinforcement
learning, a method of machine learning where agents learn an optimal action
policy in a sequential decision process, through repeated experience. Reinforcement
learning problems involve learning what to do—how to map situations to actions—
so as to maximize a numerical reward signal [4]. The chapter is organized as follows:
in Sect. 7.2. we define the Baseline Model; then, in Sect. 7.3. agents use Fictitious
Play; in Sects. 7.4 and 7.5 crisis and Reinforcement Learning, respectively, are
introduced. In Sect. 7.6 we present our final considerations.
7.2 Ultimatum Game: The Baseline Model
The Ultimatum Game has become a popular instrument of economic experiments,
as it contains simple rules that may describe very complex behaviours of the agents.
As an example, imagine you are the proposer and you own a certain amount of
money, let us say 1000 monetary units. To keep the money, you only have to offer
a percentage of that amount to another person (the responder), and that person must
accept it. Let us say you offer 300 monetary units out of 1000 to someone. If that
person agrees, you get 700 from the 1000; if that person disagrees, both of you
get nothing. This is a non-negotiable game, what means that the responder cannot
negotiate the value proposed, by saying something like: “I don’t accept 300, but I’ll
accept 500”. The responder is only allowed to say “yes” or “no” to the deal.
One of the first descriptions of the Ultimatum Game was made in 1961 by the
Hungarian Nobel Prize laureate economist, John Harsanyi. Ultimatum games are
bargaining games where one of the players can firmly commit himself in advance
under a heavy penalty that he will insist under all conditions upon a certain specified
demand, that is called his ultimatum [5, 6].
Consequently, it will be rational for the first player to commit himself to his
maximum demand, i.e., to the most extreme admissible demand he can make.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 149
As stated by Rand et al. [7], in a one-shot Ultimatum Game, a rational self-
interested proposer will offer the minimum amount that is believed to be acceptable
by the responder. On the other hand, a rational self-interested responder will accept
any nonzero offer. Therefore, under common knowledge of the rationality of both
players, we can say that the subgame perfect Nash equilibrium is for the proposer
to make the minimum possible offer, and for the responder to accept it. A Nash
equilibrium is a pair of strategies (one for the proposer and one for the responder),
where neither party can improve their reward by changing strategy.
In Game Theory, the Ultimatum Game is classified as a dynamic perfect
information game as each player, when making any decision, is perfectly informed
of all the events that have previously occurred [8].
In the first experiments of the game [9] observed that players often deviated
from this “rational” solution, preferring “fair” solutions (an even or approximately
even split) [10]. Over the years, the interest in the Ultimatum Game came from
this contrast between the theoretical solution and the way that the game is actually
played by people.
We will run the game in different ways, and with different setups. In the first
setup, agents will not be able to learn. This is the baseline model, where the proposer
may use two different strategies: offering a fair split (50% or more), or else offering
an unfair split (less than 50%). The responder, on his turn, can assume the following
strategies:
. Always accept: the responder accepts every offer
. Always reject: the responder rejects every offer
. Accept only fair splits (equal or higher than 50%)
. Accept only unfair splits (smaller than 50%)
. Accept or reject randomly
In Table 7.1, we summarize the results of our simulations with the mean absolute
values of each player’s payoffs, and mean percentages of the total split amount.
The results show that the strategy of the responder with the lowest payoff is the
strategy “Always Reject”, either if the proposer makes unfair or fair offers. This is
reminiscent of the Subgame Perfect Equilibrium, as there is a clear incentive for the
responder to play any strategy other than “Always rejecting”.
The next best strategy for the responder is to play at random, for which there is
not much to comment. A better strategy yet, depends on the proposer’s strategy: if it
only makes unfair offers, the responder is better off by accepting unfair offers; if it
only makes fair offers, the responder is better off by accepting only fair offers. This
leads us to the absolute best way that the responder can play: by accepting every
offer, no matter if it is fair or not. For the proposer, the best way to play always
depends on the reaction of the responder. If the responder only accepts fair offers,
the best strategy is to only make fair offers.
On the other hand, if the responder only accepts unfair offers, the opposite
strategy is the best one. Even if the responder plays fully randomly, in the long term,
both “accept” and “reject” should be played with equal frequencies. In this situation,
it is better for the proposer to only make unfair offers, as to maximize the payoff in

150 J.MargaridoandP.Campos
stluser
fo
elbaT
1
.7e
lbaT

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 151
those turns in which the responder does accept. Finally, if the responder always
accepts, then the proposer does best by only offering unfair splits. It is also clear
that the highest sum of the payoffs of both players is achieved when both cooperate:
when the responder requires fair offers, and the proposer offers fair offers; or when
the responder requires unfair offers, and the proposer reciprocates. The outcome of
these two preferences of the responder, however, only differ in the final distribution
of the payoffs between players—and not on the total payoff.
An implementation of this version has been made in R by Pinto et al. [11] and
can be consulted by request to the authors of this Chapter.1
7.3 Fictitious Play
There are different ways of learning in games. As seen in Chap.2, Fictitious play
is one of the easiest ways, as each player presumes that the opponents are playing
stationary (possibly mixed) strategies. At each round, each player thus best responds
to the empirical frequency of play of their opponent [12]. This method is reasonable
to follow when the opponent uses a stationary strategy, while it is inconsistent if the
opponent’s strategy is non-stationary.
In this section, we will introduce a version of Fictitious play as a strategy that
helps agents to learn with the aim of minimizing the possibility of rejection from the
responders. We will consider that the proposer will learn the best way to guarantee
a deal with a positive outcome. The idea is that the proposer uses information of
previous results to score the best option. Of course, when the game starts there are
no previous results, so the proposer must decide how much to offer without having
a background knowledge about his opponent.
In this version of the game, a threshold is created as a percentage representing
the maximum value the proposer is in the disposition to offer to the responder. So,
if the proposer owns, let us say, 1000 monetary units and the threshold is defined
as, let us say 20%, then the agent is going to offer to the responder 200 monetary
units. The threshold is given to the agent in a random way when it is instantiated
(see Fig.7.3 for a definition of Class instantiation). This is one of the parameters
that can be changed to make the proposers offer more or less money.
Moreover, the minimum percentage value that the respondent is in the disposition
to accept from the responder is also defined.
1 This version includes Reinforcement Learning where players no longer play by fixed rules, but
instead learn from experience of playing with each other repeated rounds.

152 J.MargaridoandP.Campos
Fig. 7.1 The program flow
7.3.1 Python Implementation
Fictitious Play is implemented in two different and sequential phases. Firstly, we
are going to train the proposers in making deals. Then, in the second phase, the data
collected from the training of the proposers will be used to provide the best positive
outcome deals. To implement the baseline version of the Ultimatum game, we will
follow the diagram of Fig.7.1.
The program in Python contains three parts.
. the main part (main.py) is the class that defines and instantiates the agents
. the class agent (agent.py) containing the code for the agents
. and a class used only to help execute the calculations with a point of expansibility
if needed, that is called by the agents (calculate.py).2
2 Classes provide a means of bundling data and functionality together. Creating a new class defines
a new type of object, allowing new instances of that type to be made. Each class instance can have
attributes attached to it to maintain its state. Class instances can also have methods (defined by its
class) for modifying its state. https://docs.python.org/3/tutorial/classes.html.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 153
The repeated (n-shot) version of the game illustrated in Fig.7.1 runs from a while
loop inside the “main” file. While the loop is active, the proposer is called to make
a proposal to the responder. The responder being called by proposer, analyses the
proposal and gives an answer to the proposer.
The proposer receives the answer from the responder and terminates its action
for that turn. The control of the program is again in the while loop in the main file.
If the loop has not ended yet, the proposer is called but if it has already ended,
the analyser is called to analyse the text file. When the analyser ends its work, the
program ends.
. The program starts by executing the code in the file main.py which is not a class
but calls the agents n times through the agent class method get_to_business().
. The agent class is both the proponent and the respondent depending on which
methods we call from the agent.
. The agent calls the method make_offer() in the Calculate class.
Both Agent and Calculate are Python classes. Object-oriented programming
(OOP) is based on Classes. The difference between a class and an object is that
an object is an instantiation of a class. In the next paragraphs we will explain the
code developed in Python, namely the definition of the agents that is contained in
the file main.py. It is important to note that Python uses packages for most important
features. So, we will need to import them in the top of our code. We are going to
use Pandas, Matplotlib and Random. We must also import the agent class.
import pandas as pd
import matplotlib.pyplot as pl t
import random
from agent import *
Listing 7.1 Initial code in main.py
In first three lines of Listing 7.1 the three packages are imported, and references
are created for the future: Pandas3 as pd, and pyplot from Matplotlib4 as plt.
The last line in the code of Listing 7.1 aims to import the class that defines the
agents (agent.py). After importing the packages, we call two functions: thresh-
old_proposer and threshold_responder. The function threshold_proposer defines the
maximum percentage the proposer will offer to the responder and the function
threshold_responder defines the minimum value that the responder is willing to
accept. The first function will return a random value between 0.1 and 1 and the
second will return a value between 0.1 and 0.8. These values have been decided by
the authors, based on reasonable assumptions and can be changed (Listing 7.2).
3 Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation
tool, built on top of the Python programming language. (https://pandas.pydata.org/.)
4 Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
in Python. Matplotlib makes easy things easy and hard things possible. (https://matplotlib.org/.)

154 J.MargaridoandP.Campos
Fig. 7.2 Getters and setters
def threshold_responder():
return round(random.uniform(0.1, 1), 1)
def threshold_proposer():
return round( random.uniform(0.1, 0.8), 1 )
Listing 7.2 The functions threshold_responder() and threshold_proposer()
It is time to instantiate the agents. The instances of the agents must be saved
somewhere in a list. The line in Listing 7.3 defines an empty list where the instances

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 155
Fig. 7.3 Class instantiation
of the agents (as many as we want) are going to be saved. This list is created in the
computer’s memory (Fig.7.3).
agent_list = [ ]
Listing 7.3 Definition of an empty list
We consider several players in this game. We start with 50 agents, from whom
25 are proposers and 25 are responders. The code to instantiate the agents, which
is in the file agent.py, is straightforward, as we can see in Listings 7.3 and 7.4.We
use a for loop to instantiate 25 agents. The for loop executes the program 25 times.
The variable n is used to generate the agents: If n is smaller than 10, the agent is
instantiated as a proposer. Otherwise, it is instantiated as a responder (Figs.7.2 and
7.3).
for n in range(0, 20):
if n < 10:
type_of_agent = 0 # proposer

| 156 |                  |                        |               | J.MargaridoandP.Campos |
| --- | ---------------- | ---------------------- | ------------- | ---------------------- |
|     | ag  =  agent(n,  | threshold_proposer(),  |               |                        |
|     | type_of_agent)   | #  order               | number,       |                        |
|     | base_theshold    | make  an               | offer,  type  | of  agent              |
|     | (proposer        | or  responder)         |               |                        |
else:
|     | type_of_agent    | =  1 #                  | responder   |                  |
| --- | ---------------- | ----------------------- | ----------- | ---------------- |
|     | ag  =  agent(n,  | threshold_responder(),  |             |                  |
|     | type_of_agent)   | #  order                | number,     |                  |
|     | base_theshold    | to  accept              | the  deal,  | type  of  agent  |
|     | (proposer        | or responder)           |             |                  |
agent_list.append(ag)
| Listing 7.4  | Creation of the agent list  |     |     |     |
| ------------ | --------------------------- | --- | --- | --- |
With every instance of the class agent, three values are passed through its method
__init__.
1st—the current value of the variable n and this way we give the agent a unique
id. 2nd—the threshold for that agent, that is, for the proposer the maximum value
he is willing to offer to the responder and for the responder a minimum value he is
willing to accept. 3rd—the type of agent we are instantiating. 0 for the proposer and
1 for the responder.
After each iteration, the instance of the agent is added to the list previously
created agent_list. The instance of the agent is nothing more than the position in
memory where the code for that instance is located. Let us see, on the side of the
agent class, how the class is instantiated (Fig. 7.4).
7.3.2  The Agent Class
When the class Agent  is instantiated three arguments are passed to the __init__
method.
| def  __init__(self,    |                                         | id,  base_threshold,  |     | type_of_agent):  |
| ---------------------- | --------------------------------------- | --------------------- | --- | ---------------- |
| self.id                | =  id                                   |                       |     |                  |
| self.base_threshold    |                                         | =  base_threshold     |     |                  |
| self.type_of_agent     |                                         | =  type_of_agent      |     |                  |
| self.total_earned      |                                         | =  0                  |     |                  |
| self .total_not_earned |                                         | = 0                   |     |                  |
| Listing 7.5            | The __init__ method in the agent class  |                       |     |                  |
The values passed to the class through the variables in its instantiation are
“converted” to class variables and you can see that in the code above.
Two more class variables are created in this process being self.total_earned  and
self.total_not_ earned. Every time a responder refuses a proposal, that value is added
to self.total_not_earned  and every time a proposal is accepted, that value is added
to self.total_earned. In the end, we can know how much every responder earned and
how much he didn’t earn because he refused the deal.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 157
Fig. 7.4  Classes in Python
The class Agent has some of what we call getters and setters (see Fig.7.4 for Get-
ters and Setters and Fig.7.4 for Classes in Python). The method get_to_business()
def  get_to_business(self,  file,  value,  responder,  dset,
stage):
calc  =  calculate()
| offer_value  | =  calc.calc_offer(dset,  | value,  |
| ------------ | ------------------------- | ------- |
self.base_threshold)
| result  =  | responder.make_offer(value,  | offer_value)  |
| ---------- | ---------------------------- | ------------- |
| if  result | == True:                     |               |

158 J.MargaridoandP.Campos
self.total_earned += offer_value
res = 1
else:
self.total_not_earned += offer_value
res = 0
file.writelines(f"{self.get_id()},{value},
{round(offer_value, 2)}, {res},{stage}\n")
return result
Listing 7.6 The method get_to_business()
The method get_to_business() is called to make preparations to make the offer to
the responder. All the offers are registered in a text file as a binary value, depending
on whether the outcome is positive or negative.
Four parameters are passed to the method:
. file—this is the file where the outcome of the negotiation is to be registered.
We pass the reference to the file, so that for every negotiation, its terms and the
outcome are registered in the same file. We call this file analysis_ml.csv. The
extension is csv because this is a comma separated values type of file,
. value—this is the base value to be used to make a proposal to the responder,
. responder—is the responder to whom the proposal is going to be made. This is
the address of an instance of the class agent,
. dset—this is the dataset with the values that originated a positive outcome in
previous negotiations.
. stage—1 if the transaction happens before the crisis and 2 if it happens after the
crisis.
Now is the time to calculate how much the proposer is going to offer the
responder and this is done by calculating a percentage of the base value. That
percentage comes from one of two possible places. It is either based on the threshold
created for that proposer, or it is based on previous experiences registered in the text
file. Let us suppose the proposer has 2000 monetary units, (let us say, dollars). How
much should he offer the responder to make him accept the deal? The proposers
and responders have a threshold. For the proposer, the threshold is the maximum
percentage he is willing to offer and for the responder, the threshold is the minimum
percentage he is willing to accept. Before trying to negotiate with the thresholds, the
proposer consults the file where all the previous negotiations are registered. This is
a sample of that file (Table 7.2).
Table 7.2 Structure of the
ID Value Proposed Result Value
analysis_ml.csv file
5 12749 6374.5 1 1
0 84973 67978.4 1 1
0 76551 61240.8 1 1
7 22152 2215.2 0 1
8 67978 6797.8 0 1

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 159
The first column (ID) is the ID of the proposer. This number is given to the agent
when it is created (instantiated).
The second column (Value) is the base value the proposer has to negotiate. The
third column (Proposed) is value proposed to the responder by the proposer. The
fourth column (Result), which has a value of 0 or 1 for false and true, is the outcome
of the negotiation.
The fifth column (Value) may have the value 1 or 2. 1 if the values refer to
transitions before the crisis and 2 if they are after the crisis. Every time there is
going to be a proposal, a dataset is created from this file with all the lines with a
value 1 in the fourth column.
Then, the proposer is going to search for a value that is around the base value
that he has to negotiate, in this case 2000 dollars.
Why around and not exactly? It is because you need to remember that the base
value is a random number so in this example there may not be a value of 2000 in the
text file, in this way we define a floor and a ceiling value.
Let us assume that the floor and the ceiling correspond to an interval of 10%
around the base value (i.e. an interval between 90% and 110% of the base value). We
would look for values between 1800 and 2200. This way, we increase the possibility
of finding the base value. Let us assume that the values are as in Table 7.3.
Which value are we going to propose? Should we pick the highest, the lowest,
the average of them all? That is up to the user. In this example we pick the highest
value and multiply it by 90%. So, we offer 90% of the highest value. Of course, we
can change this percentage at will. If no match is found, that is, no values between
1800 and 2200 exist in the file, the value proposed will be the base value (2000
in this example) multiplied by the threshold of the proposer, suppose it is 30%, so
we will offer 600 dollars to the responder. This calculation is made in the method
calc_offer created in the class Calculate.
7.3.3 The Calculate Class
This class has only one method—calc_offer. Let us analyse the code.
def calc_offer(self, ds, base_value, base_threshold):
floor = base_value * 0.9
ceiling = base_value * 1.1
if len(ds) > 0:
try :
values_floor = ds[ds[’Value’] >= floor]
except:
Table 7.3 Sample values for
the Ultimatum Game

| 160             |         |                                        | J.MargaridoandP.Campos |     |
| --------------- | ------- | -------------------------------------- | ---------------------- | --- |
|                 | return  | base_value  *  base_threshold          |                        |     |
| values_ceiling  |         | =  values_floor[values_floor[’Value’]  |                        | <=  |
C→  ceiling]
try:
|     | offer  =  | values_ceiling[’Proposed’].max()  | *  0.9  |     |
| --- | --------- | --------------------------------- | ------- | --- |
except :
|     | offer  =  | base_value  *  base_threshold  |     |     |
| --- | --------- | ------------------------------ | --- | --- |
else:
| return       | base_value                                          | * base_threshold |     |     |
| ------------ | --------------------------------------------------- | ---------------- | --- | --- |
| return       | offer                                               |                  |     |     |
| Listing 7.7  | Calculating if the offer should be accepted or not  |                  |     |     |
This method receives a dataset created with Pandas with all the lines registered
in the text file with positive negotiations, the base value and the threshold of the
proposer. First, we define the floor and the ceiling to determine the range of values
we want to filter from the text file. As mentioned earlier the floor is 90% of the base
value and the ceiling is 110% of the base value. Then, we have a range of 1800 to
2200 (remember the base value in our example is 2000).
| floor        | =  base_value        | *  0.9  |     |     |
| ------------ | -------------------- | ------- | --- | --- |
| ceiling      | =  base_value        | *  1 .1 |     |     |
| Listing 7.8  | Thebaseandtopvalues  |         |     |     |
If the dataset is not empty, we populate the variable values_floor with the values
in the dataset whose base value is equal or higher than the floor value calculated.
| values_floor  | =  ds[ds[’Value’]                             | > =  floor ] |     |     |
| ------------- | --------------------------------------------- | ------------ | --- | --- |
| Listing 7.9   | Filtering the list based in the floor values  |              |     |     |
If the values in the dataset cannot satisfy this condition because, for example,
there are no values equal or higher than the floor value, the method will return the
product of the base value with the threshold of the proposer. This code is in a try...
except block to prevent the code from stop running if there is any error filtering the
dataset.
try:
|     | values_floor  | =  ds[ds[’Value’]  | >=  floor]  |     |
| --- | ------------- | ------------------ | ----------- | --- |
except :
|               | return                                               | base_value  * base_threshold |     |     |
| ------------- | ---------------------------------------------------- | ---------------------------- | --- | --- |
| Listing 7.10  | Treating the exception if the values does not exist  |                              |     |     |
In case there are values in the dataset that are higher than the floor value, the
program advances to the next line of code:
| values_ceiling  | =  values_floor[values_floor[’Value’]  |     |     |     |
| --------------- | -------------------------------------- | --- | --- | --- |
< =  ceiling ]
| Listing 7.11  | Filtering the list based in the ceiling values  |     |     |     |
| ------------- | ----------------------------------------------- | --- | --- | --- |
The variable values_ceilling is populated with the values that are equal or smaller
than the ceiling value. Now, the method tries to calculate the maximum value in the

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 161
values_ceiling variable multiplied by 90% (in our code but of course this percentage
can be changed). Once again, this code is inside a try... catch block because if the
variable values_ceiling is empty, an exception will be raised and if this happens, the
catch block will calculate the value of the offer as the base value multiplied by the
base threshold. Here is the code:
try:
offer = values_ceiling[’Proposed’].max() * 0.9
except :
offer = base_value * base_threshold
Listing 7.12 Treating the exception if the values does not exist
Remember that all this code is inside an if statement that evaluates as true if
the dataset is not empty or null. If the dataset is empty or null, the product of the
base_value and the base_theshold is returned.
.
.
.
else:
return base_value * base_threshold
Listing 7.13 If the value filtered does not exist return the base_value multiplied by the
base_threshold
If everything fails, the value of the offer calculated in the block try... catch to
calculate the value of the offer from the dataset of values smaller than the ceiling, is
returned.
Now, let us return to the method get_to_business() in the agent class. After the
offer has been calculated, it is time to present it to the responder.
result = responder.make_offer(value, offer_value , stage )
Listing 7.14 Return the value from the method responder.make_offer()
This is made calling the above method. The value returned will be True or False.
If the value returned is True, the value 1 is saved in the text file and the offer value
is added to the variable self.total_earned (the self is because this is a class variable).
If the value returned is False, the value 0 is saved in the text file and the offer value
will be added to the variable self.total_not_earned (the self is because this is a class
variable). These two class variables let us know in the end of the simulation, how
much each agent has earned and how much they missed the opportunity to earn.
Here is the code:
if result == True:
self.total_earned += offer_value
res = 1
else :
self.total_not_earned += offer_value
res = 0
Listing 7.15 Adding the values earned or not earned for that agent

| 162 |     |     |     |     | J.MargaridoandP.Campos |
| --- | --- | --- | --- | --- | ---------------------- |
To finalize the method get_to_business(), the result of this transaction is saved in
the text file and the result is returned.
file.writelines(f"{self.get_id()},{value},{round(offer_value,  2)
C→  },
{res},{stage}\n" )
return  result
Listing 7.16  Saving the result of the transaction to the analysis_ml.csv file
The make_offer() method is the method in the Agent class that receives the offer
from the proposer. This is a very simple method. It receives the base value and the
offer value and returns True or False, whether it accepts the offer or not. If the offer
is below the base threshold it is refused, otherwise it is accepted. True or False is
returned to the calling method .
| def  make_offer(self,  |                        |           | value,  offer,            | stage):    |     |
| ---------------------- | ---------------------- | --------- | ------------------------- | ---------- | --- |
| #                      | if  offer              | is        | bellow  base              | threshold  |     |
| #                      | id  =                  | self.id   |                           |            |     |
| if                     | offer                  | /  value  | <  self .base_threshold:  |            |     |
|                        | self.total_not_earned  |           |                           | +=  offer  |     |
return  False
else:
|     | self .total_earned |     | += offer |     |     |
| --- | ------------------ | --- | -------- | --- | --- |
return True
| Listing 7.17  | The method make_offer()  |     |     |     |     |
| ------------- | ------------------------ | --- | --- | --- | --- |
The value received by this method with the name of stage is used to indicate if
this simulation is before or after the crisis. This method returns either False or True,
if the offer is accepted or not. If the offer is accepted, the value is added to the class
variable self.total_earned; if the value is not accepted the value is added to the class
variable self.total_not_accepted  (remember that the keyword self is used to make
the variable a class variable. Now, we can start the simulation. The variable counter
is created to hold the number of times we want the simulation to be executed:
| counter       | =                                 | 10000  |     |     |     |
| ------------- | --------------------------------- | ------ | --- | --- | --- |
| Listing 7.18  | Defining a value for the counter  |        |     |     |     |
We want the simulation to be executed 10,000 times. A while loop is used to
control the number of times the simulation is executed:
| while  | counter  | >  0:  |     |     |     |
| ------ | -------- | ------ | --- | --- | --- |
try:
data  =  pd.read_csv(’analysis_ml.csv’)
|     | data_true  |     | =  data[data[’Result’]  |     | ==  1]  |
| --- | ---------- | --- | ----------------------- | --- | ------- |
except:
data  =  []
|            | data_true  |                        | =  []  |         |     |
| ---------- | ---------- | ---------------------- | ------ | ------- | --- |
| proposer   |            | =  random.randint(0,   |        | 9)      |     |
| responder  |            | =  random.randint(10,  |        | 19)     |     |
| value      | =          | random.randint(1000,   |        | 100000) |     |

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 163
result = agent_list[proposer].get_to_business(file,
value, agent_list[responder], data_true,
counter, stage)
counter -= 1
Listing 7.19 The while loop to control the number of times the agents are called for the simulation
In terms of the procedure, first—we populate the variable data with all the values
in the text file analysis_ml.csv. Second—we filter the read data by its Result field
and load it into the variable data_true. If there is an error reading and filtering the
data from the text file, the exception is executed defining the variables data and
data_true as empty lists. Third—We find a proposer from all the proposers we
created. This is done by getting a random number. Fourth—We find a responder
to deal with. This is also done by getting a random number. Fifth—We get a value
to negotiate. This is done by getting a random number between 1000 and 100000.
And of course, that we can change this range of numbers if we want. Sixth and final
step—We call the method get_to_business and pass it the following values:
. the text file to write the result of the deal
. the base value to negotiate
. the responder to make the offer to
. the data_true variable with the results of the well-succeeded deals
. the stage (1 before the crisis; 2 after the crisis)
The last line of code:
counter -= 1
Listing 7.20 Subtracting 1 from the counter variable
Its purpose is to control the while loop. Remember that the loop will only execute
while the variable counter is higher than zero.
7.4 When the Crisis Happens
The crisis happens when the simulation is in the middle of the total iterations defined
in the variable counter, that is, in our example 5000, but this value can be changed.
The difference in the simulation after the crisis is whatever we want, but we define
it as being the responder raising the value that he is willing to accept by 50%. The
changes in the code are in the main.py file where a stage modifier was added. This
stage modifier only shows the while loop when to tell the agents that a crisis has
occurred. A stage variable was also added so that the agents may know that they are
in a crisis and act accordingly (the responders will raise their threshold by 50%).

| 164            |             |       | J.MargaridoandP.Campos |
| -------------- | ----------- | ----- | ---------------------- |
| stageModifier  | =  counter  | /  2  |                        |
stage  = 1
| Listing 7.21  The variable that controls the moment the crisis starts  |     |     |     |
| ---------------------------------------------------------------------- | --- | --- | --- |
This code is to be put before the beginning of the while loop.
| while  counter  | >  0:               |     |     |
| --------------- | ------------------- | --- | --- |
| #  Change       | the  stage          |     |     |
| if  counter     | <=  stageModifier:  |     |     |
stage  = 2
| Listing 7.22  State changer  |     |     |     |
| ---------------------------- | --- | --- | --- |
The variable stage is added to the function get_to_business() in the while loop.
| result  =  agent_list[proposer].get_to_business(file,  |     |              |           |
| ------------------------------------------------------ | --- | ------------ | --------- |
| value,  agent_list[responder],                         |     | data_true ,  | counter,  |
stage )
Listing 7.23  Executing the method get_to_business from the agent list
This function is used by the proposer, but he uses it only to pass it to the responder
and to save it in the text file, where the interaction is registered.
file.writelines(f"{self.get_id()},{value},{round(offer_value,  2)
C→  },
{res},{stage}\ n")
Listing 7.24  Saving the result of the transaction to the analysis_ml.csv file
In the responder code, the value in the variable stage is used in the following
way:
| if  stage  ==                                          | 2:  |          |     |
| ------------------------------------------------------ | --- | -------- | --- |
| self.base_threshold                                    |     | *=  1.5  |     |
| if  self.base_threshold                                |     | >  1:    |     |
| self.base_threshold                                    |     | =  0 .9  |     |
| Listing 7.25  Controlling the threshold in the crisis  |     |          |     |
If we are in a crisis, self.base_threshold is incremented by 50%. In case, after the
increment, the value of the variable is set to a value higher than 1, then the value is
set to 90%. To control the values earned and the values that the proposer missed to
earn during the crisis, two class variables were created: self.total_earned_crisis and
self.total_not_earned_crisis.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 165
Fig. 7.5  Crisis and non-crisis total gains (earns) and losses in the ultimatum game
| if  offer  /           | value   | <  self.base_threshold:  |            |     |     |
| ---------------------- | ------- | ------------------------ | ---------- | --- | --- |
| if  stage              | ==  1:  |                          |            |     |     |
| self.total_not_earned  |         |                          | +=  offer  |     |     |
else:
| self.total_earned_crisis  |        |     | +=  offer  |     |     |
| ------------------------- | ------ | --- | ---------- | --- | --- |
| return                    | False  |     |            |     |     |
else:
| if  stage          | ==  1:  |     |            |     |     |
| ------------------ | ------- | --- | ---------- | --- | --- |
| self.total_earned  |         |     | +=  offer  |     |     |
else:
| self. total_earned_crisis |                                                          |     | += offer |     |     |
| ------------------------- | -------------------------------------------------------- | --- | -------- | --- | --- |
| return                    | True                                                     |     |          |     |     |
| Listing 7.26              | Adding up the total earned and not earned for the agent  |     |          |     |     |
The blue bars represent the values in the non-crisis condition: from left to right,
they show the total amount available to negotiate, the total amount earned by the
responder, and the total amount not earned by the proposer. The red bars represent
the corresponding values during the crisis condition, in the same left-to-right order.
The values were divided by 1000 for better representation in the graphic. When the
crisis happens, the responder increases its threshold in 50% thus the low amount
earned (Fig.7.5). The following code creates the graphic:
| width  =  0.25                         | #  the  | bars  width  |     |             |      |
| -------------------------------------- | ------- | ------------ | --- | ----------- | ---- |
| df  =  pd.read_csv("analysis_ml.csv")  |         |              |     | #  reading  | the  |
text  file
| no_crisis  | =  df[df["Stage"]  |     | ==  1]  | #  filter  | the  |
| ---------- | ------------------ | --- | ------- | ---------- | ---- |
dataframe  for
| values           | without  | crisis                       |     |     |          |
| ---------------- | -------- | ---------------------------- | --- | --- | -------- |
| no_crisis_total  |          | =  no_crisis[’Value’].sum()  |     |     | /  1000  |
#  sum  the
| total  | values                        | divided  | by  1000  |     |     |
| ------ | ----------------------------- | -------- | --------- | --- | --- |
| tmp  = | no_crisis[no_crisis[’Result’] |          |           | ==  | 1]  |

166 J.MargaridoandP.Campos
# filter the values with a positive outcome
no_crisis_earns = tmp[’Proposed’].sum() / 1000
# calculate the total value divided by 1000
tmp = no_crisis[no_crisis[’Result’] == 0]
# filter the values with a negative outcome
no_crisis_losses = tmp[’Proposed’].sum() / 1000
# calculate the total value divided by 1000
crisis = df[df["Stage"] == 2]
# filter the dataframe for values with crisis
crisis_total = crisis[’Value’].sum() / 1000
# calculate the total value divided by 1000
tmp = crisis[crisis[’Result’] == 1]
# filter the values with a positive outcome
crisis_earns = tmp[’Proposed’].sum() / 1000
# calculate the total value divided by 1000
tmp = crisis[crisis[’Result’] == 0]
# filter the values with a negative outcome
crisis_losses = tmp[’Proposed’].sum() / 1000
# calculate the total value divided by 1000
lx = [’Total’, ’Earns’, ’Losses’]
# create a list for the legends in
# the graphic
ly1 = [round(no_crisis_total, 2),
round(no_crisis_earns ,2 ),
round(no_crisis_losses, 2)]
# create a list with the first set of values
ly2 = [round(crisis_total, 2), round(crisis_earns, 2),
round(crisis_losses, 2)] # create a list with the first
set of values
plt.style.use(’fivethirtyeight’) # graphic style
plt.subplot(2, 1, 1) # define the position of
# the top subplot
plt.title("Without crisis") # title for the top subplot
plt.bar(lx, ly1, width=width) # create the top subplot
for n in range(len(ly1)):
plt.text(n, ly1[n], ly1[n], ha="center",
va="bottom") # put the values above
# the bars of the top subplot
plt.subplot(2, 1, 2) # define the position of
# the bottom subplot

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 167
plt.title("With crisis") # title for the bottom
# subplot
plt.bar(lx, ly2, width=width, color="red")
# create the bottom subplot
for n in range(len(ly2)):
plt.text(n, ly2[n], ly2[n], ha="center",
va="bottom") # put the values above the
# bars of the bottom subplot
plt .show() # show the graphic
Listing 7.27 Code to create the graphic
Explanations of the code are given in the code commentaries. By negative
outcome we mean negotiations that were not successful and by positive outcome
we mean negotiations that were successful.
7.5 The Ultimatum Game with Reinforcement Learning
The main motivation for implementing Reinforcement Learning in the Ultimatum
Game was to determine whether agents could discover the game-theoretical equi-
librium through experience alone, without being explicitly programmed to play it
[13]. In Reinforcement learning individuals tend to adopt actions that yielded high
payoffs in the past, and avoid actions that have yielded low payoffs [14]. This is the
standard learning model in behavioural psychology and it has gained the attention
of economists. As in imitative models, payoffs describe choice behaviours but it is
“one’s own past payoffs that matter, not the payoffs of others”, [15].
The most important characteristic distinguishing reinforcement learning from
other types of learning is that it uses training information that evaluates the actions
taken rather than instructs by giving correct actions, [4]. If standard Machine
Learning is about learning from given data, reinforcement learning is about active
experimentation [16].
Le Gléau et al. [17] used an iterated multi-agent version of the Ultimatum Game
(also known as the Pirate Game), in which pirates have to share coins according
to specific rules. The authors used Artificial Neural Network to output an integer
partition of discrete finite resources, trained by a Reinforcement Learning agent to
identify an acceptable offer to the voting agents. They model an interest to evaluate
the performances against several kinds of voting behaviours.
In our implementation of learning in the Ultimatum Game, we employ Q-
Learning. This approach does not require a model of the environment. Q-learning
can handle problems with stochastic transitions and rewards, without requiring
adaptations. The same general framework has been approached by [3]. [9]: Two
Q matrices, one for each agent, represent the expected reward for every state-
action pair—that is, the reward that the agent expects to obtain by choosing each

168 J.MargaridoandP.Campos
Fig. 7.6 The program flow
with Q-learning
action, for each state he could be in. We adopt a e-greedy approach. E-greddy (or
Epsilon-Greedy) is a simple method to balance exploration (to discover new features
about the world) and exploitation (using what we already know about the world) by
choosing between them randomly (Fig.7.6).
The program flow can be illustrated as follows.
. The method get_to_business() in the agent proposer is called from the code in
the main.py file and gives the kick off for the simulation
. The method get_to_business() calls the method make_proposal() in the proposer
class
. This is done in a loop depending on the value defined in the variable iterations
. When this loop ends, the analyse class is called to display a graphic showing the
simulation results.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 169
| 7.5.1  Analysing the  | Code  |     |
| --------------------- | ----- | --- |
This project has three files:
. main.py—the entry point
. responder.py—the responder class with the methods concerning its functionality
. proposer.py—the proposer class with the methods concerning its functionality
. The responders are going to learn the best choice between accepting or not
accepting the offer from the proposer. To help them to decide a Q matrix is
created.
. There is only one base value, in this case 1000 monetary units.
. The responder will be offered from 10% to 90% of this amount in increments of
10% (10%, 20%, 30%, etc.).
This Q Matrix has three columns, being the first one the percentage offered, the
second one the value accepted for that offer and the third column is the value not
accepted for that offer. The Q Matrix looks like this (Table 7.4 and Fig.7.7).
Notice that we never add lines to this Q Matrix. We only update the values in the
columns.
The first column shows the percentage offered to the responder.
The second column shows the values that were accepted by the responder to the
percentage offered in the first column.
The third column has the values that were not accepted by the responder to the
percentage offered in the first column.
| def  __init__(self,         | file):      |            |
| --------------------------- | ----------- | ---------- |
| self.file                   | =  file     |            |
| self.qmatrix                | =  [[’  ’,  | 1,  0]]    |
| self.visits                 | =  {}       |            |
| for  n  in  np.arange(0.1,  |             | 1,  0.1):  |
self.qmatrix.append( [round(n,  1),  0,  0])
| self.visits[round(n , |     | 1)] = 0 |
| --------------------- | --- | ------- |
Listing 7.28  Code to create the Q Matrix
Table 7.4  The Q Matrix

170 J.MargaridoandP.Campos
Fig. 7.7  Program fluxogram
The code above creates the Q Matrix and a dictionary named visits, where the
keys are the percentages offered to the responder and the values of the number of
times that percentage was offered.
In the end, we will have a dictionary that looks like this:
{0.1:  1115,  0.2:  1095,  0.3:  1064,  0.4:  1115,  0.5:  1170,
| 0.6:  1147,   | 0.7:  1097,                        | 0.8:  1099 , | 0.9: 1098} |
| ------------- | ---------------------------------- | ------------ | ---------- |
| Listing 7.29  | Example of the dictionary content  |              |            |
As we can see, the variables are initialized in the __init__  method of the class
responder. We use the package NumPy to generate numbers from 0.1 to 0.9 in steps
of0.1(0.1,0.2,0.3,...,0.9).
Now, let us start from the beginning and analyse the code.
7.5.2  The main.py File
The code in this file is very simple:
| from  responder                   | import  | responder  |        |
| --------------------------------- | ------- | ---------- | ------ |
| from  proposer                    | import  | proposer   |        |
| file  =  open("analysis_rl.csv",  |         |            | "w+")  |
file.writelines("Num,Value,Proposed,Result,Epsilon\n")
| value  =  | 1000  |     |     |
| --------- | ----- | --- | --- |
resp  =  responder(file)
prop = proposer()

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 171
iterations = 10000
epsilon = 1
decrement = 1 / iterations
for n in range(iterations):
prop.get_to_business(n, resp, epsilon)
epsilon -= decrement
resp_qmatrix = resp.get_matrix()
prop_qmatrix = prop.get_matrix()
Listing 7.30 Code in the main.py file
The program consists of several steps: First, we must import the classes
responder and proposer.
Then, we create the handler for the file analysis_rl.cvs, where we are going to
record all the transactions in the simulation.
The variable value contains the maximum value to be used. In this case, it is
1000.
The instances of the classes are instantiated in the variables resp and prop and
the handler to the file is passed to the responder.
The algorithm we are using is called E-greedy policy, therefore we need an
.
epsilon variable. We also need a variable with the number of iterations for the
simulation and another variable that contains the decrement.
After this, we only need a loop to execute the simulation, and that is all.
Let us see why the epsilon and decrement variables are needed.
7.5.3 The E-Greedy Algorithm
.
In Reinforcement Learning (RL), exploration and exploitation form a fundamental
trade-off. Exploration seeks to expand knowledge, while exploitation leverages
knowledge. Strategies like E-greedy, UCB, and Thompson Sampling each offer
.
systematic ways to navigate this trade-off. In our case, we will use an E-greedy
.
policy to control the exploration: a higher E (epsilon) encourages more exploration
.
— trying new actions-, while a lower E (epsilon) favors exploitation — choosing
.
the best-known action. Therefore, we need to tell the algorithm where to explore
and sometimes let it explore a random possibility. This is how we assure that all the
possibilities are tested and this is where we use the epsilon variable.
In this case, the number of iterations is 1000 and the decrement is 1000 /
iterations.

172 J.MargaridoandP.Campos
Table 7.5 The Q Matrix
The epsilon value is 1 and we decrement it in every iteration of the simulation,
as shown in the code below.
for n in range(iterations):
prop.get_to_business(n, resp, epsilon )
epsilon -= decrement
Listing 7.31 Calling the method get_to_business() and the variable epsilon decrement
The proposer receives the epsilon value and passes it to the responder calling the
method make_proposal().
The responder generates a random value using the NumPy method random.
p = np.random.random ()
Listing 7.32 Generating a random value
This method returns a value from the interval [0.1 and 1.0) and, as seen in the
code above, the variable p is set with the value returned.
If p is less than epsilon, the column from which the value is read is chosen
randomly from the Q Matrix, either the column of accepted values or the column of
rejected values.
If p is equal or higher than epsilon, the higher value of the two columns will be
used.
Let us see an example. Referencing Table 7.5,wehave:
The percentage to offer is 0.3 The value p is 0.2 and the epsilon is 0.4
These values mean that the offer is 30% of 1000 and since p is smaller than
epsilon, a random column will be chosen. It will be either column 1 or 0.
The choice will be made with the following code:
col = random.randint(0, 1)
Listing 7.33 Generating a value between 0 and 1
The variable code will receive the value 0 or 1, and, according to that value a
column will be chosen.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 173
Let us see what happens when the method get_to_business  from the class
proposer is called.
7.5.4  The Class Proposer
The method __init__ initializes a few variables:
def  __init__(self):
| self.offer_values              |                                              |        | =  [0.1,  | 0.2,     | 0.3,   | 0.4,  | 0.5,  |
| ------------------------------ | -------------------------------------------- | ------ | --------- | -------- | ------ | ----- | ----- |
| 0.6,                           | 0.7,                                         | 0.8,   | 0.9]      |          |        |       |       |
| self.qmatrix                   |                                              | =      | [[’  ’,   | 1,  0]]  |        |       |       |
| self.visits                    |                                              | =  {}  |           |          |        |       |       |
| for  n                         | in  np.arange(0.1,                           |        |           | 1,       | 0.1):  |       |       |
| self.qmatrix.append([round(n,  |                                              |        |           |          | 1),    | 0,    | 0])   |
| self.visits[round(n ,          |                                              |        |           | 1)]      | = 0    |       |       |
| Listing 7.34                   | The method __init__() in the proposer class  |        |           |          |        |       |       |
The list offer_values  contains the percentages to offer from 10% to 90% in
increments of 10%.
The Q matrix creates a list like the one shown above.
The visits is a dictionary where occurrences of the percentages offered are
registered in the same way as in the example below:
| {0.1:  1644,  | 0.2:  | 1634,  | 0.3:  | 1652,  | 0.4:         | 1649,  | 0.5:  |
| ------------- | ----- | ------ | ----- | ------ | ------------ | ------ | ----- |
| 1670,         | 0.6:  | 1629,  | 0.7:  | 1722,  | 0.8:  1695 , | 0.9:   | 1640} |
Listing 7.35  Example of the content of the dictionary with the visits registration
For example, 10% has been offered 1644 times, 20% 1634, and so on.
The method get_to_business receives three arguments:
. The iteration number,
. The instance of the responder class,
. The epsilon,
. The base value of the offer, in this case 1000.
This method only has two lines of code.
| Listing 7.36                | The method get_to_business()  |     |     |       |             |           |     |
| --------------------------- | ----------------------------- | --- | --- | ----- | ----------- | --------- | --- |
| def  get_to_business(self,  |                               |     |     | num,  | responder,  | epsilon,  |     |
base_value):
| offer                          | =  self.get_offer()  |     |     |     |        |         |          |
| ------------------------------ | -------------------- | --- | --- | --- | ------ | ------- | -------- |
| responder.make_proposal(n um,  |                      |     |     |     | 1000,  | offer,  | epsilon) |
The method get_offer returns a random percentage to make an offer.
The method make_proposal in the responder class (that’s why we call it with the
responder prefix) is responsible to make the offer to the responder.
The get_offer method returns a percentage of the base value to be offered to the
responder.

174 J.MargaridoandP.Campos
Listing 7.37  The method get_offer()
def  get_offer(self):
| offer  =  random.choice(self.offer_values)  |     |     |
| ------------------------------------------- | --- | --- |
| self.visits[offer]                          | +=  | 1   |
return offer
. The code random.choice (self.offer_values) chooses a random value from the list
created in the __init__: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
. Then,  the  dictionary  visits  is  incremented,  where  the  key  is  equal  to  the
percentage offered. This way, we can see how many times that percentage was
offered to the responder.
At last, we have two getters.
Listing 7.38  The getters get_matrix() and get_visits()
def  get_matrix(self):
return  self.qmatrix
def  get_visits(self):
return  self.visits
. get_matrix to return the qmatrix,
. get_visits to return the dictionary visits.
7.5.5  The Responder Class
This is the most sophisticated and challenging class.
The __init__ class is initiated with the handler for the file where we are going to
save all the outcomes of the negotiations.
| def  __init__(self,         | file):      |            |
| --------------------------- | ----------- | ---------- |
| self.file                   | =  file     |            |
| self.qmatrix                | =  [[’  ’,  | 1,  0]]    |
| self.visits                 | =  {}       |            |
| for  n  in  np.arange(0.1,  |             | 1,  0.1):  |
self.qmatrix.append( [round(n,  1),  0,  0])
| self.visits[round(n , |     | 1)] = 0 |
| --------------------- | --- | ------- |
Listing 7.39  The __init__() method for the responder class
Three class variables are defined:
. self.file  with the handler to the file where we want to save the outcome of the
negotiations,
. self.qmatrix  where the values for the Q Matrix are going to be stored so the
decisions can be made,
. self.visits where the number of times that a percentage will be visited is, in other
words, how many times that percentage is offered to the responder

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 175
Table 7.6  The visits
dictionary
The for  loop is used to create the list Qmatrix. And the dictionary visits
(Table 7.6). The for loop is used to create the list Qmatrix. The numpy package
is used to generate the lists with the values from 0.1 to 0.9.
| for  n  in  np.arange(0.1,  | 1,  | 0.1):  |     |     |
| --------------------------- | --- | ------ | --- | --- |
Listing 7.40
Code to generate a list with the values from 0.1 to 0.9
That is what we mean in the last listing: to generate numbers starting with 0.1 to 1
with steps of 0.1. The main method of this class is make_proposal  and it is called
from the proposer to make the offer.
def  make_proposal(self,  num,  base_value,  offer,  epsilon):
| epsilon_type  | =  ""  |     |     |     |
| ------------- | ------ | --- | --- | --- |
outcome  =  False
column  =  0
p  =  np.random.random()
self.update_visits(offer)
if  p  <  epsilon:
| #  =========                | Random                              | =========  |             |            |
| --------------------------- | ----------------------------------- | ---------- | ----------- | ---------- |
| epsilon_type                | =  "Random"                         |            |             |            |
| outcome,                    | column  =  self.get_random_value()  |            |             |            |
| #  True  =                  | Accept,  False                      | =  reject  |             |            |
| #  Update                   | the  qmatrix                        |            |             |            |
| self.update_qmatrix(offer,  |                                     |            | base_value  | *  offer,  |
column)
| self.save_transaction(num,  |                 |     | base_value,  | offer,  |
| --------------------------- | --------------- | --- | ------------ | ------- |
| outcome,                    | epsilon_type )  |     |              |         |
else:
| #  =========               | Max  value                            | =========  |                |         |
| -------------------------- | ------------------------------------- | ---------- | -------------- | ------- |
| epsilon_type               | =  "Max"                              |            |                |         |
| outcome,                   | column  =  self.get_max_value(offer)  |            |                |         |
| offered_value              | =  int(base_value                     |            | *  offer)      |         |
| #  value being             |                                       |            |                |         |
| offered by                 | the proposer                          |            |                |         |
| self.update_qmatrix(offer, |                                       |            | offered_value, | column) |
Listing 7.41  The make_proposal() method

176 J.MargaridoandP.Campos
Let us go through this code. This method receives four values:
. num is the number of the iteration and is used to save in the text file, analy-
sis_rl.txt so we can track the order of the results,
. base_value is the value we are using for the transaction,
. offer is a percentage from 10% to 90% that refers to the base_value,
. epsilon is used to decide if we are going to select a column randomly or the
column with the maximum value.
We start the method by defining three variables’ values:
. epsilon_type is used to save in the text file, the way how it was decided to choose
the value, that is, if it was chosen randomly or by the maximum value of the two
columns,
. outcome will receive true or false, if the transaction was successful or not,
. column will receive the column from where the values in Q Matrix list are going
to be read.
In the calculations for the Q Matrix, we use the number of times a percentage is
visited. This value is stored in dictionary visits, and that’s the task of this code:
self.update_visits(offer)
Listing 7.42 Calling the update_visits() to update the visits dictionary
The update of the dictionary visits is straight forward:
def update_visits(self, offer):
self.visits[offer] += 1
Listing 7.43 The update_visits() method code
We simply add 1 to the value in the dictionary, which has a key equal to the offer.
For instance:
self.visits[0.3] += 1
Listing 7.44 Example of a visit update
Now a value is randomly generated to be compared to the epsilon value received:
p = np.random.random ()
Listing 7.45 Generating a random value
The variable p is loaded with a random value from the range between 0.0 and
1.0. Remember that the value in p is going to be compared to the epsilon value. If
it is smaller, a random column is chosen; otherwise, the column with the maximum
value is used.
If p is smaller than epsilon, we set the variable epsilon_type to “Random”
because the value from a random column is to be fetched. If the column is the accept
column the proposal is accepted; otherwise, if it is the reject column, the proposal
is rejected.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 177
Now, the Q Matrix must be updated, and the transaction is saved in the text file
analysis_rl.txt.
This is the code that executes this algorithm:
| epsilon_type                | =  "Random"                         |                   |            |           |
| --------------------------- | ----------------------------------- | ----------------- | ---------- | --------- |
| outcome,                    | column  =  self.get_random_value()  |                   |            |           |
| #  True                     | =  Accept,                          | False  =  reject  |            |           |
| self.update_qmatrix(offer,  |                                     | base_value        | *  offer,  | column )  |
| self.save_transaction(num,  |                                     | base_value,       | offer,     | outcome , |
epsilon_type)
Listing 7.46  Calling the methods to update the Q Matrix and save the transaction in the csv file
The random column is fetched with the method get_random_value() which will
return the second (accept) or the third (reject) column of the Q Matrix, and, returns
two values: the outcome (true or false) and the column.
def  get_random_value(self):
| column   | =  0               |            |     |     |
| -------- | ------------------ | ---------- | --- | --- |
| outcome  | =  False           |            |     |     |
| col  =   | random.randint(0,  | 1)         |     |     |
| if  col  | ==  0:             |            |     |     |
| column   | =  1               | #  accept  |     |     |
outcome  =  True
else:
| column        | =  2                         | # refuse |     |     |
| ------------- | ---------------------------- | -------- | --- | --- |
| return        | outcome,                     | column   |     |     |
| Listing 7.47  | The get_random_value() code  |          |     |     |
The variable column is set to 0, outcome is set to false and col is set to a random
value 0 or 1 generated by the method random.randint(0,  1)  and this initializes the
variables.
If col equals 0, the column is set to 1, which means the proposal is accepted and
outcome is set to true.
If col equals 1, the column is set to 2 and the outcome remains false (as it was
initialized that way), so no further changes are needed.
Finally, the variables outcome and column are returned to the calling method.
After this, the Q Matrix is updated calling the method update_qmatrix().
| def  update_qmatrix(self,  |                                | offer,  offered_value,      |                   | column):  |
| -------------------------- | ------------------------------ | --------------------------- | ----------------- | --------- |
| for  n                     | in  range(len(self.qmatrix)):  |                             |                   |           |
| if                         | self.qmatrix[n][0]             | ==                          | offer:            |           |
|                            | n_value                        | =  self.visits[offer]       |                   |           |
|                            | qtable_value                   | =  self.qmatrix[n][column]  |                   | *         |
|                            | (n_value                       | - 1)  /  n_value            | +  offered_value  |           |
/  n_value
|     | self.qmatrix[n ][column] |     | = qtable_value |     |
| --- | ------------------------ | --- | -------------- | --- |
break
| Listing 7.48  | The update_matrix() code |     |     |     |
| ------------- | ------------------------ | --- | --- | --- |

| 178 |     |     |     | J.MargaridoandP.Campos |
| --- | --- | --- | --- | ---------------------- |
This method receives:
. offer—the percentage of the offer (0.3, 0.5, etc),
. offered_value—the values of the offer (e.g., 1000 * 30% = 300),
. column—the column that is being used (the accept or reject column).
First, we must find the line with the value that is equal to the offer. Let us say the
offer is 30% (0.3), then we must find the line with that value in the first column.
The search is made through a for loop and by comparing the value in the first
column with the value of the offer.
The line of code self.qmatrix[n][0] == offer compares the value in the Q Matrix
in the line n, column 0 to the value of offer.
The variable n_value  is loaded with the value in the visits table for that offer.
Remember that the visits table has the number of times that each offer is used.
Now, we only have to update the value in the Q Matrix according to the next
formula:
| self.qmatrix[n][column]                                         |            | *  (n_value | - 1)  /  n_value  | +   |
| --------------------------------------------------------------- | ---------- | ----------- | ----------------- | --- |
| offered_value                                                   | /  n_value |             |                   |     |
| Listing 7.49  The formula to update the values in the Q Matrix  |            |             |                   |     |
The new value of the Q-matrix for this offer is calculated by multiplying the
existing value by n_value  (the number of times this offer has been used), dividing
by n_value, and then adding the offered_value—which is the base value multiplied
by the offer percentage (e.g.,1000×30%=300) divided by n_value.
.
Continuing with the method make_proposal), if p is higher or equal to epsilon,
then:
The epsilon_type will be equal to “Max” and the code outcome, column  =
self.get_max_value(offer)  will be executed and receive the outcome (false or true)
and the column from where the value was fetched.
| def  get_max_value(self,  |                                | offer):   |                          |     |
| ------------------------- | ------------------------------ | --------- | ------------------------ | --- |
| max_value                 | =  0                           |           |                          |     |
| column  =                 | 0                              |           |                          |     |
| for  n  in                | range(1,  len(self.qmatrix)):  |           |                          |     |
| if  self.qmatrix[n][0]    |                                | ==        | offer:                   |     |
| if                        | self.qmatrix[n][1]             |           | >=  self.qmatrix[n][2]:  |     |
|                           | #  returns                     | value     | from  accepted  values   |     |
|                           | and  column                    | n.  1     |                          |     |
|                           | return                         | True,  1  |                          |     |
else:
|                                                | #  returns  | value    | from  refused  values  | and |
| ---------------------------------------------- | ----------- | -------- | ---------------------- | --- |
|                                                | column      | n. 2     |                        |     |
|                                                | return      | False, 2 |                        |     |
| Listing 7.50  The get_max_value() method code  |             |          |                        |     |
This code goes through the Q Matrix and finds the line that has the value of
the offer in the first column, then, from that line, it compares the values of the two

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 179
columns and returns the column with the maximum value (if it is the accept column
or the reject one) and the value in it.
After that, the method update_qmatrix() is called to update the Q Matrix. Finally,
the transaction is saved in the text file. The method to do this is save_transaction().
def save_transaction(self, num, base_value, offer,
success, epsilon_type):
self.file.writelines(f"{num},{base_value},
{round(offer, 2)},{success },{epsilon_type}\n")
Listing 7.51 The save_transaction() method code
To this method a few values are passed:
. num is an order number
. base_value is the value from which a percentage is being offered to the responder
. offer is the percentage being offered
. success is equal to either true or false, according to the outcome of the transaction
. epsilon_type is either random or max according to the method used to select a
column
The values are written in the text file using the instance of file and its method
writelines. The parameters passed to the method are the following:
(f"{num},{base_value},{round(offer, 2)},{success},
{epsilon_type}\n ")
Listing 7.52 Parameter passed to the file.writelines() method
The letter f in the beginning allows us to insert variables in a string; this means
that the variables inside brackets are going to be replaced by the value of those
variables. Let us see an example:
name = "John"
print(f"Hello { name}")
Listing 7.53 Example of using formatted string literals
This code will print on the screen “Hello John” (without the quotation marks).
7.5.6 The Crisis
The crisis is triggered in the middle of the simulation. For the crisis to happen some
changes in the code need to be made.
crisis = False
for n in range(iterations):
if n > iterations / 2:
crisis = True

| 180                      |     |        |           |         | J.MargaridoandP.Campos |
| ------------------------ | --- | ------ | --------- | ------- | ---------------------- |
| prop.get_to_business(n,  |     | resp,  | epsilon,  | value,  |                        |
crisis)
| epsilon | -=  decrement  |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
Listing 7.54  Changes in the code to support a crisis trigger
In the main.py  file some code is added to the main loop. The variable crisis  is
created with a default value of false and will be changed to true inside the main
loop, when the value for n  is higher than the number of iterations divided by two.
This means that the crisis will happen after the middle of the simulation.
The variable crisis  is passed to the method get_to_business()  as one of its
arguments.
The proposer will do nothing with this value, so it will be passed to the responder
through the method make_proposal().
Having a crisis active will change the way the responder reacts to the proposal.
This reaction can be simulated according to the perspective of the programmer
because the responder can react in two different ways:
. The responder accepts any offer because, in a crisis, anything is considered
acceptable and better than receiving nothing.
. the responder only accepts proposals over a certain threshold, for an instance
50%.
A few modifications to the make_proposal()  method were made in the class
responder.
def  make_proposal(self,  num,  base_value,  offer,  epsilon,
crisis):
| threshold     | =  0.5       |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- |
| epsilon_type  | =  "Crisis"  |     |     |     |     |
self.update_visits(offer)
| if  crisis  | ==  True:                   |     |             |     |     |
| ----------- | --------------------------- | --- | ----------- | --- | --- |
| if          | offer  >=  threshold:       |     |             |     |     |
|             | outcome  =  True            |     |             |     |     |
|             | column  =  1                |     |             |     |     |
|             | self.update_qmatrix(offer,  |     | base_value  |     | *   |
offer,  column)
else:
|     | outcome  =  False           |     |             |     |     |
| --- | --------------------------- | --- | ----------- | --- | --- |
|     | column  =  2                |     |             |     |     |
|     | self.update_qmatrix(offer,  |     | base_value  |     | *   |
offer,  column)
| self.save_transaction(num,  |               |     | base_value , |     | offer, |
| --------------------------- | ------------- | --- | ------------ | --- | ------ |
| outcome,                    | epsilon_type) |     |              |     |        |
| return                      | outcome       |     |              |     |        |
Listing 7.55  The make_proposal() method
The method make_proposal()  receives a new parameter, which is the variable
crisis containing true or false.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 181
Threshold is defined with a default value of 0.5 but can be changed to any other
value. This value is the minimum percentage of the base value that the responder is
willing to accept.
The variable epsilon_type is set with the text “Crisis” that will be saved in the
text file analysis_rl.csv.
The visits dictionary will be incremented by 1, where the key is equal to the
percentage offered.
The rest of the code to deal with the crisis is straight forward.
If the variable crisis is equal to True, the offer is verified, if it is equal or higher
to the threshold.
If it is, then outcome is set to True, the column is set to 1 (the column of the
accepted values in the Q Matrix) and finally the method update_qmatrix() is called
to update the Q Matrix.
In case the offer is smaller than the threshold, the outcome is set to False, the
column is set to 2 (the column of the rejected values in the Q Matrix) and finally the
method update_qmatrix() is called to update the Q Matrix. In the end, the value of
the variable outcome is returned.
If crisis is equal to False, all this code will be skipped and the code before
described will be executed.
7.5.7 Analysis
The last part of the program contains the analysis of the data.
To separate roles in the code, a new class was created, the class analyse.
This class is instantiated and called from the main file, with the following code:
from analyse import analyse
analyse = analyse( )
Listing 7.56 Importing the class analyse and instantiating it
The first line of code imports the class defined in the file analyse.py. The second
line of code instantiates and, in the process, executes the class __init__ method.
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
class analyse:
Listing 7.57 Code importing the packages pandas, matplotlib and numpy in the analyse class
These lines of code are very simple.
. We import the Pandas package to analyse the text file analysis_rl.csv and give it
the name pd.
. Then we import pyplot from matplotlib and give it the name plt.
. Next the numpy package is imported with the name np.
. And then the class analyse is created

182 J.MargaridoandP.Campos
The class analyse has only one method that is executed when the class is
instantiated, which is the method __init__.
Let us go through the code.
def __init__(self):
# Analyse with Pandas
trades = pd.read_csv(’analysis_rl.csv’)
# Add column
trades["Net_value"] = trades[’Value’] *
trades[’Proposed’]
no_crisis = trades[(trades.Epsilon ==
’Random’) | ( trades.Epsilon == ’Max’)]
crisis = trades[trades[’Epsilon’] = = "Crisis"]
Listing 7.58 The __init__() method code in the analyse class
The file analysis_rl.csv is loaded into the variable trades.
To make things easier we create a calculated column with the product of the base
value and the percentage proposed to the responder.
From the variable trades we create two data frames: one with the name no_crisis
containing all the values that were the result of the simulation without a crisis, and
other with the name crisis containing all the values from the simulation with crisis.
The values without crisis have an epsilon of Random or Max. With a crisis,
Random or Max do not matter.
Now we are going to create the list of values to generate the chart.
width = 0.25
divider = 1000
plt.style.use(’fivethirtyeight’)
lx = [’Rand. True’, ’Rand. False’, ’Max True’,
’Max False’, ’Total True’, ’Total False’]
lx2 = [’Crisis True’, ’Crisis False’]
tmp = no_crisis[(no_crisis.Epsilon == ’Random’) &
(no_crisis.Result == True)]
ly = [tmp["Net_value"].sum() / divider] # Random True
tmp = no_crisis[(no_crisis.Epsilon == ’Random’) &
(no_crisis.Result == False)]
ly.append(tmp["Net_value"].sum() / divider)
# Random False
tmp = no_crisis[(no_crisis.Epsilon == ’Max’) &
(no_crisis.Result == True)]
ly.append(tmp["Net_value"].sum() / divider)
# Max True
tmp = no_crisis[(no_crisis.Epsilon == ’Max’) &
(no_crisis.Result == False)]

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 183
| ly.append(tmp["Net_value"].sum()  | /  divider)  |     |
| --------------------------------- | ------------ | --- |
# Max  False
| tmp  =  no_crisis[no_crisis[’Result’]  | ==  True]  |     |
| -------------------------------------- | ---------- | --- |
#  Total  results  true
| ly.append(tmp[’Net_value’].sum()       | /  divider)  |     |
| -------------------------------------- | ------------ | --- |
| tmp  =  no_crisis[no_crisis[’Result’]  | ==  False]   |     |
#  Total  results  false
| ly.append(tmp[’Net_value’].sum()  | / divider) |     |
| --------------------------------- | ---------- | --- |
Listing 7.59  Code in the analyse class
As we are creating a bar chart the width  variable is used to define the width of
the bars.
The variable divider is used to divide the sums to simplify the presentation of the
chart. In this case we are dividing by 1000.
The l×variable is a list that will contain the labels for the bars and the ly variable
.
is another list that will contain the values to be represented in the chart. This is done
by summing the occurrences of the movements with certain characteristics like for
example:
| tmp  =  no_crisis[(no_crisis.Epsilon  | ==  ’Random’)  | &   |
| ------------------------------------- | -------------- | --- |
(no_crisis .Result  ==  True )]
Listing 7.60  Filtering the dataframe into the variable temp
which filters all the lines referring to the transactions without crisis and where the
epsilon is random, and the result is true.
We use a temporary variable named tmp to create a dataframe with the filter, then
we sum the values in the column Net_value and append it to the ly list. In the end,
the list ly
will contain something like [933.7, 945.1, 428.4, 208.5, 1721.5, 479.0]
(remember that these values are divided by 1000).
These are the sums of the transactions made without crisis, and now we are going
to create the list with the values from the transactions in the crisis. This list has the
name of ly2.
| tmp  =  crisis[(crisis.Result  ==  True)]   |              |     |
| ------------------------------------------- | ------------ | --- |
| ly2  =  [tmp["Net_value"].sum()  /          | divider]     |     |
| tmp  =  crisis[(crisis.Result  ==  False)]  |              |     |
| ly2.append (tmp["Net_value"].sum()          | /  divider ) |     |
Listing 7.61  Code from the __init__() method in the analyse class
We use, again, the temporary variable tmp with the values filtered but this time
the values are from the epsilon with the value of Crisis which are in the dataframe
crisis.

| 184 |     |     | J.MargaridoandP.Campos |
| --- | --- | --- | ---------------------- |
We do the same with the dataframe no_crisis  but this time with the dataframe
crisis. For example:
| tmp  =  crisis[(crisis.Result  |     | ==  True)]  |     |
| ------------------------------ | --- | ----------- | --- |
ly2  =  [tmp["Net_value"].sum( )  /  divider]  #  Random true
| Listing 7.62  | Code from the __init__() method in the analyse class  |     |     |
| ------------- | ----------------------------------------------------- | --- | --- |
The tmp  variable is loaded with the value of the dataframe crisis  which contains
only the values of the crisis.
Once the decisions made by the responder during the crisis are not based in
the variable epsilon, we will have only two bars: one showing the totals for the
transactions with an outcome of true, and another for the transactions with an
outcome of false.
Now it is time to draw the chart using matplotlib.
| plt.subplot(2,                | 1,  1)              |               |               |
| ----------------------------- | ------------------- | ------------- | ------------- |
| plt.title("Without            | crisis")            |               |               |
| plt.bar(lx,                   | ly,  width=width)   |               |               |
| for  n  in  range(len(ly)):   |                     |               |               |
| plt.text(n,                   | ly[n],  ly[n],      | ha="center",  | va="bottom")  |
| plt.subplot(2,                | 1,  2)              |               |               |
| plt.title("With               | crisis")            |               |               |
| plt.bar(lx2,                  | ly2,  width=width,  | color="red")  |               |
| for  n  in  range(len(ly2)):  |                     |               |               |
| plt. text(n,                  | ly2[n],  ly2[n],    | ha="center",  |               |
va="bottom")
plt .show()
| Listing 7.63  | Code to draw the chart  |     |     |
| ------------- | ----------------------- | --- | --- |
Drawing the chart is quite simple.
We are going to draw two sets of bars. One representing the transactions without
crisis and another with the crisis.
This is done with subplots.
| plt.subplot(2,  | 1,  1 )  |     |     |
| --------------- | -------- | --- | --- |
| Listing 7.64    | Subplot  |     |     |
The first argument of subplot is the number of rows, the second the number of
columns and the third is the order number.
After telling matplotlib  where we want the chart, we give it a title, in this case
the first chart has the title “Without crisis”. Now we draw the first chart with
| plt.bar(lx,   | ly,  width= width)     |     |     |
| ------------- | ---------------------- | --- | --- |
| Listing 7.65  | Drawing the bar chart  |     |     |
Bar is the Matplotlib method used to draw the bar chart; it takes the column labels
(stored in the variable lx), the values to display (in ly), and optionally the column
width, defined in the variable width.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 185
The loop
| for  n  in  range(len(ly)):  |                                                 |                |               |
| ---------------------------- | ----------------------------------------------- | -------------- | ------------- |
| plt.text(n,                  | ly[n],  ly[n],                                  | ha="center" ,  | va="bottom ") |
| Listing 7.66                 | Centering the text above the bars of the chart  |                |               |
is used to place the value represented by the bars above them.
Now, we do the same for the second set of bars representing the values with the
crisis.
| plt.subplot(2,                | 1,  2)              |               |     |
| ----------------------------- | ------------------- | ------------- | --- |
| plt.title("With               | crisis")            |               |     |
| plt.bar(lx2,                  | ly2,  width=width,  | color="red")  |     |
| for  n  in  range(len(ly2)):  |                     |               |     |
| plt.text(n,                   | ly2[n],  ly2[n ],   | ha="center",  |     |
va="bottom ")
| Listing 7.67  | Code for the second subplot  |     |     |
| ------------- | ---------------------------- | --- | --- |
Finally, the chart is displayed on the screen.
plt.show()
| Listing 7.68  | Show the chart  |     |     |
| ------------- | --------------- | --- | --- |
7.5.8  Results
As we can see, there are two sets of bars, the top set and the bottom set: the blue
ones and the red ones.
Remember that in the non-crisis scenario, there is a variable called epsilon which,
according to the previously explained algorithm, may either point to a random
value—chosen from the True or False column—or to the maximum value, which
is the highest between the two columns (False or True) (Fig.7.8).
The top blue bars represent from left to right:
. The total amount proposed to the responder which was chosen randomly and had
a positive outcome
. The total amount proposed to the responder which was chosen randomly and had
a negative outcome
. The  total  amount  proposed  to  the  responder  which  was  chosen  from  the
maximum value of the two columns and had a positive outcome
. The  total  amount  proposed  to  the  responder  which  was  chosen  from  the
maximum value of the two columns and had a negative outcome
. The total amount with a positive outcome
. The total amount with a negative outcome
After the crisis the value of the epsilon variable is not used because a threshold
is defined.

186 J.MargaridoandP.Campos
Fig. 7.8 Accept only 50% or more when crisis is active
Fig. 7.9 Accept anything when crisis is active
The bottom red bars represent from left to right (Fig.7.9):
. The total amount with a positive outcome
. The total amount with a negative outcome
In the example above, we can see that when the crisis is active, the responder
earns 100% of whatever the offer is. It should be noticed that in a crisis, the proposer
does not learn because it has a fixed objective as discussed above.

7 TheUltimatumGameasaParadigmforLearningAgents:APythonAdventure 187
7.6 Final Considerations
This chapter delves into the utilization of Agent-Based Models (ABMs) for
comprehending economic crises and pandemics, incorporating a machine learning
framework for both description and prediction. With a focus on the significance
of Game Theory within ABMs, the Ultimatum game is employed as a template
for learning agents. In this game, featuring a proposer and responder negotiating
a split, the consequences hinge on the responder’s acceptance or refusal. The
Python implementation proceeds in stages, initially establishing a baseline model
where proposers employ fair or unfair split strategies. Subsequently, two learning
strategies—Fictitious Play and Reinforcement Learning—are introduced. Ficti-
tious Play aims to minimize responder rejections, while Reinforcement Learning
optimizes action policies through sequential decision processes. This showcases
the synergies between ABMs, Game Theory, and machine learning in economic
modeling.
During a specific time step, a crisis is initiated midway through the predetermined
iterations, leading to responders raising their acceptance threshold by 50%.
The entire implementation of the model is done step by step in Python with the
aim of illustrating the creation of an agent-based model from scratch.
References
1. M. J. Wooldridge, An Introduction to Multiagent Systems (John Wiley & Sons, Chichester,
2002)
2. G. Fagiolo, A. Roventini, Macroeconomic policy in dsge and agent-based models. Rev. OFCE
124, 67–116 (2012)
3. F. Zhong, S.O. Kimbrough, D. Wu, Cooperative agent systems: artificial agents play the
ultimatum game. Group Decis. Negot. 11(6), 433–447 (2002). https://doi.org/10.1023/A:
1020687015632
4. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, 2nd edn. (MIT Press,
Cambridge, 2018)
5. J.C. Harsanyi, On the rationality postulates underlying the theory of cooperative games. J.
Conflict Resolut. 5(2), 179–196 (1961)
6. F. Zhong, S.O. Kimbrough, D. Wu, Cooperative agent systems: artificial agents play the
ultimatum game. Group Decis. Negot. 11(6), 433–447 (2002). https://doi.org/10.1023/A:
1020687015632
7. D. Rand, C. Tarnita, H. Ohtsuki, M.A. Nowak, Evolution of fairness in the one-shot anonymous
ultimatum game. Proc. Natl. Acad. Sci. U.S.A. (2012). Edited by Kenneth Wachter. https://doi.
org/10.1073/pnas.1214167110
8. M.J. Osborne, A. Rubinstein, Extensive games with perfect information (Chapter 6), in A
Course in Game Theory (MIT Press, Cambridge, 1994)
9. W. Güth, R. Schmittberger, B. Schwarze, An experimental analysis of ultimatum bargaining.
J. Econ. Behav. Organ. 3(4), 367–388 (1982)
10. M.A. Nowak, K.M. Page, K. Sigmund, Fairness versus reason in the ultimatum game. Science
289(5485), 1773–1775 (2000)

188 J.MargaridoandP.Campos
11. J. Pinto, J. Rocha, J. Ribeiro, Multi-agent systems and simulation of organizations – Ultimatum
game. SMASO course, University of Porto (2021)
12. G.W. Brown, Iterative solution of games by fictitious play, in Activity Analysis of Production
and Allocation, ed. by T. C. Koopmans (Ed.) (Wiley, New York, 1951)
13. J. Pinto, J. Rocha, J. Ribeiro, MultiAgent Systems and Simulation of Organizations –
Ultimatum Game. Tech. rep., Faculty of Economics, University of Porto, Porto (2021)
14. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, 2nd edn. A Bradford Book
(The MIT Press, Cambridge, 2018)
15. H.P. Young, Individual Strategy and Social Structure: An Evolutionary Theory of Institutions
(Princeton University Press, Princeton, 1998)
16. A. Charpentier, R. Élie, C. Remlinger, Reinforcement learning in economics and finance.
Comput. Econ. 62, 425–462 (2023). https://doi.org/10.1007/s10614-021-10119-4
17. T. Le Gléau, X. Marjou, T. Lemlouma, B. Radier, Multi-agents ultimatum game with
reinforcement learning. Highlights in practical applications of agents, multi-agent systems,
and trustworthiness, in Communications in Computer and Information Science, ed. by F. De
La Prieta et al., vol. 1233 (Springer, 2020), pp. 267–278. ISBN: 978-3-030-51998-8. https://
doi.org/10.1007/978-3-030-51999-5_22. Note: HAL Id: hal-02967163

Chapter 8
Alternative Machine Learning
Approaches for an Agent-Based Model
of the Ultimatum Game Using R
Pedro Campos, José Matos, and Joaquim Margarido
8.1 Introduction
Agent-based modeling (ABM) entails the creation of models where agents make
dynamic decisions within a dynamic environment. Inference models based on
Machine Learning (ML) have the potential to enhance sequential decision-making
by learning the behavioral patterns of these agents. According to Dehkordi et al.,
ABM literature is still marginally leveraging the benefits of ML, maybe because
of the vastness of the ML domain, since selecting the right ML technique to
address a particular modeling challenge becomes a challenging task [1]. The authors
pinpoint two key factors contributing to this situation. Firstly, the vast scope of
ML encompasses a multitude of techniques, making it a challenge to discern
the most suitable approach for addressing specific modeling obstacles, such as
enhancingbehavioralfidelityandprecision.Secondly,theefficacyofMLtechniques
can fluctuate based on the intended purpose of the model, be it prediction or
explanation. Zhang et al. provide a comprehensive review of applying ML in ABM
based on four major scenarios, i.e., microagent-level situational awareness learning,
microagent-level behavior intervention, macro-ABM-level emulator, and sequential
decision-making [2].
P. Campos (@)
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
J. Matos
University of Porto, FEP, Porto, Portugal
e-mail: jamatos@fep.up.pt
J. Margarido
ISEP, Porto, Portugal
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 189
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_8

190 P.Camposetal.
In the previous Chapters, we introduced the Ultimatum Game and explored the
possibilities for agents to learn how to play the game. In this Chapter, we explore
more advanced ML tasks and use a more complex environment where agents can
interact as if they were connected in a network. We keep the explanations simple and
pedagogical to inspire the creation of Agent-Based Models. Program codes used in
this Chapter are available in https://ml4agents.free.nf.
The Ultimatum Game is a classic experimental game used in behavioral eco-
nomics and game theory to study fairness, bargaining, and decision-making. It
involves two players: a proposer and a responder that communicate by announcing
their decisions. Both players know in advance the consequences of the responder
accepting or rejecting the offer. The proposer splits a certain amount with another
agent, the responder. The responder may accept or refuse the offered amount. If
the responder accepts, both win the amounts corresponding to the proposer’s offer.
Otherwise, neither player wins any reward. This game is interesting because it
involves both economic and social factors, and the outcome depends on the behavior
of both players.
According to Harsanyi, these types of bargaining games are called “Ultimatum
Games” because one of the players can firmly commit himself in advance under
a heavy penalty that he will insist under all conditions upon a certain specified
demand, that is called his ultimatum [3] .
Since we are not considering a one-shot version of the game, we may simulate the
Ultimatum Game using ABM by creating a model where agents (the two players)
interact with each other repeatedly according to some rules. The power of Machine
Learning can then help us exploit the agents’ ability to learn how to maximize
profits from this game. There is a difference between running this game with just
two players, or with more than two players. In the first situation, with two players,
we only consider one proposer and one respondent, who interact successively. In
the second situation, with more than two players, several players will have the
possibility to behave as proposer, or as respondent.
Agents use Machine Learning algorithms to analyze data from the Ultimatum
Game experiments and identify patterns and strategies employed by the other
agents. By examining the decisions made by proposers and responders, Machine
Learning techniques can uncover insights about the factors influencing decision-
making, such as fairness considerations, social norms, or individual preferences.
We do not explore these factors in detail, since the main objective of this chapter
is to illustrate, in a simple way, the capabilities of various forms of agent learning
in the Ultimatum Game. We will apply Fictitious Play, Reinforcement Learning
and Classifiers systems, and we explore the possibilities of a transfer of learning
between players, where we may consider different scenarios of learning: from
Transfer Learning to learning as a group, using the paradigm of Organizational
Learning. We also consider that agents are placed in networks, as a metaphor for
the way how people interact in reality. Finally, we introduce other forms of learning
and interaction in Agent-Based Learning, such as layered sequential learning,
cooperative learning and social learning.
This chapter is organized as follows: in Sect.8.2 we make a review of the
Machine Learning perspective of Agent-Based Models; in Sect.8.3, we develop

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 191
several alternative approaches of learning in the Ultimatum Game. In Sect.8.4 we
introduce learning involving multiple agents in networks. In Sect.8.5, we explore
other forms of Organization and interaction in Agent-Based Learning. Finally, in
Sect.8.6, we make the concluding remarks and provide clues for future research
directions.
8.2 The Machine Learning Perspective of Agent-Based
Models
One of the very first ABMs was a simple model of residential housing segregation
designed by Thomas Schelling, with social purposes. Schelling’s segregation model
[4] demonstrated that even in cases where individuals (referred to as ‘agents’) had
no objection to being in proximity to or coexisting with agents from different racial
or economic backgrounds, they would naturally tend to separate from other agents
as time progressed. Despite its simplicity, this model offers an intriguing perspective
on how individuals could organically engage in self-segregation, even in the absence
of any explicit intention to do so.
Since the 1980s, Axelrod’s The Evolution of Cooperation [5] started a new
synergy between ABM and the social sciences that has led to the development of
the field of social simulation, in which this variety of computational social science is
used to examine the development and evolution of human society in a wide variety
of circumstances. In addition, ML models are also used by agents to learn during
the process of interactions with other agents and with the env ironment.
In the pursuit of modeling learning in economics, Brenner identified three
research directions [6]: the experimental investigation of individual learning pro-
cesses, the examination of the features of established learning models, primarily
within the domain of games, and the utilization of learning processes in an economic
context, frequently involving simulations. Also [7], classified the Evolutionary
Economics simulations in two different types; those rooted in Schumpeterians
tradition and the agent-based approach.
In a former Survey of Multi-Agent Systems from a Machine Learning Perspec-
tive, Peter Stone and Manuela Veloso identified four scenarios, [8]:
• The simplest systems are those with homogeneous non-communicating agents.
• The second scenario involves heterogeneous non-communicating agents.
• The third deals with homogeneous, communicating agents.
• Finally, the general MAS scenario involves communicating agents with any
degree of heterogeneity.
Focusing on a game theoretical perspective, Shoam [9] defined a formal setting
of stochastic games for Multi-Agent Learning (MAL), that generalizes Markov
Decision Problems, the setting from which much of the relevant learning literature
in AI originates. The authors stated that the area of learning in multi-agent systems

192 P.Camposetal.
is one of the most fertile grounds for interaction between game theory and artificial
intelligence.
In [10], Rand described the use of adaptive agents within Machine Learning
(ML), starting to explore some guidelines for how to more closely integrate ABM
and ML. To illustrate some of these issues, the author describes an integration of ML
within the El Farol Bar Problem. One important aspect of this work is the creation of
a framework that comprises two cycles: the ABM cycle, where the agents interact
with the world, update their internal models, and take actions; and the ML cycle,
where agents almost do the same, but they use history of their past actions to update
their internal models, new and take actions. Rand [10] also describes how different
Machine Learning techniques like genetic algorithms (GAs), neural nets (NNs), and
Bayesian Classifiers can easily be incorporated into many agent-based models.
Recently the ML cycle identified by Rand was also approached by [1], who
conducted a structured literature review to investigate how ABM process uses ML
techniques, and concluded that ML techniques are specifically fit for currently
underrepresented modeling purposes of social learning and illustration, and can be
used in a transparent and interpretable manner.
In their research, Dehkordi et al. [1] identify four most common ML techniques
in papers using ABM: Bayesian networks, Neural Networks, Decision Trees and
Reinforcement Learning, having the following main purposes: Explanation (used in
more than a quarter of the papers analysed); Prediction (another common purpose
in articles that use ML in their models), Description (the third most common
purpose in articles that use ML in ABM), Illustration (few cases, maybe because of
explainability limitations), Social learning (ML is not seen as a highly suitable tool
to support social learning ABM), and Analogy (also rarely observed). Therefore,
Explanation, Prediction and Description seem to be the most common goals of uinsg
ML in ABM, according to [1].
Explainability and interpretability of predictions produced by ML models is
far from straightforward. Recent advances and concerns have been devoted to the
interpretability of ML models. Deep-learning models in particular are enormously
complex, often containing hundreds of layers of neurons adding up to tens of
millions of parameters. Agent-Based Models have been commonly used within the
evolutionary economics perspective, which provides much more realistic settings
than neoclassical economics by allowing the consideration of learning agents acting
in a context of disequilibrium and bounded-rationality [11]. In [12], Angione et
al. compare multiple ML methods for ABM emulation in order to determine the
approaches best-suited to replicating the complex and non-linear behaviour of
ABMs. In this proof-of-concept study, the authors assess the effectiveness of various
machine learning methods as surrogate models to analyze ABMs. Their goal is to
see how the outputs of ABMs can pose challenges, given that the relationships
between input parameters can be nonlinear or chaotic, even in relatively simple
models. To address this, surrogate modeling has been proposed as an alternative
to computationally intensive Monte Carlo methods. Multiple machine learning

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 193
techniques for surrogate modeling in ABMs were used to identify the most suitable
approaches for representing the intricate behavior of ABMs.
Artificial Neural Networks (ANNs) and gradient-boosted trees outperform Gaus-
sian process surrogates, which are presently the most commonly used method for
surrogate modeling in complex computational models. Focusing again on economic
literature, and according to [13], there are essentially three ways of learning in
economic literature: Non-conscious learning, Routine-based Learning and Belief
Learning. Reinforcement Learning seems to be biologically fixed, because if an
action leads to a negative outcome—a punishment—this action will be avoided in
the future. On the other hand, if an action leads to a positive outcome—a reward—it
will reoccur.
However, the psychological literature on learning processes has been dominated
by cognitive learning process analysis, where mental models and belief learning
play important roles. An individual typically holds one mental model about reality,
and sometimes he or she might not be sure about certain issues and may consider
different expectations. However, people tend to fix their expectations quickly
on the basis of little evidence. Belief Learning focuses on how agents update
and revise these beliefs over time as they gather new information or interact
with the environment. Agents continuously update their beliefs to improve their
understanding of the environment and make better predictions or decisions. It is
particularly relevant in scenarios where uncertainty is present, and agents need to
reason about incomplete or noisy data.
There are several types of learning in Belief Learning, such as least-squares
learning that is based on the assumption that people make assumptions about the
functional dependencies in reality. Fictitious Play is also considered a type of belief
learning that involves players forming beliefs about the strategies of their opponents
based on observed outcomes and using those beliefs to make decisions. Initially,
these beliefs can be arbitrary or uniform across all possible strategies. As the game
progresses, players update their beliefs based on the observed actions and outcomes
of their opponents.
Classifier systems, such as Decision Trees, Support Vector Machines and K
Nearest Neighbor are also types of Belief Learning. According to [13], these are
models inspired in Artificial and Biology. Here, agents maintain a set of rules or
Classifiers that encode their beliefs about the environment. Each Classifier consists
of a condition part that specifies a pattern or condition in the input space and an
action part that determines the agent’s response or action for matching inputs. There
are other methods where learning can be improved not only by individual learning,
but by adopting a different policy. Transfer Learning between agents is one of
such methods. In these cases, it is possible to pass the trained model, (Decision
Tree, deep neural network, etc.), from one agent—the teacher—to another agent,—
the recipient—as the outcome of learning. In [14] different agents were able to
construct individual models in the form of rules, which were then merged into a
single combined rule set. Transfer Learning between agents recognizes that agents
can benefit from the knowledge and experience acquired by other agents, leading
to improved learning efficiency and performance. In the following, we will focus

194 P.Camposetal.
on Belief learning, and other types of Machine Learning , such as Reinforcement
Learning and Transfer Learning in more complex contexts, using the Ultimatum
Game.
8.3 Learning in the Ultimatum Game
Agents can learn in the Ultimatum Game through various learning algorithms and
strategies. The ability to learn allows agents to adapt their behavior and decision-
making based on previous experiences and outcomes, such as Fictitious Play,
Reinforcement Learning, Decision Trees and Transfer Learning. The rules of the
Ultimatum Game are simple: two agents, the proposer and the responder play the
game interactively. The proposer offers a split of a certain amount with another
agent, the responder. If the responder accepts the offer, both win the amounts
corresponding to the proposer’s offer. Otherwise, neither player gets anything.
8.3.1 Fictitious Play with 2 Agents: A Beginners’ Model in R
Fictitious Play, initially introduced by George W. Brown [15], is a learning
strategy where every player assumes that their opponents are employing unchanging
(potentially mixed) strategies. In this approach, during each iteration, each player
adjusts their strategy in response to the observed historical frequencies of their
opponents’ choices. Fictitious Play belongs to the type of Conscious Learning [13],
a type of learning where we associate meaning to our observations and build beliefs
about relationships and future events.
Here we assume that there are two players, a proposer and a responder in the
Ultimatum Game, using a Fictitious Play type of learning. We created the Fictitious
Play function to simulate the Fictitious Play algorithm. In this implementation the
proposer’s strategy is updated in each iteration, with the strategy being the average
of past offers. The program simulates 1000 iterations and calculates the average
payoffs for both players. The final proposer’s strategy is also displayed. In this
program the Total Amount (T) is the total amount of money to be divided. The
Proposer’s Offer (P) is the amount of money the proposer offers to the responder,
and the Minimum Acceptable Amount (M) is the minimum amount the responder
is willing to accept.
The program has the following pseudocode:

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 195
Algorithm 1 Ultimatum Game with Fictitious Play Learning
| Set total amount to be divided:T |     | ←100.  |     |     |
| -------------------------------- | --- | ------ | --- | --- |
1:
| Set number of iterations:N |     | ←1000.  |     |     |
| -------------------------- | --- | ------- | --- | --- |
2:
3:  Initialize proposer’s strategy vector:a[1..N]←0.
4:  Initialize total payoffs:totalProposerPayoff←0.,totalResponderPayoff←0.
5:  for iterationi=1.to N.do
| 6: Randomly draw offer by proposer:P |     |     | ←sample(1:T).  |     |
| ------------------------------------ | --- | --- | -------------- | --- |
7: Randomly draw responder’s minimum acceptable amount:M ←sample(1:T).
8:  if i≤200. then
| 9: P | ←sample(1:T).{Proposer plays randomly}  |     |     |     |
| ---- | --------------------------------------- | --- | --- | --- |
10: else
| 11: P | ←a[i] .{Proposer uses strategy}  |     |     |     |
| ----- | -------------------------------- | --- | --- | --- |
12:  end if
| 13:  if P | ≥M. then  |     |     |     |
| --------- | --------- | --- | --- | --- |
14: Responder accepts the offer
15: proposerPayoff←P.
| 16: responderPayoff←T |     | −P.  |     |     |
| --------------------- | --- | ---- | --- | --- |
17: else
18: Responder rejects the offer
19: proposerPayoff←0.
20: responderPayoff←0.
21: end if
22: if i<N. then
23: Update strategEy:a[i]←proposerPayoff.
| a[i+1]← | 1 i   | a[j] |     |     |
| ------- | ----- | ---- | --- | --- |
| 24:     | i j=1 | .    |     |     |
25: end if
26: Accumulate total payoffs:
totalProposerPayoff←totalProposerPayoff+proposerPayoff.
27:
totalResponderPayoff←totalResponderPayoff+responderPayoff.
28:
end for
29:
30:  Compute average payoffs:
31: averageProposerPayoff←totalProposerPayoff/N.
32: averageResponderPayoff←totalResponderPayoff/N.
| #  Function  | to  play  the  | Ultimatum  | Game  |     |
| ------------ | -------------- | ---------- | ----- | --- |
totalAmount  <- 100  #  Total  amount  of  money  to  be  split
proposerStrategy<-vector()
proposerStrategy<-0
| #  Number             | of  iterations  | for  Fictitious  | Play        |          |
| --------------------- | --------------- | ---------------- | ----------- | -------- |
| numIterations         | <- 1000         |                  |             |          |
| #  Initialize         | variables       | to  store        | cumulative  | results  |
| totalProposerPayoff   |                 | <- 0             |             |          |
| totalResponderPayoff  |                 | <- 0             |             |          |
#  Initialize  the  proposer’s  strategy,  based  on  an  initial
| C→  proposer   | offer       |            |     |               |
| -------------- | ----------- | ---------- | --- | ------------- |
| #  and defines | the minimum | acceptable | by  | the responder |

196 P. Campos et al.
# both are defined randomly
proposerOffer <- sample (1: totalAmount ,1) # Proposer’s offer
minimumAcceptable<-sample (1: totalAmount ,1)
# Simulate Fictitious Play
for (iteration in 1:numIterations) {
# Play the Ultimatum Game with the current proposer’s strategy
if (iteration <=200) proposerOffer<-sample(1: totalAmount, 1)
C→ else proposerOffer<-proposerStrategy[iteration]
if (proposerOffer >= minimumAcceptable) {
# Responder accepts the offer
proposerPayoff <- proposerOffer
responderPayoff <- totalAmount - proposerOffer
} else {
# Responder rejects the offer
proposerPayoff <- 0
responderPayoff <- 0
}
# Update the proposer’s strategy: average of past offers
if (iteration < numIterations) {
proposerStrategy[iteration]<-proposerPayoff
proposerStrategy[iteration + 1] <- mean(proposerStrategy[1:
C→ iteration])
}
# Accumulate the results
totalProposerPayoff <- totalProposerPayoff + proposerPayoff
totalResponderPayoff <- totalResponderPayoff + responderPayoff
}
# Compute the average results
averageProposerPayoff <- totalProposerPayoff / numIterations
averageResponderPayoff <- totalResponderPayoff / numIterations
# Display the average results and the final proposer’s strategy
cat("Average Proposer’s Payoff:", averageProposerPayoff , "\n")
cat("Average Responder’s Payoff:", averageResponderPayoff, "\n")
cat("Final Proposer’s Strategy:", proposerStrategy[numIterations
C→ ], "\n")
Listing 8.1 Implementation of the Ultimatum Game with Fictitious Play in R
This implementation of the Ultimatum Game with Fictitious Play strategy serves
as an illustrative example of how the game works. It is important to note that the
proposer offer is random in the first 200 runs, since the proposer does not know
the minimum acceptable amount of the responder. After that period, where some
background knowledge is accumulated, the proposer creates a simple strategy by
updating the offers based on the average of the past offers (obtained by the payoffs).

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 197
Fig. 8.1 (a) and( b) Evolution of the proposer offers for the first 500 iterations, based on different
minimum acceptable offers: (a) minimum acceptable offer 85; (b) minimum acceptable offer: 41
In Fig.8.1a and b we can see the evolution of the proposer offers, based on this
strategy for the first 500 iterations. The reason why we chose only the first 500 and
not all the 1000 iterations is because it facilitates visualization, as the proposer offers
remain stable after the 200th iteration.
We can see that on the left Figure (Fig.8.1a) , the strategy for the proposer offer,
based on thepast experience, goes down tozeroafter the200th iteration. Inthiscase,
the minimum acceptable offer for the respondent was 85, a high value (considering
the ceiling of 100). The proposer could not beat this and the return of was very
low. On the right (Fig.8.1b), the proposer offers stabilized near 43, because the
minimum acceptable offer for the respondent was 41. It is therefore possible to see,
in this illustrative example, how learning can be implemented in such a very simple
way in this game.
8.3.2 Reinforcement Learning
In the previous chapters, we applied Reinforcement Learning, a method of Machine
Learning where agents learn an optimal action policy in a sequential decision
process, through repeated experience. Reinforcement Learning algorithms such
as Q-learning or policy gradient methods can be employed to learn the optimal
strategies in the Ultimatum Game. Q-learning involves maintaining a Q-table that
maps state-action pairs to estimated future rewards. Agents update the Q-table
based on the observed rewards and use it to guide their decision-making. Policy
gradient methods, on the other hand, directly learn a policy that maps states to
actions, optimizing it through gradient ascent on the expected cumulative reward.
One important issue in Reinforcement Learning is the fact that we may configure
the way we explore new paths or resort to existing ones. This is called Exploration
vs. Exploitation [16]: agents may need to balance exploration (trying out different
actions to discover optimal strategies) and exploitation (taking the currently known
best action) during learning. Techniques like epsilon-greedy exploration or softmax

198 P.Camposetal.
exploration can be used to control this trade-off. We will use the epsilon-greedy
approach in this work.
With the exploration rate, or epsilon, E incorporated, the Q-learning function,
.
Q(s, a), may be described as follows [16]:
Q(s,a)=(1−α)·Q(s,a)+α·(r +γ ·max(Q(s ' ,a ' ))) ifrandom()<E
. .
(8.1)
Q(s, a) = (1 −α)· Q(s, a)+ α · (r + γ ·max(Q(s ' ,a ' ))) otherwise
(8.2)
In the equations above:
• Q(s, a) represents the current Q-value for the state-action pair (s, a).
• α is the learning rate, which determines how much the new information
.
influences the current Q-value. It typically ranges between 0 and 1, with higher
values giving more weight to the new information.
• r is the immediate reward received after taking action a in state s.
• γ is the discount factor, which determines the importance of future rewards
.
compared to immediate rewards. It is a value between 0 and 1, where higher
values prioritize long-term rewards.
• Q(s’, a’) represents the maximum Q-value among all possible actions a’ in the
next state s’. It represents the estimated future rewards.
• E is the exploration rate, controlling the probability of choosing a random action
.
instead of the greedy action selection. If the random value is less than epsilon,
the agent explores by selecting a random action, and otherwise, it exploits by
selecting the action with the maximum Q-value.
By incorporating the exploration rate E, the Q-learning algorithm balances
.
between exploration (random action selection) and exploitation (selection of the
action with the maximum Q-value) during the learning process. Reinforcement
Learning can be applied to the Ultimatum Game to enable agents to learn optimal
strategies through trial and error, based on received rewards or feedback. A version
of the Ultimatum Game with Reinforcement Learning has been implemented by
[17] that we will use in this work.
8.3.3 Classifiers Systems and Decision Trees
The psychological literature often characterises human beings as Classifiers [13].
The fact is that humans tend to sort things, events and relationships into classes and
act according to their classification. Classifier systems seem to be an adequate tool
for this purpose. There are several different types of Classifiers Systems, such as
Decision Trees, Naive Bayes, Logistic Regression, K-Nearest Neighbor, Artificial
Neural Networks/Deep Learning, Support Vector Machines, etc. All these are a

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 199
belief type of learning inspired in Artificial Intelligence and Biology, where a model
is built according to the background knowledge of previous decisions. In the Chap.1
of this book, we could see that Belief learning is one of the three types of learning
in economic literature, according to [13].
The other two are Non-conscious learning and Routine-based learning. In the
realm of Belief Learning, we gain insights into the principles that regulate our
surroundings and existence. Today, this field primarily falls under the purview of
psychology, specifically under the umbrella of cognitive learning. Here, mental
models and belief learning assume pivotal roles. Belief Learning delves into the
process by which individuals modify and refine their beliefs over time, as they
acquire fresh information or engage with their surroundings.
Focusing on the learning algorithms, a Decision Tree is a non-parametric super-
vised learning algorithm, which is utilized for both classification and regression
tasks. Decision Tree learning is one of the most widely used and practical methods
for inductive inference. It is a method for approximating discrete-valued functions
that is robust to noisy data and capable of learning disjunctive expressions [18].
There are several algorithms for implementing Decision Trees, such as ID3
[19], that learns Decision Trees by constructing them topdown. To define the first
attribute for the tree root, each instance attribute is evaluated using a statistical test
to determine how well it alone classifies the training examples. As a result, the tree’s
root node chooses and utilizes the most optimal attribute as the test. Subsequently,
a descendant node is generated for every potential value of this attribute, and the
training examples are organized into the corresponding descendant nodes. This
entire procedure is then iteratively repeated by considering the training examples
associated with each descendant node to determine the most suitable attribute
for testing at that specific node in the tree. We illustrate the use of a Decision
Tree in the Ultimatum Game using the rpart package, (Recursive Partitioning and
Regression Trees).Recursive partitioning[20],classificationentailstheconstruction
of a Decision Tree with the objective of accurately categorizing individuals within a
population. This is achieved by dividing the population into subgroups using binary
independent variables. The term ‘recursive’ is used because each subgroup can
potentially undergo further divisions repeatedly, until a specific stopping condition
is met to conclude the splitting process. The following program code implements
the rpart package in R with random data.
library(rpart.plot)
# Generate some data
set.seed(123)
n <- 100
data <- data.frame(
proposal = runif(n, 0, 10),
wealth = runif(n, 0, 10),
previous_proposals = runif( n, 0, 10),
accepted = ifelse(runif(n) > 0.5, TRUE, FALSE)
)

200 P. Campos et al.
# Train a Decision Tree Classifier
tree <- rpart(as.factor(accepted) ~ proposal + wealth + previous_
C→ proposals, data = data)
# Plot the tree
rpart.plot(tree)
Listing 8.2 Implementation of the Ultimatum Game with Decision Trees in R
In this example, data is generated by simulating the results of the Ultimatum
Game and a data frame is created with some features of the game: proposal, wealth,
previous proposals, (all varying between 0 and 10) and the outcome (accepted).
The outcome accepted can be True or False and is based on random behavior (the
probability of acceptance is 50 %).
.
We then train a Decision Tree Classifier using these features as predictors and the
outcome as the target variable. The resulting tree (see Fig.8.2) can be interpreted
as a set of rules for accepting (coded as TRUE) or rejecting (coded as FALSE)
proposals based on the values of the predictors. The package rpart.plot has been
used for the graphical representation of the tree.
Although the data has been generated randomly and no interpretation is expected
to be meaningful, we can say that the target variable (accepted) is True when
proposal is above 0.99 and wealth is above 0.47, and above 0.87. Overall, the
percentage of situations where the responder accepts the offer is 36%. The average
of profits in this case is 0.69.
Learned trees can also be represented as sets of if-then rules to improve human
readability. We will present the rules corresponding to a tree in the next example,
later on in this chapter, together with a more realistic scenario.
Fig. 8.2 A representation of the output of a Decision Tree in the Ultimatum Game using rpart
package

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 201
8.3.4 Putting It All Together
In this section we will use different learning strategies, such as Reinforcement
Learning and Belief Learning based on Decision Trees, that have been introduced
earlier in this work, as learning paradigms in the Ultimatum Game. Random
behavior and Fixed behavior are used for benchmark purposes.
The comparison between different learning approaches has been developed by
[21] with the goal of exploring and comparing different learning strategies in the
Ultimatum Game. The program code in R is available in Appendix 1. In their work,
that we partially transcribe here, the Ultimatum Game is played by N agents using a
spatial perspective: the game setup involves a board containing N ×M cells where
.
each player moves randomly across the board. The matches between the various
agents take place when the N agents meet in the same cell. The choice between
Proposer (an Agent A) and Responder (an Agent B) is determined as follows:
Proposer is the agent that moves to a certain position and Responder is the agent
that is already in that same position.
Thus, each agent can assume the role of A (proposer) or B (responder) in each
situation, although never at the same time. The frequencies of the various agent
types (proposer and responder) are similar so, the population is quite balanced in
the game. We consider a population of 5 agents in the board that can move and
face each other to play the game in pairs: proposer/responder. In the following we
describe and compare the different learning approaches used in this comparison.
Random Behaviour
In Random behavior, agents’ decisions are completely random, in the sense that the
proposer chooses the part he wants to split and the respondent decides by chance
whether to accept or reject the proposal with 50% probability. Throughout the game,
the decisions of the proposer and the responder can be changed randomly.
Fixed Behaviour
In Fixed behavior, the agents have a fixed strategy and use it throughout the game:
fair, unfair or random. As for the proposer, he can act in a fair, unfair or random
way. In the fair strategy, the proposer proposes to split the initial amount in order to
offer more than half to the opponent. In the unfair strategy, the opposite happens:
the proposer proposes to split the initial amount in order to offer less than half to the
opponent. The proposer can also act randomly, splitting the initial amount at will. In
the same way, the respondent also acts according to some fixed strategies throughout
the game: he can be fair (he rejects the propositions which are favourable to him),
unfair (he rejects the propositions which are not favourable to him), always accept
or always reject (regardless of the initial offer), or act randomly.
Reinforcement Learning
The Reinforcement Learning version used in this section is based on the work
of [17]. The decision-making process follows an E-greedy policy, which assigns
.
varying importance to exploration and exploitation:

202 P.Camposetal.
• With a probability of1−E, the agent selects the available action with the highest
.
Q-value. This is known as an E-greedy policy, emphasizing exploitation.
.
• With a probability of E, the agent randomly and uniformly selects from the
.
available actions, emphasizing exploration.
By using a greedy policy, the agent tends to exploit its learned information,
favoring actions that have yielded higher rewards in the past. This can lead to
efficient decision-making when the agent has already learned good estimates of the
values associated with different actions in various states.
The parameter E decreases as the iterations progress and more games are played
.
by the agents. This choice is motivated by the fact that in initial encounters, when
players lack extensive prior knowledge about each other, they rely more on random
strategies. The value of the Eparameter evolves following the expression:E =a·x,
. .
where a is a tunable value within the range [0, 1], allowing for faster or slower rate
of decrease.
Lower and upper limits of proposals and acceptance by agents A and B have
been defined as follows:
• The lower limit corresponds to the smallest proportion of the prize considered
acceptable by the responder. In the absence of prior knowledge, the lower limit
is set to a proportion p of the pr ize
• The upper limit is the highest value that proposer A is willing to offer. In the
absence of prior knowledge, the upper limit is set to the total pr ize.
Learning occurs by using the memory property: player A will make a random
offer on a range [0, upper limit] where this upper limit is now defined as the last
accepted offer by player B. The idea is that A will not offer anything more than
B is ready to offer. Similarly, player B will define his lower limit by setting it to
the previous accepted offer. It’s a very basic implementation where it is assumed
that players only look at games between themselves (no observation of third-party
games) and only use the last game as input for the decision and not the whole game
record.
The core program of the Ultimatum Game with Reinforcement Learning, as well
as the other strategies is available in Appendix 1.
Belief Learning using Decision Trees
As stated by [13], Belief Learning requires active thinking and, therefore, cognitive
resources, which are scarce. Decision Trees will be used in this work as a way
that agents use to analyze the outcomes of the simulation and to help them take
decisions. This is a different the situation, compared to the one in Sect.8.3.3, where
the Decision Tree was used at the end of the simulation to analyse the behaviours of
the agents. Here, we will train a Decision Tree Classifier that is used by the agents
to predict whether a proposal will be accepted or rejected based on the amount
proposed, the previous proposals, and other features of the game.

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 203
In belief learning, background knowledge is needed beforehand. Like in the
Fictitious Play of Sect.8.3.1, the proposer does not have any information about
the responder in the first 100 interactions of the game, so the proposer firstly
learns using a different strategy. We chose Reinforcement Learning as the initial
learning paradigm to accumulate some background knowledge. Therefore, for the
first decisions (while there is still no background knowledge), we considered a data
set with recorded decisions coming from Reinforcement Learning: players can do
it in two ways in terms of the background knowledge acquired with Reinforcement
Learning: randomly (with probability E), or epsilon-greedy (with probability 1-E).
. .
In both ways, the two players, A and B play the same way: random-random or
epsilon-greedy-epsilon-greedy.
In Table 8.1, the column Society Gains by game and agent contains the average
gain of the corresponding type of learning, obtained by computing the total gain
divided by the number of games. We also show the profits by agent (the game is
played by 5 agents). We can observe that society gains are higher in Belief Learning.
By comparing the two different Belief Learning strategies used by agents with
Reinforcement Learning as background knowledge, Random-Random provides a
higher gain (almost the double), than the epsilon-greedy—epsilon-greedy strategy.
On the other hand, Reinforcement Learning has low gains. No evaluation procedure
has been taken into account for the different models at this time.
8.4 Learning Involving Multiple Agents in Networks
We consider now that agents are placed in networks. There is a kind of network
awareness of the agents [22]. Thus, the fact that agents are aware of the spatial
proximity of other agents sets up a different form of interaction, allowing us to
create models that are closer to reality, because, in fact, we live in networks and
interact more with those we are closest to (friends, work colleagues, neighbours,
etc.).
The realm of agent learning is undeniably intertwined with network science, as
agents within networks acquire knowledge about both their interaction partners and
their own behavior, [23]. A critical element in models of social interaction is the
underlying network structure that governs how individuals engage with one another.
Numerous studies have delved into the subject of learning within networks, such as
those conducted by [23–27], among others.
Namatame introduced a new concept of collective evolution within a society of
interconnected agents, presenting two distinct approaches to characterize agents’
learning behavior [23]: the Microscopic model (grounded in individual learning)
and the Macroscopic model (centered on social learning). According to [22] agents
evolve through social learning (imitation) and individual learning (mutation). In
individual learning, agents are depicted as having specific behavioral rules, and they
adapt these rules by incorporating existing ones. In ‘classic’ social learning, agents
make decisions based on predefined behavioral guidelines.

204 P.Camposetal.
e
maG
mutamitlUe
ht
ni
seigetartsg
ninrael
tnereffid
fo
nosirapmoC
1.8
elbaT
5
. gAt
fiorP
4.
gAt
fiorP
3.
gAt
fiorP
2.
gAt
fiorP
1.
gAt
fiorP
)tnega
dnae
mag(
sniag
yteicoS
ygetarts
gninraeL
8
00.7027
484.2097
555.6367
688.7546
688.7546
43.69
)modnar-modnar(g
ninraeLf
eileB
3
49.1713
539.9374
111.3194
855.6513
454.8154
83.15
ydeerg-nolispE:
gninraeLf
eileB
5 852.8401
6669.606
1809.216
7056.489
1612.7401
17.11
gninraeLt
nemecrofnieR
6
03.0573
642.6454
572.6934
063.5201
218.1857
23.15
gninraeLf
oe
pyTd
exiF
403.0794
194.8453
320.9904
974.2434
207.9354
07.05
modnaR

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 205
The influence of physical proximity plays a significant role in shaping interac-
tions, as individuals involved in most social processes are more likely to interact
with those in close proximity. The likelihood of interaction diminishes proportion-
ally with the square of the distance between the locations where each individual
resides.
In this section we introduce the possibility of agents to learn in networks. [22]
calltothemodelsbuiltuponcellularautomata the“firstgenerationofnetwork-based
agent-based models”. The “second-generation models” is associated to graphs and
social networks play an important role here. Our approach in this section is merely
illustrative, and its main objective is to write small programs in R that allow us to
understand how agents can learn in networks. We start with belief learning, continue
with Reinforcement Learning and then we extend the idea of network learning by
introducing the concepts of Transfer Learning.
8.4.1 Belief Learning in Networks
A more complex version of the Decision Trees is developed now, considering
that agents (20, in total) are the nodes of a network and play the game with
their neighbours. The network is created following the Barabasi game [28]. The
Barabási–Albert (BA) model is an algorithm for generating random scale-free
networks using a preferential attachment mechanism. The agents are initialized with
some initial endowment (a value taken randomly between 1 and 10). Then, each
agent play the game with all the agents in the neighbourood (all the agents an agent
is connected to). Here the agents do not use any learning mechanism to take their
decisions. Decision Trees are only used to analyse the behaviour of the game as a
whole. The proposer’s offer is randomly generated between 1 and the corresponding
endowment of the proposer. The responder decides whether to accept or reject the
offer, if the offer is greater or equal than half the endowment of the proposer.
In Appendix 3, we provide the R code for the corresponding implementation
of Decision Trees in networks (package igraph is used). A scale-free network is
generated with 20 agents and a function is created to simulate a single instance of
the Ultimatum Game. Then, the agents iterate through edges (potential interactions)
in the network, each agent playing with its neighbours. The game is repeated 10
times and output data is produced. Like before, we used the binary outcome of the
variable Accept (yes/no), as the target feature in the game. As independent features,
we consider all the others: Offer, Proposer-Endowment and Responder-Endowment.

206 P.Camposetal.
model <-rpart(Accept~Offer+Proposer_Endowment+Responder_Endowment
C→ , data=output _table)
Listing 8.3 R syntax for the call of rpart package
The output is the following Decision Tree that can be presented as a set of rules.
n= 190
node), split, n, loss, yval, (yprob)
* denotes terminal node
1) root 190 66 yes (0.3473684 0.6526316)
2) Offer< 1.5 33 0 no (1.0000000 0.0000000) *
3) Offer>=1.5 157 33 yes (0.2101911 0.7898089)
6) Offer< 4.5 99 33 yes (0.3333333 0.6666667)
12) Proposer_Endowment >=4.5 51 18 no (0.6470588 0.3529412)
24) Proposer_Endowment >=8.5 14 0 no (1.0000000
C→ 0.0000000) *
25) Proposer_Endowment< 8.5 37 18 no (0.5135135
C→ 0.4864865)
50) Offer< 3.5 26 7 no (0.7307692 0.2692308)
100) Proposer_Endowment >=6 14 0 no (1.0000000
C→ 0.0000000) *
101) Proposer_Endowment< 6 12 5 yes (0.4166667
C→ 0.5833333) *
51) Offer>=3.5 11 0 yes (0.0000000 1.0000000) *
13) Proposer_Endowment < 4.5 48 0 yes (0.0000000
C→ 1.0000000) *
7) Offer>=4.5 58 0 yes (0.0000000 1.0000000) *
Listing 8.4 Decision tre rules (rpart output)
And to plot the tree, we used the code rpart.plot(model) to obtain the tree in
Fig.8.3.
By analyzing the rules and the tree representation, it is easy to conclude that the
responder tends to reject the offer, every time it is less than 1.5 (in the tree the value
is rounded to 2). There are also other cases for rejection. The responder accepts the
offer when it is above or greater than 2 and when the proposer endowment is less
than 9 (in that case the offer is greater or equal than 4), or less than 5. The offer can
also be accepted in the cases where it is less than 4, and the proposer endowment is
less than 6. When the offer is greater or equal than 5 the responder also accepts the
offer (in 31% of the cases).
We can now evaluate the performance of the tree, by adding the following code:
#evaluation
sampling <- sample(1:nrow(output_table),0.7*nrow(output_table))
data.model <- output_table[sampling,]
data.test <- output_table[-sampling,]
tree <- rpart(Accept ~ .,data.model)
predictions.model <- predict(tree,data.test,type ="class")
m.conf <- table(data.test$Accept,predictions.model)
perc.error <- 100*( m.conf[1,2]+m.conf[2,1])/sum(m.conf)
Listing 8.5 Code for model evaluation

8 Alternative Machine Learning Approaches for an Agent-Based Model of... 207
Fig. 8.3 Output of Decision Tree in the network version
In this code we evaluate the previous Decision Tree model with split validation:
70% of the data is used for the model and the remaining 30% for the test. We then
obtain an error percentage (perc.error) that varies from 3% to 15%. So the model
accuracy varies from 85% to 97%.
8.4.2 Reinforcement Learning in Networks
Reinforcement Learning can be implemented when agents are playing the Ulti-
matum Game in networks by defining the game as a Reinforcement Learning
problem. In the context of the Ultimatum Game, the agents represent the players
who make offers and respond to offers, and the environment represents the game
itself. Depending on the network structure, agents may communicate with each
other to share information or negotiate. The network structure can significantly
impact the dynamics of the game. Agents can use Reinforcement Learning to adapt
their communication strategies. Reinforcement Learning in a networked Ultimatum
Game can be an iterative process. Agents continually update their strategies based
on the outcomes of previous games and the information they receive from other
agents in the network.
One possible application of Reinforcement Learning is Portfolio Management
(see Chap.10). The authors implemented a Multi-Armed Bandit (MAB) algorithm
with Reinforcement Learning (RL) to optimize equity portfolios. Agents learn to
make investment decisions by allocating assets to different financial instruments to
maximize returns while managing risk. The agent is the portfolio manager, and the
environment represents the financial markets. The environment provides the agent
with data on the performance of various financial instruments, such as stocks, bonds,
or other assets, over time.

208 P.Camposetal.
Network analysis can help portfolio managers identify correlations and co-
movements between different assets. Constructing a correlation network can reveal
whichassetstendtomovetogetherandwhichmoveindependently. Thisinformation
can guide portfolio allocation by reducing overexposure to correlated assets, thereby
managing risk more effectively. We can create a graph-based representation of
assets, where assets are nodes, and edges represent various relationships, such as
historical price correlations, sector affiliations, or geographic ties. By analyzing this
graph, Reinforcement Learning agents can make more informed decisions on asset
selection. They can explore potential investment options based on their connectivity
within the network.
The integration of networks into Reinforcement Learning for portfolio manage-
ment enables agents to consider a broader range of information and relationships.
This can lead to more robust and adaptive investment strategies that are better
equipped to navigate complex and interconnected financial markets. However, it
is important to note that the design and implementation of these network-based
approaches require a deep understanding of both Reinforcement Learning and
financial markets.
8.4.3 Transfer Learning
Transfer Learning is the ability of an agent to transfer what it has leaned about
one task to help it perform a different related task [29]. In our work, we do not
distinguish Transfer Learning from knowledge transfer, although we may argue that
these are indeed different tasks. The idea is that an algorithm is able to exploit the
knowledge gained from a previous task to improve generalization about another. For
example, someone might be able to use their knowledge of ping-pong to learn tennis
and badminton. How can this be made in the context of Portfolio Management?
Transfer Learning in Portfolio Management
We can keep in mind the same example of portfolio management to bring now the
ideas of Transfer Learning. In the context of Reinforcement Learning for portfolio
management Transfer Learning involves leveraging knowledge and insights gained
from one investment environment or strategy to improve the performance of another.
One potential idea is to develop pre-trained Reinforcement Learning models
on historical data from similar or related financial markets or asset classes. Then,
knowledge gained by these pre-trained agents can be transferred to a new network
or portfolio management task. The pre-trained agents can serve as a foundation or
background knowledge for learning in the new context.

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 209
Is it also possible to train Reinforcement Learning agents to manage multiple
networks or portfolios concurrently. Each network may have shared or related
features, assets, or goals. Agents can learn from the experiences and strategies of
one network and apply them to another, thus improving their performance in various
contexts.
One important aspect here is that Transfer Learning among agents may also
imply learning from others. Garvin [30] had already touched that point, by stating
that Learning from others involves looking outside the own environment for gaining
new perspectives (best practices, recommendations on how to improve the own
processes or products.
Transferring knowledge involves spreading knowledge quickly and efficiently
in the organization. One approach involves individual agents transferring their
previously acquired knowledge to aid in the execution of another related task. In
this scenario, the same agent leverages its own expertise across multiple tasks. On
the contrary, the concept of learning from others entails the exchange of knowledge
between agents. This dynamic fosters specialization and distributed learning across
various tasks.
Ensembles and Specialization
We may consider to create an ensemble of Reinforcement Learning agents, each
specialized in managing different aspects of portfolio management across various
networks and combine the decisions, predictions, or strategies from these special-
ized agents to make more informed investment decisions in the new network.
In the following example, we start by creating a program in R to simulate
different agents in portfolio management. We use data from Yahoo Finance1 and
simulate Agents, one for stocks and one for bonds, that make decisions to either
“Buy” or “Hold” based on a simple rule: if the closing price increased compared
to the previous time step, they decide to “Buy”; otherwise, they decide to “Hold.”
These decisions are based on a simplistic rule and do not consider a wide range of
factors that are typically considered in portfolio management, such as fundamental
analysis, market sentiment, economic indicators, or risk assessments.
Portfolio allocation in this simulation is equally split between stocks and bonds.
If the stock agent recommends a “Buy,” 50% of the portfolio is allocated to stocks,
and the rest is allocated to bonds. If the bond agent recommends a “Buy,” the
allocation is reversed. This equal allocation strategy is overly simplistic and does
not take into account the risk or correlation between asset classes. In reality,
portfolio allocation is a complex task involving considerations of risk, return,
and diversification. In this initial version, agents do not learn with Reinforcement
Learning or use Transfer Learning, but they are specialized.
# Program to simulate specialized learning in portfolio
C→ management (no Transfer Learning still implemented)
library(quantmod)
1 https://finance.yahoo.com/.

210 P. Campos et al.
# Function to retrieve stock data
get_stock_data <- function(symbol, start_date, end_date) {
data <- tryCatch(
{
data <- getSymbols(symbol, from = start_date, to = end_date
C→ , src = "yahoo", auto.assign = FALSE)
if (is.null(data)) {
stop("Data retrieval failed for symbol ", symbol)
}
return(data)
},
error = function(e) {
cat("Error: Data retrieval failed for symbol", symbol, "\n"
C→ )
return(NULL)
}
)
return(data)
}
# Define the start and end dates
start_date <- "2022-01-01"
end_date <- "2022-12-31"
# Retrieve stock data for AAPL and TLT
stock_data <- get_stock_data("AAPL", start_date, end_date)
bond_data <- get_stock_data("TLT", start_date, end_date)
# Check if data retrieval was successful
if (is.null(stock_data) || is.null(bond_data)) {
cat("Data retrieval failed. Please check the stock symbols and
C→ date range.\n")
} else if (nrow(stock_data) < 2 || nrow(bond_data) < 2) {
cat("Insufficient data for decision-making. At least two data
C→ points are required.\n")
} else {
# Simplified RL agent for stock portfolio
stock_decision <- ifelse(tail(stock_data$Close, 1) > head(stock
C→ _data$Close, -1), "Buy", "Hold")
# Simplified RL agent for bond portfolio
bond_decision <- ifelse(tail (bond_data$Close, 1) > head(bond_
C→ data$Close, -1), "Buy", "Hold")
# Portfolio allocation (simplified for illustration)
stock_allocation <- ifelse(stock_decision == "Buy", 0.5, 0)
bond_allocation <- ifelse(bond_decision == "Buy", 0.5, 0)
# Calculate portfolio performance based on decisions (not
C→ included in this simplified example)
# Print decisions and portfolio allocations
cat("Stock Decision: ", stock_decision, "\n")
cat("Bond Decision: ", bond_decision, "\n")
cat("Stock Allocation: ", stock_allocation, "\n")
cat("Bond Allocation: ", bond_allocation, "\n")

8 Alternative Machine Learning Approaches for an Agent-Based Model of... 211
}
# Check if data retrieval was successful
if (is.null(stock_data) || is.null(bond_data)) {
cat("Data retrieval failed. Please check the stock symbols and
C→ date range.\n")
} else if (nrow(stock_data) < 2 || nrow(bond_data) < 2) {
cat("Insufficient data for decision-making. At least two data
C→ points are required.\n ")
} else {
# Print data for inspection
cat("Stock Data:\n")
print(head(stock_data))
cat("Bond Data: \n")
print(head(bond_data))
}
Listing 8.6 R code to simulate specialized learning in portfolio management (still no Transfer
Learning implemented)
This simulation is a starting point made for illustrative and educational pur-
poses. Real-world portfolio management is far more complex and nuanced, since
professional portfolio managers consider a wide range of factors, conduct in-depth
research, and use advanced tools and models for decision-making.
To improve the idea of creating an ensemble of Reinforcement Learning agents,
each specialized in managing different aspects of portfolio management across
various networks, we should assign the agents to nodes in the network, according to
the following pseudocode.
Algorithm 2 Portfolio Management Pseudocode
1. Retrieve stock data for AAPL and TLT
2. Create
a. Simplified RL agent for bond portfolio
b. Simplified RL agent for stock portfolio
c. Simplified RL agent for CDS portfolio
3. Portfolio allocation
4. Agents exchange learning outcomes with their closest neighbors
5. Calculate portfolio optimization based on decisions
6. Calculate portfolio performance based on decisions
A possible output network is depicted in Fig.8.4, where the layers corresponding
to the different types of agents can be seen represented in different colours.

212 P.Camposetal.
Fig. 8.4 Illustration of specialized agents playing in a network for portfolio management
8.5 Other Forms of Organization and Interaction
in Agent-Based Learning
So far we have focused on learning for agent decision-making and behavior and not
on the ways in which agents organize themselves in order to learn. These have to
do with forms of interaction, hierarchy, systematization, the existence of common
goals, etc.
In this section we are going to broaden the scope of application and go a little
outside the Ultimatum Game and explore the ways in which agents can organize
themselves to make learning more effective, namely knowledge integration, layered
sequential learning, cooperative learning and social learning.
Integrated Learning
Some authors had already thought about ways of learning that can be used in a
multi-agent context. For example, [14] constructed one system that exploits all
the knowledge that is available. The authors call it Knowledge Acquisition via
Knowledge Integration. This method merges several separate theories (also called
knowledge bases), and they we assume that that these will have been generated
by different agents. Ref.[31] explore Systemic Learning, an Integrated Learning
Approach based on the paradigm of Organizational Learning. Systemic learning is
a holistic approach, built upon the five disciplines of the learning organization, as
introduced by Peter Senge in [32]. The main idea of this approach is that the various
learning agents act as different and heterogeneous components of a system that
functions Some authors had already thought about ways of learning that can be used
in a multi-agent context. For example, Ref.[14] constructed one system that exploits
all the knowledge that is available. The authors call it Knowledge Acquisition via
Knowledge Integration.
This method merges several separate theories (also called knowledge bases), and
they we assume that that these will have been generated by different agents. In
[31] Wall and Campos explore Systemic Learning, an Integrated Learning Approach
based on the paradigm of Organizational Learning. Systemic learning is a holistic

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 213
approach, built upon the five disciplines of the learning organization, as introduced
by [32]. The main idea of this approach is that the various learning agents act as
different and heterogeneous components of a system that functions as a whole. Each
component may have different functions, like the organs of the human body.
Layered Learning
Stone and Veloso [33] introduced the concept of layered learning, where typically,
lower level concepts would be learned before learning the concepts higher up.
Basically, Layered learning is a hierarchical Machine Learning paradigm applied
to tasks for which learning a direct mapping from inputs to outputs is intractable
with existing learning algorithms.
Cooperative Learning, Concurrent Learning
Multi-agent learning is the application of Machine Learning to problems involving
multiple agents. This may involve a Single learner, when the agent may commu-
nicate with the other agents, or Multiple learners, with common goals and hence
the aim is to learn to cooperate, or opposing goals and hence the aim is to learn
to compete—and win! So the issue is how can we encourage the agents to learn
to cooperate? Common Learning Methods in Multi-agent Learning include Co-
Evolutionary Algorithms (CEA) that involves joined shared rewards, and the fitness
function is based on interaction with other individuals.
Panait and Luke [34] approach cooperative learning and explore the concepts of
Homogenous and Heterogeneous Team Learning. In Homogenous Team Learning
all agents are assigned identical behaviors, like in Swarm optimization. On the
other hand in Heterogeneous Team Learning the team is composed of agents with
different behaviors and a single learner is trying to improve the team as a whole.
There is also Hybrid Team Learning, where the set of agents is split into squads or
groups, with each agent belonging to one squad and all agents in a squad having the
same behavior. Finally, in concurrent learning, multiple learning processes exist and
attempt to improve parts of the team. Here, typically each agent has its own learning
process to modify its behavior.
For an application of team learning in Business incubators, [35], considers the
relationship among entrepreneurial teams in business incubators (BIETs) and the
relationship between the leader and members of BIETs. The authors investigate how
the learning, forgetting, exit, and entry of Business Incubation and Entrepreneurial
Teams (BIETs) influence their knowledge levels (KL) within diverse environments.
The study encompasses two overarching scenarios that encompass the evolution and
application of knowledge within BIETs and business incubators.
Hoen et al. [36] posit that concurrent learning could be a more appropriate
approach in situations where it is feasible to break down a problem into its
constituent parts, and where there is value in addressing each subproblem to some
extent in isolation. The primary difficulty lies in the fact that every learner is
adjusting its behaviors while interacting with other learners who are also adapting.
In certain studies, these co-adapting learners were treated as a component of
the environment. Key concerns for creating a successful system include credit
assignment and seeking the global optimum.

214 P.Camposetal.
Social Learning, Teaching, Altruism
Social Learning is explored by [37], who develop a general notion of social learning
and the main processes that are responsible for it, namely social facilitation and
imitation. Cognitive models of social action are introduced endowed with mental
properties for pursuing goals and intentions, and for knowledge-based action.
Namatame and Chen [22] approach the behavioral change of individuals affected
by others in a society and call it Social influence. When it is considered in the
context of networks, the degree of social influence is contingent upon numerous
factors, including the intensity of interpersonal connections, the characteristics of
each individual within the networks, the spatial separation between users in the
network, the impact of time, and the attributes of the networks themselves.
In [38], Németh and Takács explore teaching as a process of transferring knowl-
edge, which increases the chances of survival for the recipient while diminishing
the reproductive efficiency of the provider. Through an agent-based simulation, the
authors conduct a comparative analysis of the evolutionary success of genotypes.
Their findings indicate that when individuals possess both teaching and learning
capabilities and they come into contact based on spatial proximity, altruistic teach-
ing becomes evolutionarily advantageous within the population. The settlement of
the population and the accumulation of knowledge emerge as unintended outcomes
of the evolution of altruism.
8.6 Concluding Remarks and Future Research Directions
Agents can be created to learn in various ways and in different contexts. In this
chapter we sought to demonstrate the potential of different types of agent-based
learning in the context of the Ultimatum Game. We carried out an experiment in
which we compared various types of learning (Reinforcement Learning, Decision
Trees and a combination of these), and concluded that societal gains were greater
in Decision Trees in which prior knowledge was based on Reinforcement Learning
with random behaviour.
We then moved on to networks and replicated different learning strategies, such
as Reinforcement Learning and Belief Learning with Decision Trees. We also
approached Transfer Learning, in which the agents are able to exploit the knowledge
gained from a previous task to improve generalization about another. Two important
aspects related to Transfer Learning are ensembles and specialization. These aspects
can be used together or independently. Agents with specialized behaviours can be
combined in an ensemble to simulate scenarios in which different types of agents
with specific knowledge or skills interact with each other. For example, in our
financial portfolio management example, an agent responsible for investing in bonds
could transfer knowledge to the agent responsible for investing in CDS. Although
we have not implemented this possibility, this is an important issue, as interaction
promotes knowledge sharing and decision-making in agent-based models. These
techniques are valuable for improving the robustness, adaptability, and accuracy of

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 215
agent-based simulations, particularly in complex and dynamic environments where
traditional modeling approaches may fall short.
FinallyweexploredKnowledge Integration,LayeredSequentialLearning,Coop-
erative  Learning  and  Social  Learning  as  ways  in  which  agents  can  organize
themselves  to  make  their  learning  better.  There  are  still  a  number  of  avenues  that
can  be  explored  as  a  way  of  enhancing  agent  learning:  We  give  some  questions
and  suggestions  for  further  research  directions,  some  of  which  are  already  being
developed:
•  Considering several agents in which one teaches the others to learn, what is the
role of generative AI in generating agents?
Generative  AI,  which  often  involves  techniques  like  Generative  Adversarial
Networks  (GANs)  or  Variational  Autoencoders  (VAEs),  can  be  employed  to
generate  a  diverse  set  of  agents  with  different  initial  knowledge  or  skill  levels.
These  agents  serve  as  the  individuals  involved  in  the  learning  process.  On  the
other hand, among the generated agents, one is designated as the “teacher” agent.
This  agent  is  typically  more  knowledgeable  or  skilled  in  a  particular  domain
compared  to  the  others.  Generative  AI  helps  in  creating  this  teacher-agent  with
the desired expertise.
•  Is  it  possible  for  an  agent  to  decide  which  is  the  best  way  to  learn?  The
concept  of  an  agent  deciding  the  best  way  to  learn  is  closely  related  to  the
field  of  metalearning.  Metalearning,  also  known  as  “learning  to  learn,”  focuses
on  developing  algorithms,  models,  or  agents  that  can  learn  how  to  adapt  and
improve their learning processes. This is related to the capability for Autonomous
Learning:  an  agent  with  advanced  Machine  Learning  or  artificial  intelligence
capabilities  can  autonomously  assess  and  determine  the  most  effective  learning
strategy based on the task, available data, and its own knowledge and experience.
| Appendix  1: Reinforcement learning function  |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- |
########################################################
| #  (9.3)  ultimatum_game_RL |     |     |     | #   |
| --------------------------- | --- | --- | --- | --- |
#  Return  result  from  Ultimatum  Game  played  with  RL. #
#  The  variables  follow  notation  from  Zhong  et  all. #
########################################################
| ultimatum_game_RL  | <- function(proposer,  |            | responder)  | {   |
| ------------------ | ---------------------- | ---------- | ----------- | --- |
| #  Initialize      | profits                | at  zero.  |             |     |
| proposerProfit     | <- 0                   |            |             |     |
| responderProfit    | <- 0                   |            |             |     |
#  Calculate  the  value  of  epsilon  parameter  in  the  current
| C→  iteration. |                   |     |     |     |
| -------------- | ----------------- | --- | --- | --- |
| epsilon <-     | epsilonDecay^iter |     |     |     |
| # Value of     | prize.            |     |     |     |

| 216 |     |     |     |     |     |     | P. Campos et al.  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- |
N  <- prize
######################################################
| #  What  happened  |           | last   | time  A  played  | B?     |             |     |     |
| ------------------ | --------- | ------ | ---------------- | ------ | ----------- | --- | --- |
| #  Order           | matters,  | A  as  | proposer,        | B  as  | responder.  |     |     |
######################################################
| #  Previous    | decision  |                                         | was  accept  | (1)  or  | reject  | (0).  |     |
| -------------- | --------- | --------------------------------------- | ------------ | -------- | ------- | ----- | --- |
| previousGames  |           | <- games[games$proposerID==proposer@id  |              |          |         |       | &   |
games$responderID==responder@id ,]$
C→  decision
| ifelse(length(previousGames)==0,  |     |     |                                        | previousDecision  |     |     | <- 0, |
| --------------------------------- | --- | --- | -------------------------------------- | ----------------- | --- | --- | ----- |
| C→  previousDecision              |     |     | <- previousGames[length(previousGames) |                   |     |     |       |
C→  ])
#  Last  offer  from  proposer  A  accepted  by  responder  B  (upper
| C→  limit  | for  | the  | proposer).  |     |     |     |     |
| ---------- | ---- | ---- | ----------- | --- | --- | --- | --- |
previousAcceptedOffers  <- games[games$proposerID==proposer@id  &
games$responderID==responder@id
C→  &
games$decision==1,]$offer
| ifelse(length(previousAcceptedOffers)==0,  |     |                                   |     |     |     | upperLim  | <- N, |
| ------------------------------------------ | --- | --------------------------------- | --- | --- | --- | --------- | ----- |
| C→  upperLim                               |     | <- previousAcceptedOffers[length( |     |     |     |           |       |
C→  previousAcceptedOffers)])
| upperLim                 | <- as.numeric(upperLim)  |             |         |                |     |     |     |
| ------------------------ | ------------------------ | ----------- | ------- | -------------- | --- | --- | --- |
| #  Define                | lower                    | acceptance  | limit   | of  responder  |     | B.  |     |
| ifelse(previousDecision  |                          |             | ==  1,  | lowerLim       | <-  |     |     |
C→  previousAcceptedOffers[length(previousAcceptedOffers)],
| C→  lowerLim  |                          | <- p  | *  N  )  |     |     |     |     |
| ------------- | ------------------------ | ----- | -------- | --- | --- | --- | --- |
| lowerLim      | <- as.numeric(lowerLim)  |       |          |     |     |     |     |
#  Number  of  times  played  each  other;  order  is  not  relevant  for
C→  this.
| n  <- nrow(games[games$proposerID==proposer@id  |     |     |     |     |     | &   | games$    |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- |
| C→  responderID==responder@id ,])               |     |     |     |     | +   |     |           |
| nrow(games[games$proposerID==responder@id       |     |     |     |     |     |     | &  games$ |
C→  responderID==proposer@id ,])
#######################################################
#  Q  value  function  definition  for  proposer  A  and  responder  B.
#  a/a’  are  the  actions  and  s  the  state  o f  each  player.
| #  A:  Qa(a)  | action  | a   | is  the  value  | to  | be  offered.  |     |     |
| ------------- | ------- | --- | --------------- | --- | ------------- | --- | --- |
#  B:  Qb(a’,  s)  a’  is  accept/reject  and  s=a  the  offer  from  A.
#######################################################
#  (1)  A:  Chose  the  value  a  that  proposer  A  offers  based  on
| C→  epsilon-greedy  |     |     | policy.  |     |     |     |     |
| ------------------- | --- | --- | -------- | --- | --- | --- | --- |
x  <- runif(1)
| if  (x  <=    | epsilon | ||          | n == 0){ |     |     |     |     |
| ------------- | ------- | ----------- | -------- | --- | --- | --- | --- |
| a <- runif(n  |         | = 1)        | * N      |     |     |     |     |
| proposerBehav |         | <- "random" |          |     |     |     |     |
} else {
| a <- runif(n  |     | = 1,                | min = 0, | max = upperLim) |     |     |     |
| ------------- | --- | ------------------- | -------- | --------------- | --- | --- | --- |
| proposerBehav |     | <- "epsilon-greedy" |          |                 |     |     |     |

8  Alternative Machine Learning Approaches for an Agent-Based Model of... 217
}
| # (2)  A:   | Proposer   |     | A  takes  action  |      | making  this  | offer.  |     |
| ----------- | ---------- | --- | ----------------- | ---- | ------------- | ------- | --- |
| #  (3)  B:  | Responder  |     | B  observes       | its  | own  state    | s.      |     |
s  <- a
#  (4)  B:  Chose  action  a’  from  s  based  on  epsilon-greedy  policy.
x  <- runif(1)
| if  (x  <=  | epsilon  | ||  | n  ==  0){  |     |     |     |     |
| ----------- | -------- | --- | ----------- | --- | --- | --- | --- |
a_l  <- sample(x  =  c("accept",  "reject"),  size  =  1,  prob  =  c
| C→              | (0.5,0.5))  |     |           |     |     |     |     |
| --------------- | ----------- | --- | --------- | --- | --- | --- | --- |
| responderBehav  |             | <-  | "random"  |     |     |     |     |
}  else  {
ifelse  (a  >=  lowerLim,  a_l  <- "accept",  a_l  <- "reject")
| responderBehav  |     | <-  | "epsilon-greedy"  |     |     |     |     |
| --------------- | --- | --- | ----------------- | --- | --- | --- | --- |
}
#  (5)  A,B:  Calculate  the  rewards  for  proposer  A  and  responder  B
C→  .
| if  (a_l  | ==  "accept"){  |     |     |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- | --- | --- |
| ra  <-    | N - a           |     |     |     |     |     |     |
| rb  <-    | a               |     |     |     |     |     |     |
}  else  {
| ra  <- | 0   |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| rb  <- | 0   |     |     |     |     |     |     |
}
| #  (6)  A,B:  | Update  |     | value  function  |     | for  each  | player.  |     |
| ------------- | ------- | --- | ---------------- | --- | ---------- | -------- | --- |
if  (n==0){
| Qa  <- | 0   |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| Qb  <- | 0   |     |     |     |     |     |     |
}  else  {
| Qa  <- | (n-1)/n  | *   | proposer@Q[length(proposer@Q)]  |     |     |     | +  ra/n  |
| ------ | -------- | --- | ------------------------------- | --- | --- | --- | -------- |
Qb  <- (n-1)/n  *  responder@Q[length(responder@Q)]  +  rb/n
}
| proposer@Q   | <-  | as.array(c(proposer@Q,Qa))   |     |     |     |     |     |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | --- |
| responder@Q  | <-  | as.array(c(responder@Q,Qb))  |     |     |     |     |     |
#  Update  the  gains  for  each  player  according  to  the  decision.
| if  (a_l         | ==  "accept")  |     | {                   |     |           |     |     |
| ---------------- | -------------- | --- | ------------------- | --- | --------- | --- | --- |
| responderProfit  |                |     | <- responderProfit  |     | +  a      |     |     |
| proposerProfit   |                | <-  | proposerProfit      |     | +  (N-a)  |     |     |
}
| perc_proposer  |     | <- a  |     |     |     |     |     |
| -------------- | --- | ----- | --- | --- | --- | --- | --- |
ifelse(a_l  ==  "accept",  reaction_responder  <- 1,  reaction_
| C→  responder    |        | <-         | 0)                                  |     |                 |     |       |
| ---------------- | ------ | ---------- | ----------------------------------- | --- | --------------- | --- | ----- |
| ifelse(a_l       | ==     | "accept",  | payoffA                             |     | <- N-a, payoffA |     | <- 0) |
| ifelse(a_l       | ==     | "accept",  | payoffB                             |     | <- a, payoffB   |     | <- 0) |
| # Update         | player | profit.    |                                     |     |                 |     |       |
| proposer@profit  |        | <-         | c(proposer@profit,proposerProfit)   |     |                 |     |       |
| responder@profit |        | <-         | c(responder@profit,responderProfit) |     |                 |     |       |

218 P. Campos et al.
|     | #  Update  | player  | cumulative  |     | profit.  |     |     |     |     |
| --- | ---------- | ------- | ----------- | --- | -------- | --- | --- | --- | --- |
proposer@totalProfit  <- proposer@totalProfit  +  proposerProfit
|     | responder@totalProfit  |            |             | <-  | responder@totalProfit  |                    |     | +   |     |
| --- | ---------------------- | ---------- | ----------- | --- | ---------------------- | ------------------ | --- | --- | --- |
|     | C→  responderProfit    |            |             |     |                        |                    |     |     |     |
|     | #  Return              | the  game  | statistics  |     |                        | and  information.  |     |     |     |
gameStats  <- data.frame(c(proposer@id,  responder@id,  perc_
C→  proposer,  reaction_responder,payoffA,payoffB,  lowerLim,
|     | C→  upperLim ,  |     | proposerBehav,  |     |     | responderBehav))  |     |     |     |
| --- | --------------- | --- | --------------- | --- | --- | ----------------- | --- | --- | --- |
return(list(proposer  =  proposer,  responder  =  responder ,
|     | C→ gameStats |     | =   | gameStats)) |     |     |     |     |     |
| --- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- |
}
| Appendix  |     | 2: Belief learning using Decision Trees  |     |     |     |     |     |     |     |
| --------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
########################################################
| #   | (9.4)  ultimatum_game_BL |     |     |     | - Belief  |     | learning |     | #   |
| --- | ------------------------ | --- | --- | --- | --------- | --- | -------- | --- | --- |
#  Return  result  from  Ultimatum  Game  played  with  BL. #
#  Belief  learning  based  on  Decision  Trees  and  Regression  models  #
########################################################
| ultimatum_game_BL<- |                  |          | function(proposer,    |            |     |     | responder)  | {   |     |
| ------------------- | ---------------- | -------- | --------------------- | ---------- | --- | --- | ----------- | --- | --- |
|                     | #Initialize      | profits  |                       | at  zero.  |     |     |             |     |     |
|                     | proposerProfit   |          | <- 0                  |            |     |     |             |     |     |
|                     | responderProfit  |          | <-                    | 0          |     |     |             |     |     |
|                     | perc_proposer    |          | <<- runif(1,1,prize)  |            |     |     |             |     |     |
if  (iter<=100)  {  #use  data  generated  by  Reinforcement  Learning
g<-read.csv2("games.csv")  #data  obtained  by  Reinforcement
C→
Learning
g<-g[,-1]
g$proposerPayoff<-as.numeric(g$proposerPayoff)
g$responderPayoff<-as.numeric(g$responderPayoff)
g$offer<-as.numeric(g$offer)
g$lowerLim<-as.numeric(g$lowerLim)
g$upperLim<-as.numeric(g$upper)
|     | arvore <<-rpart(decision~.,  |     |     |     |     | g)  |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
reaction_responder<-0
}
|     | if  (iter>100)  |     | {   |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
write.csv2(games,"games2.csv")
g<-games
|     | g<-read.csv2("games2.csv") |          |     |     |     | #data | obtained | by Reinforcement |     |
| --- | -------------------------- | -------- | --- | --- | --- | ----- | -------- | ---------------- | --- |
|     | C→                         | Learning |     |     |     |       |          |                  |     |

8 Alternative Machine Learning Approaches for an Agent-Based Model of... 219
g<-g[,-1]
g$proposerID<-as.numeric(g$proposerID)
g$responderID<-as.numeric(g$responderID)
g$proposerPayoff<-as.numeric(g$proposerPayoff)
g$responderPayoff<-as.numeric(g$responderPayoff)
g$offer<-as.numeric(g$offer)
g$lowerLim<-as.numeric(g$lowerLim)
g$upperLim<-as.numeric(g$upper)
arvore<<-rpart(decision~., g)
reaction_responder<-0
}
# Added for compliance with game saving structure.
# Not significant for random play.
lowerLim <- -99
upperLim <- -99
reaction_responder<<-predict(arvore, data.frame(proposerID=
C→ proposer@id , responderID=responder@id , offer=perc_
C→ proposer, decision=1,proposerPayoff=prize - perc_
C→ proposer,responderPayoff=perc_proposer, lowerlim=
C→ lowerLim, upperlim=upperLim, proposerBehav="epsilon-
C→ greedy", responderBehav="epsilon-greedy"))
proposerBehav<-"epsilon-greedy"
responderBehav<-"epsilon-greedy"
payoffA <- 0
payoffB <- 0
if (reaction_responder == 1) {
decision<-reaction_responder
payoffA <- prize - perc_proposer
responderProfit <- responderProfit + payoffA
payoffB <- perc_proposer
proposerProfit <- proposerProfit + payoffB
}
if (iter>100 & reaction_responder==1) {
decision<-reaction_responder
payoffA <- prize - perc_proposer
responderProfit <- responderProfit + payoffA
payoffB <- perc_proposer
proposerProfit <- proposerProfit + payoffB
}
# Update player profit.
proposer@profit <- c(proposer@profit,proposerProfit)
responder@profit <- c(responder@profit,responderProfit)
# Update player cumulative profit.
proposer@totalProfit <- proposer@totalProfit + proposerProfit
responder@totalProfit <- responder@totalProfit +
C→ responderProfit

220 P. Campos et al.
gameStats <<- data.frame(c(proposer@id, responder@id, perc_
C→ proposer, reaction_responder,payoffA,payoffB, lowerLim
C→ , upperLim, proposerBehav, responderBehav))
return(list(proposer = proposer , responder = responder,
C→ gameStats = gameStats))
}
Appendix 3: Belief learning in networks
#########################################################
# Belief learning in networks #
#########################################################
library(igraph)
# Set the number of agents and create a scale-free network
num_agents <- 20
network<-barabasi.game(num_agents, 1, directed = FALSE)
# Initialize agents with some initial endowment
endowment <- sample(1:10, num_agents, replace = TRUE)
# Function to simulate a single instance of the Ultimatum Game
play_single_ultimatum_game <- function(network, endowment) {
# Create lists to store results
proposer_list <- integer()
responder_list <- integer()
proposer_endowment_list <- integer()
responder_endowment_list <- integer()
offer_list <- integer()
accept_list <- logical()
# Iterate through edges (potential interactions) in the network
for (edge in E(network)) {
proposer <- as.integer(tail(edge))
responders <- neighbors(network, proposer)
# Randomly select a responder from the neighbors
responder <- sample(responders, 1)
# Proposer makes an offer
offer <- sample(1:endowment[proposer], 1)
# Responder decides whether to accept or reject the offer
accept <- offer >= endowment[proposer] / 2
# Append results to lists
proposer_list <- c(proposer_list, proposer)
responder_list <- c(responder_list, responder)
proposer_endowment_list <- c(proposer_endowment_list,
C→ endowment[proposer])

8  Alternative Machine Learning Approaches for an Agent-Based Model of... 221
| responder_endowment_list  |                            |     |                 |     | <- c(responder_endowment_list, |     |
| ------------------------- | -------------------------- | --- | --------------- | --- | ------------------------------ | --- |
|                           | C→  endowment[responder])  |     |                 |     |                                |     |
| offer_list                |                            | <-  | c(offer_list,   |     | offer)                         |     |
| accept_list               |                            | <-  | c(accept_list,  |     | accept)                        |     |
}
| #  Create            | a   | data                | frame  | from                          | the  lists  |     |
| -------------------- | --- | ------------------- | ------ | ----------------------------- | ----------- | --- |
| results              | <-  | data.frame(         |        |                               |             |     |
| Proposer             |     | =  proposer_list,   |        |                               |             |     |
| Responder            |     | =  responder_list,  |        |                               |             |     |
| Proposer_Endowment   |     |                     | =      | proposer_endowment_list,      |             |     |
| Responder_Endowment  |     |                     |        | =  responder_endowment_list,  |             |     |
| Offer                | =   | offer_list,         |        |                               |             |     |
| Accept               | =   | accept_list         |        |                               |             |     |
)
return(results)
}
| #  Number        | of  | game  repetitions  |     |     |     |     |
| ---------------- | --- | ------------------ | --- | --- | --- | --- |
| num_repetitions  |     | <-                 | 10  |     |     |     |
#  Create  a  list  to  store  results  from  each  repetition
| all_results       |                         | <- list()                            |             |        |     |             |
| ----------------- | ----------------------- | ------------------------------------ | ----------- | ------ | --- | ----------- |
| #  Repeat         | the                     | game                                 | multiple    | times  |     |             |
| for  (i           | in  1:num_repetitions)  |                                      |             |        | {   |             |
| results           | <-                      | play_single_ultimatum_game(network,  |             |        |     | endowment)  |
| all_results[[i]]  |                         |                                      | <- results  |        |     |             |
}
#  Create  an  output  table  with  Accept,  Offer,  Gain  (in  accepted
C→  cases),  Proposer  Endowment,  and  Responder  Endowment
| output_table  |     | <- data.frame(  |     |     |     |     |
| ------------- | --- | --------------- | --- | --- | --- | --- |
Accept  =  unlist(lapply(all_results,  function(x)  ifelse(x$Accept
| C→  | ,  "yes",  |     | "no"))),  |     |     |     |
| --- | ---------- | --- | --------- | --- | --- | --- |
Offer  =  unlist (lapply(all_results,  function(x)  x$Offer)),
Gain  =  unlist(lapply(all_results,  function(x)  ifelse(x$Accept,
| C→  | x$Offer,  |     | NA))),  |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --- |
Proposer_Endowment  =  unlist(lapply(all_results,  function(x)  x$
| C→  | Proposer_Endowment)),  |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- |
Responder_Endowment  =  unlist(lapply(all_results,  function(x)  x$
| C→  | Responder_Endowment)) |     |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- |
)
| # Display | the | output | table |     |     |     |
| --------- | --- | ------ | ----- | --- | --- | --- |
print(output_table)

222 P.Camposetal.
References
1. M.A.E. Dehkordi, J. Lechner, A. Ghorbani, I. Nikolic, E. Chappin, P. Herder, Using machine
learning for agent specifications in agent-based models and simulations: a critical review and
guidelines. J. Artif. Soc. Soc. Simul. 26(1), 9 (2023)
2. W. Zhang, A. Valencia, N.-B. Chang, Synergistic integration between Machine Learning and
agent-based modeling: a multidisciplinary review. IEEE Trans. Neural Netw. Learn. Syst. 1–21
(2021)
3. J.C. Harsanyi, On the rationality postulates underlying the theory of cooperative games. J.
Conflict Resolut. 5(2), 179–196 (1961)
4. T.C. Schelling, Dynamic models of segregation. J. Math. Sociol. 1(2), 143–186 (1971)
5. R. Axelrod, The Evolution of Cooperation (Revised ed.) (Perseus Books Group, New York,
2006)
6. T. Brenner, Preface, in Computational Techniques for Modelling Learning in Economics, ed.
by T. Brenner (Springer Science+Business Media, LLC, Berlin, 1999)
7. W. Kwasnleic, Evolutionary models’ comparative analysis methodology proposition based
on selected neo-schumpeterian models of industrial dynamics. ICFAI J. Manage. Econ. I, 02
(2003)
8. P. Stone, M. Veloso, Multiagent systems: a survey from a Machine Learning perspective.
Auton. Robots 8, 345–383 (2000)
9. Y. Shoham, R. Powers, T. Grenager, If multi-agent learning is the answer, what is the question.
Artif. Intell. 171, 365–377 (2007)
10. W. Rand, Machine Learning meets agent-based modeling: when not to go to a bar. Northwest-
ern University, Evanston. Available at: https://ccl.northwestern.edu/papers/agent2006rand.pdf
11. F. Neves, P. Campos, S. Silva, Innovation and employment: an agent-based approach. J. Artif.
Soc. Soc. Simul. 22(1), 8 (2019)
12. C. Angione, E. Silverman, E. Yaneske, Using Machine Learning as a surrogate model for
agent-based simulations. PLoS One 17(2), e0263150 (2022)
13. T. Brenner, Agent learning representation: advice on modelling economic learning, in
Handbook of Computational Economics, ed. by L. Tesfatsion, K.L. Judd, vol. 2 (Elsevier,
Amsterdam, 2006), pp. 895–947
14. P. Brazdil, L. Torgo, Knowledge integration and learning (LIACC Technical Report No. 91-1).
Laboratory of Artificial Intelligence and Computer Science, University of Porto (1991)
15. G.W. Brown, Iterative solutions of games by Fictitious Play, in Activity Analysis of Production
and Allocation, ed. by T.C. Koopmans (Wiley, New York, 1951)
16. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, 2nd edn. (The MIT Press,
Cambridge, 2018)
17. F. Zhong, S.O. Kimbrough, D. Wu, Cooperative agent systems: artificial agents play the
Ultimatum Game. Group Decis. Negot. 11(6), 433–447 (2002)
18. T. Mitchell, Machine Learning (McGraw-Hill Education, New York, 1997)
19. J.R. Quinlan, Induction of decision trees. Mach. Learn. 1(1), 81–106 (1986)
20. L. Breiman, J. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, 1st
edn. (Chapman and Hall/CRC,1984).https://doi.org/10.1201/9781315139470
21. T. Pires, L. Costa, Simulation of organizations based on games and economic behavior:
ultimatum Game. Unpublished work (2021)
22. A. Namatame, S.-H. Chen, Agent-Based Modeling and Network Dynamics (Oxford University
Press, Oxford, 2016)
23. A. Namatame, Collective Intelligence of Networked Agents, vol. 56. Studies in Computational
Intelligence (Springer, Berlin, 2007)
24. M. Özman, Network formation and strategic firm behaviour to explore and exploit. J. Artif.
Soc. Soc. Simul. 11(1) (2007)
25. N. Seltzer, O. Smirnov, Degrees of separation, social learning, and the evolution of cooperation
in a small-world network. J. Artif. Soc. Soc. Simul. 18(4) (2015)

8 AlternativeMachineLearningApproachesforanAgent-BasedModelof... 223
26. H. Xiong, D. Payne, S. Kinsella, Identifying mechanisms underlying peer effects on multiplex
networks. J. Artif. Soc. Soc. Simul. 21(4) (2018)
27. H. Chen, S. Tao, J. Chen, W. Shen, X. Li, C. Yu, S. Cheng, X. Zhu, X. Li, Emergent collective
intelligence from massive-agent cooperation and competition (2023). arXiv:2301.01609.
https://doi.org/10.48550/arXiv.2301.01609
28. A.-L. Barabasi, R. Albert, Emergence of scaling in random networks. Science 286, 509–512
(1999)
29. M. Mitchel, Artificial Intelligence: A Guide for Thinking Humans (Pelican, New Orleans,
2020)
30. D.A. Garvin, Building a learning organization. Harvard Bus. Rev. 71(4), 78–91 (1993)
31. F. Wall, P. Campos, Organizational learning from crises with machine learning and agent-
based models, in Machine Learning Perspectives of Agent-Based Models – With Practical
Applications to Economic Crises and Pandemics with Python, R, NetLogo and Julia, ed. by
P. Campos, A. Rao, J. Margarido (Springer, Berlin, 2025)
32. P.M. Senge, The Fifth Discipline (Doubleday/Currency, New York, 1990)
33. P. Stone, M. Veloso, Layered learning, in Machine Learning : ECML 2000 (Proceedings of
the Eleventh European Conference on Machine Learning ) (Springer, Barcelona, 2000), pp.
369–381
34. L. Panait, S. Luke, Cooperative multi-agent learning: the state of the art, in Autonomous Agents
and Multi-agent Systems, vol. 11 (2005), pp. 387–434
35. W. Wu, S. Ma, K. Wang, S.-B. Tsai, W.-P. Lin, Entrepreneurial team learning, forgetting and
knowledge levels in business incubators: an exploration and exploitation perspective. J. Artif.
Soc. Soc. Simul. 22(1), 10 (2019)
36. P.J. Hoen, K. Tuyls, L. Panait, S. Luke, J.A. La Poutré, An overview of cooperative and
competitive multiagent learning, in Learning and Adaption in Multi-Agent Systems, First
International Workshop, LAMAS 2005, Utrecht, The Netherlands, July 25, 2005, Revised
Selected Papers, ed. by K. Tuyls, P.J. Hoen, K. Verbeeck, S. Sen, vol. 3898. Lecture Notes
in Computer Science (Springer, Berlin, 2005), pp. 1–46
37. R. Conte, M. Paolucci, Intelligent social learning. J. Artif. Soc. Soc. Simul. 4(1) (2001)
38. A. Németh, K. Takács, The evolution of altruism in spatially structured populations. J. Artif.
Soc. Soc. Simul. 10(3), 4 (2007)

Part  IV
| Case  Studies:  | Agent-Based  |           | Learning   |
| --------------- | ------------ | --------- | ---------- |
| and  Crisis     | Using  R,    | Netlogo,  | and  Julia |

Chapter 9
An Agent-Based Epidemic Modeling
in Julia
Ali R. Vahdati
9.1 Introduction
Agent-based models (ABMs) are computational simulations consisting of a set of
autonomous agents that can interact with one another and their environment. ABMs
are a third way of doing science, besides inductive and deductive inference [1].
Inductive inference is finding patterns in data and deriving conclusions given the
observations. Deductive inference follows the reverse path. It starts with a number
of assumptions and tests the consequences of those assumptions. ABMs mix these
two approaches. They start with a number of assumptions about the world (similar
to deduction) but they do not provide theorems (unlike deduction). ABMs produce
observations (simulated data) that can be analyzed inductively, but the data come
from a set of rules instead of the real world (unlike induction). Instead of trying to
understand why specific rules exist, ABMs test whether those rules can produce a
specific pattern we observe.
Because of their power and flexibility, ABMs are specifically helpful for
analyzing complex systems, that is, systems whose behavior is not an aggregate of
its parts but may be emergent and not derived from the basic rules of interaction (e.g.
see [2]). ABMs provide the following advantages to other modeling approaches.
An ABM can be more realistic and less abstract than mathematical models. It
can account for complex, nonlinear, discrete relationships between agents and
their environment, representing empirical observations more closely. ABMs allow
modeling a population of heterogeneous agents living in a heterogeneous and
time-varying environment. Moreover, their flexibility means that different aspects
of a problem (e.g. social, psychological, environmental, biological, etc.) can be
A. R. Vahdati (@)
University of Zurich, Zurich, Switzerland
e-mail: ali@vahdati.info
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 227
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_9

228 A.R.Vahdati
incorporated into the same model. Finally, ABMs can easily combine empirical data
and data from different disciplines.
First ABMs were created in the 1970s [3, 4] but it wasn’t until 1990s that
large-scale ABMs were built thanks to the increased computing power available
to researchers [5]. ABMs have since been used in a wide range of domains, such
as reconstruction of ancient human migrations [6], estimating the effect of climate
change on ancient civilizations [7], disease propagation in social networks [8],
analyzing colonization of plant roots by bacteria [9], effect of alterations to single
cells on multicellular behavior [10], economical modeling [11, 12], and travel
demand and transport modeling [13].
By definition, ABMs can have a large number of model inputs that determine
the rules for agent behaviors and their interactions with one another and the
environment. The exact choice of such rules is not always easy to justify. One
would have to explore a range of parameter values to test the robustness of the
model to changes of each parameter. Additionally, each model parameterization
has to be run with several replicates because of the stochasticity of the model.
This raises a challenge in terms of computational resources and time. Moreover,
the model output is often large and complex, and interpreting it is onerous. These
limitations emphasize the importance of a suitable modeling environment that helps
building models easily, running them in the shortest time possible, and analyzing
their outputs efficiently. A model is not built in a vacuum, but all the other tools
available to build, run and analyze the model and how efficient are those tools matter
for effectively gaining knowledge from an ABM.
This chapter argues for the potential of the Julia language and Agents.jl
framework [6, 14] for agent-based modeling. I assume that the reader is familiar
with programming in general. Some of the advantages of using Agents.jl for agent-
based modeling come from the Julia language and some come from the design of
the Agents.jl package.
9.2 Why Julia Language Is Suitable for Agent-Based
Modeling
In 2009, Viral Shah, Stefan Karpinski, Jeff Bezanson, and Alan Edelman at MIT
started to work on a new ambitious programming language for scientific computing.
They announced the first release of the language, called Julia, in February 2012
[15]. What they aimed for was greedy. They wanted a language that combined the
strengths of several existing languages into a single one:
We want something as usable for general programming as Python, as easy for statistics as
R, as natural for string processing as Perl, as powerful for linear algebra as Matlab, as good
at gluing programs together as the shell.
All these promises and more were satisfied with the release of the version 1.0
in August 2018 [16], marking the language as stable and ready for investment

9 ABMJ 229
of individuals and companies. Ever since, the language has been growing with
an enthusiastic community of developers and users. In 2020, the number of Julia
downloads increased by 87% and the number of packages by 73% [17]. As of this
writing, Julia is among the most popular programming languages (rank 25 on PYPL
[18] and 20 on IEEE 2021 [19]—a 12 step rise since Julia’s version 1 in 2018
[20]). The language has been chosen not only by researchers but also by some of
the biggest companies and projects. Notable examples include the Celeste program
[21, 22] to process 178 terabytes of astronomical images. Using 1.3 million threads
on the Cori supercomputer at National Energy Research Scientific Computing
Center (NERSC), the program reached a performance of 1.54 petaFLOPS [23]
(1.5×1015floating point operations per second). Only three other languages have
.
performed more than a petaFLOPS: C, C++, and Fortran. Julia is the only dynamic
language with a performance close to optimized C. Julia has also been selected by
Climate Modeling Aliance (CliMA) for their next generation climate models [24],
by large insurers for risk modeling [25], by NASA and Brazilian National Institute
for Space Research for simulating Satellites [26], by Pfizer for pharmaceutical
development [27], in Boston for optimizing public school bus system [28], and by
Federal Aviation Administration to develop the Next Generation Airborne Collision
Avoidance System [29].
Julia is free and open source, which makes it accessible to anyone with a
computer and attracts people to contributing to the language and its ecosystem.
A general-purpose programming language, Julia can be used for a broad variety
of domains. This is in contrast to domain-specific languages, such as MATLAB
for numerical computing and Mathematica for symbolic mathematics and technical
computing. As a high-level language, Julia is easy to write and learn, an important
condition for engaging scientists without extensive programming training. A REPL
(read-eval-print loop)1 environment with searchable history, tab-completion, help
and shell modes (by pressing ; or ?) comes with the language and allows to test code
and explore ideas quickly. This is an important feature for scientific computing.
The above features have helped the community to build a rich and fast-evolving
package ecosystem. It currently has more than seven thousand registered packages
[30], many of which are state-of-the-art and actively maintained. These packages
are accessible to users with a powerful package manager built in Julia: Pkg.2
Julia’s package manager makes it trivial to install, update and remove packages.
Moreover, it manages package dependencies (what versions of what other packages
a package depends on) and it can even be configured to keep separate environments
for your different projects, tracking which versions of installed packages work
for your code, and configuring them automatically when you share your code
with others. This helps code reproducibility, an important factor in scientific
programming.Thecodeofascientificprojectoftenneedstobetestedandworkedon
by different people, or even by the original programmer at a future time. Having the
1 https://docs.julialang.org/en/v1/stdlib/REPL/.
2 https://docs.julialang.org/en/v1/stdlib/Pkg/.

230 A.R.Vahdati
dependencies versions tracked and automatically installed, you can be sure that your
code will work anywhere and anytime. It is simple to activate a new environment
with a couple of commands: using Pkg; Pkg.activate("my_env"). Addition-
ally, Pkg has its own REPL interactive interface accessible from within a Julia
session (by typing ]). This further makes package management convenient. Pkg
even integrates with Github. This allows installing unregistered and unpublished
project codes by just pointing to their Github URL.
Having all the ease of access to Julia packages and a thriving ecosystem, one
may still come across functionalities that are absent in current packages or are not
with the same quality as in other languages. This is not a problem as Julia makes
it easy to use functions and code written in other languages. Julia can interact with
some of the most commonly used languagesinscientificcomputing.3 It has builtin
capabilities to call C-exported or Fortran shared library functions (using ccall4 ). It
can also employ code developed in C++ (via Cxx.jl), Python (via PyCall.jl),
R (via RCall.jl), Matlab (via MATLAB.jl), Mathematica (via MathLink.jl),
Objective C (via ObjectiveC.jl), and Java (via JavaCall.jl). Other languages
can also call code developed in Julia. There is Julia’s C API to call Julia from C and
Fortran,5 pyjulia6 for Python, and JuliaCall7 for R.
Julia’s programming paradigm is suitable for collaboration and code reuse. It
promotes composing packages and codes to building new functionality that was not
originally intended by package developers. Julia solves the “expression problem” in
programming. The expression problem was first coined in 1998 [31] (although the
problem was identified earlier in 1975 [32]) and refers to the problem of having to
re-write part of an existing code in order to extend it. The two major programming
paradigms have this problem: the functional programming and object-oriented
programming. Functional programming emphasizes writing programs as much as
possible using functions, in contrast to object-oriented programming in which
classes (objects) are the major level of code organization. Functional programming
makes it convenient to extend the functions of a program. One would not have
to change any previous function to add new ones. But adding new data types
requires changing the previously written classes. In object-oriented programming,
the situation is reverse. Adding new data types doesn’t require rewriting previous
code, but adding a new function requires changing previous written objects. This
problem limits the ability of a community to extend available packages without
having to change them. With the expression problem solved, package authors do
not have to keep specific versions of their dependencies for each specific use case.
And users can extend the packages they use without having to change the original
3 https://github.com/JuliaInterop.
4 https://docs.julialang.org/en/v1/manual/calling-c-and-fortran-code/#Calling-C-and-Fortran-
Code.
5 https://docs.julialang.org/en/v1/manual/embedding/index.html.
6 https://github.com/JuliaPy/pyjulia.
7 https://cran.r-project.org/web/packages/JuliaCall/index.html.

9 ABMJ 231
package (and possibly introduce bugs) or without having to keep a private version
of those packages.
The paradigm that lets Julia solve the expression problem is multiple dispatch.
In multiple dispatch, neither functions are subordinate to objects (object-oriented
programming) nor objects are subordinate to functions (functional programming).
Instead, the compiler chooses an appropriate method (one definition of a function
name) based on the combination of its argument types. Multiple dispatch is different
from function overloading in C++. Overloading is static. It happens at compile-time,
so it only works for types that are already available to the compiler, but multiple
dispatch is dynamic and happens at run-time.
Furthermore, the combination of ease of coding and speed of performance means
Julia has been able to solve the two language problem in programming. The two
language problem8 is having to use two different programming languages for a
single application. A high-level/dynamic language is used for prototyping, such as
Python or R, which is interactive and easy to implement and experiment with, but
too slow to be used for the final application to process large data sets or demanding
execution conditions. Therefore, the final product needs to use a low-level/static
language, such as C/C++, to implement all or only the performance-critical part of
the program that was already implemented with the high-level language. Using two
languages is inefficient, error prone, difficult to maintain and costs time and effort.
Julia solves the two language problem. Although on the surface Julia looks like
interpreted languages like Python, but it is actually a compiled language. Whenever
a function is called for the first time in Julia, the compiler first infers the types and
then Julia’s just-in-time (JIT) compiler creates optimized compiled machine code
before executing the code. Machine code is the lowest level programming language
visible to programmers; it gives specific tasks such as load, store, etc. to CPU.
Therefore, the first time a function is called in Julia, it is slower because it gets
compiled. The second time the function is called, the machine code is executed
directly. Julia is an “optionally typed” language. A “strongly typed” language
(e.g. C/C++) requires the programmer to write the type of all variables and it does
not allow changing the type of a variables during the program run. In dynamically
types languages (e.g. Python), the type can be inferred at run-time and they allow
the type of variables to change during the program run. In Julia, we can specify the
type of variables if we want to, for example to prevent some errors during run-time
or to create methods that work with different types of argument, but we do not have
to. Julia infers the type of function variables and compiles a specialized method for
each combination of variable types before running the code.
Another important feature for running agent-based models is parallel computing.
The world is a complex system where many related events happen at the same
time. Agent-based models are among the least abstract models by modeling
the world closely. This resemblance to reality, in which multiple events happen
at the same time, increases the computational resources needed for the model.
8 https://youtu.be/QTbPtKxDquc.

232 A.R.Vahdati
Therefore, large ABMs often should be to run in parallel. Parallel computing is
when many computations are performed simultaneously. This helps reducing the
computation time of large problems when they can be split into smaller problems.
With parallel computing we save time and money, can tackle larger problems, and
better use available hardware. Julia supports different types of parallel computing
with its standard libraries.9 It supports multi-threading, where multiple processes
use a shared memory, and distributed computing, where multiple processes run in
separate machines with separate memories (e.g. clusters), and GPU computing (see
CUDAnative.jl).
9.3 Developing a Simple ABM in Julia
Conceptually, building an ABM requires at minimum a separate representation of
individual entities. For most, but simplest ABMs, we need an agent type to hold
each agent’s characteristics and to guide its behavior. The type can be complex
by representing different levels/types of individuals. Additionally, we need update
functions that can update the model on possibly three levels (depending on the
complexity of the model): (a) updating agent states with respect to their environment
including other agents, (b) updating agent states with respect to time, and (c)
updating the environment with respect to time and the agents [33].
With that, we can model the following three types of micro-macro level
interactions to fully account for the behavior of a complex system [34]: (a) how
macro level situations (for example, the society) affect agents (for example, the
individuals). (b) how agents make their decisions internally (for example, based on
individual motivations such as happiness), and (c) how agent decisions affect macro
level properties.
In the following, I will build a simple agent-based model that incorporates the
basics of the model and micro-macro level interactions. All the code in this chapter
are available online on Github.10
In Julia, we can use a struct to define a compositetype11 to represent agents.
A composite type is a collection of named fields and is loosely similar to classes
without methods in object-oriented languages. Let’s define a simple agent that only
has an ID and a 2D position. All code is written as if you are working in the REPL.
struct SimpleAgent
id::Int64
x::Int64
y ::Int64
end
9 https://docs.julialang.org/en/v1/manual/parallel-computing/.
10 https://github.com/kavir1698/ABM_in_Julia.
11 https://docs.julialang.org/en/v1/manual/types/#Composite-Types.

9 ABMJ 233
A field of a composite type is represented with a name and its type. With this
definition, we can create separate agents:
agent1 = SimpleAgent(1, 5, 3 )
And access their fields with the . notations:
agent1_id = agent1.id
agent1_pos = (agent1.x , agent1. y)
This agent cannot change its position because struct is immutable. Since
almost always agents change their attributes during a simulation, we need to define
them with mutable struct instead.
9.3.1 A Performance Tip for Defining Composite Types
All types in Julia, whether user-defined or basic (e.g. Int64 or String) are
organized within a hierarchical type system. At the root of this hierarchy is the
abstract type any, which is the supertype of all other types. Types can be classified
into abstract types and concrete types.
Concrete types, such as Int64 or String, can have instances (i.e., you can create
values of these types). On the other hand, abstract types, such as Number or Real,
cannot have instances and are used to group related concrete types.
For example, Int64 is a concrete type that is a subtype of several abstract types
including Signed, Integer, Real, Number, and Any. Conversely, the abstract type
Real is a supertype of both Integer and AbstractFloat. You can explore the
hierarchy of types using the supertype andsubtypesfunctions.
For Julia to generate optimized code, it is crucial to use concrete types in the
fieldsofcompositetypes.Considerthefollowingdefinitionofanagent(Listing9.1):
mutable struct SimpleAgentSlow
id
x
y
end
Listing 9.1 Defining SimpleAgentSlow
This definition can be problematic for performance because the fields id, x, and
y can hold values of any type, hindering the compiler’s ability to optimize access to
these fields.
It would perform poorly because the fields id, x, and y can store values of any
type and the compiler cannot optimize reading objects with this type. Therefore, the
SimpleAgent definition above is a better one. There is, however, a problem with
how we defined SimpleAgent. It’s fields are strictly limited to 64 bit integers. If
we wanted to use 32 bit integers, we would have to create a new type. Defining new
composite types for each permissible concrete type is not a good solution. A naive
solution might be to define the fields to haveabstracttypes(Listing9.2).

234 A. R. Vahdati
mutable struct SimpleAgentSlow2
id::Signed
x::Signed
y ::Signed
end
Listing 9.2 Defining SimpleAgentSlow2
While this improves flexibility, it also compromises performance for the same
reasons as before: the fields do not have concrete types and the required information
is not available in the type. The correct and efficient solution is to define a parametric
composite type (Listing 9.3):
mutable struct SimpleAgentFlexible{T<:Signed}
id::T
x: :T
y::T
end
Listing 9.3 Defining SimpleAgentFlexible
This definition is generic. The fields can store values of any subtype of Signed
(Int128, Int64, Int32, etc.). But when an instance of this type is created, it
automatically chooses a concrete t ype:
ambiguous_agent = SimpleAgentSlow2(1,2,3)
typeof(ambiguous_agent) # SimpleAgentSlow2
agent1 = SimpleAgentFlexible(1,2,3)
typeof (agent1) # SimpleAgentFlexible {Int64}
In this example, SimpleAgentFlexible is a parametric abstract type, but
typeof(agent1) is a concrete type derived from SimpleAgentFlexible. This
approach provides both the flexibility of using different types and the performance
benefits of concrete types.
We can now write a function that updates the agent’s status with respect to time
by changing its position randomly by an integer between-1 and1(Listing9.4).
function move!(agent)
agent.x += rand(-1:1)
agent.y + = rand(-1:1)
end
Listing 9.4 Defining the movement function
When dealing with a single agent type, we can omit specifying the agent type in
the function (e.g., function move(x::SimpleAgentFlexible)...). However,
if we had multiple agent types, such as two different species, we could define
a specific move method for each agent type. The compiler would then select the
correct method based on the input agent type.
Next, we will create a simple environment for the agents to navigate. We can
represent this environment as a matrix of zeros, where each cell initially has a
value of zero. To track the agents’ movements, we can define an update function
that modifies the environment. Whenever an agent enters a cell, the updatefunction

9 ABMJ 235
will change the cell’s value to one, allowing us to keep track of the agent’s visited
locations (Listing 9.5).
| env  =  zeros(Int,          |           | 10,  10)  |         |     |     |
| --------------------------- | --------- | --------- | ------- | --- | --- |
| function  update_env!(env,  |           |           | agent)  |     |     |
| env[agent.x ,               | agent.y]  |           | =  1    |     |     |
end
Listing 9.5  Defining the environment update function
Finally, we can combine all the components and visualize the results. However,
it’s  essential  to  ensure  that  the  agent’s  movements  are  confined  within  the  bound-
aries  of  the  environment,  preventing  it  from  moving  outside  the  designated  space
(Listing 9.6).
| function  move!(agent,  |                 | env)           |     |     |     |
| ----------------------- | --------------- | -------------- | --- | --- | --- |
| agent.x                 | +=  rand(-1:1)  |                |     |     |     |
| agent.y                 | +=  rand(-1:1)  |                |     |     |     |
| envsize                 | =  size(env)    |                |     |     |     |
| if  agent.x             | <  1            |                |     |     |     |
| agent.x                 | =               | 1              |     |     |     |
| elseif  agent.x         |                 | >  envsize[1]  |     |     |     |
| agent.x                 | =               | envsize[1]     |     |     |     |
end
| if  agent .y     | <  1  |                |     |     |     |
| ---------------- | ----- | -------------- | --- | --- | --- |
| agent.y          | =     | 1              |     |     |     |
| elseif  agent.y  |       | >  envsize[2]  |     |     |     |
| agent .y         | =     | envsize[2]     |     |     |     |
end
end
Listing 9.6  Updating the move function to keep agents within the boundaries of the environment
And we can plot the movement of several agents in the environment (Listing 9.7
and Fig. 9.1).
using  CairoMakie
| #  Initialize       | the  | environment  |       | and  multiple  | agents  |
| ------------------- | ---- | ------------ | ----- | -------------- | ------- |
| env  =  zeros(Int,  |      | 100,         | 100)  |                |         |
agents  =  [SimpleAgentFlexible(i,  rand(1:100),  rand(1:100))
| C→  for           | i  in       | 1:10]   |         |     |     |
| ----------------- | ----------- | ------- | ------- | --- | --- |
| #  Run  the       | simulation  |         |         |     |     |
| for  timestep     | in          | 1:200   |         |     |     |
| for  agent        | in          | agents  |         |     |     |
| update_env!(env,  |             |         | agent)  |     |     |
| move!(agent,      |             | env)    |         |     |     |
end
end
| #  Create                  | a  figure  | and  | axis     | for  plotting  |     |
| -------------------------- | ---------- | ---- | -------- | -------------- | --- |
| fig  =  Figure(size=(600,  |            |      | 600),    | aspect=1)      |     |
| ax  =  Axis(fig[1,         |            | 1])  |          |                |     |
| hidespines!(ax)            |            | # #  | Hide the | axis lines     |     |

236 A. R. Vahdati
| hidexdecorations!(ax)    |              | #  No  x-ticks          |
| ------------------------ | ------------ | ----------------------- |
| hideydecorations!(ax)    |              | #  No  y-ticks          |
| #  Plot  the             | environment  | using  a  heatmap       |
| CairoMakie.heatmap!(ax,  |              | env,  colormap=:greys)  |
| #  Save  the             | plot  to     | a  file                 |
save("plots/simple100x100.png",  f ig)
Listing 9.7  Running the simulation and plotting the results
This simple model demonstrates the basic approach to implementing an Agent-
Based  Model  (ABM),  where  distinct  agents  move  independently  and  their  states
change  over  time,  while  the  environment  also  evolves  in  response  to  the  agents’
actions.  However,  real-world  models  are  often  much  more  complex.  Tracking
changes  in  agents  and  the  environment  is  a  more  intricate  task.  Creating  more
Fig. 9.1  Movement path of 10 agents

9 ABMJ 237
sophisticated environments, such as grids with varying boundary conditions, graphs,
maps, and continuous spaces, requires a significant amount of code. Furthermore,
collecting data from the model and agents across multiple simulation runs adds
to the complexity. Writing efficient code and tests for these functionalities can
be a time-consuming process. This is where a modeling framework can provide
significant benefits. By leveraging a framework, scientists without extensive pro-
gramming expertise can build and test ABMs, exploring their ideas without relying
on experienced programmers.
9.4 Agents.jl Modeling Framework
9.4.1 Features of Agents.jl
The Agents.jl framework is a powerful and lightweight tool for building agent-
based models. It has a minimalistic design, requiring users to provide only the
essential components of an ABM, as outlined in the previous section. Specifically,
users need to define at least one agent type and functions that update the agents
with respect to time, environment, and other agents. Optionally, users can also
define functions to update the environment in response to time and/or agents. With
these minimal requirements, the framework enables users to run their models with
minimal additional code.
Agents.jl has a gentle learning curve and is flexible enough to accommodate
a wide range of ABMs (see the examples on its documentation12 ). Moreover, it
is a high-performance framework that outperforms some established packages, as
demonstrated in the comparison section of the Agents.jl documentation, which
benchmarks it against Mesa [35] and NetLogo [36]. The framework is actively
maintained, and new features are added in response to user requests. If you
encounter any issues or niche cases not implemented in the package, you can expect
prompt feedback.
Agents.jl offers the following features that help agent-based modeling:
• Ecosystem integration: Agents.jl offers seamless integration with other packages
within the Julia ecosystem, empowering modelers to create complex and com-
prehensive models. By combining Agents.jl with other packages, modelers can
leverage a wide range of capabilities, including: solving differential equations
to model dynamic systems, optimizing model parameters for better accuracy,
modeling complex networks and relationships, propagating errors to quantify
uncertainty, and visualizing models interactively to gain deeper insights.
• Mixed-agent models: Agents.jl is capable of handling models that feature
multiple agent types without compromising on performance.
12 https://juliadynamics.github.io/Agents.jl/dev/examples/.

238 A.R.Vahdati
• Various built-in spaces: Multiple built-in spaces are available, each with their
corresponding functions. Specifically, the following space types can be created,
and agents can be added to, moved within, or removed from them using built-in
functions:
– Grid space: grids are regular, discrete spaces that can have any number of
dimensions, with either periodic or fixed boundaries. These grids have their
own built-in “distance metric”, which defines the neighborhood of individual
agents. Specifically, this distance metric can be set to either :chebyshev,
which considers all positions withina hypercube centered at the focal position,
or :euclidean, which considers all positions within a Euclidean distance
from the focal position.
– Graph space: graphs are discrete spaces that can take on any arbitrary shape.
Notably, graphs are mutable when used in conjunction with the Agents.jl
package. Furthermore, all space-agent interaction functions are compatible
with graphs.
– Continuous space: in this space, agents can occupy non-discrete positions
in any dimensionality. Continuous space supports both periodic and fixed
boundaries, and allows agents to move with changing velocities.
– OpenStreetMap: maps from OpenStreetMap [37] can be imported as a
network of roads on which agents move. The maps have meta-data such as
street directions, speed limits, and types of ways (e.g. highway, street, etc.).
• Agent management helper functions: the package provides functions for the
following agent management tasks:
– Creating agents: add_agent! creates a new agent with given attributes and
adds it to any of the several space types at specific or random positions.
– Accessing agents: tools for quickly accessing agents by their ids (using
model[id]), picking a random agent (random_agent), getting the total
number of agents (nagents), and an iterator over all the agents (allagents)
or ids (allids).
– Moving agents: move_agent! moves an agent to a specific or random
position in discrete spaces or moves the agent forward according to its velocity
in the continuous space.
– Removing agents: remove_agent! and remove_all! to remove single or
all agents, respectively, from the model and the space.
– Resampling agents: the sample! function replaces all agents by sampling
n times from the existing ones with or without replacement and by giving
weights to each agent according to one of its attributes.
– Search agent neighborhoods: tools for local neighborhood search.
nearby_ids returns the ids of other agents within a radius r of an
agent/position in the space. It performs differently based on the underlying
space type. Other functions include nearby_positions for all neighboring
positions in discrete spaces, nearby_agents for an iterator over nearby
agents, and euclidean_distance for returning the euclidean distance
between twoagentsorpositions.

9 ABMJ 239
– Agent-agent interactions: tools for pairwise or multi-agent interactions. For
example, elastic_collision! updates the velocity of two agents colliding,
and iter_agent_groups returns an iterator of groups of agents of a given
size.
• Flexible data collection: data collection is a key feature, allowing for easy
and powerful data gathering during simulations. The high-level run! function
enables the collection of any agent or model property, as well as summary
statistics, at specified time intervals. The collected data is then organized into
tables in the DataFrame format. For even more control over data collection, users
can utilize lower-level functions, which are used to build the run! function, to
customize their data gatheringneeds.
• Parameter exploration: parameter exploration is facilitated through the
paramscan function, which automatically generates and runs simulations (with
optional parallel processing) across a specified set of parameter ranges. This
allows for exhaustive testing of all possible parameter value combinations.
• Optional agent activation order: at each time step, agents can be activated in
different orders, allowing for flexible simulation scenarios. Agents.jl provides a
range of built-in schedulers, including: random_activation for random order-
ing, fastest for optimizing performance, partial_activation for activating
a random fraction of agents, property_activation for ordering agents based
on a specific attribute, and by_type for models with multiple agent types.
Furthermore, users can easily create custom schedulers by defining a simple
function that takes an ABM as input and returns an iterator overagents.
• Visualization: abmplot is a general plotting function. It creates a scatter plot
of agents while allowing to modify all aspect of the plot, such as agent size,
color, and shape. Moreover, since the outputs of simulations are organized in
DataFrames, they can be easily used with DataVoyager.jl (a data exploration
tool for quickly visualizing tabular data) for other types of plots and data
exploration.
• Interactive application: The same abmplot function provides is an easy way to
launch an interactive application where the user can visualize the progress of the
model and run it interactively (Fig.9.2).
9.4.2 An Epidemic Agent-Based Model
In this example, I demonstrate how Agents.jl can be used to build a disease
propagation model, specifically a SIRD (susceptible, infected, recovered, deceased)
model, in the context of a city. The individuals move around the city, arriving
at their destinations at different times. When an infected person is present in a
public place, others are at risk of infection based on the transmission rate from
the infected individual. Once infected individuals are detected, they are isolated
after a certain number of days, preventing them from moving or infecting others.

240 A.R.Vahdati
Fig. 9.2 InteractivemodelinginAgents.jl. Theplots shows how anABMmayberuninteractive.
Sliders determine how fast the model runs and can also change model properties during the run
The model illustrates the spread of the disease and how detection and quarantine
measures affect its progression.
The OpenSteetMapSpace is a powerful tool for modeling cities as
networks of roads. In this example, I have chosen a small area of Zurich,
Switzerland. To get started, you can download the map of any city using the
Agents.OSM.download_osm_network function. Alternatively, you can download
small areas of any city using the export function from openstreetmap.com or, for
larger scales, whole cities and countries from planet.openstreetmap.com.
We start by first defining an agent type using the @agent macro. This macro
automatically adds necessary fields based on the given space type, such as ID and
position fields, so that we do not have to add them. Here, we specify that we
want an OSMAgent. We just need to add fields that are specific to our simulation.
days_infected counts how many days an individual has been infected, status
is the compartment of the individual (:S for susceptible, :I for infected, :R for
recovered, and :D for infected and detected), β is transmission probability of the
.
disease from an infected to a susceptible individual, and fav_places is a list of
public places an individual keeps visiting (Listing9.8).
using Agents
@agent struct Person(OSMAgent)
destination::Tuple{Int,Int,Float64}
days_infected::Int
status::Symbol
::Float64
fav_places ::Vector{Int}
end
Listing 9.8 Defining an agent type for the OpenStreetMap space

9 ABMJ 241
Fig. 9.3 Initial distribution of agents on the map
Next, we need to define a model object and update functions for the agents
and the model. The following are parameters of the model that can be changed
and analyzed. n_public_places is the total number of public places in the city,
map_path shows the path to the map file, infection_period is how many days
it takes to recover from the infection, detection_time is how many days it
takes for an infection to be detected, reinfection_probability determines the
probability to get the infection again after being recovered, detected_movement
is the fraction of individuals that violate their quarantine and keep moving around,
death_rate is the probability of death due to the infection, N is the initial
population size, initial_infected istheinitialnumberofinfectedindividuals,β
.
is transmission probability of the infection, n_fav_places is the number of public
places each individual keeps visiting, speed is how many kilometers an individual
movespermodelstep, move_probistheprobabilityofmovingtoanotherplaceafter
arriving there, transmission_radius defines the radius around infected agents in
km within which the disease can be transmitted to others, and seed is a seed for
random number generator of the model.
We can build the space by just providing the path of the map fil e to
OpenStreetMapSpace (Listing 9.9). And the model object is created with the
StandardABM function, receiving the agent type, space, and a dictionary of model
properties that we will use in the update functions. We can then add agents to the
model by placing them on a random road on the map (Fig.9.3) and giving them
each their favorite public places to visit.
function initialize(;
n_public_places = 15,
map_path = "data/zurich_oerlikon.osm ",
infection_period = 20,

242 A. R. Vahdati
| detection_time  | =  3,  |     |
| --------------- | ------ | --- |
reinfection_probability =  0.05,
| detected_movement  | =  0.1,   |     |
| ------------------ | --------- | --- |
| death_rate         | =  0.03,  |     |
N  =  200,
| initial_infected  | =  40,  |     |
| ----------------- | ------- | --- |
=  0.1,
| n_fav_places         | =  3,       |     |
| -------------------- | ----------- | --- |
| speed  =  0.1,       | #  km/step  |     |
| movement_prob        | =  0.05,    |     |
| transmission_radius  | =  0.05,    |     |
seed  =  1234
)
m  =  OpenStreetMapSpace(map_path)
| model  =  StandardABM(Person,  | m,  |     |
| ------------------------------ | --- | --- |
properties=Dict(
| :public  =>        | Vector{Tuple{Int64,Int64,Float64}}(),  |     |
| ------------------ | -------------------------------------- | --- |
| :n_public_places   | =>  n_public_places,                   |     |
| :infection_period  | =>  infection_period,                  |     |
| :detection_time    | =>  detection_time,                    |     |
:reinfection_probability  =>  reinfection_probability,
| :death_rate         | =>  death_rate,         |     |
| ------------------- | ----------------------- | --- |
| :speed  =>          | speed,                  |     |
| :movement_prob      | =>  movement_prob,      |     |
| :detected_movement  | =>  detected_movement,  |     |
:transmission_radius  =>  transmission_radius
),
| agent_step!  | =  sir_step!,  |     |
| ------------ | -------------- | --- |
rng=Random.MersenneTwister(seed)
)
| model.public  | =  [random_position(model)  | for  i  =  1: |
| ------------- | --------------------------- | ------------- |
C→  n_public_places]
| for  ind  in  | 1:N                                    |                |
| ------------- | -------------------------------------- | -------------- |
| start  =      | random_position(model)                 |                |
| fav_places    | =  rand(1:n_public_places,             | n_fav_places)  |
| finish  =     | deepcopy(model.public[fav_places[1]])  |                |
agent  =  add_agent!(start,  model,  finish,  0,  :S,  ,  fav_places)
| plan_route!(agent,  | agent.destination,  | model)  |
| ------------------- | ------------------- | ------- |
end
| for  inf  in  | 1 :initial_infected |     |
| ------------- | ------------------- | --- |
model[inf].days_infected = 1
| model[inf].status | = :I |     |
| ----------------- | ---- | --- |
end
return model
end
Listing 9.9  A function to initialize the model

9 ABMJ 243
We can use the OSMMakie package to plot the distribution of agents on the map
(Listing9.10 and Fig. 9.3).
using  CairoMakie
using  OSMMakie
| "Define  agent  color"  |     |     |     |
| ----------------------- | --- | --- | --- |
function  ac(agent)
| if  agent.status  | ==  :I  |     |     |
| ----------------- | ------- | --- | --- |
return  :red
| elseif  agent.status  | ==  :S  |     |     |
| --------------------- | ------- | --- | --- |
return  :blue
| elseif  agent.status  | ==  :D  |     |     |
| --------------------- | ------- | --- | --- |
return  :black
else
return  :green
end
end
| "Define  agent  shape"  |     |     |     |
| ----------------------- | --- | --- | --- |
function  am(agent)
| if  agent.status  | ==  :I  |     |     |
| ----------------- | ------- | --- | --- |
return  :utriangle
| elseif  agent.status  | ==  :S  |     |     |
| --------------------- | ------- | --- | --- |
return  :circle
else
return  :rect
end
end
#  Create  a  model
| model  =  initialize(    | =0.9,  initial_infected=20,  |                      |         |
| ------------------------ | ---------------------------- | -------------------- | ------- |
| detected_movement=0.05,  | detection_time=5,            |                      | N=200,  |
| infection_period=15 ,    | speed=0.4,                   | movement_prob=0.05,  |         |
n_public_places=15,  n_fav_places=4,  transmission_radius=1,  seed
C→  =9977)
| #  Plot  the  map  with  | agents  |     |     |
| ------------------------ | ------- | --- | --- |
p  =  abmplot(model,  agent_color=agent_color,  agent_marker=
C→
| agent_marker,                | agent_size=8) |       |     |
| ---------------------------- | ------------- | ----- | --- |
| save("sir_initial_dist.png", |               | p[1]) |     |
Listing 9.10  Plotting the initial distribution of agents on the map. Infected individuals are red
As the last step of building this model, we need to define update functions. Each
individual  moves,  its  infection  progresses  if  they  have  infection,  and  transmit  the
infection  to  other  individuals.  We  can  write  a  function  for  each  of  these  updates.
You can then put them all in a single function (Listing 9.11) that accepts two inputs:
an agent and the model. Agents.jl will use this function and apply it to all agents at
each step.

244 A.R.Vahdati
| function           | sir_step!(agent,  | model)  |     |     |
| ------------------ | ----------------- | ------- | --- | --- |
| transmit!(agent,   |                   | model)  |     |     |
| update!(agent,     |                   | model)  |     |     |
| sir_move !(agent,  |                   | model)  |     |     |
end
Listing 9.11  Defining a step function
Individuals  move,  unless  they  are  in  quarantine  (:D detected)  and  obey  the
quarantine rules. Once they arrive at their destination, they move to the next favorite
place with movement_prob probability(Listing9.12).
| function  sir_move!(agent,  |     | model)                       |     |           |
| --------------------------- | --- | ---------------------------- | --- | --------- |
| if  agent.status            | ==  | :D  &&  rand(abmrng(model))  |     | >  model. |
C→  detected_movement
return
end
| if  !is_stationary(agent,  |     | model)  |               |     |
| -------------------------- | --- | ------- | ------------- | --- |
| move_along_route!(agent,   |     | model,  | model.speed)  |     |
elseif  is_stationary(agent,  model)  &&  rand(abmrng(model))  <=
C→  model.movement_prob
| #  make  sure    | the  | agent  does  choose            | the  same  | place  |
| ---------------- | ---- | ------------------------------ | ---------- | ------ |
| fav_places_copy  |      | =  deepcopy(agent.fav_places)  |            |        |
deleteat!(fav_places_copy,  findfirst(x ->  model.public[x]  ==
| C→  agent .destination,   |     | fav_places_copy))                       |              |     |
| ------------------------- | --- | --------------------------------------- | ------------ | --- |
| agent.destination         |     | =  model.public[rand(fav_places_copy)]  |              |     |
| plan_route!(agent,        |     | agent.destination,                      | model)       |     |
| move_along_route!(agent,  |     | model,                                  | model.speed) |     |
end
end
Listing 9.12  Defining the agent movement function
We update how many days infected individuals have been infected. At the end of
their infection period, they die with probability death_rate (Listing 9.13).
| function  update!(agent,  |     | model)                  |         |     |
| ------------------------- | --- | ----------------------- | ------- | --- |
| if  agent.status          | ==  | :I  ||  agent.status    | ==  :D  |     |
| agent.days_infected       |     | +=  1                   |         |     |
| if  agent.days_infected   |     | model.infection_period  |         |     |
| if  rand(abmrng(model))   |     | model.death_rate        |         |     |
| remove_agent!(agent,      |     | model)                  |         |     |
else
| agent.status         |     | =  :R  |     |     |
| -------------------- | --- | ------ | --- | --- |
| agent.days_infected  |     | =  0   |     |     |
end
elseif  agent.days_infected  >=  model.detection_time  &&  agent.
| C→  status    | ==  | :I  |     |     |
| ------------- | --- | --- | --- | --- |
| agent .status | =   | :D  |     |     |
end
end
end
Listing 9.13  Defining the agent update function

9  ABMJ   245
Finally,  infected  individuals  transmit  the  infection  to  other  individuals  that  are
in the same public place. For this concept, we can use multiple dispatch and write
two  methods  (Listing  9.14).  The  first  method  checks  whether  the  focal  individual
is  infected  and  if  so,  finds  all  other  individuals  in  its  neighborhood.  The  second
method,  works  on  pairs  of  individuals  and  transmits  the  infection  to  the  second
individual with a probability depending on whether they are healthy or recovered.
| function  transmit!(agent::AbstractAgent,  |     |                           |     | model::ABM)  |
| ------------------------------------------ | --- | ------------------------- | --- | ------------ |
| if  agent.status                           |     | !=  :I  &&  agent.status  |     | !=  :D       |
return
end
| for  neighbor  | in  | nearby_agents(agent,  |     | model,  model. |
| -------------- | --- | --------------------- | --- | -------------- |
C→
transmission_radius)
| transmit!(agent,  |     | neighbor,  | model)  |     |
| ----------------- | --- | ---------- | ------- | --- |
end
end
function  transmit!(infected::AbstractAgent,  a2::AbstractAgent,
C→
model::ABM)
| if  a2.status  | ==  | :I  ||  a2.status  | ==  | :D  |
| -------------- | --- | ------------------ | --- | --- |
return
elseif  a2.status  ==  :R  &&  rand(abmrng(model))  >  model.
C→
reinfection_probability
return
| elseif  rand(abmrng(model))  |     |     | >  infected.  |     |
| ---------------------------- | --- | --- | ------------- | --- |
return
else
| a2.status | = :I |     |     |     |
| --------- | ---- | --- | --- | --- |
end
end
Listing 9.14  Defining the disease transmission function
This  is  all  the  code  that  we  needed  to  write  to  define  this  not-so-simple  model.
To run the model, we initialize a model object and call the step! function and the
number of steps(Listing9.15).
| model  =  initialize(β=0.1,  |       |     | initial_infected=80,  |     |
| ---------------------------- | ----- | --- | --------------------- | --- |
| detected_movement=0.05,      |       |     | detection_time=10)    |     |
| step !(model,                | 100)  |     |                       |     |
Listing 9.15  How to initialize and run the model for 100 steps
To  run  the  model  and  collect  data,  we  need  to  decide  what  kind  of  information
to  collect.  Let’s  track  the  number  of  individuals  at  each  compartment  :I,  :D,  :S,
and :R. To that end, we can write functions that get the model object as input and
calculate the desired statistics (Listing 9.16).
nS(model)  =  count(a ->  a.status  ==  :S,  allagents(model))
nI(model)  =  count(a ->  a.status  ==  :I,  allagents(model))
nR(model)  =  count(a ->  a.status  ==  :R,  allagents(model))
nD (model)  =  count(a ->  a.status  ==  :D,  allagents(model))
Listing 9.16  Data collection functions

246 A. R. Vahdati
The run! function from Agents.jl runs the model and collects data into
DataFrames. It collects from two sources: the agents and the model. We do not
need to collect data from agents to get the distribution of different compartments,
so we only provide the mdata (for model data) argument(Listing9.17).
model = initialize( =0.9, initial_infected=20,
detected_movement=0.05, detection_time=5, N=200,
infection_period=15, speed=0.4, movement_prob=0.05,
n_public_places=15, n_fav_places=4, transmission_radius=1, seed
C→ =9977)
nsteps= 1000
_, mdata = run!(model, sir_step!, nsteps, mdata = [nS, nI, n R,
C→ nD])
Listing 9.17 Running the model for 1000 steps and collecting data
The simulation takes a few seconds and gives us a data-frame with the size of
compartments at each step:
1001×5 DataFrame
Row time nS nI nR nD
Int64 Int64 Int64 Int64 Int64
1 0 180 20 0 0
2 1 96 104 0 0
3 2 64 136 0 0
4 3 64 136 0 0
998 997 26 0 149 0
999 998 26 0 149 0
1000 999 26 0 149 0
1001 1000 26 0 149 0
Now we can plot the change in compartment sizes (Fig. 9.4).
using CairoMakie
fig = Figure();
ax = Axis(fig[1, 1], xlabel="Step", ylabel="Count")
lines!(ax, 0:nsteps, mdata.nS, color=:blue, label="S")
lines!(ax, 0:nsteps, mdata.nI, color=:red, label="I")
lines!(ax, 0:nsteps, mdata.nR, color=:green, label="R")
lines!(ax, 0:nsteps, mdata.nD, color=:orange, label="D")
# Add a legend
leg = Legend(fig[1, 2], ax , "SIR Model")
fig[1, 1] = ax
# Save the figure
CairoMakie.save("sir_15.png", fig)

9 ABMJ 247
Fig. 9.4 Size of different compartments with 15 public places in the city
A surprising observation from this simulation is that some individuals remain
unexposed to the disease throughout the entire process. Furthermore, the disease
eventually disappears from the population. If the number of public places is reduced,
the disease is more likely to persist in the population, as infected individuals have a
higher chance of transmitting the disease to others (Fig. 9.5).
9.5 Conclusion
The Julia language offers a unique environment for scientific computing, com-
bining the strengths of various languages. Its key features—high performance,
expressibility, and extendibility—make it an ideal choice for agent-based modeling.
The Agents.jl framework, built on Julia, leverages these advantages to provide
a modeling environment that is easy to learn, high-performance, and seamlessly
integratable with other packages. Additionally, Agents.jl offers flexibility and power
in designing diverse models, all while requiring minimal code from the user. As
a result, building agent-based models in Agents.jl is a productive path for both
researchers with limited programming experience and seasoned programmers alike.

248 A.R.Vahdati
Fig. 9.5 Size of different compartments with 5 public places in the city
References
1. R. Axelrod, The Complexity of Cooperation: Agent-based Models of Competition and
Collaboration (Princeton University Press, 1997)
2. S. Schweighofer, D. Garcia, F. Schweitzer, An agent-based model of multi-dimensional
opinion dynamics and opinion alignment. Chaos Interdiscip. J. Nonlinear Sci. 30(9), 093139
(2020)
3. T.C. Schelling, Dynamic models of segregation. J. Math. Soc. 1(2), 143–186 (1971)
4. D.B. Botkin, J.F. Janak, J.R. Wallis, Some ecological consequences of a computer model of
forest growth. J. Ecol. 60(3), 849 (1972)
5. J.M. Epstein, R. Axtell, Growing Artificial Societies: Social Science from the Bottom Up
(Brookings Institution Press, 1996)
6. A.R. Vahdati, J.D. Weissmann, A. Timmermann, M.S. Ponce de León, C.P.E. Zollikofer,
Drivers of Late Pleistocene human survival and dispersal: an agent-based modeling and
machine learning approach. Q. Sci. Rev. 221, 105867 (2019)
7. A. Angourakis, J. Bates, J.P. Baudouin, A. Giesche, M.C. Ustunkaya, N. Wright, R.N. Singh,
C.A. Petrie, How to ‘downsize’ a complex society: an agent-based modelling approach to
assess the resilience of Indus Civilisation settlements to past climate change. Environ. Res.
Lett. 15(11), 115004 (2020)
8. B. Khan, K. Dombrowski, M. Saad, A stochastic agent-based model of pathogen propagation
in dynamic multi-relational social networks. Simulation 90(4), 460–484 (2014)
9. A.L. Muci, M.A. Jorquera, Á.I. Ávila, Z. Rengel, D.E. Crowley, M. de la Luz Mora. A
combination of cellular automata and agent-based models for simulating the root surface
colonization by bacteria. Ecol. Model. 247, 1–10 (2012)

9 ABMJ 249
10. G. Letort, A. Montagud, G. Stoll, R. Heiland, E. Barillot, P. Macklin, A. Zinovyev, L. Calzone,
PhysiBoSS: a multi-scale agent-based modelling framework integrating physical dimension
and cell signalling. Bioinformatics 35(7), 1188–1196 (2019)
11. A. Botta, E. Caverzasi, A. Russo, M. Gallegati, J.E. Stiglitz, Inequality and finance in a rent
economy. J. Econ. Behav. Org. 183, 998–1029 (2021)
12. T.R.E. dos Santos, M.I. Nakane, Dynamic bank runs: an agent-based approach. J. Econ.
Interaction Coord. 16, 675 (2021)
13. W. Scherr, P. Manser, C. Joshi, N. Frischknecht, D. Métrailler, Towards agent-based travel
demand simulation across all mobility choices - the role of balancing preferences and
constraints. Eur. J. Transp. Infrastruct. Res. 20(4), 152 (2020)
14. G. Datseris, A.R. Vahdati, T.C. DuBois, Agents.jl: a performant and feature-full agent-
based modeling software of minimal code complexity. Simulation 100(10), 003754972110688
(2022)
15. J. Bezanson, S. Karpinski, V.B. Shah, A. Edelman, Why we created Julia (2012). https://
julialang.org/blog/2012/02/why-we-created-julia/
16. JuliaDevelopers. Announcing the release of Julia 1.0 (2018). https://julialang.org/blog/2018/
08/one-point-zero/
17. Jan 2021 Julia Growth Indicators. https://juliacomputing.com/blog/2021/01/newsletter-
january/
18. PYPL PopularitY of Programming Language (2021). https://pypl.github.io/PYPL.html
19. Top Programming Languages 2021 (2021). https://spectrum.ieee.org/top-programming-
languages/
20. Top Programming Languages 2018 (2018). https://spectrum.ieee.org/static/interactive-the-
top-programming-languages-2018
21. Parallel Supercomputing for Astronomy (2017). https://juliacomputing.com/case-studies/
celeste/
22. J. Regier, K. Pamnany, R. Giordano, R. Thomas, D. Schlegel, J. McAuliffe, Prabhat, Learning
an Astronomical Catalog of the Visible Universe through Scalable Bayesian Inference. arXiv
(2016)
23. Julia Joins Petaflop Club (2017). https://juliacomputing.com/media/2017/09/julia-joins-
petaflop-club/
24. CliMA 0.1: A first milestone in the next generation of climate models (2020). https://clima.
caltech.edu/2020/06/08/clima-0-1-a-first-milestone-in-the-next-generation-of-climate-
models/
25. One of Europe’s largest insurers is using Julia for Solvency II compliance (2016). https://
juliacomputing.com/case-studies/aviva/
26. R.A.J. Chagas, F.L. de Sousa, A.C. Louro, W.G. dos Santos, Modeling and design of a
multidisciplinary simulator of the concept of operations for space mission pre-phase A studies.
Concurr. Eng. 27(1), 28–39 (2019)
27. Pfizer uses Julia to accelerate simulations of new therapies for metabolic diseases up to 175x
(2016). https://juliacomputing.com/case-studies/pfizer/
28. Optimizing bus routes and times (2017). https://juliacomputing.com/case-studies/boston-
school-bus/
29. The Federal Aviation Administration is using Julia to develop the Next-Generation Airborne
Collision Avoidance System (2017). https://juliacomputing.com/case-studies/lincoln-labs/
30. JuliaHub. https://juliahub.com/ui/Packages
31. P. Wadler, The expression problem (1998). https://homepages.inf.ed.ac.uk/wadler/papers/
expression/expression.txt
32. J.C.Reynolds, User-definedtypesandproceduraldatastructuresascomplementaryapproaches
to data abstraction, in Programming Methodology (Springer New York, New York, NY, 1978),
pp. 309–317
33. F. Jopp, B. Breckling, H. Reuter, Modelling Complex Ecological Dynamics: An Introduction
into Ecological Modelling for Students, Teachers & Scientists (Springer, 2011)
34. J.S. Coleman, Foundations of Social Theory (Belnap Press, 1990)

250 A.R.Vahdati
35. D. Masad, J. Kazil, Mesa: an agent-based modeling framework, in Proc. of the 14th Python in
Science Conf. (Scipy) (2015), pp. 53–60
36. U. Wilensky, NetLogo, in Evanston, IL: Center for Connected Learning and Computer-Based
Modeling, Northwestern University, Evanston, IL (1999)
37. OpenStreetMap contributors. Planet maps at https://planet.osm.org. https://www.
openstreetmap.org (2017)

Chapter 10
Portfolio Management and Crises: A
Multi-Armed Bandit Approach
Inês Ferreira and Marta Moraes
In this chapter we develop and implement a Multi-Armed Bandit (MAB) to optimize
equity portfolios. Then, we analyse the impact that a crisis can have on the system.
The implementation of both the MAB algorithm and the crisis is made using R and
RStudio software.
10.1 Introduction
In Finance, the optimization of equity portfolios can be addressed as a portfolio
selection problem. This is a typical decision problem where the decision maker
selects the portfolio that will maximize its return and minimize its level of risk
taken, using the information on assets that is available at that moment, aiming to
optimize the allocation of wealth across a set of assets [1–3].
A portfolio consists of various components such as projects, programs, and
other tasks like maintenance and ongoing operation. In the context of this chapter,
a portfolio is a collection of a wide range of financial assets that are owned by
investors.
Several authors have investigated the Portfolio Selection Problem, with the goal
of finding an recommending the best approaches to make an optimal allocation
of funds to invest in various financial assets, with the objective of generating
steady returns while minimizing risk. In 2019, Mohagheghi et al. [4] present
a comprehensive review of portfolio selection (PPS) focusing on the evaluation
criteria, selection approach, solution approach, uncertainty modeling, and appli-
cations. However, Machine Learning-based approaches are not considered by [4].
These approaches are referred to future trends, such as rule-based expert system,
I. Ferreira (@) · M. Moraes (@)
University of Porto, FEP, Porto, Portugal
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 251
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_10

252 I.FerreiraandM.Moraes
frame-based expert system, fuzzy expert system, neural expert system, and neuro-
fuzzy expert system). Li and Hoi [1], formulate online portfolio selection as a
sequential decision problem in Computational Finance, and then survey a variety of
state-of-the-art approaches, which are grouped into several major categories, includ-
ing benchmarks, “Follow-the-Winner” approaches, “Follow-the-Loser” approaches,
“Pattern-Matching” based approaches, and “Meta-Learning Algorithms”.
Machine Learning approaches are more common in recent years. In 2022,
Zhang and other authors [5] propose a cost-sensitive portfolio selection method
with deep reinforcement learning. The authors use a two-stream portfolio policy
network to extract both price series patterns and asset correlations. In 2022, Li and
other authors [6] propose an hypergraph-based reinforcement learning approach for
stock portfolio selection. The main goal is to learn a policy function generating
appropriate trading actions given the current environments. Boli and other authors
[7] use a bidirectional incremental learning method, (Bi-BLS), and propose a
method for removing the noise based on random matrix theory and principal
component analysis.
In this Chapter we propose a Portfolio Selection model using Reinforcement
Learning, based on the Multi-Armed Bandit (MAB) paradigm. Then, we generate
a crisis situation with the objective of understanding the impact on learning
performance. The main goal is to develop a simple and intuitive approach that is
easy to understand and implement in R.1
Multiple assets need to be explored and a profit maximizing asset is exploited
making this problem fall into the explore-exploit class of Machine Learning based
decision-making problems. MAB algorithms are well suited to explore this class of
problems and their application in these problems is stated in literature, [2].
MAB is based on Reinforcement Learning and takes into account the
exploration–exploitation trade-off paradigm in which a fixed finite set of resources
must be allocated between competing choices in such a way as to maximise
the expected payoff. The n-armed bandit problem or Multi-Armed Bandit
(MAB) belongs to a class of models named evaluative feedback models (where
Reinforcement Learning belongs), different from instructive feedback (the basis of
supervised learning) that indicates the correct action to take, independently of the
action actually taken [8].
The Chapter is structured as follows: in Sect. 10.2, we introduce the Multi-Armed
Bandit (MAB) algorithm, in Sect. 10.3 we describe the Upper Confidence Bounds
Algorithm, with which we implement the MAB. Problem Description is described in
Sect. 10.4. In Sect. 10.5 we implement a crisis, by decreasing the monthly returns of
each ETF and a variation of the risk associated with the ETF. Finally, in Sect. 10.6,
we present a final discussion and concluding remarks.
1 Program codes are available in: https://ml4agents.free.nf.

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 253
10.2 Multi-Armed Bandit (MAB)
Multi-Armed Bandit (MAB) is named after the original form of the n-armed bandit
problem, by analogy to a slot machine, or one-armed bandit. In this game, someone
is repeatedly presented with a choice between n different options or actions. After
each choice, there is a numerical reward selected from a stationary probability
distribution that depends on the action chosen. The goal is to maximise the total
expected reward over a period of time, [8].
The MAB algorithm allows for the modeling of two conflicting concepts—
exploration and exploitation—in an environment characterized by uncertainty [3].
The basic model of MAB is called stochastics bandits and it consists of an algorithm
where there are K actions to choose from—arms—and there are t rounds, for known
K and t. In each round, the algorithm will choose an arm and collect a stochastic
reward generated from an unknown distribution that is associated with each chosen
arm. The final goal of the algorithm is to maximize the total reward over the t rounds
[9].
So, the model must learn the unknown distributions of the different K arms by
choosing them throughout the t rounds. Despite this and considering the final goal of
the model, MAB must also choose the arms, during those t rounds, that have already
been identified as profitable. This decision of “exploring the unknown and exploiting
the already known” reflects the already referred trade-off between exploration and
exploitation,[3].
This trade-off can be solved through the use of different allocation strategies—
these identify the next arms that are going to be chosen. These allocation strategies
aim to maximize the sum of the rewards or, following the same logic, to minimize
the regret. Regret represents the sum of loss of the potential gains in each round,
i.e. the difference between the maximum potential reward and the actual rewards
accumulated. In other words, Regret is the difference between the best reward
possible given the strategy of playing a single arm and the player’s rewards after
T time steps.
Mathematically, the stochastic reward generated from each arm i in each round t
can be represented by thevariablesX , where1≤i ≤Kandt ≥1(t is the round’s
i,t. . .
number); i.e., by choosing the arm i, the rewardsX ,X ,...are generated, which
i,1. i,2.
are independent and identically distributed according to an unknown probability
law. It is also important to mention that the rewards between the different arms are
also independent and identically distributed [3, 9].
LetT (t)be the number of times the arm i is chosen in the first t rounds. Here, the
i .
regret of the player after t rounds, which is the one desired to minimize, is defined
by the f ollowingequation:
EK
R =T ×μ ∗−μ E(T (T))) (10.1)
. T j(T) k
k=1

254 I.FerreiraandM.Moraes
where,
. μ ∗ = max i=1,...,k (μ i ) . ; μ ∗ . is the expected reward of the best arm.
. E(T (T )) is the expectation about the number of times the player will choose
k .
arm k.
. T is the total number ofrounds.
. K is the number ofarms.
. μ is the expected reward of arm i.
i.
10.3 Upper Confidence Bounds Algorithm
The implementation of MAB in this chapter will be done using the Upper
Confidence Bounds (UCB) algorithm. This algorithm initially assumes that all arms
have equal observed average value, since there is no information about what arm
is the best. Later, a confidence limit for each arm will be created and an arm will
be selected randomly. Exploration of the unknown is needed because the estimates
of the action values are uncertain. These greedy actions are those that look best at
present, but some of the other actions may actually be better [3, 8].
In each of the T rounds, the upper confidence limit will be updated depending
on whether the selected arm returns a mistake or a reward—in this specific context
the reward represents the selection of the ETF (Exchange-Traded Fund) with the
highest returns in round t and the mistake represents the selection of any other ETF.
If the reward is returned in round t, the observed average of the arm will increase
and so will the upper confidence bound, and the contrary will happen if a mistake is
returned by the s electedarm.
In fact, this UCB approach can be seen as the principle of optimism in uncertainty
[2] because whenever the value of an arm is uncertain, its largest plausible value is
considered and the best action is selected later.
UCB is a deterministic algorithm for Reinforcement Learning that focuses on
exploration and exploitation based on a confidence boundary that the algorithm
assigns to each machine on each round of exploration. The idea of using MAB
in quantitative finance is not new. Chen et al. [10] proposed a dynamic portfolio
strategy that combines Fuzzy C-means clustering with UCB-based algorithms,
optimized through Genetic Algorithms, to adapt to client risk tolerance. The results
show that the GA-UCB approach significantly improves cumulative return .
Qiu [11] combined convex optimization, multifactor models, and KL-UCB
bandit algorithms to construct adaptive investment portfolios under uncertainty.
Results show that dynamic weight adjustment using KL-UCB improves portfolio
performance during market volatility, while also revealing a preference for large-
cap growth stocks driven by systematic risk factors.

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 255
10.4 Problem Description
One of the novel approaches of this work is the application of a Multi Armed
Bandit Algorithm in a crisis scenario. In order to experiment and analyze the
implementation of the algorithm, there is a need to design an experimental problem.
Taking into account the problem and the approach presented in [3], six different
ETFs will be considered during this experiment. An ETF is a basket of securities
that is traded on an exchange just like stocks are. It is a type of fund that holds
multiple underlying assets, rather than only one like a stock does.
In practice, a portfolio can contain many ETFs, but in the case of this problem,
each portfolio will contain only one ETF and, because of that, the terms portfolio
and ETF will be used interchangeably.
The six ETFs were created, and their respective weekly returns were sampled
through the use of the rnorm function of the basic stats package. The R function
rnorm simulates random variables having a specified normal distribution. One of
the advantages of generating random ETFs is that it allow to set specific means,
variances, and reward distributions and this lets us simulate controlled crises, such
as sudden drops in expected returns or increases in volatility, and observe how the
learning algorithm reacts. Furthermore, random ETFs help decouple our analysis
from past market structure, focusing instead on algorithmic learning dynamics. The
normal distribution was chosen to represent the returns of the ETFs due to the
assumption present in the classical mean-variance analysis from Markowitz [12].
This analysis assumes that the returns of the financial assets are normally distributed
[13] and that the mean of the distribution is related to the returns and the standard
deviation is related to the risk [14].
For implementation and demonstration purposes, the normal distributions for
the weekly returns of the ETFs will present considerably different means. The
parameters for the distributions for the weekly returns are presented in Table 10.1.
A matrix containing the simulated weekly returns for the six portfolios was
created. Due to replication reasons, a random seed was set to 200. Note that, for
this implementation, a period of 20 years will be considered (the matrix will contain
1040 rows).
Table 10.5 in the Appendix of this chapter presents the first 26 rows of the matrix
created through the process previously described. Thus, the table presents the values
Table 10.1 Statistical
ETF Mean Standard deviation
measures of the normal
1 0.7 0.75
distribution for the ETFs
2 0.2 0.75
3 −0.8 0.75
4 0.0 0.75
5 −0.1 0.75
6 0.1 0.75

256 I.FerreiraandM.Moraes
of the weekly returns of the ETFs during the first half of the first year considered in
this problem.
In his work, [12] noted that investors seek to minimize variance for a given level
of expected return or, equivalently, they seek to maximize expected return for a
given constraint on variance [15].
Assuming that the portfolio is owned by an agent, for this experiment, the
objective is to maximize its return throughout the 1040 weekly periods. It will be
assumed that during the implementation of the MAB, without the occurrence of a
crisis, the risk and consequently the standard deviation of the normal distribution
creating the returns will be constant and the same for each ETF.
In this section, the implementation of the Upper Confidence Bound (UCB) Multi-
Armed Bandit algorithm made in RStudio will be shown and explained.
First, it is important to note that this implementation of the MAB algorithm
follows the approach of [3]. As it was already stated, there are six ETFs (the arms)
that are considered throughout a period of 1040 weeks (20 years). So, considering
the notation presented in Sect. 10.2, K = 6 and T = 1040; in other words, there
. .
will be 6 arms for 1040 weeks/rounds.
nobs <- 1040
narms <- 6
The creation of the data was previously explained in this section and the
corresponding code in R is presented below.
set.seed(200)
ETF1 <- as.data.frame(matrix(rnorm(mean=0.7, sd=0.75, n=nobs), nobs,1))
ETF2 <- as.data.frame(matrix(rnorm(mean=0.2, sd=0.75, n=nobs), nobs,1))
ETF3 <- as.data.frame(matrix(rnorm(mean= -0.8, sd=0.75, n=nobs),
nobs,1))
ETF4 <- as.data.frame(matrix(rnorm(mean=0.0, sd=0.75, n=nobs), nobs,1))
ETF5 <- as.data.frame(matrix(rnorm(mean= -0.1, sd=0.75, n=nobs),
nobs,1))
ETF6 <- as.data.frame(matrix(rnorm(mean=0.1, sd=0.75, n=nobs), nobs,1))
data <- cbind(ETF1, ETF2, ETF3, ETF4, ETF5, ETF6)
colnames(data) <- c("ETF 1", "ETF 2", "ETF 3", "ETF 4", "ETF 5",
"ETF 6")
After creating the data set matrix, a new matrix with the same dimensions will
also be created(nobs,narms)and it will consist of zeros, with a value of one placed
.
at the position of the maximum value in each row of the original dataset matrix.
datasel <- as.data.frame(matrix(0, nrow=nobs, ncol=narms),
col.names = Names)
for(i in 1:nobs){
for(j in 1:narms){
rowmax <- apply(data, 1, max)
if(data[i,j] == rowmax[i])
datasel[i,j] <- 1
}
}

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 257
At this point, it will be necessary to initialize the variable that will save the
ETF selected in an iterative cycle (etf selected), the number of selections made
(numselections), the sum of rewards for each arm (rewsum) and the total reward
obtained (totrew).
etfselected = integer()
numselections = integer(narms)
rewsum = integer(narms)
totrew = 0
rewards <- c()
In order to select the ETF that showed the maximum return for the highest
number of observations, two iterative cycles will be required to run the entire matrix;
one will run the rows and the other will run the columns.
For each line (first cycle—outer cycle) the variables etf and the maxupbound
are initialized to zero and then going through the columns (second cycle—inner
cycle) an UCB will be performed. Both the sum of the rewards obtained by the arm
i after n plays and the number of times the arm i is selected after the first n plays are
computed in order to obtain the average rewar/ds obtained by the arm i after n plays.
Note that the confidence interval—Δ (t) = 2/3·lnt and the maximumUCB are
i Ni(t) . .
also computed in this inner cycle. /
Note that, if theupbound =UCB (t)=μˆ (t)+ 2lnt obtained for a run of this
i i Ni(t).
cycle returns a higher value than the present maxupbound value saved, this will be
replaced by it.
After this, the values for the variables will be updated at the end of the outer cycle
and these two cycles will run again until the last line is analyzed.
for(n in 1:nobs)
{
etf = 0
maxupbound = 0
rewards [n] <- 0
for(i in 1:narms)
{
if(numselections[i]>0)
{
averagereward = rewsum[i]/numselections[i]
deltai = sqrt(3/2 * log(n)/numselections[i])
upbound = averagereward + deltai
}
else
{
upbound <- 1e400
}
if (upbound > maxupbound)
{
maxupbound = upbound
etf = i
}
}

258 I.FerreiraandM.Moraes
| etfselected <-              | append (etfselected, etf)  |     |
| --------------------------- | -------------------------- | --- |
| numselections[etf] <-       | numselections[etf] + 1     |     |
| reward <- datasel [n, etf]  |                            |     |
print(reward)
| rewsum [etf] =   | rewsum[etf] | + reward |
| ---------------- | ----------- | -------- |
| totrew <- totrew | + reward    |          |
| rewards [n]      | <- totrew   |          |
}
Note  that  the  calculation  of  the  confidence  interval,  the  updating  of  the
maxupbound variable and the updating of the variables are the most relevant
factors presented above since they allow for the RL to be implemented and applied.
In order to view the results obtained for the implementation, a barplot was
designed to show the number of times each ETF was selected, presented in Fig. 10.1.
Analyzing the barplot presented in Fig. 10.1, it is possible to see that, clearly,
the agent chose the first ETF most of the times. In fact, this ETF presents a very
considerable difference in the number of times it was selected when comparing
with the other ETFs. This was expected, since the first ETF’s weekly returns were
simulated with a normal distribution that presented a considerably larger mean than
the other distributions used for this problem.
The goal of the agent (maximize its returns) is clearly being achieved through
the arm selections.
Consider also Table 10.2 with some relevant outputs from the implementation of
the algorithm to this specific problem.
Fig. 10.1  ETFs selections for the 1040 rounds
Table 10.2  Outputs for the
Output Value
algorithm implementation
Total reward accumulated 383
Maximum up bound found  0.563

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 259
Fig. 10.2 Cumulative reward for the 1040 rounds
Fig. 10.3 Cumulative reward
and regret for the 1040
rounds
When analyzing the MAB implementation, it is also important to consider the
cumulative reward that the algorithm obtained. In the context of the problem, this
represents the reward that the agent got from the selection of the ETFs during the
rounds. Note, in Fig. 10.2, that the reward obtained by the agent in round t is
considered to be 1 if the agent chooses the portfolio with the highest return for
that round and 0 ot herwise.
Still regarding the cumulative reward, both the perfect choice scenario (in which
the agent always chooses the best portfolio and, therefore, gets a reward of 1 in
every round) and the actual scenario were plotted. Note that the regret of the agent
can be seen in the area colored in blue in Fig. 10.3. Also, the plot of the cumulative
regret can be seen in Fig. 10.4.

260 I.FerreiraandM.Moraes
Fig. 10.4 Cumulative regret
for the 1040 rounds
10.5 Implementation of a Crisis
The implementation of the crisis consists in the decrease of the monthly returns of
each ETF and a variation of the risk associated with the ETFs.
We assume that the crisis is a political one (it will destabilize fiscal policy
and regulations), having implications in financial assets’ returns and risk and,
consequently, in portfolio management.
It is important to be aware that political instabiilty affects the rates of return and
the risk of investments and, since a portfolio is a collection of financial investments,
it will also affect the rate of return and risk of the portfolios. Fiscal deficits may lead
to higher borrowing costs for businesses and an arduous regulatory approval process
can hamper business investments, for example in the resource and energy sectors.
Political instability reduces the confidence of investors and businesses since there is
less visibility into possible investment returns. Investors tend to avoid countries that
change governments frequently or have civil conflict [16].
In the context of this problem, it was decided that the best way to implement
this crisis was to acknowledge the existence of portfolios containing investments
in countries suffering from a political crisis and portfolios with investments in
countries with political instability.
As mentioned before, there are six portfolios under consideration. Let’s assume
that the first three contain investments in countries that will suffer from a political
crisis and the other three don’t. This will cause a decrease in the returns and an
increase in the risk of the first three portfolios, and it will be assumed that there will
be a maintenance of the returns and risk of the rest.
The implementation of the crisis was made in such way that the crisis only occurs
in the second half of the observations and, because of this, the following was done:
the values of the observations of ETF 4, ETF 5 and ETF 6 remained the same as
before (basic implementation without the crisis); the first 520 observations of ETF 1,
ETF 2 and ETF 3 also remained the same, while the second half of the observations

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 261
Table 10.3 Statistical
ETF Mean Standard deviation
measures of the normal
1 0.2 1
distribution for the ETFs after
the crisis hit 2 0.0 1.5
3 −0.8 1.25
4 0.0 0.75
5 −0.1 0.75
6 0.1 0.75
of these three ETFs were adapted to the values of the crisis (smaller returns and
higher risk).
Concerning the values of the crisis, the mean of the returns was decreased in
the first three ETFs (except the third one that maintained the negative mean of
the normal distribution) while the standard deviation was increased. Note that the
decreases/increases were not the same for all variables.
The mean of the distribution of the returns of ETF 1 decreased from 0.7 to 0.2.
Since this was the ETF with the largest mean of returns, it was decided that this
should also be the one with the largest drop (it could represent, for example, a
collection of securities from non-essential industries). Because this was the ETF
with the largest decrease in the mean, it was thought that the standard deviation
should not increase too much. Therefore it was only increased by 0.25.
Now, for the distribution of the returns of ETF 2, the mean decreased from 0.2 to
0 and the standard deviation increased by 0.75 because the decrease in the mean was
relatively small and it did not become negative (becoming the ETF with the normal
distribution that has the largest standard deviation, and therefore, the largest risk).
Lastly, for the distribution of the returns of ETF 3, since the mean was already
negative, it was considered best to keep it unchanged and increase only the standard
deviation by 0.5 (Table 10.3).
In order to analyze the impact of the crisis in MAB, the implementation of the
UCB Multi-Armed Bandit algorithm was made in this new dataset (with the values
of the crisis). Since the implementation follows the same steps and logic as the one
applied to the original dataset (shown in the previous section), it will not be shown-
only the results will be presented and explained.
Just like before, a barplot was designed to represent the number of times each
ETF was selected (Fig. 10.5).
Analyzing the barplot, it can be seen that the agent chose ETF 1 most of the
times (in more than half of the rounds). This ETF was chosen more than 500 times
but much less times than in the last experiment (without any crisis), in which it was
chosen more than 800 times. This could mean that the choice of this ETF could
be imputed to the first half of the observations (which are the same ones as the first
experiment). This will be further studied later by analyzing only the selections made
by the agent after the crisis started.
Also, it is possible to see that, when comparing with the same barplot without the
implementation of the crisis, all the other ETFs were chosen more times, especially

262 I.FerreiraandM.Moraes
Fig. 10.5 Selection of the ETFs during the 1040 rounds considering the crisis that started at round
520
Table 10.4 Outputs for the
Output Value
algorithm implementation
Total reward accumulated 294
Maximum up bound found 0.521
ETF 2. This larger proportion of choice of ETF 2 was expected since, despite the
mean of its distribution of returns being lower, the standard deviation is larger (for
the second half of the observations) and, because of that, this ETF can reach higher
values (more volatile).
ETF 3 is the least chosen one, which was also expected since this continues to
be the one with the lowest distribution mean (and its standard deviation was not
increased by much). Now, consider Table 10.4 with some relevant outputs from the
implementation of the algorithm to this dataset.
The total reward accumulated by the agent in this experiment is smaller than the
total reward accumulated by the agent in the first one, without a crisis. The same
happens for the maximum up bound found. These results were expected.
Just as in the first experiment, a plot was built to show the evolution of the
cumulative reward that the agent obtained in the different rounds. Note that, when
analyzing the slope of this plot it is clear to see exactly the time period when the
crisis “hit” and affected the returns of the ETFs (Fig. 10.6).
Drawing the line of the cumulative rewards for the perfect choice scenario (in
which the agent always chooses the best portfolio and, therefore, gets a reward of 1
in every round) and for the actual scenario (with the crisis), the regret of the agent
can be seen colored in red. Also, the plot of the cumulative regret can be seen below,
its values go up to 746 (Figs. 10.7 and 10.8).
It is also important to analyze the results obtained with this second experiment
but only considering the weeks after the crisis was implemented. This will allow
to see the functioning of the algorithm implemented during this crisis without the
influence of the first half of the 1040 weeks.

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 263
Fig. 10.6 Cumulative rewards during the 1040 rounds considering the crisis that started at round
520
Fig. 10.7 Cumulative
rewards and regret during the
1040 rounds considering the
crisis that started at round 520
The following barplot was built in order to show the number of times each ETF
was selected in this case (Fig. 10.9).
Here, it can be seen that the number of times that the agent chose ETF 1 is still
the largest, which was expected since this ETF, even during the crisis, continued to
be the one with the largest distribution mean.
As seen before, ETF 2 was the second most chosen, probably because of having
the largest distribution standard deviation.
Finally, it is also important to plot together the cumulative rewards obtained for
the 1040 weeks, one where the crisis does occur, and the other one where it does
not.
Consider the plot of the cumulative rewards of the agent without the crisis (in
blue) and with the crisis (in red). The plot on Fig.10.10 shows the cumulative

264 I.FerreiraandM.Moraes
Fig. 10.8 Cumulative regret
during the 1040 rounds
considering the crisis that
started at round 520
Fig. 10.9 ETFs selections only considering only the rounds where there was a crisis (the last 520)
rewards in rounds 1 to 1040 and the plot on Fig.10.11 shows only the cumulative
rewards in the rounds 521 to 1040.
As expected, the values of the cumulative rewards are much larger in the
case where there is no crisis than in the case where there is a crisis, but this
difference only occurs after the crisis hits (after round 520); in fact, until the crisis
is implemented it is possible to see that the cumulative rewards are the same for the
two experiments.
Now, comparing the cumulative regrets for both implementations, the one from
the scenario with the implementation of the crisis is higher than the one without the
crisis. This result was anticipated since lower cumulative rewards will lead to higher
cumulative regrets (Fig. 10.12).

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 265
Fig. 10.10 Cumulative
rewards for both experiments
(without a crisis—in
blue—vs with a crisis—in
red—) for all 1040 rounds
Fig. 10.11 Cumulative rewards for both experiments made (without a crisis—in blue—vs with a
crisis—in red—) for the last 520 rounds
10.6 Final Discussion and Concluding Remarks
To sum up, an implementation of MAB for optimization of equity portfolios and a
generation of a crisis producing a shock were made and further analyzed.
In order to create meaningful data for the implementation of both the algorithm
and the political crisis, some literature research was made. This allowed for the
creation of a group of six portfolios in which one would be undoubtedly superior
and for the generation of an appropriate shock in the financial assets’ returns’
distributions after a political crisis.
Analyzing the results obtained for the implementation without considering the
crisis, it was possible to see that the agent clearly selected the ETF that was designed
to present better returns most of the times and this “preference” for that “arm” is
quite significant when compared to the few times the other ETFs were selected.

266 I.FerreiraandM.Moraes
Fig. 10.12 Cumulative regret for both experiments made (without a crisis vs with a crisis) for all
1040 rounds
Regarding the results obtained for the implementation of the crisis, it was
possible to see that the agent still selected ETF 1 most of the time. Despite this,
it was possible to conclude that the agent selected the rest of the ETFs more times
than in the first implementation of the algorithm, especially ETF 2.
Considering the cumulative rewards and cumulative regrets for both implemen-
tations, these are the same until the crisis hits. After this, there is a clear difference
between the two experiences. When there is no crisis, as it would be expected, the
cumulative rewards are higher and the cumulative regret is lower than for the second
experience, where there is a crisis.
Appendix
See Table 10.5.

10 PortfolioManagementandCrises:AMulti-ArmedBanditApproach 267
Table 10.5  Weekly returns of the 6 ETFs generated for the first 26 weeks
| Week ETF 1 | ETF 2   | ETF 3  | ETF 4  | ETF 5   | ETF 6   |
| ---------- | ------- | ------ | ------ | ------- | ------- |
| 1 0.764    | −0.294  | −1.424 | −0.507 | 0.429   | −0.265  |
| 2 0.870    | 0.396   | −0.721 | 0.396  | −0.571  | 0.129   |
|            |         | −1.416 |        | −0.498  | −0.002  |
| 3 1.024    | 0.685   |        | 0.912  |         |         |
| 4 1.119    | 1.790   | −1.228 | −0.125 | 1.560   | 1.106   |
−0.457
| 5 0.745   | 0.369   | 0.366  | 0.201   |         | 0.025   |
| --------- | ------- | ------ | ------- | ------- | ------- |
| 6 0.614   | 1.285   | −0.789 | −0.019  | −0.315  | −0.096  |
| 7 −0.065  | 0.272   | −2.419 | 0.487   | 0.449   | 1.710   |
|           | −0.456  | −2.736 |         |         |         |
| 8 0.477   |         |        | 0.525   | 0.203   | 0.261   |
| 9 0.826   | 1.441   | −0.622 | −0.602  | −1.276  | 0.086   |
|           | −0.049  | −0.236 |         |         | −0.140  |
| 10 1.765  |         |        | 0.146   | 0.452   |         |
| 11 0.625  | 0.747   | −1.123 | 0.564   | −0.891  | 0.730   |
| 12 0.086  | −0.991  | −0.808 | −0.344  | 0.457   | −0.842  |
|           |         | −1.939 | −0.668  | −0.293  |         |
| 13 0.348  | 0.360   |        |         |         | 0.074   |
| 14 1.131  | −0.534  | −0.053 | 0.388   | 0.178   | 0.125   |
| −0.704    |         |        | −0.656  | −0.206  | −0.631  |
| 15        | 0.104   | 0.036  |         |         |         |
| 16 0.226  | 0.668   | −1.183 | −0.111  | 0.855   | 0.534   |
| 17 0.668  | −0.792  | −0.450 | 0.579   | −1.456  | 1.220   |
|           | −1.052  | −1.368 |         | −0.020  | −0.107  |
| 18 1.782  |         |        | 0.724   |         |         |
| 19 0.009  | 1.013   | −1.521 | −0.483  | −0.350  | 1.301   |
| 20 0.688  | 0.668   | −1.674 | 0.237   | −0.299  | 0.207   |
| 21 0.865  | 0.722   | −0.567 | 0.142   | −0.629  | −0.273  |
| 22 1.075  | −0.854  | −1.564 | −0.378  | −0.588  | 1.328   |
|           | −1.382  | −0.792 |         |         | −0.688  |
| 23 1.952  |         |        | 1.122   | 0.625   |         |
| 24 −0.053 | 0.460   | −1.678 | 0.558   | 0.235   | −0.266  |
| 25 0.996  | −0.214  | −0.907 | −0.076  | −0.013  | −0.849  |
| −0.423    |         | −0.348 |         | −0.331  |         |
| 26        | 0.305   |        | 0.204   |         | 0.398   |
References
1. B. Li, S.C.H. Hoi, Online portfolio selection: A survey. ACM Comput. Surv. 46(3), 36 (2014).
https://doi.org/10.1145/2512962
2. B. Villari, M. Abdulla, Online portfolio selection using a new stochastic multi-armed bandit
algorithm. Indore Manag. J. 10, 9–11 (2018)
3. G. Ciaburro, Hands-on Reinforcement Learning with R (2019)
4. V. Mohagheghi, S.M. Mousavi, J. Antuchevicˇiene˙, M. Mojtahedi, Project portfolio selection
problems: A review of models, uncertainty approaches, solution techniques, and case studies.
Technol. Econ. Dev. Econ. 25(6), 1380–1412 (2019)
5. Y. Zhang, P. Zhao, Q. Wu, B. Li, J. Huang, M. Tan, Cost-sensitive portfolio selection via deep
reinforcement learning. IEEE Trans. Knowl. Data Eng. 34(1), 236–248 (2022)
6. X. Li, C. Cui, D. Cao, J. Du, C. Zhang, Hypergraph-based reinforcement learning for stock
portfolio selection,  in ICASSP  2022–2022  IEEE  International  Conference  on  Acoustics,
Speech and Signal Processing (2022), pp. 4028–4032

268 I.FerreiraandM.Moraes
7. B. Li, Q. Wang, Y. Yuan, M.-Z. Sun, L.-X. Chen, Z.-L. Xiang, F. Zhao, Q.-C. Lv, Z.-Y. An,
A novel risk-control model for the online portfolio selection of high-frequency transactions.
Knowl. Based Syst. 240, 108176 (2022)
8. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction (MIT Press, 2018)
9. A. Slivkins, Introduction to Multi-Armed Bandits (Now Publishers, 2019)
10. C. Chen, X. Liu, Y. Ma, X. Zuo, Application of Multi-Armed bandit algorithm in quantitative
finance. ITM Web Conf. 73, 01011 (2025). https://doi.org/10.1051/itmconf/20257301011
11. H. Qiu, Investment Portfolio with Convex Optimization and Risk Adjustment Using Multi-
Factor Model and Multi-Armed Bandit Algorithm. Adv. Econ., Management Political Sci. 104,
55–68 (2024)
12. H.M. Markowitz, Portfolio selection. J. Finance 7(1), 77–91 (1952)
13. M. Hazny, A. Yusof, H. Hasim The Markowitz mean variance analysis: A review from Shariah
perspective, in Islamic Banking, Accounting and Finance (2012), p. 10
14. in Investopedia, available in: https://www.investopedia.com/articles/investing/100714/using-
normal-distribution-formula-optimize-your-portfolio.asp
15. M. Haugh, Mean-variance optimization and the CAPM (2023). Accessed 2 Dec 2023
16. C. Basu, What factors influence the rates of return on an investment? (2022). Accessed 24 Feb
2022

Chapter 11
Organizational Learning from Crises
with Machine Learning and Agent-Based
Models
Friederike Wall and Pedro Campos
11.1 Introduction and Background
The viability of organizations depends on their ability to learn—all the more as
the environments are uncertain and turbulent including crises like the Covid-19
pandemic. Terms like flexibility, agility, or responsiveness coin requirements that
may lead to even abandoning past knowledge, skills, or business models. The
necessity of organizations to learn is generally acknowledged and accepted in
academia and practice. However, it is also widely recognized that organizations
often resist changes and adaptations.
In this chapter we discuss the potential contributions of machine learning
and agent-based models for organizational learning with a particular focus on
organizational learning from crises. This appears the more relevant as there is
evidence that organizational learning from crises faces particular difficulties and
obstacles (e.g., [1–4]).
There is a vast body of research on organizational learning (for reviews, e.g.,
[5–8]). According to Edmondson and Moingeon [6], research on organizational
learning can be categorized along two dimensions, (1) the primary unit of analysis
and (2) the research goal: Regarding (1) the unit of analysis, some researchers
study how organizations as a whole adapt, while another stream mainly focuses
on the learning of individual organizational members. As for the (2) research goal,
the descriptive stream of research aims at precisely describing and understanding
F. Wall (@)
Department for Management Control and Strategic Management, University of Klagenfurt,
Klagenfurt, Austria
e-mail: friederike.wall@aau.at
P. Campos
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 269
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_11

270 F.WallandP.Campos
Fig. 11.1 Typology of research on organizational learning according to Edmondson and Moin-
geon [6, p. 23, slightly modified]
of organizational learning, whereas intervention research seeks to find managerial
actions that could enhance the effectiveness of organizations including learning.
Hence, from the categorization of Edmondson and Moingeon [6]a2 ×2structure
.
follows as indicated in Fig. 11.1:
1. “Residues”: Building on behavioral theories of the firm [9], this stream regards
organizations as the “outcome” of evolutionary processes of learning and
adaptation based on routines and processes of acquisition and interpretation of
knowledge (e.g., [10]).
2. “Communities”: This line of research, for example, seeks to understand how and
under which conditions individuals learn in organizations, and how individual
learning affects outcomes of organizations (e.g., [11]).
3. “Participation”: Organizational members’ participation, for example, in
problem-solving and communication, is regarded the enabler of organizational
learning, and respective interventions (e.g., systems for information sharing) are
in the center of interest (e.g., [12]).
4. “Accountability”: Organizational learning is regarded as resulting from indi-
viduals adjusting and refining their mental models and, thus, improving their
decision-making capabilities. In this sense, individuals are accountable for the
change of their organizations. This stream seeks for interventions that facilitate
the process of developing mental models [13–15].
The primary objective of this chapter is to highlight how machine learning
and agent-based models (ML/ABM hereafter) could contribute to organizational
learning, especially from crises. For this, we adopt the “accountability” perspective
of organizational learning which builds on the path-breaking works of Agyris
and Schön [13, 14] and Senge [15]. Particularly, Peter Senge’s concept coined
“The Fifth Discipline” provides a helpful framework for our purpose. Moreover,
Senge’s suggestion to employ system dynamics for exploring long-term effects of
managerial decisions and, especially, for updating mental models is close in spirit
to our endeavor.

11 OrganizationalLearningfromCriseswithML/ABM 271
The remainder of this is chapter is organized as follows: In Sect. 11.2, we
provide a brief overview of organizational learning—adopting the “accountability”
perspective—and the potential barriers to organizational learning in crises. Sec-
tion 11.3 outlines a framework for how agent-based models and machine learning
could be employed to contribute to organizational learning. These considerations
are transferred to different types of learning in Sect. 11.4, where we particularly
advocate systemic learning for organizational learning in crises. Finally, we provide
some concluding remarks.
11.2 Organizational Learning and Crises
This section aims at linking organizational learning—focusing the individual level
and pursuing an interventionist goal—with ML/ABM. For this, we build on Senge’s
“Fifth Discipline” [15] as it was operationalized in Garvin’s [16] concept of learning
organizations (Sect. 11.2.1). We show how prominent forms learning in agent-
based models (Sect. 11.2.2) could be integrated into Garvin’s building blocks of
organizational learning (Sect. 11.2.3).
11.2.1 Senge’s Fifth Discipline and Garvin’s Building Blocks
of a Learning Organization
In his prominent work “The Fifth Discipline”, Senge defines learning organizations
as
“organizations where people continually expand their capacity to create the results they
truly desire, where new and expansive patterns of thinking are nurtured, where collective
aspiration is set free, and where people are continually learning how to learn together” [15,
p. 1]
Senge suggests five “component technologies” [15, p. 10] as essential for
achieving a learning organization:
. Systems thinking should let organizational members think of the interrelated and
mutual effects of their actions even if they are distant in time and space—instead
of only focusing on their own area of competence and this in short-termism. For
supporting thinking in systems, Senge recommends Systems Dynamics.
. Personal mastery captures organizational members’ ongoing focus of “energy”
and commitment but also their continuous developing of their personal vision and
proficiency. In the center is to develop an objective understanding of the relevant
reality and the formation of high aspirations.
. Mental models comprise the assumptions and the deeply entrenched understand-
ing of how individuals understand the world and take action. However, mental
models often are “hidden” and may constitute an obstacle for new options or

272 F.WallandP.Campos
solutions if these conflict with powerful, tacit mental models. Hence, making
mental models in an organization explicit as well as questioning and adjusting
them, is advocated another “technology” of learning organizations.
. Building shared visions refers to creating a shared picture of the future in
the organization in order to foster the commitment of organizational members.
It is worth mentioning, that this does not address “formal” mechanisms like
(prescribed and official) “vision statements” or procedures of goal-setting;
instead, the focus is on organizational members adopting a shared vision and,
thus, generating genuine commitment (not compliance).
. Team learning addresses the fact that in organizations, not the learning of
the individual but of collectives is, finally, of relevance (“unless teams can
learn, the organization cannot learn” [15, p. 12]). Learning teams not only
promise extraordinary results, but let also team members learn from each other.
However, team learning requires processes of dialogue, members’ readiness to
suspend own views and to “think together”. Patterned interactions in teams (e.g.,
defending own views) may impede learning, especially if undetected; making
such patterns explicit may even foster learning.
Garvin [16] argues that—while being indisputable in the substance—Senge’s
recommendations are too abstract for effective implementation. In particular, he
argues that three aspects require further operationalization: (1) the definition of a
learning organization, (2) the guidelines for management for implementation, and
(3) the measurement of an organization’s rate and level of learning. As for the first
aspect, he suggests the following definition:
“A learning organization is an organization skilled at creating, acquiring, and transferring
knowledge, and at modifying its behavior to reflect new knowledge and insights.” [16, p. 80]
Based on practical evidence, Garvin [16] argues that learning organizations
employ five main activities which serve as “building blocks”:
. Systematic problem solving comprises employing scientific methods, like deriv-
ing and testing hypotheses, building on data and statistical tools and facts for
decision-making rather than on guesswork.
. Experimentation means to systematically search for and test new knowledge
and usually builds on “opportunity and expanding horizons” [16, p. 82]. Exper-
imentation may take two forms: first, ongoing programs in terms of incremental
improvements, e.g., continuous improvement programs known in operations
management; second, demonstration projects in terms of pioneering projects that
embody new principles and approaches to be adopted at larger scale later.
. Learning from own experience includes a systematic assessment of an organi-
zation’s success and failures. Particular focus should be on the accessibility of
the results for organizational members. Moreover, learning from past experience
should be subject to planning (rather than chance) in order avoid that hostile
behavior due to failures or ignorance prevents learning to happen.
. Learning from others, often also named “benchmarking” involves looking
outside the own environment for gaining new perspectives. Searching for best
practices could result in ideas or recommendations on how to improve the own

11 OrganizationalLearningfromCriseswithML/ABM 273
Table 11.1 Garvin’s building blocks and Brenner’s types of learning
Garvin—Building blocks Brenner—Types of learning
1. Systematic problem solving –
2. Experimentation Routine Based L (RBL): Experimentation (p.
908/909)
3. Learning from past experience RBL: Melioration Learning
and experience collection (pp. 909);
partially: Non-conscious L,
esp. reinforcement learning
4. Learning from others RBL: Imitation (pp. 911)
RBL: satisficing/aspiration-oriented
Belief L: e.g., fictitious play
5. Transferring knowledge –
processes or products. However, this also requires a careful analysis of the own
practices in comparison with other organizations.
. Transferring knowledge involves spreading knowledge quickly and efficiently
in the organization. There is a multitude of mechanisms to transfer knowledge,
e.g., including reports, visits, rotation of personnel, training programs or even
standardization with each having its particular strengths and weaknesses.
Garvin [16] argues that each of these building blocks is accompanied by
particular mind-sets, tool-kits, and behaviorial patterns.
Following [17], there are essentially three ways of learning in economic lit-
erature: Non-conscious learning, Routine-based learning, and Belief learning.
Reinforcement learning may be seen from the perspective of a non-conscious
type, since it has been studied in Psychology with different kinds of animals
and corresponds to the situation where actions leading to negative outcomes (a
punishment), will be avoided in the future, while actions with positive outcome will
occur again.
Considering Garvin’s [16] building blocks and Brenner’s [17] types of learning,
we think that some correspondencies among the concepts may be worth keeping in
mind for the endeavor of this paper, as indicated in Table 11.1.
11.2.2 Relations Between Crises and Organizational Learning
Crises may be related to various levels—e.g., society, economy as a whole or in a
sector, an organization, or at the personal level of individuals. This paper refers to
organizational crises, which according to Seeger et al. is defined as
“a specific, unexpected, and nonroutine event or series of events that create high levels of
uncertainty and threaten or are perceived to threaten an organization’s high-priority goals”
[18, p. 233]

274 F.WallandP.Campos
The term crisis is distinct from disasters which—according to the organiza-
tional literature—are often caused by natural or mass technological forces and
affect the society or major parts thereof at large scale (e.g., floods, hurricanes,
pandemics). However, disasters may induce crises at the organizational level [18].
According to Weick [19], crises show a combination of low probability and high
consequence events threatening the fundamental goals of an organization. The
following attributes were suggested for constituting a crisis (e.g., [18, 20] with
further references):
1. threat in terms of a discrepancy between aspired and actual/expected achieve-
ments regarding organizational goals;
2. short response time for reducing or confining harm for the organization;
3. surprise once the triggering events happen.
Regarding the relation between organizational learning and crises, at least, four
different perspectives are discussed [1, 4, 21]:
. Learning for Crisis aims at developing reactive capabilities in an organization in
terms of responsiveness once a threatening event happens [4].
. Learning as Crisis refers to crises that may emerge from learning—once the
core beliefs and assumptions (mental models) of key decision-makers are shaken
through learning [4].
. Learning from Crisis captures that organizations learn from their own and
other’s experiences. Learning in this sense is to help precautions and increase
organizational resilience [4, 21, 22].
. Learning in Crisis addresses an integrated concept proposed by [1] that empha-
sizes the relational dynamics between learning and crises—or “the simultaneity
of emergence and emergency” (p. 15).
11.2.3 Barriers of Organizational Learning from Crises
There is considerable evidence that, in organizations, obstacles and resistances for
learning from crises occur (e.g., [1, 4]). Learning from a crisis may happen after
the immediate effects of the crisis-inducing events have abated and the analysis of
the causes for the crisis has started. However, in hindsight, also different views and
narratives, also forming the defense routines of actors show up [2,4]. The motivation
for building up “defense lines” is that key actors may regard the occurrence of a
crisis as a failure, consequence of management errors, or lack of control (e.g., [1, 3,
4, 23]).
Building on previous research and on empirical evidence, Smith and Elliot [4]
condense the obstacles to learning from crisis into a “list” of the eight barriers:
1. Rigidity of core beliefs, values and assumptions: Sticking to beliefs, values and
assumptions is regarded to be among the most influential barriers which may
induce misunderstanding, ignorance or even denial when “things are not as

11 OrganizationalLearningfromCriseswithML/ABM 275
expected”. This obstacle also refers to the path-breaking work of Argyris and
Schön [14] indicating on anti-learning dynamics. Moreover, this barrier refers to
the role of Senge’s [15] “mental models” and the need to eventually adjust them
in organizational learning (see Sect. 11.2.1).
2. Ineffective communication and information difficulties: After a crisis, certain
issues may be subject to distorted communication of various types, including
noise, information overload, excessive expert language, “self-censorship” or even
the (tacit) cultural consent of certain issues not to be discussed. While this barrier
is also considered to be of particularly high relevance in organizational learning
from crisis, it clearly relates to Senge’s [15] “team learning” and Garvin’s [16]
“Transfer of knowledge” (see Sect. 11.2.1).
3. Denial, centrality of expertise, and disregard of outsiders: Discourse about the
crisis may be hampered by the (mis-)use of centralized expertise and preclusion
of perspectives from outside the organization. If this barrier is effective, “learning
from others” as one of the building blocks for a learning organization in Garvin’s
[16] is hampered; it also highlights a downside of “personal mastery” according
to Senge [15] (see Sect. 11.2.1).
4. Peripheral inquiry and decoy phenomenon: The implications carried from a crisis
may focus on well-defined problems, disregarding ill-structured problems. In
this sense, actions on well-defined problems may distract attention from others.
This aspect refers to a narrowed understanding that Senge [15] addresses when
stressing the importance of “systems thinking” (see Sect. 11.2.1).
5. Cognitive narrowing and fixation (reductionist): Focusing on problems that
appear manageable is related to the aforementioned barrier 4, and is particularly
detrimental when the problems or actions interfere. Again, this refers to (a lack
of) “systems thinking” and the importance of (adjusting) “mental models” as
diagnosed by Senge [15] (see Sect. 11.2.1).
6. Maladaption, threat minimization and environmental shifts: A consequence from
sticking to core beliefs and assumptions and ineffective communication (see
barriers 1 and 2) is that inadequate actions are taken that may neglect worst case
scenarios or that threats are not taken seriously which again refers to Senge’s
“systems thinking” and “mental models” [15].
7. Lack of corporate responsibility: According to Smith and Elliot [4] this barrier
leads to organizational members seeking to conform to, while not exceeding
regulatory requirements. This translates to Senge [15] who emphasizes “building
shared visions” as one of his “component technologies” for organizational
learning (see Sect. 11.2.1).
8. Focus on single-loop learning: Smith and Elliot [4] diagnose a prevalence of
single-loop learning from crises, which according to Argyris and Schön is
“instrumental learning that changes strategies of action or assumptions underly-
ing strategies in ways that leave the values of a theory of action unchanged” [24,
p. 20]; in contrast, double-loop learning means the adaptation of organizational
values or norms. Hence, adjustments with single-loop learning refer to the actions
and related assumptions for achieving an aspired performance, while double-
loop learning also relates to the values and norms that define performance.

276 F.WallandP.Campos
This obviously also refers to Senge’s [15] plea for “systems thinking” and the
questioning of the “mental models” as outlined in Sect. 11.2.1.
These considerations uncover that the barriers organizations face in learning from
crises may be related to the framework we outlined above. In particular, we conclude
that the barriers to learning from crises refer to the five “component technologies”
[15, p. 10] for a learning organization that Senge proposes. The next chapter aims
to provide more details on how ML/ABM could support organizational learning.
11.3 Organizational Learning with Agent-Based Models and
Machine Learning: A Framework
11.3.1 Learning in Agent-Based Models
The essence of models that are based on Agents lies in the notion of autonomous
agents whose behavior may evolve endogenously and therefore can generate the
corresponding complex system dynamics that the model is studying [25]. Agent-
Based Models (ABM) constitute a bottom-up approach that allows us to analyze the
effect of interactions of agents as a whole. They characterize economic processes
as dynamical systems of heterogeneous agents, because such heterogeneity, agents’
bounded rationality, and market disequilibria are explicitly taken into account.
According to [26], most work in artificial intelligence is related to the learning
performed by an individual agent and not in a Multi-Agent context. Individual
agents learn to evolve in a dynamic environment that is unknown and changes as
the agent is learning. On the other hand, in a Multi-Agent context, the learning of
the other agents will be impacted by the learning performed by our agent.
Agent-based learning approaches help to solve problems, such as market seg-
mentation, targeting clients and predicting behaviour. There are several taxonomies
of learning, from machine learning to game theoretical perspectives (see [17, 25, 27,
28], and [29], among others).
Machine learning is mainly used in ABM for two main purposes: (1) the
modelling of adaptive agents equipped with experience learning and, (2) the analysis
of outcomes produced by a given ABM [29]. This latter purpose is related to the
analysis of the simulation output: handling the model, understanding the exact
model behavior and extracting meaningful insights from simulation results. We will
focus on the modelling of adaptive agents equipped with experience learning and on
the ability to develop individuals’ mental models. These models are constructed by
individuals based on their unique life experiences, perceptions, and understandings
of the world. This is therefore suitable for the Accountability perspective of
Organizational Learning defined above, where organizational improvement emerges
though the development of individuals’ mental models.

11 OrganizationalLearningfromCriseswithML/ABM 277
11.3.2 A Mapping Between the Five Disciplines and Machine
Learning
As stated above, Organizational learning is regarded as resulting from individuals
adjusting and refining their mental models. We consider that individuals are
responsible for the change of their organizations using mental models. These mental
models allow individuals to understand the world and take action.
Argyris [14] provides a process for learning to change counterproductive inter-
personal dynamics, while Senge [15] proposes that organization members must
engage in a process of learning to understand their own system, rather than
relying upon expert consultants [15]. In both cases, we consider the existence of
mental models. Mental models involves individuals actively using data to test their
interpretations and conclusions. Senge [15] and Argyris and Schön [14] propose
working with the cognitive maps of individuals to create learning organizations.
We advocate that agents can have different cognitive maps and can learn
differentially. In other words, each agent can have its own mental model and
different learning capabilities. This perspective is in line with the egocentric view
of agents where every single individual has its own perspective of the surrounding
world. In the opposite view (allocentric view), agents have a collective or global
representation of that same world [30]. Moreover, we suggest that agents can
have different tasks for which the learning process is specific, and consequently,
it involves a different type of learning. As an example, let us imagine the process
of driving an aircraft. There are different roles for the pilots and the air traffic
controller, who are all responsible for the safety of the aircraft. According to the
US Federal Aviation Administration1 the pilot in command is directly responsible
for its safe operation of the airplane. The co-pilot can share some of the tasks of the
pilot, dividing the work of the plane with the pilot as to who does the flying and
who takes on the other tasks. The air traffic controller is responsible for giving first
priority to separating aircraft and issuing safety radar alerts, second priority to other
services that are required but do not involve separating aircraft and third priority
to additional services to the extent possible. Therefore, the learning tasks can be
different according to who does what. Furthermore, it is sometimes important to
transfer some knowledge between agents.
In the following, we explore the types of Learning in ABMs that can be suitable
for the development of mental models, such as Transfer learning and Prescriptive
Theories. We also suggest a new type of learning that combines with the perspective
of [15]: Systemic learning.
In order to develop the principles of such a “new” type of learning, we need
to define some aspects of the system itself. The whole system can be seen as
an organization where individuals are persons or software agents. An agent can
therefore be a physical or virtual entity. The interaction between software and
1 https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap5_section_5.html.

278 F.WallandP.Campos
humans agents is not new: [31] developed a model for Inducing Models of Human
Control Skills with machine learning models (decision and regression trees) for
reverse engineering with applications to the problem of controlling a simulated
plane. Basten and Haamann [5], consider a Technology Approach of organizational
learning characterized as “any computer-generated physical space”. Virtual worlds
are electronic environments in which individuals interact in a realistic manner in the
form of avatars.
A Multi-Agent System (MAS) is a collection of agents that contains an envi-
ronment, objects and agents. We consider that there are relations between all the
entities, and a set of operations that can be performed by the entities within the
System’s components [32]:
. Agents We may consider that individuals (agents) are one of the most important
parts of the organization (the system); some agents have the ability to learn and
can be autonomous;
. Objects the several parts of the system that are not agents (streets, houses, trees,
etc.)
. Environment the place where agents “live”: it can be a centralized environment,
or a distributed environment; agents are able to interact with the environment
[33], at least partially [32].
Agents are able to communicate with others and interact. An interaction occurs
when two or more agents are brought into a dynamic relationship through a set
of reciprocal actions. Communication is the basis for interactions and social orga-
nization; it is expressed as a form of interaction in which the dynamic relationship
between agents is expressed through the intermediary of mediators or signals, which
once interpreted, will affect the other agents. The environment is as a general term to
denote the medium for agent interaction. Agents and objects are put together in the
environment that can be virtual, or real, discrete or continuous, dynamic or static,
deterministic or stochastic.
The perspective of Systems’ thinking of [15] is tailored within the scope of
organizational learning. It supports that agents’ actions have created their own
reality. In Table 11.2 we map the five disciplines of organizational learning, as
proposed by [15], to the corresponding links with ABM and Machine Learning.
“Personal mastery” is associated goals and objectives to help achieving a vision,
which is well aligned with the cognitive architectures of rational agents developed
by Rao and Georgeff [34]. “Mental models” involve individuals actively using data
to test their interpretations and conclusions and can be seen as personal algorithms,
such as supervised and supervised Machine Learning algorithms. In “Building a
shared vision” individuals learn with others, and transfer knowledge from others.
They may learn by imitation and share advice, constituting the heart for team
learning. The next discipline is “Team Learning”, where individuals think together
in a collective manner, and learn as a whole, similarly to the flocking behavior
algorithms of PSO—Particle Swarm Optimization [40]. PSO applications include
Path planning of multi-robots, Job shop scheduling problem, or Segmentation
of satellite images based on multilevel thresholding, among others. Finally, in

11 OrganizationalLearningfromCriseswithML/ABM 279
|  ekat dna snoitautis sisirc ni roivaheb noitalupop  serutcetihcra evitingoc tnereffid noitaredisnoc ni |  ohw]63[ .la te uomahneB a hcus ,sisirc tneverp |     |  emit ni refsnart egdelwonK serolpxe ]93[ iruosT |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | --- | ------------------------------------------------ |
 ot desu eb nac smhtirogla LM tnereffid lareveS
|                                             |                                              |  ni degreme evah noitneverp sisirc rof smetsys |  sisirc laicnanfi rof OSP no desab sehcaorppA  evitcelloc eht ot staerht ;)]14[ .g.e( noitciderp |
| ------------------------------------------- | -------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
|  fo gnilledom eht erolpxe ]53[ .la te ergeN |  gnitsooB tneidarG htiw stneve sisirc tceted |  gninraw ylrae dna ecnanetniaM evitciderP      |                                                                                                  |
 rof smhtirogla LM weN .seerT noisiceD
?]34 ,13[ enalp detalumis a gnillortnoC
|  )selpmaxe( sisirc fo tceffE |     |  )]83 ,73[ .g.e( sraey tnecer |     |
| ---------------------------- | --- | ----------------------------- | --- |
 )]24[ .g.e( roivaheb
 sisirc fo
 gninraeL enihcaM dna MBA htiw sknil gnidnopserroc eht dna ]51[ egneS fo senilpicsid evfi ehT
 tnereffid fo seitilibissop dna ,)tnega na yb( noitca fo  ecnamrofrep eht evorpmi ot yaw a sa ,gninraelateM
|  seriseD ,)B( sfeileB :sedulcni yllacipyt dna ,stnega  eciohc ,snoitnetni ot tnemtimmoc eht era stpecnoc |  lla tsomla ,weiv fo tniop gninraeL enihcaM a morF  smhtirogla LM desivrepus dna desivrepus fo sepyt |     |  neewteb refsnart egdelwonK .srehto morf gninraeL  gnikcolF ,)OSP( ]04[ noitazimitpO mrawS elcitraP |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------------------------- |
 fo tpecnoc tsesolc eht ebyam si dna SAM ni desu  )nrael ot gninrael( smhtirogla gninrael gnitsixe fo
 ,)CB( gninolC laroivaheB ,]5[ gninraeL noitcA
|  ledom evitingoc a si ]43[ erutcetihcra IDB ehT  lanoitar htiw denrecnoc si tI .yretsam lanosrep |     |     |  gninrael evitcelloc fo sepyt rehto dna roivaheb |
| ------------------------------------------------------------------------------------------------ | --- | --- | ------------------------------------------------ |
|  tnatropmI .)I( snoitnetni dna ,)G( slaog ,)D(                                                   |     |     |  dna ,ecivda gnirahS ,noitatimi yb gninraeL      |
gninraeL enihcaM dna SAM htiw skniL
 sledom latnem sa nees eb nac
 snoitca fo semoctuo
 stnega
 lanosrep s’tnega eht fo gnipoleved suounitnoc htiw  stnegA .noisiv eht gniveihca pleh ot sevitcejbo dna  dna hturt ot tnemtimmoc ,noisnet evitaerc deen osla  noitcartsba na sa sledom latnem nwo rieht gnidliub  gninrael htiw meht wodne dna sledom latnem eseht  dnatsrednu srekam noisiced spleh taht weiv citsiloh
 eht( noisiv deen stnega ,egneS reteP ot gnidroccA  ,slaog ,)esoprup a no desab ,erised yeht taht erutuf  laudividni rieht gninepeed dna tnemnorivne sti fo  dna snoitaterpretni rieht tset ot atad gnisu ylevitca  rehto hcae morf nrael osla nac yeht tub ,smelborp  a si siht :)enilpicsid htffi eht( gniknihT smetsyS .5  dna atad gnoma spihsnoitaler tceffe-dna-esuac eht
|  detaicossa si enilpicsid sihT :yretsam lanosreP .1  .ylevitcejbo ytilaer gniees dna ycneicfiorp ,noisiv |     |  dliub ot elba eb ot atad deen ew os ,snoisulcnoc |  mrofrep nac stnegA :noisiv derahs a gnidliuB .3  evlos ot sgniteem lacihcrareihnon dna yratnulov  htiw od ot sah enilpicsid sihT :gninrael maeT .4 |
| -------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
 lanosrep sa nees eb nac sledom latneM .noisiv  slaudividni sevlovni sledom latneM .smhtirogla
 fo elbapac eb yam stnegA :sledom latneM .2
 sevlovni taht ,yllaudividni gniod yb gninrael  evitcelloc dna laudividni sdnapxe tI .elpoep  dna laudividni sevorpmi dna slliks gnikniht
 gnikam noisiced evitcelloc
]51[ senilpicsid evfi ehT
 rennam evitcaorp a ni
|  scitsiretcarahc rehto |     |     |  ”rehtegot gnikniht“ |
| ---------------------- | --- | --- | -------------------- |
 seitilibapac
2
.11e
lbaT

280 F.WallandP.Campos
“Systems Thinking” there is a holistic view of individuals that improves collective
decision making.
11.4 Types of Organizational Learning in Agent-Based
Models
11.4.1 Prominent Learning Types
11.4.1.1 Transfer Learning
Transfer learning refers to the ability of a program to transfer what it has learned
about one task to help it perform a different, related task [28]. We can call this
Intra-Agent Transfer Methods. For humans, transfer learning is automatic. For
computers, it must be considered in the process of machine learning. But Transfer
learning can also be viewed as a way of learning from other agents, (Inter-Agent
Transfer Methods) given the fact that learning from scratch is impractical due
to the huge sample complexity of algorithms. Reusing knowledge that can come
from previous experience or other agents is indispensable to scale up multiagent
Reinforcement Learning algorithms [44]. The authors consider a situation where
transfer knowledge from one agent to another occurs during the learning process.
11.4.1.2 Sharing Advice
Sharing advice among agents is one of the main approaches to improve agent learn-
ing performance [45]. The existing advising methods share a common limitation:
an adviser agent can offer advice to an advisee agent only if the advice is created
in the same state as the advisee agent’s concerned state. Ye et al. [45] developed a
differential advising method that enables agents to use advice in a state even if the
advice is created in a slightly different state.
11.4.1.3 Knowledge Transfer Between Agents
The literature has shown that the reuse of knowledge in Agent-Based models
might significantly accelerate the learning process [44]. Some approaches of agent-
based learning make strict differentiation between the learning roles: they may act
as teachers or as learner agents. Knowledge transfer and between agents include
different approaches, according to the interaction between involved subjects: indi-
vidualistic, competitive, cooperative ad collaborative [46].
Some authors, however, present agent-based approaches in which agents possess
the ability to act both as a teacher and as a learner [47]. These authors proposed a
framework where each agent possess individual characteristics, such as dimensions,

11 OrganizationalLearningfromCriseswithML/ABM 281
mobility, number and type of sensors, making them unique or at least different from
the other agents. Two different robots were trained based on cognitive maps made by
students—although there were numerous differences in knowledge representation—
to effectively recognize different concepts in their environment, such a hole, a wall
and an obstacle. Interestingly, the robots tried afterwards to exchange acquired
knowledge between them, where one of the robots was capable to teach the other
robot.
11.4.1.4 Prescriptive Theories
Prescriptive theories of learning provide guidelines, recommendations, or pre-
scriptions for how learning processes should occur to optimize outcomes. These
theories focus on the design of instructional methods, strategies, and environments
to facilitate effective learning. Several prescriptive theories of learning have been
proposed in the field of education and instructional design. Prescriptive theories ask
how agents—people, programs, or otherwise—should learn. Their main focus is not
on behavioral properties, but on normative theories, in which individual agents are
self-motivated [27].
11.4.2 Systemic Learning: An Integrated Learning Approach
The performance of a learning model depends on a training dataset, the algorithm
and the parameters of the algorithm. There are situations where several algorithms
compete or collaborate for a solution: algorithms learning to learn. This is the case
of Meta Learning, a subset of machine learning used to improve the results and
performance of a learning algorithm by changing some aspects of the learning
algorithm based on experiment results.
Systemic learning, our proposal for this holistic approach, is built upon the
five disciplines of the learning organization, as stated by [15], and described in
Table 11.3. This holistic view helps the cause-and-effect relationships among data
and people and improves individual and collective decision making, by considering
an integrated learning approach. This integrated approach assumes that learning
is taking place in a decentralized way and that the various learning agents are
heterogeneous. These agents act as components of a system that functions as a whole
and each component may have different functions in the system. Just like in the
human body, the organs work in an integrated way for a common goal. According
to Systemic Theory, the whole emerges beyond the existence of the parts and the
relationships are what give cohesion to the whole system, giving it a character of
totality or globality, one of the defining characteristics of the system [48].
One possible example of Systemic learning is provided by Sun and Naveh [43],
who use a cognitively realistic simulation to capture human performance data in a
radar task. Their model uses Clarion, a project investigating fundamental structures

282 F.WallandP.Campos
Table 11.3 Meta Learning, Hybrid Machine Learning (HML) and Systemic Learning (SL)
according to purpose and algorithmic interaction
Goal Algorithm interaction
Meta Learning Learn, select, alter or combine Algorithms combine the
different learning algorithms to predictions with other
effectively solve a given learning machine learning algorithms
problem
Hybrid Machine To combine different algorithms, In HML, algorithms work in a
Learning (HML) processes, or procedures from complementary manner to
similar or different domains of evolve a more-robust
knowledge or areas of application standalone algorithm
with the objective of
complementing each other
Systemic Learning (SL) Similar to HML, but SL follows Algorithms work in a
the architecture of a system complementary manner as
components of a system that
functions as a whole and each
component may have
different functions in the
system
and mechanisms of the human mind. Clarion contains an integrated cognitive
architecture with a dual representation consisting of two different levels: a top level
that captures explicit learning (done by humans) and a bottom level that captures
implicit learning via reinforcement learning.
The so-called Hybrid Machine Learning (HML) can be seen as a parallel idea of
Systemic Learning. HML combines different algorithms, processes, or procedures
from similar or different domains of knowledge or areas of application with the
objective of complementing each other. One commonly used example is ANFIS—
adaptive neuro-fuzzy inference system [49], a combination of the principles of
fuzzy logic and Artificial Neural Networks (ANN). The architecture of ANFIS is
composed of five layers, where the first three are taken from fuzzy logic, while the
remaining two are from ANN.
However, the idea of Systemic Learning diverges from HML, for while the latter
is based on combining suitable methods or algorithms to solve a problem, the
former explicitly uses the structural architecture of the parts of a system to find the
solution to the whole. In Systemic Learning, the parts are explicitly present in the
problem definition and contribute to its resolution. For example in the problem about
the functioning of an airplane, the Machine Learning algorithms induce human
controllers that model human control skills [31].
We now systematize the ideas of Meta Learning, Hybrid Machine Learning
(HML) and Systemic Learning (SL) according to the corresponding purpose and
algorithmic interaction.

11 OrganizationalLearningfromCriseswithML/ABM 283
11.5 Conclusion
This paper studies how machine learning and agent-based models could contribute
to organizational learning from crises. Organizational learning has been studied
from various perspectives. We adopt the “accountability” perspective as it focuses
on interventions that facilitate the process of developing mental models, which
corresponds to our research agenda: according to the accountability perspective,
organizational learning results from individuals who adjust and refine their mental
models and, thus, improve their decision-making capabilities. Regarded this way,
individuals are accountable for the change of their organizations—with crises
posing particular obstacles for organizational learning. Building on Senge’s [15]
“fifth discipline”, we show how the five disciplines could be potentially linked
and operationalized in Multi-Agent-Systems and Agent-based Models. Moreover,
we briefly discuss prominent learning types in agent-based organizational learning
models. From this, we derive Systemic Learning as an approach that, in principle,
corresponds to Senge’s five disciplines.
The ideas introduced in this chapter clearly await further research: For instance,
the concept of Systemic Learning requires further operationalizations and prototyp-
ical applications. These applications could take at least two forms: First, systemic
learning may be embedded in agent-based simulations of organizations in order to
understand its performance in comparison to other learning types for organizational
learning. Second, systemic learning may be embedded into organizations’ platforms
to foster organizational learning. This latter type of application is obviously closer
to interventions for developing mental models in “real-life” organizations as it is in
the center of the “accountability” perspective of organizational learning.
References
1. E.P. Antonacopoulou, Z. Sheaffer, Learning in crisis: Rethinking the relationship between
organizational learning and crisis management. J. Manag. Inquiry 23(1), 5–21 (2014)
2. D. Elliott, The failure of organizational learning from crisis - a matter of life and death? J.
Conting. Crisis Manag. 17(3), 157–168 (2009)
3. A. Jackson, A. Godwin, S. Bartholomew, N. Mentzer, Learning from failure: A systematized
review. Int. J. Technol. Des. Educ. 32, 1853–1873 (2022). https://doi.org/10.1007/s10798-021-
09661-x
4. D. Smith, D. Elliott, Exploring the barriers to learning from crisis:organizational learning and
crisis. Manag. Learn. 38(5), 519–538 (2007)
5. D. Basten, T. Haamann, Approaches for organizational learning: A literature review. SAGE
Open 8(3), 2158244018794224 (2018)
6. A. Edmondson, B. Moingeon, From organizational learning to the learning organization.
Manag. Learn. 29(1), 5–20 (1998)
7. G.P. Huber, Organizational learning: The contributing processes and the literatures. Org. Sci.
2(1), 88–115 (1991)
8. H.O. Odor, A literature review on organizational learning and learning organizations. Int. J.
Econ. Manag. Sci. 7(1), 1–6 (2018)

284 F.WallandP.Campos
9. R.M. Cyert, J.G. March, A Behavioral Theory of the Firm (Prentice Hall, Englewood Cliffs
(NJ), 1963)
10. B. Levitt, J.G. March, Organizational learning. Annu. Rev. Sociol. 14(1), 319–338 (1988)
11. J.S. Brown, P. Duguid, Organizational learning and communities-of-practice: Toward a unified
view of working, learning, and innovation. Org. Sci. 2(1), 40–57 (1991)
12. R.H. Hayes, S.C. Wheelwright, K.B. Clark, Dynamic Manufacturing: Creating the Learning
Organization (Simon and Schuster, 1988)
13. C. Argyris, D.A. Schön, Theory in Practice: Increasing Professional Effectiveness (Jossey-
Bass, San Fransisco, 1974)
14. C. Argyris, D.A. Schön, Organizational Learning: A Theory of Action Perspective (Addison
Wesley, Reading (MA), 1978)
15. P.M. Senge, The Fifth Discipline: The Art and Practice of the Learning Organization
(Doubleday, New York, 1990)
16. D.A. Garvin, Building a learning organization. Harv. Bus. Rev. 71(4), 78–91 (1993)
17. T. Brenner, Chapter 18: Agent learning representation: advice on modelling economic learning,
in Handbook of Computational Economics, vol. 2 (Elsevier, 2006), pp. 895–947
18. M.W. Seeger, T.L. Sellnow, R.R. Ulmer, Communication, organization, and crisis. Ann. Int.
Commun. Assoc. 21(1), 231–276 (1998)
19. K.E. Weick, Enacted sensemaking in crisis situations. J. Manag. Stud. 25(4), 305–317 (1988)
20. J. Wang, Developing organizational learning capacity in crisis management. Adv. Dev. Hum.
Resour. 10(3), 425–445 (2008)
21. K. Eismann, O. Posegga, K. Fischbach, Opening organizational learning in crisis management:
On the affordances of social media. J. Strateg. Inf. Syst. 30(4), 101692 (2021)
22. C. Lalonde, Managing crises through organisational development: a conceptual framework.
Disasters 35(2), 443–464 (2011)
23. E.P. Antonacopoulou, R. Chiva, The social complexity of organizational learning: The
dynamics of learning and organizing. Manag. Learn. 38(3), 277–295 (2007)
24. C. Argyris, D.A. Schön, Organisational Learning II: Theory, Method, and Practice, 2nd edn.
(Addison-Wesley, Reading, 1996)
25. S.-H. Chen, C.-C. Tai, Republication: On the selection of adaptive algorithms in ABM: A
computational-equivalence approach. Comput. Econ. 28, 313–331 (2006)
26. Y. Shoham, K. Leyton-Brown, Multiagent Systems: Algorithmic, Game-Theoretic, and Logical
Foundations (Cambridge University Press, New York, 2009)
27. Y. Shoham, R. Powers, T. Grenager, If multi-agent learning is the answer, what is the question?
Artif. Intell. 171(7), 365–377 (2007)
28. M. Mitchell, Artificial Intelligence: A Guide for Thinking Humans, 1st edn. (Farrar, Straus and
Giroux, 2019)
29. K. Bogner, M. Müller, A. Pyka, B. Ebersberger, T. Berger, J. Dahlke, Is the juice worth the
squeeze? Machine learning in and for agent-based modelling: a preprint. Technical report,
2020
30. T. Wagner, U. Visser, O. Herzog, Egocentric qualitative spatial knowledge representation for
physical robots. Robot. Auton. Syst. 49(1–2), 25–42 (2004), ISSN 0921-8890. https://doi.org/
10.1016/j.robot.2004.07.022
31. R. Camacho, P. Brazdil, Improving the robustness and encoding complexity of behavioural
clones, in Machine Learning: ECML 2001 (2001), pp. 37–48
32. J. Ferber, Multi-Agent Systems: An Introduction to Distributed Artificial Intelligence (Addison
Wesley Longman, Harlow, 1999)
33. M. Wooldridge, An Introduction to Multiagent Systems (Wiley, New York, 2002)
34. A. Rao, M. Georgeff, BDI agents: from theory to practice, in Proceedings of the First
International Conference on Multi-Agent Systems (ICMAS-95) (1995), pp. 312–319
35. E. Negre, M. Arru, C. Rosenthal-Sabroux, 7-Toward a modeling of population behaviors in
crisis situations, in How Information Systems Can Help in Alarm/Alert Detection (Elsevier,
Amsterdam, 2018), pp. 199–218, ISBN 9781785483028. https://doi.org/10.1016/B978-1-
78548-302-8.50007-1

11 OrganizationalLearningfromCriseswithML/ABM 285
36. E. Benhamou, J.J. Ohana, D. Saltiel, B. Guez, Detecting crisis event with Gradient Boosting
Decision Trees (2021). hal-03320297. https://hal.science/hal-03320297/document
37. S. Voronov, Machine learning models for predictive maintenance, PhD dissertation, Linköping
University Electronic Press, 2020. https://doi.org/10.3384/diss.diva-162649
38. J. Moon, F. Sasangohar, C. Son, S.C. Peres, Cognition in crisis management teams: an
integrative analysis of definitions. Ergonomics 63(10), 1240–1256 (2020). https://doi.org/10.
1080/00140139.2020.1781936
39. M. Tsouri, Knowledge transfer in time of crisis: evidence from the Trentino region. Ind. Innov.
26(7), 820–842 (2019). https://doi.org/10.1080/13662716.2018.1551124
40. J. Kennedy, R. Eberhart, Particle swarm optimization, in Proceedings of ICNN’95 - Inter-
national Conference on Neural Networks, Perth, WA, Australia, 1995, vol. 4 (1995), pp.
1942–1948. https://doi.org/10.1109/ICNN.1995.488968
41. X. Huang, Construction and analysis of financial crisis prediction based on particle swarm
optimization algorithm, in 2021 3rd International Conference on Artificial Intelligence and
Advanced Manufacture (AIAM2021) (Association for Computing Machinery, New York, NY,
2022), pp. 882–886. https://doi.org/10.1145/3495018.3495296
42. B. Afsharizand, P.H. Chaghoei, A.A. Kordbacheh, A. Trufanov, G. Jafari, Market of stocks
during crisis looks like a flock of birds. Entropy 22(9), 1038 (2020). https://doi.org/10.3390/
e22091038
43. R. Sun, I. Naveh, Simulating organizational decision-making using a cognitively realistic agent
model. J. Artif. Soc. Soc. Simul. 7(3), 1–5 (2004). https://www.jasss.org/7/3/5.html
44. F.L. Da Silva, A.H.R. Costa, A survey on transfer learning for multiagent reinforcement
learning systems. J. Artif. Intell. Res. 64, 645–703 (2019). https://doi.org/10.1613/jair.1.11396
45. D. Ye, T. Zhu, Z. Cheng, W. Zhou, P.S. Yu, Differential advising in multiagent reinforcement
learning. IEEE Trans. Cybern. 52(6), 5508–5521 (2022). https://doi.org/10.1109/TCYB.2020.
3034424
46. D.W. Johnson, R.T. Johnson, The impact of cooperative, competitive, and individualistic
learning environments on achievement, in International Handbook of Student Achievement,
ed. by J. Hattie, E. Anderman (Routledge, New York, 2013), pp. 372–374
47. G. Zaharija, S. Mladenovi, A. Grani. Learning from each other: an agent based approach,
in Universal Access in Human-Computer Interaction. Universal Access to Information and
Knowledge. UAHCI 2014, ed. by C. Stephanidis, M. Antona. Lecture Notes in Computer
Science, vol. 8514 (Springer, Cham, 2014), pp. 475–486. https://doi.org/10.1007/978-3-319-
07440-5_44
48. M.J.E. de Vasconcellos, Pensamento sistêmico: o novo paradigma da ciência. 10. ed. (Papirus,
Campinas, 2010)
49. F.A. Anifowose, Ensemble machine learning: the latest development in computational intel-
ligence for petroleum reservoir characterization, in Paper presented at the SPE Saudi Arabia
Section Technical Symposium and Exhibition, Al-Khobar, Saudi Arabia, May 2013 (2013).
https://doi.org/10.2118/168111-MS

Chapter 12
Strategic Alliances in NetLogo: A
Flocking Algorithm with Reinforcement
Learning
Sónia Teixeira and Pedro Campos
12.1 Introduction
In Economics and Management Sciences, the evolution of markets forces firms
to adopt new strategies. One of these strategies involves establishing formal or
informal agreements with other organisations. Whenever two or more organisations
share resources, activities and join forces to achieve a common goal, they form
a strategic alliance (Johanson and Mattsson, [1], and Aaker, [2], and Eiriz [3]).
Organisations belonging to an alliance aim to gain a competitive advantage over
other organisations outside the alliance. Collaboration between organisations, as an
alternative or in parallel to competition, allows them to get the edge over other
competitors in the same market or on potential new organisations [4]. Coopetition
is a situation where competitors cooperate and compete simultaneously (Dagnino
and Padula, 2000, in [5]). This is the behaviour we can find in strategic alliances
where, after all, cooperation is more often observed than competition [6]. More
recently, Tlemsani et al. [7] used game theory and simulations to model the evolu-
tion and effectiveness of international strategic learning alliances, analyzing 1200
cases to understand the costs, benefits, and success factors of inter-organizational
cooperation. The findings provide practical insights for firms on aligning strategies
with institutional risks and opportunities, contributing to the broader understanding
of complex strategic partnerships. In this work, we explore the computational
concept of flocking behaviour as a paradigm for analysing the intelligent collective
behaviour that emerges from a strategic alliance. Flocking behaviour algorithms
S. Teixeira
University of Porto, LIAAD-INESC TEC, Porto, Portugal
e-mail: sonia.c.teixeira@inesctec.pt
P. Campos (@)
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 287
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_12

288 S.TeixeiraandP.Campos
belong to a broader set of algorithms called swarm intelligence, which is self-
propelled particles. Proposed initially by Vicsek et al. [8], self-propelled particle
algorithms consider a group of particles, each of which acts as an autonomous agent.
Each follows the same simple rules as to how to regulate their behaviour. A flocking
is a form of collective behaviour of a large number of agents that interact with a
common goal of the group [9]. The algorithm of flocking behaviour is a simulation
method that uses simple rules, being appropriate to simulate the behaviour of
a group of linked organisations that moves in accordance with a common goal.
Since one of our goals is to understand the complex behaviour of this system, we
have used an agent-based approach, where each agent represents an organisation.
An agent is defined as “a real or abstract entity that can act on herself and her
environment, which has a partial representation of this environment, where in a
multi-agent universe they can communicate with other agents, and whose behaviour
is a result of their observations, their knowledge and their interactions with other
agents” Ferber and Gasser in [10]. Agent-based simulation has evolved over the
last decades. According to Gilbert [11], this type of simulation is characterised by
several agents interacting between them, with a few or without central coordination.
Axtell [12–14] proposed computational modelling based on agents as the only
way to explore social underlying processes. In 2007, Epstein mentioned that this
kind of modelling was essential for understanding complex social phenomena [15].
In strategic alliances, organisations often share their values and goals, and for
that reason, we consider a metric that takes into account the expectations of the
organisations involved in the alliance. This metric is the Shapley Value. We also
consider that organisations learn through interactions within the alliances where
they belong [16]. The environment reacts and assigns rewards that organisations try
to maximise over time. We use reinforcement learning to implement the learning
mechanism in the flocking behaviour.
Five parameter settings were analysed to better understand the application of
flocking behaviour to strategic alliances. We evaluated the algorithm’s average
number of iterations, the average permanence rate, and the average growth rate of
organisations in each alliance. We confirmed the convergence of AllFlock and the
reduction in the number of organisations over time.
The work is structured as follows: Sect.12.2 introduces the Swarm Intelligence
concept and algorithms. In Sect.12.3, Reinforcement Learning is presented. In
Sect.12.4, our simulation model using NetLogo is described. Section 12.5 is
devoted to the results and the conclusion.
12.2 Swarm Intelligence and Flocking Behaviour Algorithms
The terminology used by Saminen in [17] mentions swarm intelligence to refer
to emergent collective behaviour in simple agents. On the other hand, collective
intelligence in humans is a relatively new and multidisciplinary subject. Since the
appearance of the name of collective intelligence many other approaches arose,

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 289
as purely theoretical, conceptual, for simulations, case studies, experiences and
systems architecture [17]. Areas such as psychology, complexity, cognitive studies,
biology, computer science and the media also gave their contribute to this multi-
disciplinary theme [17]. Swarm algorithms [18] are based on social and collective
behaviour that is observed in ants, birds, or insects. Ant colony optimization (ACO),
particle swarm optimization (PSO), as well as self-propelled particle algorithms
(SPP) [8], are part of the class of swarm intelligence algorithms. The term self-
propelled particles originated with the flocking algorithm proposed by Vicsek et al.
in [8], which describes a group of particles, each acting as an autonomous agent
and each following the same simple rules as a way to regulate their behaviour.
The intelligence of these same systems is triggered by the collective behaviour
of individuals, that is, interactions between individuals lead to the emergence of
a global intelligent behaviour, named collective intelligence [19]. The flocking has
been seen by Olfati-Saber [9], as “a form of collective behaviour of a large number
of agents that interact with a common group goal”. This complex movement caught
the attention of Reynolds, who in 1987 proposed a simulation-based approach to
the flock movement [20]. This movement, very similar to a natural flock, is created
by a distributed behavioural model in which each bird acts as an independent agent
and chooses its course. In the past few years, other authors applied the paradigms of
Swarm Intelligence and Flocking behaviour to management and industry: Yelisetti
[21] developed an optimal energy management system for residential buildings with
swarm intelligence algorithms.
Beaver and Malikopoulos [22] review optimization-based approaches to robotic
flocking with a focus on safety and performance guarantees.
The flocking behaviour is the result of the interaction of simple behaviours
of agents, represented by rules. The starting point for the Cucker and Smale (C-
S) model [23], one of the most important algorithms of flocking, arises from an
extension of the same authors [24], in which an analysis is made to the flocking
model from Vicsek et al. [8]. Motivation for such extension was the observation
that under certain initial conditions of the state the flock converges, i.e. all birds fly
at the same velocity. The proposed development model [23], uses three important
parameters namely position, velocity and influence and aims at searching for the
conditions for the state under which the convergence is established. We propose an
innovative extension [25] of the flocking algorithm of [23] where the position is
viewed as the choice of potential partner organization, velocity is the performance
of the organization when compared to the alliance (measured as the growth of the
net income between two time steps) and influence is measured through the Shapley
Value [26, 27], intending to divide goods gained by the cooperation among many
organizations. We also consider that organizations learn through interactions within
the alliances where they belong. Reinforcement learning [28] is the method we use
to implement the learning mechanism in the flocking behaviour. The permanence
rate and the growth rate of the alliances were computed by each of the five
configurations in analysis. The permanence rate was also computed for simulated
and real data, by each alliance [25, 29].

290 S.TeixeiraandP.Campos
12.3 Reinforcement Learning
Reinforcement learning (RL) is an area of machine learning concerned with how
intelligent agents ought to take action in an environment to maximize the notion
of cumulative reward. Reinforcement learning can be seen as a machine learning
paradigm, together with supervised and unsupervised learning. Simplistically,
reinforcement learning can be explained as learning through interaction with the
environment or with other agents to achieve a goal or solve a problem [16, 30].
The environment reacts to the agent by assigning rewards and numerical values
that the agent attempts to maximise over time [16]. Reinforcement learning may
take into account a temporal difference method (TDM). The temporal difference
methods estimate the utility values obtained from successive state transitions for
each state of the environment.
12.3.1 Exploration Component
One of the issues addressed in reinforcement learning relates to the duality of
exploitation and exploration. In the situation where the agent should learn what
action to take, the agent should benefit from previously obtained information or
explore the environment. The exploration methods’ purpose seeks to address this
duality, for example, E. -greedy methods, Softmax, and heuristic methods.
12.3.1.1 E. -Greedy
The strategy used in the E. -greedy method gives rise to exploration. The E. -greedy
method consists of a probabilistic choice between the action that maximises the
value of the function Q for state s, and any random selection action with probability
E. . The most valued action in the function Q occurs with a probability 1-E. . This
method attempts to balance the duality between exploitation and exploration. One
of the most recent changes totheE. -greedy method resulted in the VDBE-Boltzmann
(Value-Based Difference Exploration) exploration method proposed in 2010 by
MichelTokic[31].Thismethodassociatestoeachstates aprobabilityofexploration
E. , an amount that fits with knowledge on the environment, function Q associated,
are changing [?]. By an adaptation of the Boltzmann distribution to the variation of
the estimated values of the function Q, in each state s, proposed by Tokic [31]:
| |
f (s,a,σ)=
1−e − Qt+1(s,a
σ
)−Qt(s,a)
(12.1)
. t | |
1+e − Qt+1(s,a
σ
)−Qt(s,a)

| 12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... |     |     |     | 291 |
| -------------------------------------------------------- | --- | --- | --- | --- |
In  states  where  the  agent  has  less  knowledge  of  the  environment,  where  the
variation  of  the  updated  function  Q  is  high,  the  agent  explores  more.  The  degree
of  exploration  versus  the  variation  of  knowledge  is  shaped  by  σ. ,  a  parameter  for
reverse  sensitivity.  Let ∈ ]0,+∞[ .  Concerning  exploration  rate  ,  this  has  a
|     | σ   | .   |     | E.  |
| --- | --- | --- | --- | --- |
greater  influence  when  the  value  of  reverse  sensitivity  is  lower.  The  exploration
rate  decreases  as  variations  of  knowledge  of  each  state  s  also  decrease.  When  the
variations are zero, the rate of exploration is also zero.
|     | ε =δ∗f | (s,a,σ)+(1−δ)∗ε | (s) | (12.2)  |
| --- | ------ | --------------- | --- | ------- |
|     | . t+1  | t               | t   |         |
The degree of influence of each action in the exploration rate is indicated by the
∈[0,1]. It is suggested in the literature that due to good
| quality parameter δ. Withδ | .   | .   |     |     |
| -------------------------- | --- | --- | --- | --- |
results,  the  value  δ is  the  inverse  of  the  possible  number  of  actions  for  each  state
.
[32].
| 12.3.1.2  SoftMax  |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
The SoftMax exploration method is one of the most widely used in the literature. It
is based on assigning selection probabilities to each stock according to its estimated
value,  such  that  each  possible  action  in  a  given  state  is  assigned  a  probability
proportional  to  its  relative  weight  within  the  overall  set  of  options  [33].  The
probability is defined as:
e Qt(a)/τ
= σ
|     |     | . P(a) t E |     | (12.3)  |
| --- | --- | ---------- | --- | ------- |
|     |     | k Qt( b)/τ |     |         |
e σ
b =1
where  the  parameter  τ represents  the  temperature,  which  can  vary  in  the  range
.
]0,+∞[. In this method, as the agent’s knowledge increases, actions with a higher
.
value of the Q function will be privileged.
| 12.3.2  Learning Component  |     |     |     |     |
| --------------------------- | --- | --- | --- | --- |
The  way  environmental  information  is  processed—and  how  values  are  stored—
depends  on  the  selected  algorithm,  which  in  turn  shapes  the  learning  process
(Rummery,  [33]).  In  learning,  methods  have  distinguished  the  concept  of  a  state-
value  function  and  a  value-action  function.  The  state-value  function  acquiring
knowledge  only  increases  the  importance  of  the  state,  while  the  value-action
function is valued the pair state-action.

292 S.TeixeiraandP.Campos
12.3.2.1 Q-learning
Q-learning mechanisms [34] do not consider the value of the action selected by the
exploration method but the value of the most valued action in that same state. Q-
leaning consists of updating, at each step, the action-value function (Q function)
with the value of the most valued action in the current state. That is, the value
of a state is directly proportional to that of the action with the highest value. It
can be selected [35]. Update of the action-value function, according to the learning
expression:
L L
) (
Q(s,a)=Q(s,a)+α r +γ ·maxQ s ' ,a ' −Q(s,a) (12.4)
.
a'
The discount factor γ, also known as the amortization rate, determines the degree
.
of influence that future values have on the return. If γ approaches 0 the agent
.
focuses on immediate reinforcements. If γ approaches 1, the agent considers future
.
reinforcements relevant. If γ is exactly 1, it does not matter to the agent whether the
.
reinforcement is future or present.
12.3.2.2 SARSA
The SARSA mechanism is similar to Q-learning in that the Q function is updated at
each step through the expression for the agents’ Q learning [33]. In Q-learning, the
update of the value-action function does not occur by considering the value of the
action selected by the exploration method. While in SARSA the update is always
takenthroughthevalueoftheactionselectedbytheexploration method.Thus,when
all possible actions for a state are valued, the algorithm will tend to be slower in its
convergence. The expression for the learning engine evaluates all possible actions
in a given state:
L ) ( L
Q(s,a)=Q(s,a)+α r +γ ·Q s ' ,a ' −Q(s,a) (12.5)
.
12.3.2.3 Hierarchical Mechanism
The hierarchical mechanisms divide the problem to solve into sub-problems, and
each sub-problem has its purpose [36]. In this learning mechanism, the values of
the function Q are individualised for each specific task. A learning mechanism
introduced by Dietterich in 2000 was the Hierarchical Semi-Markov Q-Learning
(HSMQ) mechanism, presented as a Q-learning extension:
L L
) (
Q(p,s,a)=(1−α)·Q(p,s,a)+α r +max·Q p,s ' ,a ' (12.6)
.
a'

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 293
In HSMQ it is possible to integrate many hierarchical tasks in a single algorithm.
That is possible without decomposing the value-action function in several compo-
nents from diverse contributions of primitive actions and sub-tasks [37].
12.4 Simulation Using NetLogo
The simulations carried out within the scope of this work were developed using the
NetLogo simulation environment, version 5.2.0. One of the biggest advantages of
using NetLogo for agent-based models is its simplicity and accessibility for rapidly
building and visualizing complex simulations. In this section, we will discuss the
environment, interface, and initialization of the proposed model. Finally, we will
present the pseudo-code used.
NetLogo is free and open-source software, allowing the authoring of new
models and modifying existing models. Besides the NetLogo Desktop (the standard
version), there is also the NetLogo Web, that runs in your browser. No installation
is required in the latter, being great for quick demonstrations and teaching. Uri
Wilensky created NetLogo at Northwestern University in the United States [38]. Its
development and maintenance are the responsibility of The Center for Connected
Learning and Computer-Based Modeling (CCL) [39].
The Netlogo modeling environment is particularly focused on the modeling and
simulation of natural and social phenomena. The simple use of this environment is
one of its biggest advantages, despite its application in several areas of knowledge
(for example: computer science, economics and social psychology), as well as
by other users who have strong programming knowledge. Another strength is the
possibility of modeling complex systems that change over time. Modelers and
users can define rules and give instructions to a large number (hundreds or even
thousands) of agents who can act independently. In this way, it is possible to vary
the agents at the micro level and analyze the consequences of this behaviour at the
macro level, that is, to explore the emergence of behaviours.
The NetLogo world is a two-dimensional world made up of four types of agents:
turtles, patches, links and the observer. Patches represent the ground over which
turtles move. Turtle-type agents are the ones that move around the world, the ones
on which our simulation hypotheses focus. On the other hand, link-type agents
represent the connections between turtles, while the observer is the agent that
monitors everything happening in the simulation.
12.4.1 Model
The original C-S model relies on three key parameters—position, velocity, and
influence—to explore the conditions under which convergence occurs. In our model
(AllFlock—Flocking in Strategic Alliances), we introduce an innovative adaption

294 S.TeixeiraandP.Campos
Fig. 12.1 Setup button
of the flocking algorithm to the context of strategic alliances, where position
represents the selection of a potential partner organization (choice), velocity reflects
the organization’s performance relative to the alliance (measured by the growth in
net income between two time steps), and influence is quantified using the Shapley
Value. For the development of the model, an environment was initially created in
which all agents are presented. For the purposes of this study, we consider that
the agents in the flocking model correspond to aviation companies, since there are
several airline alliances in this industrial sector (such as Star Alliance, Sky team and
One world, among others). Each agent has a set of rules that define its behaviour
and are updated at every iteration. It is intended to assess whether there are signs
of convergence, given the influencing rules and variables. Generaly, convergence is
related to flocking behaviour (when birds fly at the same velocity). In this model,
convergence is related to choice or preference of a potential partner organization.
This occurs when the difference between the preference ranking matrices at two
consecutive moments is close to zero. In order to facilitate the interpretation and
the bridge between the model and the simulation, we defined the following model
parameters:
• σ: exploitation rate vs knowledge
.
• δ: exploitation rate quality
.
• γ : discount factor
.
• Time: evaluation time for remaining in the alliance
• C (t): outcome of an organization i, growth compared to the alliance
i .
• L (t): Net result of an organization i
i .
• r: reward
• E: exploitation probability
.
• α: learning speed
.
To better describe the purpose of AllFlock1 and its process, the pseudocode is
presented:
12.4.2 Interface
Generally, the models in Netlogo use the button setup (Fig.12.1) to introduce the
agents in the world, and a button go (Fig.12.2) that starts the simulation.
1 The code presented throughout the chapter represents only part of three, in seven, procedures of
the AllFlock model. Please contact the first author for more details about the NetLogo code and
AllFlock model.

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 295
Algorithm 1 AllFlock pseudocode
1: Initialize variables
2: while convergence is not reached do
3: for each organization i do
4: Compute and update variables:
5: Compute weight of Growth, Impact of the alliance and Choice
6: Compute Growth expression
7: Update net profit
8: Compute Impact of the alliance on organization i
9: Compute reward or punishment
10: Compute learning velocity
11: Compute Choice expression
12: Take actions:
13: Move forward with growth value
14: Follow organization with the maximum value of choice expression
15: Decide to remain or not, or evaluate to remain in the same alliance
16: end for
17: Verify convergence
18: end while
Fig. 12.2 Go button
Fig. 12.3 Slider
In Fig.12.4, as an example, we present the Netlogo interface for our model after
performing setup. By clicking on the go button on the interface, it will continuously
execute the commands until the algorithm converges or the user clicks on it again
to shut it off. The go button has a small symbol in the lower right corner (Fig.12.2),
indicating that the model will be executed until it finds a stop condition when
activated.
The interface of the AllFlock model also has five sliders (Figs.12.3 and 12.4),
which allow us to vary the value of the five variables between the stipulated values.
Theinitial-number-firmvariableindicatesthenumberoforganizations,ofagents,
that appear in the world at time zero (ticks: 0) after performing setup. The slider
variables: sigma, delta and discount, contains the values of the respective variables
in the agents’ learning process. Finally, the slider time is the variable that defines
how long an organization, (an agent) is willing to assess its growth and the impact
of the alliance before deciding whether to remain in the alliance or not. As shown in
Fig.12.4, twenty agents of three different colours are distributed worldwide. Each
agent is an organization. In this case, they are represented by a house. The three grey
boxes represent organizations belonging to the same alliance. The agents in brown
form a second alliance, while the green agents belong to a third, distinct alliance.
Through the interface of the AllFlock model, it is possible to adjust the settings
for different scenarios to be explored, as well as hypotheses. That is, it is possible to
analyze the behaviour of the aviation companies of the different alliances. The slider

296 S.TeixeiraandP.Campos
Fig. 12.4 NetLogo interface for AllFlock
Fig. 12.5 Edit initial-number-firm slider
represents a range of numeric values, with defined minimum and maximum limits.
Only the slider corresponding to the initial number of companies is not involved in
the AllFlock machine learning engine among the five sliders.
By right-clicking and selecting edit, we can observe or change the stipulated
values for the slider. For example, in the initial-number-firm slider (Fig.12.5), we
can see that the minimum number of organizations is zero, and the maximum
number is 50, with an increment of one organization.

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 297
Fig. 12.6 Edit sigma slider
Fig. 12.7 Edit delta slider
Fig. 12.8 Edit discount slider
Fig. 12.9 Edit time slider
The sliders that present the Reinforcement Learning variables, sigma, delta and
discount and their respective values can be seen in Figs.12.6, 12.7, and 12.8.
Finally, the last slider corresponds to the time variable (Fig.12.9), with a
minimum value of 3, a maximum of 10, and increments of one unit.

298 S.TeixeiraandP.Campos
Fig. 12.10 Making the setup button (Source: NetLogo tutorial)
12.4.3 Procedures
It is necessary to create seven procedures in NetLogo so that it is possible to
represent the AllFlock model. These procedures are: setup, go, grow, death, choose,
factorial, and Shapley. However, we will emphasize the procedures: setup, go and
choose. The latter refers to learning between companies from different strategic
alliances using reinforcement learning.
12.4.3.1 Setup
The setup procedure corresponds to the settings of the setup button to start the
simulation. So, there must be a procedure for the button created in the interface.
When creating the setup procedure, in its simplest form, the code looks like this
(Fig.12.10).
In that code, clear-all resets the world, i.e. all turtles disappear, and all patches
turn black. Then, the world restores its initial empty state and is ready for the model
to run. With the create-turtles command, it is possible to create the number of turtles
and stipulate the commands for the new turtles to execute. In parentheses are the
execution commands for the new turtles. Within parentheses, the command setxy
random-xcor random-ycor defines the movement of each turtle to the point of the
coordinates found through the random-xcor (random number on the x-axis) and by
the random-ycor (random number on the y-axis) (Fig.12.11 and 12.12).
For the setup configuration to be complete, it is necessary to include the reset-
ticks (Figs. 12.12 and 12.13). This command starts the tick counter.
In the AllFlock model, the setup procedure considers the seed (if it is random
or fixed). Also, we define the shape, size and colour of the turtles (organizations),
and we initialize the variables corresponding to the reinforcement learning and the
turtles (organizations). In the case of turtles, the decision matrix is initialized based
on the choices made by other organizations within their alliance and their growth as
individual entities.

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 299
Fig. 12.11 Turtle movement
in the world (Source:
NetLogo tutorial)
Fig. 12.12 Procedure for setup button, with some initial variables configuration
Fig. 12.13 The end of setup
procedure for AllFlock
12.4.3.2 Go
The introduction of the go button and the associated procedure occurs similarly to
the setup button and procedure (Fig.12.14).
The simplest procedure in the case of go has the following structure (as shown in
the NetLogo User Manual, Fig.12.15):

300 S.TeixeiraandP.Campos
Fig. 12.14 Making the go button in AllFlock (based on NetLogo tutorial)
Fig. 12.15 Add a go
procedure to the Code tab
(Source: NetLogo tutorial)
Fig. 12.16 Add the
move-turtles procedure
(Source: NetLogo tutorial)
As we can see, in Fig.12.15, the g o procedure includes the move-turtles
procedure (which we have to define) and the ticks procedure (which counts the ticks
one by one).
In the go procedure, the turtles indicate which movement they should perform. In
the example of the NetLogo User Tutorial, Fig.12.16, we can observe the Netlogo
commands that make this movement possible. The ask turtles [ ...] command asks
turtles to do the movements between brackets (Fig.12.17). First, each turtle picks a
random value between 0 and 359. After that, the turtle (i.e., a firm, or organization)
turns with the selected value and finally, the turtle moves forward one step. Our
go procedure relies on agents’ longevity, algorithm convergence, updated growth
values, choice values, and the movement of turtles (organizations).

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 301
Fig. 12.17 Ask turtles command
Fig. 12.18 Preference
weights
Fig. 12.19 Exploration vs Exploitation
In the AllFlock model, organizations move differently than shown in the tutorial,
since the direction of each turtle (organization) is not predefined by a certain angle.
Instead, the movement of each turtle is performed according to the maximum value
of the preference in collaborating with other turtles, which allows changing the
turtle’s direction to follow in each iteration [29]. The organisation’s growth relative
to the alliance defines how much they move [25].
12.4.3.3 Choose
A given organisation chooses the following organization to maximize the benefits of
collaboration. This preference of which organization to follow depends on growth,
choice and influence of the alliance in previous moments [25]. However, the
AllFlock model considers that depending on their aspirations, each organization
assignes a different importance to each of these three aspects. The pe(t), ps(t) and
pc(t) are the weights with which organization assigns choice, influence and growth,
respectively [25, 29]. Initially these weights are randomly assigned in Netlogo
(Fig.12.18).
A very relevant aspect of AllFlock is related to the exploratory and learning com-
ponents of reinforcement learning [25, 29]. In AllFlock, the E . -greedy method has
adapted, specifically, the VDBE-Boltzman. Figure 12.19 represents this adaptation,
and the calculation of the probability function, the probability that a given action
will be selected by each organization in the next step.

| 302 |     |     |     |     | S.TeixeiraandP.Campos |     |
| --- | --- | --- | --- | --- | --------------------- | --- |
Fig. 12.20  Netlogo choice function
Fig. 12.21  Cooperation
within the alliance
Fig. 12.22  Reward or punishment to agents in the same alliance
Therefore, denoting byE (t), the choice at time t; the influence of the al lianceis
ij .
S (t), and the growth of the organization i at time t isC (t), we write the following
| i . |     |     |     |     | i . |     |
| --- | --- | --- | --- | --- | --- | --- |
equation:
)
| E (t +h)=(1−α)∗ |     | E   | (t)∗pe | (t)+S (t)∗ps | (t) |     |
| --------------- | --- | --- | ------ | ------------ | --- | --- |
| ij              |     | ij  |        | i i          | i   |     |
L
|     | +C (t)∗pc | (t)))+α∗ |       | +γE    | (t)∗ |         |
| --- | --------- | -------- | ----- | ------ | ---- | ------- |
| .   | i         | i        |       | r      | ij   | (12.7)  |
|     | pe (t)+S  | (t)∗ps   | (t)+C | (t)∗pc | (t)] |         |
|     | i         | i        | i     | i      | i    |         |
In NetLogo, this equation corresponds to the code shown in Fig.12.20.
Organizations  assess  their  cooperation  with  the  other  organizations  in  their
alliance to choose the direction to follow (Fig.12.21).
When  a  specific  organization  is  looking  for  the  best  direction  to  go,  the
organization that maximizes the choice expression collects information throughout
their  interactions  in  respect  of  previous  choices,  giving  a  reward  or  a  punishment
(Fig.12.22).

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 303
12.5  Results, Discussion and Conclusion
In the simulation process of the proposed model, we performed 100 simulations for
each  of  the  five  cases  in  question,  presented  in  Table  12.1.  The  initial  number  of
organisations set by the user was 10.
The final results are the average of the 100 simulations in their different number
of iterations.
In  the  result  of  the  100  simulations  performed,  we  obtained  evidence  of
convergence  at  configuration  2,  iteration  106.  Configuration  2  is  the  configuration
with  the  highest  average  number  of  iterations.  The  configuration  that  presents,  on
average, fewer iterations occurs in configuration 4 (Fig.12.23).
The  AllFlock  model  (Flocking  in  Strategic  Alliances)  proposed  in  this  Chapter
was  intended  to  replicate  the  way  organizations  act  in  terms  of  flocking  behavior.
AllFlock  models  the  intragroup  behavior  where  each  agent  knows  the  decisions
of  the  other  agents  (organizations)  belonging  to  the  same  alliance.  There  are  two
important  decisions:  (1)  What  company  to  follow  (based  on  a  combination  of  the
| Table 12.1  Parameters of configurations  |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- |
Parameters
|                  | The initial    | Exploration rate  |                  |              |
| ---------------- | -------------- | ----------------- | ---------------- | ------------ |
|                  | number of      | vs. knowledge     |                  | Evaluation   |
|                  | organisations  | (Sigma)           | Delta  Discount  | time (time)  |
| Configuration 1  | Low            | Low               | High  High       | Low          |
| Configuration 2  | Low            | Low               | High  High       | High         |
| Configuration 3  | Low            | Low               | High  Moderate   | High         |
| Configuration 4  | Low            | Moderate          | High  High       | Low          |
| Configuration 5  | Low            | Moderate          | High  High       | High         |
Fig. 12.23  Average number of iterations

304 S.TeixeiraandP.Campos
utility function—Choice—and the Growth; (2) The decision of remaining in the
alliance (based on Shapley value and the Growth).
Real data from the three largest strategic alliances (Star Alliance, Sky Team and
One World), was analyzed to assess the usefulness of the simulated data. However,
the actual results differ significantly from the simulated results (see [29]).
In conclusion, the proposed model can be seen as a first step toward under-
standing collective intelligence in humans by applying flocking behavior to the
context of strategic alliances. Inspired by three C-S algorithm concepts: position,
velocity and influence, we adapted the rationale of the same concepts to our
problem. In our context, position represents the selection of a potential partner
(choice), velocity reflects the organization’s performance (growth), and influence
is quantified using the Shapley Value. Regarding the position, we assume that the
organisations prefer collaborating with others that enable them to maximize the
gains of their strategy. Following this idea, we assume that the choice of which
organization to follow at the next moment depends on the alliance’s past growth,
decisions, and impact, aiming to maximize future outcomes. Our results showed
that when the balance between exploration and exploitation of knowledge is low,
and the influence of each share on the exploitation rate is high, organizations may
explore their environment but experience slow learning—an effect moderated by the
sigma and discount variables. The variable time gives importance to the most recent
choice made by the organization. If the organizations’ evaluation time is longer, the
relationship between exploration and knowledge is strong, and the discount value
is low, this benefits the most recent choice between organizations—unlike when the
evaluation time is short, where this advantage is diminished. Overall, our findings
suggest that organizational learning and strategic alliance choices are influenced
by the balance between exploration and exploitation, the timing of evaluations,
and discounting effects—with longer evaluation periods and stronger exploration-
knowledge relationships favoring recent, high-impact decisions.
References
1. J. Johanson, L.G. Mattsson, Internationalization in industrial systems-a network approach, in
Strategies in Global Competition, ed. by N. Hood, J. Vahlne (Croom Helm, New York, 1988)
2. D.A. Aaker, Strategic Market Management, 4th edn. (Wiley, New York, 1995)
3. V. Eiriz, Proposta de tipologia sobre alianças estratégicas. Rev. Admin. Contemp. 5(5), 65–90
(2001). https://doi.org/10.1590/S1415-65552001000200004
4. D. Angwin, J. Mavole, Scholes, R. Whittington, Exploring Strategy (Pearson, London, 2014)
5. M. Okura, Coopetitive strategies of Japanese insurance firms: a game-theory approach. Int.
Stud. Manag. Organ. 37(2), 53–69 (2007)
6. R. Rusko, Exploring the concept of coopetition: a typology for the strategic moves of the
finnish forest industry. Ind. Mark. Manag. 40(2), 311–320 (2011). Special issue on Service-
Dominant Logic in Business Markets
7. I. Tlemsani, R. Matthews, M.A. Mohamed Hashim, Strategic learning alliances and coopera-
tion:agametheoryperspectiveonorganizationalcollaboration.Economies 12(12),335(2024).
https://doi.org/10.3390/economies12120335

12 StrategicAlliancesinNetLogo:AFlockingAlgorithmwith... 305
8. T. Vicsek, A. Czirók, E. Ben-Jacob, I. Cohen, O. Shochet, Novel type of phase transition in a
system of self-driven particles. Phys. Rev. Lett. 75, 1226–1229 (1995)
9. R. Olfati-Saber, Flocking for multi-agent dynamic systems: algorithms and theory. IEEE Trans.
Automat. Control 51(3), 401–420 (2006)
10. J. Ferber, L. Gasser, Intelligence artificielle distribuée, in 11th Conference on Expert Systems
and their Applications, Avignon (1991)
11. N. Gilbert, Agent-based social simulation: dealing with complexity. The Complex Systems
Network of Excellence, 9 (01 2005)
12. R. Axtell, Effects of interaction topology and activation regime in several multi-agent systems,
in Multi-Agent-Based Simulation, ed. by S. Moss, P. Davidsson (Springer, Berlin, 2001), pp.
33–48
13. R. Axtell, The emergence of firms in a population of agents: local increasing returns, unstable
Nash equilibria, and power law size distributions. Santa Fe Institute Working Paper 99-03-019
(1999)
14. R.L. Axtell, Why agents? On the varied motivations for agent computing in the social sciences.
Agent Simulation: Applications, Models, and Tools, 1999 (2000)
15. J.M. Epstein, Generative Social Science: Studies in Agent-Based Computational Modeling.
Princeton Studies in Complexity (Princeton University Press, Princeton, 2006)
16. D. Jardim, L. Nunes, S. Oliveira, Hierarchical reinforcement learning: learning sub-goals and
state-abstraction, in 6th Iberian Conference on Information Systems and Technologies (CISTI
2011) (2011), pp. 1–4
17. J. Salminen, Collective intelligence in humans: a literature review (2012). ArXiv
abs/1204.3401
18. J. Wang, G. Beni, Cellular robotic system with stationary robots and its application to
manufacturing lattices, in Proceedings. IEEE International Symposium on Intelligent Control
1989 (1989), pp. 132–137
19. P. Levy, R. Bononno, Collective Intelligence: Mankind’s Emerging World in Cyberspace
(Perseus Books, New York, 1997)
20. C.W. Reynolds, Flocks, herds and schools: a distributed behavioral model. ACM SIGGRAPH
Comput. Graphics 21(4), 25–34 (1987)
21. S. Yelisetti, V.K. Saini, R. Kumar, R. Lamba, A. Saxena, Optimal energy management system
for residential buildings considering the time of use price with swarm intelligence algorithms.
J.Build.Eng.59,105062 (2022). ISSN2352-7102. https://doi.org/10.1016/j.jobe.2022.105062
22. L.E. Beaver, A.A. Malikopoulos, An overview on optimal flocking. Ann. Rev. Control 51,
88–99 (2021). ISSN 1367-5788
23. F. Cucker, S. Smale, On the mathematics of emergence. Jpn. J. Math. 2, 197–227 (2007)
24. F. Cucker, S. Smale, Emergent behavior in flocks. IEEE Trans. Automat. Control 52(5), 852–
862 (2007)
25. S.A.C. Teixeira, Flocking behaviour e alianças estratégicas. Master’s thesis, Faculty of
Economics of University of Porto, Porto (2015)
26. P. Papapetrou, A. Gionis, H. Mannila, A shapley value approach for influence attribution, in
Machine Learning and Knowledge Discovery in Databases, ed. by D. Gunopulos, T. Hofmann,
D. Malerba, M. Vazirgiannis (Springer, Berlin, 2011), pp. 549–564
27. L.S. Shapley, K.J. Arrow, E.W. Barankin, D. Blackwell, R. Bott, N. Dalkey, M. Dresher,
D. Gale, D.B. Gillies, I. Glicksberg, O. Gross, S. Karlin, H.W. Kuhn, J.P. Mayberry, J.W.
Milnor, T.S. Motzkin, J. Von Neumann, H. Raiffa, L.S. Shapley, M. Shiffman, F.M. Stewart,
G.L. Thompson, R.M. Thrall, A Value for n-Person Games (Princeton University Press,
Princeton, 1953), pp. 307–318
28. R.S. Sutton, A.G. Barto, Reinforcement learning: an introduction. Robotica 17(2), 229–235
(1999)
29. S.A.C. Teixeira, P. Campos, R. Fernandes, C. Roseira, Collective intelligence and collabo-
ration: a case study in airline industry, in Collaboration in a Hyperconnected World, ed. by
H. Afsarmanesh, L.M. Camarinha-Matos, A. Lucas Soares (Springer International Publishing,
Cham, 2016), pp. 148–155

306 S.TeixeiraandP.Campos
30. R.S. Sutton, A.G. Barto, Reinforcement Learning, 2nd edn. Adaptive Computation and
Machine Learning (MIT Press, Cambridge, 2018)
31. M. Tokic, Adaptive E.-greedy exploration in reinforcement learning based on value differences,
in KI 2010: Advances in Artificial Intelligence. KI 2010, ed. by R. Dillmann, J. Beyerer, U.D.
Hanebeck, T. Schultz. Lecture Notes in Computer Science, vol. 6359 (Springer, Berlin, 2010)
32. J. Pessoa, Análise funcional comparativa de algoritmos de aprendizagem por reforço. MSc
Thesis, Polythenic University of Lisbon (2011). https://repositorio.ipl.pt/entities/publication/
013b1b3f-bd87-477f-a85d-319ca67b616e
33. G.A. Rummery, M. Niranjan, On-line Q-learning using connectionist systems. Department of
Engineering, University of Cambridge, Cambridge (1994)
34. J.N. Tsitsiklis, Asynchronous stochastic approximation and Q-learning. Mach. Learn. 16, 185–
202 (1994)
35. R.A.C. Bianchi, C.H.C. Ribeiro, A.H.R. Costa, Heuristically accelerated Q-learning: a new
approach to speed up reinforcement learning, in Advances in Artificial Intelligence - SBIA
2004. SBIA 2004, ed. by A.L.C. Bazzan, S. Labidi. Lecture Notes in Computer Science, vol.
3171 (Springer, Berlin, 2004). https://doi.org/10.1007/978-3-540-28645-5_25
36. T.G. Dietterich, The MAXQ method for hierarchical reinforcement learning, in Proceedings of
the Fifteenth International Conference on Machine Learning (ICML ’98) (Morgan Kaufmann
Publishers Inc., San Francisco, 1998), pp. 118–126
37. T.G. Dietterich, An overview of MAXQ hierarchical reinforcement learning, in Abstraction,
Reformulation, and Approximation. SARA 2000, ed. by B.Y. Choueiry, T. Walsh. Lecture Notes
in Computer Science, vol. 1864 (Springer, Berlin, 2000)
38. U. Wilensky, Netlogo party model. Center for Connected Learning and Computer-Based
Modeling, Northwestern University, Evanston (1997)
39. U. Wilensky, NetLogo: Center for connected learning and computer-based modeling, North-
western University, Evanston (1999)

Chapter 13
Exploring the Efficiency vs. Fairness
Behavioural Spectrum in Multi-Agent
Deep Reinforcement Learning
Margarida Silva, Zafeiris Kokkinogenis, Jeremy Pitt,
and Rosaldo J. F. Rossetti
13.1 Introduction
Throughout history, RL techniques have aimed to optimise the expected sum of
rewards an agent gets for acting under its policy. More recently, fairness concerns
have been brought into the Machine Learning literature, and fairness-aware line of
algorithms have been emerging. In the multi-agent paradigm, some work attempts
to optimise the equality in the distribution of rewards of the agents in the most
efficient manner possible [35, 94]. This literature approaches fairness as a goal for
the individual agents’ policies to optimise. However, there seems to be a gap in work
considering fairness and efficiency holistically. Indeed, in a real-world scenario,
it may be that neither the efficient nor the equality extreme goals are ideal, so it
is important to study in-between solutions. The designer should be able to opt to
sacrifice one of them, to a certain extent, for the other, and there is lack of literature
to support such a decision. There is still no evidence of the outcome of mixing fair
and efficient behaviours or even training these together in a MADRL system. While
the relationship between fairness and efficiency is popularly seen as a trade-off [60],
there is still a lack in evidence that is really the case in MADRL.
M. Silva
University of Porto, FEUP-MIEIC, Porto, Portugal
Z. Kokkinogenis
University of Porto, LIACC, Porto, Portugal
J. Pitt
Imperial College London, London, UK
e-mail: j.pitt@imperial.ac.uk
R. J. F. Rossetti (@)
University of Porto, FEUP-DEI, Porto, Portugal
e-mail: rossetti@fe.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 307
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_13

308 M.Silvaetal.
The main goal of this chapter is to address the fair distribution of rewards in
MADRL in an exploratory manner. By relaxing the assumptions about the fairness
or efficiency goals the system wants to promote, we aim to observe what solutions
arise. We want to assess the impact of combining fairness and efficiency goals in the
testing and training phases.
We tackle this challenge by employing two main techniques. The first is hetero-
geneous testing, where the agents in the system act selfishly or fairly according to
a probability, without updating their policies weights. This enables a direct mix in
previously learned policies. The second is an extension to the SOTO model [94]
which enables a team-oriented policy to provide fair action insights to the self-
oriented one. Because each policy recommends the other intertwined in this setting,
we call this method Intertwined SOTO (I-SOTO). We also experiment with different
settings for the training strategy that controls how SOTO’s self-and team-oriented
policies are trained. Doing so, we believe different solutions will be found in both
extremes and heterogeneous intermediates from testing—specially in the I-SOTO
case, where both policies share action recommendations. We develop our work
under two main assumptions:
1. If selfish and fair policies are combined heterogeneously, a linear range of fair-
efficient behaviours is generated
2. If SOTO’s πIND also receives recommendations from πSWF—I-SOTO—it is
. .
possible to find solutions that are better in at least on of the goals (fairness or
efficiency) without compromising the other.
This chapter discusses the state of the art on equality fairness in MADRL in a
variety of manners. In a broad sense, our work mainly relies on presenting results for
the exploratory attempts made in combining fair and efficient policies and training
them jointly. These results are presented in environments in the equality fairness
literature for MADRL because they include dynamics that foster unequal access or
opportunities to obtain rewards, i.e., to be efficient. The the considerations we make
in exploring the behavioural spectra of fair and efficient policies is three-fold: (1) we
suggest an extension of the SOTO that intertwines recommendations from the self-
and team-oriented policies and assess it under different β(e ) training strategies;
r .
(2) we evaluate if with I-SOTO it is possible to find solutions more fair and efficient
than SOTO’s fair and efficient baseline; (3) we provide an experimental set of results
which may serve as support for a system’s designer to choose which policy setup is
most appropriate for their goals in terms of efficiency and fairness.
In the following sections we provide the necessary background to fully under-
stand the extent of our work together with related work. We start by providing
some background on Reinforcement Learning and its core concepts, then move to
methods that require function approximation and, finally, review existent literature
within the multi-agent domain, both in settings with and without fairness concerns.
We start with Reinforcement Learning, including Markov Decision Processes.

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 309
13.2 Reinforcement Learning
Reinforcement Learning (RL) is the Machine Learning paradigm of learning to
make good sequences of decisions. As its name suggests, RL agents learn by
reinforcement from the environment they are put under. Higher reinforcements
signal positive behaviours from the agent as opposed to lower reinforcement values,
almost as praise or punishment for actions. The aim of RL is then to make the most
out of this reward signal and behave in the way that optimises it—whatever it is.
13.2.1 Markov Decision Processes
Early forms of Reinforcement Learning were methods for solving the problem of a
Markov Decision Process [63] (MDP). An MDP is a stochastic control optimisation
problem [80] characterised by the 5-tuple ^T,S,A,p,r^ (See Table 13.1 for the
.
characterisation).
Illustrated by Fig.13.1, at each timestep t, an agent under state s consults
t.
its policy π to perform an action a ∼ π(s ). Then, the environment changes
. t t .
to state s t+1 ∼ p(s t+1 |s t ,a t ) . , and this agent receives the corresponding reward
r(s t ,a t ,s t+1 ) . .
The name of these processes is inherited from the assumption they rely on. The
Markov Assumption states that the next state is independent of past states, given the
Table 13.1 Characterization of the 5-tuple^T,S,A,p,r^ .
T . Is the set of decision epochs, i.e. opportunities in time for the agent
to make decisions. Can be finite/infinite, discrete/continuous.
S . Is the state space i.e. set of possible states.
A . Is the action space i.e. set of possible actions. A(s). is the set of
possible actions in state s.
r:S×A×S→R . Is the rewardr(st,at,st+1). for performing action at. under state st.
and moving to the next statest+1..
p:S×A×S→[0,1] . Is the transition probabilityp(st+1 |st,at). of moving to statest+1. as
after taking action at.under state st..
π :S×A→[0,1] . Is the policy or decision-making rule π(st). as the probability of
choosing action at.under state st.. Can be deterministic or stochastic.
Fig. 13.1
Agent-environment
interaction in a Markov
Decision Process [80]

310 M.Silvaetal.
Table 13.2 Popular options in the literature
st i =ht i . Using the complete history of observations and actions available
to the agent. This naturally leads to an explosion in the dimensions
necessary to represent the state.
st i ∼P[s,|ht i] . Building a belief of which is the current state, given the history,
as a probability distribution [57].
st i =σ(st−1 iWs +otWo). Encoding the state in a recursive manner by combining the previ-
ous state representationst−1. with the current observation ot. with
the weightsWs. andWo., respectively [28]. This encoding is com-
monly accomplished with the use of Artificial Neural Networks,
whose functioning is to be further described in Sect.13.3.1.
current state. Formally, this assumption is expressed in Eq.13.1.
. Pr{s t+1 ,r t+1 |s t ,a t ,s t−1 ,a t−1 ,...,s 0 ,a 0 }=Pr{s t+1 ,r t+1 |s t ,a t } (13.1)
As such, one can now clearly see why either of the functions that characterise an
MDP—r, s and π—provide insights on the dynamics of the environment provided
.
information on the present time step t, and only t.
To accommodate real-life challenges [21], the MDP definition has been extended
to contemplate a more general case of conditions. One of these is incomplete
or incorrect access to the world’s state. Lack of sensors, sensory inaccuracy and
environment limitations are some of many reasons that may impair the accessi-
bility of state information to the agent. A Partially Observable Markov Decision
Process [39, 77] (POMDP) is an extension the MDP fully observable model in
which agents only perceive observations o ∈ O, modelled by an observation
.
function ω : S × A × O, instead of accessing the state s ∈ S directly. Let
. .
h t i = o t ,a t−1 ,o t−1 ,...,a 1 ,o 1 ,a 0. be the history of observations and actions of
agent i since the start of the simulationUnder these circumstances, each agent i
should find alternative ways of enriching their perception of s i to overcome the
t .
lack of information in an observation. The popular options we find in the literature
are reported in Table 13.2
13.2.2 Prediction
In the RL domain, prediction refers to the task of estimating the consequences of
actions performed by agents. Oftentimes, the object of prediction in RL methods is
associated with a nomenclature. In particular, methods that make estimations of
the policy π, the transition function p and the reward function r or derivatives
.
are named policy-, model- and value-based respectively. Due to the importance
of value-based methods in the RL literature, we dedicate Sect.13.2.2.1 to it.
Section 13.2.2.2 refers to how these estimations are made throughout time steps.
Lastly, the commitment of making predictions with regards to the action provided

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 311
by the policy, or lack thereof, is also a way of naming methods as on-or off-policy,
respectively, as presented in Sect.13.2.2.3.
13.2.2.1 Value Estimation
One of the most important outcomes to employ estimations on is, naturally, the
reward value expected to arise from performing some action. The agent is then able
to control which action to take by choosing the one that seems most promising.
This potential reward outcome is commonly known as return g
t.
. AEn intuitive but
naive way of defining this return is as the sum of rewards received T r , where
k=1 k.
T is the last time step. However, many real applications are made of continuous
agent-environment interactions, making Tinfinite. In order to provide convergence
.
properties to g [80], a discounting factor0≤γ ≤1is added and g is defined as the
t. . t.
discounted sum of rewards—also referred to as the discounted return—as defined in
Eq.13.2.
ET
.
g t =r t+1 +γr t+2 +γ2r t+3 +...= γkr t+1+k
(13.2)
. k=0
=r
t+1
+γg
t+1
Because the ultimate goal of RL is to maximise this return, it is oftentimes
referred to as value. If this value is estimated only with respect to the state
the agent is under, the State-value function Vπ of some policy π is given by
. .
Eq.13.3. Notice that, contrary to the aforementioned definition of return in Eq.13.2,
because in this case, we are defining estimations of values that may depend on
stochastic processes—as seen in the MDP section—return and reward are now
random variables and, by extension, any estimations based on them.
⎡ ⎤
ET
. Vπ(s)=Eπ[G t |S t =s]=Eπ⎣ γjR t+j+1 |S t =s ⎦ (13.3)
j=0
If we extend V by also considering particular actions, we are now referring to the
Quality-value, or Q-value in short. Such function provides the estimated return for
performing a particular action a, given the agent’s policy π,asshowninEq.13.4.
.
⎤ ⎤
ET
. Q π(s,a)=Eπ[R t |S t =s,A t =a]=Eπ γkR t+k+1 |S t =s,A t =a
k=0
(13.4)
In deterministic policies, V has the same value of Q given the policy’s action—
unique in this case. However, in stochastic ones, the q-value is equal to the

| 312 |     |     | M.Silvaetal. |     |
| --- | --- | --- | ------------ | --- |
state-value distributed over the action distribution of the policy. This relationship
is formally portrayed in Eqs.13.5 and 13.6, respectively.
.
|     | Vπ(s)=Qπ(s,π(s)) |     |     | (13.5)  |
| --- | ---------------- | --- | --- | ------- |
.
E
.
|     | Vπ(s)= | |S =s)Qπ(s,a) |     |         |
| --- | ------ | ------------- | --- | ------- |
|     | .      | p(a t         |     | (13.6)  |
a∈A
The availability of a reward function—or at least an accurate one—is not trivial
in all applications. Indeed, designing a good reward function is a challenge per se in
complex environments such as driving a vehicle. Potential approaches to solve this
problem include inferring the reward function from already existing policies known
to behave well, with Inverse Reinforcement Learning [46, 54], or even learning
directly an approach from such examples, with Imitation Learning [31]. We could
also tweak the existent reward function into a more reliable one with the use of
Reward Shaping [7, 96]. While we will not be directly approaching this problem,
we acknowledge the importance of having a good reward function to rely on while
value predictions, independently of the estimation utilised.
13.2.2.2  Update Strategy
A crucial part of making estimations is how they are successively updated. There
are three essential update paradigms in RL: Dynamic Programming (DP), Monte-
Carlo methods (MC) and Temporal Difference (TD). While each of these has its own
intricacies, we compare them in a high-level manner and direct the interested reader
to [80]. We consider in this section the state-value for simplicity in understanding.
Dynamic Programming [19] was one of the first update methods that appeared
in RL. In this method, the estimation is updated at each time step t using Eq.13.7,
also known as the Bellman Equation [4, 20]. As can be seen, this method relies on
the transition function, being inapt for model-free domains. Notice that this model
requires the transition function p to function, being inapt for model-free  domains.
It is also important to note that( it b)ootstraps the return value if the estimation of the
value of the followingstateV s ' , which is naturally a source of bias.
|            | t       | .                |       |         |
| ---------- | ------- | ---------------- | ----- | ------- |
|            | ⎤       |                  | ⎤     |         |
|            | E       | E                | ( )   |         |
| ˆ          |         |                  | ' ˆ ' |         |
| V t+1 (s)= | π(a |s) | r(s,a)+γ p(s,a,s | )V s  | (13.7)  |
| .          |         |                  | t     |         |
s'∈S
a∈A
Monte Carlo methods, on another note, function quite differently. Under this
update paradigm, the agent waits for the end of the episode to update its estimation,
making this method not suitable for continuing tasks as they may never come a time
for the agent to learn. There are many variants to this method, but the general idea is
that the value of each state is a function of the summation of returns generated after
such state,G(s)over the number of times such state appeared throughout episodes .

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 313
Table 13.3 Comparison of prediction update strategies
Control Model-free domains Continuing domains Non-Markov domains Unbiased
DP X
MC X X X
TD X X
N(s)—popularly, the average, as shown in Eq.13.8. In the First-Visit variant, each
.
state is only considered once per episode, so the summation of returns is averaged
over the number of episodes.
.V ˆ (s)=G ˆ (s)/N ˆ (s) (13.8)
Temporal difference is the most recent of all methods and the most popular in
recent RL literature. Combining principles from DP and MC, TD not only supports
continuing domains but also handles Model-free domains, i.e., problems in which
the world model—transition and reward functions—are unknown. A example of a
TD variant, TD(0), is illustrated in Eq.13.9. Given the transition (s t ,a t ,r t ,s t+1 ) .
from time step t to t + 1, TD updates the estimation of the value of being in
.
state s taking into account the reward received r and the value of the next state
t.
V t+1 (s) . after performing the action a determined with the policy. The TD-error δ t.
is then defined by Eq.13.10 as the difference between the current reward plus value
estimation fort+1and the value estimation for t. Although this difference does not
.
include the true value of return g , it is the approximation possible at time step t.
t.
. V ˆ t+1 (s t )=V ˆ t (s t )+α[r t +γV ˆ t (s t )−V ˆ t (s t+1 )] (13.9)
. δ ˆ t =r t+1 +γV ˆ (S t+1 ,w t )−V ˆ (S t ,w t ),r t+1 ∼R t+1 (13.10)
A comparative summary of these three methods follows in presented Table 13.3.
13.2.2.3 On-Policy and Off-Policy
The terms on-policy and off-policy refer to value estimation methods that make
estimations limited on the policy π decision-making rules or that go beyond such
.
rules, respectively. Q-Learning [84, 85] is an example of an off-policy method,
depicted in Eq.13.11. While making q-value updates quite similar to those of
SARSA. However, after an agent performs action a under state s and state is
t. t.
updated to s t+1. , the q-value update is made considering the next best action that
can be taken under state s t+1. , which may not be necessarily equal to what the
ˆ
policyπ would dictate, since the update ofQ(s ,a )has not been completed yet.
st+1. t t .
While having a very similar update equation, SARSA is an on-policy alternative to
Q-Learning. As depicted in Eq.13.12, the main difference is on the γ parcel that
.

314 M.Silvaetal.
considers the actiona t+1 ∼π st+1 , . i.e. the action pointed by the policy with regards
to the next state, and naturally never in its updates considers other actions from such.
. Q ˆ t+1 (s t ,a t )←Q ˆ t (s t ,a t )+α[r t+1 +γ maxQ ˆ t (s t+1 ,a)−Q ˆ t (s t ,a t )] (13.11)
a
. Q ˆ t+1 (s t ,a t )←Q ˆ t (s t ,a t )+α[r t+1 +γQ ˆ t (s t+1 ,a t+1 )−Q ˆ t (s t ,a t )] (13.12)
13.3 Approximate Solution Methods
When A and S are finite sets, it is possible to make predictions using tables with
. .
entries for different states or state-action pairs, i.e. with tabular methods [9, 89].
However, when either |A| or |S| are very large—maybe even infinite—these lack
. .
in generalisation and efficiency. Not only would it be costly to store tables with a
tremendous amount of entries, but it would also take much time to be able to produce
reasonable approximations for all entries, and they are built from a sequence of
several updates. Additionally, since each action/state is treated as an independent
entity, tabular methods lack in generalisation. Given two very similar in meaning
states s and s , if s is close to convergence and s is not, when the agent lands
i. j. i. j.
s it will still perform poorly, in theory, as it has not lived that exact state several
j.
times and there is no way of inferringv(s )fromv(s . An evident case where this
j . i.
becomes problematic is when either Aor Sare continuous sets, i.e.A∈Rn,n∈N,
. . .
S∈Rn,n∈N, and thus it would be intractable to have a table with infinite entries.
.
In these cases, a parameterised function representation is used to approximate the
estimations of policies, values or models. In the Machine Learning (ML) literature,
linear models have been widely used to make these approximations. These models
frame the approximation problem as finding the best set of weights w and bias
.
b enable f(x)—as in Eq.13.13—that better represents the real values of some
.
distribution y. In order words, to minimise the differencef(x)−y.
. .
f(x)=w T x+b (13.13)
.
13.3.1 Neural Networks
While linear models can be adapted to also approximate non-linear functions—
with the use of polynomials, Fourier series or Radial Basis Functions—this process
requires manual transformation inputs and outputs (“feature engineering”) and
requires some insight to be successful. Artificial Neural Networks (ANNs), also
known as Neural Networks (NNs), are more flexible models that are able to learn at
least some of these non-linear transformations.

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 315
A Neural Network, in its simplest form, can be viewed as a set of linear layers
where each layer l is placed after theotherl −1. The values of the first layer also
.
referred to as the input layer, are the inputs given to the function h(0) = x. The
.
subsequent layers are the result of applying an activation functiong(l)to the outputs
.
of the previoush(l−1)layer multiplied by a set of weightsW(l)plus the layer biases
. .
b, as in Eq.13.14. Neural Network architectures with a large number of layers—
.
“deeply layered”—give the name to a sub-field of Machine Learning called Deep
Learning.
/ /
h(l) =g(l) W(l)h(l−1)+b(l) (13.14)
.
While NNs enable the learning of more complex functions, its fitting process is
much more challenging, requiring more data and time to converge successfully. Not
only the parameter number is much larger, but the optimisation process is rather
iterative through successive updates of the weights applying the chain rule for each
neuron u , given that the previous layer in which u is located has D dimensionality.
i. i.
ED
∂f ∂f ∂x
= d (13.15)
.
∂u ∂x ∂u
i d=1 d i
Neural Networks use Gradient-based optimisation to fit their parameters. The
most naive optimisation process is the Steepest Gradient Descent 13.16 where the
weights are updated by being subtracted with the cost function multiplied by a
learning rate η. The cost function used as an example in Eq.13.16 is the squared
.
error, having r be the vector of errors or differences between the predictions and
.
targets. However, a common loss function could be the root mean squared error,
averaging this error over the number of samples considered and then calculating the
square of such value. The important thing is that this cost function represents how
much the algorithm needs to “pay” for wrong predictions, such that its gradient
on the weights of the network ∇ [r T r] directs it to a good direction towards
w .
minimising it.
⎤ ⎤
w←w−η∇ r T r (13.16)
. w
An alternative is to use Gradient Ascent, which, as the name indicates, aims to
maximise an objective function instead of minimising a cost function. The key idea
is identical to gradient, but instead, the product between the learning rate and the
cost function is summed to the weights instead of subtracted.
However, this process demands great computational power as either the cost or
objective function needs to be evaluated for each sample of a dataset—which may
have thousands of thousands of entries in extreme cases—and for each step of the
optimisation—which may also require a great number of steps. In order to solve this,
Stochastic Gradient Descent selects on a random sample of the dataset to calculate

316 M.Silvaetal.
the value of the cost function and multiplies it by the number of samples in order
to estimate the actual dataset value. ADAM optimiser [40] is an instance of such a
method that has become widely popular, especially for Deep Learning applications.
13.3.2 Eligibility Traces
An important concept to consider in Function Approximation updates is Eligibility
Traces. Under this paradigm, a parameter λcontrols the eligibility of each dimension
.
of the weight vector of a function-approximated approximation to be updated. As
such, it offers an in-between solution for DP and MC updates with regards to how
many time steps in advance are considered. Whenλ=0—TD(0)—it only considers
.
the immediately following state as DP does. On the other hand, when λ = 1—
.
TD(1)—it gets more similar to MC by considering all the following time steps until
the end of the episode, being identical whenγ =1. The eligibility trace is a vector
.
Z ∈Rd, as defined in Eq.13.17, and the TD( λ) update is now defined as presented
t . .
in Eq.13.18.
.
. z z − t 1 = . = γλ 0 z t−1 +∇V ˆ (s t ,w t ), 0≤t ≤T (13.17)
.
. w t+1 =w t +αδ t z t (13.18)
13.3.3 Advantage
A recent approach to estimating value is the concept of advantage. As shown in
Eq.13.19, the advantageA(s,a)
.
is by definition the difference between V a(nd) Q for
a given state-action pair. If we make a TD estimate forQ ˆ (s,a)asr+γ·V ˆ s ' , then
. .
ˆ
the advantage can also be seen as the TD error δ , as previously seen. The intuition
t.
behind this idea is that if we remove to the Q-value the value of the state itself,
we are left with the value of the action itself under such a state. Naturally, in cases
where the state is very promising, all actions will have very high Q-values, so the
decision-making process may be misled and compromised. As such, the advantage
function is used to eliminate the bias for estimation of the value of an action that
comes from the value of the state itself.
.
A(s,a)=Q(s,a)−V(s)
( )
A ˆ (s,a)=r +γ ·V ˆ s ' −V ˆ (s) (13.19)
.
=δ ˆ
t

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 317
However, this advantage definition is highly dependent on the value estimation.
Should this estimation be biased, this will also be imprinted in the advantage
estimation. In order to approach this issue, the Generalised Advantage Function
[69] (GAE) brings the eligibility Traces concept to the definition of advantage. As
ˆGAE
shown in Eq.13.20, the GAE advantageA for a given transition time step is an
|     |     |     |     | t .  |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
exponential average of the advantage estimations for such transition but throughout
the following n steps. This concept, of course, implies that the update on the value
estimation is only done after a collection of n time steps.
|     |     | /   |     |     | /   | En  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
.
| ˆGAE(γ,λ) | = (1−λ) | ˆ(1)+λA | ˆ(2)+λ2A | ˆ(3)+...A | ˆ(n) | = (γλ)lδV |     |
| --------- | ------- | ------- | -------- | --------- | ---- | --------- | --- |
| .  A t    |         | A t     | t        | t         | t    |           | t+l |
l=0
(13.20)
| 13.3.4  Policy Gradients  |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- |
Policy Gradient methods are gradient-based optimisations used for policy approx-
imation. The general idea behind these algorithms is that at each timestep t, the
policy is updated—originally, through gradient ascent—towards the direction that
leads to the policy choosing the best action possible a ∗ ,asshowninEq.13.21.
.
∗
|     |     | θ t+1 | =θ +α∇π | (a  | |s) |     | (13.21)  |
| --- | --- | ----- | ------- | --- | --- | --- | -------- |
|     |     | .     | t       | θt  |     |     |          |
REINFORCE [88] is one of the earliest and simplest Policy Gradients algorithms.
Naturally, one challenge of Policy Gradient methods is finding the direction where
∗|s)
π θt (a .  gets closer to one. In order to address this, REINFORCE uses an
estimation of the expected return gˆ . This may be in the form of a q-value or even
t.
an advantage value, as in Eq.13.22. However, because this estimation may provide
very high values in earlier stages due to the initialisation utilised, the gradient is then
divided by the current probability of the action in questionπ(a |s ,θ ).
|     |     |     |     |     |     | t t t | .   |
| --- | --- | --- | --- | --- | --- | ----- | --- |
ˆ
|     |     |         | Q (s,a)∇π |        | (a |s) |     |          |
| --- | --- | ------- | --------- | ------ | ------ | --- | -------- |
|     |     | =θ      | +α        | θt     |        |     |          |
|     |     | . θ t+1 | t         |        |        |     | (13.22)  |
|     |     |         |           | π (a | | s)     |     |          |
θ
Another very common way to present the REINFORCE equation is in the
|                                       |     |     | ∇πθ(a|s) | =∇  |             | |a).  |     |
| ------------------------------------- | --- | --- | -------- | --- | ----------- | ----- | --- |
| logarithm form, as in Eq.13.23, since |     |     |          |     | θ logπ θ (s | .     |     |
πθ(a|s)
ˆ
|     |     | θ =θ  | +αA (s,a)∇ | logπ | (s |a) |     | (13.23)  |
| --- | --- | ----- | ---------- | ---- | ------ | --- | -------- |
|     |     | . t+1 | t          | θ    | θ      |     |          |
Since the appearance of REINFORCE, many alternative policy optimisation
algorithms have appeared [45, 68, 70]. Trust Policy Region Optimisation [68]
(TRPO) adds KL divergence constraints to ensure that new updated policies are
not largely deviating. In other words, the new policy is not far away from the old

318 M.Silvaetal.
policy, or we can say that the new policy is within the trust region of the old policy.
Proximal Policy Optimisation [70] (PPO) that simplifies the implementation of this
diversion implementation by imposing the policy ratio, r(θ) = πθ(a|s) to stay
πθold(a|s).
within a small interval around 1, as shown in Eq.13.24 of PPO objective function.
The clip operator is what makes sure it won’t deviate largely by clipping the update
in the range.
⎤ / /⎤
JCLIP(θ)=E min r(θ)A ˆ (s,a),clip(r(θ),1−E,1+E)A ˆ (s,a)
. θold θold
(13.24)
13.3.5 Actor-Critic
As the name implies, Actor-Critic [41] approaches involve a dynamic between
two elements: an actor—the policy—and a critic—some value estimation. The
actor performs an action, and the critic is used to access—“criticise”—the policy’s
choice in behaviour [80]. However, as previously seen, policy gradients also involve
the use of both a policy and value estimation, where the latter impacts the next
policy weights θ t+1. . From a technical point of view, the main difference between
Actor-Critic methods and Policy Gradients is that, whichever method is used, Actor-
Critic value estimations contemplate the prediction of the value of the state after
performing an action while pure policy gradients do not. From an intuitive point
of view, when I am going beyond estimating the value of the current state but also
including a prediction of value for the next, the model is no longer only named
a Policy Gradients approach but also an Actor-Critic one. An example of value
estimation associated with Actor-Critic approaches is the definition of advantage,
as previously seen in Sect.13.3.3.
In function approximation approaches, the state-value or action-value yielded by
the critic is typically part of the expression of the gradient used by the actor to
estimate the policy [24, 25, 32, 47, 50, 66, 71], linking the q-value approximation
goal with the policy.
13.4 Multi-Agent RL
When multiple RL agents are placed within a shared environment, we are now
under a Multi-agent Reinforcement Learning (MARL) problem [9, 10, 59]. Multi-
agent systems [73] bring complexity to the optimisation process when compared to
the single-agent case. In this case, the system can no longer be considered stationary.
Because the states of other agents’ are unknown to each agent within the system,
the Markov Property no longer holds. In other words, the future state depends on
more variables than the present state and action. This breach of this property is

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 319
problematic as some control methods—and especially TD—are built under this
assumption, as seen before, and bootstrap estimations accordingly. The following
sections outline a few approaches and respective concerns to take into consideration
in this setting.
13.4.1 Independence
A natural approach to extending the well-known single-agent algorithms to the
multi-agent setting is to provide each agent with an independent single-agent
model [1, 81]. This method is naturally advantageous in the sense that any model
could be very easily applied to the MARL setting. However, it also brings additional
challenges. Because every agent is acting on its own, the emergence of coordinate
behaviours is more challenging. Moreover, the computational complexity of the
model is higher,|D|times more demanding.
.
13.4.2 Joint Action
Another thread of RL models frames the action aas the vector of the actions chosen
.
by each agent—a joint action. If a model is set to optimise a joint action, perhaps the
non-stationarity problem is solved since—in centralised approaches—the actions of
all agents can be seen before making the final joint action decision. However, under
this framing, the state and action spaces exponentially grow with the number of
agents within the system. Each state can now contemplate the states of n-1 other
agents, and each action is now |A| · |D|. This dimensionality explosion—often
.
referred to as a curse—presents a serial problem and affects the RL algorithms’
ability to converge. It affects the exploration-exploitation trade-off agents need to
make since it is tough to explore the behaviour of all agents within the system.
On the other hand, should agents perform a joint action, it is only natural that
the environment should return a joint reward for such action—typically, the sum of
the individual is potentially different. Consequently, it may be difficult for agents
to infer how much they are responsible for such a reward and even ‘learn to
rest’ if other agents are already contributing very intensely to the global systems’
reward. This challenge is popularly known as the multi-agent credit assignment [12]
problem. In the literature, many approaches aim to solve this problem and transform
this joint reward into a set of individual rewards. The most relevant techniques
include neural network architectures for reward distribution [64, 76, 79] and the
usage of estimation concepts such as Difference Rewards [11, 24] and Shapley
Value [83]. In domains where the optimisation is multi-objective, this poses an even
more complicated challenge since the reward is now a multi-dimensional vector:
there is a credit to attribute for each of these dimensions [90].

320 M.Silvaetal.
13.4.3 Decentralisation and Dec-POMDPs
As seen before, when the agents only have access to a part of the environment
state, they are called partially observable MDPs (POMDPs). Oliehoek et al. [57]
introduces the concept of decentralised POMDPs (Dec-POMDPs) as a generalisa-
tion term for a system with multiple agents of a POMDP used to model a team of
cooperative agents under a stochastic, partially-observable environment [42, 58]].
Decentralisation implies there is a concern to some extent to the amount of
information the agents may share between each other and that methodologies that
require complete centralisation are to be avoided if possible. A typical approach to
this scenario is either a centralised learning and decentralised execution approach—
where the centralised learning components should be detachable for a posterior
decentralised execution—or a fully decentralised [93] approach, where communi-
cation between neighbours of state information is typically used to overcome this
problem [27, 35, 36, 49, 94]. These communication mechanisms may contemplate
weights of the functions being approximated towards building more complete
estimations [36], or even important state information that may help other agents
make decision [94].
13.5 Fairness
As with any social construct, fairness is inherently subjective [44]. As a result,
its notion has been extensively studied within various social science fields such as
political philosophy [65], political science [6] and in economics [52]. Most concepts
that emerge from the literature can be seen as particular instances of the concept of
equal treatment of equals, including:
• Impartiality, as the lack of prejudice in making decisions towards specific
individuals or groups [67].
• Equality and Equity, as a special case when the population is a set of
equals. Under such a case, what is left is promoting an equal distribution of
some resource—Equality—or equal opportunity in obtaining it—Equity. Such
a distribution is oftentimes evaluated with the use of Social Welfare Functions
(SWF) [52], which measure the welfare of the population as a function of the
individuals’ utilities.
• Paretoefficiency, as the state where no individual can improve their performance
without declining the performance of others.
• Envy-Freeness, as the perception of an individual, is that the share of resource
it has been allocated is, at least, as good as the share received by any other
agent [14].
These notions of fairness have been brought to applied mathematics fields. In
Operations Research, fair optimisation deals with promoting equitable allocation of

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 321
resources [56] in the problems of sensor placement [53], resource allocation [5],
MDPs [55] and, notably, in network routing [2, 29, 56]. Regarding Artificial Intel-
ligence, most multi-agent systems [73] work focus on resource allocation. While
some work uses pre-established fairness definitions, such as envy-freeness [14],
others attempt to provide the agents with some self-organisation power towards
achieving such a definition [61,62]. Instead, the latter develop either centralised [62]
or interaction-based [61] mechanisms for the agents to achieving rules that establish
which concept of justice, and consequently fairness. Enabling a definition of fairness
to emerge from agents also requires formal models of the world and rule generation.
A popular use of the notions of fairness in multi-agent systems is towards achieving
increased cooperative behaviour, or at least coordinate in competitive domains when
believed to be beneficial [18, 26]. Finally, there have also been considerations on
the importance of a priority-awareness model regarding fairness [37], in order to
entangle a priority relationship between fairness and efficiency as the goal of the
system. However, there seem not to be any empirical results testing this approach.
With the increased presence of Machine Learning models in real-life decision-
making situations, the notion of fairness has gained important attention in such a
field. Motivated by the impact of discriminatory harms from algorithmic bias [95],
the most dominant notion of fairness to be incorporated in Machine Learning is of
Impartiality, under many forms [67,82], either in Classification [22,43], Regression,
Decision-Making [33] or Clustering [15] tasks. A more recent approach uses a
Social Welfare Function (SWF) to measure the impact of using models that optimise
group impartiality on within-group inequality [78]. In Reinforcement Learning, this
notion of fairness has been brought to the classification task on the decision-making
task of choosing which action to take, both in the multi-armed bandit context [38]
and the more general single-agent case [33]. This idea has been extended to the
general single-agent case by imposing the constraint of never choosing one action
over another unless its long-term return of choosing the first is higher or equal to
the latter. In other words, making sure that the action is chosen actually has an
estimation of better value—otherwise, it is a biased decision to act on it. A worse
option is never favoured over a, apparently, better one.
13.5.1 Equal Distribution
More recently, the equality notion of fairness has been brought to MARL systems
with regards to distributions of quantities—resources, opportunities, rewards, etc.
A line of work focuses on equitable resource allocation [48]. Some approaches
solve the problem with domain-specific knowledge towards solving a known issue
in it. Applications include scheduling [91] in order to minimise traffic, IoT devices
[23] in order to take into account the preferences of various users in a shared
system, networks, with regards to both connectivity [13] and routing [2, 72], and
even stock trading strategies for a portfolio of clients with different goals [3]. There
are also approaches that consider resource allocation in a more abstract manner.

322 M.Silvaetal.
[92] use the max-min egalitarian notion of social welfare, in which it is defined
as the lowest utility within the system. However, it does not consider learning.
On another note [16, 17], tackle the multi-armed bandit domain by introducing
constraints relative to the allocation process.
A different line of work focuses on including the equality concept in the model
method itself. Siddique et al. [75] work on the multi-objective MDP problem, where
the reward is a multi-dimensional vector to be optimised. The approach taken was to
make use of a social welfare function [8] as a way of ensuring each of these goals is
being learned in a fair way, i.e., being given approximately equal opportunities to be
learned. On another note, [83] approach the multi-agent credit assignment problem
using the notion of Shapley value, which approximates the impact of a single agent
in a coalition of agents. Each agent then is provided with this approximation of
reward and is able to estimate the return for its action—a Shapley Q-value.
Finally, there is a line of reward which focuses on equality of the rewards between
the set of agents within the MARL system. Because this is the fairness problem this
work focuses on, we will be dedicating the next section to it.
13.5.2 Reward Equality
In this section, we address the problem of making agents of a MA system receive an
approximately equal reward. Naturally, this cannot be forced, i.e. actually providing
each agent with the same reward value. Under such a setting, we would find
ourselves with a credit assignment problem, which damages the capacity of each
agent being able to learn to perform well, as already seen in Sect..
Under competitive domains, [30] tackle this by adding to the agents’ reward
value parcels that encode aversion for inequality in two forms: advantageous and
disadvantageous, controlled by parameters α and β, as shown in Eq.13.25. While
. .
this work is successful in promoting cooperation in competitive environments such
as social dilemmas, they do not make any considerations fairness-wise.
E E
α β
U (r ,...r )=r − i max(r −r ,0)− i max(r −r ,0)
. i i N i N −1 j i N −1 i j
j/=i j/=i
(13.25)
Regarding cooperative domains, the agents are training towards a common
fairness goal—equality, in this case. However, the task of learning fair policies does
not get easier. Indeed, if an agent is trying to optimise a global characteristic of the
system, it may be the case that what they learn does not stimulate their individual
performance as the fairness goal also depends on the actions of other agents. This
issue shares many similarities with the credit assignment problem. The little existent
literature in this set focuses on the architectural side of the models to mitigate this
issue. To the best of our knowledge, there are only two approaches that attempt

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 323
to work on this problem. Both of these measure fairness according to CV, the
Coefficient of Variation [34]. As shown in Eq.13.26, CV is the standard deviation
between thEe utilities of all n agents—typically, their accumulated reward throughout
timeu = T r for each agent i—divided by the mean utility.
i t=1 i,t.
/
E E
s n u n (u −u¯)2
CV= , whereu¯ = i=1 i , s = i=1 i (13.26)
. u¯ n n−1
One of them, FEN [35] is a hierarchical policy approach consisting of a controller
that ensembles several sub-policies. A key aspect of this architecture is that only one
of the sub-policies is trained with the typical reward signal r and the remaining
t.
ones exploit an information-theoretic objective to explore alternative behaviours
that may be further beneficial to achieve fairness. Giving name to the model, the
controller is then optimised according to a fair-efficient reward, given by Eq.13.27
for each agent i. The results showed this model achieved better CV in a variety of
domains. An ablation study also showed the importance of FEN’s architecture as it
significantly improves efficiency compared to a single policy optimised with a fair-
efficient reward. The average agent utility u¯ is estimated using a gossip algorithm
.
between neighbours.
u¯ /c
rˆi = | t | (13.27)
. t E+| ui/u¯ −1 |
t t
The second one, SOTO [94], is, to the best of our knowledge, state of the art in
this problem. For this reason and because our work extends from it, we dedicate the
next section to a more in-depth description of it.
13.6 Methodological Approach
Notation We use calligraphic letters—X —to denote alphabet sets, upper-
.
case letters—X—to denote random variables and constants, hats to denote
ˆ
approximations— X—and lower-case letters—x—to denote realizations. The
.
methodology employed is an extension to SOTO [94], so we dedicate Sect.13.6.1
to describing its intricacies.
13.6.1 SOTO
The SOTO architecture [94], is, to the best of our knowledge, state of the art
in the reward equality problem. It comprises a Self-Oriented Policy πIND and
.
Team-Oriented one πSWF, trained for the selfish and the fair goals respectively.
.

| 324 |     |     |     | M.Silvaetal. |
| --- | --- | --- | --- | ------------ |
It is designed for the Dec-POMDP framework [57], such that each of these
policies is independently trained for each agent and receives the observations of
the world as ⎤iEnput. Mo⎤reover, the team-oriented policy additionally receives J =
{J (θ) =E γtr }providing thus information on the wealth of other agents,
| i θ t i,t | .   |     |     |     |
| --------- | --- | --- | --- | --- |
and πIND(a|o), that is the forwarded output self-oriented policy as an efficient
.
recommendation. While the first inform the wealth state of other agents, the latter
provides a self-oriented recommendation for efficiency to the team-oriented policy.
In the SOTO training procedure,1 at each batch of steps, throughout episodes, a
policy is chosen, either self or team-oriented, according to the value of a β . variable.
The agents act according to such policy for the length of the batch in time steps and,
by the end of it, updates the corresponding policy’s weights. As such, the training of
= e
each policy depends on the evolution of βthroughout episodesβ(e ), wheree
|     |     | .   | r . | r E.  |
| --- | --- | --- | --- | ----- |
is the episode ratio. The function chosen by the authors isβ(e )=max(1−2e ,0),
|     |     |     | r   | r . |
| --- | --- | --- | --- | --- |
where e is the episode number and E is the number of the l astepisode.
Both policies are trained with Policy Gradients algorithms. However, the team-
oriented policy is trained with a different advantage value than the self-oriented
one, it is based on a social welfare function (SWF) with regards to the distribution
of cumulative rewards J. To choose which SWF to utilise, the authors respect three
.
principles: Impartiality, Equity and Pareto-efficiency [86]. Respecting these criteria,
two families of Social Welfare Functions are considered for the set Dof agents. The
.
first family is the Generalised Gini Function [87] (GGF), depicted in Eq.13.28,
∈
which is a linear combination of the agents utilities. Under this definition w
[0,1]D is a fixed strictly decreasing weight vector (i.e., w >w >...>wD) and
| .   |     |     | 1 2 | .   |
| --- | --- | --- | --- | --- |
↑
| u . is the vector agents utilities usorted in decreasing order. Instances of this family  | .   |     |     |     |
| ----------------------------------------------------------------------------------------- | --- | --- | --- | --- |
include the utilitarian notion—∀i,w =1—and the maxmin egalitarian approach—
|       | i   | .   |     |     |
| ----- | --- | --- | --- | --- |
| = = = | =   |     |     |     |
w 1 1,w 2 ... wD 0 . . The second family is depicted in Eq.13.29. It is
the summation of the transformation of the agents utilities by a strictly decreasing
concave function U : R → R. Instances of this function include proportional
.
fairness [60], the generalised entropy index [74], and, the one utilised by the authors,
|     | = x1−α | /=  | =   |     |
| --- | ------ | --- | --- | --- |
α-fairness [51] whereU . α (x) 1−α.  ifα 1andU α (x) log(x)otherwise. The  .
∈R+
α parameter controls the aversion to inequality.
.
E
↑
|     | G (u)= | w u |     | (13.28)  |
| --- | ------ | --- | --- | -------- |
|     | . w    | k k |     |          |
k∈[D]
E
(u)=
|     | S   | U(u ) |     | (13.29)  |
| --- | --- | ----- | --- | -------- |
|     | . U | k     |     |          |
k∈[D]
Independently of the social welfare function utilised, whileA ˆIND is identical to
.
ˆSWF
the typical advantage definition, the definition of the advantageA .  is a function
1 For an in-depth explanation with pseudo-code we defer the reader to the original paper [94].

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 325
of the social welfare function φ(u) utilised as portrayed in Eqs.13.30 and 13.31
.
respectively.
A ˆIND =A ˆ (o ,a ) (13.30)
. i Ii i i
A ˆSWF =∇ φ(J ˆ (θ)) T·A ˆ (o,a) (13.31)
. u
The team-oriented advantage is the dot product between the gradient of the SWF
with regards to the agents utilities and the global advantage of the system. The
gradient term, after derivation, is then equal to:
• ∇ G (J(θ)) =w , where σ is a permutation that sorts Jin an increasing order,
u w σ. . .
as the definition of this SWF family requires.
• ∇ S (J(θ)) =J(θ) − α,forα ∈[0,1[, which is the setting in consideration.
u Uα . .
Since this method is fully decentralised, the agents resort to communication between
neighbours in order to estimate J. As a consequence, an agent i may receive
conflicting information about the quality ofπSWF, making the learning of a policy
.
under the advantageA
ˆSWF
potentially unstable. Furthermore, the value of a Social
.
Welfare function is by definition the same for all the agents within the system—
or, in this case, tends to be the same as the number of neighbours increases. These
challenges motivated the authors to include a self-oriented policy in the architecture,
providing an insight to the team-oriented policy on whether its successes/failures
are due to the individual behaviour of the agent or to behaviours of neighbours.
The distribution of probabilities estimated by such policy is provided as input to the
team-oriented policy, serving as an individualistic recommendation of how to act.
13.6.2 Problem Statement
Learning to be fair implies that the evaluation of an agent’s behaviour depends on
the outcomes of the actions of the other agents within the system. Intuitively, it
is hard to visualise what fair behaviour is, especially if the agents are placed in a
decentralised setting where they decide based on partial observation of the world.
In MADRL literature, fairness is approached as a goal that needs to be carefully
learned to prevent the agents from not being efficient at all. In particular, SOTO
employs an architecture that uses a self-oriented policy towards attempting to help
the fairness-oriented policy not forget what an efficient behaviour looks like.
While this is an intuitive syllogism towards finding the most fair-efficient
policies, there is yet, to the best of our knowledge, margin on exploring what
would be to considering these two goals not only independently but simultaneously.
That is, try to analyse the spectrum of behaviours between these to goals. In real
applications, a system designer may prefer an efficient solution that is as fair as
possible. Moreover, it is still unclear on what sort of impact learning fair and

326 M.Silvaetal.
efficient behaviours have on the final result that each of these ends up learning.
Motivated by this problem, we aim to address the following questions:
1. Can a range of behaviours be generated between two trained policies? Given
any two MARL trained sets of policies, it is possible to mix the policies being
utilised, making agents act heterogeneously. Is this range of performances linear
both in the fairness and efficiency dimensions? Are its extremes the ones that
provide better system’s performance in their respective dimension?
2. In the SOTO architecture, can different β(e ) training strategies generate
r .
solutions that Pareto-front the original model or selfish baseline?Theroleof
βin SOTO is functional—it is the probability of agents choosing to act under and
.
train the self-oriented policy instead of the team-oriented one. If β is high, the
.
behaviour of agents is then more selfish, and the self-oriented policy is trained
more often. The reverse happens when β is low. We aim to explore settings that
.
can generate solutions that Pareto-front SOTO or other independent baseline.
3. In such a model, what happens if the predictions of the team-oriented policy
are also provided to the self-oriented one? More specifically, we want to know
whether this new architecture generate solutions that Pareto-front the original
model or a selfish baseline. The inclusion of insights fromπIND as inputπSWF
. .
is for efficiency purposes, specially for agents that are under-performing. But
what if these insights were mutual, and the self-oriented policy also received fair
insights from the team-oriented policy? Is it possible that the inverse could be
beneficial? Are there any improvements in either fairness or efficiency? Does
this architecture function better under a particular β training strategy?
.
13.6.3 Heterogeneous Testing
We coin heterogeneous testing as the method utilised to explore fair vs.efficient
relative frequencies within the policies chosen by the agents. Remember that, from
SOTO, choosing either πIND and πSWF depended on the value of β(e ). Inspired
. . r .
by this, we employ the algorithm depicted in Algorithm 1 to test heterogeneous
behaviours from two different previously learned policies. In this case, β a fixed
.
parameter is provided as an argument that determines the probability of the agent
being attributed the self-oriented policy.
It is important that under this testing method, no agent acts only selfishly or fairly
but more often as to one of these according to β by the law of large numbers. The
.
intent is to expose the behaviour of interactions of each policy kind for each agent,
as all multi-agent architectures are independent per agent. Moreover, the policies
are never updated under this method. As such, this is only a testing method, putting
in evidence the policy resultant from training without changes.

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 327
Algorithm 1 Heterogeneous testing
1: Initialize π1 , π2 , v1 , v2 , respectively the pre-trained team-oriented/self-oriented policies,
i i i i
team-oriented/self-oriented critics.
2: for each episode e do
3: while episode e⎤ i(s not co)mpleted do
4: (πi, vi) ← (π
π
i 1
2
,
,
v
v
i 1
2
) w
ot
i
h
t
e
h
r
p
w
r
i
o
s
b
e
a bility β(er), er = E e
i i
5: Collect M a minibatch of transitions with πi
6: end while
7: endfor
13.6.4 Intertwined Self-Oriented Team-Oriented Networks
In the SOTO architecture, the inclusion of a self-oriented policy is intended to
provide a recommendation on how to act efficiently to the team-oriented one. It is
unknown, however, if the recommendations of a team-oriented policy could improve
the performance of the first as well.
We propose an extension to this architecture in which the self-oriented policy also
receives insights from the team-oriented policy, generating an intertwined sharing
of recommendations. We coin this model Intertwined Self-Oriented Team-Oriented
networks—I-SOTO. The team-oriented policy then receives as input the action
distribution resultant from forwardingπIND, as shown in Fig.13.2.
.
A problem that arises is the circular dependency between policy recommenda-
tions (or forwarded outputs). For instance, if we want to forward policyπSWF,first
.
we have to forward policyπIND. However, to forward this policy, we also need the
.
forwarded output of the first, which is dependent on the latter. In order to address this
Fig. 13.2 I-SOTO
architecture

| 328 |     |     |     | M.Silvaetal. |
| --- | --- | --- | --- | ------------ |
issue, whenever some policy π is being used, it forwards the other π ' substituting
|     |     | .   |     | .   |
| --- | --- | --- | --- | --- |
|A|
| the expected inputs from π | .   | with a null vector0 | . This null action recommendation  . |     |
| -------------------------- | --- | ------------------- | ------------------------------------ | --- |
could be seen as “no action”, since the output of the policies is the probability
distribution of each available action.
Note that the distribution of wealth Jis yet not passed to the self-oriented policy
.
to put in evidence the effect of intertwined selfish and fair policies.
| 13.6.5  | Training Strategy Functions  |     |     |     |
| ------- | ---------------------------- | --- | --- | --- |
In the context of this work, training strategy refers to the function ofβ(e r ), which  .
determines the probability of each agent choosing to act under the self-oriented
πIND
policy .  on a given episode for and on before mini-batch of M transitions.
Higher βmakes the agents train more the self-oriented policy and then vice-versa for
.
the team-oriented policy. Notice that, specially in I-SOTO, because learning one of
these policies has a potential impact on the other, using different training strategies
may improve the performance of the model.
= e
We test a variety of functions β(e r ), where . e r E.  is the episode rate, i.e. the
number of the current episode e divided by the total number of episodes E. In the
original training setting of SOTO,β(e )is a linearly decreasing function until half of
r .
1e
the episodes r. and constant from such point on-wards on 0. We use 4 different beta
e
families: constant, linear, baseline and v-shaped. A summary of their characteristics
is present in Table 13.4. Sample ratio refers to the ratio between the areas below
and under the curve, respectively. When β is higher,πINDis trained more often and
.  .
thus has access to a higher number of samples. The number of samples tends to the
proportions of the areas below and under the curve, by the law of large numbers.
The constant family is the most simple of all. Under this family, β is not
.
dependant  on  e r. ,  and  the  agents  train  selfishly/fairly  according  to  the  same
probability throughout episodes. In particular, we want to study two values of β:
.
0.25 and 0.5. Studying β = 0.5 is important as it gives the same opportunity for
.
Table 13.4  Strategy Functions by family: Constant, Linear (and its reverse version rl), Baseline
(and its reverse version rb) and V-shaped (and its reverse version rv)
| Family   | Variant | πIND ./πSWF .sample ratio | Equation  |     |
| -------- | ------- | ------------------------- | --------- | --- |
| Constant | 0.25    | 25/75                     | 0.25.     |     |
|          | 0.5     | 50/50                     | 0.5.      |     |
| Linear   | lin     | 50/50                     | er.       |     |
1−er.
|          | rlin | 50/50 |                |     |
| -------- | ---- | ----- | -------------- | --- |
| Baseline | b    | 25/75 | max(1−2er,0).  |     |
1−max(1−2er,0).
|          | rb  | 75/25 |                 |       |
| -------- | --- | ----- | --------------- | ----- |
| V-shaped | v   | 50/50 | max(1−2er,2er   | −1).  |
|          | rv  | 50/50 | 1−max(1−2er,2er | −1).  |

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 329
each policy πIND and πSWF to converge—equal sample ratio. On the other hand,
. .
studying β = 0.25 provides the same sample ratio as the baseline. Alternatively,
.
the linear family functions prolong the switch between choosing one or the other
policy to double a training period T compared to the baseline setting. We aim to test
whether the stabilising training period of baseline after T episodes is necessary, or
2.
if most of its performance gains come from slowly switching from self-oriented to
team-oriented. As for the baseline family, it comprises the baseline setting of SOTO
and its reverse, rb (see Table 13.4). Notice that the reverse variant ends up being
very similar to the independent baseline except that 25% of the samples are, in the
first half of episodes, directed to the team-oriented policy during training. Finally,
derived from the baseline alternative, v-shaped functions are intended to provide
the same function as baseline until E episodes and then return to the initial value
2.
linearly in a V-shaped manner. The interest relies on testing whether should the
system progressively return to the initially dominant policy during training, there is
an improvement of its behaviour afterwards.
As such, we extend the literature by exploring fair and efficient goals in a holistic
manner by evaluating execution and training methods which combine them, hoping
to find competitive solutions in both goals.
13.7 Experimental Results and Discussion
13.7.1 Evaluation
All of these methods are evaluated through simulation. We choose two environments
in which is the resource opportunity is unequal—Matthew Effect and Traffic Light
Control. As baselines, we use the original SOTO model and the same Independent
baseline utilised in its paper, which has the same architecture of SOTO self-oriented
policy. In each environment, a domain-specific meEasure per time step and agent
mi is considered. Given u = {u ,i ∈ D},u = T mi, metrics recorded were
t. E E i i t t.
the total as T |D| mi, CV2 as std( u)/mean( u), the min min(u) and the max
t i t. . . .
max(u). Lower values of CV indicate fairer solutions. Higher/Lower values of total
.
provide information on the efficiency of the model, depending whether m is to
t.
be maximised/minimised on the environment. All policies use PPO optimisation.
The importance sampling has a 0.03 exploration bonus and 0.1 clipping ratio. The
learning rate is 10
−3
for the critic and 2.5
−3
for the actor. Generalised Advantage
. .
Estimation was utilised with λ = 0.97. The neural networks have two hidden
.
layers with 256 ReLU units each. We used 50 time step batches of transitions. Two
Social Welfare Functions (SWF) were utilised: an instance of the Generalised Gini
Function, withw = 1 and an instance of α-fairness withα =0.9.
i 2i. . .
2 Coefficient of Variation.

330 M.Silvaetal.
Each model is trained three times with different seeds for stochastic processes.
The results presented are the average of every seed instance tested in 50 episodes.
The values of β used for heterogeneous behaviour were{0.02i,∀i ∈{0,1,...50}},
.  .
for models where this is applicable.
| 13.7.2  Matthew  | Effect Problem  |     |
| ---------------- | --------------- | --- |
In the Matthew Effect environment, a set of 10 agents is placed in a map. Whenever
an agent consumes a ghost, it gets bigger and faster, and a new ghost is spawned. As
such, those who consume are more likely to consume again. In other words, the rich
get richer and the poor get poorer. This is called the Matthew effect. The goal is to
maximise the income, in this case the number of consumed ghosts n. The recorded
measure for this environment coincides with n and the reward signal r, such that
| m =r =n                                                      | .   |     |
| ------------------------------------------------------------ | --- | --- |
| t t t.                                                       |     |     |
| 13.7.2.1  Behavior Generation Through Heterogeneous Testing  |     |     |
We present the behaviour outcomes of heterogeneous testing between different pairs
of policies, trained with the SOTO model, in the following paragraphs.
πINDversusπSWF
| 13.7.2.1.1 | .   | .   |
| ---------- | --- | --- |
SOTO trains two policies with different aims: a self-and a team-oriented goal. The
results of the heterogeneous behaviour produced by these policies in the Matthew
Effect environment is depicted in Fig.13.3. It seems that the two SWFs utilised can
Fig. 13.3  Heterogeneous behaviour between SOTO’sπIND .andπSWF .in Matthew Effect

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 331
Fig. 13.4 Heterogeneous behaviour between SOTO and Independent in Matthew Effect
generate ranges of behaviour, according to β, in two different directions. Regarding
.
fairness, as expected, the lower values of β seem to be associated with lower CV
.
values. This means the higher the probability of each agent to act under πSWF,
.
the fairer the system is, globally. On the other hand, with regards to efficiency,
a more complex scenario occurs. Unexpectedly, for SOTO(α ), there seems to be
.
an inverse relationship between β and the value of total income. Indeed, the most
.
efficient policy is also the fairest. As for SOTO( G ), such a relationship is no
w.
longer linear. The most efficient policy is an intermediate behaviour between the
two extremes πIND and πSWF. It is possible to observe that these two SWFs have
. .
quite distinct behaviours under this environment. However, a similarity between
them is the proximity in performance between self-oriented extremes in each SWF.
We believe this may be because such policy only trains for 25% of the training
samples. This would also justify why the efficiency of such policy is comparatively
mediocre, despite its training goal being directly oriented towards efficiency.
13.7.2.1.2 SOTO versus Independent
We test mixing SOTO with the Independent baseline. The results of this attempt are
depicted in Fig.13.4. As we can see, no Pareto solutions are found.Both ranges of
behaviours produced non-linear shapes.
13.7.2.2 I-SOTO and Training Strategies
We present the results for I-SOTO under different training strategies in Table 13.5.
As can be seen, some solutions are able to outperform SOTO. For the αSWF, the rlin
.
and b functions are both fairer and more efficient than this baseline. These functions
are the only ones where β decreases (weakly) throughout episodes, so perhaps this
.

| 332 |     |     |     | M.Silvaetal. |     |
| --- | --- | --- | --- | ------------ | --- |
Table 13.5  Training
|     | Model | β. π. | Total  CV  | Min | Max  |
| --- | ----- | ----- | ---------- | --- | ---- |
strategies (β  .) performance
|     | I-SOTO( α.) | 0.25  IND  | 1440  0.75 | 11.80  | 356  |
| --- | ----------- | ---------- | ---------- | ------ | ---- |
under the self-(IND) and
| team-oriented (SWF) policies  |     | SWF      | 1529  0.48  | 35.22  | 271  |
| ----------------------------- | --- | -------- | ----------- | ------ | ---- |
| in Matthew Effect. Bold       |     | 0.5 IND  | 1626  0.66  | 24.18  | 385  |
values are entries which
|     |     | SWF  | 1378  0.53 | 15.67  | 240  |
| --- | --- | ---- | ---------- | ------ | ---- |
perform equal or better than
|     |     | lin IND  | 1771  0.64 | 31.42  | 417  |
| --- | --- | -------- | ---------- | ------ | ---- |
the baseline (b) of the
| respective model, in Total   |     | SWF       | 888  0.69   | 4.77   | 167  |
| ---------------------------- | --- | --------- | ----------- | ------ | ---- |
| Income (higher) or CV        |     | rlin IND  | 1617  0.64  | 23.68  | 372  |
| (lower), i.e. efficiency or  |     | SWF       | 1680  0.48  | 38.34  | 306  |
fairness
|     |               | b IND       | 1138  0.94  | 3.69    | 338  |
| --- | ------------- | ----------- | ----------- | ------- | ---- |
|     |               | SWF         | 1756  0.44  | 58.02   | 316  |
|     |               | rb IND      | 1859  0.65  | 23.31   | 423  |
|     |               | SWF         | 99  1.28    | 0.16    | 37   |
|     |               | v IND       | 1641  0.64  | 22.59   | 372  |
|     |               | SWF         | 1473  0.56  | 29.96   | 293  |
|     |               | rv IND      | 1573  0.68  | 17.12   | 374  |
|     |               | SWF         | 1550  0.52  | 21.75   | 282  |
|     | SOTO(α  .)    | b IND       | 1178  0.90  | 5.88    | 342  |
|     |               | SWF         | 1663  0.49  | 43.29   | 297  |
|     | I-SOTO( Gw.)  | 0.25  IND   | 1178  0.86  | 6.91    | 327  |
|     |               | SWF         | 733  0.21   | 43.32   | 87   |
|     |               | 0.5 IND     | 1552  0.64  | 25.88   | 358  |
|     |               | SWF         | 130  0.89   | 0.90    | 34   |
|     |               | lin IND     | 1724  0.67  | 22.82   | 407  |
|     |               | SWF         | 37  1.09    | 0.07    | 10   |
|     |               | rlin IND    | 1210  0.84  | 7.47    | 332  |
|     |               | SWF         | 649  0.33   | 24.33   | 87   |
|     |               | b IND       | 1156  0.88  | 5.63    | 326  |
|     |               | SWF         | 1035  0.01  | 101.06  | 106  |
|     |               | rb IND      | 1799  0.71  | 15.05   | 433  |
|     |               | SWF         | 11  1.58    | 0.01    | 5    |
|     |               | v IND       | 1479  0.77  | 13.61   | 372  |
|     |               | SWF         | 355  0.88   | 2.68    | 100  |
|     |               | rv IND      | 1241  0.81  | 8.97    | 325  |
|     |               | SWF         | 581  0.37   | 18.50   | 81   |
|     | SOTO(G  w.)   | b IND       | 1139  0.86  | 9.00    | 324  |
|     |               | SWF         | 1052  0.03  | 99.68   | 109  |
|     | Independent   | N.A.  N.A.  | 1793  0.73  | 8.11    | 421  |

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 333
could be an intuition on the ideal function to be used in this SWF and environment.
Moreover, forG , it seems that no solution is better in both goals. We found that the
w.
baseline training strategy is able to improve in fairness, which is remarkable since
it was already very close to 0 in SOTO.
Comparing to the Independent baseline, there are solutions in both SWF that
outperform it both in fairness and efficiency. For α, the b function is the one which
.
does this with greater difference. Another interesting result for this SWF is the rb
function, achieving an even higher value of efficiency. ForG , the rb alternative is
w.
able to have slightly higher efficiency and fairness (lower CV).
13.7.3 Traffic Light Control Problem
This environment consists of a3×3grid of lanes where the traffic light state of each
.
intersection is controlled by an agent. The goal is to minimise the total weighting
time in all intersections w. As such, the reward provided to agents at each time
step is r t. =w t−1 −w t. . However, as measure, we simply record the weighting time
such that m = w . Notice that, contrary to the previous environment, the reward
t. t.
attributed to each agent dependents on external factors: the vehicles waiting in
such intersection. Again, this will naturally provide agents unequal opportunities
to receiving rewards, as waiting times of intersections dependent highly on the
trajectories of the vehicles, waiting times of other intersections, etc.
13.7.3.1 Behavior Generation Through Heterogeneous Testing
The results of the heterogeneous behaviour produced by the self-and team-oriented
policies of SOTO are depicted in Fig.13.5. It is possible to observe that the range of
SOTO behaviours generated is approximately linear in the efficiency-fairness space.
The team-oriented end is both the more efficient and fair than the self-oriented one.
When compared to the previous environment, this phenomenon also occurred for the
α-fairness metric. In theG , the performance range was not linear in the efficiency
. w.
dimension, so we can conclude that the behaviour of the same SWF can be different
under different environments.
Regarding the range of behaviours generated by πIND and πSWF, it seems to
. .
be sparser than in the Matthew Effect. Nonetheless, the Independent baseline over-
performs SOTO in any option of the range. For this reason, we did not proceed
with experiments testing heterogeneous behaviour between these two options, as
one already Pareto-fronts the other. An intuition for this phenomenon would be the
dependence between agents rewards causing a correlation between efficiency and
fairness. Under that assumption, a model which focuses 100% entirely on one of
them, compare to a model which divides samples between two policies, is more
likely to succeed in both goals should they be correlated.

334 M.Silvaetal.
Fig. 13.5 Heterogeneous behaviour between SOTO’sπIND .andπSWF .in Traffic Light Control
13.7.3.2 I-SOTO and Training Strategies
As in the previous environment, we present the results of I-SOTO in this environ-
ment in Table 13.6. As can be seen, many I-SOTO solutions are both more efficient
and fair than the SOTO baseline. In particular, at least one extreme in each training
strategy utilised outperforms SOTO. The most prominent of them would be the
rb training strategy function. This is the option with most samples dedicated to
IND.
the selfish goal, being in agreement with the intuition that fairness and efficiency—
in this environment—are somewhat correlated. This is also corroborated with the
fact that the most competitive options are on the self-oriented side of I-SOTO, and
not the team-oriented one as occurred in Matthew. As for the Independent baseline,
a similar phenomenon occurs. Only the constant functions are not able to compete
with these baseline, interestingly. While it is hard to provide an explanation for why
this happened, one hypothesis could be that these are the only ones where samples
are never entirely dedicated to one of the policies—or, more importantly in this
case—the self-oriented one.
To conclude, there is a broader analysis than can be made relative to the whole
experimental set. With regards to the self-and team-oriented policies in any of the
models, there seems to be a pattern where either (1)πSWFis the most fair andπIND
. .
is the most efficient policy, or that (2)πSWF is both the most efficient and fair. The
.
latter case occurs for SOTO( α) in Matthew Effect and SOTO( G ) in Traffic Light
. w.
Signal. While we are not able to provide an exact explanation of why this happens,
there are two potential intuitions for this reason.
On the one hand, it may have to do with the nature of the environment. As
previously seen, in Traffic Light Control, the success of an agent (intersection) is
highly dependent on the success of other agents. This leads to the intuition that
finding a fair solution, in this environment, is also finding an efficient one. A result
that is in agreement with this is the fact that the best performing model in this
environment is I-SOTO( G ) with the constant 0.5 strategy function, in which self-
w.

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 335
Table  13.6  I-SOTO performance under the self- (IND) and team-oriented (SWF) policies in
Matthew Effect. Bold values are entries which perform equal or better than the baseline (b) of
the respective model, in Total Income (higher) or CV (lower), i.e. efficiency or fairness
| Model        | β. π.     | Total    | CV Min       | Max      |
| ------------ | --------- | -------- | ------------ | -------- |
| I-SOTO( Gw.) | 0.25 IND  | 3.70e+05 | 0.08 8.5e+02 | 3.6e+04  |
|              | SWF       | 3.70e+05 | 0.09 1.2e+03 | 2.9e+04  |
|              | 0.5 IND   | 3.33e+05 | 0.14 8.4e+02 | 3.2e+04  |
|              | SWF       | 4.54e+05 | 0.12 2.2e+03 | 3.7e+04  |
|              | b IND     | 3.60e+05 | 0.09 9.8e+02 | 3.1e+04  |
|              | SWF       | 3.50e+05 | 0.08 9.8e+02 | 2.9e+04  |
|              | lin IND   | 3.36e+05 | 0.09 8.8e+02 | 3.3e+04  |
|              | SWF       | 4.72e+05 | 0.10 1.5e+03 | 4.2e+04  |
|              | rb IND    | 3.34e+05 | 0.06 7.7e+02 | 4.0e+04  |
|              | SWF       | 7.39e+05 | 0.16 2.8e+03 | 6.4e+04  |
|              | rlin IND  | 3.57e+05 | 0.13 9.7e+02 | 3.6e+04  |
|              | SWF       | 4.20e+05 | 0.11 1.4e+03 | 3.6e+04  |
|              | rv IND    | 3.44e+05 | 0.08 9.7e+02 | 3.3e+04  |
|              | SWF       | 4.38e+05 | 0.10 1.5e+03 | 3.5e+04  |
|              | v IND     | 3.37e+05 | 0.08 7.9e+02 | 3.2e+04  |
|              | SWF       | 4.24e+05 | 0.09 1.2e+03 | 3.4e+04  |
| SOTO(G  w.)  | b IND     | 4.03e+05 | 0.19 9.4e+02 | 4.1e+04  |
|              | SWF       | 3.83e+05 | 0.16 1.2e+03 | 3.2e+04  |
| Independent  | N.A. N.A. | 3.65e+05 | 0.13 9.8e+02 | 4.2e+04  |
and team-oriented insights are shared between policies and in a balanced (50/50)
way between goals.
On the other hand, this may also have to do with the nature of the social welfare
function utilised. As seen in Sect.13.6.1, the self- and team-oriented advantages
utilised in the training process are a product of the derivative of the SWF with
ˆ
respect to the agents utilities, ∇ φ(J (θ)) T , with the original advantage. In the
u .
|     |     | u0.9, while on the |     | =   |
| --- | --- | ------------------ | --- | --- |
α-fairness scenario, this derivative is . . G w.  setting it is w
−i,∀
{2 i∈D } . This means that the team-oriented advantage for the first case is a
.
sum of an exponential function to the agents utilities as opposed to a weighted
sum based on their ranking. The fact that this function interprets social welfare as
an independent concept from the ranking of individual utilities within the system
perhaps deposits more confidence in individual success—efficiency—as a means
towards fairness. Considering the utility order overall produces much fairer results
as it ensures no agent is being left behind. This, however, comes at the cost of a
great deal in efficiency.
13.8  Conclusion
We approach fairness and efficiency in a holistic manner: either by mixing pre-
trained efficient and fair policies or by changing the learning method of SOTO such

336 M.Silvaetal.
that fair-efficient recommendations are intertwined—I-SOTO. In the latter, we were
able to find some solutions which outperformed not only the fair baseline but also
the efficient baseline utilised. Despite being initial attempts in the problem, these are
important results towards better understanding the fairness-efficiency relationship.
With regards to our hypothesis we find that the heterogeneous behaviours found
between efficient and fair policies are not always linear, unexpectedly. For I-SOTO,
we confirmed that some results were indeed better performing than SOTO but for
theG SWF no solution was found to be better in both of the goals at study.
w.
This new approach to address fairness and efficiency could be particularly
important in systems with endogenous resources: i.e. computation of the reward
distribution has to be paid for from the rewards themselves so that learning a
fair and efficient combination with respect to available resources is particularly
important. For that we intend to expand the testing space along different dimensions:
environments, SWFs and training strategies.
References
1. B.H. Abed-Alguni, D.J. Paul, S.K. Chalup, F.A. Henskens, A comparison study of cooperative
q-learning algorithms for independent learners. Int. J. Artif. Intell. 14(1), 71–93 (2016)
2. E. Amaldi, S. Coniglio, L.G. Gianoli, C.U. Ileri, On single-path network routing subject to
max-min fair flow allocation. Electron Notes Discrete Math. 41, 543–550 (2013)
3. W. Bao, Fairness in Multi-agent Reinforcement Learning for Stock Trading. arXiv (2019).
http://arxiv.org/abs/2001.00918
4. R. Bellman, Dynamic programming. Science 153(3731), 34–37 (1966)
5. D. Bertsimas, V.F. Farias, N. Trichakis, The price of fairness. Oper. Res. 59(1), 17–31 (2011)
6. S.J. Brams, S.J. Brams, A.D. Taylor, Fair Division: From Cake-Cutting to Dispute Resolution
(Cambridge University Press, Cambridge, 1996)
7. T. Brys, A. Harutyunyan, P. Vrancx, A. Nowé, M.E. Taylor, Multi-objectivization and
ensembles of shapings in reinforcement learning. Neurocomputing 263, 48–59 (2017)
8. R. Busa-Fekete, B. Szörényi, P. Weng, S. Mannor, Multi-objective bandits: optimizing the
generalized Gini index, in International Conference on Machine Learning. PMLR (2017), pp.
625–634
9. L. Busoniu, R. Babuska, B. De Schutter, A comprehensive survey of multiagent reinforcement
learning. IEEE Trans. Syst. Man Cybern. C (Appl. Rev.) 38(2), 156–172 (2008)
10. L. Bus¸oniu, R. Babuška, B. De Schutter, Multi-agent reinforcement learning: an overview, in
Innovations in Multi-Agent Systems and Applications-1 (Springer, Berlin, 2010), pp. 183–221
11. J. Castellini, S. Devlin, F.A. Oliehoek, R. Savani, Difference Rewards Policy Gradients (2020).
http://arxiv.org/abs/2012.11258
12. Y.H. Chang, T. Ho, L.P. Kaelbling, All learning is local: multi-agent learning in global reward
games, in Advances in Neural Information Processing Systems 16 (NIPS 2003), 2003, ed. by
S. Thrun, L. Saul, B. Schölkopf (2004). https://papers.nips.cc/paper_files/paper/2003
13. D. Chen, Q. Qi, Z. Zhuang, J. Wang, J. Liao, Z. Han, Mean field deep reinforcement learning
for fair and efficient UAV control. IEEE Internet Things J. 8(2), 813–828 (2021). https://doi.
org/10.1109/JIOT.2020.3008299
14. Y. Chevaleyre, P.E. Dunne, U. Endriss, J. Lang, M. Lemaître, N. Maudet, J. Padget, S. Phelps,
J.A. Rodríguez-Aguilar, P. Sousa, Issues in multiagent resource allocation. Informatica 30(1),
3–31 (2006)
15. F. Chierichetti, R. Kumar, S. Lattanzi, S. Vassilvitskii, Fair clustering through fairlets. arXiv
preprint arXiv:1802.05733 (2018)

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 337
16. H. Claure, Y. Chen, J. Modi, M. Jung, S. Nikolaidis, Multi-armed bandits with fairness con-
straints for distributing resources to human teammates, in ACM/IEEE International Conference
on Human-Robot Interaction (2019), pp. 299–308. http://arxiv.org/abs/1907.00313
17. H. Claure, Y. Chen, J. Modi, M. Jung, S. Nikolaidis, Reinforcement learning with fairness
constraints for resource distribution in human-robot teams. arXiv preprint arXiv:1907.00313
(2019)
18. S. De Jong, K. Tuyls, K. Verbeeck, Fairness in multi-agent systems. Knowl. Eng. Rev. 23(2),
153–180 (2008)
19. A.K. Dixit, J.J. Sherrerd, et al., Optimization in Economic Theory (Oxford University Press on
Demand, Oxford, 1990)
20. S. Dreyfus, Richard bellman on the birth of dynamic programming. Oper. Res. 50(1), 48–51
(2002)
21. G. Dulac-Arnold, D. Mankowitz, T. Hester, Challenges of Real-World Reinforcement Learn-
ing. arXiv (2019). http://arxiv.org/abs/1904.12901
22. C. Dwork, M. Hardt, T. Pitassi, O. Reingold, R. Zemel, Fairness through awareness, in
Proceedings of the 3rd Innovations in Theoretical Computer Science Conference (2012), pp.
214–226
23. S. Elmalaki, Fair-iot: fairness-aware human-in-the-loop reinforcement learning for harnessing
human variability in personalized IoT, in Proceedings of the International Conference on
Internet-of-Things Design and Implementation (2021), pp. 119–132
24. J. Foerster, G. Farquhar, T. Afouras, N. Nardelli, S. Whiteson, Counterfactual multi-agent
policy gradients, in 32nd AAAI Conference on Artificial Intelligence, AAAI 2018 (2017), pp.
2974–2982. http://arxiv.org/abs/1705.08926
25. T. Haarnoja, A. Zhou, P. Abbeel, S. Levine, Soft actor-critic: off-policy maximum entropy
deep reinforcement learning with a stochastic actor, in International Conference on Machine
Learning. PMLR (2018), pp. 1861–1870
26. J. Hao, H.f. Leung, Fairness in Cooperative Multiagent Systems (2016), pp. 27–70. https://doi.
org/10.1007/978-3-662-49470-7_3
27. M.J. Hausknecht, Cooperation and communication in multiagent deep reinforcement learning.
Ph.D. thesis (2016)
28. M. Hausknecht, P. Stone, Deep recurrent q-learning for partially observable MDPs, in AAAI
Fall Symposium. Technical Report, vol. FS-15-06. AI Access Foundation (2015), pp. 29–37.
www.aaai.org
29. S. Huaizhou, R.V. Prasad, E. Onur, I. Niemegeers, Fairness in wireless networks: issues,
measures and challenges. IEEE Commun. Surv. Tutor. 16(1), 5–24 (2013)
30. E. Hughes, J.Z. Leibo, M. Phillips, K. Tuyls, E. Dueñez-Guzman, A.G. Castañeda, I. Dunning,
T. Zhu, K. McKee, R. Koster, et al., Inequity aversion improves cooperation in intertemporal
social dilemmas, in Proceedings of the 32nd International Conference on Neural Information
Processing Systems (2018), pp. 3330–3340
31. A. Hussein, M.M. Gaber, E. Elyan, C. Jayne, Imitation learning: a survey of learning methods.
ACM Comput. Surv. 50(2), 1–35 (2017)
32. S. Iqbal, F. Sha, Actor-attention-critic for multi-agent reinforcement learning, in International
Conference on Machine Learning. PMLR (2019), pp. 2961–2970
33. S. Jabbari, M. Joseph, M. Kearns, J. Morgenstern, A. Roth, Fairness in reinforcement learning,
in International Conference on Machine Learning. PMLR (2017), pp. 1617–1626
34. R.K. Jain, D.M.W. Chiu, W.R. Hawe, et al., A quantitative measure of fairness and discrimina-
tion. Eastern Research Laboratory, Digital Equipment Corporation, Hudson (1984)
35. J. Jiang, Z. Lu, Learning fairness in multi-agent systems. Adv. Neural Inf. Process. Syst. 32,
13854–13865 (2019)
36. J. Jiang, C. Dun, T. Huang, Z. Lu, Graph convolutional reinforcement learning, in International
Conference on Learning Representations (2019)
37. S. Jong, K. Tuyls, K. Verbeeck, N. Roos, Considerations for fairness in multi-agent systems.
Undefined (2007)
38. M. Joseph, M. Kearns, J. Morgenstern, A. Roth, Fairness in learning: classic and contextual
bandits. arXiv preprint arXiv:1605.07139 (2016)

338 M.Silvaetal.
39. L.P. Kaelbling, M.L. Littman, A.R. Cassandra, Planning and acting in partially observable
stochastic domains. Artif. Intell. 101(1–2), 99–134 (1998). https://doi.org/10.1016/s0004-
3702(98)00023-x
40. D.P. Kingma, J. Ba, Adam: a method for stochastic optimization. arXiv preprint
arXiv:1412.6980 (2014)
41. V.R. Konda, J.N. Tsitsiklis, Actor-critic algorithms, in Advances in Neural Information
Processing Systems (2000), pp. 1008–1014
42. L. Kraemer, B. Banerjee, Multi-agent reinforcement learning as a rehearsal for decentralized
planning. Neurocomputing 190, 82–94 (2016). https://doi.org/10.1016/j.neucom.2016.01.031
43. M.J. Kusner, J.R. Loftus, C. Russell, R. Silva, Counterfactual fairness. arXiv preprint
arXiv:1703.06856 (2017)
44. K. Lamertz, The social construction of fairness: social influence and sense making in
organizations. J. Organ. Behav. 23(1), 19–37 (2002)
45. T.P. Lillicrap, J.J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, D. Wierstra, Contin-
uous control with deep reinforcement learning, in 4th International Conference on Learning
Representations, ICLR 2016 - Conference Track Proceedings. International Conference on
Learning Representations, ICLR (2016). https://goo.gl/J4PIAz
46. S. Liu, M. Araujo, E. Brunskill, R. Rossetti, J. Barros, R. Krishnan, Understanding sequential
decisions via inverse reinforcement learning, in 2013 IEEE 14th International Conference on
Mobile Data Management, vol. 1 (2013), pp. 177–186. https://doi.org/10.1109/MDM.2013.28
47. R. Lowe, Y. Wu, A. Tamar, J. Harb, P. Abbeel, I. Mordatch, Multi-agent actor-critic for mixed
cooperative-competitive environments. Adv. Neural Inf. Process. Syst. 2017-December, 6380–
6391 (2017). http://arxiv.org/abs/1706.02275
48. H. Luss, Equitable Resource Allocation: Models, Algorithms and Applications, vol. 101. (John
Wiley & Sons, Hoboken, 2012)
49. L. Matignon, L. Jeanpierre, A.I. Mouaddib, Coordinated multi-robot exploration under com-
munication constraints using decentralized Markov decision processes, in Twenty-Sixth AAAI
Conference on Artificial Intelligence (2012)
50. V. Mnih, A.P. Badia, M. Mirza, A. Graves, T.P. Lillicrap, T. Harley, D. Silver, K. Kavukcuoglu,
Asynchronous methods for deep reinforcement learning, in 33rd International Conference on
Machine Learning, ICML 2016, vol. 4 (2016), pp. 2850–2869. http://arxiv.org/abs/1602.01783
51. J. Mo, J. Walrand, Fair end-to-end window-based congestion control. IEEE/ACM Trans. Netw.
8(5), 556–567 (2000)
52. H. Moulin, Fair Division and Collective Welfare (MIT Press, Cambridge, 2003)
53. A. Neidhardt, H. Luss, K. Krishnan, Data fusion and optimal placement of fixed and mobile
sensors, in 2008 IEEE Sensors Applications Symposium. IEEE (2008), pp. 128–133
54. A.Y. Ng, S. Russell, Algorithms for inverse reinforcement learning, in Proc. 17th International
Conf. on Machine Learning. Morgan Kaufmann (2000), pp. 663–670
55. W. Ogryczak, P. Perny, P. Weng, A compromise programming approach to multiobjective
markov decision processes. Int. J. Inf. Technol. Decis. Mak. 12(05), 1021–1053 (2013)
56. W. Ogryczak, H. Luss, M. Pióro, D. Nace, A. Tomaszewski, Fair optimization and networks: a
survey. J. Appl. Math. 2014 (2014)
57. F.A. Oliehoek, C. Amato, A Concise Introduction to Decentralized POMDPs. SpringerBriefs in
Intelligent Systems. Springer International Publishing, Cham (2016). https://doi.org/10.1007/
978-3-319-28929-8. http://link.springer.com/10.1007/978-3-319-28929-8
58. F.A. Oliehoek, M.T. Spaan, N. Vlassis, Optimal and approximate Q-value functions for
decentralized POMDPs. J. Artif. Intell. Res. 32, 289–353 (2008). https://doi.org/10.1613/jair.
2447
59. A. OroojlooyJadid, D. Hajinezhad, A Review of Cooperative Multi-Agent Deep Reinforcement
Learning. arXiv (2019). http://arxiv.org/abs/1908.03963
60. M. Pióro, G. Malicskó, G. Fodor, Optimal link capacity dimensioning in proportionally fair
networks, in International Conference on Research in Networking (Springer, 2002), pp. 277–
288

13 ExploringtheEfficiencyvs.FairnessBehaviouralSpectruminMulti-... 339
61. J. Pitt, Interactional justice and self-governance of open self-organising systems, in Proceed-
ings - 11th IEEE International Conference on Self-Adaptive and Self-Organizing Systems,
SASO 2017 (Institute of Electrical and Electronics Engineers Inc., 2017), pp. 31–40. https://
doi.org/10.1109/SASO.2017.12
62. J. Pitt, D. Busquets, S. Macbeth, Distributive justice for self-organised common-pool resource
management. ACM Trans. Auton. Adapt. Syst. 9(3), 1–39 (2014). https://doi.org/10.1145/
2629567. https://dl.acm.org/doi/10.1145/2629567
63. M.L. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming (John
Wiley & Sons, Hoboken, 2014)
64. T. Rashid, M. Samvelyan, C.S. de Witt, G. Farquhar, J. Foerster, S. Whiteson, QMIX:
Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning
(2018). http://arxiv.org/abs/1803.11485
65. J. Rawls, A Theory of Justice (Harvard University Press, Cambridge, 1971). http://www.jstor.
org/stable/j.ctvjf9z6v
66. H. Ryu, H. Shin, J. Park, Multi-Agent Actor-Critic with Hierarchical Graph Attention Network.
arXiv (2019). http://arxiv.org/abs/1909.12557
67. N.A. Saxena, K. Huang, E. DeFilippis, G. Radanovic, D.C. Parkes, Y. Liu, How do fairness
definitions fare? Examining public attitudes towards algorithmic definitions of fairness, in
Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society (2019), pp. 99–
106
68. J. Schulman, S. Levine, P. Abbeel, M. Jordan, P. Moritz, Trust region policy optimization, in
International Conference on Machine Learning. PMLR (2015), pp. 1889–1897
69. J. Schulman, P. Moritz, S. Levine, M. Jordan, P. Abbeel, High-dimensional continuous control
using generalized advantage estimation. arXiv preprint arXiv:1506.02438 (2015)
70. J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov, Proximal policy optimization
algorithms. arXiv preprint arXiv:1707.06347 (2017)
71. H. Shen, K. Zhang, M. Hong, T. Chen, Asynchronous Advantage Actor Critic: Non-asymptotic
Analysis and Linear Speedup (2020). http://arxiv.org/abs/2012.15511
72. H. Shi, R.V. Prasad, E. Onur, I.G.M.M. Niemegeers, Fairness in wireless networks: issues,
measures and challenges. IEEE Commun. Surv. Tutor. 16(1), 5–24. First Quarter 2014, https://
doi.org/10.1109/SURV.2013.050113.00015
73. Y. Shoham, K. Leyton-Brown, Multiagent Systems: Algorithmic, Game-Theoretic, and Logical
Foundations (Cambridge University Press, Cambridge, 2008)
74. A.F. Shorrocks, The class of additively decomposable inequality measures. Econometrica 48,
613–25 (1980)
75. U. Siddique, P. Weng, M. Zimmer, Learning fair policies in multi-objective (deep) reinforce-
ment learning with average and discounted rewards, in International Conference on Machine
Learning. PMLR (2020), pp. 8905–8915
76. K. Son, D. Kim, W.J. Kang, D.E. Hostallero, Y. Yi, Qtran: learning to factorize with
transformation for cooperative multi-agent reinforcement learning, in International Conference
on Machine Learning. PMLR (2019), pp. 5887–5896
77. M.T. Spaan, Partially observable markov decision processes, in Adaptation, Learning, and
Optimization, vol. 12. Springer Verlag (2012), pp. 387–414. https://doi.org/10.1007/978-3-
642-27645-3\protect\T1\textbraceleft\T1\textbackslash_\protect\T1\textbraceright12. https://
link.springer.com/chapter/10.1007/978-3-642-27645-3_12
78. T. Speicher, H. Heidari, N. Grgic-Hlaca, K.P. Gummadi, A. Singla, A. Weller, M.B. Zafar,
A unified approach to quantifying algorithmic unfairness: measuring individual &group
unfairness via inequality indices, in Proceedings of the 24th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining (2018), pp. 2239–2248
79. P. Sunehag, G. Lever, A. Gruslys, W.M. Czarnecki, V. Zambaldi, M. Jaderberg, M. Lanctot,
N. Sonnerat, J.Z. Leibo, K. Tuyls, T. Graepel, Value-decomposition networks for cooperative
multi-agent learning based on team reward, in Proceedings of the International Joint Confer-
ence on Autonomous Agents and Multiagent Systems, AAMAS, vol. 3 (2018), pp. 2085–2087.
http://arxiv.org/abs/1706.05296

340 M.Silvaetal.
80. R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction (A Bradford Book,
Cambridge, 2018)
81. M. Tan, Multi-agent reinforcement learning: independent vs. cooperative agents, in Proceed-
ings of the Tenth International Conference on Machine Learning (1993), pp. 330–337
82. S. Verma, J. Rubin, Fairness definitions explained, in 2018 IEEE/ACM International Workshop
on Software Fairness (Fairware). IEEE (2018), pp. 1–7
83. J. Wang, Y. Zhang, T.K. Kim, Y. Gu, Shapley q-value: a local reward approach to solve global
reward games, in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 34 (2020),
pp. 7285–7292
84. C.J.C.H. Watkins, Learning from delayed rewards (Doctoral dissertation). University of
Cambridge (1989)
85. C.J. Watkins, P. Dayan, Q-learning. Mach. Learn. 8(3–4), 279–292 (1992)
86. P. Weng, Fairness in reinforcement learning, in 34th International Conference on Machine
Learning, ICML 2017, vol. 4 (2019), pp. 2542–2557. http://arxiv.org/abs/1907.10323
87. J.A. Weymark, Generalized Gini inequality indices. Math. Soc. Sci. 1(4), 409–430 (1981)
88. R.J. Williams, Simple statistical gradient-following algorithms for connectionist reinforcement
learning. Mach. Learn. 8(3–4), 229–256 (1992). https://doi.org/10.1007/bf00992696. https://
link.springer.com/article/10.1007/BF00992696
89. E. Yang, D. Gu, Multiagent Reinforcement Learning for Multi-Robot Systems: A Survey.
Undefined (2004)
90. L. Yliniemi, K. Tumer, Multi-objective multiagent credit assignment through difference
rewards in reinforcement learning, in Lecture Notes in Computer Science (including subseries
Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 8886
(2014), pp. 407–418. https://doi.org/10.1007/978-3-319-13563-2_35. https://link.springer.
com/chapter/10.1007/978-3-319-13563-2_35
91. M. Yuan, Q. Cao, M.o. Pun, Y. Chen, Fairness-Oriented Scheduling for Bursty Traffic in
OFDMA Downlink Systems Using Multi-Agent Reinforcement Learning (2020). http://arxiv.
org/abs/2012.15081
92. C. Zhang, J.A. Shah, Fairness in multi-agent sequential decision-making, in Advances in
Neural Information Processing Systems (2014), pp. 2636–2644
93. K. Zhang, Z. Yang, H. Liu, T. Zhang, T. Basar, Fully decentralized multi-agent reinforcement
learning with networked agents, in International Conference on Machine Learning. PMLR
(2018), pp. 5872–5881
94. M. Zimmer, C. Glanois, U. Siddique, P. Weng, Learning fair policies in decentralized
cooperative multi-agent reinforcement learning, in International Conference on Machine
Learning (2021)
95. I. Žliobaite˙, Measuring discrimination in algorithmic decision making. Data Min. Knowl.
Discov. 31(4), 1060–1089 (2017)
96. H. Zou, T. Ren, D. Yan, H. Su, J. Zhu, Reward Shaping via Meta-Learning (2019). http://arxiv.
org/abs/1901.09330

Chapter 14
Resilient Agent-Based Networks in
the Automotive Industry
Ana Nogueira, Conceição Rocha, and Pedro Campos
14.1 Introduction
In a world where technology evolves very fast, consumers have more information to
make decisions. Companies compete in order to supply products and/or services
with the best quality-price tradeoff. One of the main goals of companies is to
obtain the maximum number customers satisfied with the highest possible profit.
For that purpose, businesses are compelled to react to market changes, considering
the economic circumstances they are facing at the given moment. The decisions
taken in a high paced rhythm generate expectations associated with uncertainties for
what the future regards [1]. Companies are adapting at a rapid pace to new trends
and more attention is being paid to the intersection between strategic marketing and
Artificial Intelligence (AI). [2] presented a review agenda on the evolving role of
artificial intelligence in marketing, with a focus on the acceptance of AI technology
in marketing, the role of data protection and ethics, the role of institutional support
for marketing AI, as well as the revolution of the labor market and marketers’
competencies.
Management usually takes a decision based on knowledge. Knowledge man-
agement is fundamental for decision support and can be understood as a process
of individual and collective conceptual construction [3]. In Management Sciences,
A. Nogueira
University of Porto, FEP, Porto, Portugal
C. Rocha
CPES-INESC TEC, Porto, Portugal
e-mail: conceicao.n.rocha@inesctec.pt
P. Campos (@)
University of Porto, FEP, LIAAD-INESC TEC, Porto, Portugal
e-mail: pcampos@fep.up.pt
© The Author(s), under exclusive license to Springer Nature Switzerland AG 2025 341
P. Campos et al. (eds.), Machine Learning Perspectives of Agent-Based Models,
https://doi.org/10.1007/978-3-031-73354-3_14

342 A.Nogueiraetal.
knowledge is defined with several dimensions or factors. According to [4], knowl-
edge regards to all possible factors such as human, culture, skills competencies,
intuition, organizational culture, reputation and theory; however, in the current
trend of Industry 4.0, knowledge involves large volumes of data and the amount
of decisions to be made is wider. de Bem Machado et al. [3] provide an extensive
structured literature review on knowledge management, making appropriate bridge
with digital transformation, and Industry 4.0, defining these new research streams’
interactions, ties, and interdependencies. It is crucial to have good tools to process
and analyze huge volumes of data, as well as the use of experts to get results and
answers. Having access to these resources, managers will have more reliable infor-
mation and the range of the critical time to think might increase, because the time
spent in the analysis is more efficient and effective [5]. Albeit, independently of the
proficiency of the decision support tools, conferring any decision is intertwined with
a risk analysis with applications in several areas like operational risk management
in finance, supply chain risk assessment and the risk and reliability of com-plex
technological systems [6]. So, decision-makers have always hazards towards the
finite possibilities of the path they in-tend to take.
Companies desire to survive the fierce competitiveness and the constant chal-
lenges, but at the same time, they aim to have a range of profit margins and,
correspond to customer’s expectations and have short lead-times [7]. The supply-
chain business is demanding since it is a network comprised of suppliers, clients,
distributors, competitors and final consumers. Therefore, the success of a single
business will depend on the management capability to maintain and invigorate
the company’s network of business relationships [8]. As the complexity of the
network increases so does the risk of any decision taken. It is therefore imperative
to examine the nature of B2B network disruptions. Recent trade-war between the
largest world’s economies promoted disruption in the macro-environment, but also
provide opportunities to reconfigure some business networks [9, 10].
The market, independently of the business area, is more client-focused, nowa-
days. Since the quality of life has been improving mainly due to the technology
evolution, client’s needs, quality standards and desires have also been changing
throughout the years. Thus, companies are forced to detect signs of change in the
customer behavior, and to allocate new resources to fulfil with the client’s new
demands, and, consequently, to maintain them [11]. According to [12], having the
customer’s loyalty will have a significant impact on its success and profitability.
Loyalty is an important asset in business relationships. A customer will stay in its
organizational network of buyers and suppliers if and only if his needs are fully
satisfied and if he gets more benefits than losses with his relationship with the
company.
In this work we study the resilience of a network in the automotive aftermarket.
It is the secondary market of the automotive industry related with the vehicle
parts in the process of manufacture, distribution, retailing and installation. We aim
at providing new insights about the behaviour of the partners after a network’s
perturbation such as a cessation of company. The network presented is comprised
of several aftermarket companies, some of them belonging to the same business

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 343
group. There are some interchanges between companies throughout time and, at a
certain time, a company of the business group may disappear. According to [13], the
intra-business collaborations are the first step to obtain competitiveness advantages,
otherwise, the competitiveness by integration might be at risk. Therefore, for the
entities, it might be an advantage to work and help within the network so, in the
end, the profit increases.
Networks are complex data. The more complex the data, the greater is the
challenge for businesses to manage, analyse and provide useful and timely insights
[14]. The agent-based model presented in this Chapter puts together the data of
three different partners of the automotive aftermarket and demonstrates what might
happen after a perturbation or the occurrence of an event in the network.
This work is structured into four parts. In Sect.14.2, the literature review presents
the theoretical framework. Literature review is subdivided into four main subjects:
network’s concepts, resilience, supply chain definitions and trustworthiness, and
agent-based models.
Section 14.3 exposes the problem with the details that will be tackling in this
research. In Sect.14.4 we analyse and compare the simulations’ results. These allow
answering the initial questions presented at the beginning of this project.
14.2 Literature Review
A literature review is provided concerning the topics involved in this Section. First,
a slight introduction to Networks and Resilience, is made, as well as the correspond-
ing concepts and measures. Then, the notions of supply chain management and
trustworthiness in a Supply Chain Network are described. At the end we introduce
the very basics of Agent-Based Models.
14.2.1 Networks and Resilience
Graph theory is the study of graphs, which are mathematical structures used
to model pairwise relations between objects. It is a common scientific study
through fields like mathematics, physics, computer science, sociology, psychology,
anthropology, amongst others. It is stated back in 1736 with a publication of
Leonhard Euler in the Academy of Science of St. Petersburg [15]. A network may
be seen as a graph comprised of nodes and edges, where the nodes are the entities
and the edges are the links between the individuals. The representation typically
used is G = (V(G),E(G)), where G is a set of nodes/vertex V(G) and a set of
. .
edgesE(G). One of the characteristics of a graph is the order which is the number
.
of nodes in G, |G|; the number of edges is represented as ||G||and it represents the
. .
size of the network [16]. In weighted networks, each edge or link may have a weight

344 A.Nogueiraetal.
or a number associated which can represent distances, costs or other parameters to
characterize the interaction between two nodes.
A common example of a network is a social network where people are connected
and interact with each other by sharing photos, activities and messages. Moreover,
a social network is built from relational data and it is defined with entities, that
might be organizations, companies, people or groups who have interactions, and
relationships between them [56]. The advantage of the members being connected is
that they profit by being linked to others who have some interesting to do a trade-off,
independently of their geographical position or final goals [17].
Networks are not just static, they can also be dynamic, meaning that they
vary over time (Nodes and/or edges may come and go). Dynamic networks are
becomingmoreandmorestudiedduetoitsimportanceandimpactonrealsituations,
such as Web, Local-area networks, Social Networks, Transportation networks,
and Interorganizational Networks. The basic notation for dynamic networks vary
depending on the data and its application [18–20]. A path in a temporal or dynamic
network is time-respecting or time-admitting path. A time-respecting path is a
sequence of entities that connect the starting and ending node with each contact
in the path coming after the one before in the time [57].
The dynamic connectedness can be related to an overall period or a specific
time to each node. Thus, a network is considered temporally strongly connected
if every node is reachable within the time period, and is just temporally connected
if there is, at least, one node that is reachable from others within the time frame.
Moreover, the temporal contagion connected is defined if exists some nodes such
that the remaining nodes are reachable within the time period [21].
In the study of dynamic networks, one important aspect refers to the capacity to
maintain the structure in terms of nodes and links. Many systems change abruptly
from a desired state to an undesired state when forced across a“tipping point”. The
capacity to avoid such changes or to recover quickly from such a non-resilient state
is a indicator of a system’s resilience. System resilience is a quality that enables a
system to adjust its activities to retain its basic functionality when errors and failures
occur [22]. In other words, resilience is used to indicate the ability of a system
or entity to return to the normal condition/ state after an occurrence of an event
that perturbates the initial state [23]. There are four main areas where resilience is
most used and has a great impact: organizational, social, economic and engineering.
The concept of resilience changes slightly from field to field. According to [24],
resilience is a “measure of a system’s ability to absorb continuous and unpredictable
change and still maintain its vital functions”. Haimes [25] states that resilience
is “the ability of the system to withstand a major disruption within acceptable
degradation parameters and to recover with a suitable time and reasonable costs and
risks”. Li and Zobel [26] investigate supply chain network resilience in the presence
of a risk propagation, i.e. the phenomenon that disruptions at a few firms in a supply
chain network can spread to their neighboring firm.
The study of resilience in network problems is taken by the analytical results,
which unveil the characteristics of the network that enhance or reduce resilience.
Thus, it allows the development of methods and/or solutions that prevent the col-

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 345
lapse of ecological, physical, economic and biological systems, and it demonstrates
the internal failures a system might have. Following [27], system’s dynamics may
be seen as in Eq.14.1
dx
f(β,x)= (14.1)
.
dt
Where f(β,x) is the system’s dynamics, and β represents the fluctuation of envi-
. .
ronmental conditions. Thus, the system is considered to be stable when Eqs.14.2
and 14.3 are guaranteed.
f(β,x)=0 (14.2)
.
|
|
∂f|
. | <0 (14.3)
∂x
x=x0
Where Eq.14.2 provides the system’s steady-state and Eq.14.3 assurances its
linear stability. Moreover, the solution of these two equations offers the resilience
function (x(β)), which represents the possible states of the system. At the same
.
point β , the resilience may feature a bifurcation indicating the system lost its
c.
resilience by facing a sudden transition to an undesirable, different point in Eq.14.1.
After presenting the traditional mathematics of resilience, Gao et al. [27] devel-
oped a general network-based theoretical framework that permits the exploration
and prediction of the multiple roots and dimensions of resilience. Therefore, they
considered a system of N nodes whose activities follow the coupled linear equations
in14.4.
EN
dx
i =F(x )+ A G(x ,x ) (14.4)
. i ij i j
dt
j=1
On one hand, the first term represents the self-dynamics of each component, and,
on the other hand, the second term describes the interactions between component
i and its interacting partners. The dynamical laws are represented in functions
F(x ) and G(x ,x ), while A demonstrates the interactions between the nodes.
i . i j . ij.
Therefore, an appropriated selection ofF(x )andG(x ,x )is used to model several
i . i j .
systems, which are known for their resilience.
As the resilience of a network is an important property, it is noteworthy to intro-
duce a set of principles for designing resilient networks as well as some strategies.
According to [28], the resilience principles are divided into four categories as they
represent in Fig.14.1.
The first category, “Prerequisites” has five main principles to build a resilient
network, which are:
1. Service requirements: They are needed to understand the level of resilience a
system should provide.

346 A.Nogueiraetal.
Fig. 14.1 Resilience principles. Adapted from [28]
2. Normal behaviour: A combination of design and engineering specification
to learn the network’s parameters. It is crucial to understand the network’s
requirements [60].
3. Threat and challenges models: They permit to understand and detect possible
adverse conditions.
4. Metrics: They quantify the service requirements and operational state.
5. Heterogeneity in the mechanism, trust, and policy: Considering the real-
world, it is essential to understand that it is not possible to have a set of global
homogeneous networks. There is not a single technology that is adequate for all
scenarios.
The second major category is the “Design Trade-offs”, which has three compo-
nents to it:
1. Resource trade-offs: It determines the placement of resources, which must be
balanced, to optimize the resilience and cost.
2. Complexity: The interactions of the systems at multiple levels increase the
complexity of the network, which is related to the scalability.
3. State Management: The choice of state management impacts the resilience.
Then, the resilience mechanisms themselves demand state and should achieve
its goals in increasing overall resilience.
The third category is the “Enablers” which guide the network’s design and
engineering. It is comprised of the following seven principles:
1. Self-protection and security: These two properties allow the systems to protect
itself from external and internal challenges.
2. Connectivity and association: The communication between nodes is important
even in unstable paths. This is possible by applying Disruption-tolerant network-
ing (DTN) techniques which are meant to provide connectivity in heterogeneous
networks that have communications problems due to the incessant disruptions or
delays [29].

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 347
3. Redundancy: It refers to the repetition of entities in the network which usually
provides fault tolerance. One important factor about redundancy is that it does
not inherently prevent redundant components from sharing the same outcomes.
4. Diversity: It is similar to redundancy, however, its goal is to avoid the sharing of
the same outcomes. Diversity in space, time and mechanism increases resilience
against perturbations by providing alternatives which prevent degradation from
the normal operations.
5. Multilevel resilience: It is defined according to the protocol layer, protocol lane,
and hierarchical network organization. The first dimension, resilience provides,
at each layer, a foundation for the next layer; the protocol plane is related to
the data, control and management; the last dimension, the hierarchical network
organization, considers the network architecture from fault-tolerant components
to the global internetwork, including the attached end systems.
6. Context-awareness: It is helpful for resilient nodes to monitor the link’s states,
operational states of the networks components, and the channel conditions, and
to detect adverse events or occurrences.
7. Translucency: It controls the visibility between levels in the networks, i.e., it
controls the boundaries between layers so that the states are explicitly visible
across all the levels.
The last category is the “Behaviour needed for resilience”, which covers the
behaviours and properties a system should process, and is comprised of three
principles:
1. Self-organizing and automatic behaviour: For network resilience, it is funda-
mental for the network to be highly reactive, in an automatic way. Moreover,
a resilience network should start and operate by itself with the minimal human
configuration.
2. Adaptability: A node, in a resilient network, should be capable to detect, reme-
diate, and recover from perturbations. The adaptation of the entities behaviour
based on dynamic conditions is essential for a resilient network to overcome
challenges and return to a stable state.
3. Evolvability: It is helpful to improve future behaviours, and, therefore, to
respond to perturbations in a more efficient and effective way.
Several measures may be used to quantify the ability of a network to recover after
suffering a perturbation. One measure to quantify resilience is the Spearman rank
correlation coefficient [61] that allows studying the association between two ordinal
variables. So, we have n pairs of observations from two quantitative variables, which
it is necessary to rank the values from 1 to n for each variable. In cases of ties, we
decided to scored to those observations the same rank defined by the arithmetic
mean of the ranks that would be assigned to those observations if they were not
equal.

348 A.Nogueiraetal.
The Spearman rank correlation coefficient is given by:
E
6 n D2
R =1− i=1 i (14.5)
. S n(n2−1)
WhereD =R −S ,I =1, ...,n, are the differences between the pair of ranks for
i i i. .
the n individuals. And it verifies thecondition −1≤R ≤1.
S .
One example of the application of this method is described in [62], where the
author uses it to calculate the core resilience to quantify the degree to which a
network’s core structure changes when nodes or edges are deleted uniformly at
random. The(r,p)-core resilience of a network G is defined as the rank correlation
.
between the top r% nodes (as ranked by core number) in the original network to
that of the network after p% of the edges or nodes have been removed uniformly at
random.
14.2.2 Supply Chain Management
A Supply Chain Network (SCN) is a network comprised of different entities that
must make decisions individually and collectively, in different areas, to work effi-
ciently [30], with a rather high level of interdependence and connectivity between
multiple organizations. One accurately definition of the supply chain is “A network
of connected and interdependent organisations mutually and cooperatively working
together to control, manage and improve the flow of materials and information from
suppliers to end-users” [31]. The concept of Supply Chain Management (SCM)
appeared to help the management of relationships in order to achieve a more
profitable outcome for all parties in the chain.
Moreover, SCM is one of the most concerning subjects for managers since a
supply chain demands a continuous improvement process of efficiency due to the
increasing complexity of the network.
The optimization of a maximum profit in normal circumstances isone of the great
goals for management [32]. Also, the increased volume of data, due to the increased
complexity of the network, forces the decision-makers to treat the data and turn it
into quantitative metrics so that it is possible to measure and monetize all the data
which is produced and treated [33].
The crises caused by COVID 19 and more recently by armed conflicts and
rapidly rising inflation have worried the markets and caused changes in supply chain
networks. Spieske et al. [34] explore supplies during disruptions such as COVID-19,
and investigate how it is possible to increase supply chain resilience in healthcare
by presenting empirical evidence from a multi-tier case study across nine European
medical supplies manufacturers and hospital groups.
But already before, other crises have had major impacts on the economy. For
example, the financial crises in 2008 caused a sequence of failures in areas like
the automotive industries manufacturing and, consequently, it triggered a major

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 349
recession. This is evidence of the failed approaches to supply chain management
[35]. The inefficiency of risk management in companies is highly correlated with
having the same processes throughout the years like risk identification and statistical
analysis. However, most of the risk is unknown and most of the times unpredictable
[36]. Herein, the resilience in networks has become a subject of more interest and
importance for the last years. According to Melnyk et al. [37], the resilience in
the networks is the core of supply chain management. The development of several
models is essential to analyse the resilience and to better understand the network.
[38] estimate the costs of resilience and disruptions in supply chain network using
quantitative models.
Some examples of the types of models used are quantitative, analytical, mathe-
matical programming and simulations. Simulations methods, like system dynamics
(SD) methods, examine the networks and support long-term and strategic deci-
sions. Nevertheless, they are very underrepresented [39]. The main advantage of
simulating the dynamics of a complex network (by simulating the evolution of the
network throughout time) is the possibility of demonstrating some unpredictable
effects like the bullwhip effect [40], which is the phenomena of demand variability
along a supply chain, from the retailers to distributors, manufacturer’s and the
manufacturer’s suppliers. Other effects are the loss of an important supplier and,
consequently, a client. Simulating the resilience of a network might support the
managers to understand how to keep or remove a specific pattern in the network
like, for example, a process in the interaction with a client or supplier.
Asupply chain network due toitscomplexity demands strong management sothe
different entities communicate and do not miss any important process or deadline.
There are several strategies and variables to consider in this type of networks. Some
are:
Pricing strategies which vary from company to company as well as the Key
Performance Indicators (KPI’s). The profit is one of the main measures, however,
at a supply chain management, it does not demonstrate the full rentability of the
parts, in the automotive industry. For a supply chain network to survive, all the
entities should be collaborative. Thus, in order to improve the performance of the
entire network, it is encouraged to use the policies of discounts schedules and profit-
sharing [41]. The advantage for the suppliers is the decreased fix costs related to the
inventory, so by having the clients ordering larger volumes, it allows them to have
better control with the stock. Whereas for the buyers, the price per unit and the
ordering costs decrease.
Thus, one of the discounts applied is called the Rappel, which is a percentage
agreed between the suppliers and companies where the companies must do a k
volume of orders in a year to get a monetary return corresponding to the percentage
k of the volume of the orders. This discount permits to calculate a second margin
which indicates the rentability. One advantage is that the selling price for the
customersmightreduce.

350 A.Nogueiraetal.
14.2.3 Trustworthiness in a Supply Chain Network
The environment in an SCM is highly complex and the network is shaped by
global intense competition [42]. Thus, in a logistics sector survey, in Brazil, [43]
determined that the ability of an exchange partner is important to both entities, the
supplier and customers, in their perceptions of trustworthiness. Moreover, for each
part the important characteristic of their relationship vary: the customer integrity is
important to suppliers, while to customers the supplier’s benevolence has a great
counterpart. So, trust is comprised of order accuracy, quality and cost by both
suppliers and customers and to suppliers’ on-time delivery capacity expectations.
Trust involves both the truster and the trustee. Thus, much of the prior supply
chain trust research is leaning to bias because it uses a single source to assess a
dyadic construct, implicitly assuming both entities in a relationship would assume
the level of trust in the same way [44].
There are theoretical foundations in a supply chain which are provided by
two theories: the Social Exchange Theory (SET) and Transaction Cost Economics
Theory (TCE). The first describes business relationships as inherently connected to
personal relationships, which is important in an SCM since the negotiations and the
connections are established between individuals who represent the firms [45]. As the
frequency of the interactions and its duration increase between the supply chain and
its connections, their bonds lead to the development of steady relationships which
generate trust and, consequently, it creates behavioural expectations for both entities
such has to have common goals [46]. Therefore, SET is a theory that focuses on
the positive outcomes of a relationship commitment between two business partners,
which is the development of trust. The TCE aims to avoid the negative consequences
of a non-trusting relationship. The possible costs associated with the interaction, like
for example, the cost of a transaction asset originates a transaction cost imbalance
which will be opportunistically exploited [47]. Thus, terminating the relationship
conducts to a reduction of opportunistic behaviour for the trustor.
Trust and benevolence are concepts associated with relationships, however, there
are other parameters which influence the behaviour of clients, suppliers, and the
trust between them. In the literature, trust has different meanings depending on
the field of expertise. Alves et al. [48] studied what concepts are associated with
trustworthiness in a business to business (B2B) relationship. Through an application
of an Exploratory and Confirmatory Factor Analysis in a survey made to Portuguese
companies, they concluded what determinants were significant for customers and
firms in a trusting relationship. Moreover, the concept model of trust was comprised
of the following variables:
1. Past and Experience: The trust in a supplier is related not only to the present
behaviour but also with its actions and performances in the past, its portfolio
and afore experience.
2. International Presence: A company’s origin country is another considered
factor for the trustworthiness of a supplier due to its credibility. As well as
the presence in several countries positively influences the trust of a supplier.

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 351
3. Brand: The preference for a recognizable brand is considered a risk reduction
since it provides security and quality for the customer’s options.
4. Business Network Dimension: The size of a business network is related to the
number of opportunities for the business. The larger a business network is, the
more probable it is for companies to increase their business opportunities.
5. Buyer-Supplier Relationship Duration: The experience and the duration of
supplier-buyer is of great importance in a business relationship since satisfied
buyers stay with the same suppliers.
6. Specialization: The ability to adapt to a client’s needs and investing in
specializing tools to fulfil the customer’s requirements is seen as investments
in the relationship.
7. Product’s Quality: A supplier’s credibility is also measured by the quality of
its products. Since a good quality product demonstrates a greater effort and
investment of the supplier to satisfy its customer’s needs and requirements.
8. Deadlines Fulfillment: The capability to deliver the products on time and in a
higher frequency without any additional costs for the customer translates into
a trusting relationship since the deadlines imposed by the client are always
respected.
9. Affectivity/ Familiarity: A highly frequent interaction as the familiarity
creates trust.
10. Monitoring: Monitoring is taken to verify if the transactions are made accord-
ing to the quality, delivery and performance standards. Thus, it encourages
responsible behaviours.
11. Accreditation: An independent authority assesses the competence of an
organization.
12. Legal Bonds: Legitime contracts reduce opportunistic transactions and pro-
mote trust. The management of economic activity is an important step to build
trust in a B2B relationship.
13. Feedback: Theinformationabout pasttransactionsofanenterprisediscourages
the opportunism and states the credibility in the market. Moreover, it provides
an indicator of the good reputation of the supplier.
14. Cooperative Norms: The values, mission, norms and standards of a company
reduces the opportunism, facilitates the cooperation, reduces cost and promotes
innovation in the methodologies.
15. Organizational Strength and Economical/ Financial Capacity: The finan-
cial capacity of a supplier as well as the personnel expertise, competences and
the market share position indicates that other businesses trust in the supplier
enough to make deals and have a business relationship.
After the possible variables, the authors conclude that the most important
for the trustworthiness in a B2B relationship are: feedback, deadlines fulfilment,
cooperative norms, accreditation, buyer-supplier relationship duration, past and
experience, and product’s quality. These conclusions were based on the responses
of the survey and its extensive analysis.

352 A.Nogueiraetal.
14.2.4 Agent-Based Models
Agent-based Models are commonly used to study and analyse complex systems.
The systems are characterized by the diversity of components that interact with each
other. Agent-based models attempt to replicate the behaviour of the actors in these
systems to better understand them and potentially increase their performance [49].
Citing [63] patterns, structures, and behaviours that were not explicitly programmed
into the models, but arise through the agent interaction” is a feature of the agent-
based models.
Agent-based models are characterized by an environment, agents and their
interactions. Some areas of application for these models are finance, urban planning,
segregation, security, and ecology [49]. The same authors state that these type of
models have emergent properties which are based on desirability or complexity.
The desirability is divided into positive emergent properties—desired outcomes of
interactions of agents—and negative emergent properties—not desired outcomes of
interactions between agents.
Sensitivity analysis techniques allow gaining insights about the behaviour of the
model and the corresponding emergent properties [50]. These techniques analyse
the relationship between the inputs and outputs of the model but do not reveal
the inner structure of the agent-based models. Some machine learning algorithms
have been applied to these models in order to find patterns between inputs and
outputs and to generate meta-models to predict the outcomes of a model. Despite the
demonstration of success in some cases, it is still difficult to analyse the emergent
behaviour
Some authors explore resilience in Supply Chain Networks using Agent-Based
Models: for example, Zhao et al. [51] construct and analyze a real-world supply
chain network among 2971 firms spanning 90 industry sectors and develop an
agent-based simulation to show how the model of firms’ adaptive behaviors can
leverage competition relationships within a supply chain network. The goal is to
model how disruptions propagate in the supply chain network through cascading
failures. Zhao et al. [51] try to understand if a firm’s adaptive behaviors can reduce
the impact of disruptions in supply chain networks. Lohmer et al. [52] investigated
resilience strategies and ripple effect in blockchain-coordinated supply chains using
a simulation Agent-Based Model. Their study indicates an increase in resilience if
the underlying collaboration is based on time-efficient processes.
14.3 Problem Definition
As previously mentioned, the relationships within a business network and the
respective outcomes, dictate the success or failure of a company [53]. To better
understand the concept of network, we will define it as a graph. A network is a graph
composed of nodes (vertices), which in our work corresponds to the companies

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 353
involved, and edges (links), which are the interactions between the companies.
The network to be studied in this work is defined in the scope of the automotive
industry aftermarket. This field of expertise consists of the selling of spare parts
for any vehicles with the advantage of being cheaper than the ones from the
Original Equipment Manufacturers (OEM). The latter are the original producers
of a vehicle’s components, hence the compatibility and the quality are the highest
since the producer knows exactly the properties (dimensions, characteristics,..) the
vehicle specifically demands a given part. So, OEM’s are specialized suppliers [54].
Whereas the aftermarket parts are produced by others that do not necessarily have
the same quality and compatibility as the ones produced by OEM. Consequently,
the price is more affordable than the OEM’s price.
Thus, the problem proposed here is to study how will the network of supply chain
react if it suffers a perturbation such as a cut off of an important client or supplier.
For that purpose, an agent-based model will be developed in order to achieve some
answers to the following questions: What is the new structure of the network after
suffering a perturbation? What is the resilience of the network? Which entities are
the important ones?
Before explaining the two possible points of views the network has, it is
important to expose the general structure. The network has four different types of
nodes: the suppliers, the aftermarket companies, which might belong to one group
of companies or not, retailers and the final clients or consumers. Each entity has
different characteristics. Moreover, the complex network changes its relationships,
interactions and, therefore, it is necessary to divide the entities into layers [55]. So,
the network has got four layers, as represented in Fig.14.2, the layer A contains all
the suppliers, layer B is composed of the aftermarket companies, whereas layer C
holds all the retailers and the consumers are in layer D.
There are some constraints related to the interactions between nodes. These must
be satisfied with both points of views of the network (logistics and economics),
which are:
1. The suppliers (Layer A) can only exchange goods and services with the
aftermarket companies (Layer B). In a logistic perspective, the suppliers sell the
goods to the companies, and the latter buy the parts to the suppliers.
Fig. 14.2 Layers of the network: Layer A—Suppliers; Layer B—Aftermarket Companies; Layer
C—Retailers; Layer D—Consumers

354 A.Nogueiraetal.
Fig. 14.3 Multi layer network: nodes coloured by the type of entities, which are in each layer
2. The aftermarket companies (Layer B) are connected to the suppliers (Layer A)
andtheretailers(LayerC).Thelinkwiththeformerwasexplainedabove.Further
on, the link with the retailers is characterized by selling off the parts from the
aftermarket companies to the retailers.
3. The retailers buy to the aftermarket companies and sell to the final consumers
(Layer D).
After introducing the exchange of goods within the network, it makes sense to
learn more about the economic point of view. Figure 14.3 shows the network in a
multi-layer perspective. The network has four layers, as it was previously explained,
each one with each type of nodes. The Layer “Suppliers” only contains the entities
identified as suppliers, coloured in a light green; the Layer “Companies” has all the
aftermarket companies, whose nodes are in yellow; the Layer “Retailers” with the
retailers corporates are in a dark green; the last Layer, the “Consumers” has only the
consumers, coloured in a dark pink.
There are some reasons why it is necessary to also study the economic point of
view:
1. The network is supposed to be dynamic, i.e., the network’s structure might
change through time. Therefore, it is expected for the network to suffer some
changes in each time frame by the creation or elimination of links. However,
the decision of forming or removing a link differs, just like in the basics rules
of negotiation. For creating links or keeping the existing ones, both entities
involved must agree, i.e., the decision of creating a link must be unanimous. As
it was mathematically proposed in [58], two different entities are represented by
i and j, and the decision to start/maintain or removing/not create an interaction

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 355
between i and j isrepresentedbys ∈ {0,1}. The nodes will link if and only
i,j .
if s = s = 1. To remove a link, it only matters one individual’s decision.
i,j j,i .
Moreover, one entity might be interested in keeping a link, but if the another is
not, then, the link is removed. This is represented by Eq.14.6. The decision of
creating or not an interaction with another entity will be based, firstly, in a profit
function and, after, in a final decision function. These will be explained further
in Sect.14.5.
\
0,alinkisnotdesiredtobeformed/removed
s =s = (14.6)
. i,j j,i
1,alinkisdesiredtobeformed/maintained
2. There is not any flow or exchange of goods between the layers and nodes. The
information that will be used to decide whether to link or not is mainly about
the characteristics of a node has, which will be explained in the Sect.14.4. These
features are business-related, and that a corporate considers for its partnerships.
3. The constraints about the possible interactions analysed in the logistics view are
also applied in this view.
4. The decision will be upon the profit and some characteristics of each node
as it will be better explained in Sect.14.5. The analysis and the decision
model are based on the monetary value and the qualitative aspects, such as
the trustworthiness, of an entity. So, the direction of the exchanges is not
important, making the network undirected. What really matters is the gain or
loss the link represents for both entities. Each link will have a weight, calculated
with the factors to be explained. A threshold will be necessary to determine
if a link/connection is acceptable or not for the corporates, based on the rules
presented above.
So, the problem proposed is to develop a model capable of studying the evolution
of a network after suffering some perturbations. The behaviour and the structures
will change in each time frame regarding the commercial transactions. For that
purpose, a profit function will be defined for each entity and calculated for each
possible connection. To decide if the profit is enough for an interaction to survive, a
threshold will be defined to determine whether an entity should or not link to another
one. All of this information will permit to study the adaptation of a network after
a perturbation and its breaking point. Thus, it will demonstrate the new network’s
configuration and it will be a helpful tool for managers to make decisions and define
future actions to prevent a specific link rupture or the failure of a company.
14.4 Model
In this section, we introduce the model developed and describe the functions,
assumptions and how the model makes its decisions of linking or not a pair of
nodes. The assumptions are necessary since it is a simulation and some variables,

356 A.Nogueiraetal.
such as costs are unknown for the entire network except for the node which has the
considered cost.
The developed model has some general functions and qualitative variables as
well as some rules and assumptions such as the profit of an entity, which is a node
of the network.
The first aspect that we consider for an entity is the profit obtained by interacting
with others. However, this is not enough for an aftermarket company to decide what
are the good and bad connections and what impact they will have in the near future.
There areother weighted factors which might make adifference inthe final decision.
The hypothesis is that it might be more productive and profitable, in the long term, to
have a connection with a node that has less profit than the one with the maximum.
For this reason, there will be two functions: one is the optimized function of the
profit, and the other is the decision function which will calculate every qualitative
aspect for each node. This methodology will allow comparing the links with some
level of profit with the deciding factors.
14.4.1 The Profit Function
The profit is a simple function where the cost and the selling price are calculated
with the rappel associated, which is a given percentage, defined a priori and
taking into the consideration the volume of sales, for the client. The variable cost
includes all the expenses to produce or have a product like the raw material prices,
labour work, infrastructures, which are fixed costs, and the other remaining that
contribute as an expense of producing/having a part. The general profit function, p,
is represented in Eq.14.7:
p =(Sales−Cost)+Rappel∗Sales (14.7)
.
The sign of the variable Rappel will vary depending on the considering entity
and relationship at the moment of the calculus.
14.4.2 The Decision Function
The decision function isessential to differentiate theimportance of anode regardless
of the profit it may generate. This function will be separated from the profit function
due to the different units of measurement. Thus, as it was stated in the literature
review, there are some trustworthiness factors which have some weights for decision
making. The ones selected for the present project, according to [48] and the values
adapted for this project are:

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 357
• The Brand Position in the market (B), i.e., the weight of the quality for which
the brand is well-known. There are three levels: Best Cost, which has the smallest
weight since it has the worst quality even though the prices are low; Smart Buy,
which has the medium quality in the eyes of the clients; Premium, which is the
best quality and equips original equipment.
• The Segmentation of the clients (F) that indicates the fidelity for the company.
A customer that buys more and trusts the business must have the best rewards.
Thus, these are the best clients to keep and it is divided into 5 categories: E—
Very low; D—Low; C—Medium; B—Good; A—Very Good. So, the higher the
segmentation, the higher the weight of the link will be.
• The Process’s Flow (P) is important since dealing with different companies and
having a lot of processes involved, efficiency and efficacy is high demand. Hence,
the classification will be like the II point, however, will only have four categories:
D—Bad; C—Medium; B—Good; A—Very Good.
• The Past Experience (H) represents the historical transactions and interactions
two entities have. This attribute will have the following classes: C—Recent (0–2
years); B—Medium (2–5 years); A—Old (5+ years).
• The Product’s Quality (PQ) is an important feature as it was previously stated.
Thus, the classification of this parameter will be into three possible classes: A—
The Best; B—Medium; C—Poor Quality.
• The Deadlines Fulfilments (DF) indicate if an entity satisfies the delivery’s
deadline or not. This does not only allow to deliver the product as it was agreed
with the customer but also demonstrates the credibility of the same entity. So,
the deadline fulfilment has three categories too: A—On time; B—A bit late (1–2
days after); C—Overdue (2+ days).
• The Price-Quality Quotient (PPQ) is a parameter that evaluates the balance a
product and brand have. Therefore, this variable is comprised of three classes: A-
Good quotient (the price is fair for the product); B—Medium (the product might
be a little expensive for its quality and functionality); C—Bad (the price is too
high for the product).
• The variable Product Range (PR) where it evaluates the diversity and extension
of products. Thus, the possibilities to score this attribute are the following: A—
Great offer of products; B—Medium (The range of products is sufficient to
satisfy the necessary meanings); C—Lack of products.
• The last variable is the Network’s Size (NS) takes into consideration the size
of the consumer’s network a company has. The higher the connections, better
will be the classification since there are more chances to connect to an important
entity. This is scored as A—Big; B—Medium; C—Small.
Although the variables explained above are all qualitative, the corresponding
classes will be filled with percentages, i.e., each possible classification will contain
a percentage associated with so that the profit function and decision function are in
units possible to measure quantitatively. Accordingly, the correspondence between
the classes and values is presented Table 14.1.

| 358 | A.Nogueiraetal. |     |
| --- | --------------- | --- |
Table 14.1  Correspondence of classes and percentages of the attributes
| Variables                     | Classes            | Percentage  |
| ----------------------------- | ------------------ | ----------- |
| I. Brand (B)                  | Premium            | 100%        |
|                               | Smart Buy          | 60%         |
|                               | Best Cost          | 30%         |
| II. Segmentation (F)          | A—Very Good        | 100%        |
|                               | B—Good             | 80%         |
|                               | C—Medium           | 60%         |
|                               | D—Bad              | 40%         |
|                               | E—Very Bad         | 20%         |
| III. Process’s Flow (P)       | A—Very Good        | 100%        |
|                               | B—Good             | 75%         |
|                               | C—Medium           | 50%         |
|                               | D—Bad              | 25%         |
| IV. Past Experience (H)       | A—Old              | 100%        |
|                               | B—Medium           | 60%         |
|                               | C—Recent           | 30%         |
| V. Product’s Quality (PQ)     | A—The Best         | 100%        |
|                               | B—Medium           | 60%         |
|                               | C—Poor Quality     | 30%         |
| VI. Deadline Fulfillment (DF) | A—On Time          | 100%        |
|                               | B—A bit late       | 60%         |
|                               | C—Overdue          | 30%         |
| VII. Price-Quality (PPQ)      | A—Good             | 100%        |
|                               | B—Medium           | 60%         |
|                               | C—Bad              | 30%         |
| VIII. Product Range (PR)      | A –Great Offer     | 100%        |
|                               | B—Medium           | 60%         |
|                               | C—Lack of products | 30%         |
| IX. Network Size (NS)         | A—Big              | 100%        |
|                               | B—Medium           | 60%         |
|                               | C—Small            | 30%         |
14.4.3  Assumptions
This section is essential to define the model since the present project is a simulation
and there are some variables with unknown values. So, the assumptions surpass the
gap  of  data,  and  it  allows  the  model  to  keep  running  the  simulation  and  make  the
decisions of linking or not.
As  previously  stated  the  model  has  some  assumptions  due  to  the  missing
information important for the calculus of the profit function. The production costs of
a supplier as well as the price a retailer pays to each company are unknown. In order
to  overcome  these  obstacles,  the  costs  and  the  price  sales  of  the  respective  nodes

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 359
will be calculated considering a random function between some range of margins
(a minimum and maximum values) which are considered the usual in this type of
market. For example, the suppliers are the entities which take the biggest margin
for themselves since they are the manufacturers. The range considered, based on the
real-life case and also considered in [59], for the random function is set up between
25% and 35%.
Another assumption is the thresholds considered (either the qualitative—the
trustworthiness variables—or the quantitative—the costs and price sales variables—
ones). For both types of variables, the threshold is calculated at the beginning of
each time-frame as the median values of the variables. In the qualitative variable,
the threshold is calculated through the median of the considered percentages (after
transforming the qualitative values into quantitative as previously explained in
Table 14.1) for each node. As for the quantitative ones, we consider the median
values of the profit.
The entity “Supplier” has unique characteristic others do not have. For suppliers,
there is a relation of similarity/equivalence, i.e., by removing a node of this type,
the model will search a similar replacement. By similarity we mean to consider the
same range of products: for example, two suppliers sell clutches kits and, so, they
are equivalent.
Since there is no knowledge about the volume of sales of the nodes that are
not connected, it is important to define a logic so the model is able to calculate
the profit a node would have when linking to a new one. Therefore, in the case of
the suppliers, due to having of the equivalence the volume of sales of the removed
node is transferred to the equivalent suppliers. However, for the rest type of nodes—
companies and retailers—the attribution of sales is by the median of sales the node
t as for the other types of nodes. For example, company A is calculating the profit it
would get if it was connected to the retailer D, so it would calculate the median of
sales of the remaining retailers that it is linked with.
Two other assumptions of the model are related to the time when a node dies
and the time when the model stops. For the former, we assume that if after two
consecutive iterations the node is not linked to any other within the network, then
the node disappears. For the latter, if at a given moment, the network has less than
three retailers, which are the final consumers, then the program will stop in the next
iteration. This assumption is necessary because if there are not enough clients to sell
parts then the whole system must stop operating.
The program allows the network to connect with nodes that are not linked to any
other.
The values used for the sales volume and rappel in each database are inspired in
real cases as in the automotive industry [59].

| 360     |      |                                         |     |     |     | A.Nogueiraetal. |
| ------- | ---- | --------------------------------------- | --- | --- | --- | --------------- |
| 14.4.4  | The  | Relationships and Respective Functions  |     |     |     |                 |
Each  type  of  node  (supplier,  an  aftermarket  company,  retailer,  consumer)  has  its
own  characteristics,  and,  therefore,  the  functions  to  determine  whether  two  nodes
should  or  not  have  a  connection  differ.  Thus,  each  category  of  entities  will  have
different  functions  according  to  the  type  of  a  possible  link.  To  decide  whether  or
not  two  nodes  should  link  (function  L)  there  are  some  rules  applied  to  every  kind
of  relationship.  Also,  the  nomenclature  is  similar  since  the  function  profit  will  be
represented by p 1.  and p 2.  where 1 is for some types of node and 2 is for other type
considered in the relationship, the decision function will be presented as f and f ,
1. 2.
and  the  thresholds  for  the  quantitative  and  qualitative  variables  are  represented  as
α 1.  and  α 2. ,  and  β 1.  and  β 2. ,  respectively.  The  rules  for  the  creation  (formation)  or
deletion (erosion) of the links in the network are the following:
⇒L=0,alinkiserasedornotformed
|     |          | Ifp <α  |      |                               |                               |          |
| --- | -------- | ------- | ---- | ----------------------------- | ----------------------------- | -------- |
|     |          | .  1    | 1    |                               |                               |          |
|     |          | ≥α      |      | ⇒L=0,alinkiserasedornotformed |                               |          |
|     | .  Ifp 1 | 1 andf  | 1 <α | 2                             |                               |          |
| Ifp | ≥α       | andf ≥α | andp | <β                            | ⇒L=0,alinkiserasedornotformed |          |
| .   | 1 1      | 1       | 2    | 2                             | 1                             |          |
|     | Ifp      | ≥α      | andf | ≥α andp                       | ≥β andf                       | <β ⇒L=0, |
|     | .        | 1 1     | 1    | 2                             | 2 1 2                         | 2        |
alinkiserasedornotformed
|     |        | ≥α  |        | ≥α     | ≥β         | ≥<β ⇒L=1, |
| --- | ------ | --- | ------ | ------ | ---------- | --------- |
|     | .  Ifp | 1 1 | andf 1 | 2 andp | 2 1 andf 2 | 2         |
alinkisformedormaintained
So,  if  the  profit  function  is  above  the  threshold  then  the  system  will  calculate
the decision function. However, if the profit function is below the threshold defined
then a link will not be formed or will be eliminated since one entity does not want
to  establish  a  connection  due  to  the  achieved  profit  being  under  the  defined  goals.
Thus, a connection will only be formed or maintained if and only if both nodes have
their profit and decision functions above the respective thresholds.
Initializing  with  the  relationship  supplier  and  aftermarket  company:  the  profit
function  is  comprised  of  the  quantitative  variables,  to  calculate  the  profit,  and  the
decision  function  considers  the  qualitative  variables,  after  being  transformed  into
percentages as it is in Table 14.1. As for the profit function since the only variable
that might be different is the Rappel due to the signal then it will only indicate the
sign of this variable.
For  the  supplier  the  Rappel  is  negative  and  the  qualitative  function  is  the
following:
|     |     |     |     | f =F | +P +H |     |
| --- | --- | --- | --- | ---- | ----- | --- |
|     |     |     |     | . 1  | j j j |     |

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 361
where
F —Represents the segmentation of company j for the supplier;
j.
P —Represents the process’s flow,of company j;
j.
H —Represents the past experience with company j.
j.
For the companies the Rappel is positive and the decision function is presented
as:
f =B +P +H +PQ +DF
. 2 j j j j J
where:
B —Represents the brand position of supplier j,in the market;
j.
P —Represents the process’s flow of supplier j;
j.
H —Represents the past experience with supplier j;
j.
PQ —Represents the product’s quality of supplier j;
j.
DF —Represents the deadline fulfillment of the supplier j.
J.
The second possible relationship is between an aftermarket company and a
retailer. In this case, the Rappel for the aftermarket company is negative whereas the
retailer is positive. The decision function of the aftermarket company is as below:
f =F +P +H +SN
. 3 j j j j
where:
F —Represents the segmentation of retailer j for the aftermarket company;
j.
P —Represents the process’s flow of retailer j;
j.
H —Represents the past experience with retailer j;
j.
SN —Represents the networks size of retailer j.
j.
For the retailer, the decision function is:
f =P +H +PPQ
. 4 j j j
where:
P —Represents the process’s flow of company j;
j.
H —Represents the past experience with company j;
j.
PPQ —Represents the product’ s relation price-quality of retailer j.
j.
The last relationship is between aftermarket companies and there is not the
variable Rappel involved. Since the nature of the nodes is the same, the decision
function is as follows:
f =PPQ +H +PR
. 5 j j j

362 A.Nogueiraetal.
where:
PPQ —Represents the product’s relation price-quality of company j;
j.
H —Represents the past experience with company j;
j.
PR —Represents the product range that company j has to offer.
j.
14.5 Analysis and Comparisons of Results
To study the resilience of the multilayer network by using the developed model, it
was necessary to do a considerable amount of simulations by varying the parameters
of the margins referred at the assumptions and using three different databases. The
goals for these are: to analyse if different parameters have any implication on the
network’s evolution after suffering a perturbation and to study if the size or the
number of certain types of nodes can change the evolution and behaviour of the
network.
The resilience is calculated, in this project, by applying the ranked correlation
between time-frames where the network has a different display.
14.5.1 Composition and Characteristics of Databases
In this subsection is explained how the different database (hereafter named data sets
or databases) for the simulations, and the characteristics of each node.
The number of suppliers, companies and retailers considered in each database is
represented in Table 14.2. Three different data sets have been considered: Database
1 is the smallest one, database 2 has more retailers than the previous one, and
database 3 has more companies than database 2. The main idea is to analyse
the behaviour of the network when adding more clients and then adding more
companies, increasing the competitiveness and the interactions between the same
type of node.
The nodes removed were several since we intend to analyse if removing nodes,
that are either considered important (or not) due to the small amount of sales or the
number of edges, has a different impact on the network’s evolution and resilience.
Table 14.2 Configurations of each database applied
Database number Number of suppliers Number of companies Number of retailers
Database 1 9 3 7
Database 2 9 3 13
Database 3 9 5 13

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 363
| Table 14.3  Characteristics of the nodes in Database 1  |     |     |     |
| ------------------------------------------------------- | --- | --- | --- |
The volume of sales (e)
| Node    | Type of node |           | Number of links  |
| ------- | ------------ | --------- | ---------------- |
| Node 1  | Supplier 1   | 1,250,000 | 2                |
| Node 2  | Supplier 2   | 100,000   | 1                |
| Node 3  | Supplier 3   | 1,025,500 | 3                |
| Node 4  | Supplier 4   | 0         | 0                |
| Node 5  | Supplier 5   | 120,000   | 1                |
| Node 6  | Supplier 6   | 183,000   | 2                |
| Node 7  | Supplier 7   | 0         | 0                |
| Node 8  | Supplier 8   | 357,250   | 2                |
| Node 9  | Supplier 9   | 91,000    | 1                |
| Node 10 | Company 1    | 163,750   | 8                |
| Node 11 | Company 2    | 171,250   | 10               |
| Node 12 | Company 3    | 1,056,450 | 11               |
| Node 13 | Retailer 1   | 227,500   | 2                |
| Node 14 | Retailer 2   | 199,550   | 2                |
| Node 15 | Retailer 3   | 323,050   | 2                |
| Node 16 | Retailer 4   | 195,975   | 2                |
| Node 17 | Retailer 5   | 187,850   | 2                |
| Node 18 | Retailer 6   | 239,850   | 2                |
| Node 19 | Retailer 7   | 357,500   | 1                |
The volume of sales is calculated with a random function which applies margins
with different ranges as it was mentioned in Sect.14.4.3. The range of these volumes
of sales is inspired in real-life cases.
For each database, the removed nodes are the same, so it is possible to compare
the  results.  The  selection  of  the  removed  nodes  is  based  on  its  characteristics  and
how it might possibly influence the behaviour of the network. These are represented
in  Table  14.3  and  the  selection  of  the  nodes  to  remove  is  based  on  the  values  of
Database  1.  For  the  suppliers,  node  1  has  the  greatest  volume  of  sales,  node  3  is
connected to every company, and node 9 has the smallest volume of sales. For the
companies, node 10 has the smallest volume of sales and is the company with less
connected retailers. Node 11 is linked to the other two companies and it is the second
node  of  this  type  with  the  greatest  volume  of  sales.  As  for  the  companies,  node
13  has  the  fourth  greatest  volume  of  sales  (from  buying  to  companies)  whereas
node  19  is  the  one  with  the  maximum  volume  of  sales  and  it  is  only  connected  to
one  company.  Node  16  is  the  penultimate  of  retailers  referring  to  the  volume  of
sales  they  buy  to  companies.  The  characteristics  of  the  new  nodes  in  database  2
are  described  in  Table  14.4.  These  nodes  are  only  of  the  type  retailers.  The  main
differences between the databases are the addition of the new nodes which will be
demonstrated in the next tables. The volume of sales of the already existing nodes
from Database 1 will be different as well as the number of links. These differences

| 364                                                         |     |     | A.Nogueiraetal. |
| ----------------------------------------------------------- | --- | --- | --------------- |
| Table 14.4  Characteristics of the new nodes in Database 2  |     |     |                 |
The volume of sales (e)
| Node                                                        | Type of node |         | Number of links  |
| ----------------------------------------------------------- | ------------ | ------- | ---------------- |
| Node 20                                                     | Retailer 8   | 215,000 | 2                |
| Node 21                                                     | Retailer 9   | 366,754 | 3                |
| Node 22                                                     | Retailer 10  | 50,050  | 1                |
| Node 23                                                     | Retailer 11  | 318,200 | 2                |
| Node 24                                                     | Retailer 12  | 178,500 | 2                |
| Node 25                                                     | Retailer 13  | 246,155 | 2                |
| Table 14.5  Characteristics of the new nodes in Database 3  |              |         |                  |
The volume of sales (e)
| Node    | Type of node |         | Number of links  |
| ------- | ------------ | ------- | ---------------- |
| Node 26 | Company 4    | 835,150 | 12               |
| Node 27 | Company 5    | 867,049 | 20               |
are noticeable on the graphs of the initial states of each database that will be shown
further on.
As for the nodes added in database 3, i.e., the two added companies to increase
the competitiveness, its characteristics are presented in Table 14.5.
14.5.2  Evolution of the Networks
This subsection studies how the networks evolve throughout time, it compares their
behaviours when adifferenttypeof nodeisremoved andexplore theimplementation
of  the  same  actions  in  different  databases.  In  each  database,  the  first  moment  is
the  same  for  every  simulation  independently  of  the  parameter’s  variation  and  the
removed  node  since  the  first  moment  is  the  initial  network.  The  graphs  of  the
networks are represented by giving weight to a node depending on the total profit.
The  different  types  of  nodes  are  in  different  colours  to  make  easier  to  identify  the
nodes’ type.
Database 1
Initializing with the database 1, the initial network with equal weights is represented
in Fig.14.4a. As it is visible, the suppliers are represented in yellow, retailers in blue
and companies in green. There are only two nodes which are not connected but are
available for the nodes in the network to link. The initial state of the network with
the weights, in each node, (the total profit of each node) is represented in Fig.14.4b.
Regardless  of  which  supplier  node  is  removed,  from  among  those  considered
to be eliminated,—the network would die in the 9th iteration since it only has two
retailers. The network evolution, after removing a node, is represented through three
figures, in Fig.14.5a is the second iteration, in (b) the 5th iteration and in (c) is the
last iteration. We can see that, after removing supplier 1, the network will disconnect

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 365
Fig. 14.4 (a) The initial network with equal weights; (b) the initial network with different weights
from supplier 2 and it is also visible the reduction of profit in the companies and
retailers nodes. Also, company 1 decrease a lot of its profit since it had a strong
relationship with supplier 1. In iteration 5, some nodes have died such as suppliers
4, 7 and 2. And the retailers 3, 5 and 6 are unlinked and might disappear if they do
not connect to other nodes in the following interactions. The last iteration, the 9th,
has only got 2 retailers—4 and 7—and the node with the highest profit is supplier
3. Also, company 3 has lost its connection to the network, remaining only two left.
Database 2
Next database has more retailers and the goal is to analyse if there is any difference
in the behaviour of the network after suffering some perturbation. In Fig.14.6 is
represented the initial network of the database 2. In (a) the nodes have the same
weight whereas in (b) they have weights according to their total profit.
The node to remove is company 2, node 11, from the network. As it is possible
to see in Fig .14.7a, when we remove company 2, three retailers break their links
from the network as well as three suppliers. Company 1 and retailer 8 stand out
with the greatest profit. In Fig.14.7b, the network has its last configuration having
only company 1, just what happened in the first database, but it has more 4 retailers
connected than in the previous database.
Database 3
The last database has the same number of retailers as the previous database plus
3 new companies, as it is represented in Fig.14.8. In (a) the network has the same
weight in every node while in (b) the nodes have different weights according to their
profits.
The node to remove and compare is retailer 6, as represented in Fig.14.9a.
Companies 1 and 4, and retailer 7 stand out by having greater profits. In the last

366 A.Nogueiraetal.
Fig. 14.5 Iterations 2 (a), 5 (b) and 9 (c), after removing node 1, in the Database1
iteration, represented in Fig.14.9b, all companies survive and the network has more
retailers linked than the two previous cases studied from this database. Company 2
ends up with more profit than company 4, a situation that differs from the second
iteration. Company 1 maintains the node with the greatest profit.
14.6 Comparisons of the Resilience
Analysing the behaviour of the network throughout time after suffering a perturba-
tion it is important. In addition, we also want to quantify the resilience, through
the ranked correlation and compare it afterwards. The ranks are based on the
profit between two pair of nodes. Analysing Fig.14.10, there are three graphics of

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 367
Fig. 14.6 (a) The initial network with equal weights; (b) the initial network with different weights
Fig. 14.7 Iterations 2 (a) and 35 (b), after removingComp2., in the Database 2
resilience’s evolution when removing a node of the layer Suppliers. Figure 14.10a, b
and c refer to the first, second and database 3, respectively. Relatively to the database
1, which is the smallest, the network, independently of the supplier removed, dies
at iteration 9. So, the network does not recover from the perturbation and there is no
resilience. As for database 2, the network has more iterations and the resilience is
stabilizing after iteration 30. Despite this, the removal of node 9 causes the resilience
to fall into zero, which results in the death of the network. The removal of the other
suppliers put the resilience almost to zero. The last database, number 3, has the
resilience stabilizing after iteration 6 allowing the network to survive through the
rest of time. This database has a better distribution of the number of different types

368 A.Nogueiraetal.
Fig. 14.8 (a) The initial network with equal weights; (b) the initial network with different weights
Fig. 14.9 Iterations 2 (a) and 45 (b), after removingRet6., in the Database 3
of nodes which explains the stabilization in an early time comparing to the other
databases.
Figure 14.11a, b and c show the resilience’s evolution after removing a node in
the layer of the companies in the database 1, 2 and 3, respectively. In Fig.14.11a
removing node 10 causes the network to die near iteration 8, however, removing
node 11 (Company 2), the network survives, in spite of having a real small
correlation throughout time. The variation, after, iteration 5 is very small. As for
the database 2, after iteration 5, the resilience varies poorly and is almost zero.
The behaviour when removing one of the nodes is similar, in terms of resilience.
Figure 14.11c has a different performance, particularly, at the fist iterations,

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 369
Fig. 14.10 Resilience’s evolution after removing a supplier node, in each database. (a) Database
1; (b) Database 2; (c) Database 3
comparing with the other two databases. The resilience decreases and increases,
trying to recover from the perturbation, however, after iteration 16 the network can
not recover and the correlation is close to zero.

370 A.Nogueiraetal.
Fig. 14.11 Resilience’s evolution after removing a company node, in each database. (a) Database
1; (b) Database 2; (c) Database 3
The last type of nodes to analyse the network’s resilience after its removal is the
retailers. Figure 14.12a, b and c shows the resilience’s evolution after removing a
retailer in the database 1, 2 and 3, respectively. In Fig.14.12a we can observe that
at iteration 10 the network eventually dies and the resilience is zero. However, there

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 371
Fig. 14.12 Resilience’s evolution after removing a retailer node, in each database. (a) Database 1;
(b) Database 2; (c) Database 3
is a node that causes the death of the network sooner, which is the node 13. Its
resilience is zero at iteration 6 and, therefore, the network does not recover from
this. As for the database 2, the correlation is almost the same after iteration 5, being
the disappearance of node 13 the case with a higher correlation. The last database

372 A.Nogueiraetal.
Table 14.6  Correlations
Types of node
after removing the selected
nodes in each database  Databases
| Supplier nodes    | Database 1  Database 2  | Database 3  |
| ----------------- | ----------------------- | ----------- |
| Node 1  Iter. 5   | 0.462 0.382             | 0.299       |
| Iter. 10          | 0 0.368                 | 0.416       |
| Node 3  Iter. 5   | 0.386 0.344             | 0.355       |
| Iter. 10          | 0 0.368                 | 0.494       |
| Node 6  Iter. 5   | 0.508 0.379             | 0.341       |
| Iter. 10          | 0 0.378                 | 0.529       |
| Node 9  Iter. 5   | 0.422 0.309             | 0.040       |
| Iter. 10          | 0 0.332                 | 0.377       |
| Company nodes     | Database 1  Database 2  | Database 3  |
| Node 10  Iter. 5  | 0.280 0.282             | 0.255       |
| Iter. 20          | 0 0.282                 | 0.238       |
| Iter. 30          | 0 0.281                 | 0.278       |
| Node 11  Iter. 5  | 0.305 0.272             | 0.286       |
| Iter. 20          | 0.305 0.272             | 0.217       |
| Iter. 30          | – 0.272                 | 0.251       |
| Retailer nodes    | Database 1  Database 2  | Database 3  |
| Node 13  Iter. 5  | 0.565 0.448             | 0.315       |
| Iter. 20          | 0 0.490                 | 0.332       |
| Node 16  Iter. 5  | 0.516 0.405             | 0.252       |
| Iter. 20          | 0 0.391                 | 0.322       |
| Node 18  Iter. 5  | 0.458 0.400             | 0.389       |
| Iter. 20          | 0 0.401                 | 0.516       |
| Node 19  Iter. 5  | 0.574 0.444             | 0.435       |
| Iter. 20          | 0 0.430                 | 0.416       |
has  a  greater  variation  in  the  resilience  than  the  previous  one  since  the  number  of
companies  increase.  The  case  where  node  18  is  removed,  the  correlations  have  a
greater variation, which stabilizes after iteration 29.
When changing the values of the initial parameters to calculate the costs for each
type of entity, the behaviour of the network is the same. The profit varies a little in
the iterations but not enough to modify a decision of linking or not to another node.
In  terms  of  resilience,  this  has  no  impact  since  the  obtained  ranked  correlations
coefficients are, approximately, the same of the initial parameters.
Table 14.6 shows the correlations, in each database, after removing the selected
nodes  referred  above.  In  database  2  and  3,  it  is  possible  to  see  the  variation  of
the  correlations  since  when  removing  node  3  or  9  the  correlation  increases  from
iteration 5 to 10.
Analysing  the  values  of  Database  2,  in  the  company  Nodes,  we  observe  the
constant values as it was observed in Fig.14.10b. In Database 3, at iteration 20, the

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 373
correlations decrease, however, in iteration 30, the correlation increase, surpassing
the value of iteration 20.
Table 14.6 also shows the correlations after removing a retailer in each database
and at iterations 5 and 20. In database 3 there is a lot variation as previously seen,
particularly when removing nodes 16 and 18, the values from iteration 5 to 20
increase considerably. As for database 2, the correlations do not have a greater
variation as the previous case. And as it was analysed in Fig.14.12a, database 1
is considered dead at iteration 20, since it could not recover after the perturbation.
14.7 Conclusions
A multilayer network is a complex system and the prediction of what would happen
if the network suffers some external or internal perturbation such as the death of
a node is important, particularly in a business point of view. This project aimed to
develop a multi-agent model and study the behaviour of a multilayer network when
a node is killed. The model was inspired in a real-life automotive industry case
and the rules and assumptions allow the adaptation for another case of a multilayer
network.
After several simulations, it is noticeable that the capability of the network to
recover or the time until its death depends on its structure, i.e., the proportion of
different types of nodes, and the importance of the node (like its links and volume
of sales) killed. The results also showed that the variance of parameters did not cause
a different behaviour but only a small variation of the profit a node could gain.
The network’s structure, in all databases, suffers severe modifications in terms
of disappearance of nodes. Even if the network is well distributed in terms of the
amount of each type of nodes and links, the loss of nodes is considerable. For
example, in database 3, which has the best distribution of nodes and links, the
network loses half of its clients (retailers). It is more probable for the network to
survive if the initial network is considerably big, i.e., from twenty-five nodes up.
Also, the greater the size of the network, greater is the number of iterations until the
network loses most of its nodes and, subsequently, loses the resilience. The nodes
with a greater profit tend to resist and survive until the last iteration performed.
However, if a hub, for example, a company which is connected to multiple clients
(retailers) and suppliers, is removed, then the nodes which had a large amount of
profit, e.g. some retailers or suppliers, might disappear because they were only
connected to the missing node or their greatest link was with the removed node.
So, after removing a node, the network structure changes and evolves to survive.
In this project, to measure the resilience it is used the Spearman’s ranked
correlation coefficient. To rank the pair of nodes, it is taking into consideration the
profit a node has with another. The resilience of a network might decrease a lot and
even be null. Consequently, the farther from zero the coefficient value is, the closer
the two structures are, i.e., there are more nodes whose rank is maintained or little
changed. This indicates the network has kept some of the same links throughout

374 A.Nogueiraetal.
the iterations after the removal of a node. Albeit some of these similarities with the
initial state, the network might not have the necessary stability and equilibrium to
survive the perturbation caused. So, the network does not have resilience since it did
not recover from the disturbance.
The number of links, the volume of sales and the total profit of a node has an
impact on its survival throughout time. If a node is a hub, its disappearance provokes
the loss of several links to the desired node. The results from simulation shows that
if a company (hub) disappears, then a retailer is not able to acquire products from
a given supplier that was only connected with the company. This situation causes
problems for the retailer and supplier since one cannot buy and the other does not
sell, respectively. An authority node is also an important one. In fact, this type of
node is the one that provides exactly what the other members of the network intend
therefore it is essential and unique for the network. If it disappears then the network
loses its supply source and if there are no other nodes to replace it, then the network
will not have the resilience and it would disappear.
For future work, the addition of a variable that simulates the economical variation
throughout time would be a great form to make the network more dynamic and
realistic since the market shares change constantly. Another improvement of the
model would be to incorporate the supply-demand relationship in the calculation of
profit for unlinked nodes. The metrics of resilience is not very developed in terms of
literature and trying to search and exploit this part of the work would be interesting
and innovative.
The aftermarket in the automotive industry is a complex business due to its
several variables, considerations and rules. This project helps to understand which
clients, suppliers and even competitors are crucial for the business and the capability
of a given network to recover from a loss. There is not much literature of similar
works in this business area and, it would be interesting to receive the feedback from
the business in terms of a strategy point of view. The model developed is essential
to support a decision making especially in a long-term plan.
References
1. B. Rundh, Market-led strategic change new interactions in the paper supply chain. Supply
Chain Management for Paper and Timber Industries. Växjö University School of Industrial
Engineering and Timber Logistics, Econpap, Espoo (2001), pp. 223–239
2. B. Vlacˇic´, L. Corbo, S. Costa e Silva, M. Dabic´, The evolving role of artificial intelligence in
marketing: a review and research agenda. J. Bus. Res. 128, 187–203 (2021)
3. A. de Bem Machado, S. Secinaro, D. Calandra, F. Lanzalonga, Knowledge management and
digital transformation for industry 4.0: a structured literature review. Knowl. Manage. Res.
Pract. 20(2), 320–338 (2022)
4. R. Hall, P. Andriani, Managing knowledge associated with innovation. J. Bus. Res. 56(2), 145–
152 (2003). The Dynamics of Strategy
5. G. Shankaranarayanan, Y. Cai, Supporting data quality management in decision-making.
Decis. Support Syst. 42(1), 302–317 (2006)

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 375
6. E. Borgonovo, V. Cappelli, F. Maccheroni, M. Marinacci, Risk analysis and decision theory: a
bridge. Eur. J. Oper. Res. 264(1), 280–293 (2018)
7. A. Sanayei, S. Farid Mousavi, A. Yazdankhah, Group decision making process for supplier
selection with vikor under fuzzy environment. Expert Syst. Appl. 37(1), 24–30 (2010)
8. D.M. Lambert, M.C Cooper, Issues in supply chain management. Ind. Mark. Manag. 29(1),
65–83 (2000)
9. H. Gao, M. Ren, Overreliance on china and dynamic balancing in the shift of global value
chains in response to global pandemic covid-19: an Australian and new zealand perspective.
Asian Bus. Manag. 19(3), 306–310 (2020)
10. C. Zhang, H. Gao, Managing business-to-business disruptions: surviving and thriving in the
face of challenges. Ind. Mark. Manag. 105, 72–78 (2022)
11. D.S. Johnson, S. Bharadwaj, Digitization of selling activity and sales force performance: an
empirical investigation. J. Acad. Mark. Sci. 33(1), 3–18 (2005)
12. M. Srivastava, A.K. Rai, An investigation of mediating and moderating variables in service
quality–customer loyalty relationship: a research agenda. Int. J. Customer Relationsh. Market.
Manag. 4(3), 20–43 (2013)
13. J. C. de Carvalho, Logística e gestão da cadeia de abastecimento. Edições Sílabo, 2nd edn.
(May 2017)
14. K. Govindan, T.C.E. Cheng, N. Mishra, N. Shukla, Big data analytics and application for
logistics and supply chain management. Transp. Res. E: Logist. Transp. Rev. 114, 343–349
(2018)
15. J.R. Evans, E. Minieka, Optimization Algorithms for Networks and Graphs: Revised and
Expanded (CRC Press, Boca Raton, 2017)
16. R. Diestel, Graph Theory. Graduate Texts in Mathematics (Springer, Berlin, 2018)
17. T. Arif, R. Ali, M. Asger, Article: scientific co-authorship social networks: a case study of
computer science scenario in India. Int. J. Comput. Appl. 52(12), 38–45 (2012). Full text
available
18. P. Holme, J. Saramäki, Temporal networks. Phys. Rep. 519(3), 97–125 (2012). Temporal
Networks
19. M.C. Vernon, M.J. Keeling, Representing the UK’s cattle herd as static and dynamic networks.
Proc. R. Soc. B: Biol. Sci. 276(1656), 469–476 (2009)
20. E. Valdano, L. Ferreri, C. Poletto, V. Colizza, Analytical computation of the epidemic threshold
on temporal networks. Phys. Rev. X 5, 021005 (2015)
21. J. Enright, R.R. Kao, Epidemics on dynamic networks. Epidemics 24, 88–97 (2018)
22. X. Liu, D. Li, M. Ma, B.K. Szymanski, H.E. Stanley, J. Gao, Network resilience. Phys. Rep.
971, 1–108 (2022). Network Resilience
23. S. Hosseini, K. Barker, J.E. Ramirez-Marquez, A review of definitions and measures of system
resilience. Reliab. Eng. Syst. Saf. 145, 47–61 (2016)
24. A.L. Pregenzer, Systems resilience: a new analytical framework for nuclear nonproliferation.
Technical report, Sandia National Laboratories (SNL), Albuquerque, and Livermore (2011)
25. Y.Y. Haimes, On the definition of resilience in systems. Risk Anal. 29(4), 498–501 (2009)
26. Y. Li, C.W. Zobel, Exploring supply chain network resilience in the presence of the ripple
effect. Int. J. Prod. Econ. 228, 107693 (2020)
27. J. Gao, B. Barzel, A.-L. Barabási, Universal resilience patterns in complex networks. Nature
530(7590), 307–312 (2016)
28. J.P.G. Sterbenz, D. Hutchison, E.K. Çetinkaya, A. Jabbar, J.P. Rohrer, M. Schöller, P. Smith,
Resilience and survivability in communication networks: strategies, principles, and survey of
disciplines. Comput. Netw. 54(8), 1245–1265 (2010). Resilient and Survivable networks
29. V.S. Raj, R.M. Chezian, Delay-disruption tolerant network (dtn), its network characteristics
and core applications. Int. J. Comput. Sci. Mob. Comput. 2(9), 256–262 (2013)
30. M.H. Hugos, Essentials of Supply Chain Management (John Wiley & Sons, Hoboken, 2018)
31. M. Christopher, Logistics & Supply Chain Management (Pearson, London, 2016)
32. J.P. Ribeiro, A. Barbosa-Povoa, Supply chain resilience: definitions and quantitative modelling
approaches – a literature review. Comput. Ind. Eng. 115, 109–122 (2018)

376 A.Nogueiraetal.
33. R. Bhagwat, M.K. Sharma, Performance measurement of supply chain management: a
balanced scorecard approach. Comput. Ind. Eng. 53(1), 43–62 (2007)
34. A. Spieske, M. Gebhardt, M. Kopyto, H. Birkel, Improving resilience of the healthcare supply
chain in a pandemic: evidence from Europe during the covid-19 crisis. J. Purch. Supply Manag.
28(5), 100748 (2022). Purchasing and Supply Management learning from the pandemic:
transforming for better crisis management
35. J. Wang, R. Dou, R.R. Muddada, W. Zhang, Management of a holistic supply chain network
for proactive resilience: theory and case study. Comput. Ind. Eng. 125, 668–677 (2018)
36. M. Kamalahmadi, M.M. Parast, A review of the literature on the principles of enterprise and
supply chain resilience: major findings and directions for future research. Int. J. Prod. Econ.
171, 116–133 (2016)
37. S. Melnyk, D.J. Closs, S. Griffis, C. Zobel, J. Macdonald, Understanding supply chain
resilience. Supply Chain Manag. Rev. 18, 34–41 (2014)
38. R. Aldrighetti, D. Battini, D. Ivanov, I. Zennaro, Costs of resilience and disruptions in supply
chain network design models: a review and future research directions. Int. J. Prod. Econ. 235,
108103 (2021)
39. T. Rebs, M. Brandenburg, S. Seuring, System dynamics modeling for sustainable supply chain
management: a literature review and systems thinking approach. J. Cleaner Prod. 208, 1265–
1280 (2019)
40. J.W. Forrester, System dynamics—the next fifty years. Syst. Dyn. Rev. 23(2–3), 359–370
(2007)
41. A. Kamali, S.M.T. Fatemi Ghomi, F. Jolai, A multi-objective quantity discount and joint
optimization model for coordination of a single-buyer multi-vendor supply chain. Comput.
Math. Appl. 62(8), 3251–3269 (2011)
42. C. Bode, S.M. Wagner, K.J. Petersen, L.M. Ellram, Understanding responses to supply chain
disruptions: insights from information processing and resource dependence perspectives. Acad.
Manag. J. 54(4), 833–856 (2011)
43. C. Minerbo, B. Flynn, S. Pereira, R. Outlaw, Supply chain trust: a two-way street? Acad.
Manag. Proc. 2018, 10974 (2018)
44. B. Flynn, M. Pagell, B. Fugate, Editorial: survey research design in supply chain management:
the need for evolution in our expectations. J. Supply Chain Manag. 54(1), 1–15 (2018)
45. A. Zaheer, N. Venkatraman, Relational governance as an interorganizational strategy: an
empirical test of the role of trust in economic exchange. Strateg. Manag. J. 16(5), 373–392
(1995)
46. E. Ambrose, D. Marshall, D. Lynch, Buyer supplier perspectives on supply chain relationships.
Int. J. Oper. Prod. Manag. 30, 1269–1290 (2010)
47. L. Poppo, T. Zenger, Do formal contracts and relational governance function as substitutes or
complements? Strateg. Manag. J. 23(8), 707–725 (2002)
48. P. Alves, P. Campos, E. Oliveira, Modeling the trustworthiness of a supplier agent in a b2b
relationship, in Collaborative Networks in the Internet of Services, ed. by L.M. Camarinha-
Matos, L. Xu, H. Afsarmanesh (Springer, Berlin, 2012), pp. 675–686
49. S. Janssen, A. Sharpanskykh, R. Curran, K. Langendoen, Using causal discovery to analyze
emergence in agent-based models. Simul. Model. Pract. Theory 96, 101940 (2019)
50. E. Borgonovo, E. Plischke, Sensitivity analysis: a review of recent advances. Eur. J. Oper. Res.
248(3), 869–887 (2016)
51. K. Zhao, Z. Zuo, J.V. Blackhurst, Modelling supply chain adaptation for disruptions: an
empirically grounded complex adaptive systems approach. J. Oper. Manag. 65(2), 190–212
(2019)
52. J. Lohmer, N. Bugert, R. Lasch, Analysis of resilience strategies and ripple effect in
blockchain-coordinated supply chains: an agent-based simulation study. Int. J. Prod. Econ.
228, 107882 (2020)
53. H. Hakansson, I. Snehota, Developing relationships in business networks. (Routledge, London,
NewYork, 1995)

14 ResilientAgent-BasedNetworksintheAutomotiveIndustry 377
54. K. Boissie, S.-A. Addouche, M. Zolghadri, D. Richard, Obsolescence mitigation in automotive
industry using long term storage feasibility model. Proc. Manuf. 16, 39–46 (2018). Proceedings
of the 7th International Conference on Through-life Engineering Services
55. M. Kivelä, A. Arenas, M. Barthelemy, J.P. Gleeson, Y. Moreno, M.A. Porter, Multilayer
networks. J. Complex Netw. 2(3), 203–271 (2014)
56. J. Gama, A.C. Lorena, K. Faceli, M. Oliveira, A. Ponce de Leon Carvalho, Extração de
Conhecimento de Dados, 3rd edn. (Edições Sílabo, setembro de 2017)
57. P. Holme, J. Saramäki, Temporal Networks, 1st edn. (Springer, Berlin, 2013)
58. C. Silva, I. Mota, P. Campos, A matching model of R&D Cooperation. Paper presented at the
Artificial Economics conference, Porto (2015)
59. R. Costa, Desenvolvimento de um modelo para a gestão de stocks no grupo Nors. MSc
Thesis Presented at Instituto Superior de Engenharia do Porto, ISEP, Matemática Aplicada
à Engenharia e às Finanças (2014)
60. P. Smith, D. Hutchison, M. Banfield, K. Leopold, On understanding normal protocol behaviour
to monitor and mitigate the abnormal. Paper presented at the Proceedings of the IEEE/IST
Workshop on Monitoring, Attack Detection and Mitigation (MonAM), Tuebingen (2006)
61. C. Spearman, The proof and measurement of association between two things. Am. J. Psychol.
15(1), 72–101 (1904). https://doi.org/10.2307/1412159. JSTOR 1412159
62. R. Laishram, A.E. Sariyüce, T. Eliassi-Rad, A. Pinar, S. Soundarajan, Measuring and improv-
ing the core resilience of networks, in Proceedings of the 2018 World Wide Web Conference
(WWW ’18). International World Wide Web Conferences Steering Committee, Republic and
Canton of Geneva (2018). https://doi.org/10.1145/3178876.3186127
63. C. Macal, M. North, Tutorial on agent-based modelling and simulation. J. Simul. 4, 151–162
(2010). https://doi.org/10.1057/jos.2010.3