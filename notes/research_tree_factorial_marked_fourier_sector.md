# The retained Fourier sector of the local tree factorial source

Private written proof, 16 November 2026.

For the literal same-index factorial presentation of an original
circle tree, every admitted regular stationary limit has a finite
local Fourier expansion with a common nonzero asymptotic symbol.
The original geometric logarithmic marking selects one of its
sectors. This selection is proved from the actual positive approach;
it is not an arbitrary renaming of a chamber's constant term.

On a tree the wall frequencies are independent. More strongly, after
including the exact lower angular trace denominators, their resonances
at the retained marked frequency all have positive coefficients at
both level parities. The charged cosine companions cannot resonate
at the classified common radial two-square limits, whose charge lies
strictly between \(1/2\) and \(1\).

These are statements about the specified local factorial top-form
germ and its explicit Fourier expansion. They do not identify its
coefficient in the original relative integration cycle. A genuinely
free cardinal boundary factor remains cardinal; it is not assigned
the factorial symbol by this theorem.

## 1. The actual stationary marking

Let \(T=(V,E)\) be the original finite tree and \(S\subset V\)
the selected vertices. The independent variables are all wires
\(x_e\) and selected angles \(t_v\). Outside angles are fixed at
their complete value \(t_b=0\). We consider a stationary configuration
with its original positive marking, or a limit of such configurations,
at which the pinned radial and unsummed theorems give:

* every selected angle satisfies \(|\Re t_v|<\pi\) and
  \(\Im t_v<0\);
* each edge is positive, a regular single-square corner, or one
  of the classified two-square edges;
* the original sine factors below are nonzero, and all wires have
  \(0<\Re x_e\le1/2\).

At a positive or single-square edge \(e=vw\), put
\[
 a_v=\tan(t_v/2),\qquad q_e=\cot(\pi x_e),\qquad
 q_e^2=1+a_v^2+a_w^2.
 \tag{1}
\]
The positive approach satisfies
\[
 \Re q_e>\sqrt{(\Re a_v)^2+(\Re a_w)^2};
 \tag{2}
\]
at a regular corner use its weak limiting inequality. In particular
\(q_e\pm a_v\) have positive real parts on the approach and nonzero
limits in the closed right half-plane. At a two-square edge the
pinned theorem gives
\[
 t_v=-iH_v,\quad q_e=iQ_e,\quad
 |Q_e|<\tanh(H_v/2),\qquad
 x_e=\tfrac12-\frac{i}{\pi}\operatorname{artanh}Q_e .
 \tag{3}
\]

For each incidence and sign \(\varepsilon=\pm1\), define
\[
 z_{e,v,\varepsilon}
    =\tfrac12-x_e+\frac{\varepsilon t_v}{2\pi}.
 \tag{4}
\]
Their real parts lie in \((-1/2,1)\). The original incidence
phase is
\[
 b_0(x_e,t_v)
   =-J_{\rm geom}(z_{e,v,+})-J_{\rm geom}(z_{e,v,-})
                                    -2J(x_e).
 \tag{5}
\]
Here the subscript records the logarithmic primitive continued
from completeness along the original positive branch.

Write
\[
 \Omega=\mathbb C\setminus((-\infty,0]\cup[1,\infty)),
 \qquad J'(z)=\Log(2\sin\pi z),\quad J(1/2)=0,
 \tag{6}
\]
with the canonical logarithm real on \((0,1)\). Let \(\mathcal B\)
be the list of arguments (4) having strictly negative real part
at the specified target. Every \(j\in\mathcal B\) has
\[
            -1/2<\Re z_j<0,\qquad 1/2<\Re(z_j+1)<1.
 \tag{7}
\]
There is at most one such argument at an incidence, because
\(\Re(z_{e,v,+}+z_{e,v,-})=1-2\Re x_e\ge0\).
There are none at complete outside ends: there
\(z_{e,b,\pm}=1/2-x_e\), and an edge with a complete outside
endpoint is positive. There are none at the two-square incidences
themselves, by (3) and the strict opposite half-plane test of the
pinned factorial-amplitude theorem. Negative-real-part arguments
at other incidences are included even when they are not real.

**Lemma 1 (the retained two-branch marking).** At a target argument
with \(\Re z_j\ge0\), the geometric primitive is exactly (6).
For every \(j\in\mathcal B\), there is a uniquely determined
\(\sigma_j\in\{1,-1\}\) such that, on a neighborhood,
\[
                  J_{\rm geom}(z_j)
                         =J(z_j+1)-\sigma_j\pi i z_j .
 \tag{8}
\]
The identities include their additive constants.

