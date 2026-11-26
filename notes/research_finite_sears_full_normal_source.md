# A finite Sears certificate for the actual local full-normal source

Private written proof, 16 November 2026.

The terminating Sears expression for a physical kernel row has a
four-factorial lift. An explicit finite telescoper identifies its
degree derivative with the original consumed-normal representative.
Consequently appropriate local cutoffs give all four physical jets of
the original kernel, including its independent mixed normal. The
diagonal factorial divisor is retained throughout.

This is an exact local source statement. It does not bound a tall
wire contour, eliminate its endpoint packets, or assert that one
cutoff is holomorphic on the whole angular box.

## 1. Original data and the canceled finite row

Set
\[
 N\ge2,\quad D=N-1,\quad \theta=\pi/N,\quad q=e^{i\theta},
 \quad Q=q^2,\quad s_z=2\sin(\theta z),
 \quad c(z)=2\cos((2z+1)\theta),\quad c_0=q+q^{-1}.
 \tag{1}
\]
All powers of \(Q\) use \(Q^z=e^{2i\theta z}\).
The original kernel and physical rows are
\[
 K_N(z,w)=\sum_{k=0}^{D}e_k(z)e_k(w),\qquad
 F_j(w)=K_N(c(j),w),\qquad 0\le j\le J=\lfloor D/2\rfloor.
 \tag{2}
\]
A first spectral normal is required only for
\(0\le j\le J_d=\lfloor(N-2)/2\rfloor\).

Let \(G=G_N\) be the specified canonical factorial in the pinned
factorial source. Its normalization and exact shift are
\[
 G(0)=1,\qquad G(z+1)=s_{z+1}G(z).
 \tag{3}
\]
It is a holomorphic unit on \(-1<\Re z<N\). Its finite logarithmic
derivative formula also gives the exact reflection
\[
                         G(z)G(D-z)=N.                 \tag{4}
\]
Indeed that formula is invariant under \(z\mapsto D-z\), so the
derivative of the logarithm of the left side is zero. At zero its
value is \(G(D)=\prod_{r=1}^{N-1}2\sin(r\theta)=N\).
Continuation proves (4) wherever defined. From (3), \(G\) has a
simple pole at each \(-1,\ldots,-D\), and its reciprocal is
holomorphic with a simple zero there. These are local divisor
statements, not an assertion that the reciprocal is entire.

For an angular variable \(u\), put
\[
 C_k^\pm(u)=\prod_{r=0}^{k-1}
       \frac{\cos(u/2\pm(r+1/2)\theta)}{\sin((r+1)\theta)},
 \qquad C_0^\pm=1.
 \tag{5}
\]
Then the exact physical row has the canceled convolution
\[
 \boxed{\quad F_j(-2\cos u)
       =\sum_{k=0}^j[C_k^+(u)C_{j-k}^-(u)]^2.\quad}       \tag{6}
\]
In particular there are no spectral denominators in this finite
formula. It is even in \(u\), by interchanging \(k\) and \(j-k\).

Here is the normalization directly from the finite Sears identity.
Write \(w=v+v^{-1}\), with \(v=-e^{iu}\). Converting the original
Newton products to Pochhammers gives
\[
 F_j(w)={}_4\phi_3(Q^{-j},Q^{j+1},qv,q/v;Q,Q,Q;Q,Q).
 \tag{7}
\]
The pinned finite identity, retaining the parameter \(qv\), gives
\[
 F_j(w)=(qv)^j\left[\frac{(q/v;Q)_j}{(Q;Q)_j}\right]^2
 \sum_{k=0}^j Q^k
 \left[\frac{(Q^{-j};Q)_k(qv;Q)_k}
 {(Q;Q)_k(qvQ^{-j};Q)_k}\right]^2.                \tag{8}
\]
This first holds away from its apparent spectral poles. The phase
in each quotient of four factors \(1-e^{i\varphi}\) is
\(e^{-i\theta}\); its square cancels \(Q\). The phase in the
prefactor similarly cancels \((qv)^j\). Its cosine product has
indices \(0,\ldots,j-1\). The denominator cosine product of the
\(k\)-th term has precisely its last \(k\) indices, in reverse
order. Canceling them, and then canceling the corresponding sine
factorials, gives (6). Thus (6) also holds at every removable
spectral pole of (8). No phase or scalar carrier is left over.

## 2. The four-factorial lift and its necessary local domain

