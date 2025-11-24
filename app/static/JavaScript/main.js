const positions = {
    berserk: [
        { left: -140, top: -50 },
        { left: 180, top: -50 },
        { left: 0, top: -130 }
    ],
    gachiakuta: [
        { left: -120, top: -40 },
        { left: 180, top: -125 },
        { left: 100, top: 20 }
    ],
    gto:
    [
        { left: -180, top: -20 },
        { left: 150, top: -50 },
        { left: 0, top: -150 }
    ],
    demon_slayer: [
        { left: -110, top: -40 },
        { left: 150, top: 0 },
        { left: 200, top: -120 }
    ],
    solo_leveling: [
        { left: -110, top: -20 },
        { left: 160, top: -100 },
        { left: 30, top: 20 }
    ],
    bungou_stray_dogs: [
        { left: 190, top: 10 },
        { left: 40, top: -100 },
        { left: 370, top: -100 }
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