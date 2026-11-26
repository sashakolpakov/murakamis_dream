# The actual Alexander-hole cylinder as a relative Morse cap

Private written proof, 18 November 2026.

The short-cutoff decomposition [K] assigns coefficient \(+1\) to
each counterclockwise Alexander-hole contour. At a simple actual
operator node satisfying [M], that cylinder has an explicit relative
two-cycle description. Its lower and upper boundaries remain in the
original fibers \(\xi=0\) and \(\xi=R\). The resulting signed cap
identity uses the full canonical source and its prescribed sheet.
It does not replace the upper fiber loop by a disk inside that fiber.

## 1. The actual source and the holomorphic two-form

Let \(v_*\) be the retained logarithm of the simple Alexander root,
and put \(u=v-v_*\). Thus \(v_*\ne0\). The hypotheses and conclusion
of [M] give
\[
 b(v,\xi)=E(u,\rho)+\rho^{-1/2}A(u,\rho),\qquad
 \rho=\xi+S(u),\qquad S(u)=u^2s(u),\quad s(0)\ne0,
 \tag{1}
\]
where \(E,A\) are holomorphic on a full small polydisk and
\(A(u,0)\ne0\). These are the actual canonical functions with
their original normalization. Choose the analytic Morse coordinate
\[
 w=u\sqrt{s(u)},\qquad \tau^2=\xi+w^2,
 \tag{2}
\]
so that the original lift at \(\xi=0\) is \(\tau=w\).
This fixes the sign of \(w\). Its inverse gives a holomorphic
\(v=v(w)\), with \(v(0)=v_*\) and \(v'(0)\ne0\).
Set
\[
 y=\tau-w,\qquad \zeta=\tau+w,
 \qquad \xi=y\zeta,\quad
 w=(\zeta-y)/2,\quad \tau=(\zeta+y)/2.
 \tag{3}
\]

Fix \(L\ge1\) and an observation point \(a\ne0\) outside a
buffered local node neighborhood. In particular this applies to
the physical point \(a=2\pi i\), since the Alexander root is not
\(Y=1\). Choose a bidisk
\[
                  X=\{|y|<d,\ |\zeta|<d\}
 \tag{4}
\]
small enough that (1)--(3) hold on a neighborhood of its closure,
and that \(v(w)\) meets neither \(0\) nor \(a\) there.
For a small nonzero cutoff \(R\), the literal integrand in [K] is
\[
 \Omega_{L,a,R}=
 \frac{L e^{L(R-\xi)/v}}{v(v-a)}b(v,\xi)\,dv\wedge d\xi.
 \tag{5}
\]
On the cover (3) this becomes
\[
 \Omega_{L,a,R}=
 \frac{2L v'(w)e^{L(R-\tau^2+w^2)/v(w)}}
      {v(w)(v(w)-a)}
 \{A(u(w),\tau^2)+\tau E(u(w),\tau^2)\}
                         \,dw\wedge d\tau.
 \tag{6}
\]
Thus the full two-form is holomorphic on \(X\), including
\(\tau=0\). It is closed, and is exact on this contractible bidisk.
The apparent pole of \(b\) has been canceled by the actual Jacobian,
not removed from the source. Formula (6) also retains its even part.

## 2. The original cylinder and its endpoint loops

Choose \(0<\epsilon\ll d\), and then \(0<|R|\ll\epsilon^2\).
Take as the counterclockwise hole contour
\[
                 C:\quad v=v(\epsilon e^{i\phi}),
                         \qquad 0\le\phi\le2\pi.
 \tag{7}
\]
This is a Jordan contour. It can be used directly as a hole boundary
in [K]. Equivalently an initial sufficiently small round contour
can be deformed to it through a buffered collar where the canonical
short-cutoff source is holomorphic. No singularity is crossed.

The actual lifted cylinder \(\Sigma_R\) is
\[
 w=\epsilon e^{i\phi},\qquad \xi=tR,
 \qquad \tau=w\left(1+\frac{tR}{w^2}\right)^{1/2},
                  \quad 0\le t\le1,
 \tag{8}
\]
where the unit square root is near one. Orient it by
\(d\phi\wedge dt\), which is the \(dv\)-then-\(d\xi\) ordering
of the iterated hole integral in [K]. Write \(C_0,C_R\) for its
bottom and top loops, each parametrized by increasing \(\phi\).
The boundary orientation is
\[
                         \partial\Sigma_R=C_0-C_R.
 \tag{9}
\]
The bottom loop lies in the original section \(y=0\),
\(\zeta=2w\), and bounds its holomorphic disk \(B_0\), oriented
so that \(\partial B_0=C_0\).

The top lies in \(\xi=R\). In the fiber coordinate \(q=y\), it is
\[
 q(w)=\tau-w=\frac{R}{\tau+w}
       =\frac{R}{2w}\{1+O(R/\epsilon^2)\},
 \qquad \zeta=R/q.
 \tag{10}
\]
It winds \(-1\) around \(q=0\). It is also a Jordan loop, not
merely an immersed cycle: equality of two nonzero \(q\)-values
implies equality of their
\(w=(R/q-q)/2\). For sufficiently small \(|R|/\epsilon^2\),
the loop lies strictly inside \(|q|=\sqrt{|R|}\) and encloses zero.
Its modulus is bounded above and below by fixed positive multiples
of \(|R|/\epsilon\).

Let \(\Lambda_R\) be the clockwise circle in that fiber,
\[
              q=\sqrt R\,e^{-i\phi},\qquad
              \zeta=\sqrt R\,e^{i\phi}.
 \tag{11}
\]
The choice of \(\sqrt R\) only fixes its parametrization. The
complex-oriented annulus \(A_R\) between the Jordan loop (10)
and this outer circle has
\[
                            \partial A_R=C_R-\Lambda_R.
 \tag{12}
\]
Indeed its outer boundary is counterclockwise and its inner
boundary clockwise, whereas both named loops are clockwise.
Throughout this annulus \(|q|\le\sqrt{|R|}\) and
\(|R/q|\le C\epsilon\). Thus it lies in \(X\) with a fixed buffer
after the preceding choices. The bottom disk and the whole cylinder
also lie there. Since \(B_0\) and \(A_R\) are complex curves,
\[
                         \int_{B_0}\Omega_{L,a,R}
                         =\int_{A_R}\Omega_{L,a,R}=0.
 \tag{13}
\]
This uses the pullback of a holomorphic two-form to a complex
one-dimensional submanifold, not a bound on these integrals.

## 3. The explicit cap and its sign

Define the real disk
\[
 \Delta_R:\quad
 y=\sqrt R\,r e^{-i\phi},\qquad
 \zeta=\sqrt R\,r e^{i\phi},\qquad 0\le r\le1.
 \tag{14}
\]
Use the standard disk orientation, agreeing with
\(dr\wedge d\phi\) for \(r>0\). In Cartesian coordinates
\(x=r\cos\phi,\ t=r\sin\phi\), it is the smooth disk
\[
 \tau=\sqrt R\,x,\qquad w=i\sqrt R\,t,
               \qquad x^2+t^2\le1,
 \tag{15}
\]
oriented by \(dx\wedge dt\). Its boundary is \(\Lambda_R\).
It is contained in \(X\), but its interior does not stay in
\(\xi=R\): it has \(\xi=Rr^2\). Thus the nonbounding loop in
the upper fiber has not been declared null-homologous there.

Equations (9), (12), and (14) give the closed two-chain
\[
                   \Sigma_R-B_0+A_R+\Delta_R.
 \tag{16}
\]
Exactness of (6) on \(X\), followed by (13), proves
\[
                    \int_{\Sigma_R}\Omega_{L,a,R}
                              =-\int_{\Delta_R}\Omega_{L,a,R}.
 \tag{17}
\]
For a direct orientation check, replace the holomorphic coefficient
in (6) by a constant so that the form is \(2A\,dw\wedge d\tau\).
Its cylinder integral is \(2\pi iAR\), whereas on (15)
\(dw\wedge d\tau=-iR\,dx\wedge dt\), and its disk integral is
\(-2\pi iAR\). This agrees with (17).

The actual positively oriented hole term in the color formula is
therefore exactly
\[
 \boxed{\quad
 H_{L,a,R}(C):=
 \frac{e^{-LR/a}}{2\pi i}
          \int_{\Sigma_R}\Omega_{L,a,R}
       =-\frac{e^{-LR/a}}{2\pi i}
          \int_{\Delta_R}\Omega_{L,a,R}.
 \quad}                                                        \tag{18}
\]
There is no change of state gauge, cutoff normalization, or source
branch in this identity. For \(a=2\pi i,L=N,R=ir\), its left side
is precisely the corresponding \(+1\) hole summand in [K, (17)].
The scalar endpoint and all other terms of that formula remain.

The even-source contribution to (18) vanishes locally. On the
cylinder this follows by integrating the holomorphic function
\(E(u,\xi+S(u))\) and the regular kernel around \(C\), for each
\(\xi\in[0,R]\). On the disk it follows equally from (15): all
factors other than the explicit \(\tau=\sqrt R x\) in the even
term of (6) are even in \(x\). Their integral over the symmetric
disk is zero. This is an exact local statement, not a continuation
claim for the global even source.

## 4. The relative class is determined by a fiber winding

Inside the same bidisk put
\[
 X_0=X\cap\{y\zeta=0\},\qquad
 X_R=X\cap\{y\zeta=R\}.
 \tag{19}
\]
The first space is the contractible union of the two coordinate
disks. The second is the annulus
\(|R|/d<|q|<d\), and they are disjoint. Since \(X\) is
contractible, the long exact sequence of the pair gives
\[
 \partial:H_2(X,X_0\cup X_R;\mathbb Z)
                  \xrightarrow{\ \simeq\ }
 H_1(X_R;\mathbb Z)\simeq\mathbb Z.
 \tag{20}
\]
The winding number of the \(q\)-coordinate computes this map.
Both \(C_R\) and \(\Lambda_R\) have winding \(-1\), while
the relative boundary of \(\Sigma_R\) is \(-C_R\).
Consequently
\[
                        [\Sigma_R]=-[\Delta_R]
                 \quad\hbox{in }H_2(X,X_0\cup X_R;\mathbb Z).
 \tag{21}
\]
The explicit chains in (16) realize the same statement. Both
original endpoint fibers are retained in this relative pair.
This supplies an actual class and its integer coefficient; it is
not an assumed surface chosen only to pass through a saddle.

## 5. Projection and the remaining global transport

The cap has a useful exact projection. Equation (15) gives
\[
 S(u(w))=w^2=-Rt^2,
 \quad -1\le t\le1,
 \qquad
 \tau\in\sqrt R[-\sqrt{1-t^2},\sqrt{1-t^2}].
 \tag{22}
\]
Thus its fibers are the finite Gaussian intervals with
\(\tau\)-endpoints \(\pm\sqrt{R+S(u)}\). This agrees with the
local minor formula in [M]. The projection to the \(w\)-plane
is an interval, not an asserted transverse intersection with an
arbitrary observation divisor.

The proof above keeps the observation pole \(v=a\) outside \(X\).
Crossing that pole is not an allowed deformation of (18) without
its residue. Likewise a global transport of this original class
would have to continue the actual form on the swept surface and
transport its boundaries in the fixed fibers \(\xi=0,R\), with
all encountered cut banks and other divisors retained. Continuation
of the odd minor along a regular classical branch, by itself, does
not construct those boundary chains: a fixed transverse minor
endpoint has \(\xi=\rho_0-S(u)\), which generally moves.

The local relative generator in (21) therefore does not assign
a geometric intersection number to the global original cycle.
Nor does it control the retained scalar endpoint in [K]. The
new conclusion is the exact original-hole cap (18), with the
computable relative class (21) and its full endpoint data.

## 6. Complete proof sources

| Label | Complete proof direct | SHA256 |
|---|---|---|
| K | notes/research_canonical_shift_current_cauchy_cycles.md | 4506e2020820221c3f303d2e9a709ccfcbae5f099598b7282e60cc00a8d2ff56 |
| M | notes/research_canonical_borel_regular_square_root_minor.md | 23b1e6cfc5dcb303af37d7470ab262225c1ced3ede9772f183ab813eff94e42a |

K supplies the original hole integrand, its positive coefficient,
and the constructed common short-cutoff source. M supplies the
actual regular minor, original lower sheet, and exact local action.
The chain construction, signs, relative homology, and projection
are proved here. The previous local hole-jump calculation identifies
an observation crossing but does not construct this relative cap.
Only written mathematics and source-text reads were used. No
mathematical programs, tests or builds were run, and frozen notes
and public manuscripts are unchanged.