For independent complex degree variables \(\alpha,\beta\), define
the meromorphic summand
\[
 T_k(\alpha,\beta)=
 \frac{G(\alpha+\beta-k)^2}
 {G(\alpha-k)^2G(\beta-k)^2G(k)^2},\qquad 0\le k<N.
 \tag{9}
\]
It is symmetric in \(\alpha,\beta\). By (4), equivalently
\[
 T_k(\alpha,\beta)=
 \frac{N^2}
 {[G(k)G(\alpha-k)G(\beta-k)
                         G(D-\alpha-\beta+k)]^2}.          \tag{10}
\]
These are identities of meromorphic functions; apparent factors
are combined before a limiting value is taken.

For \(\beta=D/2-Nu/(2\pi)\), one has \(c(\beta)=-2\cos u\).
The shift formula gives
\[
 C_k^+(u)=\frac{G(\beta)}{G(\beta-k)G(k)},\qquad
 C_l^-(u)=\frac{G(\beta+l)}{G(\beta)G(l)}.
 \tag{11}
\]
Consequently (6) is exactly
\[
                 F_j(c(\beta))=\sum_{k=0}^jT_k(j,\beta).
 \tag{12}
\]
Its interpretation at exceptional factors is the holomorphic
continuation supplied by (6).

The diagonal divisor must not be suppressed. For example at
\((\alpha,\beta)=(0,0)\), a term with \(1\le k<N\) has a
nonzero holomorphic unit times
\[
                         \frac{\alpha^2\beta^2}{(\alpha+\beta)^2}.
 \tag{13}
\]
Separate vanishing in either variable therefore does not give a
joint holomorphic germ there.

We will use the finite cutoff
\[
                         S_M(\alpha,\beta)=\sum_{k=0}^MT_k(\alpha,\beta).
 \tag{14}
\]
At a physical pair \((j,l)\), the safe local condition is
\[
                \max(j,l)\le M\le j+l,\qquad M<N.
 \tag{15}
\]
Every numerator argument in (9) then has nonnegative base value,
and every reciprocal denominator is holomorphic near its base
integer, which is less than \(N\). Thus (14) is jointly
holomorphic on a neighborhood of that pair. Equivalently, a
sufficient open restriction for the numerator is
\(\Re(\alpha+\beta)>M-1\); all other factors retain their
own local pole exclusions. No full-box assertion follows.

## 3. An explicit finite contiguous certificate

Use the original coefficients
\[
 A(\alpha)=\frac{s_{\alpha+1}^4}{s_{2\alpha+1}s_{2\alpha+2}},
 \qquad C(\alpha)=\frac{s_\alpha^4}{s_{2\alpha}s_{2\alpha+1}},
 \qquad C(0)=0.
 \tag{16}
\]
The following is a meromorphic finite identity, so it can first
be checked where all displayed denominators are nonzero.

Put
\[
 X=Q^\alpha,\quad Y=Q^\beta,\quad z=Q^k,\quad s=QX,
 \quad \mathcal D=(1-Xs)(1+s)(1+X),
 \quad \mathcal K=\frac{q^{-1}s^2}{Y\mathcal D},\quad \xi=z/s,
 \tag{17}
\]
and define the Laurent polynomial
\[
 \begin{split}
 \mathcal P(z)=\mathcal K\big[&
 2\{(1+X)-(1+s)Y\}\xi\\
 &+(1+s)(1+X)(Y^2-1)-4(X-s)Y\\
 &+2Y\{X(1+s)-s(1+X)Y\}\xi^{-1}\big].
 \end{split}
 \tag{18}
\]
The exact flux is
\[
 \mathcal H_k(\alpha,\beta)=T_k(\alpha,\beta)
                          \frac{(1-Q^k)^2\mathcal P(Q^k)}{(Q^k-QX)^2}.
 \tag{19}
\]
The summand and rational factor in (19) are combined before
specializing. In particular a zero of the summand is not counted
before checking the denominator in the flux.

**Proposition 1.** Where its terms are defined, the finite sum obeys
\[
 \boxed{\begin{split}
 &A(\alpha)S_M(\alpha+1,\beta)+C(\alpha)S_M(\alpha-1,\beta)\\
 &\quad-[A(\alpha)+C(\alpha)+c_0-c(\beta)]S_M(\alpha,\beta)
                         =\mathcal H_{M+1}(\alpha,\beta).
 \end{split}}                                                \tag{20}
\]
It is enough here to use \(M+1<N\). The right side is the
actual finite boundary, not an infinite-series limit.

