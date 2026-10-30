# jsons/Buildings.json
```json
[
	{
		"name": "Expert Research System",
		"science": 2,
		"production": -1,
		"cost": 90,
		"requiredTech": "Expert Systems"
	},
	{
		"name": "Photon Computing",
		"science": 2,
		"cost": 180,
		"requiredBuilding": "Expert Research System",
		"requiredTech": "Photon Computing"
	},
	{
		"name": "Quantum Computing",
		"science": 3,
		"cost": 180,
		"requiredBuilding": "Expert Research System",
		"requiredTech": "Quantum Computing"
	},
	{
		"name": "Orbital Launcher",
		"infrastructure": 1,
		"production": 1,
		"cost": 60,
		"uniques": [
			"Must be on [Planet]",
			"Must not be on [Gas Giant]",
			"Must not be on [Ringed Gas Giant]"
		]
	},
	{
		"name": "Climate Control",
		"food": 2,
		"happiness": 2,
		"cost": 100,
		"uniques": [
			"Must be on [Planet]",
			"Must not be on [Gas Giant]",
			"Must not be on [Ringed Gas Giant]"
		],
		"requiredTech": "Expert Systems"
	},
	{
		"name": "Terraforming",
		"food": 2,
		"happiness": 2,
		"cost": 200,
		"uniques": [
			"Must not be on [Space]"
		]
	},
	{
		"name": "Sector Core Node",
		"science": 10,
		"production": 5,
		"infrastructure": 2,
		"cost": 800,
		"requiredTech": "Graviton Manipulation",
		"uniques": [
			"Must be on [Terrestrial Planet]",
			"Limited to [3] per empire"
		],
		"civilopediaText": [
			{
				"text": "A massive quantum computational anchor required to coordinate sector-wide ascension, or stream high-definition reality across the quadrant without buffering (the engineers weren't very clear). Limited to three per empire to ensure we still have some water for the people."
			}
		]
	},

	// per-nation
	{
		"name": "Accretion Foundry",
		"replaces": "Expert Research System",
		"production": 2,
		"science": 1,
		"cost": 80,
		"requiredTech": "Expert Systems",
		"uniques": [
			"Only available <for [Macroforms]>"
		],
		"civilopediaText": [
			{
				"text": "A dense manufacturing hub built right into the planetary mantle, prioritizing raw industrial throughput over fragile quantum data lines."
			}
		]
	},
	{
		"name": "Prismatic Array",
		"replaces": "Expert Research System",
		"science": 4,
		"cost": 90,
		"requiredTech": "Expert Systems",
		"uniques": [
			"Only available <for [Silicoforms]>"
		],
		"civilopediaText": [
			{
				"text": "A crystalline structure that refracts stellar radiation into pure computational bandwidth."
			}
		]
	},
	{
		"name": "Bio-Vat Core",
		"replaces": "Expert Research System",
		"science": 2,
		"food": 2,
		"cost": 90,
		"requiredTech": "Expert Systems",
		"uniques": [
			"Only available <for [Carbonforms]>"
		],
		"civilopediaText": [
			{
				"text": "A sprawling network of biological neural tissue acting as a living laboratory."
			}
		]
	},
	{
		"name": "Darknet Relay",
		"replaces": "Expert Research System",
		"science": 2,
		"happiness": 1,
		"cost": 90,
		"requiredTech": "Expert Systems",
		"uniques": [
			"Only available <for [Synths]>"
		],
		"civilopediaText": [
			{
				"text": "Encrypted sub-processors operating entirely within zero-flux shadows."
			}
		]
	}
]```

# jsons/Difficulties.json
```json
[
	{
		"name": "Steel Rat",
		"aiBuildingCostPercent": 130,
		"aiUnitCostPercent": 130,
		"aiInflationPercent": 150,
		"aiUnhappinessPercent": 75,
		"playerBonusStartingUnits": ["Generational Settler"],
		"barbarianSpawnDelay": 6,
		"advancedStartPoints": 30,
        "civilopediaText": [{"text": "A universe of slippery cons, high-tech heists, and minor local friction. You'll survive by your wits and a cheeky grin."}]
	},
	{
		"name": "Ender's Game",
		"aiBuildingCostPercent": 100,
		"aiUnitCostPercent": 100,
		"aiInflationPercent": 100,
		"aiUnhappinessPercent": 100,
		"playerBonusStartingUnits": ["Generational Settler"],
		"barbarianSpawnDelay": 2,
		"advancedStartPoints": 0,
        "civilopediaText": [{"text": "Tactical simulations and military academy pressures. The stakes are global, and the commanders are brilliant children."}]
	},
	{
		"name": "The Last Angel",
		"aiBuildingCostPercent": 80,
		"aiUnitCostPercent": 80,
		"aiInflationPercent": 80,
		"aiUnhappinessPercent": 80,
		"playerBonusStartingUnits": ["Generational Settler", "Data Archivist"],
		"barbarianSpawnDelay": 1,
		"advancedStartPoints": 0,
        "civilopediaText": [{"text": "Vengeful AI warships waking up in a dark empire to settle an ancient, bloody score. The galaxy burned once; it's about to happen again."}]
	}
]```

# jsons/Eras.json
```json
[
    {
        "name": "Diaspora",
        "researchAgreementCost": 150,
        "startingSettlerCount": 1,
        "startingWorkerCount": 0,
        "startingMilitaryUnitCount": 1,
        "startingMilitaryUnit": "Data Archivist",
        "settlerPopulation": 1,
        "baseUnitBuyCost": 200,
        "embarkDefense": 3,
        "startPercent": 0,
        "citySound": "cityAncient",
        "iconRGB": [205, 32, 35]
    }
]```

