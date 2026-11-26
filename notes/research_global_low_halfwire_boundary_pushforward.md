# A global low-halfwire boundary pushforward of the original source

Private written proof, 17 November 2026.

Truncating a cardinal halfwire gives the low kernel as its wire residue.
Retaining the original radical matching unit restores the full kernel.
The difference between the full and corrected low halfwire models has an
explicit finite Laurent primitive, together with an ordinary physical-ideal
remainder. These primitives telescope on an arbitrary fixed network and
cancel on complete moving paired seams. Partial arcs retain their endpoint
currents. This is an exact finite-level source statement, not an estimate
for those partial currents or a geometric-cycle coefficient.

## 1. Cardinal halfwires and their constant modes

Fix \(N\ge2\), \(D=N-1\), \(m=\lfloor N/2\rfloor\), \(L=D-m\), and
\[
 P_N(z)=2T_N(z/2)+2,\qquad \mathcal A_N=\mathbb C[z]/(P_N),
 \qquad \phi(e_i e_j)=\delta_{i+j,D},\quad Te_j=e_{D-j}.
 \tag{1}
\]
The \(e_j\) are the original normalized Newton polynomials. No crossing
carrier or endpoint normal is changed. Source [E] supplies the literal
full cardinal representative
\[
 C_j(x)=\frac{\sin\pi N(x-j/N)}{N\sin\pi(x-j/N)},\qquad
 B(x,z)=\sum_{j=0}^D C_j(x)e_j(z).
 \tag{2}
\]
All apparent singularities of \(C_j\) are removable. Define ordinary
polynomial-valued halfwires before any deformation by
\[
 B_<(x,z)=\sum_{j=0}^{L}C_j(x)e_j(z),\qquad B_>=B-B_<,
 \quad K_<=\sum_{j\le L}e_j\otimes e_j,\quad
 H=\sum_{j>L}e_j\otimes e_j,\quad K=K_<+H.
 \tag{3}
\]
Here \(K\) is the original same-index turn kernel. At even levels the
low cutoff is \(L=m-1\); at odd levels it is \(L=m\).

Put \(w=e^{-2\pi ix}\). Each \(C_j\) has frequencies
\(\{-D/2,-D/2+1,\ldots,D/2\}\) and satisfies
\(C_j(x+1)=(-1)^D C_j(x)\). Every paired halfwire product is consequently
a single-valued Laurent polynomial in \(w\), with exponents from \(-D\)
to \(D\). Sampling at the \(N\) original points gives
\[
 [w^0](C_j C_k)=\frac1N\sum_{a=0}^{D}C_j(a/N)C_k(a/N)
                  =\frac{\delta_{jk}}N.
 \tag{4}
\]
The first equality is exact: no nonzero frequency of modulus at most
\(D<N\) is a multiple of \(N\). Thus the four products have constants
\[
 [w^0](B_<B_<)=K_</N,\quad [w^0](B_>B_>)=H/N,\quad
 [w^0](B_<B_>)=[w^0](B_>B_<)=0.
 \tag{5}
\]
These are ordinary polynomial identities at two independent angular
variables. They also hold after any prescribed identification of variables.

Since \(dx=-dw/(2\pi iw)\), a constant \(K_</N\) gives residue
\(-K_</(2\pi iN)\). The increasing original \(x\)-period is clockwise in
\(w\), so its integral is \(+K_</N\). The original wire factor \(N\)
restores \(K_<\), with this orientation and normalization.

## 2. The matching unit and the ordinary remainder

For double nodes \(c_a=2\cos((2a+1)\pi/N)\), \(0\le a<m\), use [M]:
\[
 \delta_a(z)=\frac{(-1)^D P_N(z)}{N^2(z-c_a)},\qquad
 G_{ab}=K_<(c_a,c_b),\quad W=G^{-1},\quad J_{ab}=W_{ab}/G_{ab}.
 \tag{6}
\]
The quotients in \(\delta_a\) are ordinary removable polynomials; the last
quotient is entrywise. The exact identities of [M] are
\[
 H=\sum_{a,b<m}W_{ab}\delta_a\otimes\delta_b,\qquad
 K=K_<(1+V),\quad V=\sum_{a,b<m}J_{ab}\delta_a\otimes\delta_b
 \quad\text{in }\mathcal A_N\otimes\mathcal A_N.
 \tag{7}
\]
They retain the mixed first normal. In particular \(V^2=0\) in that
algebra, not as an ordinary function of two free colors.

