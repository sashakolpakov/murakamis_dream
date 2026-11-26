# The marked reduced braid action and its meridian parity

Private written proof, 18 November 2026.

The meridian conjugate of the literal reduced braid trace is
\((-1)^{m-1}\ell_{\mathrm{intr}}\), for a braid on \(m\) original
heads. The factor is fixed by the original tail pivots. It cannot
be recovered from the complete Bloch--Wigner value alone.
The local comparison below also calibrates the meridian-dependent
constant of the first-head reduction, without asserting an
asymptotic amplitude for that reduction on its vacuum.

For an odd-head presentation of a complete hyperbolic knot,
the reduced marked action consequently has a nonzero first
meridian derivative, equal to an odd integer times \(2\pi i\).
This determines the leading first-jet multiplier of an already
supplied differentiable geometric trace contribution. It does
not supply that contribution, its cycle, or noncancellation
between different contributions.

## 1. Actual normalization and local meridian derivatives

Put
\[
 c_0=2\pi i,\qquad h=c_0/N,\qquad q=e^{h/2},\qquad
 d=N-1,\qquad M=e^\mu,\qquad x=-M/q .
 \tag{1}
\]
The meridian varies at fixed \(q=q_N\). Use the actual branch
\(\Log x=\mu+\pi i-h/2\). The original positive crossing is
\(\kappa\mathsf P D_{\mathrm{Cartan}}\Theta\); R proves that
its positive stabilization scalar is
\(\vartheta=\kappa x^{-d}\). Thus a zero-framed word can be
formed from normalized positive generators
\[
 \widehat R_i=\vartheta^{-1}R_i,\qquad
 \mathcal B_m(\widehat R_1)=x^d S_{m-1}D_{\mathrm{red}},
 \quad
 (D_{\mathrm{red}})_a=(-1)^a q^{a(a+1)}M^{-2a},
 \tag{2}
\]
and their exact inverses. This distributes the original
zero-framing scalar; it introduces no new normalization.

All occupation logarithms below are the unwrapped ones
\(a=h\,a_{\mathrm{occ}}\), and similarly for other indices.
Write \(A=e^a,B=e^b,C=e^c\). Q's literal signed coefficients,
including (2), give their principal meridian derivatives
\[
 \begin{split}
 D_\mu\mathcal S_+
 &=c_0-a-b-c+
  2\Log\frac{1-M^2C/A}{1-M^2/A},\\
 D_\mu\mathcal S_-
 &=-c_0+a+b-c+
  2\Log\frac{1-M^2C/B}{1-M^2/B}.
 \end{split} \tag{3}
\]
Here \(D_\mu\) holds independent input/transfer logarithms
fixed before restriction to their canonical graph. These
formulas can also be checked by differentiating the finite
color products before taking their principal term.
The \(c_0\)'s in (3) are the derivative of \(x^{\pm d}\);
they are not centered away.

For an \(S_s\) entry, G gives the exact \(M\)-monomial
\[
 x^{-\sum_{j=2}^s(j-1)n_j}.
 \tag{4}
\]
Its inverse has the same monomial and an additional
\((-1)^{\sum n_j}Q^{(\sum n_j)(\sum n_j-1)/2}\), independent
of \(M\). Consequently, for either literal sign,
\[
 D_\mu\mathcal S_{S_s^{\pm1}}
 =-\sum_{j=2}^s(j-1)c_j=-\Delta J_s,\qquad
 J_s=\sum_{j=1}^s j\Log A_j .
 \tag{5}
\]
The transfer logs in (5) are those of that signed entry.
Indeed its donor changes by \(-\sum c_j\) and recipient
\(j\) changes by \(c_j\). The inverse's chirp and its
half shifts remain in the primitive, but have zero
derivative in (5).

