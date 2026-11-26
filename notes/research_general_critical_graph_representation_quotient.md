# The general critical graph and the highest-cut representation quotient

Private written proof, 18 November 2026.

At any simple Alexander zero, the actual principal stationary
equations have an exact local reduction with the original highest
cut. Their diagonal gauge quotient consists of the abelian curve
and one smooth attached curve. The latter is the source critical
graph and parametrizes irreducible characters off the intersection.
No nonzero quadratic soft coefficient is assumed.

The meridian on that curve is either nonconstant, with a finite
ramification order, or identically equal to the Alexander root.
The proof identifies this alternative; it does not rule out the
second case for every knot.

## 1. Actual analytic data without a quadratic hypothesis

Use the one-component highest-cut source of [G], with
\(Y=x_0^2\), a simple Alexander zero \(\alpha\ne0,1\), and
\(z=Y-\alpha\). All coordinates are on the fixed local square-root
chart for \(x_0\). Retain
\[
 T_0=\operatorname{diag}(0,1,\ldots,1),\quad
 L=L_\beta(x_0),\quad B=LT_0,\quad K=I-B .
 \tag{1}
\]
The source has the holomorphic relative-word principal phase
\(\mathcal P(z,Z,P)\), balanced in its creation and momentum
fields and of field degree at least four. Its exact covariance
decomposition is
\[
 C=B(I-B)^{-1}=\frac{uv^T}{z}+G(z),\qquad uv^T\ne0,
 \tag{2}
\]
with constant residue factors \(u,v\) and holomorphic \(G\).
These statements require only the literal finite word and the
simple determinant zero. Their applicability without a quadratic
soft assumption is checked explicitly in [G, Sections 1--2].

The regular hard equations have the unique small analytic solution
\[
 Z=va+G^T\mathcal P_P,\qquad
 P=ub+G\mathcal P_Z .
 \tag{3}
\]
Their effective principal phase is \(\Psi(z,x)\), \(x=ab\), with
\[
 \Psi(z,x)=O(x^2),\qquad
 \Psi_a=v^T\mathcal P_Z,\qquad
 \Psi_b=u^T\mathcal P_P .
 \tag{4}
\]
The derivatives on the right are evaluated at (3). These are the
analytic hard implicit and envelope identities of [R], applied
to the general analytic source of [G]. Their proofs precede and
do not use any nonvanishing assertion about \([x^2]\Psi(0,x)\).
The independent stage marks can be retained throughout and set to
zero after differentiation, as in those sources.

Put
\[
                 F(z,x)=z-\Psi_x(z,x).
 \tag{5}
\]
The following assertions concern the original local field chart,
including its zero-coordinate faces:

1. The full highest-cut stationary ideal is analytically equivalent
   to regular hard coordinates equal to zero and
   \(aF(z,ab)=bF(z,ab)=0\).
2. Its diagonal gauge invariant ring is exactly
   \[
                         \mathbb C\{z,x\}/(xF(z,x)).
                         \tag{6}
   \]
   This is also the local character quotient in the regular
   Gauss chart with the cut eigenvalues and highest eigenline fixed.
3. The attached curve \(F=0\) is a smooth graph \(z=\zeta(x)\).
   Every point with \(x\ne0\) gives an irreducible knot
   representation. Its character has \(x\) as a local analytic
   parameter.
4. If \(\Psi(0,x)\) has finite order \(p+1\), the meridian map
   has ramification order \(p\). If \(\Psi(0,x)\equiv0\), the
   attached character curve is instead vertical: \(Y\equiv\alpha\).

No assertion of quantum-minor selection, preferred longitude,
hyperbolic identification, or physical-cycle occurrence is used
in proving these statements.

## 2. Exact stationary reduction across the singular meridian