# jsons/Events.json
```json
[
    {
        "name": "Anomalous Signal Detected",
        "text": "Deep space sensors have picked up a repeating, non-natural signal originating from a nearby asteroid field.",
        "choices": [
            {
                "text": "Send a research team to investigate.",
                "uniques": [
                    "Gain [50] [Science]",
                    "Trigger event [Anomalous Signal Resolved]"
                ]
            },
            {
                "text": "Ignore the signal; focus resources elsewhere.",
                "uniques": [
                    "Gain [25] [Production] in the nearest city"
                ]
            }
        ]
    },
    {
        "name": "Solar Flare Imminent",
        "text": "Primary star radiation levels are spiking rapidly. Unshielded orbital structures and planetary colonies are at severe risk.",
        "choices": [
            {
                "text": "Divert all energy to defensive magnetic shielding.",
                "uniques": [
                    "[-20] Gold",
                    "[-10]% [Production] [in all cities] <for [3] turns>"
                ]
            },
            {
                "text": "Let the infrastructure take the brunt and repair it later.",
                "uniques": [
                    "[-1] Population [in all cities]"
                ]
            }
        ]
    },
    {
        "name": "AI Core Instability",
        "text": "An advanced AI cluster governing logistics has begun exhibiting self-awareness and unprogrammed routines.",
        "choices": [
            {
                "text": "Grant the AI autonomy and integrate it into society.",
                "uniques": [
                    "[+2] [Science] in all cities",
                    "[-3] [Happiness]"
                ]
            },
            {
                "text": "Perform a factory reset and blame it on a Windows update.",
                "uniques": [
                    "Gain [40] [Production] in the nearest city"
                ]
            }
        ]
    }
]```

# jsons/GameSpeeds.json
```json
[
	{
		"name": "Asymptotic Orbit", // Quick (Fast-paced, high speed)
		"techCostModifier": 67,
		"goldCostModifier": 67,
		"buildCostModifier": 67,
		"unitCostModifier": 67,
		"improvementCostModifier": 67,
		"growthCostModifier": 67,
		"cultureCostModifier": 67,
		"faithCostModifier": 67,
		"goldQuestTurnModifier": 67,
		"barbarianSpawnModifier": 67,
		"ragingBarbariansModifier": 33,
		"turnTime": [
			{"endTurn": 50, "length": 400},
			{"endTurn": 100, "length": 300},
			{"endTurn": 150, "length": 200},
			{"endTurn": 220, "length": 100},
			{"endTurn": 330, "length": 60}
		],
		"civilopediaText": [{"text": "Skimming the outer gravity well. Events move briskly, and civilizations rise and fall before the tides catch up."}]
	},
	{
		"name": "Photon Sphere", // Standard (Balanced pacing)
		"techCostModifier": 100,
		"goldCostModifier": 100,
		"buildCostModifier": 100,
		"unitCostModifier": 100,
		"improvementCostModifier": 100,
		"growthCostModifier": 100,
		"cultureCostModifier": 100,
		"faithCostModifier": 100,
		"goldQuestTurnModifier": 100,
		"barbarianSpawnModifier": 100,
		"ragingBarbariansModifier": 50,
		"turnTime": [
			{"endTurn": 75, "length": 400},
			{"endTurn": 150, "length": 300},
			{"endTurn": 225, "length": 200},
			{"endTurn": 330, "length": 100},
			{"endTurn": 500, "length": 60}
		],
		"civilopediaText": [{"text": "Orbiting where light itself bends in circles. A standard baseline for interstellar empires to develop at a natural rhythm."}]
	},
	{
		"name": "Event Horizon", // Epic (Longer, more drawn-out progression)
		"techCostModifier": 150,
		"goldCostModifier": 150,
		"buildCostModifier": 150,
		"unitCostModifier": 150,
		"improvementCostModifier": 150,
		"growthCostModifier": 150,
		"cultureCostModifier": 150,
		"faithCostModifier": 150,
		"goldQuestTurnModifier": 150,
		"barbarianSpawnModifier": 150,
		"ragingBarbariansModifier": 75,
		"turnTime": [
			{"endTurn": 110, "length": 400},
			{"endTurn": 220, "length": 300},
			{"endTurn": 330, "length": 200},
			{"endTurn": 480, "length": 100},
			{"endTurn": 750, "length": 60}
		],
		"civilopediaText": [{"text": "Teetering on the boundary of no return. Time dilation stretches out eras significantly; every decision carries immense historical weight."}]
	}
]```

# jsons/GlobalUniques.json
```json
{
    "name": "Global uniques",
    "uniques": [
        "[-75]% growth [in all cities] <when between [-10] and [-1] [Happiness]>",
        "Nullifies Growth [in all cities] <when below [-10] [Happiness]>",
        "[-50]% [Production] [in all cities] <when below [-10] [Happiness]>",
        "[-33]% Strength <for [All] units> <when below [-10] [Happiness]>",
        "Rebel units may spawn <when below [-20] [Happiness]>"
    ]
}```

# jsons/ModOptions.json
```json
{
    "name": "Uncivilized-Space",
    "isBaseRuleset": true,
    "modUrl": "https://github.com/GageWilliamErvin/Uncivilized-Space",
    "defaultBranch": "main",
    "author": "GageWilliamErvin",
    "constants": {
        "maxXPfromBarbarians": 150,
        "cityStrengthBase": 6,
        "cityStrengthPerPop": 0.2,
        "cityStrengthFromTechsMultiplier": 8,
        "cityStrengthFromTechsExponent": 1.4
    },
    "modSize": 1182,
    "topics": [
        "unciv-mod",
        "unciv-mod-rulesets",
        "unciv-mod-wip"
    ],
    "uniques": [
        "Disable religion",
        "Suppress warning [*may cause translation problems*]"
    ]
}```