*Proof.* The shift relation gives the three exact ratios
\[
 \frac{T_k(\alpha+1,\beta)}{T_k(\alpha,\beta)}
       =Y^{-1}\frac{(z-QXY)^2}{(z-QX)^2},\qquad
 \frac{T_k(\alpha-1,\beta)}{T_k(\alpha,\beta)}
       =Y\frac{(z-X)^2}{(z-XY)^2},
 \tag{21}
\]
\[
 \frac{T_{k+1}}{T_k}
       =Q\frac{(z-X)^2(z-Y)^2}{(1-Qz)^2(z-XY)^2}.
 \tag{22}
\]
Thus the flux difference divided by \(T_k\) is
\[
 \frac{\mathcal H_{k+1}-\mathcal H_k}{T_k}
 =\frac{(z-Y)^2\mathcal P(Qz)}{Q(z-XY)^2}
                   -\frac{(1-z)^2\mathcal P(z)}{(z-QX)^2}.
 \tag{23}
\]
We verify that this equals the expression obtained from the left
side of (20) using (21).

Here are explicit checks of the rational identity, including its
simple poles. Write \(s=QX\). The required values and logarithmic
derivatives of \(\mathcal P\) at its two relevant arguments are
\[
 \begin{split}
 P_0:=\mathcal P(s)
     &=-\frac{A}{Y}\frac{s^2(1-Y)^2}{(1-s)^2},\\
 P_1:=\mathcal P(sY)
     &=\frac{CQX^2(1-Y)^2}{Y(1-X)^2},\\
 \frac{\mathcal P'(s)}{P_0}
     &=\frac2{s(1-Y)}+\frac2{1-s},\\
 \frac{\mathcal P'(sY)}{P_1}
     &=-\frac2{s(1-Y)}+\frac2{QY(1-X)}.
 \end{split}                                                   \tag{24}
\]
They follow by substituting (18); equalities with a vanishing
denominator mean their cleared versions. In particular
\[
 \frac{P_1}{P_0}=-\frac{(1-X)(1+s)}{(1+X)(1-s)}.
 \tag{25}
\]
Equations (24) match both principal parts at \(z=s\) and
\(z=XY\) in (23). The possible simple pole at zero cancels:
if the \(z^{-1}\) coefficient of \(\mathcal P\) is \(p_{-1}\),
both terms have coefficient \(p_{-1}/(Q^2X^2z)\).
At infinity the linear terms cancel as well. The difference of
the two sides is therefore constant.

For completeness, the constant term of (23) is
\[
 p_0(Q^{-1}-1)+2p_1\{Y(X-1)-(s-1)\},
 \qquad \mathcal P(z)=p_1z+p_0+p_{-1}/z.
 \tag{26}
\]
Substituting (18) into (26) gives
\[
 (C+q)Y+(A+q^{-1})Y^{-1}
                    -\frac{8qX}{(1+X)(1+QX)}.
 \tag{27}
\]
Directly from (16),
\[
 \begin{split}
 A&=-q^{-1}\frac{(1-QX)^4}{(1-QX^2)(1-Q^2X^2)},\\
 C&=-q\frac{(1-X)^4}{(1-X^2)(1-QX^2)},\\
 A+C+c_0&=\frac{8qX}{(1+X)(1+QX)}.
 \end{split}                                                   \tag{28}
\]
Since \(c(\beta)=qY+q^{-1}Y^{-1}\), (27) is precisely the
constant term required by (21). This proves the single-summand
identity. Summing it telescopes, and \(\mathcal H_0=0\) by
the factor \((1-Q^0)^2\), initially at regular parameters.
Meromorphic continuation proves (20). \(\square\)

At a regular physical degree \(\alpha=j\), if \(M\ge j+1\)
and \(\Re(\alpha+\beta)>M\) in the local neighborhood, the
boundary in (20) is holomorphic and
\[
                         \mathcal H_{M+1}=O((\alpha-j)^2).
 \tag{29}
\]
Indeed \(1/G(\alpha-M-1)^2\) has that double zero, the numerator
in (9) is regular, and \(Q^{M+1}-Q^{j+1}\ne0\) for the stated
finite range. In contrast, at \(M=j\) the denominator in (19)
can cancel that zero. That boundary cannot be discarded.
The recurrence use below is for \(N\ge3\), with all flux indices
strictly below \(N\); the \(N=2\) source is handled directly.

## 4. The actual independent normal

Define the short degree derivative
\[
       H_j(\beta)=
       \left.\partial_\alpha\sum_{k=0}^jT_k(\alpha,\beta)
                                                     \right|_{\alpha=j}.
 \tag{30}
\]
This is not the derivative of a terminating sum whose upper limit
has been differentiated. It is the derivative of the displayed
fixed finite formula.

Let \(\widetilde Q_N\), \(R_j\), and \(\widehat G_j\) have
exactly the normalization in the pinned physical residue source:
\[
 \widehat G_j(w)=
  \frac{c'(0)F_j(w)\widetilde Q_N(w)+R_j(w)}{c'(j)},
 \qquad c'(j)=-4\theta\sin((2j+1)\theta).
 \tag{31}
\]
Here \(R_j\) is the common-shift Jacobi determinant derivative,
with \(c_0\) fixed, and
\[
 c'(0)\widetilde Q_N(c(\beta))
                       =2[g_N'(\beta)-g_N'(0)].             \tag{32}
\]

**Theorem 2.** For every double physical degree \(0\le j\le J_d\),
as an identity on the original \(\beta\)-strip,
\[
 \boxed{\quad H_j(\beta)
     =c'(0)F_j(c(\beta))\widetilde Q_N(c(\beta))
                          +R_j(c(\beta))
     =c'(j)\widehat G_j(c(\beta)).\quad}                    \tag{33}
\]
In particular this retains the actual normal anchor, rather than
only a formally differentiated homogeneous row equation.

*Proof.* At \(j=0\), (9) gives
\[
 T_0(\alpha,\beta)=\frac{G(\alpha+\beta)^2}{G(\alpha)^2G(\beta)^2},
 \qquad H_0(\beta)=2[g_N'(\beta)-g_N'(0)],
 \tag{34}
\]
which is exactly (32).

For a recurrence step at \(\alpha=j\), first choose \(M=j+1\)
and an open \(\beta\)-domain sufficiently far to the right of
this finite cutoff, avoiding every displayed divisor. The finite
shift identity (20) and (29) hold there with zero value and zero
first \(\alpha\)-derivative of the boundary. At each of the
integer rows \(j-1,j,j+1\), the terms beyond that row have a
double degree zero. Thus differentiating (20) gives
\[
 \begin{split}
 A(j)H_{j+1}+C(j)H_{j-1}
  -[A(j)+C(j)+c_0-c(\beta)]H_j
  ={}&-A'(j)[F_{j+1}-F_j]\\
     &-C'(j)[F_{j-1}-F_j],
 \end{split}                                                   \tag{35}
\]
where all rows on the right are evaluated at \(c(\beta)\).
The step at zero uses \(C(\alpha)=O(\alpha^3)\), so its
backward contribution and its first derivative vanish. This is
also obtained directly on the same regular initial domain; at
\(j=0\) the backward terms in (35) are omitted, without assigning
an additional \(F_{-1}\) or \(H_{-1}\) datum.

The common-shift determinant \(F_j^{(\varepsilon)}\) obeys the
same three-term recurrence with \(A(j+\varepsilon)\),
\(C(j+\varepsilon)\), and fixed \(c_0\). Its derivative
\(R_j\) satisfies (35), with initial value zero. The physical
row \(F_j\) solves the homogeneous equation. Therefore the
right side of (33) satisfies (35) with the initial datum (34).
Forward uniqueness proves (33). Only regular steps below the
last needed row are used; no recurrence is imposed through the
fold. For \(N=2\) the sole required row is the already proved
initial identity.

Finally (30) is holomorphic for \(-1<\Re\beta<N\).
For \(k\le j\), its numerator argument at \(\alpha=j\) is
\(\beta+j-k\), which has no factorial pole in this region.
Possible zeros beyond the original factorial strip cause no
pole in the numerator or its derivative. Each reciprocal
\(G(\beta-k)^{-2}\) is holomorphic there; its possible negative
integer factors are zeros, and its argument never reaches the
positive zero divisor of \(G\). The other denominator is a
nonzero physical factorial. This proves the claimed holomorphy,
also after the single \(\alpha\)-derivative.
The right side of (33) is holomorphic on the same original
angular window by its pinned source formula. Analytic continuation
from the initial open domain proves the identity throughout that
window. No joint continuation of an excessive cutoff through its
diagonal pole is used. \(\square\)

## 5. Exact local full jets and cutoff transitions

Fix a physical pair \((j,l)\) and a cutoff satisfying (15).
In its joint holomorphic neighborhood,
\[
 S_M(j,\beta)=F_j(c(\beta)),\qquad
 S_M(\alpha,l)=F_l(c(\alpha)).                              \tag{36}
\]
For a double first row, every excess term \(k>j\) has a
double \(\alpha-j\) zero with holomorphic coefficient. Hence
\[
 \partial_\alpha S_M(j,\beta)
                  =c'(j)\widehat G_j(c(\beta)).              \tag{37}
\]
The same assertion holds with the endpoints interchanged.
The pinned representative preserves the value and required first
normal at every physical second endpoint. Thus, when both rows
are double,
\[
 \begin{split}
 S_M(j,l)&=K_N(c_j,c_l),\\
 \partial_\alpha S_M(j,l)&=c'(j)K_z(c_j,c_l),\\
 \partial_\beta S_M(j,l)&=c'(l)K_w(c_j,c_l),\\
 \partial_\alpha\partial_\beta S_M(j,l)
                  &=c'(j)c'(l)K_{zw}(c_j,c_l).
 \end{split}                                                   \tag{38}
\]
No terminating-value differentiation has replaced the independent
high Newton normal in this formula; it entered through (32)--(35).

At \(N=2\), the only physical pair is \((0,0)\), and (15)
requires \(M=0\). The original kernel is
\(K_2(z,w)=1+zw/16\). The factorial formula gives
\(\partial_\alpha\partial_\beta S_0(0,0)=2g_2''(0)\).
The finite logarithmic-derivative formula yields
\(g_2''(0)=\pi^2/8\), while \(c'(0)=-2\pi\); hence
\(2g_2''(0)/c'(0)^2=1/16\), as required. No isolated
\(T_N\) or singular flux factor is evaluated in this check.

If an endpoint is the odd simple node, only its value and the
other endpoint's required normal are prescribed. There is no
division by its vanishing \(c'(J)\). To obtain a local spectral
germ there, average the local angular germ under
\(\alpha\mapsto D-\alpha\), or under the corresponding
\(\beta\) reflection. Use both averages if both endpoints
are simple. This preserves every prescribed datum and gives
holomorphic descent through the spectral fold. The same operation
does not assert global evenness of an unsymmetrized fixed cutoff.

If two cutoffs both satisfy (15) at the same physical pair,
their difference is a sum of terms with \(k>\max(j,l)\).
Each is a holomorphic unit times a factor divisible by
\((\alpha-j)^2(\beta-l)^2\), or has still higher vanishing.
All four prescribed jets therefore agree on overlaps where
the respective local cutoff conditions hold. The same holds
after the odd-fold symmetrization. Products at a shared color
retain these exact full jets by the ordinary product rule.
They may be consumed by subsequent original traces, with their
original crossings and spectators retained.

These transitions are local full-Hermite-null source changes.
They do not establish an untraced free-polynomial identity, one
global holomorphic kernel, a bounded relative primitive, or a
small norm for the transition away from the physical grid.
In particular the finite boundary (20) and the diagonal divisor
(13) remain relevant to every attempted moving-wire contour.

## Direct sources and proof scope

The complete direct texts and the used implications were read at
these versions:

* [Finite balanced Sears proof](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/finite_balanced_sears_operator_proof.md),
  SHA256 4b32a5c71f5cc4484f773007e34d980266e0ba9688b0237d30f108e8a8e4ab8d:
  the terminating rational transformation with its complete prefactor.
* [Canonical factorial](research_exact_cyclotomic_factorial.md),
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b:
  the specified factorial, exact shift, finite logarithmic derivative,
  and normalization used to prove (4) and the local divisors.
* [Original physical residue packets](research_compact_positive_contour_residue_control.md),
  SHA256 cac1016d5f515510b95071a25c8d97345b334043492a6b430c4e924f87d82bb0:
  the Newton source, common-shift Jacobi determinant, actual normal
  anchor and representative, full mixed jets and the odd simple node.

The explicit finite flux and its source normalization are proved above.
Only written mathematics, source-text reads, and hashes were used.
No mathematical program, numerical experiment, test or compilation was
run. Adopted notes and public manuscripts are unchanged.