First record a linear algebra consequence of the actual residue.
The simple zero of \(\det K\) implies
\[
 \ker K(0)=\mathbb C u,\qquad
 \ker K(0)^T=\mathbb C v .
 \tag{7}
\]
Both kernels have dimension one: otherwise the adjugate, hence
the determinant derivative, would vanish. Define analytic vectors
\[
                   A(z)=\frac{K(z)u}{z},\qquad
                   D(z)=\frac{K(z)^Tv}{z}.
 \tag{8}
\]
Their apparent divisions are removable by (7).
Multiplying (2) on either side by \(K\) gives
\[
 KG=B-Av^T,\qquad K^TG^T=B^T-Du^T.
 \tag{9}
\]
Since \(v^TB(0)=v^T\), the first identity at zero implies
\[
                         v^TA(0)=1.
 \tag{10}
\]
Similarly \(u^TD(0)=1\). These normalizations follow from the
residue itself; no condition \(v^Tu\ne0\) is needed.

The coherent stationary equations with the original cut are, by
the direct generating-function calculation in [R, (14)--(16)],
\[
               KP-B\mathcal P_Z=0,\qquad
               K^TZ-B^T\mathcal P_P=0 .
 \tag{11}
\]
They include the highest input \(p_1=0\), highest output
\(Z_1=0\), and closure of both fields on strands \(2,\ldots,b\),
where the original input momentum is \(p=L^{-1}P\).

Make the analytic change of field coordinates
\[
             q_P=P-G\mathcal P_Z,\qquad
             q_Z=Z-G^T\mathcal P_P .
 \tag{12}
\]
Its field Jacobian is the identity at zero, for every small \(z\),
because \(\mathcal P\) is quartic. Choose fixed linear forms
\(\ell_u u=\ell_v v=1\), and decompose
\[
 q_P=ub+p_\perp,\quad \ell_u p_\perp=0,\qquad
 q_Z=va+q_\perp,\quad \ell_v q_\perp=0.
 \tag{13}
\]
Using (9), the first residual in (11) is exactly
\[
       Kp_\perp-A\bigl(v^T\mathcal P_Z-zb\bigr).
 \tag{14}
\]
The linear map
\[
 (p_\perp,t)\longmapsto K(z)p_\perp-A(z)t
 \tag{15}
\]
is invertible on a fixed neighborhood of \(z=0\). At zero,
\(K(0)\) maps \(\ker\ell_u\) isomorphically onto
\(\ker v^T\), and (10) makes its last column transverse to
that image. Its determinant remains a unit after shrinking.
The transpose residual similarly becomes
\[
       K^Tq_\perp-D\bigl(u^T\mathcal P_P-za\bigr),
 \tag{16}
\]
with an invertible coefficient matrix.

Consequently (11), as an ideal of convergent analytic germs, is
equivalent to
\[
 p_\perp=q_\perp=0,\qquad
 v^T\mathcal P_Z=zb,\qquad u^T\mathcal P_P=za.
 \tag{17}
\]
The first equations are exactly the hard equations (3). Their
analytic elimination and the envelope identities (4) reduce the
last two to
\[
                          bF(z,ab)=aF(z,ab)=0.
 \tag{18}
\]
Thus the reduction is valid at \(z=0\) as well as away from it.
It deletes no equation by division by an occupation or by \(z\).

Balancedness also sharpens the reconstruction to
\[
             Z=a\,\mathcal Z(z,x),\qquad
             P=b\,\mathcal Q(z,x),\qquad x=ab,
 \tag{19}
\]
where
\(\mathcal Z(z,0)=v\) and \(\mathcal Q(z,0)=u\).
Indeed a weight-one analytic monomial is \(a(ab)^j\), and a
weight-minus-one monomial is \(b(ab)^j\). At \(b=0\) or \(a=0\),
the quartic balanced gradients in (3) vanish in the required
component, giving the displayed values. These identities prove
that both reconstructed field vectors are nonzero whenever
\(ab\ne0\) and the coordinates are sufficiently small.

## 3. Full local representation correspondence with the cut retained

