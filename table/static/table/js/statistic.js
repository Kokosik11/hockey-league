const teams = document.querySelectorAll('.stats-table .teamlist-row');

fetch(`/api/matches`)
    .then(response => response.ok ? response : Promise.reject(response))
    .then(response => response.json())
    .then(data => {
        console.log(data);

        let teamList = [];

        data.forEach(__team => {
            teamList.push({ 
                name: __team.first_team.name, 
                matches: 0,
                wins: 0,
                loses: 0,
                scores: 0,
                goals: 0,
                misses: 0,
            })
            teamList.push({ 
                name: __team.second_team.name, 
                matches: 0,
                wins: 0,
                loses: 0,
                scores: 0,
                goals: 0,
                misses: 0,
            })
        })

        const filteredStrings = teamList.filter((thing, index, self) =>
            index === self.findIndex((t) => (
                t.place === thing.place && t.name === thing.name
            ))
        )

        data.forEach(__team => {
            filteredStrings.forEach(team => {
                if(team.name === __team.first_team.name) {
                    team.matches += 1;
                    team.wins += __team.score_hometeam > __team.score_awayteam ? 1 : 0;
                    team.loses += __team.score_hometeam < __team.score_awayteam ? 1 : 0;
                    team.scores += __team.score_hometeam > __team.score_awayteam ? 2 : 0;
                    team.scores += __team.score_hometeam < __team.score_awayteam && __team.is_overtime ? 1 : 0;
                    team.goals += __team.score_hometeam;
                    team.misses += __team.score_awayteam;
                }
                else if(team.name === __team.second_team.name) {
                    team.matches += 1;
                    team.wins += __team.score_hometeam < __team.score_awayteam ? 1 : 0;
                    team.loses += __team.score_hometeam > __team.score_awayteam ? 1 : 0;
                    team.scores += __team.score_hometeam < __team.score_awayteam ? 2 : 0;
                    team.scores += __team.score_hometeam > __team.score_awayteam && __team.is_overtime ? 1 : 0;
                    team.goals += __team.score_awayteam;
                    team.misses += __team.score_hometeam;
                }
            })
        })

        teams.forEach(team => {
            filteredStrings.forEach(__team => {
                if(team.querySelector(".team-name").textContent == __team.name) {
                    team.querySelector(".match-count").innerHTML = __team.matches;
                    team.querySelector(".match-wins").innerHTML = __team.wins;
                    team.querySelector(".match-lose").innerHTML = __team.loses;
                    team.querySelector(".team-score").innerHTML = __team.scores;
                    team.querySelector(".team-goals").innerHTML = __team.goals;
                    team.querySelector(".team-miss").innerHTML = __team.misses;
                }
            })
        })

        console.log(filteredStrings);

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