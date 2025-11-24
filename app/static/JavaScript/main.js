const positions = {
    berserk: [
        { left: -140, top: -50 },
        { left: 180, top: -50 },
        { left: 0, top: -130 }
    ],
    gachiakuta: [
        { left: -120, top: -40 },
        { left: 180, top: -125 },
        { left: 70, top: 20 }
    ],
    gto:
    [
        { left: -180, top: 0 },
        { left: 150, top: -50 },
        { left: 0, top: 150 }
    ],
    demon_slayer: [
        { left: -150, top: 0 },
        { left: 150, top: 0 },
        { left: 0, top: 150 }
    ],
    solo_leveling: [
        { left: -130, top: -30 },
        { left: 160, top: -70 },
        { left: 0, top: 130 }
    ],
    bungou_stray_dogs: [
        { left: -160, top: -20 },
        { left: 140, top: -80 },
        { left: 0, top: 140 }
    ]
};

const items = document.querySelectorAll('.item');

items.forEach(item => {
    const anime = item.dataset.anime;
    const gifContainer = item.querySelector('.gif-container');
    const gifs = gifContainer.querySelectorAll('img');

    item.addEventListener('mouseenter', () => {
        const pos = positions[anime];

        gifs.forEach((img, i) => {
            img.style.left = pos[i].left + "px";
            img.style.top = pos[i].top + "px";
            img.style.opacity = "1";
        });
    });

    item.addEventListener('mouseleave', () => {
        gifs.forEach(img => {
            img.style.opacity = "0";
        });
    });
});