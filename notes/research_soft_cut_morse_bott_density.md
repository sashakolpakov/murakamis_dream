# The literal soft-cut Morse–Bott one-form

Private written proof, 18 November 2026.

The actual complex-binomial braid source has a nonzero leading
one-form on its remaining complete geometric framing curve. With
the original factorial and Gaussian square-root marks retained, that
form is a representation-dependent constant times \(dr/s\). This is
an amplitude calculation, including the finite \(N-1\) cut correction;
it is not an inference from the principal centralizer vector field.

The complete positive gluing certificate remains an explicit
hypothesis. No relative framing period or physical cycle coefficient
is calculated here. The older two-form/torsion comparison is used in
its stated regularity range, and that range is checked below.

## 1. Source, coordinates, and the one-form being computed

Let the fixed knot braid have \(b\) strands and \(c\) crossings, with

\[
 m=c+1,\qquad c_0=2\pi i,\qquad h=c_0/N.
 \tag{1}
\]

Use the actual integral chord coordinates and logarithmic occupations
\(\zeta=c_0x\) of H and F. The unweighted logarithmic phase is
\(S_0\), including the original pivotal and framing terms. Use the
full correcting integer Fourier covector, including the cut entry.
For a complex cut parameter \(\theta\) near \(1/2\), write

\[
 \Phi_\theta=S_0-c_0 n\cdot\zeta+g_\theta(u),\qquad
 g_\theta(u)=c_0 b_\theta(u/c_0),
 \tag{2}
\]
\[
 b_\theta(t)=-t\log t-(1-t)\log(1-t)
               +t\log\theta+(1-t)\log(1-\theta).
\]

All logarithms are the compatible original ones. The geometric
critical curve has

\[
 u=u_\theta=c_0\theta,\qquad
 s=s_\theta=e^{-c_0\theta}-1\ne0,
 \tag{3}
\]

and its remaining coordinate is \(r\). H proves that the Hessian
in the actual \(m\) occupation coordinates has rank \(c\). These
coordinates have already removed the common momentum; no further
phase variable is quotiented here.

Separate only the explicitly supplied occupation-independent factors
of the literal source, such as its common Cartan scalars and any
external modified-dimension line. Denote their unchanged product by
\(E_N\). In equations (4) and (20), the phase is the phase of the
quotient by \(E_N\): a constant exponential contained in \(E_N\)
is not counted a second time in \(\Phi_\theta\). Equivalently one
may restore that same constant term to the phase and remove its
factor from \(E_N\). Neither convention changes any Hessian below.
The line is never set to one or replaced by an unspecified
normalization. In particular this convention does not
retain an extra old cut average \(1/N\): the binomial weight multiplies
the unnormalized diagonal partial-trace summand.

In the variable-amplitude convention of D and Q, let
\(a_{\rm lit}(\zeta)\) be the leading crossing/pivot amplitude of
the actual factorial section A, after this separation. F gives

\[
 E_N^{-1}I_N(Nx)=N^{-m/2}a_{\rm lit}(c_0x)
 B_\theta(u/c_0)e^{\Phi_\theta(c_0x)/h}(1+O(N^{-1})),
 \tag{4}
\]
\[
 B_\theta(t)=\frac{1-t}{(1-\theta)\sqrt{2\pi t(1-t)}}.
 \tag{5}
\]

The Fourier character in (4) is included in \(I_N\) for this formula.
All fixed derivatives of the error are uniform on smaller regular
slit charts. In F's complete Fourier expansion the selected integral
has coefficient one; its relative boundary currents are unchanged.

Choose local coordinates \((r,y_1,\ldots,y_c)\) with critical curve
\(y=0\), and write
\(d\zeta_1\wedge\cdots\wedge d\zeta_m=J(r,y)\,dr\wedge dy\).
The logarithmic Gaussian one-form is, by definition,

\[
 \omega_\theta=
 \left.
 \frac{a_{\rm lit} B_\theta J}
      {\sqrt{\det(-\partial_y^2\Phi_\theta)}}
 \right|_{y=0}dr.
 \tag{6}
\]

