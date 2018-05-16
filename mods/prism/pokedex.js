'use strict';

exports.BattlePokedex = {
	gengar: {
		inherit: true,
		types: ["Ghost", "Gas"],
	},
	haunter: {
		inherit: true,
		types: ["Ghost", "Gas"],
	},
	gastly: {
		inherit: true,
		types: ["Ghost", "Gas"],
	},	
	torkoal: {
                inherit: true,
                types: ["Fire", "Gas"],
	},
	koffing: {
                inherit: true,
                types: ["Poison", "Gas"],
	},
	weezing: {
                inherit: true,
                types: ["Poison", "Gas"],
	},		
	porygonz: {
		inherit: true,
		types: ["Sound"],
	},
	igglybuff: {
	        inherit: true,
		types: [Sound", "Normal"],
	},	
	jigglypuff: {
	        inherit: true,
		types: ["Sound", "Fairy"],
	},
	wigglytuff: {
	        inherit: true,
		types: ["Sound", "Fairy"],
	},
	whismur: {
	        inherit: true,
		types: ["Sound"],
	},
	loudred: {
	        inherit: true,
		types: ["Sound"],
	},
	exploud: {
	        inherit: true,
		types: ["Sound"],
	},
	chingling: {
	        inherit: true,
		types: ["Sound", "Psychic"],
	},
	chimecho: {
	        inherit: true,
		types: ["Sound", "Psychic"],
	},		
	azumarill: {
		inherit: true,
		types: ["Fairy", "Water"],
	},	
	sylveon: {
		species: "Sylveon",
		types: ["Fairy"],
		genderRatio: {M: 0.875, F: 0.125},
		baseStats: {hp: 95, atk: 65, def: 65, spa: 110, spd: 130, spe: 60},
		abilities: {0: "Cute Charm", H: "Pixilate"},
		heightm: 1,
		weightkg: 23.5,
		color: "Pink",
		prevo: "eevee",
		evoLevel: 2,
		eggGroups: ["Field"],
	},
	fambaco : {
		species: "Fambaco",
		types: ["Ghost", "Fighting],
		genderRatio: {M: 0, F: 0},
		baseStats: {hp: 100, atk: 100, def: 100, spa: 100, spd: 125, spe: 125},
		abilities: {0: "Naljo Fury", H: "Naljo Fury"},
		heightm: 1,
		weightkg: 23.5,
		color: "White",
		eggGroups: ["None"]
};
