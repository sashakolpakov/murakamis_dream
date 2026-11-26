# The complete early first 3,3 pair at sufficiently negative first height

Private research proof, 10 November 2026. Retaining the radial smoothing
of the first numerator pays the remaining wrapped high rows when the
actual first retained height is at most \(-3/50\). The second height may
have either sign. A separate sufficient region is given by a lower bound
on the original reflected drift. Both deductions compare the original
absolute row rates and then use the already calibrated complete cap.

## 1. Fixed actual source and the remaining rows

Fix an actual positive three/four open word of length at least three
beginning with \(3,3\). Use precisely the fixed reference and targets of
[the first33 outer-row theorem](research_mixed_early_three_outer_high_blocks.md):
\[
 a_*=a_0+ic,\qquad b_*=b_0+id,\qquad
 a=x+ic,\quad b=z+id,
\]
\[
 1/10\le x\le11/50,\qquad 11/50\le z\le9/20,
 \qquad -.072<c<.021,\quad -.065<d<.068.
\tag{1}
\]
The heights belong to the same original geometric solution. Let
\(q_N=e^{-2\pi i/N}\), \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi ib}\), and
retain the complete first cap \(U_{0,N}(w,X)\) and exact ordinary rows
\[
 R_{j,N}(a,b)=X^{-j}
 \frac{(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^2},
 \qquad C_{0,N}(X,Y)=\sum_{j=0}^{N-1}R_{j,N}(a,b).
\tag{2}
\]
There is no type-four Fourier weight at either of these coordinates.
The external scalar, all later factors and every original logarithmic
lift are unchanged.

Write \(E_0(s)\) for the full continuous absolute row rate, including
the chirp \(X^{-j}\), as in equation (4) of the outer-row theorem.
Its exact last rate is
\[
 E_0(1)=\lambda,\qquad
                    \lambda=2\pi\{(-c)_++d_+\}.
\tag{3}
\]
The continuous endpoint \(1\) is a rate, not an additional finite row.
That theorem already pays the full complete-cap product on
\[
 [1/2,s_L(z)]\ \cup\ [1-x,1],\qquad
                    s_L(z)=\max(2/3,1-z).
\tag{4}
\]
The only remaining continuous high interval has
\[
 s=1-v,\qquad x<v<\min(z,1/3).
\tag{5}
\]
In particular its closure is contained in \(1/10\le v\le1/3\),
and every such row has \(v\le z\).

## 2. Retaining the radial improvement

Use the original radial primitive of
[the reflection theorem](research_mixed_right_tail_reflection.md):
\[
 G_H(t)=\Re g(t-iH),\quad H\ge0,\qquad
 G_H'(t)=f_H(t)=\log|1-e^{-2\pi H-2\pi it}|.
\tag{6}
\]
Here \(G_0=J\), and \(G_H\) is odd and one-periodic. On
\([0,1/2]\), \(f_H\) increases with its argument and
\(J\le G_H\le0\). Let
\[
 \Phi(v)=E_0(1-v)-E_0(1),\qquad
 h(v)=J(v)-2J(v/2),\qquad
 A_H(v)=2\{G_H(v/2)-J(v/2)\}\ge0.
\tag{7}
\]
The exact reflected identity is
\[
 \Phi(v)=G_{|c|}(x-v)-G_{|c|}(x)
        +G_{|d|}(z-v)-G_{|d|}(z)+2J(v)-\lambda v.
\tag{8}
\]
For \(0\le v\le z\), the first arc \([x-v,x]\) is contained in
\((-1/2,1/2)\). An even integrand increasing with absolute argument
has its least integral on the centered arc of the same length. The
second arc \([z-v,z]\subset[0,1/2]\) has integral at least
\(G_{|d|}(v)\). Therefore
\[
 \begin{split}
 \Phi(v)&\le-2G_{|c|}(v/2)-G_{|d|}(v)+2J(v)-\lambda v\\
        &\le h(v)-\lambda v-A_{|c|}(v).
 \end{split}
\tag{9}
\]
This retains the first radial term that was discarded in the outer-row
theorem's equation (21). It changes no actual contour height.

For \(0<t<1/2\), the number \(1-e^{-2\pi H-2\pi it}\) has
positive real and imaginary parts. Its original logarithm therefore
has imaginary part in \((0,\pi/2)\). Factoring that number as
\(2e^{-\pi H-i\pi t}\sinh(\pi H+i\pi t)\), and retaining
\(g'(t-iH)=\Log(1-e^{-2\pi H-2\pi it})\), gives the exact identity
\[
 \partial_HG_H(t)=\Im g'(t-iH)
 =\frac\pi2-\pi t-\arctan\{\tanh(\pi H)\cot(\pi t)\}>0.
\tag{10}
\]
The arctangent is its real principal value. At \(H=0\) the identity
holds by its limit at fixed \(t>0\); no logarithmic lift is changed.
In particular \(A_H(v)\) increases with \(H\).

Let \(H_0=3/50\). Since \(\arctan u\le u\),
\(\tanh u\le u\) for \(u\ge0\), and
\(\cot y\le1/y\) for \(0<y<\pi/2\), equation (10) gives
\[
 \begin{split}
 A_{H_0}(v)
 &=2\int_0^{H_0}
   \left[\frac{\pi(1-v)}2
       -\arctan\{\tanh(\pi H)\cot(\pi v/2)\}\right]dH\\
 &\ge\pi H_0(1-v)-\frac{2H_0^2}{v}
   =\frac{3\pi}{50}(1-v)-\frac9{1250v}.
 \end{split}
\tag{11}
\]
Only the auxiliary primitive is integrated in (11). The original
source still has the fixed actual values \(c,d\).

The other term in (9) satisfies
\[
 h'(v)=\log(2\cos(\pi v/2)),\qquad
 h(v)\le v\log2-\frac{\pi^2v^3}{24}.
\tag{12}
\]
Indeed \(\tan u\ge u\) implies \(\log\cos u\le-u^2/2\);
integrate this inequality from zero to \(v\). Its domain includes
every \(v\) in (5).

## 3. The negative-height region

**Lemma 1.** If the actual first height satisfies \(c\le-3/50\),
then every row in (5) has
\[
                       E_0(1-v)<E_0(1)-\frac{403}{45000}.
\tag{13}
\]
There is no condition on the sign of \(d\).

*Proof.* Put \(H=-c\ge H_0\). Then \(\lambda\ge2\pi H_0\),
and (10) implies \(A_H\ge A_{H_0}\). Equations (9), (11) and
(12) yield
\[
 \Phi(v)\le v\log2-\frac{\pi^2v^3}{24}
               -\frac{3\pi}{50}(1+v)+\frac9{1250v}.
\tag{14}
\]
Use \(\log2<7/10\), \(\pi>25/8\) and \(\pi^2>9\).
The logarithm bound follows from the first five positive terms of
\(e^{7/10}>2\); the elementary \(\pi\) bound is weaker than
the one used in the original transport proofs. Thus, on
\([1/10,1/3]\),
\[
 \Phi(v)<g(v):=\frac{41}{80}v-\frac3{16}
                      +\frac9{1250v}-\frac38v^3.
\tag{15}
\]
For \(w=v^2\),
\[
 g'(v)=-\frac{Q(w)}w,\qquad
 Q(w)=\frac98w^2-\frac{41}{80}w+\frac9{1250},
\]
\[
 Q'(w)=\frac94w-\frac{41}{80}
              \le-\frac{21}{80}<0
                     \quad(1/100\le w\le1/9).
\tag{16}
\]
Consequently the sign of \(g'\) can change only from negative to
positive. An interior critical point cannot be a maximum. The exact
endpoint identities are
\[
 g(1/10)=-\frac{517}{8000},\qquad
 g(1/3)=-\frac{403}{45000},\qquad
                  g(1/10)<g(1/3)<0.
\tag{17}
\]
Equations (15)--(17) prove (13). All comparisons are written rational
inequalities; no source value or polynomial maximum is evaluated.
\(\square\)

There is also an independent drift region.

**Lemma 2.** At any actual heights in (1), if
\[
                              \lambda\ge\log2,
\tag{18}
\]
then every row in (5) satisfies
\[
                         E_0(1-v)<E_0(1)-\frac3{8000}.
\tag{19}
\]

*Proof.* Equations (9), (12), \(A_{|c|}\ge0\), and (18) give
\(\Phi(v)\le-\pi^2v^3/24\). Since \(v\ge1/10\) and
\(\pi^2>9\), this is strictly less than \(-3/8000\).
The drift is the literal correlated expression (3), not an independent
parameter assigned to a fixed numerator. \(\square\)

## 4. Complete finite first-pair consequence

Retain the original plane and gap
\[
 \begin{split}
 \Gamma(z)&=\Re L_0(a_*)+\Re\phi_{00}(a_*,b_*)
   +\Re\partial_b\phi_{00}(a_*,b_*)(z-b_0)-\kappa(z-b_0)^2,\\
 \kappa&=1/2500000,\qquad
                     \gamma_* =\kappa(a_0-11/50)^2>0.
 \end{split}
\tag{20}
\]
Here \(L_0,\phi_{00}\), all primitives and additive constants are
exactly those of the joint low- and central-source theorems. The
first-coordinate marginals cancel at the original geometric solution.

**Theorem 3.** Under (1), assume either \(c\le-3/50\) or (18).
For every \(\tau>0\), both level parities obey
\[
 |U_{0,N}(w,X)|\sum_{j=\lceil N/2\rceil}^{N-1}|R_{j,N}(a,b)|
       \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}},
\tag{21}
\]
and the complete pair satisfies
\[
 |U_{0,N}(w,X)C_{0,N}(X,Y)|
       \le C_\tau N^{A_\tau}e^{N\{\Gamma(z)-\gamma_*+\tau\}}.
\tag{22}
\]
These hold on a sufficiently small fixed ordinary-color neighborhood
of \(w=-2\), including every fixed color derivative on a smaller
neighborhood. No sign restriction on the private ordinary height is
required.

*Proof.* The outer-row theorem controls (4). For the remaining interval
(5), either (13) or (19) bounds each rate by the literal last rate at
the same targets. Lemma 1 of that theorem already places every complete
cap profile plus that last rate below \(\Gamma-2\gamma_*\).
This includes both aliases, the extra positive-height physical allowance
when present, and the separate true cap ends. No cap term or finite
ordinary row is removed.

Apply the original zero-safe finite-product upper estimate uniformly at
every physical index. Continuous rate comparisons cover rounded cut
indices without comparing them to possibly vanishing finite endpoint
values. Summing at most \(N\) high rows costs a polynomial, and the
source tolerances can be chosen within \(\tau\) and the reserve between
\(2\gamma_*\) and \(\gamma_*\). This proves (21), first uniformly
over the entire real ordinary-color interval.

The exact remaining finite partition is
\[
 \begin{split}
 &0\le j\le\lfloor3N/20\rfloor,\\
 &\lfloor3N/20\rfloor+1\le j\le\lceil N/2\rceil-1,\\
 &\lceil N/2\rceil\le j<N.
 \end{split}
\tag{23}
\]
The low block has the stronger joint gap \(1/2000\). For the central
block use the original central-source theorem at nonpositive private
height and the first33 positive-private-height theorem at nonnegative
private height. Both give the gap \(\gamma_*\), retain every cap
profile and every ordinary zero-mode join and alias, and agree at zero
private height. Adding their bounds to (21), with one total tolerance,
proves (22).

The all-real cap bounds and its degree less than \(N\) give a fixed
ordinary-color neighborhood at any prescribed additional exponential
cost. Intersect this neighborhood with those of the low and central
estimates, and use Cauchy's formula on smaller disks for fixed color
derivatives. The base height inequalities are imposed only on the
original reference; they are not assertions about a color-dependent
critical point. No color-independent multiplier or Fourier factor is
divided out. All external scalars and both parity partitions are
unchanged. \(\square\)

This is a complete first33 bound on the early fixed-height targets for
the two stated actual-height regions. It does not claim that all actual
references lie in them, or estimate changing-height joins, other outer
intervals or the full open word. No closed-knot or finite-exception
conclusion is asserted.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_right_tail_reflection.md | e3928f2d9549159f6955c654b202dc87198137f4cfdb80f85151af567a976ce1 |
| research_mixed_early_three_outer_high_blocks.md | ece4f34c6dbe288649ff45b54acb705e50b0dc0d63926263ff26eb644d694c3f |
| research_mixed_early_joint_low_tail.md | 72ee3edebe390f213751e7774913d7d6552d6eff3bdea61b13f4d23159ad6606 |
| research_mixed_early_joint_central_source.md | f19a7b5c42a4f372e9671c95dec5670f501065802fa96279b542efaa5005aec3 |
| research_mixed_early_three_positive_private_central.md | d7f54fc0a20c5ccce15b028d16dbcaee2ef0eefbea70795089da097c9730635e |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |

All directly used source statements and proofs were read. This is
written analysis only, without mathematical numerical evaluation,
saved-value arithmetic, import, compilation, test or frozen-source edit.
