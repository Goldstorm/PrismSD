'use strict';

exports.BattlePokedex = {
	rotomheat: {
		inherit: true,
		types: ["Electric", "Ghost"],
	},
	rotomwash: {
		inherit: true,
		types: ["Electric", "Ghost"],
	},
	rotomfrost: {
		inherit: true,
		types: ["Electric", "Ghost"],
	},
	rotomfan: {
		inherit: true,
		types: ["Electric", "Ghost"],
	},
	rotommow: {
		inherit: true,
		types: ["Electric", "Ghost"],
	},
	gengar: {
		inherit: true,
		types: ["Ghost", "Gas"],
	},
	porygonz: {
		inherit: true,
		types: ["Sound"],
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
};
