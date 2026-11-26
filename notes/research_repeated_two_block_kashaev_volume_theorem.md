# The original capped list (2,4,2,3): sharp Kashaev asymptotic and volume

Private research theorem, 8 November 2026. This is an assembly of the
proved complete finite-source asymptotic, positive complete gluing,
and relative rational-tangle identification. No numerical evaluation,
subdivision replay, or new saved-data computation is used.

## 1. The fixed original knot and invariant

Let \(R\) be the original positive two-strand crossing, \(T\) the
physical clockwise quarter-turn with its recorded four endpoint
labels, and \(C\) the original cylindrical closure. Fix the diagram
\[
 \mathcal K=C\!\left(R^2T\!\left(R^4T\!\left(R^2T(R^3)\right)\right)\right).
 \tag{1}
\]
This is the literal positive capped list \((2,4,2,3)\), not a
replacement observation of another tangle. The endpoint and fraction
calculation in
[the repeated-block source, Section 5](research_repeated_reflected_block_positive_moments.md)
proves that it has one component and original fraction \(29/17\).

Write \(K_N(\mathcal K)\) for the reduced zero-framed Kashaev
invariant at quantum parameter \(Q=e^{2\pi i/N}\), with unknot
value one. There is exactly one reduced cut. The matrix convention
uses its fixed square root
\[
       q=e^{\pi i/N},\qquad D=N-1,\qquad
       \kappa=q^{D^2/2},\qquad q^s=e^{\pi i s/N}.
 \tag{2}
\]

**Theorem.** The knot (1) is hyperbolic. There are constants
\(\mathfrak s>0\) and \(\mathcal D_*>0\), specified below, such that
\[
 \boxed{\quad
 |K_N(\mathcal K)|
   =N^{3/2}\mathcal D_*e^{2N\mathfrak s}
                          (1+O(N^{-1})).
 \quad}
 \tag{3}
\]
The asymptotic and the following limit hold through all integer
levels, with no parity restriction:
\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(\mathcal K)|
       =4\pi\mathfrak s
       =\operatorname{Vol}(S^3\setminus\mathcal K).
 \quad}
 \tag{4}
\]
For every \(N\ge3\) the invariant is nonzero, by the exact positive
pairing below; its zero-framing phase is retained in (7).

## 2. The original finite scalar and its normalization

Let \(M_N\) be multiplication by the actual crossing in the full
normalized Newton basis, let \(\mathsf J_N\) reverse that basis,
and let \(\phi_N=\mathbf e_D^T\) be its original cylindrical
closing row. The finite turn and closing formulas are
Proposition “Newton turn and closure” and equations
\(\mathrm{eq:phi\text{-}physical}\),
\(\mathrm{eq:newton\text{-}turn}\) of
[the original Newton-tangle calculus](../papers/newton-tangles/main.tex).
They include the true reduced cut and its factor \(1/N\) before
the basis calculation. In this basis \(\phi_N\) is exactly a
coordinate row; no further dimension or \(N\) factor is to be
inserted.

Define
\[
 \begin{split}
 K_{2,N}&=(M_N^2)^*M_N^2,\qquad
       \beta_N=K_{2,N}\mathbf e_0,\\
 Z_{2,2,N}
   &=\phi_N\!\left(
           M_N^2\mathsf J_N M_N^4\mathsf J_N
                 M_N^2\mathsf J_N M_N^3\mathbf e_0\right),\\
 \mu_{2,N}&=\|\beta_N\|_2^2
             =\mathbf e_0^*K_{2,N}^{\,2}\mathbf e_0.
 \end{split}
 \tag{5}
\]
The exact full-matrix identity in
[the repeated-block theorem, equations (2)--(7)](research_repeated_reflected_block_positive_moments.md)
is
\[
                   Z_{2,2,N}=\kappa^3\mu_{2,N},
                \qquad \mu_{2,N}>0,\qquad N\ge2.
 \tag{6}
\]
The powers, original cap and closing row in (5) are literal.
Invertibility of \(M_N\) proves the strict positivity in (6).
It is not obtained by removing phases from the individual terms
of a different state sum.

For the original oriented blackboard diagram \(\mathscr D\) in
(1), let \(w(\mathscr D)\) be its actual writhe. The original
normalization theorem, Theorem 10.1 and equations
\(\mathrm{de:enhanced\text{-}comparison}\),
\(\mathrm{de:raw\text{-}invariant}\) in
[Finite spectral evaluation and uniform filling bounds](../papers/filling-bounds/sections/diagram-evaluation.tex),
gives, for \(N\ge3\),
\[
 \begin{split}
 K_N(\mathcal K)
   &=\zeta_{N,\mathscr D}Z_{2,2,N}
     =\zeta_{N,\mathscr D}\kappa^3\mu_{2,N},\\
 \zeta_{N,\mathscr D}
   &=\theta^{-w(\mathscr D)},\qquad
       \theta=q^{-D^2/2}=\kappa^{-1},\qquad
       |\zeta_{N,\mathscr D}|=1.
 \end{split}
 \tag{7}
\]
The same curl factor is derived in equation
\(\mathrm{mt:twist}\) of
[the physical meridian-tangle calculus](../papers/meridian-tangles/main.tex).
If one starts with another specified ribbon framing, use its
recorded integer correction in (7). In particular the writhe is
not inferred from the sum of the four unoriented crossing powers.
The component sign of the enhanced comparison is one because (1)
is a knot.

