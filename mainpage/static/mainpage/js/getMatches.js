Date.prototype.daysInMonth = function() {
    return 32 - new Date(this.getFullYear(), this.getMonth(), 32).getDate();
};

const date = new Date();
date.setMonth(date.getMonth(), 1);

const renderMonth = (month) => {
    const months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"];
    const monthDOM = document.querySelector('.month');

    // console.log(date)

    monthDOM.innerHTML = `${months[month]}, ${date.getFullYear()}`;
    // getCeils(date);
}

const arrows = document.querySelectorAll('.arrow');

renderMonth(date.getMonth());

arrows.forEach(arrow => {
    arrow.onclick = () => {
        date.setMonth(date.getMonth() + +arrow.dataset.direction, 1);
        renderMonth(date.getMonth());
        getCeils();
    }
})

const renderCeils = (ceils) => {
    const ceilsDOM = document.querySelector('.ceils-content');
    ceilsDOM.innerHTML = "";

    ceils.forEach(ceil => {
        if(ceil.teams) {
            console.log(ceil.teams)
            let ceilDOM = `<div class="date">
                <span class="day">${ceil.day}</span>
                <span class="date-content">
                <a href="teams/profile/${ceil.teams[0].slug}"><img src="${ceil.teams[0].logo}"></a>
                <a href="teams/profile/${ceil.teams[1].slug}"><img src="${ceil.teams[1].logo}"></a>
                </span>
                </div>`
            ceilsDOM.innerHTML += ceilDOM;
        } 
        else {
            let ceilDOM = `<div class="date"><span class="day">${ceil.day}</span><span class="date-content"></span></div>`
            ceilsDOM.innerHTML += ceilDOM;
        }
    })
}

const getCeils = () => {
    fetch(`/api/matches`)
        .then(response => response.ok ? response : Promise.reject(response))
        .then(response => response.json()) // или как текст `response.text()`
        .then(json => {
            console.log(json)

            let ceils = [];
                    
            for(let i = 0; i < date.daysInMonth(); i++) {
                ceils.push( { day: i + 1 });
            }

            json.forEach(data => {
                let _date = new Date(data.date);
                
                if(_date.getMonth() === date.getMonth() && _date.getFullYear() === date.getFullYear()) {
                    console.log(true);

                    ceils.forEach((ceil, index) => {
                        if(ceil.day == _date.getDate()) {
                            ceils[index] = { day: index + 1, teams: [data.first_team, data.second_team] };
                        }
                    })
                    console.log(ceils)

                }
            })

            ceils = new Set(ceils);
            renderCeils(ceils);

            // let newDate = new Date(json[0].date)

            // console.log(newDate.getMonth());

            // 

            // if(!json.err) {
            //     json.forEach(j => {
            //         for(i = 0; i < ceils.length; i++) {
            //             if(j.matchDate.day == ceils[i].day) {
            //                 ceils[i] = { day: i + 1, teams: [...j.teams] };
            //             }
            //         }
            //     })
            // }
            // ceils = new Set(ceils);
            // console.log(ceils)
            // renderCeils(ceils);
        })
}

getCeils();
