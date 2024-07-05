const stopwatchBtn = document.querySelector('.stopwatch');
const timerBtn = document.querySelector('.timer');
const recordContainer = document.querySelector('.record__container');
const watchContainer = document.querySelector('.watch__container');
const timerContainer = document.querySelector('.timer__container');

// 기본 설정값: 스톱워치
timerContainer.classList.add('hidden');

// 스톱워치로 전환
stopwatchBtn.addEventListener("click", () => {
   watchContainer.classList.remove('hidden');
   timerContainer.classList.add('hidden');
   recordContainer.classList.remove('hidden');
})
// 타이머로 전환
timerBtn.addEventListener("click", () => {
   watchContainer.classList.add('hidden');
   timerContainer.classList.remove('hidden');
   recordContainer.classList.add('hidden');
})

/***** 스톱워치 *****/
// interval을 설정하기 위한 변수
let stopwatchIntervalState;
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

const allCheckBtnContainer = document.querySelector('.top__circle');
const allCheckBtn = document.createElement('i');
allCheckBtn.className = 'fa-regular fa-circle';
allCheckBtnContainer.appendChild(allCheckBtn);

const stopwatchStartBtn = document.getElementById('stopwatch__start');
stopwatchStartBtn.addEventListener("click", () => {
   if (stopWatchState == false) {
      console.log("pushed start!!");
      stopwatchIntervalState = setInterval(startStopwatch, 10);
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

   // nonChecked 클릭 -> Checked || checked 클릭 -> nonChecked
   nonCheckedBox.addEventListener("click", () => {
      nonCheckedBox.classList.toggle('fa-circle');
      nonCheckedBox.classList.toggle('fa-circle-check');
      // record 요소에 selected가 있으면 제거 || 없으면 추가
      record.classList.toggle('selected');

      const allRecords = document.querySelectorAll('.record');
      const selectedRecords = document.querySelectorAll('.record.selected'); 
      if (allRecords.length != selectedRecords.length) {
         if (allCheckBtn.classList.contains('fa-circle-check')) {
            allCheckBtn.classList.remove('fa-circle-check');
            allCheckBtn.classList.add('fa-circle');
         }
      } else {
         if (!allCheckBtn.classList.contains('fa-circle-check')) {
            allCheckBtn.classList.remove('fa-circle');
            allCheckBtn.classList.add('fa-circle-check');
         }
      }
   })

   // <p>"기록"</p>
   let recordText = document.createElement('p');
   recordText.innerText = recordSecond + ':' + recordMillisecond;
   record.appendChild(nonCheckedBox);
   record.appendChild(recordText);
   records.appendChild(record);

   console.log(recordText.innerText);
   // setInterval 멈추기
   clearInterval(stopwatchIntervalState);
   stopWatchState = false;
})

const resetBtn = document.getElementById('reset');
resetBtn.addEventListener("click", () => {
   console.log("pushed reset!!");
   clearInterval(stopwatchIntervalState);
   millisecond = 0;
   millisecondText.innerText = '00';
   second = 0;
   secondText.innerText = '00';
   stopWatchState = false;
})

const trashBtn = document.querySelector('.trash');
trashBtn.addEventListener("click", () => {
   const selectedRecord = document.querySelectorAll('.record.selected');
   selectedRecord.forEach(record => {
      records.removeChild(record);
   })
})

allCheckBtn.addEventListener("click", () => {   
   console.log("클릭");
   const allRecords = document.querySelectorAll('.record');
   const selectedRecords = document.querySelectorAll('.record.selected'); 
   // selected 되지 않은 것이 있다면 selected로 바꿔주고
   // 해당 버튼도 체크표시될 수 있도록
   if (allRecords.length != selectedRecords.length) {
      console.log("selected 덜 됨");
      allRecords.forEach(record => {
         if (!record.classList.contains('selected')) {
            record.classList.add('selected');
            let circleIcon = record.querySelector('.fa-regular');
            if (circleIcon) {
               circleIcon.classList.remove('fa-circle');
               circleIcon.classList.add('fa-circle-check');
            }
         }
      })
      if (!allCheckBtn.classList.contains('fa-circle-check')) {
         allCheckBtn.classList.remove('fa-circle');
         allCheckBtn.classList.add('fa-circle-check');
      }
   } else { // 모든 기록이 선택된 경우
      console.log("selected 다 됨")
      allRecords.forEach(record => {
         // 각 record에 대응하는 체크박스 설정
         let circleIcon = record.querySelector('.fa-regular');
         if (circleIcon) {
            circleIcon.classList.remove('fa-circle-check');
            circleIcon.classList.add('fa-circle');
            record.classList.remove('selected');
         }
      });
      if (allCheckBtn.classList.contains('fa-circle-check')) {
         allCheckBtn.classList.remove('fa-circle-check');
         allCheckBtn.classList.add('fa-circle');
      }
   }
})

function startStopwatch() {
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


/***** 타이머 *****/
const inputSecond = document.getElementById('second');
const inputMillisecond = document.getElementById('millisecond');
const finishText = document.querySelector('.finish');

inputSecond.value = '00';
inputMillisecond.value = '00';
finishText.classList.add('hidden');

// interval을 설정하기 위한 변수
let timerIntervalState;
let stopTimerState = false;
const timerStartBtn = document.getElementById('timer__start');
timerStartBtn.addEventListener("click", () => {
   finishText.classList.add('hidden');
   if (stopTimerState == false) {
      console.log("pushed start!!");
      timerIntervalState = setInterval(startTimer, 10);
      stopTimerState = true;
   }
})

const pauseBtn = document.getElementById('pause');
pauseBtn.addEventListener("click", () => {
   console.log("pushed pause!!");
   clearInterval(timerIntervalState);
   stopTimerState = false;
})

const playBtn = document.getElementById('play');
playBtn.addEventListener("click", () => {
   if (stopTimerState == false) {
      console.log("pushed play!!");
      timerIntervalState = setInterval(startTimer, 10);
      stopTimerState = true;
   }
})

function startTimer() {
   inputMillisecond.value--;
    
   if (inputMillisecond.value < 0) {
       inputSecond.value--;
       inputMillisecond.value = 99;
   }

   if (inputMillisecond.value <= 9) {
      inputMillisecond.innerText = '0' + inputMillisecond.value;
   } else {
      inputMillisecond.innerText = inputMillisecond.value;
   }

   if (inputSecond.value <= 9) {
      inputSecond.innerText = '0' + inputSecond.value;
   } else {
      inputSecond.innerText = inputSecond.value;
   }
   
   if (inputSecond.value == 0 && inputMillisecond.value == 0) {
      clearInterval(timerIntervalState);
      inputMillisecond.innerText == '00';
      inputSecond.innerText == '00';
      finishText.classList.remove('hidden');
      stopTimerState = false;
   }
}