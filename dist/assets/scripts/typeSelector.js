const types = document.querySelectorAll('.player-type');
const tables = document.querySelectorAll('.table');
const line = document.querySelector('.line');

const pos = ["40px", "40px + 20%", "30px + 40%", "20px + 60%", "80% - 5px"];

types.forEach((type, index) => {
    type.onclick = () => {
        types.forEach(t => {
            t.classList.remove("active");
        })

        tables.forEach(table => {
            table.classList.remove("active-table");
        })

        tables[index].classList.add("active-table");

        console.log(`Index: ${index} - Pos: ${pos[index]}`)

        type.classList.add("active");
        line.style.left = `calc(${pos[index]})`;
    }
})