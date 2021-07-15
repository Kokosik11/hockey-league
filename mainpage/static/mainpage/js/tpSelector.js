const selectionBtn = document.querySelectorAll(".selection-btn");
const switchTable = document.querySelectorAll(".switch-table");

selectionBtn.forEach(btn => {
    btn.onclick = () => {
        selectionBtn.forEach(b => b.classList.remove("btn-active"));
        switchTable.forEach(st => st.style.display = "none" );

        const table = document.querySelector(`.switch-table[data-id="${btn.dataset.id}"]`);
        table.style.display = "block";
        btn.classList.add("btn-active");
    }
});