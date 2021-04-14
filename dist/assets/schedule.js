Date.prototype.daysInMonth = function() {
    return 32 - new Date(this.getFullYear(), this.getMonth(), 32).getDate();
};

class Schedule {
    months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"];
    date = new Date();
    month = this.date.getMonth();

    renderMonth = (value) => {
        let monthDOM = document.querySelector('.month');
        monthDOM.innerHTML = this.months[value];
    }

    getPrevMonth = (date) => {
        let prevMonthDays = [];
        let _tmpDate = new Date(date);
        _tmpDate.setMonth(date.getMonth() - 1);
        _tmpDate.setDate(_tmpDate.daysInMonth());

        _tmpDate.setDate(_tmpDate.daysInMonth() - _tmpDate.getDay() + 1);
        
        console.log(_tmpDate.daysInMonth() - _tmpDate.getDate());

        let days = _tmpDate.getDate();
        for(let i = 0; i < _tmpDate.daysInMonth() - days; i++) {
            console.log(_tmpDate);

            let _tmpMonth = { date: new Date(_tmpDate), content: []};
            _tmpDate.setDate(_tmpDate.getDate() + 1);
            prevMonthDays[i] = _tmpMonth;
        }

        if(prevMonthDays.length > 0 && prevMonthDays[prevMonthDays.length - 1].date.getDay() !== _tmpDate.daysInMonth() 
            || prevMonthDays.length === 0); 
        {
            _tmpDate.setDate(_tmpDate.getDate());
            let _tmpMonth = { date: new Date(_tmpDate), content: []};
            prevMonthDays.push(_tmpMonth);
        }
        console.log(prevMonthDays);
    }

    getNextMonth = (date) => {}

    getTableCeils = (date = this.date) => {
        let _tmpDate = new Date();
        _tmpDate.setMonth(date.getMonth());
        _tmpDate.setFullYear(date.getFullYear())
        _tmpDate.setDate(1);

        let scheduleDates = [];

        for(let i = 0; i < _tmpDate.daysInMonth(); i++) {
            _tmpDate.setDate(i+1);
            scheduleDates[i] = { date: new Date(_tmpDate), content: [] };
        }
        console.log(scheduleDates)

        date.setDate(1);

        if(date.getDay() !== 1) this.getPrevMonth(date);
    }

    onArrowClick = () => {
        const arrows = document.querySelectorAll('.arrow');

        arrows.forEach(arrow => {
            arrow.addEventListener("click", e => {
                let _tmpMonth = 0;

                if(arrow.dataset.direction === 'right') _tmpMonth++;
                else if(arrow.dataset.direction === 'left') _tmpMonth--;

                this.month += _tmpMonth;
                this.month = this.month === -1?11:this.month === 12?0:this.month;
                this.renderMonth(this.month);

                let tmpDate = new Date();
                tmpDate.setMonth(this.month);
                this.getTableCeils(tmpDate);
            })
        })
    }

    constructor() {
        this.renderMonth(this.month);
        this.onArrowClick();
        let month = new Date();
        month.setMonth(this.months.indexOf(this.months[3]));
        this.getTableCeils(month);
    }

}

let schedule = new Schedule();