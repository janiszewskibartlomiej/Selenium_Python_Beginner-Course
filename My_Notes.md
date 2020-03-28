##### 1. metod get url is Json object:

-> localhost:8080/{"url":"https://exaple.pl"}

##### 2. Comamnds:

- .send_keys("test" + Keys.ENTER) - wpisanie tekstu i naciśnięcie Enter
- print(driver.title)- tytul strony
- driver.quit() - zamkniecie wszytskich okien i sesji -> czyszczenie po testach
- find_element_by_name -> znajdź element po tagu <name=...>
- do lokalizacji mozemy użyć metody selenium "find_element(By.ID,
'#example)
- print(element.text)
- `self.addCleanup(self.driver.quit())`  -> auto sprzatanie po testach


##### 3. if __name__ == '__main__':

-unittest.main(verbosity=2)   -> wiecej detali testowych, obszerniejszy wydruk

##### 4. `pip install nose`:
 
- tworzy klase suit case i odpala wszytskie testy 
- nazwa pliku musi sie zaczynac od 'test_'
- odpalenie -> `nosetests`
