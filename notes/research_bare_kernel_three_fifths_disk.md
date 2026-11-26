# The full original edge kernel on a three-fifths angular disk

Private written proof, 16 November 2026.

The full same-index kernel has its original nonzero geometric
expansion on the complex disk of radius \(3/5\) in each angle. This
extends the available height range near completeness. The proof uses
the existing split-cotangent contour mechanism, with new disk-specific
phase, omitted-index and lattice-mode estimates. No numerical
certificate is used. This is an edge-source theorem; an angular
complement estimate for a subsequent network contraction is separate.

## 1. Statement and the original interpolation

Put \(D=N-1\), \(N\ge2\), and
\[
 S_j=\prod_{a=1}^j2\sin(\pi a/N),\qquad
 e_j(z)=S_j^{-2}\prod_{a<j}
       \{2\cos((2a+1)\pi/N)-z\},
\]
\[
 K_N(t,u)=\sum_{j=0}^{D}e_j(-2\cos t)e_j(-2\cos u),
 \qquad r=3/5.
 \tag{1}
\]
An index is low when \(2j<N\), and high otherwise. Keep the
canonical sine primitive and the complete edge branch
\[
 J'(z)=\Log(2\sin\pi z),\quad J(0)=0,
\]
\[
 \begin{aligned}
 b(x,t)&=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),\\
 A(x,t,u)&=b(x,t)+b(x,u),\\
 C(t,u)&=\frac{1-\cos t\cos u}{2+\cos t+\cos u},\qquad
 x_* =\frac{\arccos C}{2\pi},\\
 \psi(t,u)&=A(x_*,t,u),\qquad
 \psi(0,0)=M_\infty=4G/\pi.
 \end{aligned}
 \tag{2}
\]
All branches continue from \(t=u=0,x_*=1/4\).

**Theorem.** Uniformly on a neighborhood of
\(\{|t|\le3/5,\ |u|\le3/5\}\), the full original sum satisfies
\[
 K_N(t,u)=N^{-3/2}a(t,u)e^{N\psi(t,u)}
                 (1+O_{\rm hol}(N^{-1})),
 \qquad
 a(t,u)=\frac{\sqrt{2\pi}}
 {4\sin^2(\pi x_*)\sqrt{-A_{xx}(x_*,t,u)}}\ne0.
 \tag{3}
\]
The square root is positive at completeness, where \(a=1/4\).
Every fixed further expansion order and every fixed ordinary
boundary-color derivative is retained, at both level parities.
This includes the ramification of \(-2\cos t\) at \(t=0\).