For the normalized reduced positive boundary generator,
with donor input logarithm \(u\), (2)--(5) give
\[
 D_\mu\mathcal S_{\mathrm{red},1}
 =c_0-2u-\sum_{j=3}^{m}(j-2)c_j^{\mathrm{red}} .
 \tag{6}
\]
The displayed recipient labels retain the original numbering.
Its negative generator is the actual inverse in the order
\(D_{\mathrm{red}}^{-1}S_{m-1}^{-1}x^{-d}\).

## 2. The generic-meridian free quotient graph

We first extend the algebra used in G's complete resolved
chart; this is needed to compare marked derivatives.
Its literal \(S_m\) graph (G (7)--(15)) is already defined
for generic \(M\), with \(x=-M\) in principal formulas:
\[
 K=x/A,\qquad e=(M/A-M^{-1})p,\qquad f=(1-A)/p .
 \tag{7}
\]
Set the new first position to \(A_1=1\), retaining its
flag \(p_1\). The first lowering coordinate is zero.
Put \(C=1-p_1F_{\mathrm r}/x\). On the unit domain of
the Gauss prefixes and partial \(S\) denominators, the
old first physical head is
\[
 K_{1,\mathrm{old}}=xC,\quad
 f_{1,\mathrm{old}}=-F_{\mathrm r}/(xC),\quad
 e_{1,\mathrm{old}}=(MC-M^{-1})p_1 .
 \tag{8}
\]
There is no use of \(M=1\) in these identities.

At \(p_1=0\) define
\[
 H_1^0=\begin{pmatrix}x&0\\-F_{\mathrm r}&x^{-1}\end{pmatrix},
 \qquad
 h_0=\begin{pmatrix}1&0\\-F_{\mathrm r}/x&1/x\end{pmatrix}.
 \tag{9}
\]
The old remaining dressed meridians are
\(h_0H_j^{\mathrm r}h_0^{-1}\). For arbitrary \(p_1\) the
whole old tuple is its simultaneous conjugate by
\[
 U(p_1)=\begin{pmatrix}1&p_1\\0&1\end{pmatrix}.
 \tag{10}
\]
For the first head, multiply \(U H_1^0U^{-1}\):
its upper-right entry is
\(p_1(M-M^{-1})+p_1^2F_{\mathrm r}
 =(MC-M^{-1})p_1\), giving (8).
For all later heads the product of the first lower-Gauss
inverse with G's recipient conjugator is exactly
\[
 \begin{pmatrix}C&p_1/x\\-F_{\mathrm r}/x&1/x\end{pmatrix}
 =U(p_1)h_0 .
 \tag{11}
\]
This proves (10) for every prefix, at generic meridian.
It also proves
\[
 F_\Sigma=0,\qquad K_\Sigma=xK_{\mathrm r},\qquad
 E_\Sigma=E_{\mathrm r}
              +p_1(K_\Sigma^{-1}-K_\Sigma).
 \tag{12}
\]

The quotient-generator calculation in G likewise remains
valid with arbitrary \(x=-M\). On the section (9), the
original first head has \(e_1=0\). The positive crossing
has transfer clock one (transfer logarithm zero) and sends the first pair to
\[
 K_{1,R}=K_2,\quad K_{2,R}=x,\quad
 e_{1,R}=e_2/x,\quad e_{2,R}=0,\quad
 f_{1,R}=xf_2,\quad
 f_{2,R}=-xK_2f_2-F_T/x .
 \tag{13}
\]
Undoing \(S_m\) uses \(p_{1,\mathrm{new}}=p_2/x\).
Its remaining donor is
\[
 K_{2,\mathrm{new}}=K_2+p_2F_T/x^2,\qquad
 p_{2,\mathrm{new}}=-p_2/(xK_2).
 \tag{14}
\]
These are \(D_{\mathrm{red}}\), then \(S_{m-1}\).
For every later head the matrix identity G (27),
whose entries involve \(x,K_2,p_2,F_T\) and no relation
\(x^2=1\), identifies the same ordered lower prefixes.
Thus this is equality of the entire quotient maps.
Physical generators \(i\ge2\) preserve the recipient
ordered totals and give the original physical crossing.
Inversion proves the negative maps.

