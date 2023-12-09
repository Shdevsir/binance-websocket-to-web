const myButton = document.querySelector("button");
const myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
  }

if (!localStorage.getItem("name")) {
    setUserName();
} else {
    const storedName = localStorage.getItem("name");
    myHeading.textContent = `Mozilla is cool, ${storedName}`;
}

myButton.onclick = () => {
    setUserName();
  };

const mainDiv = document.createElement('div');
mainDiv.id = 'mainDiv';
function createBlock() {
    const n = 8;

    for(let i = 0; i < n; i ++) {
        mainDiv.appendChild(createMiniBlocks());
    }

    document.body.appendChild(mainDiv)
}

function createMiniBlocks() {
    const n = 5;
    const div = document.createElement('div')
    for(let i = 0; i < n; i ++) {
        const ifame = document.createElement('div');
        ifame.innerHTML = '<iframe width="76" height="76" src="https://www.youtube.com/embed/glGaHATSfkU?si=8YqwShMl-aSDea6C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;" allowfullscreen></iframe>';
        div.appendChild(ifame);
        div.classList.add('video')
    }

    return div;
}

createBlock()