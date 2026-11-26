# Global logarithmic phases on the proper-return domains

Private written proof, 15 November 2026.

The proper-return strip of the original positive primitive equations
supports a single global Newton label and value phase. The domain for
two disjoint proper subproducts is contractible, and all seven
multiplication factorial arguments have fixed global logarithms and
primitives calibrated from the original strict real gate. The same
statement holds for both signed crossing gates, with their existing
integer Fourier characters retained.

These functions pull back to an arbitrary-degree vertex and any
binary resolution with allocated integer crossing powers. The
resulting phases telescope to the original angular action,
independently of the resolution. This is a global statement about
logarithmic marks and actions. It does not determine a Fourier
coefficient of the complete lattice kernel or an intersection
coefficient of the original finite cycle.

**Theorem.** The domains \(\mathcal E,\mathcal D\) and
\(\mathcal V_{d,n}\) defined below are contractible.
The globally normalized phases satisfy the multiplication,
crossing and complementary identities (23), (32) and (38).
Every allocated proper-subproduct resolution on
\(\mathcal V_{d,n}\) therefore has the same marked action (39).
The original crossing characters and finite pairing are retained.

## 1. The universal proper-return domain

Put
\[
 \mathcal T=\{t\in\mathbb C:|\Re t|<\pi,\ \Im t<0\},
 \qquad H=-\Im t,\qquad a=\tan(t/2),
\]
\[
 \mathcal S_t=\{R\in\mathbb C:
                  0<\Re(R\overline t)<\pi H\},\qquad
 \mathcal E=\{(t,R):t\in\mathcal T,\ R\in\mathcal S_t\}.
 \tag{1}
\]
This is an open domain in \(\mathbb C^2\). It is contractible.
Indeed every return has unique real coordinates
\[
                    R=-\pi i u+i t v,\qquad
                         0<u<1,\quad v\in\mathbb R,
 \tag{2}
\]
because \(\Re(R\overline t)=\pi Hu\) and \(H>0\).
Thus (2) is a homeomorphism
\(\mathcal E\simeq\mathcal T\times(0,1)\times\mathbb R\).
It is used for topology, not as a holomorphic coordinate change.

Use the original prefix functions
\[
 \mathcal N_R=a\cosh R+i\sinh R,\qquad
 \mathcal D_R=a\cosh R-i\sinh R,\qquad
 Y_R=\mathcal N_R/\mathcal D_R,\qquad
 Q_R=\mathcal N_R\mathcal D_R.
 \tag{3}
\]
Here \(Q_R\) is not the root of unity. The source prefix identities
give the zeros of \(\mathcal N_R,\mathcal D_R\) respectively at
\[
                  R=it/2+\pi i k,\qquad
                  R=-it/2+\pi i k,\qquad k\in\mathbb Z.
 \tag{4}
\]
The zeros of \(\sinh R\) are \(\pi i k\).
Every value in these lists has real pairing
\(-\pi kH\), outside the strict interval in (1).
Also \(a\ne0\) and \(1+a^2\ne0\) on \(\mathcal T\).
Consequently all these factors are holomorphic units on
\(\mathcal E\).

Every holomorphic unit on a simply connected domain has a
holomorphic logarithm: integrate its closed logarithmic
derivative and fix one value. Define the global label \(X(t,R)\)
by
\[
                   e^{2\pi iX(t,R)}=Y_R,\qquad
                   X(t,-\pi i/2)=1/2.
 \tag{5}
\]
The second condition is consistent for all \(t\), because
\(Y_{-\pi i/2}=-1\) identically. It fixes the logarithm globally.
In particular \(\sin(\pi X)\ne0\).
The unit
\[
                  \chi_R=\mathcal D_R e^{\pi iX(t,R)}
 \tag{6}
\]
is a specified square root of \(Q_R\), with
\(\chi_{-\pi i/2}=-i\). Exact algebra gives
\[
             \sin(\pi X(t,R))=\frac{\sinh R}{\chi_R},
 \qquad
             X_R=\frac{a}{\pi Q_R},\qquad
             X_t=-\frac{(1+a^2)\sinh R\cosh R}{2\pi Q_R}.
 \tag{7}
\]
Thus \(X_R\) never vanishes.

