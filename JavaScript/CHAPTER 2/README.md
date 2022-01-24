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