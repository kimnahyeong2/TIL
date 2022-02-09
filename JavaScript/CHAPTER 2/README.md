## 조건문

- 프로그램이 조건에 따라서 다른 기능들이 다른 순서에 따라서 실행되도록 만들어주는 것

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<h1> Conditional statements </h1>
		<h2> Program </h2>
		<script>
			document.write("1<br>");
			document.write("2<br>");
			document.write("3<br>");
			document.write("4<br>");
		</script>
		<h2>If-true</h2>
		<script>
			document.write("1<br>");
            if(true){
			    document.write("2<br>");
            } else {
                document.write("3<br>");
            }			
			document.write("4<br>");
		</script>

    <h2>If-false</h2>
		<script>
			document.write("1<br>");
            if(false){
			    document.write("2<br>");
            } else {
                document.write("3<br>");
            }			
			document.write("4<br>");
		</script>
	</body>
</html>
```

- if() 괄호 안에는 불리언 데이터 타입이 옴

### 조건문을 활용한 토글 만들기

```html
<!DOCTYPE html>
<html>
    <head>
        <title>WEB1 - JavaScript</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>WEB</h1>
        <input type="button" value="night" onclick="
        document.querySelector('body').style.backgroundColor = 'black';
        document.querySelector('body').style.color = 'white';
        ">
        <input type="button" value="day" onclick="
        document.querySelector('body').style.backgroundColor = 'white';
        document.querySelector('body').style.color = 'black';
        ">

        <input id="night_day" type="button" value="night" onclick="
            if (document.querySelector('#night_day').value === 'night'){
                document.querySelector('body').style.backgroundColor = 'black';
                document.querySelector('body').style.color = 'white';
                document.querySelector('#night_day').value = 'day';
            }
            else {
                document.querySelector('body').style.backgroundColor = 'white';
                document.querySelector('body').style.color = 'black';
                document.querySelector('#night_day').value = 'night';
            }
        ">
    </body>
</html>
```

---

## 비교연산자와 불리언

### 비교 연산자 ===

- 왼쪽과 오른쪽이 같은지 판단하는 것
- 이항 연산자임 (하나의 결과, 즉 True, False를 만들어냄)

### 불리언 (Boolean)

- 비교 연산자를 사용하면 결과로 True 혹은 False가 만들어지는데 이때 True와 False를 불리언 데이터 타입이라고 함
- 딱 두가지만 존재함

### 비교 연산자 <, >

- 두 값의 크기를 서로 비교하는 연산자
- HTML에서 사용할 경우 &lt; (<), &gt; (>)로 사용함

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>Comparison operator & Boolean</h1>
        <h2>===</h2>
        <h3>1===1</h3>
        <script>
            document.write(1===1);
        </script>

        <h3>1===2</h3>
        <script>
            document.write(1===2);
        </script>

        <h3>1+1===2</h3>
        <script>
            document.write(1+1===2);
        </script>

        <h3>1&lt;2</h3>
        <script>
            document.write(1<2);
        </script>

        <h3>1&lt;1</h3>
        <script>
            document.write(1<1);
        </script>

        <h3>1&gt;2</h3>
        <script>
            document.write(1>2);
        </script>

        <h3>1&lt;=1</h3>
        <script>
            document.write(1<=1);
        </script>
    </body>
</html>
```

---

## 리팩토링 (중복의 제거)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>WEB1 - JavaScript</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>WEB</h1>
        <input id="night_day" type="button" value="night" onclick="
            if (document.querySelector('#night_day').value === 'night'){
                document.querySelector('body').style.backgroundColor = 'black';
                document.querySelector('body').style.color = 'white';
                document.querySelector('#night_day').value = 'day';
            }
            else {
                document.querySelector('body').style.backgroundColor = 'white';
                document.querySelector('body').style.color = 'black';
                document.querySelector('#night_day').value = 'night';
            }
        ">
        <ol>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ol>
        <h2>JavaScript</h2>
        <p>
            JavaScript, often abbreviated as JS, is a high-level,
            dynamic, weakly typed, prototype-based, multi-paradigm, and interpreted
            programming language. Alongside HTML and CSS, JavaScript is one of the three
            core technologies of World Wide Web content production. It is used to make
            webpages interactive and provide online programs, including video games. The
            majority of websites employ it, and all modern web browsers support it
            without the need for plug-ins by means of a built-in JavaScipt engine. Each
            of the many JavaScript engines represent a different implementation of
            JavaScript, all based on the ECMAScript specification, with some engines not
            supporting the spec fully, and with many engines supporting additional
            features beyond ECMA.
        </p>

        <input type="button" value="night" onclick="
            var target = document.querySelector('body');
            if (this.value === 'night'){
                target.style.backgroundColor = 'black';
                target.style.color = 'white';
                this.value = 'day';
            }
            else {
                target.style.backgroundColor = 'white';
                target.style.color = 'black';
                this.value = 'night';
            }
        ">
        <input type="button" value="night" onclick="
            var target = document.querySelector('body');
            if (this.value === 'night'){
                target.style.backgroundColor = 'black';
                target.style.color = 'white';
                this.value = 'day';
            }
            else {
                target.style.backgroundColor = 'white';
                target.style.color = 'black';
                this.value = 'night';
            }
        ">
    </body>
</html>
```

### 리팩토링 - this 사용하기

- 비효율적인 코드를 효율적으로 만들어서 가독성을 높이고 유지보수가 쉽도록 만드는 것
- 코드의 기능적인 면에서는 변화가 없음
- 자기 자신을 가리키기 위한 this 라는 키위드를 사용한다면, 코드를 복사하더라도 따로 id값을 바꿔줘야하는 작업을 진행할 필요없이 계속 사용 가능함

### 리팩토링 - 중복 제거하기

- 코딩을 할 때 중복을 제거해 주는 것이 중요함
- 변수를 하나 만든 뒤 중복으로 사용된 태그를 찾아서 넣는다면, 변수만 간단하게 사용해 코드의 길이를 줄일 수 있음

---

## 반복문과 배열

### 반복문

- 같은 작업을 반복적으로 실행해주는 문법

```jsx
var links = document.querySelectorAll('a');
var i = 0;
while (i<links.length) {
  links[i].style.color = 'powerblue';
  i=i+1;
}
```

### 배열

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		<h1> Arrays </h1>
		<h2> Syntax </h2>
		<script>
			var coworkers = ["egoing", "leezche"];
		</script>

		<h2> get </h2>
		<script>
			document.write(coworkers[0]);
			document.write(coworkers[1]);
		</script>

		<h2> add </h2>
		<script>
			coworkers.push('duru');
			coworkers.push('taeho'); #뒤쪽에 추가
			coworkers.unshift('mina'); #앞쪽에 추가
			coworkers.splice(2,0,'nari','dongbin'); #인덱스2의 위치에 2개의 요소 추가
		</script>

		<h2> remove </h2>
		<script>
			coworkers.pop(); #뒤쪽제거
			coworkers.shift(); #앞쪽제거
			coworkers.splice(2,1); #인덱스2부터 1개요소 제거
		</script>

		<h2> count </h2>
		<script>
			document.write(coworkers.length);
		</script>
	</body>
</html>
```