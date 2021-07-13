Date.prototype.daysInMonth = function() {
  return 32 - new Date(this.getFullYear(), this.getMonth(), 32).getDate();
};

class Schedule {
  months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"];
  date = new Date();
  month = this.date.getMonth();
  days = [];

  setHeading = (DOMElement = this.DOMMonth) => {
      let tmpMonth = new Date();
      tmpMonth.setMonth(this.months.indexOf(this.months[this.month]));
      DOMElement.innerHTML = `${this.months[this.month]}, ${this.date.getFullYear()}`;
      console.log(this.date);
      console.log(this.month);
  }

  renderMonth = () => {
      this.getMonths();

      const ceilDOM = document.querySelector(".ceils-content");
      ceilDOM.innerHTML = "";
      for(let i = 0; i < this.date.daysInMonth(); i++) {
          let ceil = `<div class="date"><span class="day">${this.days[i].date.getDate()}</span><span class="date-content"></span></div>`
          ceilDOM.innerHTML += ceil;
      }

  }

  getMonths = () => {
      this.days = [];
      this.date.setDate(1);

      for(let i = 0; i < this.date.daysInMonth(); i++) {
          let _tmpMonth = new Date(this.date);
          _tmpMonth.setDate(i + 1);
          this.days[i] = { date: _tmpMonth, content: [] };
      }

      // console.log(this.days);
  }

  switchMonth = () => {
      const arrows = document.querySelectorAll(".arrow");
      this.renderMonth();

      arrows.forEach(arrow => {
          arrow.addEventListener("click", e => {                
              if(+arrow.dataset.direction === 1 && this.month === 11) this.date.setFullYear(this.date.getFullYear() + 1);
              if(+arrow.dataset.direction === -1 && this.month === 0) this.date.setFullYear(this.date.getFullYear() - 1);

              this.month += +arrow.dataset.direction;

              this.month = this.month === -1?11:this.month === 12?0:this.month;
              this.date.setMonth(this.month);
              this.setHeading();
              this.renderMonth();

          })
      })
  }

  constructor(DOMMonth) {
      this.DOMMonth = document.querySelector(DOMMonth);
      this.setHeading();
      this.switchMonth();
  }
}

let schedule = new Schedule(".month");