We recall exactly which part of [R] is used. For each strand,
\[
 t=ZP,\quad K_{\rm str}=x_0e^{-t},\quad
 f=Z,\quad e=P\,\frac{(1-e^t)(1-Ye^{-t})}{x_0t}.
 \tag{20}
\]
The final quotient is its analytic extension at \(t=0\), a unit
there. It gives a local analytic chart on
\[
 K_{\rm str}+K_{\rm str}^{-1}+ef=x_0+x_0^{-1}.
 \tag{21}
\]
The two literal signed kernel maps are exactly the Gauss
crossing maps of [R, (10)--(13)] throughout this chart.
Their only displayed denominators are units near the abelian
point. This calculation uses no soft quadratic coefficient.

Write
\[
 b_+=\begin{pmatrix}K_{\rm str}&e\\0&1\end{pmatrix},\qquad
 b_-=\begin{pmatrix}1&0\\-K_{\rm str}f&K_{\rm str}\end{pmatrix},
 \qquad G_{\rm str}=b_-^{-1}b_+ .
 \tag{22}
\]
Every signed crossing conserves the same two ordered products
of \(b_+\) and \(b_-\). For a solution of (11), all noncut
fields close. Canceling their identical invertible matrix factors
forces the cut matrices to agree as well. The original vacuum
conditions then give all four cut field values zero, and
\[
                      G_{\rm str,1}
                         =\operatorname{diag}(x_0,x_0^{-1}).
 \tag{23}
\]
As in [R], this is an identity using the two vacuum conditions,
not scalarity or an averaged boundary functional. The same
argument works modulo the stationary ideal: matrix differences
of the noncut factors lie in that ideal, and every cancellation
uses an analytic unit. Thus the additional cut closure equations
do not change the ideal.

With \(B_{-,j}=b_{-,j}\cdots b_{-,1}\), set
\[
                 H_j=B_{-,j-1}^{-1}G_{\rm str,j}B_{-,j-1}.
 \tag{24}
\]
The elementary triangular identities give the Hurwitz braid
action on these \(H_j\). Full closure therefore gives the
original knot-group representation, with actual meridians
\(\mu_j=-H_j\) in the convention of [R].

Conversely, start with a representation sufficiently close to
the diagonal abelian one, and fix its first meridian to
\(-\operatorname{diag}(x_0,x_0^{-1})\) with the same eigenline.
Such a diagonalization is locally possible because the two
eigenvalues are distinct. Put
\[
                 P_j=H_j\cdots H_1,\qquad P_0=I .
 \tag{25}
\]
All \((P_j)_{11}\) are units near the abelian point. Their regular
Gauss factors are explicitly
\[
 B_-(P_j)=
 \begin{pmatrix}1&0\\-(P_j)_{21}&(P_j)_{11}\end{pmatrix},
 \quad
 B_+(P_j)=
 \begin{pmatrix}(P_j)_{11}&(P_j)_{12}\\0&1\end{pmatrix},
 \quad P_j=B_-(P_j)^{-1}B_+(P_j).
 \tag{26}
\]
Consecutive quotients recover each \(b_{\pm,j}\).
The local crossing identities intertwine this inverse with the
braid relations, so the reconstructed Gauss fields are a fixed
point of the original signed word. The local chart (20) then
recovers the unique coherent fields. Their full closure and
diagonal cut imply precisely (11). This proves the local converse
by explicit maps and units, not by dimension counting.

If \(x=ab\ne0\), (19) makes both the input creation vector and
the input momentum vector nonzero. Any common invariant line
must be one of the two cut eigenlines. Preservation of the second
line forces every \(e_j=0\), hence all momenta zero. Preservation
of the first line inductively forces every \(f_j=0\), using the
lower triangular prefixes in (24), hence all creation fields
zero. Both are impossible. These representations are irreducible.

## 4. The exact quotient and a separating character coordinate