Take the displayed ordinary polynomial lift \(\widehat V\) of \(V\).
For a selected wire \(e=vv'\), set
\[
 A_e(w_e)=B(x_e,z_v)B(x_e,z_{v'}),\quad
 L_e(w_e)=B_<(x_e,z_v)B_<(x_e,z_{v'}),\quad
 Q_e=(1+\widehat V_e)L_e,\quad
 \mathcal R_e=K_e-(1+\widehat V_e)K_{<,e}.
 \tag{8}
\]
Equation (7) means precisely
\[
 \mathcal R_e\in(P_N(z_v),P_N(z_{v'})).
 \tag{9}
\]
It is not an ordinary zero at free colors. The notation \(Q_e\) denotes
the corrected low paired halfwire, not a new turn kernel.

Write \(A_e-Q_e=\sum_{k=-D}^{D}d_{e,k}w_e^{-k}\). By (5),
\(d_{e,0}=\mathcal R_e/N\). Define the explicit nonzero-mode primitive
\[
 \mathcal D_e(w_e)=\sum_{0<|k|\le D}
                         \frac{d_{e,k}}{2\pi i k}w_e^{-k}.
 \tag{10}
\]
Direct differentiation gives the ordinary identity
\[
 \boxed{\ (A_e-Q_e)\,dx_e
       =d_{x_e}\mathcal D_e+\frac{\mathcal R_e}{N}\,dx_e
       =d_{w_e}\mathcal D_e-
                    \frac{\mathcal R_e}{2\pi iN}\frac{dw_e}{w_e}.\ }
 \tag{11}
\]
In particular, reducing both angular variables in their full physical
algebras removes the last term and gives an exact transgression. The
corrected low residue is still \((1+V_e)K_{<,e}=K_e\). Neither the high
matching correction nor the ordinary ideal remainder has been discarded.

For an ordinary wire-dependent co-source \(a\), the same identity is
\[
 a(A_e-Q_e)dx_e=d_{x_e}(a\mathcal D_e)
       -\mathcal D_e\,d_{x_e}a+a\mathcal R_e\,dx_e/N.
 \tag{12}
\]
Thus even a periodic inserted wire observable can have a nonzero bulk
correction \(-\mathcal D_e\,d_{x_e}a\).

## 3. Ordered tensor transgression

Take any fixed finite collection of original same-index wires, ordered
\(1,\ldots,q\), with two distinct angular endpoints on each wire.
Parallel wires and shared angular vertices are allowed. Other factors
remain in the co-source. Let \(\nu(\mathbf z)\) be a closed meromorphic
top-degree form in all varying angular variables, on a domain avoiding
its poles; it may be the original product of trace differentials.
Free parameters are not differentiated or reduced. Put
\[
 \omega_0=dx_1\wedge\cdots\wedge dx_q\wedge\nu,\qquad
 T_e=\prod_{f<e}Q_f\prod_{f>e}A_f,
 \quad \widehat U=\prod_e(1+\widehat V_e),
 \tag{13}
\]
\[
 \Xi=\sum_e\mathcal D_eT_e\,\iota_{\partial/\partial x_e}\omega_0,
 \qquad \mathcal I=\sum_e\frac{\mathcal R_e}{N}T_e\,\omega_0.
 \tag{14}
\]
The global ordinary source identity is
\[
 \boxed{\quad
 \left(\prod_eA_e-\widehat U\prod_eL_e\right)\omega_0
                                      =d\Xi+\mathcal I .\quad}
 \tag{15}
\]
Indeed the product difference telescopes as
\(\sum_e(A_e-Q_e)T_e\). In \(d\Xi\), every angular derivative wedges
with the angular top form and every derivative in \(x_f\), \(f\ne e\),
wedges with an already present \(dx_f\). Also \(T_e\) is independent
of \(x_e\). The surviving derivative is (11). The contraction sign
\(\iota_{\partial_{x_e}}\omega_0=(-1)^{e-1}dx_1\wedge\cdots
\widehat{dx_e}\cdots\wedge dx_q\wedge\nu\) gives exactly the sign in (15).

The coefficient of \(\mathcal I\) relative to \(\omega_0\) lies in the
joint physical ideal. It vanishes after reducing every angular endpoint
of the chosen wires. Equivalently it has zero original joint physical jets;
multiplication
by holomorphic attachments does not change this. If only some angular
variables are reduced, only their corresponding ideal summands may be
dropped. For ordinary free colors or chains on which such reduction has
not been justified, retain the remainder.
In particular an arbitrary partial angular chain is not silently replaced
by an original residue trace.

Modulo that ideal, \(\widehat U\) is exactly the finite matching unit of
[M]. Overlapping products of its radical factors vanish there. Those
products need not vanish in the ordinary lift used in (13)--(15).
All signed crossing powers, their full physical normals, and an arbitrary
joint angular attachment may be multiplied into (15).

For a co-source \(a(\mathbf x,\mathbf z)\) holomorphic on the working
domain (meromorphic away from its excluded poles), the exact formula is
\[
 a\left(\prod A_e-\widehat U\prod L_e\right)\omega_0
             =d(a\Xi)-da\wedge\Xi+a\mathcal I,
 \qquad da\wedge\Xi=
       \sum_e(\partial_{x_e}a)\mathcal D_eT_e\omega_0.
 \tag{16}
\]
This supplies the current for arbitrary inserted wire moments rather than
assuming that their observation commutes with truncation.

## 4. Moving complete seams and genuine partial boundaries

Every paired factor in (8), and every \(\mathcal D_e\), is periodic under
\(\tau_f:x_f\mapsto x_f+1\). Hence \(\tau_f^*\Xi=\Xi\), including
every component whose omitted differential is not \(dx_f\).
Consider any admissible lifted chain whose paired \(f\)-faces are the
graphs \(x_f=\beta_f\) and \(x_f=\beta_f+1\) over the same remaining
coordinates, with opposite induced orientations. The seams may depend
on angular variables and other wires. Their maps differ by \(\tau_f\),
so their pullbacks of \(\Xi\) agree exactly. They therefore cancel.
This argument retains the differentials of the moving seam functions;
it does not set them to zero.

For a wire-independent co-source the same cancellation holds for \(a\Xi\).
It also holds for a wire-dependent co-source invariant under the paired
deck maps, but then the bulk term in (16) remains. At any finite truncation,
Stokes gives exactly
\[
 \int_C a(\Omega_A-\Omega_Q)
       =\int_{\partial C}a\Xi-\int_C da\wedge\Xi+\int_Ca\mathcal I,
 \quad\Omega_A=(\prod A_e)\omega_0,\quad
 \Omega_Q=(\widehat U\prod L_e)\omega_0.
 \tag{17}
\]
Other angular sides and unpaired wire faces remain in \(\partial C\).
On a single partial wire arc their contribution is the actual difference
of endpoint values of \(\mathcal D_e\), with its attached factors.
No limiting deletion at \(w_e=0\) or \(\infty\) follows: the primitive is
a Laurent polynomial and can grow there.

For complete original wire periods and wire-independent attachments,
(15) reduces to the matching identity
\(\prod K_e=U\prod K_{<,e}\) under the prescribed physical traces.
Each wire still has its original factor \(N\). The theorem is a cardinal
source pushforward. It does not replace the untraced factorial by a
periodic function; the factorial-to-cardinal currents of [E] remain when
that different representative is used.

## 5. The degree condition belongs to the attached state

Let \(F(z,z';\boldsymbol\xi)\) be a joint ordinary polynomial with
\(\deg_zF\le m\); there is no degree restriction at the opposite
incidence. Let \(a_r\) extract the canonical Newton coefficient in a
traced variable. From (1), before taking absolute values,
\[
 \boxed{\begin{split}
 (\phi\otimes\phi)(F K_<)&=(a_m\otimes a_m)F,\\
 (\phi\otimes\phi)(F H)&=\sum_{r<m}(a_r\otimes a_r)F.
 \end{split}}                                                   \tag{18}
\]
Indeed \(K_<\) selects equal state indices \(r=D-j\ge D-L=m\);
the degree hypothesis leaves only \(r=m\). The high kernel selects
\(r<m\). These statements include \(N=2\), both parities, and all free
parameter derivatives. They also describe the corrected low residue:
its \(V_e\) part is exactly the second row of (18).

Source [T] expresses every \(a_r\), \(r\le m\), of an arbitrary class
by a matrix \(B_N\) of polynomial size in the short physical data.
At odd levels those are all distinct physical values; at even levels
they are the \(m\) values and the first ordinary derivative at the last
double node. Thus both rows of (18) have polynomial upper bounds in the
corresponding joint short data, including the original central normal.

More generally use independent paired incidence variables and suppose
each edge has at least one incidence at which the entire attached state
has degree at most \(m\). For any prescribed low/high choice on the edges,
expand that state in the tensor Newton basis. A low edge imposes the
single index \(m\); a high edge imposes an index in \(0,\ldots,m-1\).
Applying the short-data rows in every variable gives a polynomial bound
for every such completed residue contraction on a fixed graph. This
also covers loops pairing two distinct incidences of the same tensor.
Identifying or multiplying ports before contraction requires checking
the degree hypothesis on the resulting state again.

Low degree of \(K_<\) itself is not this hypothesis. Multiplication by
the matching unit need not preserve low degree; (18) instead keeps its
exact high-kernel correction. The residue bound does not bound the
nonconstant Laurent primitives on partial arcs. It supplies no parent
action comparison, positivity, or lower bound for the selected closing.

## Complete direct sources and coverage

* [E] [Original stationary-wire escape](research_stationary_wire_escape_current.md),
  SHA256 03f902ea70818cf8432dd3d947822b49d1f762487552b20dac7e431b8222aa4e:
  original cardinal halfwire, finite Fourier band, wire orientation and
  the distinction between a main-period residue and a completed alias cap.
* [M] [Full radical matching transport](research_full_radical_matching_unit_transport.md),
  SHA256 437867f73282cf09d7bd7b7e9b03759401cf6e96733f9e6116854dc867e40112:
  exact full-jet matching unit, polynomial lifts and retained closing.
* [T] [Low-degree coherent turn graphs](research_low_degree_coherent_turn_graph_bound.md),
  SHA256 43071efb1c5b88db76fa5cce8656675d6350d7b4d79931bb5008b085157293e8:
  original Newton pairing and polynomial short-data coefficient rows.

All three complete direct texts were read at these matching versions,
their used implications checked, and their hashes renewed. Existing
factorial/cardinal descent and full-kernel escape retain different
currents; the addition here is the explicit global low-halfwire primitive,
its ordinary ideal remainder, and its completed-residue degree scope.
Only written mathematics and source-text/hash operations were used.
Frozen proofs and public manuscripts are unchanged.
