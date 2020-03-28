##### 1. metod get url is Json object:

-> localhost:8080/{"url":"https://exaple.pl"}

##### 2. Comands:

- .send_keys("test" + Keys.ENTER) - wpisanie tekstu i naciśnięcie Enter
- print(driver.title)- tytul strony
- driver.quit() - zamkniecie wszytskich okien i sesji -> czyszczenie po testach
- find_element_by_name -> znajdź element po tagu <name=...>
- do lokalizacji mozemy użyć metody selenium "find_element(By.ID,
'#example)
- print(element.text)

##### 3. if __name__ == '__main__':
- unittest.main(verbosity=2)   -> wiecej detali testowych, obszerniejszy wydruk
