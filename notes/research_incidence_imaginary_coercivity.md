# Imaginary coercivity and a finite angle program for the original incidence action

Private written deduction, 15 November 2026. No mathematical code,
numerical calculation, test, or saved numerical evidence is used.
Frozen notes and public manuscripts are unchanged.

For the original acute incidence action, imaginary minimization is
controlled by an explicit finite zonotope. Strict feasibility is
equivalent to coercivity and to existence of a finite minimizing
height. The minimizer is unique and real analytic; its reduced
action is strictly concave and is exactly a sum of positive ideal
tetrahedron volumes divided by \(2\pi\). The associated angle
constraints are affine equations from the actual source.

This does not assert feasibility or an interior maximum for every
diagram. Indeed, one terminal signed Markov stabilization, with an
arbitrary original exterior retained, prevents imaginary coercivity
on every Fourier lift. Nor are the tetrahedra below identified with
a triangulation of the knot complement, or their critical point
with a nonzero contribution of the original residue cycle.

## 1. The original action and the meaning of coercivity

Use the fixed real cut and the integral transfer/clock coordinates of
[the acute incidence theorem](research_original_incidence_acute_tube.md).
Write \(m=2c\), where \(c>0\) is the crossing count. The crossing
incidences are real affine functions
\[
 n(z)=a+Lz,\qquad
 \mathscr S(z)=-\sum_{e=1}^{4c}\mathcal J(n_e(z))
                    +i\pi\mathcal Q(z),
 \quad
 \mathcal Q(z)=\tfrac12z^{\mathsf T}\mathcal H z+b^{\mathsf T}z+b_0 .
 \tag{1}
\]
Here \(a,b,b_0\) are real, \(\mathcal H\) is real symmetric,
and \(L\) has rank \(m\). The fixed real cut is essential to these
reality statements. Every bend phase and recorded Fourier character
is included in the specified affine part of \(\mathcal Q\).
The rank assertion follows directly because the crossing incidences
recover each transfer and clock. Closing-pair entropy terms have
already canceled by their exact reflection identity.

