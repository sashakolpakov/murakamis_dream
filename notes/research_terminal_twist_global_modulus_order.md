# Strict global modulus ordering of the terminal shift roots

Private written proof, 16 November 2026.

For every fixed integer turn with absolute value at least two,
one selected physical shift root has strictly largest modulus
throughout the physical interior. In fact all the growing
moduli have a strict global order. The argument uses the exact
terminal polynomial and monotonicity on confocal ellipses.
The double multiplicity of each shift root is retained.
This result permits a maximum-root upper-bound integral to use
one fixed branch; it does not prove a nonzero coefficient of that
branch, a lower source bound, or identification with a filled action.

## 1. Original shift convention and conjugate pairs

Retain the operators \(C,J,D_n\), principal cubic, and signed
terminal parametrization of the pinned characteristic source.
Let \(n\ne0\), put \(m=|n|\), and write
\[
 x=2\cos\nu,\quad 0<\nu<\pi,\qquad
 h=\sin(\nu/2)\in(0,1),\qquad
 a=\tan^2(\nu/2)=\frac{h^2}{1-h^2}.
 \tag{1}
\]
The formal forward physical shift \(\tau\) means
\(F_{j+1}=\tau F_j\) in a frozen row. Thus \(|\tau|>1\)
is growth under increasing physical row \(j\), or increasing
\(t=j/N\). In this leading chart \(\nu=2\pi t\),
\(0<t<1/2\), and \(x\) decreases as \(t\) increases.
The exact finite-row angle is \((2j+1)\pi/N\), as retained
in the original operator formula.

For \(y,z\), the symbols of \(J,D_1\), respectively, one has
\[
 y=2+2a-a(\tau+\tau^{-1}),\qquad
 z=2+2a+a(e^{-i\nu}\tau+e^{i\nu}\tau^{-1}).
 \tag{2}
\]
The terminal characteristic \(D_n=2\) selects
\[
 x=f_m(y),\qquad
 z=
 \begin{cases}
 f_{m-1}(y),& n>0,\\
 f_{m+1}(y),& n<0,
 \end{cases}
 \tag{3}
\]
where
\[
 f_0=2,\quad f_1=4-y,\quad
 f_{r+1}=8-yf_r-f_{r-1}.
 \tag{4}
\]
The source proves that these are \(m\) distinct selected
shift roots, each of algebraic multiplicity two. The \(y\)
roots are simple for \(x<2\). For even \(m\) all \(y\)
roots are nonreal; for odd \(m\) exactly one is real,
and it is in \((2,2+4a)\).

The following reciprocal relation concerns the selected
points, including the signed choice in (3).
Put \(Y=y-(2+2a)\), \(Z=z-(2+2a)\). The conic inverse is
\[
 \tau=-\frac{Z+e^{i\nu}Y}{2ia\sin\nu},\qquad
 \tau^{-1}=\frac{Z+e^{-i\nu}Y}{2ia\sin\nu}.
 \tag{5}
\]
All the polynomials in (3) have real coefficients.
Taking conjugates in (5) therefore gives exactly
\[
                    \tau(\bar y)=\frac1{\overline{\tau(y)}}.
 \tag{6}
\]
For a nonreal \(y\), a unit-circle shift is impossible by
the first equation in (2). Consequently each conjugate \(y\)
pair gives one selected growing root and one selected
decaying root, with reciprocal moduli. The unique real
branch for odd \(m\) gives a single selected unit-circle root.
In particular there are
\[
                         q_m=\lfloor m/2\rfloor
 \tag{7}
\]
distinct growing roots, with double multiplicities still understood.

## 2. A symmetric real-rooted polynomial on an ellipse

Let \(U_r\) be the ordinary Chebyshev polynomial of the
second kind, and define
\[
                         p_m(\zeta)=\zeta U_{m-1}(\zeta).
 \tag{8}
\]
The exact terminal formula gives the unified identity
\[
             f_m(2-4\zeta^2)-2=4p_m(\zeta)^2.
 \tag{9}
\]
For example substitute \(y=2-4\zeta^2\) in
\[
 f_m(y)-2=\frac{2(y-2)}{y+2}
                         [T_m(-y/2)-1]
\]
and use
\(T_m(2\zeta^2-1)=T_{2m}(\zeta)\) and
\(1-T_{2m}(\zeta)=2(1-\zeta^2)U_{m-1}(\zeta)^2\).
These are polynomial identities, including their removable
values at \(\zeta=\pm1\).