The square root belongs to the transported normal Gaussian orientation
line. Under a normal coordinate change the Hessian determinant gains
the square of the normal Jacobian, so (6) is independent of that
choice with its orientation line retained.

Let \(\mathcal T_\beta\) be Q's actual holonomy torsion, with its
specified ordered bases. Then the result is

\[
 \boxed{\quad
 \omega_\theta^2=
 i^{\,1-c}(-1)^b\frac{\mathcal T_\beta}{2}
                   \left(\frac{dr}{s_\theta}\right)^2.
 \quad}
 \tag{7}
\]

The square does not choose a fresh sign. The actual factorial marks
and one oriented normal Gaussian fix the nonzero constant in (6).

## 2. The fixed-trace regularity needed for the torsion comparison

For completeness, the fixed-trace premise in Q follows here from
H's exact fixed-eigencharacter rigidity; it is not inferred merely
by differentiating the trace function at a parabolic.

At a noncentral complete meridian \(\mu\), let its retained eigenvalue
be \(\varepsilon=\pm1\). On every local Artin deformation with
\(\operatorname{tr}\mu=2\varepsilon\) and \(\det\mu=1\),

\[
                 \det(\mu-\varepsilon I)=0.
 \tag{8}
\]

A fixed nonzero entry of the original rank-one matrix
\(\mu-\varepsilon I\) stays a unit. Eliminating with that entry
shows that its kernel is a unique free rank-one direct summand.
It is the exact eigenline for eigenvalue \(\varepsilon\), not an
arbitrary invariant line with a nilpotently varying eigencharacter.
Commuting peripheral matrices preserve this kernel. Thus the
unaugmented fixed-trace deformation carries a canonical decoration
of precisely the kind used in H's rigidity argument.

H's positive-certificate comparison makes the decorated fixed-meridian
quotient a point over these Artin rings. Conversely forgetting the
canonical exact eigenline recovers the same fixed-trace deformation.
Hence the kernel of the linearized braid fixed-point map consists
exactly of simultaneous conjugation directions.

In Q's notation the actual holonomy complex is therefore acyclic:

\[
 0\longrightarrow\mathfrak{sl}_2\mathop{\longrightarrow}^{A}V
 \mathop{\longrightarrow}^{D=dF-I}V
 \mathop{\longrightarrow}^{M}\mathfrak{sl}_2\longrightarrow0.
 \tag{9}
\]

Here \(A\) is injective by irreducibility. Surjectivity of \(M\)
can also be checked directly: an element annihilating the product
differential under the trace pairing commutes successively with
every meridian, and is zero. Rank-nullity then proves exactness.
The torsion \(\mathcal T_\beta\) is nonzero and independent of the
framing point. The latter follows either from Q's determinant ratio
or from applying the same simultaneous conjugation to its two
middle bases and the same adjoint map to its endpoint bases.

Thus Q's comparison is applicable to this actual source. It is not
an additional acyclicity assumption on an unrelated presentation.

## 3. The literal subprincipal crossing factors

This step is needed because the chosen root-factorial section has
a definite phase and \(N^{1/2}\) normalization. One must not insert
only its leading dilogarithm into a torsion formula.

At complete color put \(A=e^a,B=e^b,C=e^v\) for one crossing's
two input log occupations and transfer. A proves that the squared
single-factor amplitude is \(i(1-e^z)\). Its positive five-factor
ratio therefore has squared amplitude

\[
 \frac1i\frac{(1-BC)(1-A)}{(1-B)(1-C)(1-A/C)}.
 \tag{10}
\]

After retaining its common Cartan scalar, the exact monomial in A
contributes \(AB/C\) to that squared amplitude: the half-step in
\(x=-q^{-1}\) gives \(AB\), and its last transfer factor gives
\(C^{-1}\). Since

\[
 \frac{1-A}{1-A/C}
                  =C\frac{1-1/A}{1-C/A},
 \tag{11}
\]

the literal positive amplitude is

\[
 a_{{\rm lit},+}^2=i^{-1}
 AB\frac{(1-BC)(1-1/A)}{(1-B)(1-C)(1-C/A)}
                         =i^{-1}a_+^2.
 \tag{12}
\]