The remaining conjugations fixing the diagonal cut and its ordered
eigenline are diagonal. On the coherent fields and soft coordinates
their effective action is
\[
 (Z,P)\mapsto(\lambda Z,\lambda^{-1}P),\qquad
                      (a,b)\mapsto(\lambda a,\lambda^{-1}b).
 \tag{27}
\]
The invariant analytic series are exactly the series in \(z,x=ab\).
The weight-zero part of the ideal \((aF,bF)\) is exactly \((xF)\).
To see the nontrivial inclusion, project a representation
\(aF g+bF h\) to weight zero. The required weight-minus-one
part of \(g\) is \(b g_0(z,x)\), and the weight-one part of \(h\)
is \(a h_0(z,x)\). Their result is
\(xF(g_0+h_0)\). Weight extraction preserves convergence on
smaller disks, for example by averaging the diagonal unit-circle
action. This proves (6) as an analytic local-ring identity.

There is an explicit trace coordinate detecting \(x\), so the
quotient is a character quotient, not only a field-orbit notation.
At the initial strand section, (19) and \(p=L^{-1}P\) give
\[
 e_i f_j
   =x\left[(x_0-x_0^{-1})(L^{-1}u)_i v_j+O(x)\right].
 \tag{28}
\]
Choose \(i,j\) for which the coefficient at \(z=0\) is nonzero.
Such a choice exists because \(L\) is invertible and \(u,v\)
are nonzero. Neither index needs to be the cut: from
\(B(0)u=u\) and \(v^TB(0)=v^T\), both
\((L(0)^{-1}u)_1\) and \(v_1\) are zero.

Here is a direct expression of (28) in character data. Let
\(\Pi_\pm\) be the spectral projectors of \(H_1\), explicitly
\[
             \Pi_+=\frac{H_1-x_0^{-1}I}{x_0-x_0^{-1}},
                         \qquad \Pi_-=I-\Pi_+ .
 \tag{29}
\]
Write \(a_j=(P_j)_{11}\), \(b_j=(P_j)_{12}\),
\(c_j=(P_j)_{21}\). Equation (26) gives
\[
 K_j=a_j/a_{j-1},\qquad
 e_j=b_j-K_jb_{j-1},\qquad
 f_j=c_j/K_j-c_{j-1}.
 \tag{30}
\]
Every \(a_j=\operatorname{tr}(\Pi_+P_j)\), while
\[
                  b_i c_j
                    =\operatorname{tr}(\Pi_+P_i\Pi_-P_j).
 \tag{31}
\]
Thus \(e_i f_j\) is a rational expression in traces of group
words and the chosen \(x_0\), with unit denominators.
Locally \(x_0\) itself is determined analytically by the meridian
trace, since the derivative of \(x_0+x_0^{-1}\) with respect
to \(Y=x_0^2\) is nonzero at \(\alpha\ne1\).

After division by the nonzero constant in (28), this trace
function is \(\chi(z,x)=x+O(zx,x^2)\).
The change \((z,x)\mapsto(z,\chi)\) is analytically invertible.
Conversely every word trace is a gauge-invariant analytic
function of \(z,a,b\), hence a function of \(z,x\).
These explicit functions identify the quotient (6) with the
local character germ of the regular cut-diagonal representation
chart. In particular different nearby nonzero \(x\) points on
the attached curve have different characters.

## 5. Smooth critical graph, finite ramification, and the vertical case

By (4)--(5),
\[
       F(z,0)=z,\qquad F_z(0,0)=1.
 \tag{32}
\]
Hence \(F=0\) is one smooth analytic graph \(z=\zeta(x)\).
The two factors \(x\) and \(F\) in (6) meet transversely at
the origin. The component \(x=0\) is the abelian character
curve; the component \(F=0\) is the attached curve, irreducible
as a curve and consisting of irreducible representations at
its points \(x\ne0\).