The unit \(2\sin(\pi X)\) has a global logarithm
\(\mathcal K\), normalized to be real on
\(t=-iH,\ R=-i\rho,\ 0<\rho<\pi\).
There the label lies in \((0,1)\), as verified in (19).
The one-form \(\mathcal K\,dX\) is closed, so it has a
global primitive \(\mathcal J(t,R)\), normalized by
\[
 d\mathcal J=\mathcal K\,dX,\qquad
 \mathcal J(t,-\pi i/2)=J(1/2)=0.
 \tag{7a}
\]
The normalization is consistent because \(X=1/2\) on that
line. This primitive agrees with the original
\(J(x)=\int_0^x\log(2\sin\pi s)\,ds\) on the real slice.

There is a global logarithm
\(\mathcal L(t,R)=\Log[\sin(t/2)/\sinh R]\), normalized to be
real when \(t=-iH,\ R=-i\rho,\ 0<\rho<\pi\).
On that slice the ratio is
\(\sinh(H/2)/\sin\rho>0\).
The one-form
\[
             \omega=2\mathcal L(t,R)\,dX-\frac R\pi\,dt
 \tag{8}
\]
is closed. To check this directly, use
\(\mathcal L_t=1/(2a)\), \(\mathcal L_R=-\coth R\) and (7):
\[
 2\mathcal L_tX_R-2\mathcal L_RX_t+\frac1\pi
 =\frac{1-(1+a^2)\cosh^2R}{\pi Q_R}+\frac1\pi=0.
 \tag{9}
\]
Contractibility therefore gives a unique holomorphic primitive
\(\mathcal B\), normalized by
\[
             d\mathcal B=\omega,\qquad
             \mathcal B(t,-\pi i/2)=it/2.
 \tag{10}
\]
Along the indicated line \(dX=0\), so (8) gives \(i\,dt/2\);
the normalization is consistent.

This is the original value phase, globally lifted to \(\mathcal E\).
On the strict initial chart it agrees with
\[
 B(x,c)=\int_0^x\Log(2\cos(2\pi s)-c)\,ds-2J(x),
 \quad c=-2\cos t,\quad x=X(t,R).
 \tag{11}
\]
Indeed the source derivatives are \(B_t=-R/\pi\) and
\[
 B_x=\Log\frac{2\cos(2\pi x)-c}{4\sin^2\pi x}
    =2\Log\frac{\sin(t/2)}{\sinh R},
 \tag{12}
\]
with their real logarithms on the purely imaginary slice.
Its source normalization \(B(1/2,c)=it/2\) is (10).
Thus (8)--(10) continue the specified phase, without an
undetermined additive constant.

## 2. Two proper subproducts and their seven primitives

Define
\[
 \mathcal D=\{(t,\alpha,\beta):
 t\in\mathcal T,\ 
 \Re(\alpha\overline t)>0,\ 
 \Re(\beta\overline t)>0,\ 
 \Re((\alpha+\beta)\overline t)<\pi H\}.
 \tag{13}
\]
In (2), write \(\alpha=-\pi i u_1+itv_1\) and
\(\beta=-\pi i u_2+itv_2\). Then
\[
             u_1,u_2>0,\qquad u_1+u_2<1,\qquad
                         v_1,v_2\in\mathbb R.
 \tag{14}
\]
This identifies \(\mathcal D\) topologically with
\(\mathcal T\), an open triangle and \(\mathbb R^2\).
It is contractible.

