# Exact factorial bounds on clipped quantum Legendre chains

Private written proof, 19 November 2026.

The positive Legendre contour has an explicit quantum-factorial block
whose amplitude remains controlled as the angles approach their true
faces and its radial coordinates grow logarithmically. The bounds below
pay the entire moving clipped boundary and the calibrated radial prism.
They also give the nonzero coefficient of this specified block period.

This is not an identification of an original braid source with that
block. In particular, the original cotangent support cycle, the
five-function crossing transformation, and wrong-edge alias walls are
not replaced by positive angles. The complete directs are L, the
classical marked Legendre construction, and F, the exact factorial
interpolant. The all-height Gamma estimate also has established coverage
in research_balanced_gauss_global_cardinal_strip.md, Section 3; its
required endpoint version is proved again below from F.

## 1. The marked positive data and an exact finite-level block

Use L's positive chart in dimension \(t\). Put \(c_0=2\pi i\),
\[
 W(x)=\sum_{j=1}^t\operatorname{Li}_2(e^{x_j})+Q_{\rm quad}(x),
 \qquad
 Q_{\rm quad}(x)=\tfrac12x^{\mathsf T}(I-C)x
                     +i(\kappa-\pi\mathbf1)^{\mathsf T}x,
 \tag{1}
\]
where \(C=C^{\mathsf T}\) is real and \(\kappa\) is real. Retain
the exact logarithmic and dilogarithmic marks of L. Its angle domain is
\[
 \gamma(\theta)=\kappa-C\theta,\qquad
 \beta(\theta)=\pi\mathbf1-\theta-\gamma(\theta),\qquad
 P=\{\theta,\beta(\theta),\gamma(\theta)>0\}.
 \tag{2}
\]
The supplied complete critical point \(x_*=\rho_*+i\theta_*\)
lies in this domain and satisfies \(W_x(x_*)=0\). The positive
Legendre graph is
\[
 \rho_L(\theta)=
       \log\frac{\sin\beta(\theta)}{\sin\gamma(\theta)},\qquad
 x_L(\theta)=\rho_L(\theta)+i\theta.
 \tag{3}
\]
Write \(V_*=\operatorname{Im}W(x_*)\). L proves
\(\operatorname{Im}W(x_L(\theta))=V(\theta)\), the marked
Rivin volume, with unique maximum \(V_*\), and supplies its
nonvanishing Jacobian. These are classical data for the theorem,
not a proposed substitution into a physical occupation sum.

Let \(\widehat F_N\) be F's exactly normalized function:
\[
 \begin{split}
 G_N(z)&=(2\pi/N)^z\Gamma(z+1)
  \prod_{k\ge1}
  \frac{\Gamma(Nk+z+1)}
       {\Gamma(Nk-z)(Nk)^{2z+1}},\\
 \widehat F_N(z)&=
   e^{i\pi z(z+1)/(2N)-i\pi z/2}G_N(z).
 \end{split}
 \tag{4}
\]
It is holomorphic and nonzero on \(-1<\operatorname{Re}z<N\),
and
\[
 \widehat F_N(0)=1,\qquad
 \frac{\widehat F_N(b+n)}{\widehat F_N(b)}
                    =(Q^{1+b};Q)_n,\qquad Q=e^{c_0/N}.
 \tag{5}
\]
The shifts \(b=(b_1,\ldots,b_t)\) lie in a fixed closed polydisk
\(|b_j|\le b_0<1\), enlarged slightly within that unit polydisk
when derivatives are taken. Define the literal holomorphic block
\[
 Z_{N,b}(x)=
 \exp\!\left\{\frac{N}{c_0}
        [Q_{\rm quad}(x)+t\operatorname{Li}_2(1)]\right\}
 \prod_{j=1}^t
 \frac{\widehat F_N(b_j)}
      {\widehat F_N(Nx_j/c_0+b_j)}.
 \tag{6}
\]
Thus every denominator in (6), at an allowed integer index
\(Nx_j/c_0=n\), is the actual shifted reciprocal factorial in
(5). The exponential and all numerator constants in (6) are
part of its definition. In particular no periodic interpolation
factor or unknown source normalization has been chosen.
The factor \(t\operatorname{Li}_2(1)\) makes its leading
potential exactly (1); it is not a freely adjustable imaginary
action constant.

## 2. Uniform endpoint and height estimates