The exact interpolation used in the pinned original-kernel proof is
\[
 B_N(x,t)=\frac{N}
 {G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{4}
\]
It equals \(e_j(-2\cos t)\) at \(x=j/N\), as an ordinary
polynomial identity in the color. On every compact strict factorial
strip it has the original all-fixed-order expansion
\[
 B_N(x,t)B_N(x,u)=
 \frac{e^{NA(x,t,u)}}{4N^2\sin^2(\pi x)}
                     (1+O_{\rm hol}(N^{-1})).
 \tag{5}
\]
We use (4)--(5), including the actual offsets \(-1/2\), from the
original kernel source; we do not replace its interpolation.

## 2. The disk phase and the entire high half

For \(|t|,|u|\le r\), define the removable function
\[
 f(t,u)=\frac{2\operatorname{asinh}(\tan(t/2)\cos(u/2))}{t}-1.
\]
The following elementary estimates hold on this disk:
\[
 \begin{aligned}
 |\tan(t/2)|&\le13|t|/25,&
 |\tan(t/2)-t/2|&\le |t|^3/20,\\
 |\cos(u/2)|&<21/20,&
 |\cos(u/2)-1|&\le21|u|^2/160,\\
 |\operatorname{asinh}z-z|&\le |z|^3/5
                         &&(|z|\le1/3).
 \end{aligned}
 \tag{6}
\]
The Taylor coefficients of \(\tan z\) are nonnegative, as follows
recursively from \((\tan z)'=1+\tan^2z\). Thus
\(|\tan z|\le\tan|z|\), and \(\tan a/a\) is increasing for
\(0<a\le3/10\). The alternating sine and cosine estimates give
\[
 \tan(3/10)\le
 \frac{3/10-(3/10)^3/6+(3/10)^5/120}{1-(3/10)^2/2}
 <\frac{39}{125}=\frac{26}{25}\frac3{10}.
\]
Therefore \(|\tan z|\le(26/25)|z|\) on that disk.
Integrating \(\tan^2z\) along the radial segment gives
\(|\tan(t/2)-t/2|\le(26/25)^2|t|^3/24<|t|^3/20\).
The positive cosh series proves the cosine estimates; the
binomial derivative bound proves the asinh estimate by integration.
The asinh argument has modulus at most \(819/2500<1/3\).
Consequently
\[
 |f(t,u)|\le
 \left\{\frac{21}{200}+\frac25(273/500)^3\right\}|t|^2
       +\frac{21}{160}|u|^2
 <\frac13\max(|t|,|u|)^2.
 \tag{7}
\]
The calibrated derivative is
\(\psi_t=-t(1+f(t,u))/(2\pi)\), and similarly in \(u\).
Radial integration therefore gives
\[
 \psi(t,u)=M_\infty-\frac{t^2+u^2}{4\pi}+E(t,u),
 \qquad
 |E(t,u)|\le\frac{r^2(|t|^2+|u|^2)}{24\pi}.
 \tag{8}
\]
Write \(H=|\Im t|, L=|\Im u|\). Since
\((\Re t)^2\le r^2-H^2\), and similarly for \(u\),
\[
 \begin{aligned}
 \Re\psi-H-L
 &\ge M_\infty-\frac{r^2}{2\pi}-\frac{r^4}{12\pi}
       +\frac{H^2+L^2}{2\pi}-H-L\\
 &\ge M_\infty-2r+\frac{r^2}{2\pi}-\frac{r^4}{12\pi}
 >\frac{94}{6875}>\frac1{100}.
 \end{aligned}
 \tag{9}
\]
The second line minimizes the two decreasing quadratics on
\([0,r]\). For the last inequality use \(3<\pi<22/7\) and
\(M_\infty>29/25\). A rational proof of the latter is
\(G>8/9+24/1225+40/9801>8207/9000>319/350\), from the
first six alternating Catalan terms.

The pinned full-radical Fourier estimate, which retains every
double-root normal and the odd simple root, gives
\[
 \left|\sum_{2j\ge N}e_j(-2\cos t)e_j(-2\cos u)\right|
       \le C N^a e^{N(H+L)}.
 \tag{10}
\]
Thus the entire high half has the strict gap (9). This is an
estimate on the actual high polynomials, not their distinct-node
values.

## 3. Uniform low-index tails

For imaginary arguments put
\[
 A_{H,L}(x)=
 \int_0^x\log\{2\cos(2\pi v)+2\cosh H\}\,dv
 +\int_0^x\log\{2\cos(2\pi v)+2\cosh L\}\,dv-4J(x).
 \tag{11}
\]
The exact positive Laurent coefficients of every low polynomial give
\[
 |e_j(-2\cos t)e_j(-2\cos u)|
       \le e_j(-2\cosh H)e_j(-2\cosh L).
 \tag{12}
\]
Uniform midpoint comparison of the numerator products and the sine
factorials gives the upper estimate
\[
 e_j(-2\cosh H)e_j(-2\cosh L)
       \le C N^a e^{NA_{H,L}(j/N)},
       \quad 2j<N,\quad 0\le H,L\le r.
 \tag{13}
\]
This includes \(H=0\) or \(L=0\). One can see the uniformity
directly: the numerator logarithm is monotone on \([0,1/2]\);
every included last midpoint and terminal integration endpoint is
at distance at least a constant times \(N^{-1}\) from its possible
zero at \(1/2\). The endpoint logarithmic errors are consequently
\(O(\log N)\), uniformly in the nonnegative height. The usual
two endpoint logarithms for the sine factorial give the same error.
These are the same comparisons as in the pinned Fourier source.

The unique maximum of (11) has
\[
 q_*:=\cos(2\pi x_*)=
 \frac{1-\cosh H\cosh L}{2+\cosh H+\cosh L},
 \qquad -1/10<q_*\le0,\quad 1/4\le x_*<4/15.
 \tag{14}
\]
Here \(\cosh r<6/5\); monotonicity in the two coshes proves
the \(q_*\) bound. The final bound follows from
\(\sin(\pi/30)>1/10\). The derivative of (11) changes sign
only at (14): after exponentiating it, the difference between
numerator and denominator is linear in \(q=\cos(2\pi x)\).

On \(1/10\le x\le2/5\), its curvature satisfies
\[
                         -A_{H,L}''(x)\ge4\pi\sqrt3.
 \tag{15}
\]
Indeed, with \(q=\cos\theta,\theta=2\pi x,C=6/5\),
\[
 -A_{H,L}''\ge
 4\pi\frac{(1+C)\cot(\theta/2)}{q+C}.
\]
For \(q\ge0\), the last factor is at least \(11/6>\sqrt3\),
using \(\sqrt{(1+q)/(1-q)}\ge1+q\). For \(q=-v\le0\),
one has \(0\le v<5/6\). Its square exceeds three because
\[
 13-49v+105v^2-75v^3>0:
 \quad p'(v)=-(15v-7)^2,\qquad p(5/6)=121/72.
\]
Outside that interval the monotonicity around (14) suffices.
It follows that every \(x\notin(3/20,7/20)\) loses at least
\[
 \frac{\pi\sqrt3}{72}>\frac{17}{240}
 \tag{16}
\]
relative to \(\psi(-iH,-iL)=\max A_{H,L}\).
On the other hand (8) gives
\[
 \psi(-iH,-iL)-\Re\psi(t,u)
 \le D_r:=\frac{r^2}{2\pi}+\frac{r^4}{6\pi}
             <\frac{42}{625}.
 \tag{17}
\]
Thus every omitted low index has a gap greater than
\(17/240-42/625=109/30000>3/1000\) below \(\Re\psi\).
The same comparison gives, on the retained real wire interval,
\[
                  \Re A(x,t,u)\le\Re\psi(t,u)+D_r.
 \tag{18}
\]
For (18), the continuum modulus inequality follows from (12),
(5) at real wire points, and dense sequences \(j/N\to x\).
All factorial arguments here are in strict strips.

## 4. The exact lattice modes and the nonzero coefficient

Use the fixed wire rectangle
\[
 \mathcal R=[3/20,7/20]+i[-1/25,1/25].
 \tag{19}
\]
Every \(x\) and \(1/2-x\pm t/(2\pi)\), and the corresponding
arguments for \(u\), has real part strictly between zero and
\(1/2\), uniformly on (19) and the parameter disks. Thus (5)
holds throughout. In particular
\[
                         \Re A_{xx}<0
 \tag{20}
\]
uniformly: \( -A_{xx}/\pi\) is the sum of the four cotangents
at those factorial arguments and \(4\cot(\pi x)\), all with
strictly positive real part.

The saddle is strictly inside (19). In fact
\(|\cos t-1|<1/5\) implies \(|C|<11/90\), and
\[
 |x_*-1/4|\le
 \frac{|C|}{2\pi\sqrt{1-|C|^2}}<\frac{11}{534}<\frac1{25}.
 \tag{21}
\]
The logarithmic critical equation is exactly \(A_x(x_*)=0\):
its exponential is one algebraically, and connected continuation
from completeness in these strict strips fixes the integer branch.
This also calibrates (2) and the derivative used in (8).

There is a uniform bound on the imaginary derivative:
\[
                         |\Im A_x|<23\pi/20.
 \tag{22}
\]
To prove it put \(q=\cos(2\pi x)\), \(c=\cos t\). On (19),
\[
 |\Re q|<78/125,\quad |\Im q|<13/50,\quad
 \Re c\ge41/50,\quad |\Im c|<24/125.
\]
Here \(\cos(3\pi/10)<3/5\),
\(\cosh(2\pi/25)<26/25\), \(\sinh(2\pi/25)<13/50\),
\(\sinh(3/5)<16/25\), and
\(|\Re t\Im t|\le9/50\) suffice. Hence
\[
 \frac{|\Im(q+c)|}{\Re(q+c)}<\frac{113}{49}<1+\sqrt2,
 \qquad
 \frac{|\Im(1-q)|}{\Re(1-q)}<\frac{65}{94}
                                  <\tan(\pi/5).
\]
The first argument has magnitude below \(3\pi/8\), and the
second below \(\pi/5\). Apply the exact continued identity
\[
 A_x=\Log(q+\cos t)+\Log(q+\cos u)-2\Log(1-q)
\]
to obtain (22). All three quantities remain in the right
half-plane; no branch is reset in this calculation.

Choose vertical sides \(a_N,b_N\) on half-grid lines tending to
\(3/20,7/20\), and let \(f_N=B_N(x,t)B_N(x,u)\). The exact
residue identity is
\[
 \sum_{a_N<j/N<b_N}f_N(j/N)
       =\frac N{2i}\oint f_N(x)\cot(\pi Nx)\,dx.
 \tag{23}
\]
Split the cotangent into \(-i\operatorname{sgn}\Im x\) and
its remainder, including on the vertical sides. As in the pinned
original proof, the constant pieces give exactly
\(N\int_{a_N}^{b_N}f_N(x)\,dx\). The vertical remainder has
modulus at most \(2e^{-2\pi N|\Im x|}\); (22) therefore
preserves the real endpoint gap (16)--(17). On the horizontal
sides its rate relative to \(\Re\psi\) is at most
\[
 D_r-(2\pi-23\pi/20)/25
 <42/625-51/500<-3/100.
 \tag{24}
\]
All these gaps survive the half-grid rounding.

Translate the constant real integral to the horizontal through
\(x_*\). By (20) this line has its unique strict real maximum
at \(x_*\); its endpoints have a uniform gap. The real endpoints
have (16)--(17). Along each connecting vertical segment, the
real phase is convex because its second vertical derivative is
\(-\Re A_{xx}>0\). The larger of its two endpoint values
therefore bounds the entire connector strictly below the saddle.
This controls the actual constant-piece connectors, not just the
lattice-mode remainder.

Ordinary holomorphic Laplace expansion of this translated integral,
with (5), proves (3). Its exact coefficient is \(+N\); the powers
are \(N\cdot N^{-2}\cdot N^{-1/2}=N^{-3/2}\). Sections 2--3
restore every omitted original index with a strict exponential gap.

All inequalities have strict reserves on compact sets, so the proof
works on a slightly enlarged parameter neighborhood. Cauchy estimates
retain every fixed angular derivative. Separate evenness of the
actual sum and of the uniquely continued phase and amplitude gives
holomorphic descent to the ordinary colors near the ramified complete
angles; away from ramification it is immediate. Ordinary-color
Cauchy estimates give all fixed spectral derivatives. No artificial
odd-level normal is introduced. This completes the theorem.

## 5. Scope and pinned direct sources

The existing rectangular kernel theorem, its exact interpolation,
normalization and split-cotangent mechanism are prior coverage.
The contribution here is the larger angular disk, with fully written
uniform estimates for its high half, low tails and lattice modes.
The disk contains the small positive saddles relevant to a possible
degree-twelve network extension, but the theorem does not bound the
whole angular complement or prove that network extension.

Direct source versions:

- `research_bare_kernel_thin_rectangle.md`,
  SHA-256 `04797c52fca87548857482461a470c46f70d3cb476b5f18249920527b733d847`:
  exact factorial interpolation, original phase/amplitude calibration,
  all-fixed-order strict-strip expansion and split-cotangent identity.
- `research_high_newton_radical_contraction.md`,
  SHA-256 `1faa5d2e02edf0a1462cc43b243e0ab4403bf56e9f1af0befb6b492441d9dd03`:
  complete high-index Fourier bound, including both parities and normals.
- `research_zero_power_subtree_fourier_bound.md`,
  SHA-256 `9c7e71319ba9f416f5ea510dee472e481894396d0c8a3cebf6ff9cce05816c58`:
  exact positive low Laurent coefficients and uniform elementary
  factorial/product comparison; the height-zero uniformity used here
  is explicitly checked after (13).