Put \(\gamma=\alpha+\beta\) and
\[
                   x=X(t,\alpha),\qquad
                   y=X(t,\beta),\qquad z=X(t,\gamma).
 \tag{15}
\]
Every one of
\[
                   x,\ y,\ z,\ x+y,\ z-x,\ z-y,\ x+y-z
 \tag{16}
\]
avoids the integers throughout \(\mathcal D\).
Besides (7), the exact identities are
\[
 \begin{split}
 \sin\pi(x+y)&=\frac{a\sinh\gamma}{\chi_\alpha\chi_\beta},\\
 \sin\pi(z-x)&=\frac{a\sinh\beta}{\chi_\gamma\chi_\alpha},\\
 \sin\pi(z-y)&=\frac{a\sinh\alpha}{\chi_\gamma\chi_\beta},\\
 \sin\pi(x+y-z)&=
  \frac{(1+a^2)\sinh\alpha\,\sinh\beta\,\sinh\gamma}
       {\chi_\alpha\chi_\beta\chi_\gamma}.
 \end{split}
 \tag{17}
\]
They follow by expanding the numerators using (3) and (6).
All factors on the right are units by Section 1.

The global marks have an actual strict real calibration slice:
\[
 t=-iH,\qquad \alpha=-i\rho_1,\quad\beta=-i\rho_2,
 \qquad \rho_1,\rho_2>0,\quad\rho_1+\rho_2<\pi.
 \tag{18}
\]
To verify this, set \(A=\tanh(H/2)\in(0,1)\). On the slice
\[
 \chi_{-i\rho}=-i\sqrt{A^2\cos^2\rho+\sin^2\rho},\qquad
 \frac{d}{d\rho}X(-iH,-i\rho)
       =\frac{A}{\pi(A^2\cos^2\rho+\sin^2\rho)}>0.
 \tag{19}
\]
This label increases from zero to one and obeys
\(X(-iH,-i(\pi-\rho))=1-X(-iH,-i\rho)\).
Hence \(x+y<1\) and \(z>\max(x,y)\).
All four sines in (17) are positive on (18).
Since \(-1<x+y-z<1\), its positive sine implies \(x+y-z>0\).
Thus
\[
                     0<x,y,\qquad \max(x,y)<z<x+y<1.
 \tag{20}
\]

For each argument \(\ell\) in (16), the unit
\(2\sin(\pi\ell)\) has a global logarithm normalized to its
real logarithm on (18). The one-form
\[
                     \Log(2\sin\pi\ell)\,d\ell
 \tag{21}
\]
is closed: its exterior derivative is
\(\pi\cot(\pi\ell)\,d\ell\wedge d\ell=0\).
It therefore has a global primitive \(J_\ell\), fixed by
the original \(J(\ell)\) at any one point of (18).
These primitives agree with the source \(J\)'s on the
entire slice, and are their unique continuations on
\(\mathcal D\).

Define the globally marked multiplication action
\[
 \mathcal M=
 J_{x+y}+J_z-J_x-J_y-J_{z-x}-J_{z-y}-J_{x+y-z}.
 \tag{22}
\]
Then the exact global critical-value identity is
\[
 \boxed{\quad
 \mathcal M(t,\alpha,\beta)=
      \mathcal B(t,\alpha)+\mathcal B(t,\beta)
                               -\mathcal B(t,\alpha+\beta).
 \quad}
 \tag{23}
\]
For a direct verification of its differential, (17) gives
\[
 \frac{\sin\pi(x+y)\sin\pi(z-x)}
      {\sin\pi x\sin\pi(x+y-z)}
       =\frac{\sin^2(t/2)}{\sinh^2\alpha},
 \tag{24}
\]
the analogous identity with \(\beta\), and
\[
 \frac{\sin\pi z\sin\pi(x+y-z)}
      {\sin\pi(z-x)\sin\pi(z-y)}
       =\frac{\sinh^2\gamma}{\sin^2(t/2)}.
 \tag{25}
\]
The calibrated logarithms turn these into exact logarithmic
identities, since the possible integer discrepancies are
constant and zero on (18). Hence
\[
 d\mathcal M=
      2\mathcal L(t,\alpha)\,dx+
      2\mathcal L(t,\beta)\,dy-
      2\mathcal L(t,\gamma)\,dz.
 \tag{26}
\]
This is the differential of the right side of (23), because
the \(dt\) terms cancel by \(\gamma=\alpha+\beta\).
Its additive constant is zero by the original strict
multiplication identity, on (18).

## 3. Both signed crossings with their original Fourier marks

