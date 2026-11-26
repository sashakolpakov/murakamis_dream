# The actual reduced braid operators and their pointed trace

Private written proof, 18 November 2026.

The first-meridian-jet source formula can be used with an explicit
finite braid representation. The reduced operator is not an
unspecified quotient: its generators are the original crossings
on the remaining factors and one triangular Euler operator.
The same source formula proves cyclicity on the actual
intertwiner algebra. No modified-trace theorem is imported.

The complete directs are C for the prefix quotient, H for its
scalar source kernel, E for the original crossing matrices, and
M for the marked Hurwitz convention. All additional generator,
cyclicity, stabilization and norm arguments are below.

## 1. The actual quotient and its algebra map

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\).
Keep \(q\) fixed and vary the common meridian \(M\) near one.
Write \(x=-M/q\) and \(f_a=\prod_{j=1}^a(1-Q^j)\), \(f_0=1\).
The original balanced factors have
\[
 K w_a=xQ^{-a}w_a,\qquad
 Fw_a=(1-Q^{a+1})w_{a+1}\quad(a<d),\qquad Fw_d=0.
 \tag{1}
\]
The lowering matrix has coefficient \(MQ^{-a}-M^{-1}\)
for \(a>0\), and its vacuum arrow is zero.

For \(m\) factors let \(F_{\rm r},K_{\rm r}\) be the ordered
coproducts on factors \(2,\ldots,m\). With the literal shift
\(L_1w_a=w_{a-1}\), \(L_1w_0=0\), C gives
\[
 S_m=\sum_{j=0}^{d}
       \frac{(x^{-1}L_1F_{\rm r})^j}{f_j},\qquad
 S_m^{-1}F_\Sigma S_m=F_1,\qquad [S_m,K_\Sigma]=0.
 \tag{2}
\]
Its inverse has coefficient
\((-1)^jQ^{j(j-1)/2}/f_j\) in degree \(j\).
For one factor use \(S_1=I\).

Let \(i_0v=w_0\otimes v\) and let \(p_0\) extract first
occupation zero. For an actual total intertwiner \(W\), C proves
\[
 S_m^{-1}WS_m=\sum_{n=0}^{d}F_1^n\otimes B_n(W).
 \tag{3}
\]
The constant coefficient is the exact finite matrix
\[
 \mathcal B_m(W):=B_0(W)=p_0S_m^{-1}Wi_0.
 \tag{4}
\]
Here \(S_mi_0=i_0\). Since positive powers of \(F_1\)
cannot contribute a constant term, (3) proves
\[
 \mathcal B_m(XY)=\mathcal B_m(X)\mathcal B_m(Y),\qquad
 \mathcal B_m(I)=I,\qquad
 [\mathcal B_m(W),K_{\rm r}]=0.
 \tag{5}
\]
An invertible total intertwiner has invertible image, with
inverse \(\mathcal B_m(W^{-1})\). All statements concern the
actual common-meridian family at the fixed quantum root.

## 2. Explicit braid generators

Assume \(m\ge2\). Let \(R_i\) be the original positive checked
crossing on factors \(i,i+1\), including its common Cartan
scalar \(\kappa\). E fixes the literal formula
\[
 R_i=\kappa\,\mathsf P_iD_i\Theta_i,\qquad
 (D_i)_{a,b}=x^{-a-b}Q^{ab},
 \tag{6}
\]
where the Euler transfer lowers the first input occupation.
The negative crossing is the actual inverse.
These crossings are total intertwiners at the fixed root
throughout the common-meridian family.

For \(i\ge2\), the crossing is internal to the remaining tensor.
It commutes with its ordered total \(F_{\rm r}\) and
\(K_{\rm r}\), hence with \(S_m\). It also commutes with
the exposed first-factor maps. Thus, with the remaining
positions relabelled \(1,\ldots,m-1\),
\[
                         \mathcal B_m(R_i)=R_{i-1}.
 \tag{7}
\]
The right side is precisely the original physical crossing
on those two remaining factors.

