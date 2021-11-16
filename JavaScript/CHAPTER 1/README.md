## HTML과 JavaScript

- javascript는 html 위에서 동작하는 언어
- 서로 다른 언어를 합치기 위해서는 꼭 script태그가 필요함

### Script 태그

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>JavaScript</h1>
        <script>
            document.write(1+1);
        </script>
        <h1>html</h1>
        1+1
    </body>
</html>
```

- JavaScript로 쓴 코드는 동적
- HTML으로 쓴 코드는 정적

---

## JavaScript와 사용자의 상호작용, 이벤트(Event)

- 웹 브라우저에서 일어나는 사건
- 약 20가지 정도의 이벤트 속성이 존재

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <input type="button" value="Hi" onclick="alert('hi')">
        <input type="text" onchange="alert('changed')">
        <input type='text' onkeydown="alert('key down!')">
        <input type='button' value="click me" onmouseover="alert('mouse over!')">
    </body>
</html>
```

### (위의 코드를 기준으로 보는 이벤트 속성)

### Onclick 이벤트 속성

- HTML 태그 안에서 onclick 속성은 JavaScript 코드를 가지게 됨
- onclick이 포함된 태그가 클릭되었을 때, JavaScript 코드에 따라 웹 브라우저가 동작
- 웹브라우저는 alert라는 코드를 기억하고 있다가, 사용자가 클릭하면 이를 실행

### Onchange 이벤트 속성

- 입력창에 입력한 후 바깥쪽을 클릭했을 때를 기준으로, 그 전과 내용이 바뀌었는지 확인 후 이벤트 발생

### Onkeydown 이벤트 속성

- 키보드를 누를 경우 이벤트 발생

### Mouseover 이벤트 속성

- 버튼 위에 마우스를 올려놓을 경우 이벤트 발생

---

## 콘솔 (Console)

- 파일을 만들지 않고도 바로 JavaScript 코드 실행 가능
- 콘솔을 이용한 코드는, 페이지에서 즉석으로 실행되는 것임
- shift + Enter : 다음줄로 넘어가기 위해서

---

## JavaScript의 데이터 타입

- 크게 6종류의 데이터 타입이 존재
- Boolean, Null, Undefined, Number, String, Symbol

### 숫자 (Number)

- 숫자 데이터 타입은 연산이 가능
- 1+1에서 '+'는 이항 연산자 라고 함
    - 이항 연산자 = 산술 연산자 : +, -, /, *

### 문자열 (String)

- 따옴표로 시작해 따옴표로 끝남( ' ', " " )
- 문자열의 길이 : 문자열.length
- 문자열을 대문자로 변환 : 문자열.toUpperCase()
- 문자열 위치 찾기 : 문자열.indexOf('')

---

## 변수와 대입연산자

- 변수 : 바뀔 수 있는 수
- 대입 연산자 : =, 왼쪽에 있는 변수에 오른쪽에 있는 것을 대입
- 상수 : 변하지 않는 수

```jsx
x = 1000;
y = 1;
// x와 y는 변수
// =는 대입 연산자
x + y;
// 결과 1001
1 = 2;
// 1은 상수이기 때문에 오류가 남
```

### 변수의 필요성

- 변수를 이용해 원하는 모든 값을 한 번에 바꿀 수 있음
- 변수 이름 앞에 var을 붙이면 좋음

```jsx
var word = 'NaHyeong'
'Hello, my name is '+word+'. I am a student.
'+word' is good. '+word' like peach.'
// word에 들어갈 단어를 한번에 바꿀 수 있음
```

---

## 제어할 태그 선택하기

- 이벤트가 일어났을 때, 어떤 태그에 스타일이 지정될지 선택하는 작업이 필요
- CSS 선택자 : 태그 선택자, class 선택자, id 선택자

### querySelector

- 선택자를 이용해 원하는 태그 선택 가능

```jsx
documnet.querySelector('body')
documnet.querySelector('.this') // class 선택자
documnet.querySelector('#that') // id 선택자
```

```jsx
<input type="button" value="night" onclick="
	documnet.querySelector('body').style.backgroundColor='black';
	documnet.querySelector('body').style.color='white';
">
<input type="button" value="day" onclick="
	documnet.querySelector('body').style.backgroundColor='white';
	documnet.querySelector('body').style.color='black';
">
```