For \(\sigma=\pm1\), use the same contractible domain
\(\mathcal E\), and set
\[
 R_{\rm in}=R,\qquad R_{\rm out}=R-i\sigma t/2,\qquad
 y=X(t,R_{\rm in}),\quad x=X(t,R_{\rm out}).
 \tag{27}
\]
Translation by \(-i\sigma t/2\) preserves \(\mathcal S_t\).
Both individual sines are units, and
\[
 \sin\pi(x-y)=
     \frac{a\,\sinh(-i\sigma t/2)}
               {\chi_{R_{\rm out}}\chi_{R_{\rm in}}}\ne0.
 \tag{28}
\]
Thus all three crossing factorial primitives have global
marks on \(\mathcal E\).

Here is a strict real crossing point in this domain, fixing
their calibration:
\[
 H_*=\operatorname{arsinh}1,\quad
 t_*=\sigma\pi/2-iH_*,\quad a_*=(\sigma-i)/\sqrt2,
\]
\[
 R_{{\rm in},*}=\sigma H_*/2-i\pi/4,\qquad
 R_{{\rm out},*}=-i\pi/2,\qquad
                      y_*=1/4,\quad x_*=1/2.
 \tag{29}
\]
Both pairings equal \(\pi H_*/2\), and (27) holds.
The global label lift in (5) gives exactly these labels.
To see the input mark without an integer reset, use
\[
 t_s=s\sigma\pi/2-iH_*,\qquad
 R_{\rm out}=-i\pi/2,\qquad
 R_{\rm in}=R_{\rm out}+i\sigma t_s/2,\quad 0\le s\le1.
 \tag{30}
\]
Along this path \(Y_{\rm out}=-1\) and
\(Y_{\rm in}=(-\cos t_s)^{-\sigma}\).
Its continuous argument decreases from \(\pi\) to \(\pi/2\).
The input label at the endpoint is \(1/4\); the output stays
\(1/2\). The initial input is connected to \(R=-\pi i/2\)
by the horizontal segment at \(t=-iH_*\); its label has
real part \(1/2\). Along (30),
\(1/4\leq\Re y\leq1/2\), so its
individual primitive remains the original analytic \(J\)
in \(0<\Re y<1\). The same path gives the original logarithm in
(12): at its input \(\sin(t/2)/\sinh R_{\rm in}=ia\),
continued from a positive value to \((1+i\sigma)/\sqrt2\).
Thus this is the old strict crossing mark.

The additive value-phase constant also agrees with the source.
At fixed \(t=t_*\), let the real label decrease from \(1/2\)
to \(1/4\), and use
\(R=\operatorname{artanh}(a_*\tan\pi x)\), continued from
\(R=-\pi i/2\). Its elementary logarithm gives
\[
 0\leq\sigma\Re R\leq H_*/2,\qquad
             -\pi/2\leq\Im R\leq-\pi/4.
 \tag{30a}
\]
For example the real-part bound follows by maximizing
\(\frac14\log[(1+\sqrt2\lambda+\lambda^2)/
(1-\sqrt2\lambda+\lambda^2)]\) for \(\lambda\geq1\);
its maximum at \(\lambda=1\) is \(H_*/2\).
The imaginary-part bounds follow from the arguments of
\(1\pm a_*\lambda\). Therefore this whole return path lies
in \(\mathcal S_{t_*}\), since its pairing is between
\(\pi H_*/4\) and \(3\pi H_*/4\).
Starting from the common normalization at \(x=1/2\), it
continues exactly the source \(B(x,-2\cos t_*)\) to \(x=1/4\).
There is no additional additive constant at (29).

