# Classification

### Words and phrases

Definition 1. ***Word*** $w = c_1c_2...c_n \in A^+$ of length $n$ is a non-empty sequence of characters $c_i \in A$ where $A$ is the set of all alphanumeric characters.

Definition 2. ***Phrase*** $p = (w_1, w_2, ..., w_n) \in W^+$ of length $n$ is a non-empty sequence of words $w_i \in W$ where $W = A^+$ is the set of all words[^1].

[^1] $(\cdot)^+$ is the _Kleene plus_ operation on characters (Def. 1) or on words (Def. 2).

Definition 3. The set of all alphanumeric (word) characters is a disjoint union of
* ***uppercase*** characters $U$ (example: characters A-Z)
* ***lowercase*** characters $L$ (example: characters a-z)
* ***nocase*** characters $N$ (example: characters 0-9)

$$A = U \sqcup L \sqcup N$$

Definition 4. Let $C$ denote the set of ***caseful*** characters: $C = U \sqcup L$.

For every uppercase character $c_1 \in U$  there is a corresponding lower case character $c_2 \in L$, and vice versa (example: "a" <-> "A"). For nocase characters there is no such property as case.

TODO: Define uppercase, lowercase transformations on characters then on words.

### Well known case names

| Case rule \ Delimiter | `""` | `"_"` | `"-"` | `" "` | 
|---|---|---|---|---|
| All words lower case  | flatlowercase | snake_case | kebab-case | lower case |
| All words title case | PascalCase | Ada_Case | Train-Case | Title Case |
| All words upper case | FLATUPPERCASE | CONST_CASE | COBOL-CASE | UPPER CASE |
| First word lower case, other words title case | camelCase | — | — | — |
| First word title case, other words lower case | Sentence case | — | — | — |

### Alternative case names

#### Common cases

* **snake_case**: pothole_case
* **CONST_CASE**: CONSTANT_CASE, MACRO_CASE, SCREAMING_SNAKE_CASE, UPPER_SNAKE_CASE
* **camelCase**: lowerCamelCase, dromedaryCase, humpCase
* **PascalCase**: UpperCamelCase, CamelCase
* **kebab-case**: dash-case, hyphen-case, lisp-case, css-case, caterpillar-case, param-case, slug-case, spinal-case

#### Exotic cases

* **Ada_Case**: Pascal_Snake_Case
* **Train-Case**: Header-Case, Http-Header-Case
* **COBOL-CASE**: TRAIN-CASE, UPPER-TRAIN-CASE, SCREAMING-KEBAB-CASE

#### Flat cases

* **flatlowercase**: flatcase, lowercase
* **FLATUPPERCASE**: UPPERFLATCASE, UPPERCASE

#### Text cases

* **lower case**: clear case, no case, lower space case, normal case
* **Sentence case**: Space case
* **Title Case**: Capital Case, Start Case, Upper First Case
* **UPPER CASE**: UPPER SPACE CASE

### Convert from any string

### Mappings between case classes

### Digits and other nocase characters

### Acronyms (initialisms)


# Case conversion packages

1. GitHub [blakeembrey/change-case](https://github.com/blakeembrey/change-case) (JavaScript)
1. GitHub [mesqueeb/case-anything](https://github.com/mesqueeb/case-anything) (JavaScript)
1. GitHub [rutrum/convert-case](https://github.com/rutrum/convert-case) (Rust)
1. GitHub [pearxteam/kasechange](https://github.com/pearxteam/kasechange) (Kotlin)
1. GitHub [chanced/caps](https://github.com/chanced/caps) (Go)