In particular, if \(K_\Sigma^2\ne1\), a reduced fixed
tuple closes the first flag as well: conservation of
the last expression in (12) makes its possible change
times \(K_\Sigma^{-1}-K_\Sigma\) zero. This uses a unit,
and holds on the generic-meridian critical scheme.
It is not a scalarity assumption about a cut amplitude.

## 3. Calibration of the meridian-only primitive constant

Let \(\chi\) be the free \(S_m\) graph just described.
On a common nondegenerate logarithmic graph compare the
sum of literal primitives for
\[
                  \chi^{-1}\widehat R_i^{\pm1}\chi
 \tag{15}
\]
with the primitive of its literal reduced generator.
Choose the additive input/output and transfer logs
consistently. Internal Fourier integer covectors can be
assigned to these graphs as in G; their pullbacks use
integer occupation conservation and preserve the finite
lattice weights. The new first occupation logarithm
is the actual zero lift of \(A_1=1\).

At fixed \(\mu\), the canonical differentials of (15)
and the reduced primitive agree. Every internal boundary
term cancels; the first-head boundary is
\(\log p_1\,d\log A_1=0\) on this level. Their difference
is therefore a function of \(\mu\) alone on each matched
logarithmic component. Equality of canonical maps alone
does not determine that function.

Here its derivative has an explicit calibration.
First take generic \(M^2\ne1\), and let the free input
flag \(p_1\) tend to zero while the remaining inputs are
generic. Compute the limit of the explicit partial
derivatives (3),(5), rather than differentiating a
singular vacuum amplitude. All initial \(S_m\) transfer
logs tend to zero, so its derivative tends to zero.
For \(i=1\), the physical crossing has input logs
\((0,u)\) and transfer log zero. Its color ratio in
(3) tends to one, giving \(c_0-u\).

After this crossing its first occupation is \(u\),
its second is zero, and all later inputs are unchanged.
In the final inverse \(S_m\), compare the same output
positions with the reduced \(S_{m-1}D_{\mathrm{red}}\).
The inverse \(S_m\)'s transfer logs are exactly
\[
 c_2=u-\sum_{j=3}^{m}c_j^{\mathrm{red}},\qquad
 c_j=c_j^{\mathrm{red}}\quad(j\ge3).
 \tag{16}
\]
They retain the full donor/output conservation equality.
Equation (5) gives its derivative
\[
               -u-\sum_{j=3}^{m}(j-2)c_j^{\mathrm{red}} .
 \tag{17}
\]
Adding \(c_0-u\) gives exactly (6). Hence the derivative
of the meridian-only discrepancy is zero.

This calculation is on the free generating graph before
closing the braid. Some limiting dilogarithm shapes are
one. Their \(0\Log0\) primitive limits are retained,
while (3),(5) have the specified finite limits for
generic \(M^2\ne1\). No value or asymptotic expansion of
the finite \(S_m\) matrix on the first vacuum is used.
The derivative identity, initially on its unit domain,
then continues with its actual logarithmic sheets.

For \(i\ge2\), take the same \(p_1\to0\) limit.
Both \(S_m\) boundaries have zero transfers and the
middle crossing is exactly the remaining physical one,
so the same derivative discrepancy is zero.

The negative calibration retains the actual inverse.
For a physical inverse graph the input/transfer logs
change by
\[
                    (a,b,c)\longmapsto(b+c,a-c,-c).
 \tag{18}
\]
Substitution into (3) changes its derivative to its
negative, modulo \(4\pi i\) from the retained logarithm
branches. In (5), \(\Delta J\) changes sign; the inverse
chirp is independent of \(\mu\). The diagonal factors
and \(x^d\) invert literally. Thus the calibrated
extended meridian graphs are inverses, including
their scalar sign. This proves the comparison for
both signs of every generator.

