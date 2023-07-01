<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
  >
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../../static/css/style.css"> 
  <title>Расчет энергоэффективности умного дома</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Расчитай энергоэффективность своего дома!</h1>
      <p>Реши проблему излишнего электропотребления самостоятельно!</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title main__title--margin">Энергоэффективность твоего дома:</h2>
    <div class="main__rez" id="end">
        {%if result <= 150%}
        <img class="rez__img" src="../../static/img/planet_good.svg" alt="">
        <span>Ваш результат {{result}} кВт⋅ч</span>
        <span>Ваш дом имеет отличную энергоэффективности!</span>
        {%elif result >= 151 and result < 300%}
        <img class="rez__img" src="../../static/img/planet_medium.svg" alt="">
        <span>Ваш результат {{result}} кВт⋅ч</span>
        <span>Ваш дом имеет среднюю энергоэффективности!</span>
        {%elif result >= 300%}
        <img class="rez__img" src="../../static/img/planet_bad.svg" alt="">
        <span>Ваш результат {{result}} кВт⋅ч</span>
        <span>Ваш дом имеет плохую энергоэффективности!</span>
        {%endif%}
    </div>
    {% endblock %}
  </main>
  <footer>

  </footer>
</body>
</html>
