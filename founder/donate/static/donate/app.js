window.onbeforeunload = function () {
  window.scrollTo(0, 0);
}

window.addEventListener("hashchange", function(e){
    e.preventDefault()
    let navHeight = document.getElementById("nav").offsetHeight
    const newNavHeight = navHeight + 100
    const target = document.getElementById(window.location.hash.substring(1))
    window.scrollTo(0, target.offsetTop - newNavHeight)
})