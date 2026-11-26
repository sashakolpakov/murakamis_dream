# The geometric saddle before the last two crossings

The complete geometric point of the adjacent three-crossing
pendant belongs to the branch selected by the original endpoint
of \(\gamma=MJM^3e_0\). This note proves that identification in
the original canonical coordinates. It also writes the exact
remaining contraction and identifies a nondegenerate stationary
point of its candidate phase.

The characteristic branch and its phase extend holomorphically
to the saddle. An asymptotic expansion for an actual finite
polynomial interpolation of \(\gamma\) there is a separate
statement. The real-color expansion alone does not give it.
Nor does this local calculation prove a global contour comparison
or a nonzero coefficient in the whole boundary polynomial.

## 1. The original canonical maps

Use the positive crossing matrix \(M\), reversal \(J\), and the
coefficient shift \(E:f_j\mapsto f_{j-1}\) from
[the exact boundary current](research_three_crossing_boundary_current.md).
Write \(\xi=e^{2\pi i x}\) for the physical clock, and
\[
                 K=\frac{-1+(\xi-1)E}{\xi}.                    \tag{1}
\]
The active point maps of the literal crossing and turn are
\[
\begin{split}
\mathcal M:(\xi,K)&\longmapsto
                   (\xi+\xi K+1,-\xi^{-1}),\\
\mathcal J:(\xi,E)&\longmapsto(\xi^{-1},E^{-1}).
\end{split}                                                    \tag{2}
\]
These are the inverses of the corresponding pullbacks on
observables. They are the actual maps of the Newton crossing
kernel, as proved in
[the original canonical-graph calculation](actual_newton_twist_canonical_graph.md),
Sections 3--4. No physical turn is removed.

The incoming three-crossing curve has parameter \(\tau\):
\[
                \xi=\tau,\quad
                K=-\frac1{\tau-1},\quad
                E=-\frac1{(\tau-1)^2}.                          \tag{3}
\]
Set
\[
 r=\tau^2-3\tau+3,\qquad
 z=4-5\tau+4\tau^2-\tau^3,\qquad P=zr-1.
 \tag{4}
\]
Apply first the turn and then the crossing in
\(\gamma=MJM^3e_0\). Direct substitution in (1)--(3) gives
\[
 \boxed{\quad
       \xi_\gamma=r,\qquad K_\gamma=-\tau,\qquad
       E_\gamma=-\frac{(\tau-1)^2}{\tau-2}.
       \quad}                                                  \tag{5}
\]
For example the clock after the turn is \(1/\tau\);
the next clock is \(r\), and the new \(K\) is \(-\tau\).

The remaining literal vector operation is \(JM^2\). Its two
crossing clocks, followed by its turn, are
\[
         z-\tau,\qquad z-\frac1r,\qquad
         Y=\frac rP .                                          \tag{6}
\]
Here \(Y=e^{2\pi i y}\) is the final coefficient clock, paired
with the actual boundary Newton polynomial. It is not
\(\gamma\)'s inverse clock.

## 2. Which recurrence branch contains the geometric point?

In the left-endpoint profile of \(\gamma\), the convenient
clock is
\[
                 X=e^{-2\pi i x}=\xi_\gamma^{-1}.
\]
The two characteristic roots for its normalized recurrence are
\[
 \lambda=\frac{3-2X+\sqrt{4/X-3}}2,\qquad
 \mu=\frac{3-2X-\sqrt{4/X-3}}2.                                 \tag{7}
\]
The square root is \(1\) at \(x=0\). On the curve (5),
\[
\boxed{\quad
 X=\frac1r,\qquad
 \lambda=-\frac{(\tau-2)^3}{r},\qquad
 \mu=\frac{(\tau-1)^3}{r},\qquad
 \lambda-\mu=3-2\tau.
 \quad}                                                        \tag{8}
\]
Indeed \(4r-3=(2\tau-3)^2\). The original left endpoint
\(\lambda(0)=1,\mu(0)=0\) is \(\tau=1\), not \(\tau=2\).
Also \(-\lambda/(2-X-X^{-1})=E_\gamma^{-1}\), exactly as
required by the original consecutive-coefficient ratio.

