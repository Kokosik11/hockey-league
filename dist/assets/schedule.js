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
        _tmpDate.setDate(1);

        let _tmpPrevMonth = new Date();
        _tmpPrevMonth.setMonth(date.getMonth() - 1);
        _tmpPrevMonth.setDate(_tmpPrevMonth.daysInMonth() - _tmpPrevMonth.getDay());

        // console.log(_tmpPrevMonth.daysInMonth() - _tmpPrevMonth.getDate());

        if(_tmpPrevMonth.getDay != 0) {
            let _tmpDatePrevMonth = [];
            for(let i = 0; i < _tmpPrevMonth.daysInMonth() - _tmpPrevMonth.getDate(); i++) {
                let _tmpDayPrevMonth = new Date(_tmpPrevMonth);
                _tmpDayPrevMonth.setDate(_tmpDayPrevMonth.getDate() + i);
                _tmpDatePrevMonth[i] = {date: new Date(_tmpDayPrevMonth), content: []};
            }    
            scheduleDates.unshift(..._tmpDatePrevMonth);
        }

        let _tmpNextMonth = new Date();
        _tmpNextMonth.setDate(date.daysInMonth());
        if(_tmpNextMonth.getDay != 0) {
            _tmpNextMonth.setMonth(date.getMonth() + 1);
            _tmpNextMonth.setDate(1);
            console.log(_tmpNextMonth.getDay());

            for(let i = _tmpNextMonth.getDay(); i < 7; i++) {
                let _tmpDayNextMonth = new Date(_tmpNextMonth);

                _tmpDayNextMonth.setDate(i);

                scheduleDates.push({ date: new Date(_tmpDayNextMonth), content: []});
            }
        }

        console.log(scheduleDates);
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
            })
        })
    }

    constructor() {
        this.renderMonth(this.month);
        this.onArrowClick();
        let month = new Date();
        month.setMonth(this.months.indexOf(this.months[4]));
        this.getTableCeils();
    }

}

let schedule = new Schedule();