The primitive is the marked one with
\(\mathcal J'=\Log(2\sin\pi z)\), real on \((0,1)\), and
\(\mathcal J(0)=0\). In particular \(\mathcal J(1/2)=0\).
Let
\[
 \mathcal A=\{x\in\mathbb R^m:0<n_e(x)<1/2\text{ for all }e\}.
 \tag{2}
\]
It may be empty. Fix \(x\in\mathcal A\) and an actual Fourier
lift \(k\in\mathbb Z^m\). Set
\(\mathscr S_k(z)=\mathscr S(z)-2\pi i k\cdot z\), and define
\[
 \begin{split}
 F_k(x,y)&=\Re\{\mathscr S(x+iy)-2\pi i k\cdot(x+iy)\},\\
 \alpha_e&=n_e(x),\qquad w_e=\tfrac12-\alpha_e>0,\\
 \xi_k(x)&=\mathcal Hx+b-2k,\\
 Z_x&=L^{\mathsf T}\operatorname{diag}(w_e)[-1,1]^{4c}.
 \end{split}
 \tag{3}
\]
This is a full-dimensional compact zonotope: \(L^{\mathsf T}\)
is onto and every width is positive. Its support function is
\[
                     h_{Z_x}(v)=\sum_e w_e |(Lv)_e|.
 \tag{4}
\]

Here **coercive** means \(F_k(x,y)\to+\infty\) as
\(\|y\|\to\infty\), equivalently compact sublevel sets.
It does not mean merely that the map to \(\mathbb R\) is proper.
A function tending to opposite infinities at the two ends of
a line can be a proper map without being bounded below.

## 2. Exact one-incidence asymptotics

For \(0<\alpha<1/2\), put
\[
                g_\alpha(t)=-\Re\mathcal J(\alpha+it).
 \tag{5}
\]
The principal logarithm of the sine gives, for every real \(t\),
\[
 \begin{split}
 g_\alpha'(t)
   &=\arg(2\sin\pi(\alpha+it))
     =\arctan\{\cot(\pi\alpha)\tanh(\pi t)\},\\
 g_\alpha''(t)
   &=\pi\Re\cot\pi(\alpha+it)>0.
 \end{split}
 \tag{6}
\]
The arctangent is its value in \((-\pi/2,\pi/2)\).
Thus \(g_\alpha'\) increases strictly from
\(-\pi(1/2-\alpha)\) to \(+\pi(1/2-\alpha)\).

There is an exact remainder formula, not just a recession limit:
\[
 \begin{split}
 g_\alpha(t)&=\pi(1/2-\alpha)|t|+r_\alpha(t),\\
 r_\alpha(t)&=\int_\alpha^{1/2}
       \log|1-e^{-2\pi|t|+2\pi is}|\,ds,\\
 0<r_\alpha(t)&\le r_\alpha(0)=-\mathcal J(\alpha),\qquad
 r_\alpha(t)=O(e^{-2\pi|t|})\quad(|t|\to\infty).
 \end{split}
 \tag{7}
\]
For the formula, \(\Re\mathcal J(1/2+it)=0\): its initial
value is zero, and its vertical derivative is purely imaginary.
Integrate \(\Log(2\sin\pi(s+it))\) horizontally from
\(\alpha\) to \(1/2\). For \(t\ge0\),
\[
 2\sin\pi(s+it)
      =i e^{-i\pi s+\pi t}
                          (1-e^{-2\pi t+2\pi is}).
 \tag{8}
\]
Taking real parts gives (7); conjugation gives the negative
half-line. The last integral tends to zero exponentially,
using \(|\Log(1-z)|\le |z|/(1-|z|)\) for \(|z|<1\).
By (6), \(r_\alpha'(t)<0\) for \(t>0\). Its limit zero
then proves strict positivity and the bound in (7).
These estimates are uniform when \(\alpha\) ranges over
a compact subinterval of \((0,1/2)\).

In particular the asymptotic affine term has constant zero.
The chosen primitive does not leave an unknown real constant
in the following coercivity or volume identities.

## 3. The zonotope criterion, including its boundary

The quadratic term of (1) has real part
\(-\pi(\mathcal Hx+b)\cdot y\). Equations (3) and (7)
therefore give the exact identity
\[
 \boxed{\quad
 F_k(x,y)=\pi\{h_{Z_x}(y)-\xi_k(x)\cdot y\}
                   +\sum_e r_{\alpha_e}((Ly)_e).
 \quad}
 \tag{9}
\]
Its final sum is positive and at most \(F_k(x,0)\).
Consequently, along every nonzero real direction \(v\),
\[
 \begin{split}
 F_k(x,tv)
  ={}&\pi t\{h_{Z_x}(v)-\xi_k(x)\cdot v\}\\
    &-\sum_{(Lv)_e=0}\mathcal J(\alpha_e)
                       +O(e^{-2\pi t\mu_v}),\qquad t\to+\infty,
 \end{split}
 \tag{10}
\]
where \(\mu_v=\min_{(Lv)_e\ne0}|(Lv)_e|>0\).
There is at least one such coordinate because \(L\) is injective.
Formula (10) also records the bounded contribution of incidences
which do not move along that ray.

**Theorem 1.** For fixed \(x\in\mathcal A\), the following are
equivalent:

1. \(F_k(x,\cdot)\) is coercive.
2. \(\xi_k(x)\in\operatorname{int}Z_x\).
3. \(F_k(x,\cdot)\) has a finite minimizer.

When these conditions hold, the minimizer is unique. If
\(\xi_k(x)\in\partial Z_x\), the infimum is finite but is
not attained. If \(\xi_k(x)\notin Z_x\), the infimum is
\(-\infty\).

**Proof.** An interior vector has a strictly positive support
margin
\[
 \delta_k(x)=\min_{\|v\|=1}
                   \{h_{Z_x}(v)-\xi_k(x)\cdot v\}>0 .
 \tag{11}
\]
Indeed a small Euclidean ball about that vector lies in
the zonotope. Conversely, this support margin places such
a ball inside the intersection of its supporting half-spaces.
Equation (9) gives
\[
                     F_k(x,y)\ge\pi\delta_k(x)\|y\|,
 \tag{12}
\]
so a finite minimum exists. Its Hessian in \(y\) is
\[
          \pi L^{\mathsf T}\operatorname{diag}
                  (\Re\cot\pi(\alpha_e+i(Ly)_e))L>0 ,
 \tag{13}
\]
which proves uniqueness.

For the converse, put
\(\theta_e(y)=\arg(2\sin\pi(\alpha_e+i(Ly)_e))\).
Differentiating gives
\[
               \nabla_yF_k=L^{\mathsf T}\theta-\pi\xi_k .
 \tag{14}
\]
Every \(\theta_e/\pi\) belongs strictly to \((-w_e,w_e)\)
by (6). The image of this open box under the onto map
\(L^{\mathsf T}\) is exactly \(\operatorname{int}Z_x\).
For one elementary verification, the image is open and
lies in \(Z_x\). Conversely an interior point of \(Z_x\)
can be expanded slightly radially while remaining in
\(Z_x\); scaling back a box preimage gives a strict
box preimage. Thus (14) cannot vanish unless the
force is interior.

If the force is exterior, separation from the compact
convex zonotope gives \(v\) with
\(\xi_k\cdot v>h_{Z_x}(v)\); (10) tends to \(-\infty\).
If it is on the boundary, take a nonzero supporting
direction with equality. Equation (9) bounds the
function below by zero, while (10) gives a finite
limit on that ray. No finite minimum is possible
by (14). In fact the directional derivative along
this ray is strictly negative at every finite point:
\(\theta_e/\pi\) lies strictly inside each interval,
and some \((Lv)_e\ne0\). This proves all assertions.
\(\square\)

The same proof gives a useful exact image statement:
\[
 y\longmapsto \pi^{-1}L^{\mathsf T}\theta(y)
          \quad\hbox{is a real-analytic diffeomorphism }
          \mathbb R^m\longrightarrow\operatorname{int}Z_x .
 \tag{15}
\]
Its differential is positive definite, and strict convexity
makes it injective. Coercivity for every interior target
gives surjectivity; the inverse function theorem gives the
analytic inverse. This identifies the entire image, not
only a neighborhood of a previously known critical point.

## 4. Analytic minimizing heights and the reduced Hessian

For a fixed actual Fourier lift define
\[
       \mathcal D_k=\{x\in\mathcal A:
                     \xi_k(x)\in\operatorname{int}Z_x\}.
 \tag{16}
\]
It is an open convex domain, possibly empty. More concretely,
its membership is a finite strict linear feasibility problem:
\[
      L^{\mathsf T}\zeta=\mathcal Hx+b-2k,\qquad
        -w_e(x)<\zeta_e<w_e(x),\qquad x\in\mathcal A.
 \tag{17}
\]
All these equations and inequalities are affine in
\((x,\zeta)\). Convexity follows by taking convex
combinations of strict solutions. Openness follows
by retaining their positive margins and using a fixed
linear right inverse of \(L^{\mathsf T}\) for small
changes of the equality. No nonlinear critical-point
equation has to be assumed solvable to specify this domain.

Let \(y_k(x)\) be the unique minimizer and set
\[
                         V_k(x)=F_k(x,y_k(x)).
 \tag{18}
\]
The implicit function theorem applied to (14) and
(13) makes both functions real analytic on all of
\(\mathcal D_k\). Uniqueness glues the local branches.
There is the explicit height bound
\[
       \|y_k(x)\|\le
           \frac{-\sum_e\mathcal J(\alpha_e(x))}
                         {\pi\delta_k(x)} .
 \tag{19}
\]
It follows by comparing the minimum with \(F_k(x,0)\)
in (12). Compact subsets of \(\mathcal D_k\)
therefore give bounded heights and uniform Hessian
bounds on the actual acute chart.

At \(z=x+iy_k(x)\), write
\[
                      -\mathscr S_k''(z)=A+iB,
               \qquad A>0,\quad A,B\text{ real symmetric}.
 \tag{20}
\]
The Cauchy--Riemann equations give
\[
        F_{xx}=-A,\qquad F_{xy}=B,\qquad F_{yy}=A.
 \tag{21}
\]
Differentiating the minimizing equation yields
\[
 \boxed{\qquad
 Dy_k=-A^{-1}B,\qquad
 \nabla V_k=\Re\nabla\mathscr S_k,\qquad
 V_k''=-A-BA^{-1}B<0 .
 \qquad}
 \tag{22}
\]
This is a real minimization Schur complement; it keeps
the full imaginary quadratic coupling. In particular
\(V_k\) is strictly concave on the convex domain
\(\mathcal D_k\). A critical point of \(V_k\) is exactly
a full critical point of \(\mathscr S_k\), since the
height equation already sets its imaginary gradient
to zero. Neither (16) nor concavity asserts that such
a critical point exists.

There is a genuine escape at a force boundary. If
\(x_\nu\to x_0\in\mathcal A\), with \(x_\nu\in\mathcal D_k\)
and \(\xi_k(x_0)\in\partial Z_{x_0}\), then
\(\|y_k(x_\nu)\|\to\infty\). Otherwise a bounded
subsequence would converge in (14) to a finite
minimizer at a boundary force, contrary to Theorem 1.

## 5. Exact tetrahedral volume and affine angle constraints

The reduced value has a fixed volume normalization.
For \(n=\alpha+it\), \(0<\alpha<1/2\), set
\[
       Z=e^{2\pi in}\in\mathbb H,\qquad
       \theta=\arg(2\sin\pi n),\qquad w=1/2-\alpha .
 \tag{23}
\]
Use the Bloch--Wigner function in its upper-half-plane
branch,
\[
                  D(Z)=\Im\operatorname{Li}_2(Z)
                            +\arg(1-Z)\log|Z|.
 \tag{24}
\]
The exact primitive identity is
\[
 \mathcal J(n)
     =\frac{i\pi}{2}(n-n^2)
          +\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi in})
          -\frac{i\pi}{12}.
 \tag{25}
\]
To prove it, differentiate, using
\[
 \Log(2\sin\pi n)
      =i\pi(1/2-n)+\Log(1-e^{2\pi in}).
 \]
The two sides of (25) then have the same derivative.
Their limit at \(n=0\) fixes the constant by
\(\operatorname{Li}_2(1)=\pi^2/6\).
Initially the identity can be checked at positive
imaginary height; both sides continue on the same
acute strip, where \(Z\in\mathbb H\).

Since \(1-Z=e^{i\pi(n-1/2)}2\sin\pi n\), the
retained arguments give
\[
        \arg(1-Z)=\theta-\pi w,\qquad
                         \log|Z|=-2\pi t .
 \tag{26}
\]
There is no branch reset: (6) makes
\(-\pi<\theta-\pi w<0\). Taking real parts in
(25) and using (26) proves
\[
              \boxed{\quad
              \frac{D(Z)}{2\pi}
                       =-\Re\mathcal J(n)-t\theta .
              \quad}
 \tag{27}
\]

At the minimizing height, \(t=Ly_k(x)\) and (14)
gives \(L^{\mathsf T}\theta=\pi\xi_k(x)\).
Thus \(\sum_e t_e\theta_e=\pi\xi_k(x)\cdot y_k(x)\),
which cancels the whole real quadratic/Fourier term
in (3). Consequently
\[
                   \boxed{\quad
                   V_k(x)=\frac1{2\pi}\sum_eD(Z_e),
             \qquad Z_e=e^{2\pi in_e(x+iy_k(x))}.
                   \quad}
 \tag{28}
\]
The normalization in (25) makes this an equality of
values, not only of differentials.

There is an equivalent finite angle maximization.
For each incidence put
\[
 \begin{split}
 A_e&=2\pi\alpha_e,\qquad
 B_e=\pi w_e-\theta_e,\qquad
 C_e=\pi w_e+\theta_e,\\
 A_e+B_e+C_e&=\pi .
 \end{split}
 \tag{29}
\]
All three angles are positive by (6).
Conversely, with \(A_e=2\pi\alpha_e\) fixed,
every positive pair \(B_e+C_e=2\pi w_e\)
comes from one real \(t_e\). Explicitly
\[
       e^{-2\pi t_e}
                  =\frac{\sin B_e}{\sin C_e},\qquad
       Z_e=\frac{\sin B_e}{\sin C_e}e^{iA_e}.
 \tag{30}
\]
These are the angles and modulus of the triangle
with vertices \(0,1,Z_e\).

Let \(\Lambda(t)=-\int_0^t\log(2\sin s)\,ds\)
on \((0,\pi)\). The elementary tetrahedral identity is
\[
             D(Z)=\Lambda(A)+\Lambda(B)+\Lambda(C).
 \tag{31}
\]
It can be checked without an additive ambiguity:
differentiate (24) on \(Z=r e^{iA}\) and use the
sine law (30). This gives the differential of the
right side. Both sides vanish at the flat limit
\(B\to0,\ C\to\pi-A\), because
\(\Lambda(\pi-A)=-\Lambda(A)\). Equivalently,
at fixed \(A\) the derivative with respect to \(B\)
of both sides is
\(\log(\sin C/\sin B)\).

Define the strict angle fiber at \(x\) by
\[
 \begin{gathered}
     0<B_e<2\pi w_e,\qquad C_e=2\pi w_e-B_e,\\
     L^{\mathsf T}B
          =\pi\{L^{\mathsf T}w-\xi_k(x)\}.
 \end{gathered}
 \tag{32}
\]
It is nonempty exactly when \(x\in\mathcal D_k\),
by (17). The minimizing-height angles are its
unique maximizer of
\[
                \sum_e\{\Lambda(A_e)+\Lambda(B_e)+\Lambda(C_e)\}.
 \tag{33}
\]
Indeed the derivative of one summand with respect
to \(B_e\) is
\[
               \log\frac{\sin C_e}{\sin B_e}
                                      =2\pi t_e .
 \tag{34}
\]
At the constructed point \(t=Ly_k(x)\), this
derivative annihilates \(\ker L^{\mathsf T}\),
the tangent space of (32). Its second derivative
is
\[
          -\cot B_e-\cot C_e
             =-\frac{\sin(B_e+C_e)}
                         {\sin B_e\sin C_e}<0 .
 \tag{35}
\]
Strict concavity proves uniqueness and global
maximality, including comparison with boundary
limits by continuity. Its maximum is \(2\pi V_k(x)\)
by (28)--(31).

The complete strict angle set in variables \((x,B)\)
is convex: (2), (29), and (32) are all strict
affine inequalities or affine equalities. The
tetrahedral volume is strictly concave there.
Indeed, in the two angles \(A,B\), its negative
Hessian is
\[
 \begin{pmatrix}
 \cot A+\cot C&\cot C\\
 \cot C&\cot B+\cot C
 \end{pmatrix}.
 \tag{35a}
\]
Both diagonal entries are positive by sine
addition, and its determinant is one because
\(A+B+C=\pi\). Summing is still strict
because \(L\) is injective, so the angle map
detects every variation of \((x,B)\).
An interior global maximum is therefore unique
and gives a critical point of the original
\(\mathscr S_k\), by (22). The maximum on the
closed angle set can instead lie on its boundary;
no interior-maximizer assertion is supplied.

These are positive ideal-tetrahedron volumes and
explicit angle equations for the actual source
action. A combinatorial face gluing, peripheral
marking and fundamental-class comparison would
be needed to identify their sum with the volume
of the knot complement. None is inferred from
the affine equations alone.

## 6. Clock directions and an arbitrary-exterior obstruction

The original clock directions give a useful check
of every sign and width in the criterion.
At crossing \(j\), changing only \(H_j\) changes
incidences \(n_{j1},n_{j2}\) by \(-1,+1\).
Consequently
\[
 h_{Z_x}(e_{H_j})=1-U_j,\qquad
 \xi_{k,H_j}=1+\sigma_j(U_j+2J_j)-2k_{H_j}.
 \tag{36}
\]
The necessary strict support inequality is
\(|\xi_{k,H_j}|<1-U_j\). On the acute physical
domain it forces
\[
                k_{H_j}=(1+\sigma_j)/2 .
 \tag{37}
\]
For this lift the inequality is exactly
\[
       |U_j+2J_j-1|<1-U_j
                  \quad\Longleftrightarrow\quad
                          0<J_j<J_j+U_j<1.
 \tag{38}
\]
The latter bounds already hold for the actual
acute source. Thus the separate clock directions
are compatible; they do not decide the coupled
physical-flow inequalities.

There is nevertheless a general failure of
coercivity inside the original source. Start
with any closed knot braid, keep its cut on an
old head, add a new last head, and append one
signed Markov crossing with the preceding head.
The exterior is arbitrary and remains unchanged.
Use the exact braid phase of the joint source,
including its actual closing pivots.

Let \(A\) be the exterior head degree at this
crossing, and \(U,H\) the new transfer and clock.
For the positive sign the new-head closure gives
\[
       J=V=A-U,\qquad I=A,\qquad
       n=(1-A,\ A-H,\ H-A+U,\ A-U).
 \tag{39}
\]
The old head exits with degree \(A\), so varying
the new transfer leaves every exterior degree
form unchanged. Its leading phase is
\[
                  H+H(2A-U)-A+U .
 \tag{40}
\]
In the independent new-transfer direction,
\[
        h_{Z_x}(e_U)=1-H,\qquad
                     \xi_{k,U}=1-H-2k_U .
 \tag{41}
\]
For the negative sign the role order gives
\[
        J=V=A,\qquad I=A+U,\qquad
        n=(1-A-U,\ A+U-H,\ H-A,\ A),
 \tag{42}
\]
again with the exterior degree unchanged. The
new phase is \(H-H(U+2A)+A\), so
\[
                 h_{Z_x}(e_U)=H,\qquad
                        \xi_{k,U}=-H-2k_U .
 \tag{43}
\]
These calculations retain the actual checked
degree order at both signs. The new pivot has
only bounded logarithmic size in the root
scaling, so it adds no leading transfer term;
it is not discarded from the finite source.

At every acute point \(0<H<1\).
In (41), \(k_U=0\) saturates the positive
support inequality. Every other integer
\(k_U\) violates one of the two support
inequalities. In (43), \(k_U=0\) saturates the
negative inequality, and every other integer
again violates one. Hence:

**Proposition 2.** Every such stabilized presentation
has \(\mathcal D_k=\varnothing\) for every integral
Fourier lift \(k\). This is independent of the
original exterior and all its other variables.

Compatible signed stabilizations of an
alternating-generator-sign braid preserve its
alternating sign pattern, so the acute tube can
remain nonempty while all its coercive-height
domains are empty. The exact original Markov
contraction removes this added cell and retains
the same knot invariant, as proved in the
[source-homology note](actual_cotangent_homology_and_global_gluing_criterion.md),
Section 2. Thus the obstruction belongs to the
unreduced source presentation and does not
contradict source-preserving Markov pruning.
It is not an isolated calculation for an unknot
or a change to an arbitrary co-source.

## 7. Scope

Theorems (9)--(22) replace a missing imaginary
properness assertion by an exact linear
feasibility condition, a complete boundary
classification, and a uniquely normalized
analytic reduction. Equations (28)--(35)
identify its value with a finite positive
tetrahedral angle optimization for the actual
action. These statements apply to every
specified original acute source with real cut.

Neither feasibility nor an interior maximum is
automatic, and the Markov calculation shows
why it cannot be automatic for unreduced
presentations. Even an interior maximum would
still require its geometric identification and
a nonzero intersection with the original
finite residue cycle. No volume limit or
general short-partial-filling theorem is
claimed.

For historical coverage, the volume method is
classical; see
[Rivin, *Euclidean structures on simplicial surfaces and hyperbolic volume* (1994)](https://annals.math.princeton.edu/1994/139-3/p02)
and
[Futer--Guéritaud, *From angled triangulations to hyperbolic structures*](https://arxiv.org/abs/1004.0440).
The latter describes the linear angle polytope and
volume critical-point criterion for an already
supplied ideal triangulation of a manifold.
That input is not established for (32).
The publisher's bibliographic record and the
survey abstract were checked for coverage;
none of their proofs is a premise above.
The claim here is the derivation and normalization
for this exact incidence source, not a new
general dilogarithm or Rivin variational principle.

## Direct written source versions

| Source | SHA-256 |
| --- | --- |
| research_original_incidence_acute_tube.md | 17892b7654e7f7668be2fde7743d5adab0bf8e9dc813c29f8114023e740e78f6 |
| research_joint_clock_phase_equations.md | 71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867 |
| actual_cotangent_homology_and_global_gluing_criterion.md | 630877ca81dd3fafe096bac5c3987c4eba9a5de134c3817c5cee57a374b5fb59 |

The arguments above are written directly. Recession,
Legendre duality, and Schur complements are established
methods; no novelty is claimed for those general tools.
The retained source force, exact remainder, finite
angle constraints and signed arbitrary-exterior
obstruction are the assertions proved here.