For the negative crossing the exact monomial has squared
subprincipal factor \(1/(AB)\): its \(q^n\) and last transfer
half-step cancel. Applying (11) with \(B\) in place of \(A\) gives

\[
 a_{{\rm lit},-}^2=i^{-1}
 \frac C{AB}\frac{(1-AC)(1-1/B)}
                       {(1-A)(1-C)(1-C/B)}
                         =i^{-1}a_-^2.
 \tag{13}
\]

The quantities \(a_\pm\) are exactly D's balanced principal
amplitudes, not amplitudes of a coherent transform. D proves
their mixed-Hessian/momentum factorization, including both signs.
Multiplying it through the actual word cancels internal momenta
and retains the original pivotal multiplier. Consequently

\[
                          a_{\rm lit}^2=i^{-c}a_\beta^2.
 \tag{14}
\]

The phases have the same Hessian. To check the reciprocal-factorial
convention explicitly, the positive literal monomial has quadratic
part \(ab-bv+\pi i(v-a-b)\). Inverting its reflected factorial
pair adds \(av-v^2/2-\pi iv\), giving
\(ab+(a-b)v-v^2/2-\pi i(a+b)\), the balanced phase.
Negatively the corresponding two parts are
\(-ab-bv+v^2/2+\pi i(a+b)\) and
\(bv-v^2/2-\pi iv\), giving \(-ab+\pi i(a+b-v)\).
The continued dilogarithm inversion identity follows by
differentiation; its integration constant is independent of the
occupations. Other compatible branch marks add their recorded
affine Fourier characters and constants. They do not change the
Hessian used here. No root phase is replaced by its modulus.

## 4. The unweighted two-form and the additional binomial Gaussian

Before adding \(g_\theta\), the actual phase has its two framing
directions. The incidence adapter in H applies with \(g=0\), and
the same rigidity argument above gives precisely this smooth
two-dimensional critical germ. Its complete-color coordinates are

\[
 F(r,s)=\begin{pmatrix}r&1-r\\s&-s\end{pmatrix},\qquad
 u=-\Log(1+s),\qquad
 \Omega_{\rm cut}=-\frac{dr\wedge ds}{s(1+s)}
                         =\frac{dr\wedge du}{s}.
 \tag{15}
\]

Q proves, with the actual kernel/cokernel identification and
original lattice cofactor, that its raw variable Gaussian two-form
obeys

\[
       \Omega_{\rm raw}^2=(-1)^b\frac{\mathcal T_\beta}{2}
                                      \Omega_{\rm cut}^2.
 \tag{16}
\]

In particular this is the raw parity convention, not Q's separately
parity-normalized square. Combining (14) and (16), the two-form
from the literal factorial section is a marked constant times
\(dr\wedge du/s\), with squared constant
\(i^{-c}(-1)^b\mathcal T_\beta/2\).

Choose \((r,u,y)\) as local coordinates before the binomial insertion,
with \(y\) transverse to the two-dimensional critical surface and
\(u\) the actual cut coordinate. The symmetric normal Hessian is
invertible. Taylor expansion followed by its holomorphic symmetric
matrix square root puts the unweighted phase into a quadratic
normal form while keeping \(r,u\) fixed. Adding \(g_\theta(u)\)
therefore adds one independent normal Gaussian. This proves the
iterated Gaussian determinant formula here directly; no nonzero
normal or tangential Jacobian is suppressed.

The two needed scalar values are

\[
 B_\theta(\theta)^2=\frac1{2\pi\theta(1-\theta)},\qquad
 g_\theta''(u_\theta)=-\frac1{c_0\theta(1-\theta)}.
 \tag{17}
\]

Their quotient is

\[
             \frac{B_\theta(\theta)^2}{-g_\theta''(u_\theta)}
                              =\frac{c_0}{2\pi}=i.
 \tag{18}
\]

The factor \((1-t)/(1-\theta)\) in (5) is the actual \(N-1\)
correction; at this particular stationary value it is one. The
calculation retains it before evaluation, including its derivatives.
Equations (14), (16), and (18) prove (7).

## 5. Transport, original normalization, and retained currents

On a connected marked chart, define \(C_\beta\) by