Set
\[
 I(z)=\frac{\operatorname{Li}_2(1)
                  -\operatorname{Li}_2(e^{c_0z})}{c_0}.
 \tag{7}
\]
Its mark is the continuation from \(0<z<1\); in particular
\(I'(z)=\operatorname{Log}(1-e^{c_0z})\).
For \(0<a\le1/4\), uniformly on
\[
        a\le\operatorname{Re}z\le3/4,\qquad
        \operatorname{Im}z\in\mathbb R,\qquad Na\ge2,
 \tag{8}
\]
F's Gamma product implies
\[
 \log\widehat F_N(Nz)
 =NI(z)+\tfrac12\operatorname{Log}[iN(1-e^{c_0z})]
     +\frac{\pi\cot(\pi z)}{12N}
     +O((Na)^{-3}+N^{-3}).
 \tag{9}
\]
The half logarithm has F's mark; no independent square root
is reset. The constant in this estimate is independent of
the imaginary height.

Here are the endpoint details. Apply the Stirling formula
through \(1/(12Z)\) to \(Nz\), \(N(k+z)\), and \(N(k-z)\)
in (4), first shifting Gamma by its functional equation where
necessary. Its remainder on the closed right half-plane is
bounded by \(C|Z|^{-3}\); F derives that bound from the
Bernoulli integral remainder. The first term is at most
\(C(Na)^{-3}\). The remaining sum is bounded by
\[
 CN^{-3}\sum_{k\ge1}
        [(k+a)^{-3}+(k-3/4)^{-3}]\le CN^{-3}.
 \tag{10}
\]
Neither bound depends on the imaginary parts. The same
convergent sine-product summations as in F give \(I\), the
marked half logarithm, and the cotangent term in (9).
Moreover \(|\cot\pi z|\le C/a\) on (8).
This proves (9), including a bound for its holomorphic
logarithmic error and therefore for the reciprocal.

For bounded \(b\) in the indicated disk the same product at
bounded argument gives
\[
 \widehat F_N(b)=(-c_0/N)^b\Gamma(1+b)(1+O(N^{-1})),
 \qquad \operatorname{Log}(-c_0)=\log(2\pi)-i\pi/2.
 \tag{11}
\]
For example the logarithm of the infinite Gamma-product
correction is \(O(N^{-2})\) there; the explicit Gaussian
factor supplies the marked \(O(N^{-1})\) correction.
There are no Gamma poles or zeros on this disk.

Take \(x=\rho+i\theta\) with \(0<\theta<\pi\), and assume
\[
       \epsilon\le\theta\le\pi-\epsilon,\qquad
       |\rho|\le C_1(1+|\log\epsilon|),\qquad
       N\epsilon\longrightarrow\infty.
 \tag{12}
\]
Apply (9) with \(z=x/c_0+b/N\). Taylor's formula along this
bounded shift gives
\[
 \widehat F_N(Nx/c_0+b)=
 [iN(1-e^x)]^{1/2}
 e^{NI(x/c_0)}(1-e^x)^b
                  (1+O((N\epsilon)^{-1})).
 \tag{13}
\]
Indeed \(|e^x/(1-e^x)|\le C/\epsilon\) throughout the
shift segment, so the quadratic remainder of \(NI\) is
\(O((N\epsilon)^{-1})\); the half logarithm has the same
bound. Formula (9) pays the rest. These estimates are uniform
in \(b\). On a fixed interior compact the error improves to
\(O(N^{-1})\), with all fixed derivatives on smaller buffers.

On the upper half-plane of \(e^x\), \(\operatorname{Log}(1-e^x)\)
has argument in \((-\pi,0)\), and \(i(1-e^x)\) is in the right
half-plane. Its square root continued from the real-index
interval is exactly the right-half-plane square root in (13).
Together with (11) this fixes every mark in
\[
 \begin{split}
 Z_{N,b}(x)
 &=N^{-t/2-\sum b_j}\,
       e^{NW(x)/c_0}\,A_b(x)
          (1+O((N\epsilon)^{-1})),\\
 A_b(x)&=\prod_{j=1}^t
   \Gamma(1+b_j)(-c_0)^{b_j}
   [i(1-e^{x_j})]^{-1/2}(1-e^{x_j})^{-b_j}.
 \end{split}
 \tag{14}
\]
The power of \(N\) always uses the real logarithm.

## 3. The full logarithmically clipped chains

Fix \(A>0\) and, for sufficiently large \(N\), put
\[
 \epsilon_N=A\log N/N,\qquad
 P_N=\{\theta\in P:
       \theta_j,\beta_j(\theta),\gamma_j(\theta)\ge\epsilon_N
                         \text{ for all }j\}.
 \tag{15}
\]
It is a compact convex polytope containing \(\theta_*\).
Use the actual chains and homotopy
\[
 x_s(\theta)=
       (1-s)\rho_*+s\rho_L(\theta)+i\theta,\qquad
 0\le s\le1,\quad\theta\in P_N.
 \tag{16}
\]
Every shape stays in the upper half-plane. From (3),
\[
 |\rho_L|\le C+|\log\epsilon_N|,\qquad
 \|D_\theta\rho_L\|\le C/\epsilon_N.
 \tag{17}
\]
Consequently (12)--(14) apply uniformly to the entire
homotopy, with relative error \(O(1/\log N)\).
Here the lower bound for \(\theta\) is sufficient for (13);
the other two angle bounds pay the logarithmic radius in (17).

All \(A_b(x_s)\) and their reciprocals have polynomial size
in \(N\), uniformly in \(s,\theta,b\). To check this directly,
\(e^{|\rho_s|}\le C\epsilon_N^{-C}\), while
\[
       |1-e^{\rho_s+i\theta}|\ge c\epsilon_N.
 \tag{18}
\]
For \(0<\theta\le\pi/2\), minimizing over the radius gives
\(\sin\theta\); for \(\theta\ge\pi/2\) the minimum is one.
This proves (18), and the upper bound is immediate from (17).
The arguments of the logarithms in (14) remain bounded.
The Gamma factors are units on the fixed shift polydisk.
In particular the following is a genuine whole-chain bound:
\[
 N^{-C}e^{N\operatorname{Im}W(x_s)/(2\pi)}
 \le |Z_{N,b}(x_s)|
 \le N^C e^{N\operatorname{Im}W(x_s)/(2\pi)} .
 \tag{19}
\]
No compact-height hypothesis has been extended without proof.

The graph Jacobian and all homotopy minors have polynomial
upper bounds, by (17) and
\(|\partial_s x_s|=O(1+|\log\epsilon_N|)\).
L proves that \(D_\theta x_L\) is everywhere invertible;
at the selected maximum it is a fixed nonzero matrix.
Thus no vanishing density at that point is hidden in (19).

There is a fixed \(\delta>0\), independent of \(N\), such that
\[
 \sup_{\theta\in\partial P_N,\ 0\le s\le1}
           \operatorname{Im}W(x_s(\theta))\le V_*-\delta.
 \tag{20}
\]
For completeness, both functions
\(V(\theta)\) and \(F_0(\theta)=\operatorname{Im}W(\rho_*+i\theta)\)
extend continuously to \(\overline P\), have their unique
maximum \(V_*\) at \(\theta_*\), and have a strict gap on
\(\partial P\). For \(F_0\) this also follows directly from
its negative diagonal angle Hessian and its critical point.
Every point of \(\partial P_N\) has some angle equal to
\(\epsilon_N\); compactness therefore places all its limit
points in \(\partial P\). The gaps persist uniformly for
large \(N\). Finally L's radial convexity gives, on (16),
\[
 \operatorname{Im}W(x_s(\theta))
        \le(1-s)F_0(\theta)+sV(\theta),
 \tag{21}
\]
which proves (20). The finite number of fixed face normals
also bounds the face volumes of \(P_N\) uniformly.

## 4. Exact deformation and the nonzero block coefficient

Let \(\Omega_{N,b}=Z_{N,b}(x)\,dx_1\wedge\cdots\wedge dx_t\),
with exactly this normalization. On the entire homotopy (16)
and a neighborhood of it this form is holomorphic. Indeed
all denominator arguments in (6) remain strictly within
F's zero-free strip. Stokes on the polytope homotopy gives the
exact difference between its integrals on \(x_1(P_N)\) and
\(x_0(P_N)\) as its oriented boundary-prism integral.
Equations (19)--(20), the polynomial minors, and the bounded
face volumes prove
\[
 \left|\int_{x_1(P_N)}\Omega_{N,b}
            -\int_{x_0(P_N)}\Omega_{N,b}\right|
       \le N^C e^{N(V_*-\delta)/(2\pi)}.
 \tag{22}
\]
This includes all moving clipped faces. It is an actual
finite-level comparison, not an assumption about an
unspecified amplitude at radial infinity.

Here is also its coefficient. Set
\[
 J_*=D_\theta x_L(\theta_*),\quad H_*=W_{xx}(x_*),\quad
 \mathcal H_*=-J_*^{\mathsf T}H_*J_*/c_0.
 \tag{23}
\]
L gives \(\operatorname{Re}\mathcal H_*>0\) and
\(\det J_*\ne0\). Give \(\sqrt{\det\mathcal H_*}\) the
Gaussian mark on the accretive symmetric matrices, continued
from positive real matrices. It is nonzero. With the
orientation \(d\theta_1\wedge\cdots\wedge d\theta_t\), put
\[
 C_b=(2\pi)^{t/2}
       \frac{A_b(x_*)\det J_*}{\sqrt{\det\mathcal H_*}}.
 \tag{24}
\]
It is a nonzero holomorphic function of the shift parameters.
Both periods in (22) have the same expansion
\[
 \boxed{\quad
 \int_{x_j(P_N)}\Omega_{N,b}
   =N^{-t-\sum b_i}e^{NW(x_*)/c_0}
                       \bigl(C_b+O(N^{-1})\bigr),
       \qquad j=0,1 .
 \quad} \tag{25}
\]
The error is uniform on the indicated shift polydisk.

To verify all parts of this saddle statement, fix a small
neighborhood of \(\theta_*\) independent of \(N\).
Formula (14) there has holomorphic relative \(O(N^{-1})\)
error. Taylor expansion of \(W\circ x_L\) and the accretive
matrix (23) give its usual real Gaussian integral
\((2\pi/N)^{t/2}/\sqrt{\det\mathcal H_*}\).
Odd cubic terms integrate to zero on a symmetric shrinking
neighborhood; the bounded fourth and amplitude derivatives
give relative \(O(N^{-1})\). A growing central ball and
Gaussian tails justify the expansion.
On its entire complement in \(P_N\), strict concavity,
continuity on \(\overline P\), and (19) give a fixed
exponential loss, absorbing all polynomial endpoint factors.
This proves (25) for \(j=1\). Equation (22) proves it for
\(j=0\) with the same coefficient, rather than a separately
chosen saddle sign. No equality of unmarked square roots is used.

Fixed derivatives in \(b\) follow by Cauchy on a slightly
larger shift polydisk, after factoring out the explicit
\(N^{-t-\sum b_i}\). If \(b_i=b_i(u)\) is a bounded
holomorphic scaled-meridian function, this power must remain:
its derivatives can contain \(\log N\). For \(u=N\mu\),
true fixed-\(q\) \(\mu\)-derivatives additionally cost the
corresponding powers of \(N\). The statement does not erase
these terms or identify them with a whole braid normal.

## 5. Source and alias scope

The finite function (6), the marks (4),(11),(14), and the
oriented chains (15)--(16) specify exactly what (19),(22),(25)
estimate. They pay the endpoint amplitude and the noncompact
radial behavior left conditional for a quantum form in L.
They do not prove that a physical R/X word, its pointed
prefactor, or its finite cotangent support cycle equals this
block period. Such an identification must preserve its
entire Gaussian, factorial, framing and meridian lines.
An additional extensive monomial is an action term, not an
uncontrolled amplitude to be absorbed into (19).

The faces in (20) are the true faces of the single marked
positive polytope (2). They are not wrong-edge alias walls.
L explicitly records a counterexample to volume domination
on weak wrong-edge loci. Neither (20) nor a bound on a
positive alias bulk chain applies to those different face
sources. Likewise this proof does not discard any cotangent
boundary or alias term of the original finite-sum cycle.
Those currents must be excluded or controlled by an actual
source transformation.

The resulting reusable estimate is a whole moving-domain
quantum bound and a selected coefficient for an explicitly
normalized positive factorial block. No geometric contribution
to the original knot source, arbitrary short-component
comparison, or new volume-conjecture case is inferred.

## Complete proof directs

* L: notes/general_legendre_rivin_contour.md, 421 lines,
  SHA256 b51be11036b05fbccd586c2d0a4505559631870357cf128dd256dcc87e26970b.
* F: notes/exact_factorial_interpolation_and_complex_contours.md,
  226 lines, SHA256
  1f34f65437dfe0bfb4062a7a74840beae1676353cf13bb8a86f8849a8a36bc72.

Both complete directs were freshly read nontruncated in this
author sequence. Only written mathematics and text/hash
operations are used. Frozen and public files are unchanged.
