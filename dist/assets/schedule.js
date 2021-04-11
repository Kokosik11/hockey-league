class Schedule {
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"];
    date = new Date();
    month = this.date.getMonth();

    renderMonth = (value) => {
        let monthDOM = document.querySelector('.month');
        monthDOM.innerHTML = this.months[value];
    }

    onArrowClick = () => {
        const arrowLeft = document.querySelector('.arrow-left');
        const arrowRight = document.querySelector('.arrow-right');

        arrowLeft.addEventListener("click", () => {
            if(this.month == 0) { 
                this.month = 11;
                this.renderMonth(this.month);
            }
            else {
                this.renderMonth(--this.month);
            }
        })

        arrowRight.addEventListener("click", () => {
            if(this.month == 11) {
                this.month = 0;
                this.renderMonth(this.month);
            }
            else {
                this.renderMonth(++this.month);
            }
        })
    }

    constructor() {
        this.renderMonth(this.month);
        this.onArrowClick();
    }

}

let schedule = new Schedule();