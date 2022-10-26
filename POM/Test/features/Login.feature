Feature: Login the Automation Test Store
  As a user,
  I want to be able to enter the page, entering my username and password,
  to be able to enter my account and see different products.

@Regression
  Scenario Outline: login in Automation Test Store
    Given I am on the Automation test store page
    When enter a value in "<username>" and "<password>"
    Then I check if I can enter my account and "<message>"


      Examples: users
        | username  | password     | message                                           |
        | gonza_mol | Chicharito10 | Estoy dentro de la página de My account           |
        | sergito   | Cachavacha20 | Estoy dentro de la página de My account           |
        | pablo     | Charrua30    | Estoy dentro de la página de My account           |
        |           | Charrua30    | Error al no ingresar nombre de usuario            |
        | pablo     |              | Error al no ingresar una contraseña               |
        | pablos    | Charrua30    | Error al ingresar usuario o contraseña incorrecta |