\[
 \omega_\theta=C_\beta\frac{dr}{s_\theta},\qquad
 C_\beta^2=i^{1-c}(-1)^b\mathcal T_\beta/2\ne0.
 \tag{19}
\]

Since the square is independent of \(r\), differentiating it proves
\(\partial_r C_\beta=0\). Thus the leading actual one-form is
invariant under \(s_\theta\partial_r\). Its constant remains on
the original factorial/Gaussian orientation line; independently
changing a square-root sign is not the same marked continuation.
There are no additional finite-\(r\) poles on this regular source
fiber. Boundary degenerations or a changing representation can
still affect the torsion and its domain.

For clarity, the original scalar normalization can be restored
without choosing it from the torsion. The measure in a Fourier
integral is \(N^m dx=c_0^{-m}N^m d\zeta\). Formal integration of
only its \(c\) normal variables therefore has leading one-form

\[
 E_N N^{1/2}(2\pi)^{c/2}c_0^{c/2-m}
                 e^{\Phi_\theta(\zeta_*)/h}\omega_\theta.
 \tag{20}
\]

All powers in (20) use the same normal orientation. A different
explicit external normalization multiplies \(E_N\) by precisely
that whole factor. It does not alter (19). Uniformity with a
relative \(O(N^{-1})\) error on compact \(r\)-charts follows from
A/F's derivative bounds and H's holomorphic normal form: on a
small descending normal ball the Gaussian tail is exponentially
small, odd Taylor terms integrate to zero, and the first remaining
Taylor terms have order \(h\). This constructs a local normal
integral, not a deformation of the original global chain to it.

The weighted Ward source has not been replaced by an invariant
trace. Put \(P_\theta\) equal to the actual binomial cut tensor
the original pivots. For every one of its ordered weighted Ward
terms, and every marked word \(O\), finite matrix cyclicity gives
the exact identity

\[
 \operatorname{Tr}(P_\theta[X,A B]O)
  =\operatorname{Tr}([P_\theta,X]A B O)
                  +\operatorname{Tr}(P_\theta A B[O,X]).
 \tag{21}
\]

Summing (21), with the actual weights and any prescribed factor
\(1/h\), retains all cut, pivotal and marked-word currents. Nothing
in (12)--(20) sets either term on its right to zero. The leading
invariance in (19) was obtained from the actual subprincipal
amplitude and determinant, not by discarding those currents.
An additional observable with leading symbol \(o(r)\), when its
same local expansion is justified, multiplies (19) by \(o(r)\);
no invariance or absence of poles is asserted for arbitrary marks.

Finally, on the affine fiber (19) has primitive
\(C_\beta r/s_\theta\). Compact closed loops have zero leading
period. A specified finite-endpoint relative chain would pair as
\(C_\beta/s_\theta\) times its signed endpoint sum, but the original
chain's transverse pushforward and any infinity regularization
remain unproved here. The one-form does not supply their values.

## Complete proof-source pins

* A: notes/research_literal_crossing_slit_chart_amplitude.md,
  SHA256 c3682b0f84000aad4c2f53235b9c93bbd86283905a75d6f07ac03b1a3c00bc4a.
* D: notes/actual_cut_residue_and_principal_density.md,
  SHA256 31ae47377d3fff90f177020e18ab1394866facdf9b783aa7823b52d2cebd0bda.
* Q: notes/quantum_source_bridge_extension.md,
  SHA256 c8f75699921a83cbc2c5cc533b7b8441cf185f9cd45b130b44ad453ea6d734fb.
* H: notes/research_positive_certificate_braid_morse_bott.md,
  SHA256 6ef5423e542170ffe3b5464753613ae042341d9c2ee20a2fa94fd0d828738410.
* F: notes/research_oblique_top_fourier_aliases.md,
  SHA256 9fa4d981c401c1b744fa12b1241f0404d7ba8da90d21f6b90f556ef6a065b584.

Every complete direct was read nontruncated in the active author
sequence. The used implications and their marked normalization
conventions were checked. The older plat Ward-density theorem was
read for coverage only; it is not substituted for this braid source.
Only written mathematics and text/hash operations were used.
Frozen and public files are unchanged.