Normalize the three crossing primitives at (29), and put
\[
 \mathcal F_\sigma
     =J_x-J_y-J_{x-y}
                     +\sigma i\pi(1/2+x+xy).
 \tag{31}
\]
The individually occurring \(J_x,J_y\) are the pullbacks
of the same global individual-label primitive in Section 1;
the difference argument is calibrated at \(x-y=1/4\).
The source crossing comparison extends globally to
\[
 \boxed{\quad
 \mathcal B(t,R_{\rm in})-\mathcal B(t,R_{\rm out})
       +\sigma i\left(\frac\pi4+\frac{t^2}{4\pi}\right)
       =\mathcal F_\sigma-2\pi i\sigma x.
 \quad}
 \tag{32}
\]
Indeed the pinned crossing identity proves it on a neighborhood
of (29). Its strict gate parametrization is regular there:
the explicit relation, obtained by substituting (27) into (3),
\[
 -2\cos t=2-4\sin(\pi x)\sin(\pi y)e^{i\sigma\pi(x-y)}
 \tag{33}
\]
has nonzero \(t\)-derivative and nonzero \(x\)-derivative
there, and \(X_R\ne0\). All functions in (32), with their
just-specified marks, are holomorphic on the connected
\(\mathcal E\). The identity theorem proves (32) throughout.
Equivalently its differential and its value at (29) give
the same continuation.

The linear term \(-2\pi i\sigma x\) is retained. On the
original integer output \(I=Nx+\delta_I\), its exponential
is \(e^{-2\pi i\sigma I}=1\); its offset contribution is
also one for every actual integer \(\delta_I\).
Off the integer grid it changes the Fourier character and
cannot be deleted.

## 4. Arbitrary degree, allocated powers, and the final pairing

Fix a degree \(d\ge2\) and the actual signed integer total
power \(n\). Consider the open primitive return domain
\[
 \mathcal V_{d,n}=
 \left\{(t,r_1,\ldots,r_d):
 \begin{array}{l}
 t\in\mathcal T,\quad \Re(r_e\overline t)>0\ \text{for all }e,\\
 \sum_er_e-int/2=-\pi i
 \end{array}\right\}.
 \tag{34}
\]
It is an open domain in the complex affine constraint bundle.
Writing \(r_e=-\pi i u_e+itv_e\) identifies it topologically
with
\[
 \mathcal T\times
       \{u_e>0:\sum_eu_e=1\}\times
       \{v_e\in\mathbb R:\sum_ev_e=n/2\}.
 \tag{35}
\]
It is contractible.

For any nonempty proper subset \(A\) and any allocated
integer power \(n_A\), put
\[
                    R_A=\sum_{e\in A}r_e-i n_A t/2.
 \tag{36}
\]
The allocation term \(-i n_A t/2\) has zero real pairing
with \(t\), and
\[
          \Re(R_A\overline t)
                  =\pi H\sum_{e\in A}u_e\in(0,\pi H).
 \tag{37}
\]
Thus every allocated prefix pulls back the same global
functions of Section 1. At a multiplication gate with
disjoint nonempty \(A,B\) and proper union, allocated
powers add and \(R_{A\cup B}=R_A+R_B\); its map lands in
\(\mathcal D\). At a signed crossing on a proper prefix,
\(n_A\) increases by \(\sigma\) and (27) applies.
Hence every finite binary proper-subproduct resolution,
with any such allocated integer crossing layers, has
globally fixed factorial logs and actions on (34).
The same subset with the same allocated power always has
the same label; reassociation does not reset that label.

The final complementary pairing has its own exact lift.
For \(R\in\mathcal S_t\), also \(-\pi i-R\in\mathcal S_t\).
From (3), \(Y_{-\pi i-R}=Y_R^{-1}\), and calibration gives
\[
       X(t,-\pi i-R)=1-X(t,R),\qquad
       \mathcal B(t,-\pi i-R)=it-\mathcal B(t,R).
 \tag{38}
\]
For the second identity, \(\sinh(-\pi i-R)=\sinh R\), so
the logarithms in (8) agree by calibration; differentiating
the sum gives \(i\,dt\), with the stated constant at
\(R=-\pi i/2\).

Summing (23) and (32) over the gate tree cancels every
internal value phase. If the last factor is reserved for
the complementary pairing, (38) gives the remaining
vertex action
\[
 \boxed{\quad
    \sum_{e=1}^d\mathcal B(t,r_e)
          +\frac{int^2}{4\pi}-it+\frac{i\pi n}{4}.
 \quad}
 \tag{39}
\]
Here the left side of each crossing identity (32) is used;
in factorial coordinates this is exactly the sum of
the globally marked \(\mathcal F_\sigma\)'s minus
\(2\pi i\sum_g\sigma_gx_{{\rm out},g}\), and the multiplication
actions (22). Signed inverse layers cancel with their
literal signs; only their total \(n\) occurs in (39).
The value does not depend on the binary tree or the
distribution of its crossing powers.