**Proof.** The literal sine identity is
\[
 \sin(\pi z_{e,v,\varepsilon})
   =\sin(\pi x_e)\cos(t_v/2)(q_e+\varepsilon a_v).
 \tag{9}
\]
Along the positive approach, the three factors on the right
are in the right half-plane. Indeed \(0<\Re x_e<1/2\),
\(|\Re t_v|<\pi\), and (2) applies. Their principal logarithms
agree at completeness with the original logarithm in (5).
The same is true along the actual simultaneous tangent contraction
to completeness, which stays positive by the pinned product-domain
theorem. Consequently their sum, plus the real constant \(\log2\),
is the geometric logarithm, without a further integer multiple
of \(2\pi i\).

At a regular limit, the first two factors still have strictly
positive real parts, while the last is nonzero in the closed
right half-plane. Hence the imaginary part \(\vartheta_j\) of
the resulting geometric logarithm obeys
\[
                   -3\pi/2<\vartheta_j<3\pi/2.
 \tag{10}
\]
If \(0<\Re z_j<1\), the canonical sine logarithm has imaginary
part in \((-\pi/2,\pi/2)\). No nonzero \(2\pi\) translate
fits (10). If \(\Re z_j=0\), nonvanishing forces
\(\Im z_j\ne0\); the canonical imaginary part is \(\pi/2\)
or \(-\pi/2\), and strictness in (10) gives the same conclusion.

If (7) holds, \(2\sin\pi(z_j+1)\) lies in the right half-plane.
Since \(\sin\pi z_j=-\sin\pi(z_j+1)\), the logarithmic
derivatives permitted by (10) are exactly
\[
                 J'(z_j+1)-\sigma_j\pi i,\qquad \sigma_j=\pm1 .
 \tag{11}
\]
This fixes the sign from the original marking.