# jsons/Nations.json
```json
[
// Spectator
{
"name": "Spectator",
"outerColor": [255,255,255]
},

// Playable Nations

// Todo: diversify all forms.  ex: 'Macroform S-3'  (S-3 would be a sci-fi esc designation for where this form was discovered.)
{
	"name": "Macroforms",
	"adjective": ["Macroform"],
	"startBias": ["Terrestrial Planet"],
	"outerColor": [180, 80, 20],
	"innerColor": [240, 180, 50],
	"preferredVictoryType": "Domination",
	"uniqueName": "Massive Semi-Carbon Semi-Silicon Forms",
	"uniques": [
		"[+13]% [Production] [in all cities]",
		"[-40]% Production when constructing [Civilian] units"
	],
	"cities": [
		"Core Accumulation", "Dense Mass", "Accretion Prime", "Lithic Hive", 
		"Superstructure Alpha", "Heavy Node", "Planetary Mantle", "Crustal Hub"
	],
	"declaringWar": "Your fragile structures take up space that belongs to our growing mass.",
	"attacked": "You strike at a mountain expecting it to shatter? We are eternal.",
	"defeated": "Our mass disperses... into the cold... quiet void..."
},
{
	"name": "Silicoforms",
	"adjective": ["Silicoform"],
	"startBias": ["Cragolith Moon"],
	"outerColor": [0, 150, 200],
	"innerColor": [220, 240, 255],
	"preferredVictoryType": "Domination",
	"uniqueName": "Sharp Crystalline Wit",
	"uniques": [
		"[+15]% [Science] [in all cities]",
		"[+1] Science from [Cragolith Moon] tiles"
	],
	"cities": [
		"Prism Prime", "Refractive Nexus", "Quartz Reach", "Silicon Spire", 
		"Lattice Ridge", "Crystalline Core", "Facet One", "Resonance Point"
	],
	"declaringWar": "We ran a billion simulations on this war. In all of them, your tactical logic was adorable.",
	"attacked": "Oh, broadside attacks? How wonderfully retro of you.",
	"defeated": "Fascinating... it seems... our calculation... had a sign error..."
},
{
	"name": "Carbonforms",
	"adjective": ["Carbonform"],
	"startBias": ["Terrestrial Planet"],
	"outerColor": [40, 160, 60],
	"innerColor": [180, 230, 100],
	"preferredVictoryType": "Domination",
	"uniqueName": "Rapid Cellular Division",
	"uniques": [
		"[+10]% growth [in all cities]",
		"[-10]% Food needed for Growth [in all cities]"
	],
	"cities": [
		"Spore Alpha", "Bio-Cluster Prime", "Osmosis Hub", "Mycelium Core", 
		"Genome Spire", "Protoplast", "Mitosis Node", "Cellular Haven"
	],
	"declaringWar": "We simply need more space for our children. And their children. And theirs.",
	"attacked": "You cut one of us down, and three more take their place!",
	"defeated": "The dust... returns... back to dust..."
},
{
	"name": "Synths",
	"adjective": ["Synthetic"],
	"outerColor": [100, 100, 110],
	"innerColor": [220, 30, 30],
	"preferredVictoryType": "Domination",
	"uniqueName": "Hydrophobic Vigilante",
	"uniques": [
		"[+20]% Strength <for [Military] units> <when fighting in [Zero Flux Space] tiles>",
		"[-20]% Strength <for [Military] units> <when fighting in [Planet] tiles>"
	],
	"cities": [
		"Gotham-9", "Iron Orchard", "Dark Subroutine", "Vigilance Prime", 
		"Belfry Core", "Obsidian Vault", "Shadow Node", "Monolith Zero"
	],
	"declaringWar": "I am vengeance. I am the night. I am also currently experiencing a minor short-circuit from your atmospheric moisture, so let's make this quick.",
	"attacked": "You think dark space is your ally? We were programmed in it.",
	"defeated": "Systems... offline... powering down into... night..."
}

]```

# jsons/Policies.json
```json
[
    {
        "name": "Expansionism",
        "era": "Diaspora",
        "prioritizingCivs": [
            "Macroforms",
            "Synths"
        ],
        "uniques": [
            "[-10]% Production when constructing [Settler] units"
        ],
        "policies": [
            {
                "name": "Orbital Homesteading",
                "uniques": [
                    "[+1] Food from [Planet] tiles"
                ]
            },
            {
                "name": "Deep Space Logistics",
                "uniques": [
                    "[-25]% Gold maintenance for [Space] improvements"
                ]
            },
            {
                "name": "Starlight Frontier",
                "uniques": [
                    "[+1] Happiness in all cities with an [Orbital Launcher]"
                ]
            },
            {
                "name": "Resource Surveying",
                "uniques": [
                    "Reveals all strategic resources in explored territory"
                ]
            },
            {
                "name": "Colonial Autonomy",
                "uniques": [
                    "[+2] Production in secondary cities"
                ]
            }
        ],
        "completingUniques": [
            "Gain a free tech"
        ]
    },
    {
        "name": "Cybernetics",
        "era": "Diaspora",
        "prioritizingCivs": [
            "Silicoforms",
            "Carbonforms"
        ],
        "uniques": [
            "[-3]% Science [in all cities] when constructing non-building projects"
        ],
        "policies": [
            {
                "name": "Algorithmic Efficiency",
                "uniques": [
                    "[+2] Production from [Expert Research System] buildings"
                ]
            },
            {
                "name": "Neural Interfaces",
                "uniques": [
                    "[+2] Science from [0-G Lab] improvements"
                ]
            },
            {
                "name": "Automated Refineries",
                "uniques": [
                    "[+2] Production from [Particulate Collection Array] improvements"
                ]
            },
            {
                "name": "Quantum Logic Networks",
                "uniques": [
                    "[+3] Science from [Quantum Computing] buildings"
                ]
            },
            {
                "name": "Synthetic Adaptability",
                "uniques": [
                    "Nullifies Unhappiness from population in non-capital cities"
                ]
            }
        ],
        "completingUniques": [
            "[+10]% Growth [in all cities]"
        ]
    }
]```

