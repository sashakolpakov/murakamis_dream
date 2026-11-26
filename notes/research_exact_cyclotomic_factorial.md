# An exact formula for the canonical factorial

This note evaluates the logarithmic derivative of the canonical factorial
as a finite sum. Integrating that sum gives an exact formula in the lower
half-plane, including its additive constant. In particular, its behavior
at large negative imaginary part is determined by the original gamma
product; no unspecified periodic factor remains.

The result concerns the interpolation used in
[`papers/conway-asymptotics/factorial.tex`](../papers/conway-asymptotics/factorial.tex).
It is not by itself an estimate for a quantum sum or a proof that a
correction contour can be discarded.

## 1. Definition and statement

Fix an integer $N\geq2$. For $-1<\Re z<N$, define
\[
 G_N(z)=\left(\frac{2\pi}{N}\right)^z\Gamma(z+1)
 \prod_{m=1}^{\infty}
 \frac{\Gamma(Nm+z+1)}{\Gamma(Nm-z)(Nm)^{2z+1}}.                 \tag{1}
\]
Powers of positive numbers use their real logarithms. The product is
locally normally convergent, is nonzero in this strip, and has $G_N(0)=1$.
Its logarithm is chosen to be zero at $z=0$. These facts also follow
directly from the product: its $m$-th logarithmic factor is
\[
 -\frac{z(z+1)(2z+1)}{6N^2m^2}+O(m^{-3}).                       \tag{2}
\]
The shift relation
\[
 G_N(z+1)=2\sin\frac{\pi(z+1)}N\,G_N(z)                       \tag{3}
\]
continues $G_N$ to a nonzero holomorphic function on $\Im z<0$.
There is a unique logarithm there agreeing with the logarithm of (1) on
the overlap. Write this logarithm as $g_N$.

**Theorem.** The logarithmic derivative is the finite sum
\[
 g_N'(z)=\frac{\pi}{N^2}\sum_{k=0}^{N-1}
 (z-k)\cot\frac{\pi(z-k)}N.                                  \tag{4}
\]
Terms at $z=k$ have their removable values. Formula (4) holds on the
original strip and by continuation wherever both sides are regular.

For $\Im t<0$, put
\[
 L(t)=\frac{i\pi t^2}{2}
       +t\Log(1-e^{-2\pi it})
       +\frac{i}{2\pi}\operatorname{Li}_2(e^{-2\pi it}).       \tag{5}
\]
Here $\Log(1-w)=-\sum_{j\geq1}w^j/j$ and
$\operatorname{Li}_2(w)=\sum_{j\geq1}w^j/j^2$ for $|w|<1$.
Thus the branches in (5) are specified without analytic continuation
across a cut. For every $\Im x<0$,
\[
 \boxed{
 g_N(Nx)=\frac12\log N-\frac{i\pi N}{12}
                 +\sum_{k=0}^{N-1}L\left(x-\frac{k}{N}\right).}
                                                                    \tag{6}
\]

The remainder form of the same identity is
\[
 \begin{split}
 g_N(Nx)={}&\frac{i\pi N x^2}{2}
       -\frac{i\pi(N-1)x}{2}+\frac12\log N\\
 &+i\pi\left(\frac{N}{12}-\frac14+\frac{1}{12N}\right)
       +E_N(x).                                               \tag{7}
 \end{split}
\]
Writing $w=e^{-2\pi ix}$ and $\zeta_N=e^{2\pi i/N}$, the remainder is
exactly
\[
 \boxed{
 E_N(x)=x\Log(1-w^N)
       -\frac1N\sum_{k=0}^{N-1}k\Log(1-w\zeta_N^k)
       +\frac{i}{2\pi N}\operatorname{Li}_2(w^N).}             \tag{8}
\]
Every logarithm and dilogarithm on the right is analytic in the disk
$|w|<1$. The factor $x\Log(1-w^N)$ is displayed separately;
$x$ is still the coordinate on the covering half-plane.

If $r=|w|<1$, one explicit bound is
\[
 |E_N(x)|\leq
 \left(|x|+\frac{1}{2\pi N}\right)\frac{r^N}{1-r^N}
 +\frac{N-1}{2}\frac{r}{1-r}.                                 \tag{9}
\]
For fixed $N$, (9) gives the stated quadratic asymptotic, with error
$O_N((1+|x|)e^{2\pi\Im x})$, as $\Im x\to-\infty$ in any
fixed vertical strip. The explicit bound (9), rather than this shorthand,
also applies when $x$ and $N$ vary simultaneously.

## 2. Finite evaluation of the logarithmic derivative