Let \(\tau_{\mathrm g}\) be the negative-pendant geometric
root identified in
[the marked quartic calculation](research_three_crossing_pendant_geometric_branch.md):
\[
 v(\tau_{\mathrm g})=2i,\qquad
 v(\tau)=(\tau-2)^2(\tau^2-2\tau+2),\qquad
 |\tau_{\mathrm g}-(944+1303i)/1000|<1/1000.
 \tag{9}
\]
For the positive source \(M^3\), use its conjugate
\[
                   \tau_*=\overline{\tau_{\mathrm g}},
                   \qquad v(\tau_*)=-2i.                       \tag{10}
\]
This is reflection of the original marked geometry. Using
\(\tau_{\mathrm g}\) without conjugating the positive quantum
clock would put the candidate on the wrong side of the color
interval.

Use principal logarithms to define
\[
                 x_*=\frac{\log r(\tau_*)}{2\pi i},\qquad
                 y_*=\frac{\log Y(\tau_*)}{2\pi i}.             \tag{11}
\]
The exact rational root rectangle in (9), with its imaginary
part conjugated, gives
\[
\begin{split}
 -13/20&<\Re r<-63/100,&
 36/25&<\Im r<73/50,\\
 9/100&<\Re Y<4/25,&
 3/5&<\Im Y<7/10 .
\end{split}                                                    \tag{12}
\]
Evaluate \(r=(\tau-3/2)^2+3/4\) and
\(z=2+(1-\tau)^2(2-\tau)\) before forming \(Y=r/(zr-1)\);
these factorizations give the displayed rational bounds
directly. Their denominator is bounded away from zero.

They imply the useful logarithmic rectangle
\[
\boxed{\quad
 3/10<\Re x_*<1/3,\quad -1/10<\Im x_*<0,\qquad
 1/5<\Re y_*<1/4,\quad 0<\Im y_*<1/10 .
 \quad}                                                        \tag{13}
\]
For the argument of \(r\), its ratio \(-\Re r/\Im r\)
lies between \(2/5\) and \(1/2\), while
\(\tan(\pi/10)<1/3\) and \(\tan(\pi/6)>1/2\).
Also \(1<|r|<8/5<e^{\pi/5}\).
For \(Y\), the imaginary-to-real ratio exceeds \(15/4\),
whereas \(\tan(2\pi/5)=\sqrt{5+2\sqrt5}<31/10\).
Finally \(e^{-\pi/5}<3/5<|Y|<1\).
These facts prove (13). For orientation only,
\[
 x_*\simeq .3160347182-.0732789305i,\qquad
 y_*\simeq .2210215475+.0646684488i .
\]

**Proposition 1.** The characteristic root at \(x_*\) is the
analytic continuation of the branch selected by the actual
left endpoint. It is strictly dominant there. More generally,
for every \(b<1/2\), \(H<\infty\), that branch is holomorphic
on a neighborhood of
\[
              0\le\Re x\le b,\qquad -H\le\Im x\le0,             \tag{14}
\]
and has a uniform strict modulus gap on this rectangle.

**Proof.** For \(0<\Re x<1/2,\Im x\le0\), \(X\) lies in
the lower half-plane and \(|X|\le1\). Consequently \(4/X-3\)
has positive imaginary part. Its selected square root has
positive real and imaginary parts. So does \(3-2X\), whose
real part is at least \(1\). Therefore
\[
 |\lambda|^2-|\mu|^2
     =\Re\bigl((3-2X)\overline{\sqrt{4/X-3}}\bigr)>0.             \tag{15}
\]
On the vertical side \(\Re x=0\), \(0<X\le1\);
the same expression is strictly positive and real.
The discriminant never vanishes on (14), and neither does
\(\lambda\). Compactness now supplies a uniform gap and a
holomorphic neighborhood. At (10), \(3-2\tau_*\) is in the
first quadrant, so (8) uses exactly this square root.
In fact the rational rectangle already gives
\[
 \left|\frac{\mu(x_*)}{\lambda(x_*)}\right|
       =\left|\frac{\tau_*-1}{\tau_*-2}\right|^3<\frac12 .
\]
\(\square\)