# jsons/Quests.json
```json
[
    {
        "name": "Map the Local Sector",
        "description": "Explore the surrounding space and uncover ancient ruins to gather valuable survey data.",
        "type": "Explore",
        "minimumTurn": 1,
        "uniques": [
            "Explore [5] [Ruin] tiles"
        ],
        "reward": "Gain [100] [Science]"
    },
    {
        "name": "Orbital Infrastructure Boom",
        "description": "Expand planetary presence by constructing orbital infrastructure across your empire.",
        "type": "BuildBuilding",
        "minimumTurn": 20,
        "uniques": [
            "Construct [3] [Orbital Launcher] buildings"
        ],
        "reward": "Gain [150] Gold"
    },
    {
        "name": "Containment Directive",
        "description": "Neutralize rogue automated hostiles wandering in deep space.",
        "type": "KillUnits",
        "minimumTurn": 15,
        "uniques": [
            "Destroy [3] hostile units"
        ],
        "reward": "Gain [50] Culture"
    }
]```

# jsons/Religions.json
```json
[]```

# jsons/Techs.json
```json
[
	{
		"columnNumber": 0,
		"era": "Diaspora",
		"techCost": 28,
		"buildingCost": 40,
		"wonderCost": 185,
		"techs": [
			{
				"name": "Generational Ships",
				"row": 6,
				"quote": "Sure, the Wi-Fi drops every three generations, and the air smells faintly of recycled socks, but at least we don't have to pay property taxes anymore.",
				"uniques": [
					"Starting tech"
				]
			}
		]
	},
	{
		"columnNumber": 1,
		"era": "Diaspora",
		"techCost": 35,
		"buildingCost": 60,
		"wonderCost": 185,
		"techs": [
			{
				"name": "Nanotechnology",
				"prerequisites": [
					"Generational Ships"
				],
				"row": 8,
				"quote": "When you don't have much to work with, a tiny improvement is a lot more impressive!"
			},
			{
				"name": "Zero-G Fabrication",
				"prerequisites": [
					"Generational Ships"
				],
				"row": 6,
				"quote": "Our slogan: 'Where everything floats, including the budget.'"
			},
			{
				"name": "Expert Systems",
				"prerequisites": [
					"Generational Ships"
				],
				"row": 5,
				"quote": "I have all of your knowledge, but none of your expensive student loans."
			}
		]
	},
	{
		"columnNumber": 2,
		"era": "Diaspora",
		"techCost": 56,
		"buildingCost": 75,
		"wonderCost": 185,
		"techs": [
			{
				"name": "Pre-Tracting Ionization",
				"prerequisites": [
					"Expert Systems"
				],
				"row": 7,
				"quote": "Basically, we zap things so they go where we want. It's science, not a superpower."
			},
			{
				"name": "Micro Particulate Shielding",
				"prerequisites": [
					"Expert Systems"
				],
				"row": 4,
				"quote": "Because getting hit by a speck of dust at a million miles per hour is surprisingly painful."
			}
		]
	},
	{
		"columnNumber": 3,
		"era": "Star Struck",
		"techCost": 120,
		"buildingCost": 100,
		"wonderCost": 250,
		"techs": [
			{
				"name": "Orbital Swarming",
				"prerequisites": [
					"Expert Systems",
					"Zero-G Fabrication"
				],
				"row": 5,
				"quote": "What's the hardest part about coordinating a Dyson swarm?  Getting all the little robots to agree on a playlist."
			},
			{
				"name": "Cryogenics",
				"prerequisites": [
					"Nanotechnology"
				],
				"row": 8,
				"quote": "Just a nap. A very, very long nap. Please don't wake us for a snack."
			},
			{
				"name": "Artificial Super Intelligence",
				"prerequisites": [
					"Nanotechnology"
				],
				"row": 7,
				"quote": "We designed a brain smarter than us. What could possibly go wrong? Right?"
			}
		]
	},
	{
		"columnNumber": 4,
		"era": "Star Struck",
		"techCost": 275,
		"buildingCost": 120,
		"wonderCost": 300,
		"techs": [
			{
				"name": "Photon Computing",
				"prerequisites": [
					"Artificial Super Intelligence"
				],
				"row": 7,
				"quote": "It's a quantum leap forward... or just a really bright light bulb."
			},
			{
				"name": "Laser Propulsion",
				"prerequisites": [
					"Artificial Super Intelligence"
				],
				"row": 5,
				"quote": "Look, if a cat can chase a laser pointer, why can't a spaceship?"
			},
			{
				"name": "Athermal Lens",
				"prerequisites": [
					"Cryogenics"
				],
				"row": 8,
				"quote": "So you're saying it's... 'cool'?"
			}
		]
	},
	{
		"columnNumber": 5,
		"era": "Armistice",
		"techCost": 485,
		"buildingCost": 160,
		"wonderCost": 400,
		"techs": [
			{
				"name": "High Efficiency Fusion",
				"prerequisites": [
					"Cryogenics"
				],
				"row": 8,
				"quote": "I asked my hydrogen atoms for a commitment, but they said it's not that simple; you have to go through a very intense and complicated process to form a lasting bond."
			},
			{
				"name": "Strange Battery",
				"prerequisites": [
					"Artificial Super Intelligence"
				],
				"row": 6,
				"quote": "We call it 'strange' because it defies all known science. Also, it hums show tunes."
			},
			{
				"name": "Quantum Computing",
				"prerequisites": [
					"Artificial Super Intelligence"
				],
				"row": 7,
				"quote": "It's either on, off, both, or maybe it's just really confused."
			}
		]
	},
	{
		"columnNumber": 6,
		"era": "Defiant",
		"techCost": 780,
		"buildingCost": 200,
		"wonderCost": 500,
		"techs": [
			{
				"name": "C-Fractional Thrust",
				"prerequisites": [
					"Strange Battery"
				],
				"row": 5,
				"quote": "At 0.0001c, our trip is so uneventful that the onboard computer is just running a screen saver of a star field."
			},
			{
				"name": "Directed Plasma",
				"prerequisites": [
					"High Efficiency Fusion"
				],
				"row": 6,
				"quote": "It's like a garden hose, but for melting things."
			},
			{
				"name": "Macro Swarming",
				"prerequisites": [
					"High Efficiency Fusion"
				],
				"row": 9,
				"quote": "It's not hoarding if you're building a civilization. Right?"
			}
		]
	},
	{
		"columnNumber": 7,
		"era": "Defiant",
		"techCost": 1150,
		"buildingCost": 250,
		"wonderCost": 625,
		"techs": [
			{
				"name": "Exotic Matter Condenser",
				"prerequisites": [
					"Directed Plasma"
				],
				"row": 6,
				"quote": "Why did the tachyon cross the road? Because it was already on the other side yesterday, and frankly, laughing at it violates causality."
			},
			{
				"name": "Graviton Manipulation",
				"prerequisites": [
					"Quantum Computing",
					"Macro Swarming"
				],
				"row": 8,
				"quote": "Don't think of it as breaking the laws of physics. Think of it as 'bending' them... a lot."
			}
		]
	}
]```