Let $\psi=\Gamma'/\Gamma$. Logarithmic differentiation of the locally
normally convergent product gives
\[
 g_N'(z)=\log\frac{2\pi}{N}+\psi(z+1)
 +\sum_{m\geq1}\bigl[
 \psi(Nm+z+1)+\psi(Nm-z)-2\log(Nm)\bigr].                      \tag{10}
\]
All manipulations below may first be made away from the isolated poles
of the individual digamma terms. The resulting identities extend across
their removable singularities.

Set
\[
 a_j=\frac{z+1+j}{N},\qquad b_j=\frac{-z+j}{N},
 \qquad 0\leq j<N.                                           \tag{11}
\]
The Gauss multiplication identity, differentiated once, says
\[
 \psi(Nv)=\log N+\frac1N\sum_{j=0}^{N-1}\psi(v+j/N).
                                                                    \tag{12}
\]
Consequently the part of the sum in (10) with $1\leq m\leq K$ is
\[
 \frac1N\sum_{j=0}^{N-1}\bigl[T_K(a_j)+T_K(b_j)\bigr]
                  -2\log\Gamma(K+1),                         \tag{13}
\]
where the functional equation of the digamma function gives the exact
finite identity
\[
 T_K(a):=\sum_{m=1}^K\psi(m+a)
 =(K+a)\psi(K+a+1)-a\psi(a+1)-K.                              \tag{14}
\]
For example, subtracting the expression at $K-1$ from that at $K$
gives $\psi(K+a)$, and the expression at $K=0$ vanishes.

For $a$ in a compact set,
\[
 T_K(a)=K\log K-K+a\log K+a+\frac12-a\psi(a+1)+O(K^{-1}).      \tag{15}
\]
Also
\[
 \frac1N\sum_{j=0}^{N-1}(a_j+b_j)=1.
\]
Substitution of (15) into (13), followed by Stirling's formula for
$\Gamma(K+1)$, therefore gives the limit
\[
 2-\log(2\pi)
 -\frac1N\sum_j\bigl[a_j\psi(a_j+1)+b_j\psi(b_j+1)\bigr]
 =-\log(2\pi)
 -\frac1N\sum_j\bigl[a_j\psi(a_j)+b_j\psi(b_j)\bigr].        \tag{16}
\]
The constants $2$ cancel because $a\psi(a+1)=a\psi(a)+1$.
The error tends locally uniformly to zero. Equations (10) and (16) give
\[
 g_N'(z)=\psi(z+1)-\log N
 -\frac1N\sum_j\bigl[a_j\psi(a_j)+b_j\psi(b_j)\bigr].        \tag{17}
\]

The pairing $b_{N-1-j}=1-a_j$ and the reflection identity
\[
 \psi(1-a)-\psi(a)=\pi\cot(\pi a)
\]
transform the summand into
\[
 a\psi(a)+(1-a)\psi(1-a)
 =\psi(a)+(1-a)\pi\cot(\pi a).
\]
Applying (12) once more cancels $\psi(z+1)-\log N$ in (17). Thus
\[
 g_N'(z)=-\frac\pi N\sum_{j=0}^{N-1}(1-a_j)\cot(\pi a_j).
                                                                    \tag{18}
\]
With $k=N-1-j$, one has $a_j=1+(z-k)/N$; (18) is exactly (4).
This argument starts from (1), rather than from a difference equation,
so it determines the derivative of the specified interpolation.

## 3. Integration and the constant

Direct differentiation of the convergent series in (5) gives
\[
 L'(t)=i\pi t\frac{1+e^{-2\pi it}}{1-e^{-2\pi it}}
      =\pi t\cot(\pi t).                                    \tag{19}
\]
The derivative with respect to $x$ of the sum in (6) is therefore
$N g_N'(Nx)$. Their difference is constant on the lower half-plane.
To determine it, take $x\to0$ from below.

For $0<r<1$, the boundary value from below has
\[
 \Log(1-e^{2\pi ir})=\log(2\sin\pi r)+i\pi(r-1/2).
\]
The elementary Fourier identity
\[
 \Re\operatorname{Li}_2(e^{2\pi ir})
     =\pi^2(r^2-r+1/6)                                      \tag{20}
\]
then gives
\[
 \begin{split}
 \Im L(-r)&=\pi/12,\\
 \Re L(-r)&=-r\log(2\sin\pi r)
       -\frac1{2\pi}\Im\operatorname{Li}_2(e^{2\pi ir}).      \tag{21}
 \end{split}
\]
Identity (20) can be obtained by integrating the imaginary part of
$-\Log(1-e^{2\pi ir})=\sum_{m\geq1}e^{2\pi imr}/m$, first with
an Abel factor less than one. The integration constant is
$\sum_{m\geq1}m^{-2}=\pi^2/6$. All dilogarithm boundary series
converge absolutely. At $r=0$, the term $t\Log(1-e^{-2\pi it})$
tends to zero, so $L(0)=i\pi/12$ in this limiting sense.

