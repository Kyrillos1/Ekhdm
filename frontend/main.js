let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///C:/Users/Dennis%20Ivy/Desktop/frontend/login.html'
})



let demomethodsUrl = 'http://127.0.0.1:8000/api/demomethods/'

let getDemomethods = () => {

    fetch(demomethodsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            buildDemomethods(data)
        })

}

let buildDemomethods = (demomethods) => {
    let demomethodsWrapper = document.getElementById('demomethods--wrapper')
    demomethodsWrapper.innerHTML = ''
    for (let i = 0; demomethods.length > i; i++) {
        let demomethod = demomethods[i]

        let demomethodCard = `
                <div class="demomethod--card">
                    <img src="http://127.0.0.1:8000${demomethod.featured_image}" />
                    
                    <div>
                        <div class="card--header">
                            <h3>${demomethod.title}</h3>
                            <strong class="vote--option" data-vote="up" data-demomethod="${demomethod.id}" >&#43;</strong>
                            <strong class="vote--option" data-vote="down" data-demomethod="${demomethod.id}"  >&#8722;</strong>
                        </div>
                        <i>${demomethod.vote_ratio}% Positive feedback </i>
                        <p>${demomethod.description.substring(0, 150)}</p>
                    </div>
                
                </div>
        `
        demomethodsWrapper.innerHTML += demomethodCard
    }

    addVoteEvents()

    //Add an listener
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')

    for (let i = 0; voteBtns.length > i; i++) {

        voteBtns[i].addEventListener('click', (e) => {
            let token = localStorage.getItem('token')
            console.log('TOKEN:', token)
            let vote = e.target.dataset.vote
            let demomethod = e.target.dataset.demomethod

            fetch(`http://127.0.0.1:8000/api/demomethods/${demomethod}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({ 'value': vote })
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data)
                    getDemomethods()
                })

        })
    }
}


getDemomethods()