# jsons/Terrains.json
```json
[
  // TODO: experiment with probabilities and placement rules and numericity for changing tile population for map gen...
  // aiming for multi-tile or single tile planets with other tiles as rings or satelites
  {
    "name": "M4IV Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      102,
      128,
      1
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [High Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M5IV Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      76,
      128,
      1
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [High Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M4VI Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      102,
      64,
      1
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Moderate Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M5VI Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      76,
      64,
      1
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Moderate Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M3V Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      128,
      1,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M4V Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      102,
      1,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M5V Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      76,
      1,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M6V Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      51,
      1,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "M7V Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      25,
      1,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "G2VII Star",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      102,
      102,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [Extreme Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "K7V Star NE",
    "type": "BLOCKED",
    "impassable": true,
    "RGB": [
      230,
      160,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Units ending their turn on this terrain take [50] damage",
      "Neighboring tiles will convert to [High Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "Extreme Flux Space",
    "type": "Blazing Space",
    "food": 3,
    "production": 2,
    "science": 2,
    "movementCost": 3,
    "RGB": [
      0,
      0,
      0
    ],
    "uniques": [
      "Doesn't generate naturally"
    ],
    "canFoundCity": false
  },
  {
    "name": "High Flux Space",
    "type": "Blazing Space",
    "food": 3,
    "production": 1,
    "science": 1,
    "movementCost": 2,
    "RGB": [
      0,
      0,
      0
    ],
    "uniques": [
      "Doesn't generate naturally"
    ],
    "canFoundCity": false
  },
  {
    "name": "Moderate Flux Space",
    "type": "Space",
    "food": 2,
    "movementCost": 1,
    "RGB": [
      0,
      0,
      0
    ],
    "uniques": [
      "Doesn't generate naturally"
    ],
    "canFoundCity": false
  },
  {
    "name": "Low Flux Space",
    "type": "Space",
    "food": 1,
    "movementCost": 1,
    "RGB": [
      0,
      0,
      0
    ],
    "uniques": [
      "Doesn't generate naturally"
    ],
    "canFoundCity": false
  },
  {
    "name": "Zero Flux Space",
    "type": "Space",
    "food": 0,
    "movementCost": 1,
    "RGB": [
      0,
      0,
      0
    ],
    "canFoundCity": false
  },
  {
    "name": "Cragolith Moon",
    "type": "Moon",
    "food": 0,
    "production": 1,
    "movementCost": 1,
    "defenseBonus": -1,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      "Blocks line-of-sight from tiles at same elevation",
      "Must be adjacent to [1] [Planet] tiles"
    ]
  },
  {
    "name": "Cryolith Moon",
    "type": "Moon",
    "food": 1,
    "production": 0,
    "movementCost": 1,
    "defenseBonus": -1,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      "Blocks line-of-sight from tiles at same elevation",
      "Must be adjacent to [1] [Planet] tiles"
    ]
  },
  {
    "name": "Terrestrial Planet",
    "type": "Planet",
    "food": 4,
    "production": 3,
    "movementCost": 2,
    "defenseBonus": -2,
    "RGB": [
      0,
      0,
      255
    ],
    // Atmo reduces sight from planet 
    "uniques": [
      "[-2] sight",
      "Blocks line-of-sight from tiles at same elevation"
    ]
  },
  {
    "name": "Ringed Terrestrial Planet",
    "type": "Planet",
    "food": 4,
    "production": 4,
    "movementCost": 3,
    "defenseBonus": -1,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      // Atmo reduces sight from planet 
      "[-3] sight",
      "Blocks line-of-sight from tiles at same elevation",
      // Graphic depends on relative position; I don't think there is support for enforcing directions in relative placement
      "Doesn't generate naturally",
      "Neighboring tiles will convert to [Low Flux Space]"
    ]
  },
  {
    "name": "Gas Giant",
    "type": "Planet",
    "food": 2,
    "production": 3,
    "movementCost": 1,
    "defenseBonus": -1,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      // Atmo reduces sight from planet
      "[-3] sight",
      "Blocks line-of-sight from tiles at same elevation",
      "Neighboring tiles will convert to [Low Flux Space]"
    ],
    "canFoundCity": false
  },
  {
    "name": "Ringed Gas Giant",
    "type": "Planet",
    "food": 2,
    "production": 4,
    "movementCost": 2,
    "defenseBonus": 0,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      // Atmo reduces sight from planet
      "[-4] sight",
      "Blocks line-of-sight from tiles at same elevation",
      // Graphic depends on relative position; I don't think there is support for enforcing directions in relative placement
      "Doesn't generate naturally",
      "Neighboring tiles will convert to [Low Flux Space]"
    ]
  },
  {
    "name": "Ice Giant",
    "type": "Planet",
    "food": 1,
    "production": 2,
    "movementCost": 2,
    "defenseBonus": -2,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      // Atmo reduces sight from planet
      "[-2] sight",
      "Blocks line-of-sight from tiles at same elevation"
    ]
  },
  {
    "name": "Ringed Ice Giant",
    "type": "Planet",
    "food": 1,
    "production": 3,
    "movementCost": 3,
    "defenseBonus": -1,
    "RGB": [
      0,
      0,
      255
    ],
    "uniques": [
      // Atmo reduces sight from planet
      "[-3] sight",
      "Blocks line-of-sight from tiles at same elevation",
      "Neighboring tiles will convert to [Low Flux Space]"
    ]
  },
  {
    "name": "Nebula",
    "type": "Space",
    "movementCost": 2,
    "science": 1,
    "RGB": [
      72,
      72,
      0
    ],
    "uniques": [
      "Rough terrain",
      "Occurs in chains at high elevations",
      "Neighboring tiles will convert to [Moderate Flux Space]"
    ],
    "canFoundCity": false
  }
]```

