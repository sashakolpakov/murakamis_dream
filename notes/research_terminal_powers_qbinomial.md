# Exact terminal fillings with arbitrary fixed crossing power

Research note, 2 November 2026. The frozen manuscripts are unchanged.

A terminal crossing circle has one remaining boundary after it is filled.
Its contribution must therefore be calculated as a polynomial in that
boundary variable. A formula for a closed knot does not determine this
polynomial. This note gives an exact finite formula for every signed
crossing power, reduces its number of summations by pairing crossings,
and proves a bound near the opposite end of the real boundary interval.
These results retain the first derivatives at the double roots of the
pair algebra.

For powers $2$ and $-2$, the stronger asymptotic theorem is already proved
in [the two-crossing note](research_two_crossing_terminal_filling.md).
For fixed powers of absolute value at least three, the formulas below
are starting points for the remaining global estimate. They do not,
by themselves, prove that estimate or a volume conjecture for these
additional fillings.

## 1. The boundary polynomial

Fix an integer $N\geq3$ and set

\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \kappa=q^{d^2/2}.
\]

Fractional powers of $q$ use this displayed exponential. For
$0\leq k<N$, define

\[
 S_k=\prod_{a=1}^k2\sin(\pi a/N),\qquad
 F_k=(Q;Q)_k=\prod_{a=1}^k(1-Q^a),
 \qquad S_0=F_0=1.
\]

None of these finite products vanishes. The relation between them is

\[
 S_k=i^k q^{-k(k+1)/2}F_k.                                  \tag{1}
\]

Let $T_N$ be the monic Chebyshev polynomial characterized by
$T_N(t+t^{-1})=t^N+t^{-N}$. Work in the full algebra

\[
 \mathcal A_N=\mathbb C[z]/(P_N(z)),\qquad P_N(z)=T_N(z)+2.
\]

Every element has a unique representative of degree less than $N$.
Its real Newton basis is

\[
 e_k(z)=S_k^{-2}\prod_{a=0}^{k-1}(c_a-z),\qquad
 c_a=2\cos((2a+1)\pi/N).
\]

The closing functional and the turn are

\[
 \phi(f)=(-1)^dN^2[z^d]\operatorname{rem}_{P_N}f,
 \qquad
 \phi(e_i e_j)=\mathbf1_{i+j=d},
\]

\[
 \mathsf T\left(\sum_{k=0}^d v_ke_k\right)
                 =\sum_{k=0}^d v_{d-k}e_k.
\]

The turn is a linear involution; it is not an algebra homomorphism.
The physical positive crossing and its multiplication matrix are

\[
 R=\kappa\sum_{k=0}^d(-q)^ke_k,\qquad
 R_{kj}=\kappa(-1)^kq^{k(j+1)}
              \frac{S_k}{S_jS_{k-j}}\quad(0\leq j\leq k<N).    \tag{2}
\]

The other matrix entries are zero. The finite algebra calculation
in [the Newton calculus](../papers/newton-calculus/finite.tex)
proves (2) with the double-root derivatives included.

If the terminal vertex has signed crossing power $n\in\mathbb Z$,
its exact open-boundary contribution is

\[
 \mathcal H_{n,N}(z)=\mathsf T(R^n)(z)
     =\sum_{k=0}^d\phi(R^ne_k)e_k(z).
 \qquad
 H_{n,N}(u)=\mathcal H_{n,N}(-2\cos u).                       \tag{3}
\]

The parameter $n$ is the original physical crossing power. No surgery
slope has been replaced by an effective coefficient in this definition.

## 2. A finite transform for all positive powers

For $0\leq j\leq k<N$, define the Gaussian binomial coefficient

\[
 {k\brack j}_Q=\frac{F_k}{F_jF_{k-j}},
\]

and define two lower triangular matrices by

\[
 C_{kj}=\frac{(-1)^jQ^{j(j+1)/2}}{F_{k-j}},
 \qquad
 B_{kj}=Q^{j(j+1)}{k\brack j}_Q.                            \tag{4}
\]

Entries above the diagonal are zero. Let $D$ be the invertible diagonal
matrix with $D_{kk}=(-q)^kF_k$, and let $\mathbf1$ be the vector whose
$N$ entries are all one.

**Proposition 1.** Multiplication by the original crossing satisfies

\[
 R=\kappa DCD^{-1},\qquad C^2=B.                            \tag{5}
\]