The phase \(I(x)=\int_0^x\log\lambda(s)\,ds\) and the nonzero
profile amplitude \(\sqrt{\lambda/(\lambda-\mu)}\), both
normalized at zero, therefore extend to (14). Proposition 1
is about those analytic functions. It is not a theorem
about evaluating the finite vector at a nonintegral index.

## 3. The exact remaining row and its local phase

Let \(F_j=(q^2;q^2)_j\), and retain the original Newton
polynomials \(e_i\). The exact two-crossing identity gives
\[
 (JM^2)_{ij}
 =Nq^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2},
 \qquad i+j<N,
 \tag{16}
\]
with zero entries outside that triangle. Thus the entire
remaining free-boundary contraction is
\[
 F_N(w)=N\sum_{i+j<N}
       q^{(i-j)^2}\frac{F_{i+j}}{F_i^2F_j^2}
                     e_i(w)\gamma_j .                         \tag{17}
\]
Equation (17) retains every original coefficient and every
normal derivative. Its proof is the finite matrix identity in
[the two-crossing formula](research_degree_two_power_two_formula.md).

Put \(\mathcal J(z)=\int_0^z\log(2\sin\pi s)\,ds\), with the
original branch on \(0<\Re z<1\). The known real-color
profile of \(\gamma\) has the exact factor
\[
 (-q)^j=e^{-i\pi Nx}e^{i\pi x},\qquad x=j/N.
 \tag{18}
\]
Its exponential phase can therefore be written
\(I(x)-2\mathcal J(x)-i\pi x\); the factor \(e^{i\pi x}\)
stays in its amplitude.
At \(w=-2\), the local candidate phase for (17) is
\[
\boxed{\quad
 \Phi(x,y)=I(x)+\mathcal J(x+y)-4\mathcal J(x)
       -6\mathcal J(y)+\mathcal J(2y)
       +\frac{i\pi}{2}\bigl((x-y)^2-x+y\bigr).
 \quad}                                                        \tag{19}
\]
All its factorial arguments at (13) lie strictly in their
original strips: \(x,y,x+y,2y\) have real parts between
zero and one.

The alternative exact choice
\((-1)^j=e^{i\pi Nx}\) changes (19) by \(2\pi i x\).
It gives the same finite lattice sum, but labels the
following stationary point by a different Fourier alias.
No Fourier current is omitted by recording this choice.

**Proposition 2.** The point (11) satisfies the full
logarithmic equations
\(\Phi_x=\Phi_y=0\), on the branches just specified.
Its Hessian is nonsingular; on its horizontal tangent
plane the real Hessian is negative definite.

**Proof.** With \(X=e^{-2\pi i x}\), \(Y=e^{2\pi i y}\),
exponentiating the two derivatives gives
\[
 e^{\Phi_x}
    =\frac{\lambda X(X-Y)}{Y(1-X)^4},\qquad
 e^{\Phi_y}
    =\frac{Y(Y-X)(1+Y)^2}{(1-Y)^4}.                             \tag{20}
\]
Substitute (8) and \(Y=r/P\). The first is identically one
as a rational function of \(\tau\). For the second,
\[
 e^{\Phi_y}-1
 =\frac{rP\,[v(\tau)^2+4]}
          {(\tau-2)^7(\tau^2-2\tau+2)^4}.                       \tag{21}
\]
All denominators are nonzero at (10); hence both expressions
in (20) equal one there.

Here the logarithmic branch is fixed, not inferred from
exponentiation. For \(a+ib\) in an original factorial strip,
\[
 \arg\sin\pi(a+ib)=\arctan\{\cot(\pi a)\tanh(\pi b)\}.
 \tag{22}
\]
The rectangle (13) and the first-quadrant value of \(\lambda\)
give
\[
\begin{gathered}
 0<\arg\lambda<\pi/2,\qquad
 |\arg\sin\pi x|<\pi/10,\qquad
 |\arg\sin\pi y|<3\pi/20,\\
 |\arg\sin2\pi y|<\pi/15,\qquad
 |\arg\sin\pi(x+y)|<\pi/30.
\end{gathered}                                                  \tag{23}
\]
For example \(\cot(\pi/5)<3/2\),
\(\cot(2\pi/5)<1/3\), and
the absolute cotangent on \(1/2<\Re(x+y)<7/12\)
is less than \(1/3\). Use \(|\tanh s|<|s|\) and
\(|\arctan s|<|s|\) to obtain (23).
The imaginary magnitude of either explicit phase derivative
in (19) is less than \(9\pi/20\).
Consequently
\[
       |\Im\Phi_x|<83\pi/60<2\pi,\qquad
       |\Im\Phi_y|<91\pi/60<2\pi.
\]
Together with (20), these strict inequalities force both
derivatives to be zero, not a nonzero integer multiple of
\(2\pi i\).