The crossing \(R_1\) has a different explicit image. On input
\(w_0\otimes w_b\otimes v\), its positive transfer is forced
to be zero, so
\[
 R_1(w_0\otimes w_b\otimes v)
      =\kappa x^{-b}w_b\otimes w_0\otimes v.
 \tag{8}
\]
In \(p_0S_m^{-1}\), only the degree-\(b\) term can then
reach the first row. Equation (4) gives
\[
 \mathcal B_m(R_1)(w_b\otimes v)
   =\kappa\frac{(-1)^bQ^{b(b-1)/2}x^{-2b}}{f_b}
                   F_{\rm r}^{\,b}(w_0\otimes v).
 \tag{9}
\]
C's finite prefix identity on the remaining \(m-1\) factors
is
\[
 S_{m-1}(w_b\otimes v)
                  =f_b^{-1}F_{\rm r}^{\,b}(w_0\otimes v).
 \tag{10}
\]
Consequently define the diagonal matrix on the first remaining
factor by
\[
 D_{\rm red}w_b=(-1)^bQ^{b(b-1)/2}x^{-2b}w_b
               =(-1)^bq^{b(b+1)}M^{-2b}w_b .
 \tag{11}
\]
The exact reduced generator is
\[
 \boxed{\quad
 \mathcal B_m(R_1)=\kappa S_{m-1}D_{\rm red},\qquad
 \mathcal B_m(R_1^{-1})
       =\kappa^{-1}D_{\rm red}^{-1}S_{m-1}^{-1}.
 \quad}
 \tag{12}
\]
For \(m=2\), \(S_{m-1}=I\). Every endpoint in (8)--(12)
is the actual finite endpoint. No cyclic wrap or infinite
series replaces it.

Equations (5), (7), and (12) give the original braid
relations on the remaining space: they are images of the
actual braid relations under an algebra map. They also
give \(\mathcal B_m(W_\beta)\) by a literal finite product.
All common crossing scalars and any separately prescribed
zero-framing line remain. First meridian derivatives follow
by the ordinary product rule for this finite product,
including derivatives of \(S_{m-1},D_{\rm red},\kappa\).
No condition-number bound for the triangular factor is asserted.

## 3. Cyclicity with the original pointed and pivotal source

The original highest-cut source is
\[
 \Phi_0(W)=\operatorname{Tr}
                     ((P_0\otimes K_{\rm r}^{1-N})W).
 \tag{13}
\]
H proves the exact meromorphic identity
\[
 \Phi_0(W)=\operatorname{Tr}_{\rm r}
       \left(\frac{D_N(M)}{D_N(MK_{\rm r})}\mathcal B_m(W)\right),
 \qquad D_N(z)=\frac{z^N-z^{-N}}{z-z^{-1}},
 \tag{14}
\]
with its prescribed removable continuation for an actual
analytic intertwiner. The fraction is a function of the
actual remaining Cartan, not a scalar Casimir choice.

For two such intertwiners \(X,Y\), their constant coefficients
commute with that function of \(K_{\rm r}\). On the generic
meridian set where its denominator is invertible, (5) and
the ordinary matrix trace therefore give
\[
                              \Phi_0(XY)=\Phi_0(YX).
 \tag{15}
\]
The two original finite source functions are analytic.
Thus (15) extends through completeness, as an equality
of their common-meridian germs. In particular
\[
                       \Phi_0(GWG^{-1})=\Phi_0(W)
 \tag{16}
\]
for an invertible actual total intertwiner \(G\).
This permits unmarked braid conjugation with the original
highest cut and tail pivot. Braid conjugation also preserves
the writhe, so its prescribed external zero-framing scalar
is unchanged. This conclusion does not apply to arbitrary
marked matrices failing the total intertwining equations.

## 4. A source bound on an actual meridian collar

