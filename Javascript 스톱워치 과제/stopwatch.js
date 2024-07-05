// interval을 설정하기 위한 변수
let intervalState;
let second = 0;
let millisecond = 0;
// 스탑워치가 stop이거나 reset일 때 true
let stopWatchState = false;
// <div class="time"></div>
const timeContainer = document.querySelector('.time');
// <p class="second"></p>
const secondText = document.createElement('p');
secondText.className = 'second';
secondText.innerText = '00';
// <p></p>
let textNode = document.createTextNode(':');
// <p class="millisecond"></p>
const millisecondText = document.createElement('p');
millisecondText.className = 'millisecond';
millisecondText.innerText = '00';

const startBtn = document.getElementById('start');
startBtn.addEventListener("click", () => {
   if (stopWatchState == false) {
      console.log("pushed start!!");
      intervalState = setInterval(startTimer, 10);
      stopWatchState = true;
   }
})

const stopBtn = document.getElementById('stop');
stopBtn.addEventListener("click", () => {
   console.log("pushed stop!!");
   clearInterval(intervalState);
   stopWatchState = false;
})

const resetBtn = document.getElementById('reset');
resetBtn.addEventListener("click", () => {
   console.log("pushed reset!!");
   clearInterval(intervalState);
   millisecond = 0;
   millisecondText.innerText = '00';
   second = 0;
   secondText.innerText = '00';
   stopWatchState = false;
})

function startTimer() {
   millisecond++;
   if (millisecond <= 9) {
      millisecondText.innerText = '0' + millisecond;
   } else {
      millisecondText.innerText = millisecond;
   }

   if (millisecond > 99) {
      second++;
      if (second <= 9) {
         secondText.innerText = '0' + second;
      } else {
         secondText.innerText = second;
      }
      millisecond = 0;
      millisecondText.innerText = '00';
   }
}

timeContainer.appendChild(secondText);
timeContainer.appendChild(textNode);
timeContainer.appendChild(millisecondText);