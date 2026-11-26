# The original quantum source for positive internal pairs

Research proof, updated 4 November 2026. Frozen manuscripts are unchanged.

For an internal pair with powers \(n,p\ge3\), the complete outside
kernels now have an independently normalized complex phase. This
allows one to retain those kernels as whole factors. The exact
remaining contour has three variables: the shared Newton index and
the two trace angles. No separate asymptotic for either one-vertex
Fourier source is required.

Sections 1–5 give a contour reduction for every pair of powers at
least three. Sections 6–7 complete the estimate when both powers
are at least seven. In that range the original two-boundary source
has a nonzero geometric leading coefficient at every sufficiently
large level, with a uniform expansion near the complete boundary
colors. The proof retains the original first-normal traces and
their endpoint terms.

This is a theorem for a specified partially filled three-edge
circle-tree exterior. It does not establish stability under every
short partial filling, arbitrary tangle composition, or finitely
many exceptional assignments per template.

## 1. The original source and the complete-end normalization

Let \(\phi_N,R_N,e_j\) be the original trace, crossing and Newton
polynomials, including the first normal at each double physical
root. Put
\[
 \begin{split}
 L&=\lfloor(N-1)/2\rfloor,\qquad \eta=(-1)^{N-1},\\
 K_N(t,r)&=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos r),\\
 \mathcal L_N(t)&=\sum_{j=0}^L e_j(-2\cos t)e_j(-2),\\
 \mathcal P_{n,p,N}
 &=\phi_N^{(t)}\phi_N^{(r)}
   [R_N(t)^nR_N(r)^pK_N(t,0)K_N(t,r)K_N(r,0)] .
 \end{split}
 \tag{1}
