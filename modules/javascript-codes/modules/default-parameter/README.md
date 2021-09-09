# Trabalhando com Parâmetros Default

Um dos novos recursos do ES6 é o parâmetro padrão (default). Com essa funcionalidade, quando criamos uma função ao declarar seus parâmetros, já podemos definir valores que serão padrão se eles chamarem essa função, nenhum valor será passado como argumento para esse parâmetro. Veja o exemplo abaixo:

```js
function employee(name = 'anonymous', business = 'Google') {
  console.log(`Nome: ${name}, ${business}`);
}

employee();
employee(undefined, 'IBM');
employee('drigols');
employee('Rodrigo', 'Amazon');
```

**NOTE:**  
Como você pode ver quando não passamos um determinado parâmetro, ele usa o padrão e isso é muito interessante em algumas aplicações.

---

**Rodrigo Leite -** *Software Engineer*