## 4. Closing the word and restoring the original pivot

Sum Section 3 over the signed word. At intermediate
interfaces all \(\chi\) terms cancel. At a reduced
fixed tuple with \(K_\Sigma^2\ne1\), Section 2 makes
the two remaining full endpoints equal as well.
Consequently the marked meridian derivative of the
literal reduced trace equals that of the original
zero-framed crossing word with no tail pivots.

The comparison with Q's original source must therefore
restore those pivots. A single original tail pivot is
\[
 g_a=x^{1-N}Q^{a(N-1)}.
 \tag{19}
\]
Its principal term is
\[
 \mathcal S_g=c_0\Log A-c_0(\mu+\pi i),\qquad
                         D_\mu\mathcal S_g=-c_0 .
 \tag{20}
\]
There are \(m-1\) such factors and none on the opened
head. The \(c_0\Log A\) terms are the specified integer
Fourier shifts of the internal stationary equations;
they do not change the exponentiated critical tuple.
They have zero partial \(\mu\)-derivative. The remaining
\(-c_0(m-1)\mu\) is a meridian character and cannot be
removed as an internal Fourier character.

Write \(\mathcal S_{\mathrm{red,flat}}\) for the reduced
literal primitive with its assigned internal Fourier
correction. Q proves that the original marked source
has derivative \(2\Log\ell_{\mathrm{intr}}\).
The preceding calibration and (20) give
\[
 \boxed{\quad
 \exp\!\left(\tfrac12D_\mu
                    \mathcal S_{\mathrm{red,flat}}\right)
       =(-1)^{m-1}\ell_{\mathrm{intr}} .
 \quad} \tag{21}
\]
On matched logarithmic lifts this says
\[
 D_\mu\mathcal S_{\mathrm{red,flat}}
   =2\Log\ell_{\mathrm{intr}}+c_0(m-1)
                       \pmod{4\pi i\mathbb Z}.
 \tag{22}
\]
The unspecified integer is locally constant. No value
of it is needed for the parity consequence.
On a differentiable log-critical branch the derivative
of the restricted flat action is this partial derivative:
all its internal derivatives vanish after the retained
Fourier correction. Q's preferred eigenvalue is invariant
under a change of the free flag frame. Thus one can use
a generic nonzero first flag to apply Q's cut convention,
and then continue the same identity on the reduced chart;
no quantum cut is changed by this classical comparison.

Equations (21)--(22) concern the literal reduced
primitive and its critical meridian normal. They were
not obtained by substituting the physical root identity
\(K_{\mathrm r}^N=\varepsilon M^{(m-1)N}\) at an off-grid
geometric clock. Nor were they inferred from equality
of complete Bloch--Wigner values.

At resolved factorial faces, (21) is the continuation
of the rational, exponentiated meridian character with
the stated cancellations. A holomorphic differentiated
phase at such a face still requires an actual local
phase chart. The correspondence identity does not
manufacture its amplitude or move a physical contour.

## 5. Odd presentation and the complete derivative

L proves, in Q's retained determinant-one convention,
\(\ell_{\mathrm{intr}}(1)=-1\) for every complete
hyperbolic knot exterior in \(S^3\).
For odd \(m\), equations (21)--(22) imply
\[
 \left.D_\mu\mathcal S_{\mathrm{red,flat}}\right|_{M=1}
       =c_0\,\nu,\qquad \nu\in2\mathbb Z+1 .
 \tag{23}
\]
In particular this derivative cannot vanish on any
compatible marked branch for which it is defined.