There is also an exact transversality proof. Along (8),
\(x'(\tau)=(2\tau-3)/(2\pi i r)\ne0\), and
\[
       \Phi_{xy}=\frac{2\pi i}{rY-1}
                 =\frac{2\pi iP}{(\tau-2)(\tau-1)^4}\ne0.
 \tag{24}
\]
Differentiate the identically zero \(\Phi_x\) along this
curve. Differentiating (21) at its simple root then yields
\[
 \det\Phi''
 =-\frac{\Phi_{xy}}{x'(\tau)}
      \frac{rP\,2v(\tau)v'(\tau)}
           {(\tau-2)^7(\tau^2-2\tau+2)^4}\ne0.                 \tag{25}
\]
The simplicity of \(v(\tau)+2i=0\) is supplied by (9).

For completeness, the real Hessian can be bounded without
floating-point eigenvalues. Writing \(\Phi''=i\pi H\), its
rational entries on the source curve are
\[
\begin{split}
H_{xx}&=\frac{6r}{(\tau-2)(2\tau-3)}-1
            +\frac{rY+1}{rY-1}-4\frac{r+1}{r-1},\\
H_{xy}&=\frac2{rY-1},\\
H_{yy}&=\frac{rY+1}{rY-1}
             -6\frac{Y+1}{Y-1}+4\frac{Y^2+1}{Y^2-1}+1 .
\end{split}                                                    \tag{26}
\]
Exact rectangle arithmetic on (9), using the factorizations
before (12), gives
\[
              \Im H_{xx}>2,\qquad
              \Im H_{yy}>4,\qquad
              |\Im H_{xy}|<1/5.                              \tag{27}
\]
Thus \(-\Re\Phi''\ge(9\pi/5)I\) on the horizontal tangent
plane. All denominator intervals are separated from zero.
The focused verifier below reproduces these rational
inequalities. \(\square\)

## 4. From the saddle to the finite boundary source

The canonical maps (2)--(6) identify the original geometric
quartic point, and (19)--(27) give its local remaining-row
saddle with its logarithmic alias fixed. The separate
[complex next-step theorem](research_three_crossing_complex_next_step.md)
now proves the actual column's holomorphic asymptotic there,
with the original endpoint current and chirp retained.
The [whole preparation-error theorem](research_three_crossing_global_preparation_error.md)
bounds the discarded preparation error below the selected rate.
The [absolute action comparison](research_three_crossing_action_volume_calibration.md)
identifies that rate with the original partial-exterior volume
divided by \(2\pi\).

The [full local boundary theorem](research_three_crossing_full_boundary_asymptotic.md)
now proves the prepared main source's contour coefficient and bounds
all complementary contours and omitted real index sectors. It uses
the exact cellwise residue identity, whose principal coefficient is
\(+1\), together with seven horizontal and 144 boundary estimates.
The characteristic-root gap and the action identity remain distinct
inputs; neither alone determines what the original finite source
observes. The separate
[whole-period estimate](research_three_crossing_whole_period_source.md)
now supplies the global input for the
[long-closing theorem for this piece](research_three_crossing_long_closing_fiber.md).

## 5. Exact verification

[check_three_crossing_geometric_remaining_saddle.py](../experiments/check_three_crossing_geometric_remaining_saddle.py)
checks the canonical maps, both exponentiated stationary
equations, all displayed rational denominator exclusions,
and the rectangle bounds (12) and (27). The root-isolation
input is the exact four-disk certificate in the earlier
geometric-branch checker. No numerical gradient or fitted
asymptotic is used as a proof. The
[saved exact result](../repro/results/research-three-crossing-geometric-remaining-saddle.json)
records fourteen rational identities, ten excluded factors,
eight interval denominator bounds, and the script and
dependency hashes.
