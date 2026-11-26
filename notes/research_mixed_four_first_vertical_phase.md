# Vertical decrease at a type-four left argument

Research deduction, 5 November 2026. The unused second-tangent gain
in the ending-four collar comparison pays the following edge's entire
vertical **phase** remainder, including either selected Fourier branch.
The proof uses two exact small Bernstein tables and no new root cover.
A complete finite upper-rate bound on this vertical path is still a
separate source obligation; no full-collar finite comparison follows
from phase continuation alone.

## 1. The real-endpoint marginal

Use the original phases and right-half-plane logarithms of
[the acute-gradient theorem](research_mixed_acute_gradient_height_transfer.md).
For the left argument of type four,
\[
 \phi_{1\epsilon,a}
  =\log_{\rm R}(S+P)-\log_{\rm R}(S-i)-\tfrac12g'(a),
 \quad P=\cot\pi a,
 \quad S=\cot\pi s_*,\quad \epsilon\in\{0,1\}.          \tag{1}
\]
The original selected root satisfies \(\Re S>0,|\Im S|<1\).
At real \(a\in(0,1/2]\), write \(p=\cot\pi a\ge0\)
and \(Q=q+i\beta\) for the other outer cotangent, with
\(q>0\). For \(\epsilon=0\) take \(|\beta|\le.37\);
for \(\epsilon=1\) take \(0\le\beta\le.61\).
The quadratic chamber from the
[four-three proof](research_mixed_four_three_cap_collar.md)
and the one-sided cubic chamber from the
[ending-four proof](research_mixed_second_four_cap_collar.md)
give the original strip branch throughout these connected domains.
Their boundary arguments also permit \(p=0\), with \(q>0\).

**Lemma 1.** If \(0\le p\le\sqrt5/2\), then
\[
                         \Im\phi_{1\epsilon,a}(a,b)>0.  \tag{2}
\]
This is a statement about the calibrated phase, not a derivative
of an absolute-row maximum.

