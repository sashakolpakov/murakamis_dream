# Rivin crossing frames, exact seams, and fused bridge angle volumes

Written derivation, 14 November 2026. The external matrices are those of
[rivin-jones at e956fb919ac7d1bbc7cb3d3873fbac993feb94b7](https://github.com/igorrivin/rivin-jones/tree/e956fb919ac7d1bbc7cb3d3873fbac993feb94b7),
`docs/MATHEMATICS.md` and `python/rivin_jones/r_matrix.py`. Only their
displayed formulas were read; no code was executed or imported.

Each literal signed crossing has a direct two-cell positive angle
half-density after an explicit change of its four boundary frames. The
frames depend on whether the strand passes over or under. Their seams
are part of the exact arbitrary-word identity. The existing coherent
overbridge contraction then gives a useful fused form: its complete
factorial magnitude is one angle-simplex weight, including the clock
factor that would otherwise be mistaken for a harmless phase. On an
explicit positive chamber its action is the volume of an ideal
bipyramid. None of these statements removes the actual phase or proves
survival of the original geometric scalar.

## 1. Both literal crossing signs in one notation

Put
\[
 d=N-1,\qquad q=e^{\pi i/N},\quad A=e^{-\pi i/(2N)},\qquad
 S_a=\prod_{j=1}^a2\sin(\pi j/N),\quad S_0=1.
\]
Every displayed index lies between zero and \(d\). Write \(I\) for the
overstrand input and \(J\) for the understrand input. Their outputs are
\(I-k\) and \(J+k\), respectively, where
\[
 0\le k\le\min(I,d-J).                                      \tag{1}
\]
For the positive crossing these are the external input indices
\((i,j)=(I,J)\); for the negative crossing they are \((i,j)=(J,I)\).
The checked outputs are in the order specified in the external source.
The exact coefficient for either sign is
\[
 R_\sigma(I,J;k)=A^{Q_\sigma(I,J,k)}
             \frac{S_I S_{J+k}}{S_{I-k}S_J S_k},             \tag{2}
\]
with
\[
 \begin{split}
 Q_+&=(d-2I+2k)(d-2J-2k)+k(k-1)+Nk,\\
 Q_-&=-(d-2I)(d-2J)-k(k-1)-Nk.
 \end{split}                                                \tag{3}
\]
Indeed the symmetric Gaussian binomial at this root is its positive
sine-factorial quotient. The positive product in the external formula
contributes \((-i)^kS_I/S_{I-k}=A^{Nk}S_I/S_{I-k}\); the negative
product and its printed sign contribute \(i^kS_I/S_{I-k}=A^{-Nk}S_I/S_{I-k}\).
This verifies (2)--(3), including both parity conventions.

The exact external-to-physical adapter in
[the local crossing theorem](research_rivin_jones_local_crossing_adapter.md)
reverses crossing sign at this choice of \(A\). Equation (2) uses the
external signs throughout; it does not silently relabel them physical.

## 2. A direct two-cell half-density

Define positive port frames
\[
 g_\epsilon(a)=\left(\frac{S_a}{\sqrt N}\right)^{\epsilon/2},
 \qquad \epsilon=+1\text{ on an overstrand},\quad
 \epsilon=-1\text{ on an understrand}.                     \tag{4}
\]
The output port keeps its strand's role at that crossing. Let
\(\widehat R_\sigma=G_{\rm out}R_\sigma G_{\rm in}^{-1}\), with the
tensor products of these diagonal frames in the actual port order.
Put
\[
 w_N(a,b,c)=\frac1{S_aS_bS_c},\qquad a+b+c=d.
\]
Then the complete entry is exactly
\[
 \boxed{\quad
 \widehat R_\sigma(I,J;k)=A^{Q_\sigma(I,J,k)}N
   \sqrt{w_N(k,I-k,d-I)\,w_N(k,J,d-J-k)}.
 \quad}                                                    \tag{5}
\]
The square root is positive real; the full original phase is outside it.

To prove (5), the squared frame ratio is
\(S_{I-k}S_J/(S_I S_{J+k})\). Multiplying it by the squared magnitude
in (2) gives
\[
 \frac{S_I}{S_kS_{I-k}}\frac{S_{J+k}}{S_kS_J}.
\]
Root reflection \(S_aS_{d-a}=N\) converts this expression to the
square of the magnitude in (5). The frames are positive, so the phase
in (3) is unchanged. The proof includes all zero-transfer and endpoint
entries; no additional internal summation variable has been introduced.

The two triples in (5) have a shared first entry. Conversely two
nonnegative sum-\(d\) triples with a shared first entry determine
exactly one admissible \((I,J,k)\). Thus this is an actual local
charge correspondence, not independent angles assigned after a sum.

For the limiting interior coordinates \((u,v,t)=(I/N,J/N,k/N)\),
write
\[
 \begin{split}
 \mathcal V_1&=V(\pi t,\pi(u-t),\pi(1-u)),\\
 \mathcal V_2&=V(\pi t,\pi v,\pi(1-v-t)),\qquad
 V(\alpha,\beta,\gamma)=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma),
 \end{split}
\]
where \(\alpha+\beta+\gamma=\pi\) and
\(\Lambda'(\theta)=-\log(2\sin\theta)\), \(\Lambda(0)=0\).
The uniform sine-factorial estimate proved in
[the complete crossing norm calculation](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/weighted_crossing_source_gap.md),
Section 2, gives
\[
 \frac{2\pi}{N}\log|\widehat R_\sigma|
       =\mathcal V_1+\mathcal V_2+O(\log N/N).              \tag{6}
\]
At finite level one can use the exact positive angles
\(\pi(a+1/3)/N\) for each triple in (5); they sum to \(\pi\), and
the same error estimate holds. The limiting action in (6) is strictly
concave on \(0<t<u<1\), \(0<v<1-t\). For
\(\gamma=\pi-\alpha-\beta\), the negative Hessian of \(V\) is
\(\left(\begin{smallmatrix}\cot\alpha+\cot\gamma&\cot\gamma\\
\cot\gamma&\cot\beta+\cot\gamma\end{smallmatrix}\right)\).
Its determinant is one and its first diagonal entry is
\(\sin\beta/(\sin\alpha\sin\gamma)>0\). Hence each tetrahedral
volume has negative definite Hessian on its angle plane. The joint affine map
from \((u,v,t)\) to the two triples is injective. Therefore a nonzero
variation cannot lie in both Hessian kernels.

This uses two cells for a whole crossing, compared with the six cells
from the three fusion factors in
[the reassociation angle kernel](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_reassociation_angle_kernel.md),
Section 6. The price is that (4) is a role-dependent port frame,
whereas that earlier theorem uses one fixed physical frame. This price
must be retained in the next section.

## 3. The exact seams and the complete source

On an internal strand segment of color \(a\), let \(\epsilon\) be its
role at the preceding output and \(\epsilon'\) its role at the next
input. The required diagonal connector is
\[
 H_{\epsilon',\epsilon}(a)
  =g_{\epsilon'}(a)g_\epsilon(a)^{-1}
  =\left(\frac{S_a}{\sqrt N}\right)^{(\epsilon'-\epsilon)/2}.
                                                               \tag{7}
\]
It is one for equal roles and is \(S_a/\sqrt N\) or its reciprocal
for a role switch. These are generally exponential weights.

For example, for consecutive complete operators,
\[
 R_m\cdots R_1
  =G_{{\rm out},m}^{-1}\widehat R_m
    (G_{{\rm in},m}G_{{\rm out},m-1}^{-1})\widehat R_{m-1}
       \cdots\widehat R_1G_{{\rm in},1}.                  \tag{8}
\]
Spectator frames are simply transported along their unchanged wires.
Equation (8) is an equality of full matrices and therefore holds in an
arbitrary exterior. Every original source vector is multiplied by its
input frame and every original output row by its inverse output frame.
An ordinary turn is transported by that same tensor rule. In particular
\(g_\epsilon(a)g_\epsilon(d-a)=1\); two equally framed complementary
legs fix their ordinary cup or cap pointwise. Unequal frames have their
explicit remaining factor and are not declared source-fixing.

For the external closed-braid prescription the quantum trace is
diagonal, so its weight commutes with (7); the closing connector stays
in the traced matrix element. The original highest-weight pin remains
the index zero. Its possible endpoint-frame ratio is a power of \(N\),
because \(g_\epsilon(0)=N^{-\epsilon/4}\). The writhe correction is
unchanged. Thus (8), including closing seams, computes the prescribed
original scalar for every fixed signed braid word. The full boundary
adapter and [split-incidence theorem](research_rivin_jones_split_boundary_source_equivalence.md)
transport the same equality to
the original tangle source; this does not replace a full pair module
by its semisimple spectrum or discard its Hermite normals.

The seam action is also explicit. With \(x=a/N\), uniformly in \(a\),
\[
 \frac{2\pi}{N}\log H_{\epsilon',\epsilon}(a)
   =-(\epsilon'-\epsilon)\Lambda(\pi x)+O(\log N/N).       \tag{9}
\]
Consequently the whole physical-state expansion has the sum of the
two-cell actions (6), plus all terms (9) and the transported source
action. The phase is exactly the sum of (3), the original pivot phases
and writhe phase. Positive frame changes have not altered it. Strict
concavity of an isolated two-cell expression alone says nothing about
the Hessian after the seam terms are restored.

## 4. Coherent bridge fusion absorbs the factorial bookkeeping

There is a source-exact way to combine these weights, rather than
discard the seams. First undo the displayed port frames algebraically
in (8), then apply the finite Fourier transformations and exact signed
overbridge contraction of
[the bridge theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_signed_overbridge_unwinding.md) and
[the whole charged-source theorem](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_global_charged_bridge_flow.md).
These are equalities of the original source. Their Fourier clocks are
new summation coordinates; no termwise identification with the physical
colors of (2) is asserted.

For a bridge with \(m\ge1\) encounters, put \(r=m+1\) and use its
monotone clocks \(d\ge h_1\ge\cdots\ge h_m\ge0\). Its block lengths are
\[
 L_0=d-h_1,\quad L_j=h_j-h_{j+1}\ (1\le j<m),\quad L_m=h_m,
 \qquad \sum_{j=0}^mL_j=d.                              \tag{10}
\]
The exact bridge numerator is \(\Gamma_e\) times \(r\) homogeneous
root-interval blocks. All its phase factors are prescribed in the
whole charged-source theorem, equations (4), (6), (8)--(9). In
particular
\[
 |\Gamma_e|=\frac{S_{h_1}}{S_{h_m}\prod_{j<m}S_{h_j-h_{j+1}}}
             =\frac{N}{\prod_{j=0}^mS_{L_j}}.            \tag{11}
\]
Expand each block with head charge \(t_j\), \(0\le t_j\le L_j\).
Its coefficient magnitude is \(S_{L_j}/(S_{t_j}S_{L_j-t_j})\).
Therefore the complete magnitude, including the clock factor, is
\[
 \boxed{\quad
 |\Gamma_e|\prod_{j=0}^m\frac{S_{L_j}}{S_{t_j}S_{L_j-t_j}}
     =\frac{N}{\prod_{j=0}^m S_{t_j}S_{L_j-t_j}}.
 \quad}                                                   \tag{12}
\]
This cancellation includes every zero-length block. It is valid for
arbitrary sign patterns along the bridge.

The phase in (12) has not disappeared. If a block is
\(\prod_{a<L}(\alpha X-Q^a\beta Y)\), its head-charge coefficient is
exactly
\[
 \alpha^L\frac{S_L}{S_tS_{L-t}}
       \bigl[-(\beta/\alpha)q^{L-1}\bigr]^t.              \tag{13}
\]
At the complete source \(\alpha,\beta\) are specified unit phases.
Thus the complete bridge phase is
\(\Gamma_e/|\Gamma_e|\) times the product of (13)'s unit factors.
Anchor charges, closure adapters and their pivots are still exactly
those of the whole charged-source theorem. For any specified complete
choice of block charges, (12)--(13) give its actual complex weight;
when several choices produce the same monomial they must still be
summed coherently. The cancellation of factorials is not cancellation
of the phase character.

Writing the \(2r\) halfedge charges as
\(a_{j,0}=L_j-t_j\), \(a_{j,1}=t_j\), one has \(\sum a=d\).
For \(x_a=a/N\), the limiting bridge action is
\[
 \mathcal B(x)=2\sum_{a=1}^{2r}\Lambda(\pi x_a),
 \qquad x_a>0,\quad\sum_a x_a=1.                         \tag{14}
\]
Indeed \((2\pi/N)\log\) of (12) equals (14) up to
\(O_m(\log N/N)\), uniformly up to the closed simplex. The shift
\(x_a=(a+1/(2r))/N\) makes the simplex equation exact at finite level
with the same error.

## 5. Genuine local geometry and its precise limit

The function (14) is strictly concave on its open simplex. An explicit
tetrahedral decomposition proves this without an assumed global angle
incidence. For \(n=2r\), \(s_j=x_1+\cdots+x_j\),
\[
 \sum_{a=1}^n\Lambda(\pi x_a)
   =\sum_{j=2}^{n-1}V(\pi s_{j-1},\pi x_j,\pi(1-s_j)).     \tag{15}
\]
The equality telescopes using \(\Lambda(\pi-y)=-\Lambda(y)\).
Every triple is positive. The map of simplex tangent spaces into all
these triangle tangent spaces is injective: the first triangle fixes
the variations of \(x_1,x_2\), then each next triangle fixes the next
variation. Strict concavity of tetrahedral volume proves the assertion.

On the smaller chamber \(x_a<1/2\) for every \(a\), (14) is literally
the volume of a convex ideal cyclic \(n\)-gonal bipyramid. In the sphere
at infinity put its two apices at \(0,\infty\), and its equatorial
vertices successively on the unit circle with angle gaps \(2\pi x_a\).
Every gap is less than \(\pi\), so the center belongs to the interior
of the equatorial polygon. In the Klein ball the convex hull is the
two pyramids on this polygon; the central axis and its successive
equatorial edges subdivide it into nonoverlapping ideal tetrahedra.
The tetrahedron at gap \(2\pi x_a\) has dihedral angle triple
\[
 (2\pi x_a,\ \pi/2-\pi x_a,\ \pi/2-\pi x_a).
\]
Its volume is \(2\Lambda(\pi x_a)\), by the Lobachevsky duplication
identity, which also follows by differentiating both sides and fixing
the value at zero. Summing proves (14)'s geometric assertion. Outside
that chamber, (14)--(15) remain strictly concave positive-tetrahedron
identities, but the central-axis bipyramid subdivision just described
is not a positive subdivision and is not claimed as one.

The actual anchor equations linearly couple the halfedge charges of
different bridges. They have not here been identified with the edge
and peripheral angle equations of the desired hyperbolic complement.
Nor does a maximum of (14) remove the phase (13), select a complex
critical point, or prove its nonzero coefficient under the prescribed
closing. What is established is a direct literal-crossing angle
half-density, its exact arbitrary-source seams, and their source-exact
coherent fusion into an explicit geometric local volume functional.
The earlier reciprocal raw-Psi chart obstruction does not apply to
these coefficient identities; no replacement of that off-grid density
or its relative cycle has been made.