In the sum over $r=k/N$, the imaginary parts of the dilogarithms in
the second line of (21) cancel in the pairs $k,N-k$. The same pairing
gives
\[
 \sum_{k=1}^{N-1}\frac{k}{N}\log(2\sin\pi k/N)
     =\frac12\sum_{k=1}^{N-1}\log(2\sin\pi k/N)
     =\frac12\log N,                                        \tag{22}
\]
where the last equality follows by evaluating
$\prod_{k=1}^{N-1}(1-\zeta_N^k)=N$ and taking absolute values.
It follows that
\[
 \sum_{k=0}^{N-1}L(-k/N)=-\frac12\log N+\frac{i\pi N}{12}.
                                                                    \tag{23}
\]
Since $g_N(0)=0$, equation (23) fixes the constant in (6).

## 4. Disk expression and the lower end

Summing the quadratic terms in (6) uses
\[
 \sum_{k=0}^{N-1}\frac{k}{N}=\frac{N-1}{2},\qquad
 \sum_{k=0}^{N-1}\frac{k^2}{N^2}
       =\frac{(N-1)(2N-1)}{6N}.
\]
These sums give the polynomial and constant in (7). The remainder before
resummation is
\[
 E_N(x)=\sum_{k=0}^{N-1}
 \left[
 \left(x-\frac{k}{N}\right)\Log(1-w\zeta_N^k)
 +\frac{i}{2\pi}\operatorname{Li}_2(w\zeta_N^k)
 \right].                                                   \tag{24}
\]
Absolute convergence in the disk proves the root-of-unity identities
\[
 \sum_k\Log(1-w\zeta_N^k)=\Log(1-w^N),\qquad
 \sum_k\operatorname{Li}_2(w\zeta_N^k)
       =\frac1N\operatorname{Li}_2(w^N).                      \tag{25}
\]
There is no additive logarithmic ambiguity: both sides of the first
identity vanish at $w=0$. Substitution gives (8).

The elementary series bounds
\[
 |\Log(1-v)|\leq\frac{|v|}{1-|v|},\qquad
 |\operatorname{Li}_2(v)|\leq\frac{|v|}{1-|v|}
\]
and $\sum k/N=(N-1)/2$ prove (9).

One may equivalently exponentiate (7) and (8):
\[
 \begin{split}
 G_N(Nx)={}&\sqrt N\exp\left\{
 \frac{i\pi N x^2}{2}-\frac{i\pi(N-1)x}{2}
 +i\pi\left(\frac{N}{12}-\frac14+\frac1{12N}\right)\right\}\\
 &\cdot\exp\{x\Log(1-w^N)\}
 \prod_{k=0}^{N-1}\exp\left\{-\frac{k}{N}\Log(1-w\zeta_N^k)\right\}
 \exp\left\{\frac{i}{2\pi N}\operatorname{Li}_2(w^N)\right\}.
                                                               \tag{26}
 \end{split}
\]
The finite product on the second line, excluding the displayed factor
containing $x$, is a nonzero holomorphic function of $w$ at $w=0$,
with value one. Thus (26) records exactly which factor still depends on
the logarithmic covering coordinate. Applications to a source containing
several factorials must combine these factors with the original quadratic
phases before concluding that the source descends to a function of $w$.

## 5. Numerical reproduction

The standalone script
[`experiments/check_exact_cyclotomic_factorial.py`](../experiments/check_exact_cyclotomic_factorial.py)
checks the finite formula against truncated versions of the original
gamma product and its logarithmic derivative. It also checks the lattice
normalization, shift, reflection, equality of (6) and (8), and the explicit
bound (9). Run

```sh
python3 experiments/check_exact_cyclotomic_factorial.py --output repro/results/research-exact-cyclotomic-factorial.json
```

The saved values are in
[`repro/results/research-exact-cyclotomic-factorial.json`](../repro/results/research-exact-cyclotomic-factorial.json).
These finite-precision calculations are diagnostics; the proof is the
finite digamma calculation and the determination of its constant above.

## 6. Relation to the existing cyclic dilogarithm

The weighted finite product in (26) is the inverse of the cyclic
dilogarithm
\[
 D_N(w;\zeta_N)=\prod_{k=1}^{N-1}(1-w\zeta_N^k)^{k/N},
 \qquad D_N(0;\zeta_N)=1,
\]
with its local branches fixed at zero. This is an established function;
see equation (9) and Section 1.2 of Garoufalidis and Kashaev,
[*Evaluation of state integrals at rational points*, version 2](https://arxiv.org/pdf/1411.6062v2).
That paper also treats formulas at roots of unity in Section 1.4.

This attribution concerns the known finite product. The proof above
derives the specified Gamma interpolation, its constant and its
logarithmic covering factor directly. Its application here is to the
original finite source and the precise contour correction in
[the adjacent-pair translation calculation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_adjacent_pair_cyclotomic_gauge.md).