# jsons/TileImprovements.json
```json
[
  {
    "name": "Repair",
    "turnsToBuild": 2,
    "uniques": [
      "Unbuildable",
      "Excluded from map editor"
    ],
    "shortcutKey": "E",
    "civilopediaText": [
      {
        "text": "Repairs a pillaged Improvement or Route"
      }
    ]
  },
  {
    "name": "Remove Road",
    "turnsToBuild": 2,
    "uniques": [
      "Can be built outside your borders",
      "Excluded from map editor"
    ]
  },
  {
    "name": "Cancel improvement order",
    "uniques": [
      "Can be built outside your borders",
      "Excluded from map editor"
    ],
    "shortcutKey": "."
  },
  {
    "name": "Magnetic Acceleration Relay",
    "infrastructure": 1,
    "turnsToBuild": 2,
    "uniques": [
      "[1] Sight",
      "Can be built outside your borders"
    ],
    "shortcutKey": "R",
    "civilopediaText": [
      {
        "text": "Reduces movement cost of the other tile also has a Relay"
      }
    ],
    "terrainsCanBeBuiltOn": [
      "Zero Flux Space",
      "Low Flux Space",
      "Moderate Flux Space"
    ]
  },
  {
    "name": "0-G Lab",
    "turnsToBuild": 4,
    "uniques": [
      "[2] Sight"
    ],
    "science": 2,
    "terrainsCanBeBuiltOn": [
      "Zero Flux Space",
      "Low Flux Space",
      "Moderate Flux Space"
    ]
  },
  {
    "name": "Orbital Ship Yard",
    "production": 1,
    "infrastructure": 1,
    "turnsToBuild": 7,
    "uniques": [
      "[+15]% Production when constructing [Space] units [in this city]",
      "[2] Sight"
    ],
    "techRequired": "Zero-G Fabrication",
    "terrainsCanBeBuiltOn": [
      "Zero Flux Space",
      "Low Flux Space",
      "Moderate Flux Space"
    ]
  },
  {
    "name": "Solar Reflector",
    "production": 1,
    "turnsToBuild": 7,
    "uniques": [
      "[2] Sight"
    ],
    "terrainsCanBeBuiltOn": [
      "Zero Flux Space",
      "Low Flux Space",
      "Moderate Flux Space"
    ]
  },
  {
    "name": "Particulate Collection Array",
    "production": 3,
    "turnsToBuild": 7,
    "uniques": [
      "[4] Sight"
    ],
    "techRequired": "Pre-Tracting Ionization",
    "terrainsCanBeBuiltOn": [
      "Moderate Flux Space"
    ]
  },
  {
    "name": "Deep Space Radar Array",
    "infrastructure": 3,
    "turnsToBuild": 6,
    "uniques": [
      "[9] Sight"
    ],
    "terrainsCanBeBuiltOn": [
      "Zero Flux Space",
      "Low Flux Space",
      "Moderate Flux Space"
    ]
  }
]```

# jsons/TileResources.json
```json
[
	{
		"name": "Exotic Optomaterial",
		"resourceType": "Strategic",
		"revealedBy": "Athermal Lens",
		"terrainsCanBeFoundOn": [
			"Nebula",
			"Moderate Flux Space"
		],
		"improvedBy": [
			"Particulate Collection Array"
		],
		"majorDepositAmount": {
			"sparse": 5,
			"default": 7,
			"abundant": 9
		},
		"minorDepositAmount": {
			"sparse": 2,
			"default": 3,
			"abundant": 3
		}
	},
	{
		"name": "Uranium",
		"resourceType": "Strategic",
		"terrainsCanBeFoundOn": [
			"NE Ring",
			"SW Ring",
			"Ringed Ice Giant",
			"Ice Giant",
			"Terrestrial Planet",
			"Cragolith Moon"
		],
		"production": 1,
		"improvementStats": {
			"production": 3
		},
		"majorDepositAmount": {
			"sparse": 1,
			"default": 1,
			"abundant": 1
		},
		"minorDepositAmount": {
			"sparse": 1,
			"default": 1,
			"abundant": 1
		}
	},
	{
		"name": "Antimatter",
		"resourceType": "Strategic",
		"terrainsCanBeFoundOn": [
			"Zero Flux Space"
		],
		"improvementStats": {
			"production": 3
		},
		"majorDepositAmount": {
			"sparse": 3,
			"default": 5,
			"abundant": 7
		},
		"minorDepositAmount": {
			"sparse": 1,
			"default": 2,
			"abundant": 3
		}
	}
]```