Suppose
\[
               \Psi(0,x)=\tau x^{p+1}+O(x^{p+2}),
                     \qquad p\ge1,\quad\tau\ne0.
 \tag{33}
\]
Then
\[
                   \zeta(x)=(p+1)\tau x^p+O(x^{p+1}).
 \tag{34}
\]
Indeed the remaining meridian-dependent terms in \(\Psi\) are
\(O(zx^2)\), so the equation \(z=\Psi_x\) has the stated first
coefficient. Taking a holomorphic \(p\)-th root of the unit
factor in (34) gives a coordinate \(s\) with \(z=s^p\).
Equivalently, over this ramification there are precisely \(p\)
branches
\[
 x_j(s)=\lambda_j s+O(s^2),\qquad
                  (p+1)\tau\lambda_j^p=1 .
 \tag{35}
\]
Their characters are analytic in \(s\), and are distinct over
each sufficiently small nonzero \(z\), by the coordinate (28).
The balanced representatives \(a=b=\sqrt{x_j(s)}\) are analytic
after one further square-root cover and limit to the diagonal
abelian representation; their sign change is diagonal conjugation.

One can alternatively obtain representatives analytic in \(x\)
without that further cover: fix any sufficiently small
\(a=a_*\ne0\), and set \(b=x/a_*\).
Equations (19), with \(z=\zeta(x)\), then give analytic
representatives whose limit at \(x=0\) is a triangular reducible
representation. Their characters are the same as those of the
balanced representatives. This is a gauge choice on the actual
local critical set, not a change of the source cut.

Finally,
\[
 \Psi(0,x)\equiv0
 \quad\Longleftrightarrow\quad
 F(0,x)\equiv0
 \quad\Longleftrightarrow\quad
                         \zeta(x)\equiv0.
 \tag{36}
\]
The first equivalence uses \(\Psi(0,0)=0\), and the second uses
uniqueness of the graph. In this case the same construction
gives a nonconstant irreducible character family at the fixed
meridian \(Y=\alpha\); nonconstancy follows from (28), even
though the meridian is constant.

Thus the finite-order condition (33) is exactly nonconstancy
of the meridian function on this actual attached character germ.
No calculation above forces it. The simple determinant, regular
field chart, conserved products, and transverse two-curve
quotient remain compatible with \(\zeta\equiv0\).
Excluding that case would require an additional theorem about
the meridian fibre of this representation branch. It is not
an automatic consequence of corank one or of the local group
relations proved here.

## 6. Marks, scope, and complete proof directs

All original stage marks remain analytic parameters in the
principal construction. At a critical point with \(x\ne0\),
the same envelope calculation as [R, (28)] identifies
\(\partial_{\mathbf t}\Psi\) with its actual stage occupations.
Their prescribed linear combinations give every original clock.
The finite-order discussion makes no deletion of zero-valued
occupations and no change to the vacuum rows.

This note supplies a local algebraic class criterion in the
representation chart. It does not prove that the meridian is
nonconstant for every knot, create a seed when \(\Delta=1\),
identify a hyperbolic component or preferred longitude, or
establish a physical-cycle coefficient. Any separate Borel
reconstruction or minor identification retains its own source
and continuation requirements.

| Label | Complete proof source | SHA256 |
|---|---|---|
| G | notes/research_actual_borel_phase_surface.md | ba682a18ac0ae3efa05ffbc7e6fef02c128800ccbbffda1867756ba5a8275429 |
| R | notes/research_principal_critical_highest_cut_representation.md | d77b2193d34c0e174389cfdf3d52e34f6ab59f61f2d5263842b65a6769e7d9d4 |

G supplies the general analytic source, balanced hard phase and
simple determinant residue without a soft quadratic hypothesis.
R supplies the literal local field maps, source stationary
equations, triangular conservation and meridian conventions.
Only the displayed algebraic and analytic constructions from R
are used, not its former restriction for constructing a particular
quadratic critical branch. The analytic ideal reduction, complete
local converse, invariant ring, trace coordinate and vertical
equivalence are proved above.

Only written mathematics, source reads and hash checks were used.
Frozen notes and public manuscripts are unchanged.
