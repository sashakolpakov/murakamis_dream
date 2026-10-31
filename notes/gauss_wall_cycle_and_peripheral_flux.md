# Independent Gauss-wall cycle and peripheral-flux calculation

Proof and audit, 27 October 2026. The fixed-meridian physical and
exceptional spheres differ by a nonzero integral wall-torus class.
This gives an explicit Gysin obstruction, stronger than an obstruction
only to section homotopies. The meridian detour transfers the charge
to a peripheral logarithm and changes the retained \(SL_2\) lift.
The actual quantum wall residues and the inverse-flux character have
the stated normalizations below.

This independently checks
[the meridian wall theorem](meridian_homotopy_wall_and_source_residues.md)
and [the flux/peripheral character](gauss_wall_flux_and_actual_peripheral_character.md).
It does not identify a quantum source pushforward or a volume norm.

## 1. The cut divisor and its closed detecting form are global

On \(Y\), the two charts have
\[
 V=v^{-1},\qquad \eta'=-v^2\eta,\qquad a'=v-v^2a.
\]
The fixed-ambient matrix entry
\[
 F=\mu_{11}=1-\eta v=1+\eta'V
\]
is one global function. In particular the south expression has a
plus sign. Using \(1-\eta'V\) would select the other diagonal
entry, not another expression for this same divisor.
Its zero divisor is
\[
 D\simeq\mathbb G_{m,v}\times\mathbb A^1_a,\qquad\eta=1/v.
\]

The closed form
\[
 \Xi=\frac{dv\wedge d\eta}{F}
      =d\log F\wedge d\log v
      =\frac{dV\wedge d\eta'}{F}                  \tag{1}
\]
is regular everywhere on \(Y\setminus D\); the displayed affine
fractions remove its apparent flag-coordinate poles.
Its residue is \(d\log v\).

Put \(c=2\pi i\), \(T=va\), and orient the compact source by
\[
 v=\sqrt{T/(1-T)}e^{i\phi},\quad
 a=\sqrt{T(1-T)}e^{-i\phi},\quad
 \Omega=dv\wedge da=-i\,dT\wedge d\phi.
\]
For the exceptional sphere \(\eta=0\), the pullback of \(\Xi\)
is zero. For the physical sphere
\(\eta=(1-e^{-cT})/v\), it is \(c\Omega\). Hence
\[
 \int_{\Gamma_{\mathrm{phys}}}\Xi=-c^2=4\pi^2,\qquad
 \int_{\Gamma_E}\Xi=0.                            \tag{2}
\]
This already excludes any homology between them in \(Y\setminus D\),
without requiring a proposed homotopy to preserve its flag coordinates.

## 2. Integral Gysin class and its orientation

The radial three-chain \(\eta=\lambda\eta_{\mathrm{phys}}\) has
\[
 F=1-\lambda+\lambda e^{-cT}.
\]
It meets \(D\) once in the transverse \((\lambda,T)\) plane,
at \(\lambda=T=1/2\), along the circle
\[
 \gamma_v:\quad v=e^{i\phi},\quad
 a=1/(2v),\quad\eta=1/v.
\]
Near it,
\[
 F=-2(\lambda-1/2)+\pi i(T-1/2)+\text{higher terms}.
\]
Thus the complex-normal orientation is opposite the
\((\lambda,T)\) orientation, and the oriented intersection is
\(-\gamma_v\). Define the tube by a positive complex-normal
circle followed by the positive \(v\)-circle. Excision gives
\[
 [\Gamma_{\mathrm{phys}}]-[\Gamma_E]=-\operatorname{Tube}[\gamma_v].
                                                               \tag{3}
\]
Its period checks the sign:
\[
 \int_{\operatorname{Tube}\gamma_v}\Xi
   =(2\pi i)\int_{\gamma_v}d\log v=c^2.
\]

This tube is a generator, rather than a possible torsion correction.
The affine-bundle projection \(Y\to\mathbb P^1\) has contractible
two-dimensional fibres. A continuous section and affine fibre
contraction give a deformation to \(\Gamma_E\). Hence
\(H_3(Y,\mathbb Z)=0\), \(H_2(Y,\mathbb Z)=\mathbb Z\).
A normal neighborhood of \(D\) has the explicit normal coordinate
\(F\), and the relative homology shifts that of
\(D\simeq\mathbb C^*\times\mathbb C\) by two.
Its long exact sequence gives
\[
 0\longrightarrow H_1(D,\mathbb Z)
   \xrightarrow{\mathrm{Tube}}H_2(Y\setminus D,\mathbb Z)
   \longrightarrow H_2(Y,\mathbb Z)\longrightarrow0 .
\]
The following intersection map is zero because the generator
\(\Gamma_E\) is disjoint from \(D\).
Consequently \(H_2(Y\setminus D,\mathbb Z)\simeq\mathbb Z^2\),
split by \(\Gamma_E\), and (3) is its nonzero wall component.

## 3. Meridian variation transfers the charge

For a retained eigenvalue \(m\), the resolved meridian is
\[
 \mu=\begin{pmatrix}
 m-\eta v&\eta\\
 (m-m^{-1})v-\eta v^2&m^{-1}+\eta v
 \end{pmatrix},
 \quad
 \eta'=(m-m^{-1})v-v^2\eta.                       \tag{4}
\]
It has determinant one and the stated eigenflag.
The global cut function is \(F=m-\eta v=m^{-1}+\eta'V\).
The explicit path
\[
 m_\lambda=e^{c\lambda/2},\quad
 \eta_\lambda=
      m_\lambda(1-e^{-c\lambda T})/v
\]
has nonzero \(F=m_\lambda e^{-c\lambda T}\) and a removable
south expression
\(m_\lambda^{-1}(e^{c\lambda T'}-1)/V\).
It ends at the central negative of the physical meridian.
It is a cut-meridian homotopy, not continuation of an entire
knot representation or its quantum word.

The sign is necessary for this once-winding clock if the pole
clutches remain specified. If \(m\) were instead a closed
path \(1\to1\) with winding \(k\), the boundary of the
\((\lambda,T)\) rectangle under a nonzero \(F\) would have
winding \(2k-1\): each polar edge supplies \(k\), while the
physical edge supplies \(-1\). It cannot bound a nonzero
function on that rectangle. The half-path \(1\to-1\)
supplies the required two half windings.

The local regular varying-meridian forms differ by
\[
 \Xi_S-\Xi_N=2d\log m\wedge d\log v
             =d(2\log m\,d\log v).
\]
Their compact period is
\[
 I=-2c\log m=2c\log M,\qquad M=m^{-1}.            \tag{5}
\]
This inverse-eigenvalue convention matters. The literal signed
quantity \(\int\Xi/(c h_N)=-N\lambda\) is opposite the Chern
degree convention \(c_1=-F_{\mathrm{curvature}}/(2\pi i)\) of the
compact \(O(N)\) source; the latter degree is \(+N\lambda\).
Either signed curvature index can be used if identified explicitly.

The fixed-root Weyl matrix compares \(M\) and \(M^{-1}\); it
does not by itself implement this path or identify the central
sign \(M=1\) with \(M=-1\). Its full scalar and source divisors
must remain when using the even reduced meridian coordinate.

## 4. Global three-form primitive and marked radial period

The source connection \(\theta=-a\,dv\) obeys
\(\theta'=\theta+d\log v\). Thus
\[
 \vartheta=d\log\eta-2\theta
\]
is global off \(E\), with \(d\vartheta=-2\Omega\).
For \(H_G=-d\log\eta\wedge\Omega\) and \(H_{\mathrm{cut}}=H_G/F\),
the exact global primitive is
\[
 H_{\mathrm{cut}}-H_G=dB,\qquad
 B=\tfrac12d\log F\wedge\vartheta
  =\frac{1-2va}{2F}d\eta\wedge dv.               \tag{6}
\]
It is regular along \(E\), with poles only on \(D\). Its south
expression is \((2Va'-1)d\eta'\wedge dV/(2F)\).
The residue is
\[
 \operatorname{Res}_D B=(a-1/(2v))\,dv,\qquad
 -d\operatorname{Res}_D B=\Omega.
\]
It vanishes on the radial intersection circle. Also
\(B|_{\Gamma_{\mathrm{phys}}}=-(1-2T)\Xi/2\) has zero period.
This does not remove the distinct two-cycle class (3).

Radial integration of \(H_{\mathrm{cut}}-H_G\) uses the logarithm
along the chord from \(1\) to \(e^{-cT}\). That logarithm is
\(-cT\) below \(T=1/2\), and \(c(1-T)\) above it; its compact
mean is zero. The physical marked logarithm is \(-cT\) throughout.
Its correction is therefore
\[
 (-c)\int_{T>1/2}\Omega=c^2/2=-2\pi^2 .
\]
At \(h_N=c/N\) the numerical exponential is \((-1)^N\).
This is a marked relative-period phase. Its appearance in the
actual quantum action still requires the actual action/source map.

## 5. Actual character and polynomial wall charges

For the actual variable \(M\), (5) gives the direct flux
\(I_{\mathrm{phys}}=2c\log M\). Its explicit inverse character is
\[
 \chi_H=\exp(-I_{\mathrm{phys}}/H)
        =\exp(-2c\log M/H).
\]
It is invariant under \(M\mapsto e^{H/2}M\); its marked
square root changes sign. At \(H_N=c/N\) they are
\(M^{-2N}\) and \(M^{-N}\), respectively. The meridian-log
deck multiplier is \(e^{-2c^2/H}\), with value one but
logarithmic-\(Q\) derivative \(2N^2\) at the root.

For the original phase \(\epsilon_N=i^{N+3}\),
\[
 d_N(M)=\epsilon_N
       \frac{\kappa\chi^{1/2}}{1-\chi},\qquad
 \kappa=M-M^{-1},                                \tag{7}
\]
is exactly its full modified dimension at those roots.
Its canceled complete value is \(\epsilon_N/N\), and its
half-step ratio is \(-\kappa(qM)/\kappa(M)\).
This checks the root character, not an auxiliary off-root
finite-matrix normal lift.

Along \(M=e^{-\pi i\lambda}\), the actual source poles at
\(\lambda=k/N\) have precisely
\[
 \operatorname{Res}\bigl[d_N(M)F_N(M^2)d\lambda\bigr]
 =\frac{\epsilon_N(-1)^k\sin(\pi k/N)}{\pi N}
       C_k(q_N).
\]
For \(d\log M\), multiply by \(-\pi i\).
The ordinary-color bound therefore gives total absolute
canonical-meridian residues below \(2D_N/\pi\), or total
\(d\lambda\) contour corrections below \(4D_N/\pi\).
The flux note's weaker bound \(2D_N\) for those latter
corrections is valid. These charges do not estimate a transport
kernel or the Kashaev point value.

All matrix, cycle, sign and source statements above check.
The remaining global continuation of the geometric A-branch,
source-current pushforward and selected regular-sector norm
are explicitly separate.
