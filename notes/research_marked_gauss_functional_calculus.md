# Marked factorial calculus and the original Gauss source normalization

Private written proof, 18 November 2026.

The exact factorial ratio represents the actual finite Gauss operator
on its prescribed physical logarithm germs, including endpoints,
Casimir Jordan blocks, and the whole fixed-root meridian family.
The marking matters. An individual integer logarithm shift can have
a genuine radical meridian pole. A simultaneous shift of both logarithms
is the scalar inverse cyclic Green multiplier, and changes the original
sewn source if the other kernel is held fixed.

This is an exact definition and normalization result. It removes an
ambiguity in replacing a finite polynomial by a special-function
expression. It supplies neither a coherent propagation estimate nor
a contribution of a geometric relative cycle.

## 1. The actual norm relation and its physical logarithms

Use the complete directs B, G, J, and U pinned below. Fix
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 c_0=2\pi i,\quad m\ge2,\quad r=m-1,\quad \mu=\Log M.
 \tag{1}
\]
On G's actual remaining-head space let \(K,E,F,\Omega\) be its
commuting Cartan--Casimir pair and balanced arrows:
\[
 \Omega=FE+qK+q^{-1}K^{-1},\qquad
 K(M)=M^rK_0,\qquad K_0^{2N}=I.
 \tag{2}
\]
G proves the full matrix identity, including all Jordan blocks,
\[
 W_N(K,\Omega):=C_N(\Omega)+K^N+K^{-N}=F^NE^N=0,
 \quad C_N(z+z^{-1})=z^N+z^{-N}.
 \tag{3}
\]
It also proves the literal factorization
\[
 \begin{split}
 A_N&=H_d(M)K^d\,\mathcal S_N(u,v;c),&
 c&=M^{-2}Q,\\
 u+v&=\Omega/(qK),&uv&=1/(QK^2),\\
 T&=\mathcal B_m(W_\tau^{-1})A_ND_{\rm top}\mathscr C_r(M),
 &J_{\rm op}&=D_N(MK)^{-1}T.
 \end{split}\tag{4}
\]
Here \(H_d=\prod_{j=1}^d(MQ^{-j}-M^{-1})\),
\(D_N(z)=(z^N-z^{-N})/(z-z^{-1})\), and the routed factors
and original scalars have exactly G's order. The notation
\(\mathcal S_N(u,v;c)\) means its symmetric polynomial evaluation
in \(K,\Omega\), not a choice of scalar Casimir eigenvalue.
We write \(J_{\rm op}\) for J's opposite kernel to avoid confusing
it with other scalar functions.

Introduce roots \(u,v\) only as local scalar coordinates. Their
symmetric powers satisfy the polynomial identity
\[
 (1-u^N)(1-v^N)=K^{-N}W_N(K,\Omega).
 \tag{5}
\]
Indeed \(u^Nv^N=K^{-2N}\) and
\(u^N+v^N=-K^{-N}C_N(\Omega)\), since \(q^N=-1\).

At \(M=1\), every actual joint eigenvalue of \(K_0,\Omega(1)\)
has \(u^Nv^N=1\) and \((1-u^N)(1-v^N)=0\); hence
\(u^N=v^N=1\). Thus each unordered physical pair is
\[
              \{u,v\}=\{Q^l,Q^k\},\qquad 0\le l,k<N.
 \tag{6}
\]
Only pairs actually present in the joint spectrum are used.
The physical marking is the germ of the logarithms
\[
 u=e^{c_0x},\quad v=e^{c_0y},\qquad x(Q^l)=l/N,\quad y(Q^k)=k/N.
 \tag{7}
\]
These are fixed-\(N\) germs. In particular the germ at \(u=1\)
has \(x=0\), not \(x=1\). Swapping the two roots swaps their
marked logarithms.

## 2. Exact endpoint germs and symmetric descent

Let \(F_N\) denote B's exact marked factorial, and put
\[
 \beta=-2N\mu/c_0,\qquad
 \mathfrak b_N(x,y;\mu)=
 \frac{F_N(N(x+y)+\beta)F_N(\beta)}
 {F_N(Nx+\beta)F_N(Ny+\beta)}.
 \tag{8}
\]
At every pair (6), this is holomorphic on a sufficiently small
\((u,v,\mu)\)-neighborhood with the logarithms (7).
The denominator arguments \(l+\beta,k+\beta\) are in the
zero-free strip \(-1<\Re z<N\). The numerator is holomorphic
also when \(l+k\ge N\), where it may vanish. Thus \(l=0\) or
\(k=0\) presents no fixed-\(N\) obstruction.

