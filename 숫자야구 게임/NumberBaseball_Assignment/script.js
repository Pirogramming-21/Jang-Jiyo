/*** 게임 초기화 ***/
// 시도 가능 횟수 설정
let cnt = 10;

// 중복되지 않는 랜덤한 숫자 num1, num2, num3 설정
function randomInt(min, max) {
   var randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
   return randomNum;
}
const num1 = randomInt(0, 9);
const num2 = randomInt(0, 9);
const num3 = randomInt(0, 9);

// html의 input과 결과창의 내용 비우기
const inputNum1 = document.getElementById('number1');
const inputNum2 = document.getElementById('number2');
const inputNum3 = document.getElementById('number3');
const resultDisplay = document.querySelector('.result-display');

inputNum1.value = '';
inputNum2.value = '';
inputNum3.value = '';
resultDisplay.innerText = '';