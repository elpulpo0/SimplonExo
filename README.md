
# Guide des Balises Markdown

Markdown est un langage de balisage léger qui permet de formater du texte facilement. Ce fichier présente les balises les plus courantes utilisées en Markdown.

## Titres
Les titres sont créés en utilisant des signes dièse (`#`). Plus il y a de dièses, plus le titre est petit.

```markdown
# Titre de niveau 1
## Titre de niveau 2
### Titre de niveau 3
#### Titre de niveau 4
##### Titre de niveau 5
###### Titre de niveau 6
```

## Texte en gras et en italique
Vous pouvez formater le texte en gras ou en italique en utilisant des astérisques (`*`) ou des tirets bas (`_`).

- **Gras** : Utilisez deux astérisques ou tirets bas autour du texte.
- *Italique* : Utilisez un seul astérisque ou tiret bas.
- ***Gras et italique*** : Utilisez trois astérisques.

```markdown
**Texte en gras**
*Texte en italique*
***Texte en gras et italique***
```

## Listes
### Liste à puces
Les listes à puces sont créées avec des tirets (`-`), des astérisques (`*`), ou des plus (`+`).

```markdown
- Élément 1
- Élément 2
    - Sous-élément 1
    - Sous-élément 2
```

### Liste ordonnée
Les listes ordonnées sont créées avec des nombres suivis d'un point (`1.`).

```markdown
1. Premier élément
2. Deuxième élément
    1. Sous-élément
    2. Sous-élément
```

## Liens et images
### Lien
Les liens sont créés en utilisant des crochets `[ ]` suivis de parenthèses `( )` contenant l'URL.

```markdown
[Lien vers Google](https://www.google.com)
```

### Image
Les images utilisent une syntaxe similaire aux liens, mais avec un point d'exclamation (`!`) au début.

```markdown
![Texte alternatif](https://example.com/image.png)
```

## Citations
Les citations sont créées avec un signe supérieur (`>`).

```markdown
> Ceci est une citation.
```

## Blocs de code
Les blocs de code sont encadrés par trois accents graves (` ``` `).

### Bloc de code simple

```markdown
`Code inline`
```

### Bloc de code multi-lignes

```markdown
```
function helloWorld() {
    console.log("Hello, World!");
}
```
```

## Tableaux
Les tableaux sont créés avec des barres verticales (`|`) et des tirets (`-`) pour séparer les en-têtes.

```markdown
| Titre 1     | Titre 2     |
| ----------- | ----------- |
| Élément 1   | Élément 2   |
| Élément 3   | Élément 4   |
```

## Séparateurs
Les lignes horizontales sont créées avec trois tirets (`---`), astérisques (`***`), ou underscores (`___`).

```markdown
---
```

## Listes de tâches
Les cases à cocher sont créées avec des crochets `[ ]` pour des tâches non terminées et `[x]` pour des tâches complétées.

```markdown
- [x] Tâche 1 terminée
- [ ] Tâche 2 à faire
```

## Liens vers sections
Il est aussi possible de créer des liens internes vers des sections du même document. Par exemple, pour lier vers la section "Titres" :

```markdown
[Aller à la section Titres](#titres)
```

## Conclusion
Ce document couvre les éléments de base de Markdown. Vous pouvez mélanger ces différentes balises pour formater vos documents efficacement.