There is an elementary local divisibility proof that does not use
an infinite strip contour at those endpoints. B's finite cardinal
identity and the factorial shift give, identically in the other
variable and in \(\mu\),
\[
 \begin{split}
 \mathcal S_N(Q^l,v;c)
     &=\frac{(cv;Q)_l}{(c;Q)_l}
       =\mathfrak b_N(l/N,y;\mu),\\
 \mathcal S_N(u,Q^k;c)
     &=\frac{(cu;Q)_k}{(c;Q)_k}
       =\mathfrak b_N(x,k/N;\mu).
 \end{split}\tag{9}
\]
The equalities include \(l=0,k=0\). Expand the holomorphic
difference at \((Q^l,Q^k)\). Its terms of degree zero in either
variable vanish by (9), so it is divisible by
\((u-Q^l)(v-Q^k)\). Since the other factors of \(1-u^N\) and
\(1-v^N\) are units on the germ, there is a holomorphic function
\(\mathfrak r_N\) such that
\[
 \boxed{\quad
 \mathcal S_N(u,v;c)-\mathfrak b_N(x,y;\mu)
       =(1-u^N)(1-v^N)\mathfrak r_N(u,v;\mu).
 \quad}\tag{10}
\]
On B's fixed interior logarithmic patches this is also its exact
paired strip current divided by the two Fermat factors. At endpoint
germs, (9) proves (10) directly.

Both the difference and its divisor are symmetric. The quotient
is therefore symmetric on the union of the two swapped germs,
first off the divisor and then by holomorphic continuation.
For \(u\ne v\), the unordered roots are local coordinates through
their elementary symmetric functions. At \(u=v=u_0\), write
\(u=u_0+a+t,\ v=u_0+a-t\). A symmetric holomorphic function
has an even convergent power series in \(t\), hence is holomorphic
in \(a,t^2\), which are holomorphic functions of \(u+v,uv\).
This proves descent also at
\[
                         u=v\quad\Longleftrightarrow\quad\Omega=\pm2.
 \tag{11}
\]
No division by \(u-v\) is used for (10) or for this descent.

For clarity, the actual local functional calculus is finite and
unambiguous. On a fixed \(K_0\)-weight space, choose a small Riesz
contour enclosing one root joint Casimir value and all the eigenvalues
that split from it when \(M\) varies. Keep the contour away from the
other root values. Its projector \(P(M)\) is analytic for sufficiently
small fixed-\(N\) \(\mu\). The descended holomorphic functions are
evaluated by their convergent Taylor series on the generalized
eigenspaces, or equivalently by their Cauchy resolvents. This includes
the nilpotent parts. Empty primary spaces contribute zero.

Equations (3),(5),(10) now give the actual identity
\[
 \boxed{\quad
 \mathcal S_N(K(M),\Omega(M);c)\,P(M)
          =\mathfrak b_N(K(M),\Omega(M);\mu)\,P(M).
 \quad}\tag{12}
\]
The notation on the right means the descended marked germ (8).
The finitely many primary projectors sum to the identity, so
these formulas prescribe the full actual Gauss matrix. On overlaps
their values agree because each equals the original polynomial.
This statement is not a claim that arbitrary logarithm decks give
the same representative.