For every integer $n\geq2$, put $g^{(n)}=C^{n-2}\mathbf1$.
Then the complete polynomial (3) is

\[
 \boxed{\displaystyle
 \mathcal H_{n,N}(z)=\kappa^n
  \sum_{k=0}^d(-q)^{d-k}F_{d-k}\,g^{(n)}_{d-k}\,e_k(z).}     \tag{6}
\]

In particular, all the identities in (5) and (6) hold before closing
the remaining boundary.

*Proof.* From (1) and (2), direct cancellation gives

\[
 \frac{R_{kj}D_{jj}}{\kappa D_{kk}}
 =\frac{(-1)^j q^{j(j+1)}}{F_{k-j}}=C_{kj}.
\]

This proves the similarity in (5). To compute its square, write
$a_j=(-1)^jQ^{j(j+1)/2}$ and $m=k-j$. The finite binomial identity

\[
 \sum_{r=0}^m(-1)^rQ^{r(r-1)/2}{m\brack r}_Q x^r
             =\prod_{r=0}^{m-1}(1-xQ^r)                   \tag{7}
\]

follows by multiplying the factors on the right, or by induction on
$m$. It implies

\[
 \begin{aligned}
 (C^2)_{kj}
 &=a_j\sum_{h=j}^k\frac{a_h}{F_{k-h}F_{h-j}}\\
 &=\frac{a_j^2}{F_m}
       \prod_{r=0}^{m-1}(1-Q^{j+1+r})\\
 &=Q^{j(j+1)}\frac{F_k}{F_jF_{k-j}}=B_{kj}.
 \end{aligned}                                             \tag{8}
\]

Let $\mathbf e_0$ denote the coordinate vector of the identity element
$e_0=1$. The first column of $B$ is $\mathbf1$, so
$C^2\mathbf e_0=\mathbf1$. Hence the coefficient vector of $R^n$ is
$\kappa^nDC^n\mathbf e_0=\kappa^nDg^{(n)}$ for $n\geq2$.
Reversing this vector proves (6). Every denominator in the calculation
has index less than $N$; no division by a root-of-unity zero or passage
to the reduced algebra occurred. $\square$

The formula also gives an efficient exact recurrence: form $g^{(2)}$
as the constant vector and successively multiply by $C$. A fixed
power requires $O(|n|N^2)$ scalar operations. Pairing applications of
$C$ and using $B$ instead reduces the number of steps by about half.
This statement concerns the number of arithmetic operations; it is not
an assertion that cancellation at large $N$ can be computed accurately
at fixed floating-point precision.

## 3. The nested sums after pairing crossings

For $p\geq1$, Proposition 1 gives

\[
 g^{(2p)}=B^{p-1}\mathbf1,\qquad
 g^{(2p+1)}=CB^{p-1}\mathbf1.                               \tag{9}
\]

Thus an even power $n=2p$ requires only $p-1$ summation variables:

\[
 g^{(2p)}_k=
 \sum_{0\leq j_1\leq\cdots\leq j_{p-1}\leq k}
 \prod_{a=1}^{p-1}
    \left(Q^{j_a(j_a+1)}{j_{a+1}\brack j_a}_Q\right),
 \qquad j_p=k.                                             \tag{10}
\]

When $p=1$, the sum and product are empty and have value one.
An odd power requires one additional sum:

\[
 g^{(2p+1)}_k=
  \sum_{j=0}^k
   \frac{(-1)^jQ^{j(j+1)/2}}{F_{k-j}}\,g^{(2p)}_j.           \tag{11}
\]

For example,

\[
 g^{(2)}_k=1,\qquad
 g^{(3)}_k=\sum_{j=0}^k\frac{(-1)^jQ^{j(j+1)/2}}{F_{k-j}},
 \qquad
 g^{(4)}_k=\sum_{j=0}^k Q^{j(j+1)}{k\brack j}_Q.             \tag{12}
\]

Formula (10) has no explicit alternating sign. Its summands are
nevertheless complex at $Q=e^{2\pi i/N}$. Replacing them by their
absolute values is a new estimate, not an identity. In particular,
(10) does not supply a positivity proof for a filled volume limit.

Since the basis $e_k$ is real and $R^{-1}$ is the coefficient conjugate
of $R$, the exact negative-power polynomial is

\[
 \mathcal H_{-n,N}(z)
       =\overline{\mathcal H_{n,N}(\bar z)}.                 \tag{13}
\]