To check constants, every argument path of a positive contraction
stays in the strip \(-1/2<\Re z<1\) and avoids zero. Zero
is its only possible sine zero. On this strip
\(2\sin(\pi z)/z\) extends as a holomorphic nonzero function
through zero. Thus the original primitive on its logarithmic
cover has the form
\[
 J_{\rm geom}(z)=z\Log z-z+K(z),\qquad
 K'(z)=\log\frac{2\sin\pi z}{z},\quad K(0)=0,
 \tag{12}
\]
where the logarithm in \(K'\) is fixed by its real value near
zero. The normalization agrees with (6), since \(J(0)=0\)
as a one-sided limit. A turn about zero changes the primitive
by exactly \(2\pi i z\), with no constant term. The two
branches in (8) are the adjacent branches of (12): their
derivatives are (11), and their limits at zero are zero because
\(J(1)=0\). Equality of derivatives therefore identifies their
full primitives. This also proves the constant assertion for
the arguments with nonnegative real part. The unit sine factors
extend these identities to the independent-variable local germs.
\(\square\)

## 2. An exact finite Fourier expansion of all factorial factors

Use the original \(G_N\), \(N\ge2\), \(D=N-1\), and
\[
 B_N(x,t)=\frac{N}{
 G_N(N(1/2-x+t/(2\pi))-1/2)
 G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{13}
\]
Let \(\mathcal I\) denote all four signed incidence arguments
per edge, and put
\[
 z'_j=\begin{cases}z_j+1,&j\in\mathcal B,\\z_j,&j\notin\mathcal B.\end{cases}
 \tag{14}
\]
Every \(z'_j\) belongs to \(\Omega\). Near a target with
\(\Re z_j=0\), its nonzero imaginary part gives the required
fixed neighborhood in \(\Omega\).

The exact full-period identity of the original factorial gives
\[
 \frac1{G_N(Nz-1/2)}
   =\frac{e^{i\pi Nz}+e^{-i\pi Nz}}{G_N(N(z+1)-1/2)}.
 \tag{15}
\]
Indeed \(G_N(w+N)=-2\sin(\pi w)G_N(w)\), and
\(-2\sin\pi(Nz-1/2)=2\cos\pi Nz\).
The centered offset \(-1/2\) is essential to the plus sign.

Set \(m=|E|\) and define the exact common factor
\[
 U_N=\frac{N^{2m}}
 {\displaystyle\prod_{j\in\mathcal I}G_N(Nz'_j-1/2)
                 \prod_{e\in E}G_N(Nx_e)^4},\qquad
 S_{\rm base}=-\sum_{j\in\mathcal I}J(z'_j)-4\sum_eJ(x_e).
 \tag{16}
\]
The divisor theorem implies that \(U_N\) is a holomorphic unit
on one neighborhood independent of \(N\ge2\). For arguments
in a positive-real-part strip this uses
\(-1<\Re(Nz'_j-1/2)<N\), after shrinking the neighborhood;
arguments on the imaginary axis instead have imaginary parts
bounded away from zero. All wires remain in \(0<\Re x_e<1\).

The centered expansion of the pinned factorial-amplitude theorem
therefore gives an exact holomorphic unit \(A_N\), defined by
\[
 U_N=N^{-2m}e^{NS_{\rm base}}A_N,\qquad
 A_N=A_0(1+O_{\rm hol}(N^{-1})),\qquad
                  A_0=\prod_{e\in E}(2\sin\pi x_e)^{-2}\ne0.
 \tag{17}
\]
It has the complete holomorphic inverse-power expansion supplied
by that theorem. This is a relative expansion of the common
unit even when the full product below has exact zeros.

Write \(S_{\rm geom}=\sum_{e=vw}\{b_0(x_e,t_v)+b_0(x_e,t_w)\}\).
Lemma 1 and (15) now give the exact local identity
\[
 \boxed{\quad
 \prod_{e=vw}B_N(x_e,t_v)B_N(x_e,t_w)
   =N^{-2m}A_N e^{NS_{\rm geom}}\,
       \prod_{j\in\mathcal B}
                    \bigl(1+e^{-2\pi iN\sigma_j z_j}\bigr).
 \quad}
 \tag{18}
\]
All constants, finite offsets and level-dependent zeros are
retained. In particular the exponentials selected in (18)
come from the actual signs in (8), including a selected
exponentially small sector when that occurs; no dominance
choice was used to define the geometric marking.

**Lemma 2 (tree frequency independence).** In the independent
variables \((x_e,t_v)_{e\in E,v\in S}\), the differentials
\((dz_j)_{j\in\mathcal B}\) are linearly independent. Consequently
all subsets in the finite product (18) have distinct affine
frequencies, and its constant-frequency coefficient is exactly one.

**Proof.** Suppose \(\sum_{j\in\mathcal B}c_j dz_j=0\).
Every incidence supplies at most one term. The coefficient of
each \(dx_e\) forces the two endpoint coefficients to sum to
zero; if one endpoint has no term, the other coefficient is zero.
The edges with a nonzero coefficient thus have both endpoints
in \(S\). They form a forest. A leaf of a nonempty component has
only one nonzero incident coefficient, so its independent
\(dt_v\) coefficient, equal to \(\varepsilon_j c_j/(2\pi)\),
cannot vanish. This contradiction eliminates every coefficient.
Multiplying the differentials by \(\sigma_j=\pm1\) preserves
independence. Apply it to differences of subset indicator vectors.
\(\square\)

The constant term \(1/2\) in every \(z_j\) is not suppressed.
If it is separated from the linear frequency, it contributes
\((-1)^N\) for each selected wall factor. These coefficients
are nonzero at both parities. Keeping the affine forms as in
(18) gives coefficient one for every subset.

## 3. The exact angular denominators and resonant positivity

For the literal factorial top form of the pinned joint-lens source,
retain the fixed original signed powers \(n_v\) and
\[
 \eta=(-1)^{N-1},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta e^{-iNt})^2},\qquad
 \cos(N(1-c_v)t_v),\qquad
 e^{in_vNt_v^2/(4\pi)}\sin t_v .
 \tag{19}
\]
On the selected lower angular neighborhood,
\[
 (1-\eta e^{-iNt_v})^{-2}
   =\sum_{k_v\ge0}(k_v+1)\eta^{k_v}e^{-iNk_vt_v}
 \tag{20}
\]
converges absolutely and locally uniformly for every level.
The original exterior normalization is
\[
 \mathfrak c_N=N^m\prod_{v\in S}
       \frac{-N^2C_{N,n_v}}{\pi i},\qquad
                 C_{N,n}=e^{\pi i n(N-1)^2/(4N)}.
 \tag{21}
\]
It is nonzero and is not changed here. In an application with
additional traced vertices their original factors remain as well.

Extract the marked charged action
\[
 \Phi_c=S_{\rm geom}+
              \sum_{v\in S}\left(\frac{in_vt_v^2}{4\pi}-ic_vt_v\right).
 \tag{22}
\]
Relative to this exponential, the remaining Fourier multiplier is
\[
 \mathcal R_{N,c}
 =\prod_{j\in\mathcal B}(1+e^{-2\pi iN\sigma_jz_j})
   \prod_{v\in S}
       \frac{\frac12(1+e^{-2iN(1-c_v)t_v})}
            {(1-\eta e^{-iNt_v})^2}.
 \tag{23}
\]
For \(c_v=1\) its numerator is exactly one. Thus the local top
form, apart from the unchanged overall scalar (21), is exactly
\[
 N^{-2m}e^{N\Phi_c}A_N
       \left(\prod_{v\in S}\sin t_v\right)
          \mathcal R_{N,c}\,d\mathbf x\,d\mathbf t .
 \tag{24}
\]
No trace denominator or cosine term has been discarded.

Equation (24) is an identity of the literal factorial germ.
It is an exact original joint-lens density only where every
endpoint replaced by (13) satisfies that source's traced-end
convention, or an independently proved adapter supplies the
replacement. In particular, for a proper selected set with
untraced or free outside ends, specializing their angles to
\(t_b=0\) does not itself authorize replacing their prescribed
cardinal factors by \(B_N(x,0)\).

By the marked-frequency coefficient of (23) we mean its coefficient
at zero linear frequency in the full independent variables
\((\mathbf x,\mathbf t)\), including the actual affine constants
of (4). This is a coefficient in this specified expansion,
not a coefficient assigned to an integration cycle.

**Theorem 3.** When every \(c_v=1\), that coefficient is a
positive integer \(\mathcal M\ge1\), independent of level parity.
When every \(c_v=\chi\) with \(1/2<\chi<1\), it equals
\(2^{-|S|}\mathcal M>0\), with the same integer.
In particular the latter case applies to every classified common
radial limit with a two-square edge.

**Proof.** Choose a subset \(\mathcal A\subset\mathcal B\)
of wall terms. Zero wire frequency forces every used edge
to have both endpoint terms present and their signs opposite:
\[
                     \sigma_{e,v}+\sigma_{e,w}=0.
 \tag{25}
\]
Thus \(\sum_{j\in\mathcal A}\sigma_j=0\), and the affine
constant of the wall exponent contributes exactly
\(\exp(-\pi iN\sum_{\mathcal A}\sigma_j)=1\).

At unit charges, the angular balance is
\[
          k_v=-\sum_{\substack{j\in\mathcal A\\j\text{ at }v}}
                              \sigma_j\varepsilon_j\ge0.
 \tag{26}
\]
It fixes the integers \(k_v\) uniquely. Summing (26) edgewise
using (25) gives
\[
 \sum_vk_v
   =-\sum_{e\ {\rm used}}
          \sigma_{e,v}(\varepsilon_{e,v}-\varepsilon_{e,w})
                       \ \in 2\mathbb Z .
 \tag{27}
\]
No equality of the two \(\varepsilon\)'s is assumed.
Therefore \(\eta^{\sum k_v}=1\) at both parities. This subset,
when (26) is nonnegative, contributes the positive integer
\(\prod_v(k_v+1)\). There are finitely many subsets, and the
empty subset contributes one. Explicitly,
\[
 \mathcal M=
 \sum_{\substack{\mathcal A\subset\mathcal B:
                  \text{(25) holds}\\
                  k(\mathcal A)\text{ in (26) is nonnegative}}}
                    \prod_v(k_v(\mathcal A)+1)\ge1 .
 \tag{28}
\]
Absolute convergence of (20) permits this grouping; for each
subset there is at most one resonant multiindex.

For \(1/2<\chi<1\), a choice of the companion exponential at
vertex \(v\) would replace (26) by
\[
 k_v+2(1-\chi)\ell_v
       =-\sum_{j\in\mathcal A,\ j\text{ at }v}
                         \sigma_j\varepsilon_j,\qquad
                         \ell_v\in\{0,1\}.
 \tag{29}
\]
The right side and \(k_v\) are integers, whereas
\(0<2(1-\chi)<1\). Hence every \(\ell_v=0\).
Only the marked cosine choice contributes, with its original
factor \(2^{-|S|}\), and (28) remains unchanged. The radial
two-square classification supplies \(1/2<\chi_*<1\).
\(\square\)

In the unit case the positivity calculation (25)--(28) itself
does not use the absence of graph cycles; the tree assumption
is used in Lemma 2 and in the stated original radial setting.
The common radial restriction in the second assertion is not
silently extended across \(\chi=1/2\), where a companion can
resonate and the parity argument changes.

## 4. The precise local gain and its boundary

The marked-frequency symbol in (24) is therefore
\[
 A_0\left(\prod_{v\in S}\sin t_v\right)
       \begin{cases}
          \mathcal M,&c_v=1\ \text{for all }v,\\
          2^{-|S|}\mathcal M,&c_v=\chi\in(1/2,1)\ \text{for all }v .
        \end{cases}
 \tag{30}
\]
It is nonzero: every wire sine is a unit, and
\(\Im t_v<0\) excludes \(\sin t_v=0\). The marked term after
phase extraction has an all-order holomorphic expansion with
this leading unit. Exact zeros of the unseparated factorial product can still
occur by cancellation between its distinct frequencies; (30)
is not a pointwise lower bound on that product.

At a classified two-square critical point the pinned full
unsummed Hessian theorem permits an ordinary local Morse
calculation for this marked mode. Its formal leading Gaussian
coefficient is nonzero because (30) and the coordinate Jacobian
are nonzero. This fixes a local amplitude issue of the prescribed
factorial representative. It neither proves that its descending
disk occurs in the original relative cycle nor bounds the
connectors, endpoint currents, or other stationary sectors.

The coefficient is taken only after the exact common-unit
normalization (17). Although \(A_N\) has an all-order expansion,
it may retain exponentially small terms; multiplying those by
larger competing modes can matter. Thus (30) exhibits a nonzero
marked term of this exact decomposition, not a coordinate- or
interpolation-independent transseries coefficient of the period.

The statement concerns exactly the literal factors (13), (19).
An additional spectator with a zero at the critical point is
not made a unit by this calculation. A reversed-index halfwire
retains its different phase and is not covered by this same-index
frequency argument. At a genuinely free spectral endpoint the
original compiler retains the entire cardinal polynomial; it
cannot be replaced by (13) from complete-boundary geometry alone.
All original source placement and full Hermite data remain those
of the pinned joint-lens theorem.

The coefficient in (30) is consequently not claimed to be
invariant under changing the source representative by an exact
relative current. It is the nonzero marked coefficient of the
specified canonical factorial presentation, with its angular
kernels retained. The remaining global task is still to identify
and estimate the entire original relative class.

## Direct sources and author readback

* [Two-square factorial amplitude](research_two_square_factorial_amplitude.md),
  SHA256 995c38d1cc6fcd5a1a1306601778ce6068b5f1d766364216e7cdd933f344290f:
  centered all-order expansion on \(\Omega\), exact normalization,
  and units at the two-square incidences. The complete author
  readback is retained at the unchanged hash.
* [Positive wire product domain](research_positive_wire_product_contour.md),
  SHA256 5646f2d6b2a8dfa2d8c49662d17f19f3743fc4efcaf3c3685c6a899975a4c230:
  canonical inverse cotangent, actual tangent contraction and
  positive right-half-plane condition. Complete read retained.
* [Radial two-square primitive lift](research_radial_two_square_primitive_lift.md),
  SHA256 21d9af750653621cc82bd73373a99a138210fc4cdb10407faabcb209505df9ad:
  the admitted radial limits, matching, nonzero factors and
  strict common-charge bound \(1/2<\chi_*<1\).
  Complete author and direct-source readbacks retained.
* [Full unsummed fold phase](research_unsummed_two_square_morse_lift.md),
  SHA256 82ad7a75e6ab2857bbebb2f003f7e182ab1f26da1cf425f579106cdad11d15dd:
  the original marked phase and full Hessian, with its stated
  source and boundary limitations. Complete read retained.
* [Joint factorial-lens source](research_joint_factorial_lens_relative_source.md),
  SHA256 a14ca148bd55b36b1eea9de8be8a63025532c3bbbb928482b0d7cb8edae56e54:
  the exact angular factors, normalization, complete physical
  normals, and free-cardinal/relative-cycle distinctions.
  The entire text was reread in this proof sequence.
* [Exact canonical factorial](research_exact_cyclotomic_factorial.md),
  SHA256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b:
  original gamma normalization and sine recurrence underlying
  (15). The complete read is retained at the unchanged hash.

The existing factorial chamber atlas already retains exact
Fourier divisors. The new assertions here are the bound on the
actual geometric logarithmic lift, its identification with one
finite sector, tree frequency independence, and positive resonance
after the original angular kernels are included.

Only written proofs, source-text reads and hashes were used.
No mathematical program, numerical calculation, test or compilation
was run. Frozen notes and public documents were unchanged.
