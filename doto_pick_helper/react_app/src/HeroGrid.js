import React, { useState } from 'react';
import './HeroGrid.css';

function HeroGrid() {
    const heroes = [
        "abaddon",
        "alchemist",
        "ancient-apparition",
        "anti-mage",
        "arc-warden",
        "axe",
        "bane",
        "batrider",
        "beastmaster",
        "bloodseeker",
        "bounty-hunter",
        "brewmaster",
        "bristleback",
        "broodmother",
        "centaur-warrunner",
        "chaos-knight",
        "chen",
        "clinkz",
        "clockwerk",
        "crystal-maiden",
        "dark-seer",
        "dark-willow",
        "dawnbreaker",
        "dazzle",
        "death-prophet",
        "disruptor",
        "doom",
        "dragon-knight",
        "drow-ranger",
        "earth-spirit",
        "earthshaker",
        "elder-titan",
        "ember-spirit",
        "enchantress",
        "enigma",
        "faceless-void",
        "grimstroke",
        "gyrocopter",
        "hoodwink",
        "huskar",
        "invoker",
        "io",
        "jakiro",
        "juggernaut",
        "keeper-of-the-light",
        "kunkka",
        "legion-commander",
        "leshrac",
        "lich",
        "lifestealer",
        "lina",
        "lion",
        "lone-druid",
        "luna",
        "lycan",
        "magnus",
        "marci",
        "mars",
        "medusa",
        "meepo",
        "mirana",
        "monkey-king",
        "morphling",
        "muerta",
        "naga-siren",
        "natures-prophet",
        "necrophos",
        "night-stalker",
        "nyx-assassin",
        "ogre-magi",
        "omniknight",
        "oracle",
        "outworld-destroyer",
        "pangolier",
        "phantom-assassin",
        "phantom-lancer",
        "phoenix",
        "primal-beast",
        "puck",
        "pudge",
        "pugna",
        "queen-of-pain",
        "razor",
        "riki",
        "rubick",
        "sand-king",
        "shadow-demon",
        "shadow-fiend",
        "shadow-shaman",
        "silencer",
        "skywrath-mage",
        "slardar",
        "slark",
        "snapfire",
        "sniper",
        "spectre",
        "spirit-breaker",
        "storm-spirit",
        "sven",
        "techies",
        "templar-assassin",
        "terrorblade",
        "tidehunter",
        "timbersaw",
        "tinker",
        "tiny",
        "treant-protector",
        "troll-warlord",
        "tusk",
        "underlord",
        "undying",
        "ursa",
        "vengeful-spirit",
        "venomancer",
        "viper",
        "visage",
        "void-spirit",
        "warlock",
        "weaver",
        "windranger",
        "winter-wyvern",
        "witch-doctor",
        "wraith-king",
        "zeus"
    ];

    const [selectedHeroes, setSelectedHeroes] = useState([]);
    const [recommendations, setRecommendations] = useState([]);
    const [showRecommendations, setShowRecommendations] = useState(false);

    const handleHeroClick = (hero) => {
        if (selectedHeroes.includes(hero)) {
            setSelectedHeroes(selectedHeroes.filter((selectedHero) => selectedHero !== hero));
        } else {
            setSelectedHeroes([...selectedHeroes, hero]);
        }
    };

    const handleConfirmationClick = () => {
        if (selectedHeroes.length < 1 || selectedHeroes.length > 5) {
            alert('Выберите от 1 до 5 героев для отправки.');
            return;
        }

        const selectedHeroNames = selectedHeroes.join(',');

        // Отправка POST запроса на API бэкенда
        fetch('http://127.0.0.1:8000/api/dota2recommendations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ heroes: selectedHeroNames }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
                setRecommendations(data.recommendations);
                setShowRecommendations(true); // Show recommendations after fetching
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    };

    const renderHeroes = () => (
        <div className="hero-grid">
            {heroes.map(hero => (
                <div
                    key={hero}
                    onClick={() => handleHeroClick(hero)}
                    className={`hero ${selectedHeroes.includes(hero) ? 'selected' : ''}`}
                >
                    <img src={`/icons/${hero}.jpg`} alt={hero} />
                    <span>{hero}</span>
                </div>
            ))}
            <div className="scroll-button" onClick={handleConfirmationClick}>Подтвердить выбор</div>
        </div>
    );

    const renderRecommendations = () => (
        <div className="recommended-heroes">
            {recommendations.map((heroData, index) => (
                <div key={index} className="hero">
                    <img src={`/icons/${heroData[0]}.jpg`} alt={heroData[0]} />
                    <span>{heroData[0]}</span>
                    <span>Recommendation Score: {heroData[1]}</span> {/* Отобразите оценку рекомендации */}
                </div>
            ))}
        </div>
    );

    return (
        <div>
            {showRecommendations ? renderRecommendations() : renderHeroes()}
        </div>
    );
}

export default HeroGrid;