Thus (6), (10), and (11) describe every fixed nonzero integer power.
For comparison, $\mathcal H_0=e_d$,
$\mathcal H_1=R^{-1}$, and $\mathcal H_{-1}=R$. The powers $0$ and
$\pm1$ have separate exact topological reductions; they are not
additional saddles to be inferred from (10).

## 4. A uniform bound near the other endpoint

The exact formulas also give a useful bound without resolving their
oscillation. Write

\[
 G=\sum_{a=0}^{\infty}\frac{(-1)^a}{(2a+1)^2},\qquad
 M_2=\frac{2G}{\pi}=\frac{v_{\rm oct}}{2\pi}.
\]

Here $v_{\rm oct}=4G$ is the volume of a regular ideal octahedron.
The endpoint in this section is $u=\pi$, equivalently $z=2$.
The geometric maximum used for long fillings is at $u=0$, or $z=-2$.

**Proposition 2.** There are absolute constants $A,C>0$ such that,
for every integer $n$, every $N\geq3$, and every $0\leq\delta\leq\pi$,

\[
 |H_{n,N}(\pi-\delta)|
 \leq C(1+|n|)N^A
   \exp\!\left[N\left\{M_2+
          \operatorname{arsinh}(\sin(\delta/2))\right\}\right].
                                                               \tag{14}
\]

The bound applies equally to the reflected endpoint $u=-\pi$.

*Proof.* Put $m=\lfloor(N-1)/2\rfloor$. For $0\leq k\leq m$,
factor each cosine difference to obtain

\[
 \begin{aligned}
 |e_k(2\cos\delta)|
 &=\prod_{a=0}^{k-1}
  \frac{|\sin^2((a+1/2)\pi/N)-\sin^2(\delta/2)|}
       {\sin^2((a+1)\pi/N)}\\
 &\leq\prod_{j=1}^m
       \left(1+\frac{s^2}{\sin^2(\pi j/N)}\right),
 \qquad s=\sin(\delta/2).
 \end{aligned}                                               \tag{15}
\]

The inequality uses monotonicity of sine on $[0,\pi/2]$ and
$|a-b|\leq a+b$ for $a,b\geq0$. Set $a=\operatorname{arsinh}s$.
The elementary sine product identity is

\[
 \prod_{j=1}^{N-1}
       \left(1+\frac{\sinh^2a}{\sin^2(\pi j/N)}\right)
       =\left(\frac{\sinh(Na)}{N\sinh a}\right)^2.            \tag{16}
\]

For completeness, the numerator after multiplying by
$\prod_{j=1}^{N-1}\sin^2(\pi j/N)$ is the product of the nontrivial
factors in $w^N-1$, evaluated at $w=e^{2a}$ and at $w=e^{-2a}$.
The factors $j$ and $N-j$ are equal. Thus the half product in
(15) equals $\sinh(Na)/(N\sinh a)$ for odd $N$ and equals this
quantity divided by $\cosh a$ for even $N$. Since
$\sinh(Na)\leq Na e^{Na}$ and $a\leq\sinh a$, both are at most
$e^{Na}$. The limiting value at $a=0$ is one. Therefore

\[
 |e_k(2\cos\delta)|\leq e^{N\operatorname{arsinh}s}
                  \qquad(0\leq k\leq m).                   \tag{17}
\]

We next bound the coefficients in (3), including all first normal
coordinates. At a double root $c_j=2\cos\theta_j$, where
$\theta_j=(2j+1)\pi/N<\pi$, the original crossing has