Write \(B(M)=\mathcal B_m(W(M))\). H proves, in the original
remaining occupation norm,
\[
 |\Phi_0(W(1))|
   \le N^{m-1}\big(\|B(1)\|+m^{-1}\|B'(1)\|\big).
 \tag{17}
\]
Suppose the actual finite matrix \(B\) is analytic on a
neighborhood of \(|M-1|\le\eta/N\). Matrix Cauchy estimates
and the maximum principle give
\[
 |\Phi_0(W(1))|
 \le N^{m-1}\left(1+\frac{N}{m\eta}\right)
                   \sup_{|M-1|=\eta/N}\|B(M)\|.
 \tag{18}
\]
This is a polynomial cost at fixed \(m,\eta\). Every external
scalar line must still be included if the source convention
places it outside \(W\). Neither (17) nor (18) bounds the
actual reduced word. A large norm does not imply that its
specified trace functional is nonzero.

## 5. A regular semisimple total product after at most three stabilizations

There is a useful presentation choice for an irreducible complete
representation of the knot group. The tuple of its ordered
noncentral parabolic meridians is denoted \(H_1,\ldots,H_m\)
in M's sign convention, and \(P=H_m\cdots H_1\).
Positive Hurwitz motion sends an adjacent pair to
\[
 (H_i,H_{i+1})\longmapsto
                  (H_i^{-1}H_{i+1}H_i,H_i).
 \tag{19}
\]
It preserves \(P\). Applying positions \(j,j+1,\ldots,m-1\)
therefore moves a chosen \(H_j\) to the last position unchanged.
Conjugate the braid by that explicit Hurwitz word.

Append a new last meridian equal to the old last one, and
positively stabilize the braid. Its last crossing fixes this
equal pair, so the new tuple still satisfies every braid
fixed-point relation. Its total product is \(H_jP\).
Repeated stabilization on this last meridian gives \(H_j^tP\).
Topologically these are Markov stabilizations of the same knot.

If \(\operatorname{tr}(P)^2\ne4\), no change is needed.
If \(P\) is noncentral parabolic, write
\[
 P=\epsilon(I+A),\qquad H_j=\delta(I+B),\qquad
 A^2=B^2=0,\qquad \epsilon,\delta\in\{1,-1\}.
 \tag{20}
\]
Irreducibility supplies a meridian whose eigenline differs
from the unique eigenline of \(P\). For this choice
\(\operatorname{tr}(BA)\ne0\): in a basis making \(A\)
strictly upper triangular, the lower-left entry of \(B\)
is nonzero and computes this trace. Thus
\[
 \operatorname{tr}(H_j^tP)^2
               =(2+t\,\operatorname{tr}(BA))^2 .
 \tag{21}
\]
For a nonzero number \(c\), the two numbers \(2+c\)
and \(2+2c\) cannot both belong to \(\{2,-2\}\).
One or two positive stabilizations therefore make this
product regular semisimple. If \(P\) was central, a first
stabilization makes it noncentral parabolic; the preceding
argument then uses at most two more. The enlarged tuple
is still irreducible because it generates the same group.
This proves the bound of three.

For completeness the exact quantum scalar of each such
stabilization follows directly from (6), with no generic
modified-trace assumption. Put \(g=K^{1-N}\).
Integer-degree conservation makes
\(\operatorname{Tr}_2((I\otimes g)R_+)\) diagonal.
For its input occupation \(a\), set
\(t=Q^{1-a}x^2\). The literal finite crossing coefficients give
\[
 \begin{split}
 T_a={}&\kappa x^{1-N}x^{-2a}Q^{a(a-1)}
 \sum_{n=0}^a(-1)^nQ^{n(n-1)/2+(1-a)n}
                 {a\brack n}_Q(t;Q)_n .
 \end{split}
 \tag{22}
\]
The finite sum is \(t^a\). To check it, its coefficient
of \(t^k\), \(k<a\), is a nonzero scalar factor times
\((Q^{k+1-a};Q)_{a-k}\), which contains \(1-Q^0\).
This follows by expanding the products and using the
finite product expansion for the Gaussian coefficients.
Its leading coefficient is one. All products have length
at most \(a<N\), so no root denominator was inverted.
It follows that
\[
 \operatorname{Tr}_2((I\otimes g)R_+)
                     =\alpha I,\qquad
                    \alpha=\kappa x^{1-N}.
 \tag{23}
\]
The actual zero-framing compensation multiplies by
\(\alpha^{-1}\) when the positive writhe increases by one.
It consequently cancels exactly the scalar in (23).
Equivalently, define the normalized zero-framed raw braid
source by its prescribed factor \(\alpha^{-\mathrm{wr}(\beta)}\);
(23) verifies its positive Markov invariance directly.
Any separately retained modified-dimension line is unchanged.
Together with (16), these operations preserve the original
normalized root-meridian source, with its actual meridian germ.
This is not an off-root quantum-normal argument.

For the resulting regular semisimple \(P\), there is always an
eigenline different from the selected meridian flag. It supplies
a finite classical frame with \(P_{21}=0\). This statement
does not place every other shape in a common regular slit
chart or put the geometric point on the original integration
cycle. The stabilization lemma establishes presentation
regularity only.

## 6. Scope and complete proof-source pins

The reduction is exact on the root-quantum common-meridian
family. Quantum normals retain C's additional prefix row
\(J_N\); the root generator reduction is not differentiated
as an ordinary-color quantum-normal identity. No assertion
about a geometric integration cycle, source positivity,
or a surviving geometric contribution is made.

* C: notes/research_prefix_commutant_and_pointed_normal_functional.md,
  SHA256 b4fb801a1482316aebb4799f1d0b80d5b43ced39138d903c04cfde811ca166b0.
* H: notes/research_scalar_prefix_kernel_and_first_meridian_jet.md,
  SHA256 d7d82848a1b3f50709352905bafcc7ddfee36f41e434bf5de4663b4b6181dc9e.
* E: notes/research_actual_compressed_endpoint_euler_transition.md,
  SHA256 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16.
* M: notes/marked_braid_holonomy.md,
  SHA256 eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f.

All four complete directs were read nontruncated in this active
sequence and are retained unchanged. Every used implication was
checked. Only written mathematics and text/hash operations were used.
Frozen and public files were not changed.
