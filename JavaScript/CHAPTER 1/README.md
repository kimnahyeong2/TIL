# HTML과 JavaScript

- javascript는 html 위에서 동작하는 언어
- 서로 다른 언어를 합치기 위해서는 꼭 script태그가 필요함

## Script 태그

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