Formula (39) is the original angular vertex action and
its known scalar phase. The finite source still uses
\(\phi_N(e_i e_j)=\mathbf1_{i+j=N-1}\); its reversal has
the exact offset \(-1\), not a changed finite pairing.
The finite crossing carriers and their subleading scalars
are those of the pinned spectral adapter. The global
action identity does not replace them by their limits.

The positive primitive theorem places every actual
selected vertex with positive incident edges in (34).
The functions above therefore pull back to any such
finite original network. This does not require the
network's geometric realization locus itself to be
contractible: the marked functions are already defined
on the ambient product of the domains (34).
Degree-one traces have no proper-prefix chart here.
The degree-two zero-power case retains its exact
complementary delta pairing without adding a fictitious
strict gate.

The condition in (34) is the primitive return equation,
not the whole inverse-period contour. On the latter the
return sum is generally \(\xi-\pi i\) with real
\(\xi\ne0\); the final complement is then
\(\xi-\pi i-R\), for which (38) does not apply.
Thus this theorem gives coherent phases on the primitive
locus and does not carry that existing descent contour
into Newton variables.

## 5. What global phase transport implies about coefficients

The theorem fixes logarithmic marks, additive action constants,
and the original crossing Fourier characters throughout the
proper-return domains. It removes path ambiguity in those
data. It does not place every factorial argument in its
original strip: the positive-star construction has a real
negative argument, and the exact chamber atlas retains its
level-dependent wall factors.

At a chosen point, compare these globally marked primitives
with a chamber's canonical \(J_+\) or \(J_-\). The difference
is an explicitly retained integer-affine Fourier character,
as in the atlas. Its integer coefficients are constant on
any connected chart where the corresponding branch
comparison is defined.
Contractibility does not say that this character is zero.

In particular, the support test cannot use the wall polynomial
alone. Already on the original strict signed-crossing triangle
all wall factors are one, whereas (32) has the nonzero
character \(-2\pi i\sigma x\). That character belongs to
the original lattice lift, not to a missing wall term.
A coefficient test must retain both the lattice kernel and
the wall factors with the fixed action above.

Even a nonzero coefficient of a specified local expansion
of those complete factors does not compute the original
relative-cycle intersection. The finite supported residue
cycle, its endpoint currents, and its deformed boundary
terms still require control. No full scalar noncancellation,
new knot class, or extension of the volume theorem is
asserted.

## Direct sources

* [Positive primitive prefixes](research_positive_primitive_prefix_regularity.md),
  SHA256 \(\texttt{a01b55a71d133aadff4aac0929e50de03e1059991d6874e81646c770eb5604a6}\):
  the actual proper-return strip, numerator/denominator divisors,
  all seven sine exclusions, crossing translations and original
  proper-subproduct resolution.
* [Spectral--Newton adapters](research_newton_spectral_legendre_adapters.md),
  SHA256 \(\texttt{34c0e2e1114488c6ac82a5dffbdbd8a4a8d85e7fbba252de91833dc8d697e303}\):
  original value-phase derivatives and constants, strict gate
  calibration, crossing Fourier character, exact final pairing,
  carrier and whole-source telescoping.
* [Factorial chamber atlas](research_newton_factorial_chamber_atlas.md),
  SHA256 \(\texttt{34d6e0e4e82a98bf8e6063558ecafdedb0a58d6229fbe462e7e4bfff48f4db4c}\):
  source-preserving wall factors and the distinction between their
  constant coefficient and the premarked geometric character.
* [Positive star real wall](research_positive_star_real_factorial_wall.md),
  SHA256 \(\texttt{8e58d9a8a430ed3f54277e1c960d68bf42486d6879f64c03df953936708f32af}\):
  the stated limitation on inferring an original factorial strip
  from positive primitive geometry.

Only written proofs, source-text reads and file hashes are used.
No mathematical code, numerical evaluation, tests or compilation
are used.
