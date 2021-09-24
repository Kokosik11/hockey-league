const teams = document.querySelectorAll('.stats-table .teamlist-row');

fetch(`/api/matches`)
    .then(response => response.ok ? response : Promise.reject(response))
    .then(response => response.json())
    .then(data => {
        console.log(data);
    
        teams.forEach(team => {
            let teamObj = {
                name: team.querySelector('.team-name').textContent,
                matches: team.querySelector('.match-count'),
                wins: team.querySelector('.match-wins'),
                loses: team.querySelector('.match-lose'),
                score: team.querySelector('.team-score'),
                draw: team.querySelector('.team-draw'),
                goals: team.querySelector('.team-goals'),
                miss: team.querySelector('.team-miss'),
            }

            team.querySelector('.match-count').innerHTML = 0
            team.querySelector('.match-wins').innerHTML = 0
            team.querySelector('.match-lose').innerHTML = 0
            team.querySelector('.team-score').innerHTML = 0
            team.querySelector('.team-goals').innerHTML = 0
            team.querySelector('.team-miss').innerHTML = 0

            data.forEach(datateam => {
                let teamStatistic = {
                    matches: +teamObj.matches.innerHTML,
                    wins: +teamObj.wins.innerHTML,
                    loses: +teamObj.loses.innerHTML,
                    winScore: 0,
                    drawScore: +teamObj.draw.innerHTML,
                    score: +teamObj.score.innerHTML,
                    goals: +teamObj.goals.innerHTML,
                    miss: +teamObj.miss.innerHTML
                }

                if(datateam.first_team.name == teamObj.name) {
                    // Total matches for team
                    teamStatistic.matches += 1,
                    teamObj.matches.innerHTML = teamStatistic.matches;

                    // Total wins for team
                    teamStatistic.wins += datateam.score_hometeam > datateam.score_awayteam ? 1 : 0
                    teamObj.wins.innerHTML = teamStatistic.wins;

                    // Total loses for team
                    teamStatistic.loses += datateam.score_hometeam < datateam.score_awayteam ? 1 : 0; 
                    teamObj.loses.innerHTML = teamStatistic.loses;

                    // Total scores for team 
                

                    // Total goals for team
                    teamStatistic.goals += datateam.score_hometeam;
                    teamObj.goals.innerHTML = teamStatistic.goals;

                    // Total misses for team
                    teamStatistic.miss += datateam.score_awayteam;
                    teamObj.miss.innerHTML = teamStatistic.miss;

                }

                if(datateam.second_team.name == teamObj.name) {
                    // Total matches for team
                    teamStatistic.matches += 1,
                    teamObj.matches.innerHTML = teamStatistic.matches;

                    // Total wins for team
                    teamStatistic.wins += datateam.score_awayteam > datateam.score_hometeam ? 1 : 0; 
                    teamObj.wins.innerHTML = teamStatistic.wins;

                    // Total loses for team
                    teamStatistic.loses += datateam.score_awayteam < datateam.score_hometeam ? 1 : 0; 
                    teamObj.loses.innerHTML = teamStatistic.loses;

                    // Total scores for team 


                    // Total goals for team
                    teamStatistic.goals += datateam.score_awayteam;
                    teamObj.goals.innerHTML = teamStatistic.goals;

                    // Total misses for team
                    teamStatistic.miss += datateam.score_hometeam;
                    teamObj.miss.innerHTML = teamStatistic.miss;
                }

                teamStatistic.drawScore = +teamObj.draw.innerHTML + (datateam.score_hometeam == datateam.score_awayteam ? 1 : 0);
                teamObj.draw.innerHTML = teamStatistic.drawScore;

                teamObj.score.innerHTML = (+teamObj.wins.innerHTML * 3) + teamStatistic.drawScore;
            })
        })
    })
    .then(data => {
        let tableBody = document.querySelector(".stats-table tbody");
        let itemList = [];
        teams.forEach(team => {
            itemList.push(team)
        })
        itemList.sort((a, b) => { 
            let firstTeam = a.querySelector(".team-score").textContent;
            let secondTeam = b.querySelector(".team-score").textContent;
            let numA = parseInt(firstTeam);
            let numB = parseInt(secondTeam);
            if(numA < numB) return -1;
            if(numA > numB) return 1;
            return 0;
        })
        .reverse()
        .forEach(function(node) {
            tableBody.appendChild(node)
        });

        // tableBody.innerHTML = ""
        // tableBody.innerHTML = teams
    })