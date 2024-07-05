// interval을 설정하기 위한 변수
let intervalState;
// 현재 시간을 위한 변수
let second = 0;
let millisecond = 0;
// 기록용 시간을 위한 변수
let recordSecond;
let recordMillisecond;
// 스탑워치가 stop이거나 reset일 때 true
let stopWatchState = false;
// <div class="time"></div>
const timeContainer = document.querySelector('.time');
// <p class="second"></p> && 초기화
const secondText = document.createElement('p');
secondText.className = 'second';
secondText.innerText = '00';
// <p></p>
let textNode = document.createTextNode(':');
// <p class="millisecond"></p> && 초기화
const millisecondText = document.createElement('p');
millisecondText.className = 'millisecond';
millisecondText.innerText = '00';
// <div class="record__bottom"></div>
const records = document.querySelector('.record__bottom');


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
   // 기록하기
   if (second <= 9) {
      recordSecond = '0' + second;
   } else {
      recordSecond = second;
   }
   if (millisecond <= 9) {
      recordMillisecond = '0' + millisecond;
   } else {
      recordMillisecond = millisecond;
   }
   // <div class="record"></div>
   const record = document.createElement('div');
   record.className = 'record';
   // <button class="button__circle"></button>
   const circleBtn = document.createElement('button');
   circleBtn.className = 'bottom__circle';
   // <i class="fa-regular fa-circle"></i>
   const nonCheckedBox = document.createElement('i');
   nonCheckedBox.className = 'fa-regular fa-circle';
   circleBtn.appendChild(nonCheckedBox);
   // <p>"기록"</p>
   let recordText = document.createElement('p');
   recordText.innerText = recordSecond + ':' + recordMillisecond;
   record.appendChild(nonCheckedBox);
   record.appendChild(recordText);
   records.appendChild(record);

   console.log(recordText.innerText);
   // setInterval 멈추기
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
