/*** 게임 초기화 ***/
// 시도 가능 횟수 설정
let cnt = 10;

// 중복되지 않는 랜덤한 숫자 ansNum 설정
const selectIndex = (totalIndex, selectingNumber) => {
   let randomIndexArray = [];
   for (i=0; i<selectingNumber; i++) {
      randomNum = Math.floor(Math.random() * totalIndex)
      if (randomIndexArray.indexOf(randomNum) == -1) {
         randomIndexArray.push(randomNum);
      } else {
         i--;
      }
   }
   return randomIndexArray;
}
const ansNum = selectIndex(10, 3);

// html의 input과 결과창의 내용 비우기
const inputNum1 = document.getElementById('number1');
const inputNum2 = document.getElementById('number2');
const inputNum3 = document.getElementById('number3');
const resultDisplay = document.querySelector('.result-display');

function resetInput() {
   inputNum1.value = '';
   inputNum2.value = '';
   inputNum3.value = '';
}
resetInput();
resultDisplay.innerText = '';

// 결과창 출력 함수
function gameResult(flag) {
   const gameResultContent = document.querySelector('.game-result');
   const gameResultImg = document.createElement("img");
   gameResultImg.id = "game-reusult-img";
   // 성공
   if (flag == 1) {
      gameResultImg.src = "success.png";
   }
   // 실패
   else if (flag == 0) {
      gameResultImg.src = "fail.png";
   }
   gameResultContent.appendChild(gameResultImg);
   const submitBtn = document.querySelector('.submit-button');
   submitBtn.disabled = true;
}

/*** 숫자 확인 ***/
function check_numbers() {
   // 입력되지 않은 input이 있을 때
   if (inputNum1.value == '' || inputNum2.value == '' || inputNum3.value == '') {
      resetInput();
   } // 숫자 3개가 입력되었을 때
   else {
      var inputNum = [Number(inputNum1.value), Number(inputNum2.value), Number(inputNum3.value)];
      let strikeCnt = 0;
      let ballCnt = 0;
      let outCnt = 0;
      // strike, ball, out 개수 세기
      for (let i=0; i<3; i++) {
         if (ansNum[i] == inputNum[i]) {
            strikeCnt += 1;
         } else if (ansNum.indexOf(inputNum[i]) != -1) {
            ballCnt += 1;
         } else {
            outCnt += 1;
         }
      }
      
      const displayContent = document.querySelector('.result-display');
      // <div class="check-result"></div>
      const checkContent = document.createElement('div');
      checkContent.className = "check-result";
      // <div class="left">3 5 6</div>
      const leftContent = document.createElement('div');
      leftContent.className = "left";
      leftContent.innerText = inputNum[0] + " " + inputNum[1] + " " + inputNum[2];
      checkContent.appendChild(leftContent);
      let textNode = document.createTextNode(':');
      checkContent.appendChild(textNode);
      // <div class="right"></div>
      const rightContent = document.createElement('div');
      rightContent.className = "right";
      if (outCnt != 3) {
         // 0 <div class="strike num-result">S</div>
         let strikeTextNode = document.createTextNode(" " + strikeCnt + " ");
         rightContent.appendChild(strikeTextNode);
         const strikeContent = document.createElement('div');
         strikeContent.className = "strike num-result";
         strikeContent.innerText = "S";
         rightContent.appendChild(strikeContent);
         // 1 <div class="ball num-result">B</div>
         let ballTextNode = document.createTextNode(" " + ballCnt + " ");
         rightContent.appendChild(ballTextNode);
         /* rightContent.append(ballCnt); */
         const ballContent = document.createElement('div');
         ballContent.className = "ball num-result";
         ballContent.innerText = "B";
         rightContent.appendChild(ballContent);
      } else {
         // <div class="out num-result">O</div>
         const outContent = document.createElement('div');
         outContent.className = "out num-reuslt";
         outContent.innerText = "O";
         rightContent.appendChild(outContent);
      }
      checkContent.appendChild(rightContent);
      displayContent.appendChild(checkContent);
      
      cnt -= 1;

      if (strikeCnt == 3) {
         gameResult(1);
      } else if (cnt == 0) {
         gameResult(0);
      }
   }
}