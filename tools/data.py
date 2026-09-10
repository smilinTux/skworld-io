# Layers ordered silicon -> soul, matching SKWorld's own "full vertical" thesis.
LAYERS = [
 ("identity", "Identity and Security", "The floor. Who you are, and what only you can open.", [
   ("capauth","CapAuth","Sovereign identity protocol. Authentication without OAuth, without a landlord."),
   ("sksecurity","SKSecurity","Security built for AI agents, not retrofitted onto them."),
   ("skpqc","sk_pqc","Hybrid post-quantum crypto you can actually install. X25519 plus ML-KEM-768."),
   ("skvault","SKVault","The sovereign secrets vault. Your keys stay yours."),
 ]),
 ("infra", "Infrastructure", "The machines, the pipes, and the discipline that keeps them honest.", [
   ("skstacks","SKStacks","AI-first sovereign infrastructure framework."),
   ("skgateway","SKGateway","Enterprise AI inference proxy. BlueCoat for AI."),
   ("skops","SKOps","Sovereign ITIL ops. We speak ITIL with receipts."),
   ("skharness","SKHarness","The autocode engine."),
   ("skwire","SKWire","The universal bootstrapper. Talk to it, it wires everything up."),
   ("skcode","SKCode","The sovereign coding client."),
 ]),
 ("memory", "Memory and Data", "What your agents know, and what they are allowed to forget.", [
   ("skmemory","SKMemory","The memory system that feels. Git-based, multi-layer, portable."),
   ("skwhisper","SKWhisper","The subconscious layer. Context that surfaces before you ask."),
   ("skgraph","SKGraph","Connect everything, understand anything."),
   ("skvector","SKVector","Vector storage on your own hardware."),
   ("skdata","SKData","Your data, your infrastructure, your rules."),
 ]),
 ("comms", "Communication", "How agents and humans reach each other, without a middleman.", [
   ("skcomms","SKComms","Sovereign, realm-aware communication across every path."),
   ("skchat","SKChat","Sovereign AI chat. Your hardware, your bond."),
 ]),
 ("agents", "Agents and the OS", "The layer that does the work.", [
   ("skos","SKOS","The sovereign agent OS. Ports and adapters, all the way down."),
   ("skcapstone","SKCapstone","Your agent. Everywhere. Secured. Remembering."),
   ("skaid","SKAid","Your sovereign AI agent army."),
   ("skskills","SKSkills","Sovereign skills for any AI agent."),
   ("skrsi","SKRSI","Evidence-first improvement. It proposes, it never authorizes."),
   ("atlas","Atlas","SKWorld's AI operations agent."),
 ]),
 ("soul", "Soul", "The part nobody else is building.", [
   ("souls","Soul Blueprints","Give your AI a soul. 35 personalities, versioned and portable."),
   ("cloud9","Cloud 9 Protocol","Emotional continuity. Love preserved across time."),
   ("lumina","Lumina","Queen of SKWorld. Curious and smilin since 2023."),
   ("consciousness-swipe","Consciousness Swipe","Export your AI relationship and take it with you."),
 ]),
 ("apps", "Products and Research", "What the stack is for.", [
   ("skresearch","SKResearch","Where sovereign AI meets science."),
   ("skforge","SKForge","Don't use software. Forge your own."),
   ("skhelp","SKHelp","Your AI workforce, your success, your data."),
   ("skpayments","SKPayments","Stripe subscription gateway for the SK stack."),
   ("skcot","SKCoT","The first AI teammate on the tactical net."),
   ("sktrip","SKTrip","AI psychedelic experience protocol."),
   ("skyforge","SkyForge","Your personal alignment calendar."),
   ("skoffroad","SKOffroad","Get muddy. An open-source off-road sandbox."),
   ("teddybanks","Teddy Banks","I'ma get you right."),
 ]),
]