\]
The outside colors in this note are exactly complete. Denote the
original geometric rate by \(M_{n,p}\). The
[complete-pair energy theorem](research_radical_path_sector_gap.md#6-a-uniform-estimate-for-every-positive-pair-of-powers-at-least-three)
gives
\[
 M_{n,p}>2M_\infty+\frac1{100},\qquad M_\infty=\frac{4G}{\pi}.
 \tag{2}
\]

For complex \(t\) in any compact subset of
\[
                  \Re(-2\cos t)<2,
 \tag{3}
\]
the [last-row normalization](research_last_physical_row_riccati.md)
and the [even low-kernel comparison](research_even_complete_low_kernel.md)
give, through both level parities,
\[
 \mathcal L_N(t)=
       \exp\{N\Psi(t)+O(\log N)\},\qquad \Psi(t)=\psi(t,0).
 \tag{4}
\]
Here the error is a holomorphic logarithm with all fixed derivatives
bounded by \(O(\log N)\) on smaller compact sets. The branch is
fixed by the original first physical row. Equivalently, with
\(w=-2\cos t\),
\[
 \Psi(t)=\frac2\pi\int_0^{\pi/2}
       \operatorname{arsinh}
       \left(\frac{\sqrt{2-w}}2\cot y\right)\,dy .
 \tag{5}
\]
The square root and inverse hyperbolic sine are their branches in
the right half-plane. Formula (5) fixes \(\Psi(0)=M_\infty\)
and is holomorphic on (3). This input is stronger than a formal
stationary phase identity: it estimates the actual finite
low-index polynomial on the contours used below.

## 2. Uniform removal of the original real tails

Use the continuous real Newton entropy
\[
 V_t(x)=L_{\cos}(x+t/(2\pi))+L_{\cos}(x-t/(2\pi))-2J(x),
 \quad
 L_{\cos}(s)=\int_0^s\log|2\cos\pi y|\,dy ,
 \tag{6}
\]
for real \(0\le t\le\pi\) and \(0\le x\le1/2\). Write
\(m(t)=\max_x V_t(x)\). The
[real Newton theorem](research_three_crossing_real_period_newton_bound.md)
proves
\[
 \begin{gathered}
 |e_j(-2\cos t)|\le C N^A e^{NV_t(j/N)},\\
 0\le V_t(x)\le V_0(x),\quad
 V_0(0)=V_0(1/2)=0,\quad
 m(0)=M_\infty/2,\quad m(t)\longrightarrow0\quad(t\to\pi).
 \end{gathered}
 \tag{7}
\]
All constants may be enlarged to cover the finitely many small
levels. Let \(\mathcal P^{\rm all\,low}_{n,p,N}\) be (1) with
all three edges restricted to their literal indices \(0,\ldots,L\).

**Proposition 1.** For every fixed \(n,p\ge3\),
\[
 |\mathcal P_{n,p,N}-\mathcal P^{\rm all\,low}_{n,p,N}|
                       \le C N^A e^{2NM_\infty}.
 \tag{8}
\]
One may choose fixed cuts \(0<\alpha<\beta<1/2\) and \(0<T<\pi\)
such that retaining only
\[
 \alpha\le j/N\le\beta,\qquad |t_a|<T_N,\qquad |r_b|<T_N,
 \quad T_N=T+O(N^{-1})
 \tag{9}
\]
in the shared index and the two original physical traces changes
the source by at most
\[
 C N^A e^{N(2M_\infty+1/200)}
                 <C N^A e^{N(M_{n,p}-1/200)}.
 \tag{10}
\]
The physical cut can be chosen as \(T_N=\pi-2\pi m_N/N\),
so \(e^{iNT_N}=-\eta\); it lies strictly between grid angles.
The shared-index contour boundaries obey
\(N\alpha_N,N\beta_N\in\mathbb Z+1/2\).
Thus no pole lies on a cut and no half-residue is introduced.
The odd simple node at angle zero is retained with its original
value contribution. Every first normal remains on the side of the cut to which
its original physical root belongs.

*Proof.* Each radical edge has polynomial norm on the real color
square, with polynomial bounds for its fixed ordinary normals,
by the [radical Fourier theorem](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials).
Every full or low edge has real-square norm at most
\(C N^A e^{NM_\infty}\), by (7). Expand the difference of the
products of three edges. Each term has at least one radical
and at most two exponentially sized factors. Applying the
original two Hermite traces and fixed powers of the crossing
costs only powers of \(N\). This proves (8).

For a fixed low shared index \(j\), the complete two-trace
integrand before applying the crossings is
\[
 e_j(-2\cos t)e_j(-2\cos r)\mathcal L_N(t)\mathcal L_N(r).
 \tag{11}
\]
Its norm on the real color square is at most a polynomial
times \(e^{N(2V_0(j/N)+2M_\infty)}\). Hence the omitted shared
indices have rate at most
\(2M_\infty+2\sup_{x\notin[\alpha,\beta]}V_0(x)\).

If instead \(|t|\ge T\), then uniformly over all low \(j\)
and all real \(r\),
\[
 \begin{split}
 |e_j(-2\cos t)|&\le C N^A e^{Nm(T)},\\
 |\mathcal L_N(t)|&\le C N^A e^{N(m(T)+m(0))},\\
 |e_j(-2\cos r)|&\le C N^A e^{Nm(0)},\\
 |\mathcal L_N(r)|&\le C N^A e^{2Nm(0)} .
 \end{split}
 \tag{12}
\]
Their product has rate \(2m(T)+2M_\infty\). The same estimate
holds with \(t,r\) exchanged.

These are bounds on entire real color rectangles for the
polynomial (11). Apply Markov's inequality in each variable
on those rectangles before restricting to physical nodes.
Every required first or mixed first normal has the same
exponential bound and only a polynomial additional factor.
The crossing and trace have polynomial physical Hermite norm
for each fixed power. Thus the bounds also apply to the
original sums of values and normals; no assertion about a
derivative is inferred from sampled values alone.

Choose the cuts so that
\[
 2\sup_{[0,\alpha]\cup[\beta,1/2]}V_0<1/200,\qquad
                         2m(T)<1/200 .
 \tag{13}
\]
Their existence follows from (7). Integer rounding and the
midpoint angular cuts preserve the strict inequalities for
all sufficiently large \(N\). There are only polynomially
many original terms. Equations (8), (12), and (13) prove
(10). The cuts may be enlarged to include the selected
geometric point; this only decreases the removed tails.
\(\square\)

## 3. A compact contour with the original trace kernels

Write the geometric point as
\[
 z_*=(x_*,t_*,r_*),\qquad
 Y=\Im x_*>0,\quad H_t=-\Im t_*>0,\quad H_r=-\Im r_*>0 .
 \tag{14}
\]
It has \(0<\Re x_*<1/4\) and \(0<\Re t_*,\Re r_*<\pi/2\).
Increase \(T\), if needed, so \(T>\pi/2\).

Choose even positive smooth functions \(h_t,h_r\) on \([-T,T]\).
They equal \(H_t,H_r\) respectively near the corresponding
positive critical angle, and their graphs
\[
 \Gamma_t:\ t=\tau-ih_t(\tau),\qquad
 \Gamma_r:\ r=\sigma-ih_r(\sigma)
 \tag{15}
\]
lie in (3). Such paths always exist: for \(|\tau|\le\pi/2\)
there is no height restriction from (3), while for
\(\pi/2<|\tau|<\pi\) it suffices to take
\[
              h_t(\tau)<\operatorname{arcosh}(-1/\cos\tau).
 \tag{16}
\]
Their endpoint heights may be made arbitrarily small and
positive. Choose them so the folded vertical segments
\[
 V_t:\ t=T+i\eta,\quad |\eta|\le h_t(T),\qquad
 V_r:\ r=T+i\eta,\quad |\eta|\le h_r(T)
 \tag{17}
\]
also lie in (3). Use the \(O(N^{-1})\)-adjusted paths at \(T_N\).
All these paths and their enclosed deformations lie in a
fixed compact set satisfying (3).

For the shared index use the rectangle with horizontal sides
\[
 X_+=[\alpha,\beta]+iY,\qquad
 X_-=[\alpha,\beta]-iY
 \tag{18}
\]
and two vertical sides \(X_\alpha,X_\beta\), with their endpoints
adjusted to the exact half-index grid boundaries. The factorial
representative is
\[
 B_N(x,t)=
 \frac{N}{
 G_N(N(1/2-x+t/(2\pi))-1/2)
 G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{19}
\]
At \(x=j/N\) it equals the original polynomial
\(e_j(-2\cos t)\) as an entire identity in \(t\).
Throughout the retained product contours, \(0<\Re x<1/2\)
and the two shifted real parts belong to a fixed compact
subinterval of \((-1,1)\). Thus (19) is holomorphic there.
A negative shifted factorial argument introduces reciprocal
factorial zeros; it does not justify deleting a term or
introduce an unaccounted pole in this domain.

Apply the [folded exact trace identity](research_exact_complete_trace_contour.md),
equation (12), separately to \(t\) and \(r\), deforming its
lower segments to (15). Apply the
[one-cell wire identity](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_three_crossing_retained_polytope_contour.md#2-the-one-cell-identity-with-its-orientations)
to the retained integer indices. The result has exactly the
sixteen choices
\[
 X_\nu\times T_\epsilon\times R_\delta,\qquad
 \nu\in\{+,-,\alpha,\beta\},\quad
 T_\epsilon\in\{\Gamma_t,V_t\},\quad
 R_\delta\in\{\Gamma_r,V_r\}.
 \tag{20}
\]
All integrations and interpolations are performed on the whole
product (11). In particular the below-triangle first normals
have not been separated into a new sum.

The signs and scalar factors are the literal ones of those
three identities. On the principal piece
\(X_+\times\Gamma_t\times\Gamma_r\), the leading scalar is
\[
                    -C_{N,n}C_{N,p}N^5/\pi^2 ,
 \tag{21}
\]
with the orientations and \(C_{N,k}\) of the
[local packet](research_internal_pair_local_gaussian.md).
The exact lower trace factors are
\(e^{-iNt}/(1-\eta e^{-iNt})^2\) and the corresponding function
of \(r\); their higher charges have not been truncated.
The vertical trace weights are \(1/(4\cosh^2(N\eta/2))\).
The wire factor is \(1/(1-e^{2\pi iNx})\), with the exact
orientations on all four sides.

## 4. One explicit function bounds all sixteen pieces

Let \(\mathfrak b(x,t)\) denote the continuous upper exponent
of the [uniform reciprocal-factorial theorem](research_uniform_factorial_and_boundary_decay.md),
equation (5), with the side of each negative argument retained.
It equals \(\Re b(x,t)\) on the original regular chart. Define
\[
 \begin{split}
 \mathcal E_{n,p}(x,t,r)={}&
       \mathfrak b(x,t)+\mathfrak b(x,r)+\Re\Psi(t)+\Re\Psi(r)\\
 &-\frac{n\Re t\,\Im t+p\Re r\,\Im r}{2\pi}
       -|\Im t|-|\Im r|-2\pi(-\Im x)_+ .
 \end{split}
 \tag{22}
\]

**Theorem 2.** The absolute value of each exact current in (20)
is bounded by
\[
                  C N^A \exp\{N\sup_{\mathcal C}\mathcal E_{n,p}\},
 \tag{23}
\]
where \(\mathcal C\) is its limiting compact contour. More
precisely one may use its \(O(N^{-1})\)-adjusted finite-level
contour in the supremum. A strict bound on the limiting
compact contour persists with an arbitrarily smaller gap
for all sufficiently large levels.

*Proof.* Each factorial factor is bounded by
\(CN^{-1}e^{N\mathfrak b}\), including its reciprocal zeros.
Equation (4) bounds the two whole outside factors. The
modulus of the crossing exponential is
\(e^{-Nn\Re t\,\Im t/(2\pi)}\). On a lower trace graph, its
rational weight is at most a fixed multiple of
\(e^{-N|\Im t|}\); on its folded vertical segment the same
upper bound follows from the displayed hyperbolic cosine.
The shared wire weight is bounded on both half-grid vertical
sides by \(e^{-2\pi N(-\Im x)_+}\). On its upper horizontal
side it is bounded, and on the lower side it supplies
\(e^{-2\pi NY}\). These are exactly the three last penalties
in (22). All scalar factors, contour lengths and bounded
Jacobians cost a polynomial in \(N\). This proves (23).
Uniform continuity of the upper exponents, including their
integrable-factorial-zero limits, proves the final statement.
\(\square\)

This is a finite analytic comparison in explicit functions \(J\)
and \(\Psi\). The same shared \(x\) occurs in the two terms of
(22). Replacing its maximum by the sum of two separately
maximized one-vertex rates would give a weaker problem and
is not needed by this reduction.

## 5. A sufficient inequality for the full source

Let \(U\) be a sufficiently small fixed real neighborhood of
\(z_*\) in the principal piece; choose both lower graphs to be
horizontal there. On \(U\), the phase in (22) is the real part
of the original holomorphic phase, and the
[explicit local theorem](research_internal_pair_local_gaussian.md#7-the-explicit-local-packet-with-two-free-outside-colors)
already gives its nonzero coefficient and all original normals.

Consequently it suffices to exhibit the cuts and paths above
and a number \(\delta>0\) for which
\[
 \max\left\{
  \sup_{(X_+\times\Gamma_t\times\Gamma_r)\setminus U}\mathcal E_{n,p},
  \ \max_{\mathcal C\ne X_+\times\Gamma_t\times\Gamma_r}
                                      \sup_{\mathcal C}\mathcal E_{n,p}
 \right\}<M_{n,p}-\delta .
 \tag{24}
\]
If (24) holds, the exact contour identities, (10), (23), and
the local theorem give the complete-boundary asymptotic
\[
 \mathcal P_{n,p,N}
 =C_{N,n}C_{N,p}N^{-3/2}\mathcal A(0,0)
        e^{N\mathcal S(0,0)}(1+O(N^{-1})),
 \qquad \mathcal A(0,0)\ne0 .
 \tag{25}
\]
The coefficient of the localized principal piece in this
finite contour decomposition is one. Equation (24) is what
would prevent its cancellation by the rest of that decomposition.

Mixed concavity alone controls only the part of the principal
horizontal piece in its positive factorial chamber. It does
not prove (24) on the whole product contour. The later
construction uses coupled two-dimensional trace surfaces,
together with exact grouping of the angular endpoints.
Section 7 verifies the needed complement bounds for
\(n,p\ge7\). For smaller powers the reduction here does not
by itself supply them.

There is a second scope distinction. The packet in the small
outside-color bidisk is already proved locally. In (4) the
global compact-contour bound is presently used at complete
outside colors. A complete-boundary proof of (24) alone
would not justify continuing an exponentially small error
to a fixed outside bidisk. Such an extension must retain
uniform original-source estimates on the whole contour,
as the separate free-boundary edge theorem does on its own
domain. Section 7 supplies those bounds from the physical-row
interpolation and the uniform free-boundary defect theorem;
it does not deduce them from (25) at a single boundary point.


## 6. A coupled left angular contour for powers at least seven

This section controls the entire angular surface on the left wire
interval, including a transition to small trace heights at the left
wire cut. The two heights move together. In particular, it does not
replace a coupled deformation by a rectangle of independently
chosen heights.

Fix integers \(n,p\ge7\), with the outside colors exactly complete,
and put \(H_1=H_t\), \(H_2=H_r\). The
[proved geometry and action bounds](research_real_pair_geometry_and_tail_gap.md#7-a-global-comparison-for-real-trace-angles)
give
\[
 H_i<3/10,\qquad L:=2\pi Y<2/15,\qquad
 1/5<\xi_*<1/4,\qquad M_{n,p}>163/50.
 \tag{26}
\]
Also \(\alpha(Y)<1/25\) and
\(\alpha(H_i/(2\pi))<1/20\), with \(\alpha\) as in the
mixed concavity theorem. We use the fixed central angular square
\(|\tau|,|\rho|\le\pi/2\). This choice keeps both the negative-angle
comparison and the lower-wire alias within their proved regular
chambers on \(3/50\le\xi\le1/4\).

### 6.1. A uniform bound outside the central square

**Lemma 3.** For real trace angles, \(0<\xi<1/2\), and
\(|y|\le Y\), if at least one of \(|\tau|,|\rho|\) is at
least \(\pi/2\), then
\[
 \mathcal E_{n,p}(\xi+iy,\tau,\rho)
 <\frac{865637}{266400}
 =\frac{163}{50}-\frac{2827}{266400}
 <M_{n,p}-\frac1{100}.
 \tag{27}
\]
This is an upper-phase statement at real angles. On any fixed
compact wire interval and angular cut \(T<\pi\), sufficiently
small positive trace heights turn it into an upper bound for the
actual original density, with any smaller fixed gap.

*Proof.* The real Newton maximum \(m(\tau)\) decreases with
\(|\tau|\). Its maximizing wire at \(\tau=\pi/2\) is \(1/6\),
so duplication and reflection of \(J\) give
\[
 \begin{split}
 m(\pi/2)
 &=-J(7/12)-J(1/12)-2J(1/6)\\
 &=-\frac52J(1/6)=\frac54c,
 \qquad c=-3J(1/3)=-2J(1/6).
 \end{split}
 \tag{28}
\]
For example, the identity used in the second line is
\(J(1/12)+J(7/12)=J(1/6)/2\), obtained by differentiating
the sine duplication formula and fixing its constant.
The positive Fourier-block estimate (55)–(56) in the
[real-pair bound](research_real_pair_geometry_and_tail_gap.md#7-a-global-comparison-for-real-trace-angles)
therefore proves
\[
 c<\frac{3(26/15)}{4(333/106)}\,\frac{157}{200}
     =\frac{108173}{333000},\qquad
 m(\pi/2)<\frac{108173}{266400}.
 \tag{29}
\]
Use also \(\Psi(\pi/2)<24/25\),
\(m(0)=M_\infty/2\), and \(M_\infty<7/6\).
If \(|\tau|\ge\pi/2\), the two real vertex factors have
combined exponent at most
\[
 m(\pi/2)+\Psi(\pi/2)+m(0)+M_\infty.
\]
The same argument applies when \(\rho\) is the large angle.
Equation (48) of the real-pair bound adds at most
\(2\pi|y|\le L<2/15\) for the two Newton factors. The wire
penalty can only reduce the rate. Consequently the total is less
than \(108173/266400+24/25+7/4+2/15=865637/266400\),
which proves (27).

For the finite-density statement, choose positive heights small
enough that the compact set stays in
\(\Re(-2\cos t)<2\), and that
\(\Re\Psi(t)>|\Im t|\), and similarly for \(r\).
The actual low complete-kernel theorem and the radical Fourier
bound then give the full complete-kernel upper rate \(\Re\Psi\).
Uniform continuity of the factorial upper exponent, including
its zeros, preserves the strict gap. Trace heights remain
strictly positive, and the wire is either on a nonzero horizontal
height or on a half-grid vertical side. Thus no finite bound at a
physical trace pole has been used. \(\square\)

### 6.2. Convexity when the two heights move together

**Lemma 4.** For either \(x=\xi+iY\) or \(x=\xi-iY\), with
\(3/50\le\xi\le1/4\) and \(|\tau|,|\rho|\le\pi/2\), the
continuous upper phase
\[
 q(\lambda)=\mathcal E_{n,p}
       (x,\tau-i\lambda H_1,\rho-i\lambda H_2),
                                      \qquad 0\le\lambda\le1,
 \tag{30}
\]
is convex. On the boundary of this angular square, it has a
uniform strict gap below \(M_{n,p}\), for both wire signs.

*Proof.* For one trace, away from a factorial zero, direct
differentiation of the original primitive gives
\[
 \frac{\partial^2}{\partial h^2}
 \left\{\mathfrak b(x,\tau-ih)+\Re\Psi(\tau-ih)
                              +\frac{n\tau h}{2\pi}-h\right\}
 =\frac{\Re\tan(\pi x+t/2)+\Re\tan(\pi x-t/2)
                              +2\Re\sec(t/2)}{4\pi}.
 \tag{31}
\]
Both tangent arguments have real part in \([-\pi/4,\pi/2]\).
At most one has negative real part. Its real tangent is at
least \(-1\), since
\(\Re\tan(a+ib)=\sin(2a)/(\cos(2a)+\cosh(2b))\)
and \(-\pi/4\le a\le0\); the other real tangent is nonnegative.
For \(|\tau|\le\pi/2\) and \(0\le h\le3/10\), put
\(c_0=\cos(\tau/2)\). Then
\[
 \Re\sec(t/2)
 =\frac{c_0\cosh(h/2)}{c_0^2+\sinh^2(h/2)}
 >\frac{7/10}{21/20}=\frac23.
 \tag{32}
\]
Here \(c_0\ge1/\sqrt2>7/10\), and
\(\sinh^2(3/20)<1/20\); the latter follows, for instance,
from \(\sinh z\le z/(1-z^2/6)\) at \(z=3/20\).
Thus (31) is greater than \(1/(12\pi)\).
This argument treats both wire signs directly and does not
apply an upper-wire Hessian formula to a lower wire.

At \(\xi=1/4\), \(|\tau|=\pi/2\), a shifted factorial can
vanish at \(h=L\). Its local primitive is
\(-\Re(z\Log z)\), up to a continuously differentiable term,
with \(z=\pm i(h-L)/(2\pi)\). Its contribution
\(|h-L|/4\) gives an upward derivative jump of \(1/2\).
Convexity therefore persists through this point, for the
continuous original upper exponent. Summing the two one-trace
functions proves (30).

We justify the endpoint at \(\lambda=1\) carefully. For
\(0\le\tau,\rho\le\pi/2\), the convex hull of this central
region and the geometric point lies in the closed regular
mixed-phase domain:
\[
 \xi>\alpha(Y),\quad b_i\ge\xi,\quad
 b_i>\alpha(H_i/(2\pi)),\quad b_i\le1/2,
 \qquad b_i=1/2-\tau_i/(2\pi).
\]
The strict inequalities have fixed positive margins. The
[height-independent mixed Hessian theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_mixed_phase_height_extension_and_wire_order.md),
with the closed-wall argument in the
[right-horizontal theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_right_horizontal_bulk.md#4-the-closed-wall-and-a-fixed-reflected-width),
gives a uniformly negative real Hessian. The possibly singular
\(\Re\cot\pi(s_i-x)\) is in a nonnegative rank-one term;
the remaining positive diagonal retains a fixed lower bound.
The phase is continuous at the wall. Integration along segments
therefore proves that the positive central upper phase has its
unique maximum at the original saddle.

For negative real angles use the
[original negative-angle reflection](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_negative_angle_reflection.md),
not a new Hessian assertion on the negative-angle region. On
its regular interior each reflected negative angle loses at
least \((n_i-1)|\tau_i|H_i/\pi\). Continuity gives the
non-strict comparison on the closed boundary. The zero-angle
faces are separated from the positive saddle; all other negative
faces have the additional strictly positive reflection loss.
Thus the whole signed central upper phase has its unique maximum
at that saddle. In particular its angular-square boundary has a
uniform strict gap.

For the lower wire, the
[original alias comparison](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_internal_pair_wire_alias_reflection.md)
gives a non-strict bound by the corresponding upper phase on
the closed square. It is strictly better on a neighborhood of
the actual saddle: there \(\xi<1/4\) and both angles are
strictly below \(\pi/2\), so its original \(2\pi Y\) penalty
exceeds the two reflection excesses by a fixed amount. Off that
neighborhood the upper phase already has a strict gap. Hence
the entire lower central square has a uniform gap.

At \(\lambda=0\), one boundary angle equals \(\pi/2\) in
absolute value, so Lemma 3 gives the gap. Convexity bounds (30)
by its two endpoints. Compactness makes the resulting boundary
gap uniform in \(\xi\), both trace signs, and both wire signs.
Only the phase was evaluated at \(\lambda=0\). \(\square\)

### 6.3. An exact coupled surface and the left wire side

**Theorem 5.** Fix \(0<\alpha<3/50\), and a physical angular
cut \(\pi/2<T<\pi\). For every fixed integer pair \(n,p\ge7\)
there is a coupled lower-trace surface above each
\(x=\xi\pm iY\), \(\alpha\le\xi\le1/4\), with these
properties:

- On the upper wire it agrees with the original horizontal
  geometric trace heights in a neighborhood of the positive saddle.
  Everywhere else it has a strict exponential gap below
  \(M_{n,p}\), after removing any fixed sufficiently small
  neighborhood of that saddle.
- On the entire lower wire it has a strict exponential gap.
- Near the left cut \(\xi=\alpha\), both heights are constant
  and small. The same choice bounds the whole half-grid wire side
  \(x=\alpha_N+iy\), \(-Y\le y\le Y\).
- At the distant angular boundary the heights are constant and
  small. The horizontal two-form integral equals the original
  product horizontal integral with those boundary heights, exactly.

All statements concern the original density with its two first-normal
trace kernels and full complete-end factors. They hold at both
parities and with every fixed selected ordinary-color derivative.
They do not assert a free-outside-color extension.

*Proof.* Write \(\xi_0=3/50\). Lemma 4 bounds every common
height scale on the boundary of the central angular square.
Uniform continuity gives a fixed neighborhood of that boundary
with the same gap, uniformly over the scale interval \([0,1]\).
Choose a small \(\epsilon>0\), with
\(\pi/2+\epsilon<\min(T,2\pi/3)\), within this neighborhood.
Take a smooth even cutoff \(\chi\) equal to one on
\([-\pi/2+\epsilon,\pi/2-\epsilon]\), equal to zero outside
\((-\pi/2-\epsilon,\pi/2+\epsilon)\), and strictly between
zero and one on the transition intervals.

Lemma 3 supplies the small-height bound on the compact outside
region. At \(\xi=\xi_0\), the
[left all-angle bound](research_real_pair_geometry_and_tail_gap.md#8-two-useful-endpoint-cuts)
also controls both real trace angles, without restriction, at
all \(|y|\le Y\). Its strict margin persists in a small fixed
wire neighborhood to the right of \(\xi_0\). At the geometric
height endpoint, the central region in this neighborhood is
separated from \(\xi_*>1/5\), and so has a strict concavity
and reflection gap. Lemma 4 then bounds every intermediate
common height there, throughout the central square. Its angular
boundary neighborhood has already been treated. This provides
an overlap in which the entire central lift can turn on.

Choose a smooth function \(\zeta(\xi)\in[0,1]\) equal to zero
for \(\xi\le\xi_0\), and equal to one for
\(\xi\ge\xi_0+\epsilon_x\), with a sufficiently small fixed
\(\epsilon_x>0\) in that overlap. A single sufficiently small
\(\lambda_0>0\) works in all the compact small-height bounds.
Define
\[
 \begin{split}
 \lambda(\xi,\tau,\rho)
 &=\lambda_0+(1-\lambda_0)
                  \zeta(\xi)\chi(\tau)\chi(\rho),\\
 t&=\tau-i\lambda H_1,\qquad
 r=\rho-i\lambda H_2,
 \qquad |\tau|,|\rho|\le T_N .
 \end{split}
 \tag{33}
\]
On the central part where \(\lambda=1\), the unique upper
maximum and lower gap were proved in Lemma 4. On an angular
transition, the point belongs to the compact neighborhood of
the square boundary, where every common height has a gap.
On a wire transition, the preceding overlap argument applies.
Where an angular cutoff vanishes, at least one real angle is
larger than \(\pi/2\), and Lemma 3 controls the small heights.
Finally \(\xi\le\xi_0\) is covered by the left all-angle bound.
These alternatives cover the entire surface (33).

The central and angular-transition pieces have real angles less
than \(2\pi/3\) in absolute value and heights below \(3/10\).
The full complete-kernel rectangle proved in Lemma 12 of the
[reflected-current note](research_internal_pair_reflected_current_identity.md#10-a-connected-reflected-contour-with-the-full-outside-kernels)
therefore supplies their actual finite upper exponent. On the
outer small-height region choose \(\lambda_0\) small enough
for the full-kernel justification at the end of Lemma 3.
The uniform reciprocal-factorial bound applies on every piece,
including the small reflected neighborhoods. All trace heights
are at least the fixed positive numbers \(\lambda_0H_i\).
The exact wire and trace denominators consequently have their
prescribed exponential weights and bounded remaining factors.
The heights, lengths and parametrization derivatives are bounded.
These facts convert the phase gaps into uniform bounds
\(CN^A e^{N(M_{n,p}-\delta)}\). Fixed selected ordinary normals
cost only powers of \(N\): \(|\sin t|\ge\sinh(\lambda_0H_1)>0\),
and similarly for \(r\); use slightly smaller holomorphic
neighborhoods in the strict-gap estimates.

For completeness, the exact contour equality uses the fixed-boundary
homotopy
\[
 \lambda_s=\lambda_0+s(\lambda-\lambda_0),
                         \qquad 0\le s\le1.
 \tag{34}
\]
For fixed \(x\), the original two-form
\(\mathcal I_N(x,t,r)\,dt\wedge dr\) is holomorphic throughout
this homotopy. All trace poles remain on the real angles;
reciprocal-factorial continuation retains its zeros and introduces
no discarded wall pole. On the entire outer angular boundary,
\(\lambda=\lambda_0\), so that boundary is fixed pointwise.
Stokes' theorem gives equality of the horizontal integrals.
Equivalently, a sharp central-square lift would retain the four
simultaneous-height side surfaces, with their induced orientations;
(33) smooths those surfaces inside regions with the same gap.
No independent mixed-height corner is introduced. The exact
pullback is
\[
 \frac{dt\wedge dr}{d\tau\wedge d\rho}
       =1-i\{H_1\partial_\tau\lambda+H_2\partial_\rho\lambda\}.
 \tag{35}
\]
Its absolute value is uniformly bounded. Near the saddle
\(\lambda=1\), it is exactly one.

The construction may depend on \(\xi\). When it is combined
with the shared-wire integral, terms proportional to \(dx\)
in \(dt\) or \(dr\) vanish in \(dx\wedge dt\wedge dr\).
This is also the exact pointwise trace-deformation principle:
for every wire point, the original trace value is unchanged.
At \(\alpha_N\), keep \(\lambda=\lambda_0\) throughout
\(-Y\le y\le Y\). The all-angle left bound controls this side;
the half-grid condition keeps its wire denominator bounded at
\(y=0\). Rounding cuts by \(O(N^{-1})\) stays in the same strict
neighborhoods. This proves every assertion. \(\square\)

At \(\xi=1/4\), choose the same cutoff and the same sufficiently
small \(\lambda_0\) as in the
[coupled right angular surface](research_internal_pair_reflected_current_identity.md#13-a-coupled-angular-contour-on-the-right-wire-interval).
The two formulas agree there because its moving wall equals
\(\pi/2\). They therefore join without an extra angular boundary
current. If \(T\) is chosen near \(\pi\), shrink \(\lambda_0\)
also to meet the
[grouped angular-endpoint allowances](research_internal_pair_grouped_angular_connectors.md#4-group-with-the-whole-other-trace-before-taking-absolute-values).
The homotopy fixes the distant boundary, so the original folded
endpoint terms retain exactly their old grouping with the whole
other trace. Their intersections and first normals have not been
estimated separately or removed. This supplies the left horizontal
and left vertical portions of a global contour; a conclusion for
the complete source also requires the remaining wire side and all
previously removed source terms.

## 7. The full source for every fixed pair of powers at least seven

We now assemble the preceding estimates. The source has two free
outside colors, and it is important to keep them in the statement:
an estimate only at the complete colors would not describe the
boundary function that a subsequent gluing operation uses.

Write \(\zeta=-2\cos u\), \(\omega=-2\cos v\), and define
\[
 \mathcal P_{n,p,N}(u,v)=
 \phi_N^{(t)}\phi_N^{(r)}
 [R_N(t)^nR_N(r)^pK_N(t,u)K_N(t,r)K_N(r,v)] .
 \tag{36}
\]
This is a polynomial in each ordinary color \(\zeta,\omega\).
It uses the original trace, including every first derivative at
a double physical root and the value at the odd simple root.
Its original carriers and primitive filling curves are fixed.
Let \(\mathcal S(u,v)\) and \(\mathcal A(u,v)\) be the critical
action and explicit nonzero Gaussian coefficient in
[the local pair theorem](research_internal_pair_local_gaussian.md#7-the-explicit-local-packet-with-two-free-outside-colors),
equations (33)–(35). At the complete colors,
\(\Re\mathcal S(0,0)=M_{n,p}\).

**Theorem 6.** Fix integers \(n,p\ge7\). There is a fixed
ordinary-color bidisk about \((\zeta,\omega)=(-2,-2)\) on which
the original source satisfies
\[
 \boxed{\quad
 \mathcal P_{n,p,N}(u,v)
 =C_{N,n}C_{N,p}N^{-3/2}\mathcal A(u,v)
       e^{N\mathcal S(u,v)}(1+O(N^{-1})),\qquad
              \mathcal A(u,v)\ne0 .
 \quad}
 \tag{37}
\]
The expansion holds through all sufficiently large integer levels,
with both parities included. The normalized remainder is
holomorphic on a smaller fixed bidisk; all its fixed ordinary-color
derivatives are \(O(N^{-1})\) there. An expansion to any prescribed
finite inverse-power order follows from the local theorem.

Let \(Y_{n,p}\) be the original three-edge circle-tree exterior
with the two internal circles filled by these powers and both
outside auxiliary cusps left complete. When
\(n=\eta_1-2f_1\), \(p=\eta_2-2f_2\) are its original carrier
and integer filling data, its marked hyperbolic volume is
\[
 2\pi\Re\mathcal S(0,0)=\operatorname{Vol}Y_{n,p}.
 \quad\text{Consequently}\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
          \log|\mathcal P_{n,p,N}(0,0)|
             =\operatorname{Vol}Y_{n,p}.
 \tag{38}
\]
The statement concerns this partial-exterior source. It does not
identify an unspecified closing with the Kashaev invariant of a
knot.

### 7.1. Removing indices without changing the boundary source

At complete outside colors retain the low shared indices
\[
       \alpha_N<j/N<\beta_N,\qquad
       \alpha_N=1/50+O(N^{-1}),\quad
       \beta_N=2/5+O(N^{-1}),
 \tag{39}
\]
with both cuts on the half-index grid. They are separated from
\(\xi_*\in(1/5,1/4)\). The
[original tail estimates](research_real_pair_geometry_and_tail_gap.md#4-the-original-low-coefficients-and-the-discarded-indices)
and their improved right cut in Section 8 of that note give
a strict rate gap for the omitted low indices after the traces.
Rounding spends at most an arbitrarily small part of the gap.

These estimates may be used while retaining the full outside
kernels in (36). Here is one direct verification. For a fixed
low shared index \(j\), replacing either outside kernel by its
radical changes a product on the real selected-color square by
at most a polynomial times
\[
                   e^{N\{2V_0(j/N)+M_\infty\}}
                         \le e^{2NM_\infty}.
 \tag{40}
\]
The two Newton factors have rates at most \(V_0(j/N)\), the
other full outside kernel has rate at most \(M_\infty\), and
the radical has polynomial real norm. Ordinary Markov
inequalities retain every selected first or mixed first derivative.
There are only \(O(N)\) indices. Thus (40) applies to any chosen
index subset before taking absolute values of its traced terms.
The same real-polynomial argument bounds the entire shared
radical by \(CN^Ae^{2NM_\infty}\).
Since \(2M_\infty<7/3<M_{n,p}\), all these replacements are
strictly below the desired rate.

### 7.2. An exhaustive contour decomposition at complete colors

For the retained indices apply the exact wire rectangle with
horizontal heights \(\pm Y\) and the two half-grid vertical sides.
At every wire point keep the full half-band one-trace sources
\(W_n,W_p\), not only their physical values. The
[full interpolation theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_newton_interpolation_finite_fourier_band.md)
identifies the factorial representative with all their physical
values and first derivatives. Thus the original folded trace
identities remain valid off the real wire.

Choose a common angular cut \(T\) sufficiently close to \(\pi\).
The grouped identity
\[
 W_nW_p-H_nH_p=(V_n+O_n)W_p+H_n(V_p+O_p)
 \tag{41}
\]
is exact. The
[grouped endpoint theorem](research_internal_pair_grouped_angular_connectors.md#4-group-with-the-whole-other-trace-before-taking-absolute-values)
bounds its entire right side below \(M_{n,p}\), uniformly on
the wire rectangle. In particular every folded vertical endpoint,
omitted physical-angle term, and their intersections have been
included before taking absolute values.

It remains to integrate \(H_nH_p\). Replace its product horizontal
rectangle by the coupled trace surfaces proved above and in
Sections 13–14 of
[the reflected-contour note](research_internal_pair_reflected_current_identity.md#13-a-coupled-angular-contour-on-the-right-wire-interval).
The following list accounts for the full wire rectangle:

| Wire piece | Estimate and exact contour |
|---|---|
| Upper side, \(\alpha_N\le\Re x\le1/4\) | Theorem 5: the sole maximum is the positive geometric critical point; the complement of any fixed small neighborhood has a gap. |
| Lower side, \(\alpha_N\le\Re x\le1/4\) | Theorem 5: the entire surface has a gap, including the reflected copy of the geometric neighborhood. |
| Both horizontal sides, \(1/4\le\Re x\le\beta_N\) | Theorem 19 of the reflected-contour note: the moving-wall coupled surface has a gap. |
| Left half-grid side | Theorem 5 and (58) of the real-pair note: small positive trace heights bound the entire side, including zero wire height. |
| Right half-grid side | Theorem 21 of the reflected-contour note: joint variation of the wire and trace heights bounds the entire side. |

The surface changes are exact relative-boundary deformations
of a closed holomorphic two-form. All trace heights stay positive,
and the outer angular boundary stays fixed. No physical trace pole
is crossed. Factorial reflection zeros remain in the exact
integrand; no artificial wall residue is removed. The surfaces
can be chosen to agree at their interfaces. More generally the
pointwise trace identities allow each wire piece to use its own
representation of the same source, so no unestimated interface
current is created.

Each fixed surface has bounded parametrization derivatives.
Its trace heights have a fixed positive lower bound. The exact
wire factor is bounded on the upper side, has its retained
exponential penalty on the lower side, and is bounded on both
half-grid vertical sides, including their real points. Taking the
minimum of the finitely many proved gaps gives a number
\(\delta_{n,p}>0\) for the entire complement of the local
geometric piece.

Near that piece the coupled heights are exactly \(H_n,H_p\);
the surface Jacobian is one. Its scalar and orientation are
therefore exactly those of the local pair theorem. It occurs
once, with coefficient one, in this exact contour decomposition.
The wire factor is \(1+O(e^{-cN})\) there, since
\(\Im x=Y>0\); it does not alter the local leading amplitude.
The local theorem supplies
\(C_{N,n}C_{N,p}N^{-3/2}\mathcal A(0,0)e^{N\mathcal S(0,0)}\).
The other terms have total absolute bound
\(CN^A e^{N(M_{n,p}-\delta_{n,p})}\).
They cannot cancel this nonzero leading term. This proves
(37) at complete colors.

### 7.3. Uniformity in the two ordinary boundary colors

A value at one boundary point cannot justify this extension.
We use three estimates for the actual finite functions.

First, the
[free-outside physical-defect theorem](research_free_boundary_half_charge_observation.md#4-uniform-physical-defects-and-exterior-pair-colors)
is uniform over every physical node on a fixed ordinary color
disk. Applied to the literal trace with the full outside kernel,
it gives for every low shared index
\[
 |W_{n,j,N}(\zeta)|
 \le CN^A
       e^{N\{\Re\mathcal S_n(\zeta)+V_0(j/N)\}} .
 \tag{42}
\]
Here \(\mathcal S_n\) is the one-vertex half-charge action,
so \(\Re\mathcal S_n(-2)=\mu(n)\). It is not the pair action
\(\mathcal S\) in (37).
To see (42), use the exact normal-defect trace identity: every
double-node weight is polynomially bounded, \(e_j(c_a)=0\)
for \(a<j\), and \(0\le e_j(c_a)\le e_j(-2)\) for \(a\ge j\).
At odd levels the top low index instead uses the full-node
observation and its exact rank-one top-degree term, given by
Theorem 2 and equation (24) of that same note. It has the same
half-charge rate. No derivative is assigned to the odd simple
node. The uniform defect and observation expansions
also retain all ordinary outside derivatives.
Continuity of these proved analytic actions preserves the
removed-low-index gaps on a sufficiently small fixed bidisk.

For the shared radical, its real outside-color norm is bounded
by (40), uniformly through both real periods. The omitted sum
is a polynomial of degree at most \(N-1\) in each outside color.
The polynomial Bernstein bound therefore gives the rate
\(2M_\infty+|\Im u|+|\Im v|\) on complex angular strips.
Ordinary Markov inequalities before this extension, or Cauchy
estimates on smaller disks, retain its fixed derivatives.
Thus this error has a strict gap on a fixed small ordinary bidisk
as well.

Second, the whole-contour kernel bound in
[Lemma 3 of the free-outside connector theorem](research_internal_pair_grouped_angular_connectors.md#5-free-outside-colors-original-normals-and-coupled-trace-surfaces)
states
\[
 |K_N(t,u)|\le CN^A e^{N\{\Re\Psi(t)+|\Im u|\}}
 \tag{43}
\]
on any of the compact trace domains above, with fixed ordinary
derivatives. Its hypotheses are satisfied: the central and
transition pieces lie in the full complete-kernel rectangle,
and the outer pieces have sufficiently small heights at the
fixed cut \(T<\pi\). All mapped colors lie strictly in
\(\Re w<2\), and \(\Re\Psi(t)>|\Im t|\) with a fixed margin.
This is a physical-row interpolation estimate for the full
kernel, including its radical. It does not continue a
complete-point asymptotic without a bound.
Consequently each noncritical contour exponent increases by
at most \(|\Im u|+|\Im v|\).
Theorem 4 in that note likewise preserves the exact grouped
endpoint estimate (41) on a fixed ordinary bidisk.

Finally, near the unique critical point use the independently
proved free-edge expansions and the local pair theorem.
The critical point \(z(u,v)\) moves holomorphically. Deform
the contour only in a fixed small neighborhood to pass through
it, leaving the boundary of that neighborhood fixed. For a
small enough ordinary bidisk this deformation stays inside
the regular factorial and edge charts, and its collar retains
the strict complete-point gap. The holomorphic three-form
has no pole there. Thus the local deformation is exact, and
its coefficient remains one. On the rest of the contour
(43) and continuity of \(\Re\mathcal S(u,v)\) preserve a
fixed gap relative to that moving action.

The local expansion now proves (37) uniformly on the bidisk.
Evenness in \(u,v\) makes its action, amplitude, and remainder
holomorphic in \(\zeta,\omega\) through the complete colors.
The amplitude remains nonzero after shrinking the bidisk.
Cauchy's formula on smaller ordinary-color disks proves the
derivative assertions for the normalized remainder.

### 7.4. The original marked volume

At the critical wire, the stationary identity proved in
[the unsummed edge calculation](research_unsummed_network_phase_coercivity.md#5-what-positive-geometry-does-imply-locally)
is
\[
 b(x_*,t_*)+b(x_*,r_*)=\psi(t_*,r_*).
 \tag{44}
\]
Its logarithmic lift and absolute constant are fixed by
continuation from the complete positive edge. Hence
\[
 \mathcal S(0,0)=
 \psi(t_*,0)+\psi(t_*,r_*)+\psi(r_*,0)
       +\frac{i(nt_*^2+pr_*^2)}{4\pi}-i(t_*+r_*).
 \tag{45}
\]
The positive-pair variational theorem gives positive original
edge shapes, the full primitive filling equations, and
\(\Im t_*,\Im r_*<0\).
The
[marked completion theorem](research_positive_point_marked_completion.md#1-statement-and-conventions)
therefore identifies their face assembly with the specified
smooth partial filling, with its original carriers and primitive
curves. The
[pointwise volume identity](research_positive_edge_volume_identity.md#4-a-stationary-action-on-an-arbitrary-selected-region)
gives \(2\pi\Re\mathcal S(0,0)=\operatorname{Vol}Y_{n,p}\);
its outside correction vanishes because \(u=v=0\).
Exactly three original edges occur, so no extra complete-edge
constant is added. Since \(|C_{N,n}C_{N,p}|=1\) and
\(\mathcal A(0,0)\ne0\), taking the logarithm of (37) proves
(38).

The same source statement for the mirror pair \((-n,-p)\)
follows by conjugation at real boundary colors and holomorphic
continuation in the ordinary colors. Its absolute rate is unchanged.
This conclusion still concerns the corresponding marked block.
The next section supplies the whole-period bounds needed for
the existing finite-kernel composition theorem. It does not treat
every remaining short or mixed-sign internal pair.

## 8. Boundary decay and the hypotheses for further composition

The nonzero expansion near the complete boundary does not by
itself estimate a later boundary trace. For that purpose we
also need an upper bound over the entire real boundary period.
The already proved edge and half-charge estimates provide it
on the complete contour used in Section 7. No critical point
for a distant outside angle is needed.

**Theorem 7.** Fix integers \(n,p\ge7\). There are constants
\(c,B,h_*>0\) such that, for every pair of fixed ordinary
derivative orders \(k,\ell\), suitable \(C_{k,\ell},A_{k,\ell}\)
give
\[
 \begin{split}
 &\left|\partial_\zeta^k\partial_\omega^\ell
       \mathcal P_{n,p,N}(u+is,v+it)\right|\\
 &\quad\le C_{k,\ell}N^{A_{k,\ell}}
   \exp N\{M_{n,p}-c(1-\cos u)-c(1-\cos v)+B(s^2+t^2)\},
 \end{split}
 \tag{46}
\]
for \(-\pi\le u,v\le\pi\), \(|s|,|t|\le h_*\), at both
level parities. The derivatives act in the ordinary colors
\(\zeta=-2\cos(u+is)\), \(\omega=-2\cos(v+it)\), including
their ramified angular endpoints.

*Proof.* Keep the complete-boundary contour from Section 7
fixed as the outside angles vary. On a small fixed neighborhood
of its geometric critical point, both selected trace angles lie
in the domain of the
[whole-period free-edge bound](research_pair_free_boundary_kernel.md#7-whole-outside-period-decay-and-a-complex-strip).
That theorem bounds the two actual outside kernels, with their
ordinary derivatives, by
\[
 CN^A e^{N\{\Re\Psi(t_1)+\Re\Psi(t_2)
          -c_0(1-\cos u)-c_0(1-\cos v)+B_0(s^2+t^2)\}}.
 \tag{47}
\]
All remaining factors are unchanged. The complete real phase
on this neighborhood is at most \(M_{n,p}\), by the strict
mixed-phase maximum. Its absolute integral therefore has
the upper exponent required in (46).

For the removed low indices use
[Theorem 4 of the free-outside observation note](research_free_boundary_half_charge_observation.md#5-whole-outside-period-decay-with-a-complex-strip).
It estimates every actual physical defect row and the odd
rank-one top term over the whole outside period. The exact
trace argument proving (42) now gives
\[
 |\partial_\zeta^k W_{n,j,N}(-2\cos(u+is))|
 \le CN^A e^{N\{\mu(n)+V_0(j/N)
                          -c_n(1-\cos u)+B_ns^2\}} .
 \tag{48}
\]
The analogous bound holds for \(p\). Thus the entire removed
low-index sum retains its complete-point rate gap, together
with the two angular losses and a quadratic strip cost.
Uniformity in the row is essential here; a finite-order
approximation to its entries is not substituted into the
coherent trace.

Every other complementary contour piece has a complete-point
gap. Equation (43) bounds its full outside kernels for all real
outside angles with additional cost at most \(|s|+|t|\).
The grouped angular terms have exactly this property by
Theorem 4 of the free-outside connector note. The shared
radical has the same property by its real-square bound and
the polynomial Bernstein estimate. Let \(\delta>0\) be a
common gap for these finitely many types of errors, after
removing the fixed geometric neighborhood.

Choose
\[
 h_*\le\delta/8,\qquad
 c\le\min\{c_0,c_n,c_p,\delta/16\},\qquad
 B\ge\max\{B_0,B_n,B_p\},
 \tag{49}
\]
also respecting the strips in the cited theorems.
Then \(|s|+|t|\le\delta/4\), while
\(c\{(1-\cos u)+(1-\cos v)\}\le\delta/4\).
The fixed gap pays both costs. Every complementary contribution
therefore obeys (46), and so does the sum.
The bounds used above already include fixed ordinary derivatives,
before integration or summation; no division by an angular sine
at an endpoint is involved. This proves the theorem.
\(\square\)

For completeness, the boundary Hessian needed in the finite-kernel
composition theorem is
\[
 \mathcal S_{uu}(0,0)=-\frac{\cos(t_*/2)}{2\pi},\qquad
 \mathcal S_{vv}(0,0)=-\frac{\cos(r_*/2)}{2\pi},\qquad
 \mathcal S_{uv}(0,0)=0.
 \tag{50}
\]
Indeed the edge phase is even in each outside angle, so
\(\Phi_u(z;0,0)=\Phi_v(z;0,0)=0\) identically in the internal
variables. Implicit stationary differentiation introduces no
Schur correction to these second derivatives. The original
complete-edge derivative is
\(\psi_{uu}(t,0)=-\cos(t/2)/(2\pi)\); separate evenness gives
the mixed zero. The positive geometric angles have
\(\Re\cos(t_*/2),\Re\cos(r_*/2)>0\).
Consequently a smaller fixed bidisk has a strictly negative
real boundary Hessian. Conjugation gives the same conclusion
for the mirror block.

Equations (37), (46), and (50), together with degree at most
\(N-1\) in each ordinary color, verify the analytic hypotheses
of the finite two-boundary kernel theorem. Any prescribed
finite collection of these blocks and their mirrors has common
domains and constants, obtained by taking finite minima and
maxima. Its separator threshold may depend on that collection.
No bound uniform over the entire infinite collection of pairs
has been proved by this finite-family argument. Arbitrary
adjacent short words, unrestricted tangle assembly, and the
cofinite-assignment theorem remain separate obligations.

The finite computations used in this argument are limited to the
rigorous \((7,7)\) action enclosure and exact rational comparisons.
The [action certificate](../experiments/certify_pair_seven_action.py)
proves the original logarithmic root and its positive edge domain;
the [scalar checker](../experiments/check_real_pair_geometry_and_tail_gap.py)
reproduces the comparison constants in Sections 6–8.
Their saved records are
[the interval certificate](../repro/results/research-pair-seven-action.json)
and [the rational comparisons](../repro/results/research-real-pair-geometry-and-tail-gap.json).
The contour identities, inequalities on whole regions, source
decomposition, and volume identification are the written proofs;
they are not conclusions drawn from numerical samples.