Take the member \(y\) of a nonreal conjugate pair in the
lower half-plane, and choose the square root
\[
                 y=2-4\zeta^2,\qquad
                 \operatorname{Re}\zeta>0,\quad
                 \operatorname{Im}\zeta>0.
 \tag{10}
\]
It is unique. Equations (1), (3), and (9) give
\[
                         p_m(\zeta)=\pm ih,
                 \qquad |p_m(\zeta)|=h.
 \tag{11}
\]
The larger modulus of the two roots of the \(J\)-quadratic
in (2), hence the growing selected modulus of this pair
by (6), is
\[
               \rho(\zeta)=
               \exp\!\left(2\operatorname{Re}
                           \operatorname{asinh}(\zeta/\sqrt a)\right).
 \tag{12}
\]
Here the inverse hyperbolic sine takes the first quadrant
to \(\{R+i\theta:R>0,\ 0<\theta<\pi/2\}\).
One can check this branch without using a logarithmic convention:
there is a unique \(R>0\) solving
\[
 \frac{(\operatorname{Re}\zeta)^2}{a\sinh^2R}
  +\frac{(\operatorname{Im}\zeta)^2}{a\cosh^2R}=1.
 \tag{13}
\]
The left side decreases strictly from infinity to zero.
Then the positive cosine and sine defined by its two terms
give a unique \(\theta\in(0,\pi/2)\) and
\(\zeta=\sqrt a\,\sinh(R+i\theta)\).
The two \(J\)-quadratic roots are \(e^{\pm2(R+i\theta)}\),
which proves (12).
The selected growing root may belong to the other member
of the conjugate \(y\) pair; only its modulus is used here.

**Lemma 1.** Fix \(a>0\), \(R>0\), and \(m\ge1\).
The function
\[
       \theta\longmapsto
       |p_m(\sqrt a\,\sinh(R+i\theta))|,
               \qquad 0<\theta<\pi/2,
 \tag{14}
\]
is strictly increasing.

*Proof.* All roots of \(p_m\) are real and symmetric.
More explicitly, with \(r_k=\cos(k\pi/m)>0\),
\[
 p_m(\zeta)=
 \begin{cases}
 2^{m-1}\zeta
       \displaystyle\prod_{k=1}^{(m-1)/2}(\zeta^2-r_k^2),
                         &m\ \text{odd},\\[2mm]
 2^{m-1}\zeta^2
       \displaystyle\prod_{k=1}^{m/2-1}(\zeta^2-r_k^2),
                         &m\ \text{even}.
 \end{cases}
 \tag{15}
\]
Empty products are allowed. This is the usual root
factorization of \(U_{m-1}\), with its zero at the origin
included in the even case.

Put \(A=a\sinh^2R>0\), \(u=\sin^2\theta\), and
\(\zeta=\sqrt a\,\sinh(R+i\theta)\). Then
\[
 |\zeta|^2=A+au,\qquad
 |\zeta^2-r^2|^2
  =(A-r^2)^2+
       [\,2a(A+r^2)+4Ar^2\,]u+a^2u^2
 \tag{16}
\]
for every real \(r\).
Both expressions increase strictly for \(0<u<1\);
the second is positive there.
Every factor in the modulus of (15) is therefore
positive and strictly increasing. This proves (14).
\(\square\)

## 3. Strict ordering and identification of the maximal branch

**Theorem 2.** Fix \(n\ne0\). The growing selected shift
moduli have a strict order on the whole physical interval:
\[
                 \rho_1(x)>\rho_2(x)>\cdots>
                 \rho_{q_m}(x)>1,\qquad -2<x<2.
 \tag{17}
\]
The branches in (17) can be labeled once and for all;
they never exchange this order. For \(m\ge2\) there is
exactly one selected root of largest modulus. For \(m=1\)
the only selected root has modulus one.
The complete modulus ordering consists of (17), the one
unit modulus when \(m\) is odd, and the reciprocals in
reverse order. Every distinct root retains multiplicity two.

For \(m\ge3\), the maximal branch is the growing selected
member of the \(y\) pair tending, as \(x\uparrow2\), to
\[
                         -2\cos(2\pi/m).
 \tag{18}
\]
For \(m=2\), the sole conjugate pair tends to \(y=2\)
and supplies the maximal root.

*Proof.* Suppose two different conjugate pairs had the same
growing modulus. Their representatives \(\zeta_1,\zeta_2\)
from (10) would have the same value \(R>0\) in (12).
Both obey \(|p_m(\zeta_i)|=h\). Lemma 1 forces the same
\(\theta\), hence the same \(\zeta\), contradicting that
the pairs differ. Thus all growing moduli are distinct
at every point of the physical interval.

The simple \(y\) roots admit continuous, indeed analytic,
labels on \(x<2\), by the characteristic source. Their
nonreal pairs cannot cross the real line: such a crossing
would merge a pair, contrary to simplicity.
Equation (6) and the exclusion of unit moduli on these
pairs give continuous growing-root labels. Distinct
continuous moduli cannot exchange order on an interval.