The identity is analytic in the actual meridian family before
differentiation. It therefore keeps every moving-matrix and projector
normal. In particular a derivative of a function of \(\Omega(M)\)
is its Fréchet derivative, with a term
\[
 \frac1{2\pi i}\oint f(\zeta)
    (\zeta-\Omega)^{-1}\Omega'
    (\zeta-\Omega)^{-1}\,d\zeta,
 \tag{13}
\]
as well as explicit parameter derivatives and any moving localizer.
No commutation of \(\Omega'\) with \(\Omega\) is assumed.
The vanishing in (12) is the identity \(W_N(M)=0\) of actual
matrices and its derivatives, not substitution in a large-degree
principal symbol.

## 3. Which channels are units, and which begin in the first normal

The marking gives an exact local description stronger than scalar
node values. On a fixed Cartan weight \(K(M)=M^r\kappa\), put
\(n=l+k\). Since \(uv=1/(QK^2)\), the chosen logarithms satisfy
\[
                   x+y=n/N-2r\mu/c_0.
 \tag{14}
\]
Define the symmetric holomorphic operator unit
\[
 \mathfrak D_{lk}(M)
      =F_N(Nx+\beta)F_N(Ny+\beta)
 \tag{15}
\]
on the localized space. Its scalar eigenvalue at the root is
\(f_lf_k\ne0\), where \(f_j=(Q;Q)_j\). All nilpotent parts are
included in its inverse. Equations (8),(12),(14) give exactly
\[
 \boxed{\quad
 \mathcal S_N(M)P(M)=
 F_N(n-2mN\mu/c_0)F_N(-2N\mu/c_0)
                      \mathfrak D_{lk}(M)^{-1}P(M).
 \quad}\tag{16}
\]
If \(n<N\), the root restriction is the unit
\(f_n\mathfrak D_{lk}(1)^{-1}\). It admits a local analytic
logarithm on the primary block. If \(n\ge N\), the entire
root restriction in (16) is zero, not merely its eigenvalues.
This does not delete that channel: the exact factorial identity
\(F_N(z+N)=(1-e^{c_0z})F_N(z)\) gives
\(F_N'(N+j)=-c_0f_j\), and hence
\[
 \boxed{\quad
 \left.\partial_\mu(\mathcal S_N(M)P(M))\right|_0
       =2mN f_{n-N}\,\mathfrak D_{lk}(1)^{-1}P(1),
                         \qquad n\ge N.
 \quad}\tag{17}
\]
This is nonzero if that primary space is nonzero. It is an exact
operator statement, with no norm or original closed-source lower
bound. The factor \(2mN\) includes the motion of the physical
arguments; holding the Fourier arguments fixed would lose part
of it. The analytic projector was retained in (16) before taking
the derivative.

These upper **primary channels** are distinct from U's upper Fourier
coefficient sector. In U's two-tail degree-\(d\) example the physical
primary labels satisfy \(l+k=d<N\), and the full Gauss root block
is a unit, even though its prescribed upper Fourier normal has an
exponentially large norm. Equation (17) neither removes nor bounds
that Fourier sector separately.

There is an exact common divisor, not only a first-normal formula.
Put
\[
                    \delta_m(M)=1-M^{-2mN}.
 \tag{17a}
\]
For \(n=N+s\), the factorial \(N\)-shift gives
\[
 F_N(n-2mN\mu/c_0)
       =\delta_m(M)F_N(s-2mN\mu/c_0).
 \tag{17b}
\]
The second factor is a holomorphic unit on the primary germ.
Since \(H_d(1)=(-1)^dN\ne0\), inclusion of the prefactor
\(H_dK^d\) in (4) proves that each lower restriction of \(A_N\)
is a holomorphic unit, while every upper restriction is
\(\delta_m\) times a holomorphic unit. Each actual channel has
vanishing order exactly zero or one.

This factorization can be assembled at fixed \(N\). The Cartan
weight projectors are constant, and within each weight the distinct
root Casimir values have disjoint small Riesz contours. Group the
whole cluster splitting from each root value; do not separate a
colliding Jordan pair. The unordered pair (6), and hence \(n=l+k\),
is uniquely determined by that joint root value. Therefore the sum
\(P_{\rm up}(M)\) of the upper primary projectors is holomorphic
near \(M=1\), after reducing the meridian neighborhood if needed.
It commutes with \(A_N(M)\), and the complementary primary sum is
\(I-P_{\rm up}\). Define
\[
 \mathfrak G_N
   =A_N(I-P_{\rm up})+\delta_m^{-1}A_NP_{\rm up}.
 \tag{17c}
\]
Equation (17b) gives the holomorphic continuation of the second
term. Each primary restriction of \(\mathfrak G_N\) is a unit,
so \(\mathfrak G_N\) is a holomorphic invertible matrix and
\[
 \boxed{\quad
 A_N=\mathfrak G_N\bigl[(I-P_{\rm up})+\delta_mP_{\rm up}\bigr].
 \quad}\tag{17d}
\]
This is a reduced finite-dimensional primary resolution, not a lift
of \(P_{\rm up}\) to an original total-intertwiner projector.
Its contour widths and conditioning may depend on \(N\).
All the routed factors on both sides of \(A_N\) in (4) remain
attached to this factorization.

On compact lower angle patches, B additionally gives the scalar
logarithm \(N^{-1}\log\mathfrak b_N=\Phi+O((\log N)/N)\) and
its scalar unit amplitude. This does not estimate the physical
Riesz projector or its coherent kernel. At time zero a localized
operator evolution has kernel \(P\), not the identity.
Endpoint germs can shrink with \(N\), and the upper channels in
(17) cannot be included in a holomorphic logarithm of the root
matrix.

## 4. Exact logarithm decks and the cyclic Green scalar

Now continue the marked factorial expression itself, keeping the
scalar arguments \(u,v\) fixed while shifting a logarithm. Put
\[
 \rho=M^{-2N},\qquad \alpha=u^N,\quad \zeta=v^N,\qquad
 k_N=\alpha\zeta=K^{-2N}.
 \tag{18}
\]
The letter \(\zeta\) here denotes a power of \(v\), not a contour
coordinate. From the factorial \(N\)-shift,
\[
 \begin{split}
 \mathfrak b_N(x+1,y)&=\tau_x\mathfrak b_N(x,y),&
 \tau_x&=\frac{1-\rho\alpha\zeta}{1-\rho\alpha},\\
 \mathfrak b_N(x,y+1)&=\tau_y\mathfrak b_N(x,y),&
 \tau_y&=\frac{1-\rho\alpha\zeta}{1-\rho\zeta}.
 \end{split}\tag{19}
\]
These are meromorphic identities; omitted denominators are not
declared units at \(M=1\).

On the actual norm quotient, (5) says
\(\alpha+\zeta=1+k_N\). Consequently
\[
 \tau_x=\frac{1-\rho\zeta}{1-\rho},\qquad
 \tau_y=\frac{1-\rho\alpha}{1-\rho},\qquad
 \tau_x\tau_y=\frac{1-\rho k_N}{1-\rho}.
 \tag{20}
\]
For example multiply \(1-\rho\alpha\) by \(1-\rho\zeta\)
to get \((1-\rho)(1-\rho k_N)\); this proves (20)
generically and then meromorphically, including Jordan blocks.
The individual formulas use an ordered nonramified root pair.
Their product is symmetric and requires no such choice.

Since \(K^{2N}=M^{2rN}I\), the simultaneous deck is the scalar
\[
 \boxed{\quad
 d_{{\rm deck},N}(M)=\tau_x\tau_y
     =\frac{1-M^{-2mN}}{1-M^{-2N}}
     =\sum_{a=0}^{m-1}M^{-2aN}
     =\mathcal R_N(M)^{-1}.
 \quad}\tag{21}
\]
Here \(\mathcal R_N\) is exactly G's finite cyclic transport
multiplier, not a newly chosen normalizer. In particular
\[
 d_{{\rm deck},N}(1)=m,\qquad
 \left.\partial_\mu d_{{\rm deck},N}(e^\mu)\right|_0
                              =-Nm(m-1).
 \tag{22}
\]
It is a holomorphic unit on a sufficiently small scaled meridian
disk. This notation is distinct from \(D_N(M)/N\), which occurs
in the turnover and other source frames.

The individual decks can have genuine operator poles. At the root,
on an ordered local cover, write
\(\alpha(0)=I+R\). Equation (5) gives
\(\zeta(0)=I-R\) and \(R^2=0\). Expanding (20) yields
\[
                  \operatorname*{Res}_{\mu=0}\tau_x
                       =R/(2N),\qquad
                  \operatorname*{Res}_{\mu=0}\tau_y
                       =-R/(2N).
 \tag{23}
\]
On a double Casimir block with root value
\(\lambda=z_0+z_0^{-1}\), \(\Delta=z_0-z_0^{-1}\ne0\), choose
\(u=(qKz)^{-1}\). For \(L=\Omega-\lambda I\), \(L^2=0\),
the logarithmic derivative of \(u^N\) with respect to \(\Omega\)
is \(-N/\Delta\). Thus
\[
 R=-\frac N\Delta L,\qquad
 \operatorname*{Res}\tau_x=-\frac{L}{2\Delta},\qquad
 \operatorname*{Res}\tau_y=\frac{L}{2\Delta}.
 \tag{24}
\]
These are nonzero when the Casimir block is genuinely Jordan.
Such blocks occur in the actual source: U proves, for every even
\(N=2p\), on the two-tail degree-\(d\) block with \(K=1\),
that the nodes \(2\cos((2j+1)\pi/N)\), \(0\le j<p\), have
actual columns \(v_j,v'_j\) with
\((\Omega-\lambda_j)v'_j=v_j\ne0\). Their \(\Delta\)'s are
nonzero. Their physical pair has \(l+k=d<N\), so (16) is
a root unit there; an individual shifted Gauss expression has
a genuine pole on these blocks as well.

The scalar branchwise limits \(m\) and \(1\) on the two split
components therefore do not define a regular individual operator
transition through a Jordan collision. At \(\Omega=\pm2\), the
unordered functional identity in Section 2 remains valid, but an
individual deck is not claimed to descend across the ramification.
The simultaneous scalar (21) does descend.

## 5. The original closing source changes if a deck is dropped

For the same actual braid word \(W\) and its reflected reduced word
\(B_-\), J proves the sewn expression with its original cut, pivot,
framing line, and finite coherent resolutions,
\[
 \Phi_0(W(M))=
 \frac{D_N(M)}{a_N(M)}
 \operatorname{Tr}\!\left(
 J_{\rm op}(M)B_-(M^{-1})J_{\rm op}(M^{-1})\right),
 \tag{25}
\]
where
\[
 \gamma_N(M)=(-1)^dD_N(M)/N,\qquad
 a_N(M)=(-1)^dN\gamma_N(M)^m.
 \tag{26}
\]
The full trace is analytically continued from its punctured meridian
expression as prescribed by the original source.

Make the simultaneous logarithm shift in the left Gauss factor
of (4), on its marked primary germs, and hold every other factor,
in particular the right reflected kernel in (25), fixed.
Equations (20)--(21) give exactly
\[
 A_N^{\rm deck}=d_{{\rm deck},N}A_N,\qquad
 T^{\rm deck}=d_{{\rm deck},N}T,\qquad
 J_{\rm op}^{\rm deck}=d_{{\rm deck},N}J_{\rm op}.
 \tag{27}
\]
These identities hold after summing the physical primary spaces,
because the multiplier is the same scalar on every one. Therefore
the modified sewn expression is
\[
 \boxed{\quad
 \Phi_0^{\rm deck}(W(M))
           =d_{{\rm deck},N}(M)\Phi_0(W(M)).
 \quad}\tag{28}
\]
In particular its root value is \(m\Phi_0(W(1))\), and its
first \(\mu\)-normal is
\[
 m\,\partial_\mu\Phi_0(W)|_0
                 -Nm(m-1)\Phi_0(W(1)).
 \tag{29}
\]
This is an equality of source expressions, not a claim that a given
source value is nonzero. It shows precisely why an untracked deck
choice is not a source-preserving normalization.

The same scalar multiplication holds before integration in J's
three-kernel compact period. All occupation caps, factorial duals,
Cartan twists, and meridian finite parts remain. An inverse scalar
on another leg could compensate it, but that would be an explicit
additional source transformation, not omission of (21).
For individual decks the nonscalar meromorphic transitions and
their residues (23) must instead remain in their actual order.
On a relative window with polar terms, the finite part uses the
entire product with \(d_{{\rm deck},N}(M)\); it cannot in general
be replaced by \(m\) times that window's finite part.

## 6. What is defined, and what is still not estimated

The original finite polynomial is now exactly represented by the
factorial germs with labels \(0,\ldots,d\), including every root
endpoint and normal channel. This equality survives arbitrary
ordered outer matrices and windows when the same primary resolution
is retained. It does not identify a shifted logarithm germ with that
same physical definition: (19)--(29) record the difference.

This establishes the marked local functional calculus, its unit and
first-normal channels, and the concrete deck effect on the original
source. No estimate of the primary projectors, their Fréchet normals,
or the resulting coherent kernel has been supplied. In particular
an analytic scalar logarithm is not an actual near-identity coherent
evolution, and scalar nonvanishing in B is not a matrix norm estimate.
Transporting these marked germs along a geometric contour still
requires the actual logarithm transitions, endpoint channels, and
relative-window currents. No intersection coefficient or knot
noncancellation conclusion is asserted.

## Complete proof directs

* B: notes/research_balanced_gauss_global_cardinal_strip.md,
  SHA256 bde4e38cb64477d13a558000545e53fc81413f2fcfe82f80562ce3691d8a19ca.
* G: notes/research_opposite_kernel_forced_cyclic_normalization.md,
  SHA256 42e6d6c3a5039859c241a2832de56301eff49d749db86d67868f3534c89aaaaa.
* J: notes/research_opposite_polarization_source_kernel.md,
  SHA256 d52c6dd8e62f575a262fc7af460e258f7cb0e40b5a9c037ac46dd8d151002d44.
* U: notes/research_actual_upper_gauss_carry_conditioning.md,
  SHA256 19d9942be54c4dcde7209b332d70ca3ce19b888b20d60480ae74f6ac1e9af4c3.

The entire final and all four complete directs were read nontruncated
in this author sequence; every used implication and all matching pins
were checked. Only written mathematics and text/hash operations were
used. Frozen and public files were not edited.