Thus \(|K_N(\mathcal K)|=\mu_{2,N}\) exactly at these levels.
There is no unmentioned polynomial factor, quantum dimension,
ordinary trace, or extra auxiliary-circle normalization. The
source identity (6) also holds at \(N=2\); the normalization
statement (7) on \(N\ge3\) already suffices for the all-level
limit (4).

## 3. The complete positive moment and its fixed action

Use the original logarithmic primitive
\[
 J(z)=\int_0^z\operatorname{Log}(2\sin\pi s)\,ds,\qquad
 F(x,t)=J(x+t)-3J(x)+i\pi tx .
 \tag{8}
\]
The branch is continued from the real interval \((0,1)\).
Let \(x(t)\) be the selected solution of \(F_x=0\) with
\(x(0)=1/6\), and put
\[
 \Phi(t)=F(x(t),t),\qquad
 \mathcal S(t)=\Re\Phi(t)-2J(t),\qquad
 \mathfrak s=\mathcal S(t_*).
 \tag{9}
\]
Sections 1--6 of
[the complete half-interval packet](research_repeated_two_block_half_interval_packet.md)
prove that \(\mathcal S\) has a unique nondegenerate maximum
\(t_*\in(0,1/4)\). They estimate every actual coefficient of
\(\beta_N\), including both physical endpoints and the entire
upper half. Their finite contour argument keeps all aliases and
connectors and both level parities. In particular its equation
(43) is the full original norm asymptotic
\[
 \mu_{2,N}=N^{3/2}\mathcal D_*e^{2N\mathfrak s}
                         (1+O(N^{-1})),
 \qquad
 \mathcal D_*=
 \left|\frac{A(t_*)}{2\sin\pi t_*}\right|^2
            \sqrt{\frac{\pi}{-\mathcal S''(t_*)}}>0,
 \tag{10}
\]
where the original nonzero Gaussian symbol is
\[
 A(t)=\sqrt{\frac{\pi}{2}}\,
      \sqrt{\frac{\sin\pi(x(t)+t)}{\sin^3\pi x(t)}}\,
                \frac1{\sqrt{-F_{xx}(x(t),t)}}.
 \tag{11}
\]
The roots in (11) have the continued choices fixed by that
source theorem. Equations (7) and (10) prove (3), including
the \(N^{3/2}\) prefactor.

Set
\[
 u=e^{2\pi ix(t_*)},\quad p=e^{2\pi it_*},\quad
 w=u(1-u),\quad V=\frac{u^3(1-u)}{(1-u+u^2)^2}.
 \tag{12}
\]
The source equation and maximum condition give
\[
 u^2p-u=(1-u)^3,\qquad |p|=|V|=1.
 \tag{13}
\]
For the single-valued Bloch--Wigner function \(\mathcal D\),
the absolutely calibrated action identity in equation (49)
of the same packet is
\[
       2\pi\mathfrak s
       =3\mathcal D(u)+2\mathcal D(p)-\mathcal D(pu).
 \tag{14}
\]
Its constant is fixed by the exact primitive
\[
 J(z)=\frac{i}{2\pi}\operatorname{Li}_2(e^{2\pi iz})
            +\frac{i\pi}{2}(z-z^2)-\frac{i\pi}{12}.
 \tag{15}
\]
The zero lift of \(F_x\) supplies the logarithmic correction in
(14). No uncalibrated choice of a volume potential is used.

## 4. Complete geometry of the same exterior

The five positive shapes in
[the original layer dictionary](research_repeated_two_block_five_shape_layer_dictionary.md)
are \(u,u,w,w,-V\), and its exact regulator identity is
\[
 2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)
       =3\mathcal D(u)+2\mathcal D(p)-\mathcal D(pu).
 \tag{16}
\]
[The five-core face theorem](research_repeated_two_block_five_core_faces.md)
constructs the literal doubled ten-cell manifold
\(\mathcal M_{\rm dbl}\). It verifies every face and edge,
the single torus link, all positive angle lifts \(2\pi\),
and a nonidentity parabolic peripheral loop. The resulting
translation cusp is complete. Consequently
\[
 \operatorname{Vol}(\mathcal M_{\rm dbl})
      =2\{2\mathcal D(u)+2\mathcal D(w)+\mathcal D(-V)\}
      =4\pi\mathfrak s.
 \tag{17}
\]
The equality is the volume of a complete positive metric, not
just a formal Bloch sum.

The new
[core boundary-word theorem](research_repeated_two_block_core_boundary_word.md)
identifies \(\mathcal M_{\rm dbl}\) with the exterior of (1),
allowing orientation reversal. Its proof uses the actual handle
cancellations, all four free boundary meridians, the separating
cap disk and primitive annuli. The closing map's half-lattice
translation is absorbed by an automorphism which extends over
the proved rational core. Thus this step is not inferred from
the critical polynomial, a cap trace, or a slope alone.

Transporting the complete metric gives hyperbolicity of
\(S^3\setminus\mathcal K\), with the same positive volume.
Equations (7), (10), and (17) now prove (4). No preferred
longitude is needed for this unmarked volume identification;
the quantum framing has already been corrected independently
in (7).

This theorem concerns the fixed original capped example (1).
The positive higher moments of the repeated-block operator do
not by themselves give sharp rates or geometric identifications
for its longer words. No such family extension, ordinary-color
transfer theorem, or general finite-exceptions conclusion is
asserted here.