It remains to identify the order near \(x=2\), or \(h=0\).
Each positive simple root
\[
                    r_k=\cos(k\pi/m),\qquad 1\le k<m/2,
 \tag{19}
\]
of \(p_m\) gives exactly one first-quadrant solution of
\(p_m(\zeta)=ih\) or \(p_m(\zeta)=-ih\) near \(r_k\).
This follows from the implicit function theorem and the
nonzero real derivative \(p_m'(r_k)\).
It satisfies \(\zeta=r_k+O(h)\).
Since \(a\sim h^2\), (12) gives
\[
                       \rho_k\sim\frac{4r_k^2}{h^2}.
 \tag{20}
\]
For example this follows directly from
\(\operatorname{asinh} w=\log(2w)+O(w^{-2})\)
in a neighborhood of the positive real direction.
The numbers \(r_k\) decrease strictly with \(k\), so these
branches are ordered as in (19).

When \(m\) is even, there is one additional first-quadrant
solution at the double origin of \(p_m\). Since
\[
 p_m(\zeta)=(-1)^{m/2-1}m\zeta^2+O(\zeta^4),
\]
it has
\[
 \zeta=e^{i\pi/4}\sqrt{h/m}\,(1+O(h)),\qquad
                         \rho_{\mathrm{last}}\sim\frac4{mh}.
 \tag{21}
\]
The same inverse-hyperbolic-sine expansion applies here in a
neighborhood of argument \(\pi/4\).
This branch is smaller than all branches in (20) for
small \(h\), and remains last everywhere.
When \(m\) is odd, the remaining root is the already
identified real \(y>2\) branch of unit modulus.
The counts in (7) show that no growing branch is missing.
Finally \(2-4r_1^2=-2\cos(2\pi/m)\), proving (18).
\(\square\)

The order is the same for both signs of \(n\), and the
selected roots themselves are conjugated. To see this
with the physical shift fixed, the backwards initial
symbol is
\[
 x_{-1}=8-yx-z
       =2+2a+a(e^{i\nu}\tau+e^{-i\nu}\tau^{-1}).
 \tag{22}
\]
This is coefficient conjugation of \(x_1=z\).
Both forward and backward sequences obey
\(x_{r+2}=8-yx_{r+1}-x_r\), with real coefficients
in \(x,y\). Induction therefore proves
\[
            x_{-m}(\tau)=\overline{x_m(\bar\tau)}.
 \tag{23}
\]
Thus the negative-turn root is the conjugate of the
corresponding positive-turn root, with its modulus unchanged.

## 4. Consequence for a spectral-radius upper bound

For fixed \(m\ge2\), let \(\tau_{\max,n}(t)\) denote the
unique selected growing root identified above, with
\(x=2\cos(2\pi t)\). It is an analytic branch locally in
the physical interior, with a globally consistent label.
Then exactly
\[
 \max_{\tau:\,x_n(\tau)=2}\log|\tau|
           =\log|\tau_{\max,n}(t)|=\log\rho_1(t).
 \tag{24}
\]
The same maximum for the inverse shifts is \(\log\rho_1\),
by (6). On a compact interior interval the differences
between successive logarithmic moduli are bounded below
by positive constants. This is stronger than separation
of the roots alone, while leaving their double multiplicity intact.

For clarity the classical integral also has finite endpoint
limits as an improper integral. At \(t\downarrow0\),
\(h=\sin(\pi t)\), and (20)--(21) give at most a logarithmic
singularity of \(\log\rho_k\).
At \(t\uparrow1/2\), the simple roots of \(f_m(y)=-2\)
have finite limits. Their first-quadrant representatives
have limits \(\zeta_k^*\), with positive real part.
Equation (12) gives
\[
 \log\rho_k
     =2\operatorname{Re}\zeta_k^*\sqrt{1-h^2}
                          +O((1-h^2)^{3/2}).
 \tag{25}
\]
Indeed these representatives vary analytically near \(h=1\)
and \(a^{-1/2}=\sqrt{1-h^2}/h\).
Consequently \(\int_0^{1/2}\log\rho_1(t)\,dt\) is finite.
This endpoint statement concerns the characteristic only;
it supplies no uniform finite-level transfer estimate there.

If an actual transfer theorem has already bounded an
original source by the integral of the largest characteristic
modulus, (24) identifies that integrand with one globally
selected branch. No further branch maximization or branch
switching is required. The present theorem does not prove
that upper bound, a surviving coefficient of this branch,
or a comparison of its integral with the original filled action.
It also does not replace the mixed branching forcing or
the original Jordan companion by a scalar equation.

## 5. Direct-source readback

The sole direct proof source is
[the all-power terminal characteristic theorem](research_terminal_twist_characteristic_geometry.md),
SHA256
3606f43995336bc0481acf9e04a96da5efd65f67706bef42cc9b1b1011694d1b.
Its entire final text was read at that unchanged pin,
and the used signed parametrizations, physical conic
inverse, simple \(y\) roots, and double shift multiplicities
were checked again.

The new ellipse inequality, order comparison, and endpoint
labels are proved above. Only written mathematics, source-text
reads and hashes were used. No mathematical program, numerical
experiment, test, or build was run. Frozen notes and public
manuscripts are unchanged.