\[
 |R(c_j)|=1,\qquad
 \frac{R'(c_j)}{R(c_j)}
       =\frac{i(d-2j)}{4\sin\theta_j}.                      \tag{18}
\]

Consequently the complete Hermite norm of $R^n$ is at most
$C(1+|n|)N^2$ for every signed integer $n$. The exact trace formula is

\[
 \phi(f)=(-1)^d\sum_{c\ {
m double}}
        \bigl((4-c^2)f'(c)-cf(c)\bigr)
       +\mathbf1_{N\ {
m odd}}f(-2).                       \tag{19}
\]

It follows that $|\phi(R^ne_k)|$ is at most a polynomial in $N$,
times $1+|n|$, times the complete Hermite norm of $e_k$.

The elementary basis estimates from
[the finite-bound calculation](../papers/circle-tree-volume/finite-bounds.tex)
are

\[
 \|e_k\|_{\mathcal J}\leq CN^A
 \begin{cases}
 e^{Ng(k/N)},&k\leq m,\\
 1,&k>m,
 \end{cases}
 \qquad
 g(x)=J(2x)-4J(x),\quad
 J(x)=\int_0^x\log(2\sin\pi t)\,dt.                         \tag{20}
\]

The interval norm of each high-index $e_k$ is also polynomial.
Here is why these estimates retain the data needed in (19). For low
indices, the values at all distinct nodes are nonnegative and at most
$e_k(-2)$. Interpolation at the distinct Chebyshev nodes has polynomial
conditioning; differentiation has polynomial cost. Uniform comparison
of the logarithmic products with their integrals gives
$\log e_k(-2)=Ng(k/N)+O(\log N)$, including the endpoints. For
high indices, reflection of the Newton factors makes every nodal value
zero; the remaining derivatives are bounded by the explicit sine
factorial ratio in the cited calculation, at most $N^2/16$. Hermite
interpolation again has polynomial cost. Thus vanishing values have
not been substituted for a bound on the normal directions.

On $[0,1/2]$, direct differentiation gives
$g'(x)=2\log\cot(\pi x)$. Its maximum is at $x=1/4$, with value
$g(1/4)=2G/\pi=M_2$. Apply (17) and (20) to the low terms in
(3). The high terms contribute only a polynomial. Summing at most
$N$ terms proves (14). $\square$

**Consequence for the next analytic step.** Suppose a fixed nonzero
power $n$ has a proved local geometric asymptotic at $u=0$ with real
action $M_n>M_2$. Choose $\delta_0>0$ so that

\[
 \operatorname{arsinh}(\sin(\delta_0/2))<M_n-M_2.
\]

Then (14) gives a strict exponential gap throughout
$\pi-\delta_0\leq |u|\leq\pi$. It is enough to treat the remaining
compact real interval. This consequence requires the stated proof
that $M_n>M_2$; the finite computations below are not a substitute.

The endpoint gap also persists on a sufficiently thin complex
neighborhood. Indeed, apply the ordinary polynomial Bernstein bound
to $\mathcal H_{n,N}$ on a slightly larger real interval
$[2\cos\delta_1,2]$, where
$0<\delta_0<\delta_1$ and the inequality above remains strict.
For $u=\pi-\delta+ib$, $0\leq\delta\leq\delta_0$, the Bernstein
ellipse parameter of $z=2\cos(\delta-ib)$ relative to this interval
is $O_{\delta_0,\delta_1}(|b|)$. Away from $\delta=0$ this follows
from the smooth inverse cosine; at $\delta=0$ the displacement is
$O(b^2)$ and the square-root endpoint coordinate is $O(|b|)$.
Since the polynomial degree is at most $N-1$, the additional factor
is $e^{CN|b|}$. A small fixed $|b|$ preserves the strict gap. This
argument supplies a complex bound in the discarded endpoint region;
it does not assert a quadratic bound in $b$ near the geometric saddle.

## 5. Two restrictions on a norm-based proof

### 5.1. The crossing is not unitary on the full algebra

The eigenvalues in (18) have modulus one, but the derivative there is
nonzero. At a double root the local algebra is
$\mathbb C[\epsilon]/(\epsilon^2)$, and multiplication by $R$ is

\[
 R(c)\begin{pmatrix}1&0\\ R'(c)/R(c)&1\end{pmatrix}
\]

in the basis $1,\epsilon$. It has a nontrivial Jordan block. Therefore
no positive definite Hermitian inner product on the full algebra can
make multiplication by $R$, or by any nonzero fixed power $R^n$,
unitary: a unitary operator is diagonalizable. Passing to distinct
root values alone removes this obstruction but also removes the
first derivatives used by the actual trace (19).

This is an obstruction to exact unitarity in the original algebra.
It does not rule out a weighted estimate with polynomial losses, nor
does it rule out a different finite transform whose norm can be proved
useful for the asymptotic problem.

### 5.2. An exact phase identity for two crossings

The two-crossing phase relation can be proved in the full algebra,
without a limiting argument or a numerical guess.

**Proposition 3.** The exact two-crossing polynomials satisfy

\[
 R\mathcal H_{2,N}=\kappa\mathcal H_{-2,N}
                         \quad\hbox{in }\mathcal A_N.       \tag{21a}
\]

At every double node $c_j$, they consequently satisfy

\[
 \mathcal H_{2,N}'(c_j)\mathcal H_{-2,N}(c_j)
 -\mathcal H_{2,N}(c_j)\mathcal H_{-2,N}'(c_j)
 =-\frac{i(d-2j)}{4\sin\theta_j}
      |\mathcal H_{2,N}(c_j)|^2.                            \tag{21b}
\]

If $\mathcal H_{2,N}(c_j)\ne0$, this gives

\[
 \operatorname{Im}
   \frac{\mathcal H_{2,N}'(c_j)}{\mathcal H_{2,N}(c_j)}
       =-\frac{d-2j}{8\sin\theta_j}
       =-\frac{N(\pi-\theta_j)}{8\pi\sin\theta_j}.           \tag{21c}
\]

*Proof.* The exact coefficient formula from the two-crossing note is

\[
 \mathcal H_{2,N}=N\sum_{j=0}^d\frac{q^{j^2}}{F_j}e_j,
 \qquad
 \mathcal H_{-2,N}=N\sum_{j=0}^d
                         \frac{(-1)^jq^j}{F_j}e_j.
\]

Multiply the first expression by the triangular matrix (2). The
coefficient of $e_k$ is

\[
 \kappa N(-1)^kq^kF_k
       \sum_{j=0}^k\frac{Q^{j^2}}{F_j^2F_{k-j}}.            \tag{21d}
\]

The required finite identity is

\[
 \frac1{F_k}=\sum_{j=0}^k
                  \frac{Q^{j^2}}{F_j}{k\brack j}_Q.        \tag{21e}
\]

Here is an elementary proof, initially in formal power series in $Q$.
The left side counts partitions whose largest part is at most $k$.
If such a partition has a Durfee square of side $j$, the square
contributes $Q^{j^2}$. The portion to its right fits in a rectangle
of height $j$ and width $k-j$, whose generating polynomial is
${k\brack j}_Q$. The portion below has largest part at most $j$,
whose generating series is $1/F_j$. These choices are independent
and uniquely recover the partition. The rectangle generating
polynomial follows by separating paths along its upper and right
boundary, which gives the Gaussian binomial recurrence. Summing over
$j$ proves (21e). Alternatively, that recurrence gives a finite
algebraic induction. After multiplying by the denominators, (21e)
is a polynomial identity, so it applies to the present root of unity;
all indices are below $N$.

Dividing (21e) by $F_k$ evaluates the sum in (21d) as $1/F_k^2$.
This proves (21a) coefficient by coefficient. Differentiate (21a)
at a double node, where equality in the quotient also gives equality
of first derivatives. Subtract the two products and use (18) to
obtain (21b). Coefficient conjugacy then gives (21c). $\square$

Identity (21b) has no nonvanishing premise. Dividing by the squared
modulus in (21c) does have that premise. A separate positive norm
formula would supply it at all nodes.

### 5.3. Reduced norm polynomials are not pointwise norms

The two-crossing calculation suggests the particularly simple identity

\[
 \operatorname{rem}_{P_N}
       (\mathcal H_{2,N}\mathcal H_{-2,N})
       =N^2\sum_{2k<N}\frac{S_{2k}}{S_k^4}e_k.              \tag{21}
\]

At the time of writing this section, (21) has been checked at finite
levels; its general algebraic proof is a separate calculation. Even
if that proof is supplied, the remainder must not be treated as the
pointwise squared modulus on the entire real interval.

For example, at $N=3$, direct exact calculation gives

\[
 |\mathcal H_{2,3}(z)|^2
   =\frac{(z+8)^2(z^2-5z+13)}{81},\qquad z\in\mathbb R,
\]

\[
 \operatorname{rem}_{P_3}
       (\mathcal H_{2,3}\mathcal H_{-2,3})=10-z,
\]

\[
 |\mathcal H_{2,3}(z)|^2-(10-z)
       =\frac{(z-1)^2(z+2)(z+11)}{81}.                     \tag{22}
\]

The last expression is positive at interior points such as $z=0$.
The quotient identity records values and derivatives at the roots of
$P_3$; it is not a pointwise upper bound between them. A reconstruction
argument, with controlled values and normals, is still necessary.

Nor does nonnegativity of all the Newton coefficients of the reduced
norm hold for arbitrary powers. The exact example $N=3$, $n=7$ is

\[
 \operatorname{rem}_{P_3}
       (\mathcal H_{7,3}\mathcal H_{-7,3})=127-18e_1.        \tag{23}
\]

A proposed restriction $N\geq2|n|$ does not repair this assertion.
There is an exact counterexample at $N=24$, $n=9$: the coefficient
of $e_3$ is

\[
 \begin{aligned}
 -{}&667276414\cos(3\pi/8)
     -227489320\cos(11\pi/24)\\
 -{}&930022046\{\cos(7\pi/24)+\cos(\pi/24)\}\\
 -{}&998071796\{\cos(5\pi/24)+\cos(\pi/8)\}<0.              \tag{23a}
 \end{aligned}
\]

Every cosine displayed is strictly positive. This is an exact
cyclotomic calculation, reproduced by

```sh
python3 experiments/audit_terminal_norm_positivity_counterexample.py
```

The script requires `sympy`. It raises the original triangular
crossing matrix to the ninth power in
$\mathbb Q[q]/(q^{16}-q^8+1)$, reverses the coefficients, and applies
the exact Newton multiplication law to the polynomial and its
conjugate. The unit factor $\kappa^9$ cancels. It then verifies that
the $e_3$ coefficient equals (23a). No floating-point sign decision
is used.

These examples do not disprove every eventual positivity statement
with $n$ fixed and $N$ sufficiently large. They do disprove
unrestricted positivity and the particular threshold $N\geq2|n|$.

Finally, the especially simple phase derivative seen for $n=2$ does
not extend by replacing $2$ by $n$. At $N=3$, $n=3$,

\[
 \mathcal H_{3,3}(z)=\frac{z^2+7z-26}{9}+3\sqrt3\,i,
\]

and at its double node $z=1$,

\[
 \frac{\mathcal H_{3,3}'(1)}{\mathcal H_{3,3}(1)}
       =-\frac2{31}-\frac{3\sqrt3}{31}i.                   \tag{24}
\]

Its imaginary part is not the value $-\sqrt3/9$ predicted by the
simple reciprocal-power phase rule. A general formula would need
the actual filled action or an additional finite identity.

## 6. Numerical checks and the unresolved estimate

The proofs in Sections 2–4 are algebraic and elementary analytic
arguments. Numerical checks were used only to detect normalization
errors and investigate possible extensions.

Run the finite verification with

```sh
python3 experiments/audit_terminal_power_qbinomial.py
```

The script requires `mpmath`. At 90 decimal digits, direct triangular
matrix powers and the paired version of (6) were compared for every $3\leq N\leq18$ and $1\leq n\leq8$. The largest
absolute discrepancy was $5.8\times10^{-84}$. The similarity and
square identities were checked in 1,136 lower triangular entries;
their largest discrepancies were $1.2\times10^{-87}$ and
$2.4\times10^{-89}$, respectively. The full Durfee transport identity (21a) was checked at
the same levels with maximum error $9.9\times10^{-88}$. The formulas
(22)–(24) were
computed exactly over $\mathbb Q(\sqrt3,i)$, not inferred from these
floating-point checks.

For orientation, the following table gives
$N^{-1}\log|H_{n,N}(u)|$ at $N=120$, evaluated from (6) at 120
decimal digits. These numbers are samples, not certified limits or
a bound between sample points.

| $n$ | $u=0$ | $u=\pi/4$ | $u=\pi/2$ | $u=3\pi/4$ |
|---:|---:|---:|---:|---:|
| 2 | 0.577382 | 0.552847 | 0.475018 | 0.326265 |
| 3 | 0.840519 | 0.808021 | 0.704191 | 0.501066 |
| 4 | 0.966634 | 0.928979 | 0.808092 | 0.569195 |
| 5 | 1.030574 | 0.989478 | 0.857548 | 0.597848 |
| 6 | 1.065886 | 1.022558 | 0.883692 | 0.611932 |

For $|n|\geq3$, the remaining theorem must establish a contributing
geometric critical point, a nonzero controlled amplitude, and a bound
for the complete finite sum away from that point. The paired formula
(10) reduces the number of internal variables. Proposition 2 removes
the opposite endpoint once the strict action comparison is proved.
The intervening compact interval still requires control of cancellation
in the original finite sum. Neither a quotient norm identity nor the
samples in this table establish that missing estimate.