*Proof.* Write \(S=u+iv\). The imaginary numerator of
\((S+p)/(S-i)\) is \(u+p(1-v)>0\). Hence its continuous
right-half-plane argument difference \(\theta\) lies in
\((0,\pi)\). At a real left argument,
\(\Im g'(a)=\arctan p\), so a zero of (2) would require
\(\theta=\tfrac12\arctan p\). For \(p>0\), set
\[
 t=\tan(\tfrac12\arctan p),\quad T=t^2,\quad
 p=\frac{2t}{1-t^2},\quad 0<T\le1/5.
\]
That zero has the necessary equation
\[
 G=u+p(1-v)-t(u^2+up+v^2-v)=0.                         \tag{3}
\]

For the quadratic critical equation, solve exactly for
\[
 Q_0=\frac{1-S^2-p(S-i)}{S+i},\qquad
 \Re Q_0=\frac{n_0}{u^2+(v+1)^2},\quad
 n_0=u\{2-u^2-(v+1)^2\}+p(1-u^2-v^2).                \tag{4}
\]
Reduction by (3) gives the exact identity, on \(G=0\),
\[
\begin{split}
 t^2(1-T)n_0={}&
 u\{T(3T-1)v-(1-T)^2\}\\
 &+t(v-1)\{(1-3T)v+2(1-T)\}<0.                       \tag{5}
\end{split}
\]
Indeed the first brace is at most
\(-1+3T-4T^2=-4(T-3/8)^2-7/16<0\), while the second
is at least \(1+T>0\). Here \(u,t>0\), \(-1<v<1\),
and \(T\le1/5<1/3\). Thus \(\Re Q_0<0\), contrary
to \(q>0\).

For the cubic write
\[
 D=(S+i)(S+p)-2i(p-i),\quad
 N=S(S+i)(S+p)+2(p-i),\quad Q_1=-N/D.                 \tag{6}
\]
At a strip root \(D\ne0\): if \(D=0\), the critical
equation would also give \(N=2i(p-i)(S-i)=0\), impossible
when \(u>0\). Put \(n_1=-\Re(N\overline D)\), so
\(\Re Q_1=n_1/|D|^2\). On (3), exact polynomial division gives
\[
             t^4(1-T)^2n_1=-uA(T,v)+t(v-1)B(T,v).     \tag{7}
\]
The two polynomials are
\[
\begin{split}
 A={}&11T^4v^2-T^4v-2T^4-11T^3v^2+21T^3v+T^3\\
     &+9T^2v^2-11T^2v+T^2-Tv^2-Tv-T+1,\\
 B={}&16T^3v^2+5T^3v+4T^3-16T^2v^2-29T^2v+2T^2
                                      -Tv+v+2.
\end{split}                                                   \tag{8}
\]
Define \(B_i^n(x)=\binom ni x^i(1-x)^{n-i}\). In tensor
Bernstein form after \(T=x/5,v=2y-1\), the following matrices
have row index \(i\) and column index \(j\): they give
\(A(x/5,2y-1)=\sum_{i=0}^4\sum_{j=0}^2a_{ij}B_i^4(x)B_j^2(y)\)
and
\(B(x/5,2y-1)=\sum_{i=0}^3\sum_{j=0}^2b_{ij}B_i^3(x)B_j^2(y)\).
The coefficient matrices are
\[
\begin{split}
 A:\quad&
 \begin{pmatrix}
 1&1&1\\
 19/20&1&17/20\\
 26/25&71/75&52/75\\
 151/125&108/125&69/125\\
 176/125&472/625&288/625
 \end{pmatrix},\\
 B:\quad&
 \begin{pmatrix}
 1&2&3\\
 16/15&2&44/15\\
 4/3&56/25&172/75\\
 48/25&328/125&32/25
 \end{pmatrix}.
\end{split}                                                   \tag{9}
\]
On \([0,1]^2\) these tensor basis weights are nonnegative
and sum to one, by the binomial theorem. Thus
\(A\ge288/625>0\), \(B\ge1\) on the entire rectangle.
Equation (7) gives \(\Re Q_1<0\), again a
contradiction. These are exact rational polynomial bounds, not a
root or parameter-grid test.

At \(p=0\), the half-factorial argument is zero and
\(\theta>0\), so (2) holds. The root and original logarithms
continue along \(p\in[0,\sqrt5/2]\) with the other cotangent
fixed in its stated chamber. Equations (5)--(9) exclude every zero
of (2); its sign therefore remains positive. \(\square\)

## 2. The whole actual vertical phase path

Assume the word has at least three retained coordinates. Suppose its
second type is four and write that reference as \(r_2=b+ic\).
Keep the next reference \(r_3\) unchanged and unselected. The actual
universal ordinary/private unions are
\[
 .24<b<.363,\quad -.102<c<-.001;\qquad
 \begin{cases}
 .267<\Re r_3<.438,\ -.065<\Im r_3<.068,&\epsilon=0,\\
 .24<\Re r_3<.363,\ -.102<\Im r_3<-.001,&\epsilon=1.
 \end{cases}                                                 \tag{10}
\]
Use \(z=b+ik\) with \(c\le k\le H=.014\). For its
cotangent and the other argument's cotangent,
\[
 -.1<\Im\cot\pi z<.61,
 \quad
 \begin{cases}
 |\Im\cot\pi r_3|<.37,&\epsilon=0,\\
 0<\Im\cot\pi r_3<.61,&\epsilon=1.
 \end{cases}                                                 \tag{11}
\]
The negative-height comparisons are already proved in the two collar
notes. The positive endpoint adds only the fixed scalar bound
\[
 \frac{\sinh(.028\pi)}
      {\cosh(.028\pi)-\cos(.48\pi)}<.1.                 \tag{12}
\]
For the quadratic the earlier imaginary-axis estimate still uses
its maximum first imaginary part \(.61\) and the other modulus
\(.37\), giving \(1243/1250<1\). Allowing the first part
down to \(-.1\) only improves that axis bound; both full
horizontal-side signs remain strict. For the cubic, (11) lies in
the one-sided chamber of Lemma 1 of the ending-four note. The
original strip branches and positive triangle/Schur forms therefore
hold along the **entire** path, not just at the reference.

At \(k=0\),
\(p=\cot\pi b<\cot(.24\pi)<11/10<\sqrt5/2\).
Lemma 1 gives the negative vertical derivative
\[
 \frac{d}{dk}\Re\phi_{1\epsilon}(b+ik,r_3)\big|_{k=0}
                         =-\Im\phi_{1\epsilon,a}(b,r_3)<0.
                                                               \tag{13}
\]
The negative real Hessian gives vertical convexity, so this derivative
is no larger at any \(k\le0\). Consequently
\[
 \Re\phi_{1\epsilon}(b+ik,r_3)
       \le\Re\phi_{1\epsilon}(r_2,r_3),\qquad c\le k\le0.
                                                               \tag{14}
\]

For a selected second coordinate retain the true allocated Fourier
alternatives. Put \(\psi=\phi_{1\epsilon}+g(z)/2\), which
removes only the first argument's Fourier halfweight. The selected
phase envelope is exactly
\[
 e_1(k)=\max\{\Re\phi_{1\epsilon}(b+ik,r_3)-\pi k,
                              \Re\psi(b+ik,r_3)\}.
                                                               \tag{15}
\]
The first branch is the factorial contribution with its selected
monomial; the second is the forced-frequency contribution. No
branch is dropped. On (11), the bare marginal has angle
\[
 \theta(k)=\Im\{\log_{\rm R}(S+P)-\log_{\rm R}(S-i)\}>0,
\]
because its ratio's imaginary numerator is
\(u(1+\Im P)+\Re P(1-v)>0\). Also
\(0<\Im g'(b+ik)<\pi\). The two derivatives in (15) are
therefore respectively
\[
 -\theta(k)+\tfrac12\Im g'(b+ik)-\pi<0,
                         \qquad -\theta(k)<0.           \tag{16}
\]
Both branches decrease for \(0\le k\le H\). At zero,
\(J(b)<0\), so the first is larger and
\(e_1(0)=\Re\phi_{1\epsilon}(b,r_3)\). Thus
\[
             e_1(k)\le\Re\phi_{1\epsilon}(r_2,r_3),
                              \qquad0\le k\le H.        \tag{17}
\]
For the unselected negative-height interval the actual Fourier
factorial rate is \(-\Re g(z)>0\), whereas its forced rate
\(2\pi k_+\) is zero throughout \([c,0]\).
Hence (14) is precisely its allocated coherent/Fourier phase bound.

## 3. What the tangent pays, and the remaining source hypothesis

Let \(P_2\) denote the second marginal of the first-pair phase
in the ending-four theorem. Its equations (23)--(24) prove the
stronger first-pair upper rate \(M_\alpha-1/20\), before
the favorable supporting tangent is added. Thus relative to that
plane the retained debit is
\(1/20+(k-c)(-\Im P_2)\). Original stationarity gives
\(\phi_{1\epsilon,a}(r_2,r_3)=-P_2\). Set
\(\Delta=k-c\ge0\). The unused first-pair supporting-plane gain is
\(\Delta(-\Im P_2)\). The following allocated phase's tangent
change is \(\Delta\Im P_2\). These cancel exactly.
Thus paying its Taylor remainder with that unused gain is equivalent
to the full rate comparison (14) or (17), which is now proved.
There is no phase need for a small reset or for an unselected second
coordinate in this comparison at the unchanged next reference.

For a finite-source consequence, however, one still needs the
following explicit **upper** bound, uniformly over (10)--(11):
\[
 \begin{split}
 &|C_{\epsilon,N}(e^{-2\pi iz},e^{-2\pi ir_3})|
 |d_N(e^{-2\pi iz})e^{2\pi iN\sigma z}|^{1/2}
 |d_N(e^{-2\pi ir_3})|^{\epsilon/2}\\
 &\hspace{15mm}\le C_\eta N^A\exp N\{e_\sigma(k)+\eta\},
 \end{split}                                                   \tag{18}
\]
where \(e_0=\Re\phi_{1\epsilon}\) on \([c,0]\), and
\(e_1\) is (15) on \([0,H]\). A complete nonzero asymptotic
is not required; all original rows, aliases and forcing must still
be bounded. If (18) is established, combining it with the full
ending-four pair estimate leaves its \(1/20\) gap, apart from
one arbitrary final source tolerance, at fixed \(\Re z=b\)
and \(z_3=r_3\).

The existing reduced-disk packets give an ambient germ at the actual
conditional image, not automatically (18) on the full vertical path.
The independent right packets have narrower height hypotheses;
near-left actual third references in (10) can exceed those bands.
The analytic chamber and monotonicity proof do not enlarge either
finite-source theorem. Establishing (18), or a sufficient weaker
upper allowance smaller than the retained pair gap, remains the
precise finite-source obligation.

## Reproduction

The focused checker
[`check_mixed_four_first_vertical_phase.py`](../experiments/check_mixed_four_first_vertical_phase.py)
verifies the exact numerator reductions, all 27 displayed Bernstein
coefficients, current inherited path bounds and the fixed scalar
comparisons. It performs no root search or parameter cover:

```sh
python3 experiments/check_mixed_four_first_vertical_phase.py --precision 256
```

The canonical record is
[`research-mixed-four-first-vertical-phase.json`](../repro/results/research-mixed-four-first-vertical-phase.json).
Its scope explicitly records that (18) has not been proved.
