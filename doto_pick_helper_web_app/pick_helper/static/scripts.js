document.addEventListener('DOMContentLoaded', function () {
    const heroGrid = document.getElementById('hero-grid');
    const confirmButton = document.getElementById('confirm-button');
    let selectedHeroes = [];

    heroGrid.addEventListener('click', function (event) {
        console.log('heroGrid clicked');
        if (event.target.closest('.hero')) {
            const hero = event.target.closest('.hero');
            const name = hero.getAttribute('data-name');

            if (hero.classList.contains('selected')) {
                hero.classList.remove('selected');
                const index = selectedHeroes.indexOf(name);
                if (index > -1) {
                    selectedHeroes.splice(index, 1);
                }
            } else if (selectedHeroes.length < 5) {
                hero.classList.add('selected');
                selectedHeroes.push(name);
            }

            // Обновление состояния кнопки "ОК"
            if (selectedHeroes.length > 0 && selectedHeroes.length <= 5) {
                confirmButton.removeAttribute('disabled');
                confirmButton.classList.add('enabled');
            } else {
                confirmButton.setAttribute('disabled', 'true');
                confirmButton.classList.remove('enabled');
            }
        }
    });

    confirmButton.addEventListener('click', function () {
        console.log('Confirm button clicked');
        if (selectedHeroes.length > 0 && selectedHeroes.length <= 5) {
            // Здесь отправляем выбранных героев на сервер
        }
    });
});
