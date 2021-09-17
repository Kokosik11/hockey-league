console.log('hello, world!');

const postBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadaBox = document.getElementById('loading-box')
let visible = 3

const handleGetData = () => {
  $.ajax({
    type: 'GET',
    url: `/posts-json/${visible}/`,
    success: function(response){
      // console.log(response.max)
      max_size = response.max
      const data = response.data
      spinnerBox.classList.remove('not-visible')
      setTimeout(()=>{
        spinnerBox.classList.add('not-visible')
        data.map(post=>{
          postBox.innerHTML += `<div class="news-block" id="posts-box">
                                  <img src="pictures/${post.image}" alt="news photo">
                                  <div><span><a href="/posts/${post.slug}" id="more">Читать</a></span></div>
                                  <h3 class="news-heading">${post.title}</h3>
                                </div>`
        })
      }, 500)
      if(max_size){
        console.log('done');
      }
    },
    error: function(error){
      console.log(error);
    }
  })
}

handleGetData()

loadBtn.addEventListener('click', ()=>{
  visible += 3
  handleGetData()
})