An odd presentation with regular semisimple total
product is available using actual source-preserving
operations. R first makes the total product \(P\)
regular semisimple with at most three positive
stabilizations and braid conjugation. If its resulting
head number is even, move any meridian \(H=\delta(I+B)\)
to the last position by R's Hurwitz conjugation and
stabilize repeatedly there. Its product becomes
\(H^tP\), with
\[
 \operatorname{tr}(H^tP)
          =\delta^t(\operatorname{tr}P+t\operatorname{tr}(BP)).
 \tag{24}
\]
If \(\operatorname{tr}(BP)=0\), every \(t\) keeps it
regular. Otherwise at most two \(t\)'s make its trace
equal to \(2\) or \(-2\), up to the displayed sign.
One of \(t=1,3,5\) therefore gives both odd head number
and regular total product. The tuple remains a knot
fixed tuple by R's equal-meridian stabilization rule.
R's exact partial pivotal trace
\(\operatorname{Tr}_2((I\otimes g)R_+)=\vartheta I\)
and its zero-framing compensation preserve the
original common-meridian source. This is not an
off-root quantum-normal assertion.

## 6. The first-jet multiplier and its precise hypothesis

Let \(B_N(M)\) be the zero-framed actual reduced word.
H gives the original pointed source exactly:
\[
 \Phi_N(1)=\frac1{2\varepsilon}
     \operatorname{Tr}((K_0+K_0^{-1})B_N(1))
 +\frac1{2\varepsilon m}
     \operatorname{Tr}((K_0-K_0^{-1})B_N'(1)),
 \quad
 \varepsilon=(-1)^{(N+1)(m-1)} .
 \tag{25}
\]
All separately prescribed peripheral scalar lines remain
outside or inside this expression exactly as originally
specified. In particular no additional factor \(N\) is
inserted for the first-jet row.

Suppose an actual differentiable localized trace sector
has already been established with phase
\(\mathcal S_{\mathrm{red,flat}}\), nonzero leading
amplitude, and a first-meridian asymptotic differentiable
to relative \(o(N)\). Suppose also that insertion of the
literal \(K_0^{\pm1}\) in that same sector has leading
symbols \(k^{\pm1}\). These are hypotheses about the
actual sector and its derivative, not conclusions from
the rational critical scheme. If its uninserted leading
term is \(N^\alpha a e^{\mathcal S(1)/h}\), then (23)
and the product rule give the contribution of (25):
\[
 N^{\alpha+1}e^{\mathcal S(1)/h}
 \left(\frac{\nu(k-k^{-1})a}{2\varepsilon m}+o(1)\right).
 \tag{26}
\]
For the regular-total geometric tuple,
\(K_\Sigma=-k\) at completeness, so \(k^2\ne1\);
the coefficient in (26) is nonzero. For odd \(m\),
\(\varepsilon=1\). The \(N\) in (26) is exactly
\(D_\mu\mathcal S/h=\nu N\).

No decomposition into such sectors is proved here.
In particular the finite physical Cartan pair
localizers do not by themselves localize either
off-circle geometric total-product eigenline.
Even if (26) holds for individual sectors, their
coefficients can cancel in the complete closing sum.
All boundary/projector currents, the original cycle,
and arbitrary fixed short fillings retain that issue.

## Complete proof directs

* G: notes/research_actual_reduced_braid_critical_scheme.md,
  SHA256 ddddcd9bf75f35afdf3e5de0c03323acee2c66e624db36142c2344ef729a977a.
* Q: notes/quantum_longitude_and_regulator_action.md,
  SHA256 e8ac5dc6bab05be0dad3810311dc3a8b169ad810b898aa3db75582087dbe8aa7.
* R: notes/research_actual_reduced_braid_source.md,
  SHA256 9a472ef27b08305a519ff1f24b6d2b909e63a0acbdc49b3a29e001c52a2f2243.
* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* L: notes/research_complete_longitude_sign_and_marked_derivative.md,
  SHA256 7b8d3fe68cfb360e7074ee5f03f18be5dc8b1b93da4b4c39649911de705bff32.

All five complete directs were read nontruncated in this active
sequence, and every used implication was checked. The proof uses
written algebra and logarithmic differentiation only. Frozen and
public files were not changed.