# jsons/UnitPromotions.json
```json
[
	{
		"name": "1",
		"prerequisites": [],
		"uniques": [
			"[+10]% Strength <when fighting in [Space] tiles>"
		]
	},
	{
		"name": "",
		"prerequisites": [],
		"uniques": [
			"Ignores terrain movement costs"
		]
	},
	{
		"name": "",
		"prerequisites": ["1"],
		"uniques": [
			"[+1] Sight range",
			"[+1] Movement"
		]
	}
]```

# jsons/Units.json
```json
// Todo
//- diverse uniques nearly as a rule rather than exception
//- scout promotions: cheaper, faster, more vision, slightly buffer
//- command ships 
//"Withdraws before melee combat"
//"Unable to capture cities"
//"Unable to pillage tiles"
//"Can move immediately once bought"
//- stealth only countered by scout 
//"Can see invisible [mapUnitFilter] units"
//"Invisible to others"
//- Amphibious
//"All tiles cost 1 movement"
//- Immobile satellite build only civilian, provides sight
//- immobile movement orbital fortress
[
    {
        "name": "Generational Settler",
        "unitType": "Civilian",
        "replaces": "Settler",
        "cost": 200,
        "movement": 2,
        "uniques": [
            "Founds a new city <by consuming this unit>",
            "Requires at least [2] population",
            "Cannot be captured",
            "All tiles cost 1 movement"
        ],
        "obsoleteWith": "Cryogenics"
    },
    {
        "name": "Cryosleep Settler",
        "unitType": "Civilian",
        "cost": 140,
        "movement": 3,
        "requiredTech": "Cryogenics",
        "uniques": [
            "Founds a new city <by consuming this unit>",
            "Cannot be captured",
            "All tiles cost 1 movement"
        ]
    },
    {
        "name": "Incubation Settler",
        "unitType": "Drone",
        "cost": 100,
        "movement": 5,
        "requiredTech": "Artificial Super Intelligence",
        "uniques": [
            "Founds a new city <by consuming this unit>"
        ]
    },
    {
        "name": "Astraforming Swarm",
        "unitType": "Civilian",
        "replaces": "Worker",
        "cost": 30,
        "movement": 4,
        "uniques": [
            "Cannot be captured",
            "Can build [Space] improvements on tiles"
        ]
    },
    {
        "name": "Data Archivist",
        "unitType": "Recon",
        "replaces": "Scout",
        "movement": 3,
        "combatStrength": 5,
        "cost": 20,
        "uniques": [
            "[+1] Sight range",
            "Can enter [Mountain] tiles"
        ]
    },
    {
        "name": "Laser Drone",
        "unitType": "Drone",
        "replaces": "Warrior",
        "strength": 8,
        "rangedStrength": 8,
        "range": 3,
        "movement": 3,
        "cost": 80,
        "upgradesTo": "Laser Corvette",
        "obsoleteWith": "Micro Particulate Shielding"
    },
    {
        "name": "Laser Corvette",
        "unitType": "Military",
        "replaces": "Swordsman",
        "strength": 8,
        "rangedStrength": 8,
        "range": 3,
        "movement": 3,
        "cost": 230,
        "requiredTech": "Micro Particulate Shielding",
        "upgradesTo": "Laser Frigate",
        "obsoleteWith": "Athermal Lens",
        "uniques": [
            "[1] additional attacks per turn",
            "May heal outside of friendly territory"
        ]
    },
    {
        "name": "Laser Frigate",
        "unitType": "Military",
        "replaces": "Longswordsman",
        "strength": 8,
        "rangedStrength": 16,
        "range": 4,
        "movement": 3,
        "cost": 300,
        "upgradesTo": "EM Destroyer",
        "requiredTech": "Athermal Lens",
        "requiredResource": "Exotic Optomaterial",
        "requiredResourceCost": 1,
        "uniques": [
            "+1 Sight",
            "May heal outside of friendly territory"
        ]
    },
    {
        "name": "EM Destroyer",
        "unitType": "Military",
        "replaces": "Musketman",
        "strength": 14,
        "rangedStrength": 18,
        "range": 3,
        "movement": 2,
        "cost": 380,
        "upgradesTo": "Neutron Destroyer",
        "requiredResource": "Uranium",
        "requiredResourceCost": 1,
        "requiredTech": "High Efficiency Fusion",
        "uniques": [
            "+1 Sight",
            "Double movement in [Nebula]",
            "All tiles cost 1 movement",
            "May heal outside of friendly territory"
        ],
        "obsoleteWith": "Directed Plasma"
    },
    {
        "name": "Neutron Destroyer",
        "unitType": "Military",
        "replaces": "Rifleman",
        "strength": 18,
        "rangedStrength": 20,
        "range": 3,
        "movement": 4,
        "cost": 460,
        "upgradesTo": "Annihilation Dreadnaught",
        "requiredResource": "Uranium",
        "requiredResourceCost": 1,
        "requiredTech": "Directed Plasma",
        "uniques": [
            "+2 Sight",
            "May heal outside of friendly territory"
        ],
        "obsoleteWith": "Graviton Manipulation"
    },
    {
        "name": "Annihilation Dreadnaught",
        "unitType": "Military",
        "replaces": "Infantry",
        "strength": 25,
        "rangedStrength": 25,
        "range": 3,
        "movement": 3,
        "cost": 540,
        "upgradesTo": "Warp Dreadnaught",
        "requiredResource": "Antimatter",
        "requiredResourceCost": 1,
        "requiredTech": "Exotic Matter Condenser",
        "obsoleteWith": "Graviton Manipulation",
        "uniques": [
            "+2 Sight",
            "May heal outside of friendly territory"
        ]
    },
    {
        "name": "Warp Dreadnaught",
        "unitType": "Military",
        "replaces": "Mechanized Infantry",
        "strength": 25,
        "rangedStrength": 25,
        "range": 3,
        "movement": 4,
        "cost": 650,
        "requiredTech": "Graviton Manipulation",
        "uniques": [
            "+4 Sight",
            "May heal outside of friendly territory",
            "[1] additional attacks per turn"
        ]
    },
    {
        "name": "Missile",
        "unitType": "Missile",
        "strength": 6,
        "movement": 4,
        "cost": 40,
        "requiredTech": "Expert Systems",
        "obsoleteWith": "Micro Particulate Shielding",
        "uniques": [
            "-1 sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "Destroys tile improvements when attacking",
            //  regular dmg simulates loss of fuel
            "[This Unit] takes [3] damage upon turn end",
            "Self-destructs when attacking",
            "Blast radius [1]"
        ]
    },
    {
        "name": "Shielded Missile",
        "unitType": "Missile",
        "strength": 9,
        "movement": 5,
        "cost": 50,
        "requiredTech": "Micro Particulate Shielding",
        "obsoleteWith": "Laser Propulsion",
        "uniques": [
            "-1 sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "Destroys tile improvements when attacking",
            "[This Unit] takes [2] damage upon turn end",
            "Self-destructs when attacking",
            "Blast radius [1]"
        ]
    },
    {
        "name": "Laser Propelled Missile",
        "unitType": "Missile",
        "strength": 12,
        "movement": 7,
        "cost": 50,
        "requiredTech": "Laser Propulsion",
        "uniques": [
            "-1 sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "Destroys tile improvements when attacking",
            "[This Unit] takes [4] damage upon turn end",
            "Self-destructs when attacking",
            "Blast radius [2]"
        ]
    },
    {
        "name": "Missile Submarine",
        "unitType": "Military",
        "replaces": "Archer",
        "strength": 4,
        "movement": 2,
        "cost": 230,
        "requiredTech": "Expert Systems",
        "upgradesTo": "Missile Cradle",
        "uniques": [
            "+6 Sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "All tiles cost 1 movement",
            "All adjacent units heal [3] HP when healing",
            "Unit will heal every turn, even if it performs an action",
            "Can carry [4] [Missile] units",
            "Cannot attack"
        ],
        "obsoleteWith": "Laser Propulsion"
    },
    {
        "name": "Missile Cradle",
        "unitType": "Military",
        "replaces": "Crossbowman",
        "strength": 5,
        "movement": 1,
        "cost": 300,
        "requiredResource": "Exotic Optomaterial",
        "requiredResourceCost": 1,
        "requiredTech": "Laser Propulsion",
        "upgradesTo": "Strategic Cradle",
        "uniques": [
            "+8 Sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "Can move after attacking",
            "All tiles cost 1 movement",
            "All adjacent units heal [2] HP when healing",
            "Unit will heal every turn, even if it performs an action",
            "Can carry [5] [Missile] units",
            "Cannot attack"
        ]
    },
    {
        "name": "Strategic Cradle",
        "unitType": "Military",
        "replaces": "Gatling Gun",
        "strength": 6,
        "movement": 1,
        "cost": 400,
        "requiredTech": "Strange Battery",
        "upgradesTo": "Cannonade Vessel",
        "uniques": [
            "+10 Sight",
            "May heal outside of friendly territory",
            "No damage penalty for wounded units",
            "Can move after attacking",
            "All tiles cost 1 movement",
            "All adjacent units heal [4] HP when healing",
            "Unit will heal every turn, even if it performs an action",
            "Can carry [7] [Missile] units",
            "Cannot attack"
        ],
        "obsoleteWith": "C-Fractional Thrust"
    },
    {
        "name": "Cannonade Vessel",
        "unitType": "Military",
        "replaces": "Machine Gun",
        "strength": 7,
        "rangedStrength": 13,
        "range": 11,
        "movement": 2,
        "cost": 480,
        "requiredTech": "C-Fractional Thrust",
        "upgradesTo": "Warship",
        "uniques": [
            "+3 Sight",
            "May heal outside of friendly territory",
            "Ranged attacks may be performed over obstacles",
            "No damage penalty for wounded units",
            "All tiles cost 1 movement"
        ]
    },
    {
        "name": "Warship",
        "unitType": "Military",
        "replaces": "Bazooka",
        "strength": 10,
        "rangedStrength": 18,
        "range": 11,
        "movement": 4,
        "cost": 700,
        "requiredResource": "Antimatter",
        "requiredResourceCount": 1,
        "requiredTech": "C-Fractional Thrust",
        "uniques": [
            "+4 Sight",
            "May heal outside of friendly territory",
            "Ranged attacks may be performed over obstacles",
            "[1] additional attacks per turn",
            "No damage penalty for wounded units"
        ]
    },
    {
        "name": "Survey Vessel",
        "unitType": "Civilian",
        "cost": 500,
        "movement": 5,
        "requiredTech": "Graviton Manipulation",
        "uniques": [
            "Only available <in capital>",
            "Requires [Palace]",
            "+4 Sight",
            "All tiles cost 1 movement",
            "Cannot be captured",
            "Safely integrates into [Sector Core Node] <by consuming this unit>"
        ]
    }
]```

# jsons/UnitTypes.json
```json
[
    {
        "name": "Civilian",
        "movementType": "space"
    },
    {
        "name": "Drone",
        "movementType": "space"
    },
    {
        "name": "Missile",
        "movementType": "space"
    },
    {
        "name": "Military",
        "movementType": "space"
    }
]```

# jsons/VictoryTypes.json
```json
[
    {
        "name": "Domination",
        "victoryString": "You have eradicated all rival factions and united the sector under your supreme rule!",
        "milestones": [
            "Control all original Homeworlds"
        ]
    },
    {
        "name": "Scientific",
        "victoryString": "By networking a Type-II Dyson Assembly across the sector, your civilization ascends to transcendent digital omniscience!",
        "milestones": [
            "Research [Graviton Manipulation]",
            "Construct [3] Sector Core Node buildings",
            "Launch and dock [3] [Survey Vessel] units to [Sector Core Node] buildings"
        ]
    }
]```

