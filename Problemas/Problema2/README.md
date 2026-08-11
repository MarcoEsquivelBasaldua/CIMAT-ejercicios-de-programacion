# Problema 2

Un bano publico esta conformado por $N+2$ habitaculos dispuestos en una fila. Los habitaculos de los extremos (el 1 y el $N+2$) estan siempre ocupados por unos guardias de seguridad, mientras que los N habitaculos restantes son para los usuarios. Siempre que alguien entra a un bano intenta ubicarse en un habitaculo que este lo mas alejado del resto de habitaculos que estan ocupados. Concretamente actua de la siguiente forma: para cada habitaculo $S$ que no esta ocupado, calcula $Ls$ y $Rs$, siendo $Ls$ el numero de habitaculos contiguos libres a la izquierda de $S$ (hasta llegar a un habitaculo ocupado) y $Rs$ el numero de habitaculos contiguos libres a la derecha de $S$ (hasta llegar a un habitaculo ocupado). De entre todos los habitaculos elige aquel en el que $min(LS, Rs)$ sea maximo y lo ocupa. En caso de empate, elige entre ellos aquel en el que $max(Ls, Rs)$ sea maximo. Si aun sigue habiendo varios habitaculos posibles, elige aquel que este mas a la izquierda.

Supongamos que hay $K \leq N$ personas que van a entrar al bano. Las personas van entrando en orden, de forma que cuando la persona $i$ entra, la persona $i-1$ ya ha elegido y ocupado habitaculo. Al intentar entrar la persona K, cual sera el valor de $min(Ls, Rs)$ para el habitaculo que elige? Cual sera el valor de $max(Ls, Rs)$ para el habitaculo que elige?

## a

Desarrollar una funcion void getMinMax(int N, int K) que calcule los dos valores solicitados tras haber entrado las $K$ personas.

Ejemplo: al ejecutar con $N=8$, $K=2$ los valores calculados serian 2 y 1.

## b

Estime el numero de pasos que ejecutaria la funcion desarrollada considerando que $N=K$. Se pretende encontrar una estimacion y no el valor exacto, pero la estimacion deberia ser suficientemente buena para poder predecir de forma correcta los siguientes casos:

- Su codigo podria ejecuar en menos de 1 segundo si $N=k=100$?
- Su codigo podria ejecuar en menos de 1 segundo si $N=k=2500$?
