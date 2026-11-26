# Parameter-leading rank for an augmented single-kernel source window

Private written proof, 16 November 2026.

For products of independently parameterized single-kernel turned factors,
there is an augmented exact finite-window presentation whose generic
physical rank is full at every fixed rational interior phase. The proof
uses formal endpoint-source specialization and a leading endpoint
parameter. It does not require avoiding the scalar indicial hits.

The presentation supplies the whole transformed pure-terminal packet
and both exterior collars. Its estimate retains their actual budgets.
In particular the pure-terminal packet contains a bare branching-star
source; its filled-action bound is not proved here.

## 1. The restricted source and its terminal hierarchy

Fix \(\tau=\pm1\), nonzero integers \(n_1,\ldots,n_r\), and \(r\ge1\).
Each input here is a single endpoint kernel:
\[
 f_i=V_{n_i}K_N(w_i,\cdot),\qquad
 F=U_\tau\operatorname{can}\prod_{i=1}^r f_i,\qquad
 w_i=2\cosh(\alpha_i/N).
 \tag{1}
\]
There is no additional base endpoint product in this theorem.
A product of several kernels inside one \(V_{n_i}\) is not covered
by replacing it with (1). Its mixed source is different.

Retain \(h=N^{-1}\), \(q=e^{\pi ih}\), \(c_0=q+q^{-1}\),
\(\eta=(-1)^{N-1}\), \(\kappa=q^{(N-1)^2/2}\), and put
\[
 p_i=P_N(w_i),\quad G_{n_i}=T(R^{-n_i}),\qquad
                    g_i=\eta\kappa^{n_i}h^2G_{n_i}.
\]
The exact full-quotient equations are
\[
                 (w_i-J)f_i=p_i g_i,\qquad
                         (D_{n_i}-c_0)g_i=0.
 \tag{2}
\]
The rescaling places the entire scalar carrier in the actual source
channel \(g_i\). No varying-level source is promoted to a coefficient.
All ordinary endpoint parameters remain free.

In the full-step lift \(C=v+v^{-1}\), \(E:v\mapsto q^2v\), write
\[
 J=r(v)-A(v)E-B(v)E^{-1},\qquad
 r(v)=\frac8{C+c_0},
\]
\[
 A(v)=-\frac{(qv-1)^4}{q(v^2-1)(q^2v^2-1)},\qquad B(v)=A(v^{-1}).
 \tag{3}
\]
Use the second-order companion of the first equation of (2), together
with the order \(2|n_i|\) companion of the second equation. Its matrix is
\[
                    M_i=
       \begin{pmatrix}M_{f_i}(w_i)&p_iL_i\\0&M_{g_i}\end{pmatrix}.
 \tag{4}
\]
This is an exact physical recurrence after its original denominators
are cleared; first angular derivatives of its ordinary residuals give
the actual normal rows. It is not an off-grid equation for a canonical
polynomial.

All coefficient matrices have bounded rational degrees in
\(h,q,v,\mathbf w,\mathbf p\). The scalar determinant of \(M_{f_i}\)
is \(B/A\), independent of \(w_i,p_i\). The determinant of \(M_{g_i}\)
is the ratio of its original nonzero extreme coefficients, also
independent of the endpoint parameters. Thus every tensor companion
and its inverse are rational with nonzero denominators after
\(\mathbf p=0\). The inverse is used only to derive cleared equations;
no nonunit is inverted in the original quotient.

Take the tensor of these full companions. Include reflected shifted
coordinates when forming the even/odd descent. At
\(\mathbf p=0\), its coefficient matrix is block diagonal according
to the choice, at each factor, of the \(f_i\) or \(g_i\) block.
The involution preserves these choices. Call the choice with only
\(g_i\) the pure-terminal sector.

Apply \(U_\tau\) to both descended components of each ordinary
tensor coordinate. The entire transformed pure-terminal sector,
including every shifted and reflected component and every first
normal, is supplied data. Remove only those columns exactly.
A mixed sector with even one \(f_i\) remains unknown.

## 2. Exact appended product rows

Choose a factor \(i\). Let \(y\) be the tensor companion of all other
factors, so
\[
                           Ey=M(v)y.
\]
Its coefficients are independent of \(w_i,p_i\). For each retained
fixed shift \(k\) of the \(f_i\) coordinate, set
\[
                       U(v)=f_i(q^{2k}v)y(v).
\]
The scalar equation (2), multiplied by \(y(v)\), gives exactly
\[
 \begin{split}
 w_iU={}&r(q^{2k}v)U
 -A(q^{2k}v)M(v)^{-1}EU\\
 &-B(q^{2k}v)M(q^{-2}v)E^{-1}U
                  +p_i\,g_i(q^{2k}v)y(v).
 \end{split}
 \tag{5}
\]
For example \(M(v)^{-1}EU=f_i(q^{2k+2}v)y(v)\);
the backward term is checked in the same way. This fixes
both shifts and the positive sign of the source term.

Choose an inversion-symmetric scalar polynomial clearing for all
rational coefficients in (5), its reflection, and the even/odd
descent. It may depend on the other endpoint symbols, but not on
\(w_i\). A Laurent denominator in \(v\) can be multiplied by its
inversion-reflected partner; their product is a polynomial in \(C\)
up to a Laurent unit. There are only finitely many fixed shifts.

The exact full-step conversion to \(C,J,D_1\) introduces additional
powers of \(C-c_0\). Keep those factors. Multiplying by them on both
sides gives a polynomial operator equation for the full descended
vector \(\mathcal U\), of the form
\[
 \bigl[w_i d_i(C)I-\mathcal P_i(C,J,D_1)\bigr]\mathcal U
                         =p_i\mathcal Q_i(C,J,D_1)\mathcal V_i .
 \tag{6}
\]
Here \(d_i\ne0\) is scalar, and \(d_i,\mathcal P_i,\mathcal Q_i\)
are independent of \(w_i\). They have fixed bounded degrees.
The vector \(\mathcal V_i\) is the actual descended
\(g_i(q^{2k}v)y(v)\) source and its required reflected coordinates.
No division by a physical source factor has been made.

Why does the leading term stay scalar? Multiplication by
\(w_i d_i(C)\) commutes with inversion, so it acts identically on
both even/odd descended components. All changes of coefficient
operators occur in the other terms. This also covers the odd
ramified angular point by the exact free decomposition
\(\mathcal B_N=\mathcal A_N\oplus(v-v^{-1})\mathcal A_N\);
it is not a division of sampled values by \(v-v^{-1}\).

Now apply the actual outer turn. Since its ordered substitutions are
\(C\mapsto D_\tau\), \(J\mapsto J\), \(D_1\mapsto D_{\tau+1}\),
equation (6) becomes
\[
 \bigl[w_i d_i(D_\tau)I
       -\mathcal P_i(D_\tau,J,D_{\tau+1})\bigr]\widetilde{\mathcal U}
 =p_i\mathcal Q_i(D_\tau,J,D_{\tau+1})
                                   \widetilde{\mathcal V}_i .
 \tag{7}
\]
All orders and original full-normal equations remain.
Append these rows for every relevant factor, sector coordinate,
and fixed shift, together with their actual first-normal rows.

These are augmented source-exact equations. No assertion is made
that a smaller previously chosen window already contains their
row span or one of the minors established below.

## 3. A scalar no-compact-string fact

Work over the field of rational functions in independent formal
\(h,q,\mathbf w\) and the required rational power of \(q\).
Fix
\[
                  v_j=\zeta q^{\delta+2j},\qquad
                       \zeta\ne1,-1,\quad \delta\in\mathbb Q.
 \tag{8}
\]
The parameter \(q\) is transcendental here. For a physical rational
interior phase, \(\zeta=e^{2\pi ia/b}\), \(0<a/b<1/2\).
The field can include the other formal parameters.

Every coefficient \(A(v_j),B(v_j)\) is a unit in this field.
A numerator or denominator zero would require \(\zeta=1\) or
\(\zeta^2=1\), because a nonzero rational power of a transcendental
\(q\) is not a fixed complex number. The forward and backward
extremes of the unit turn are
\[
       q^{-\tau}v^{-\tau}A(v),\qquad
                         q^{-\tau}v^\tau B(v).
 \tag{9}
\]
They too are units at every integer translate in (8).

Consequently, if \(d(C)\ne0\) is any scalar polynomial with
coefficients independent of the sequence index, then
\(d(D_\tau)\) has a unit forward extreme. If \(\deg d=s\ge1\),
it is the leading coefficient of \(d\) times the product of the
\(s\) shifted forward extremes in (9); all lower powers have
smaller shift range. If \(s=0\), the operator is a nonzero scalar.

It follows that
\[
 d(D_\tau)x=0\text{ on all integer rows},\qquad
            x\text{ finitely supported}\quad\Longrightarrow\quad x=0.
 \tag{10}
\]
Indeed let \(j_0\) be the first nonzero entry. For \(s\ge1\), the
output row \(j_0-s\) contains only its forward extreme times
\(x_{j_0}\); every other term lies before the support. This contradicts
the unit extreme. The scalar case is immediate. The same argument
applies componentwise to a vector and to arbitrary finite support.

## 4. The complete collar and the nonzero minor

Choose any fixed finite support interval for all unknown descended
channel values and first normals. Supply the entire transformed
pure-terminal sector and every component outside that support which
occurs in the equations to be used. Include every output row of (7)
or of the retained source equations whose shift range touches the
unknown support. The required collar is finite, with width determined
only by the fixed operator orders.

This closure requirement is substantive. Rows centered only inside
the support would not justify zero extension: omitted exterior-center
rows can detect its first nonzero entry.

Let \(\mathsf A\) be this augmented finite matrix after removal of
the supplied columns and polynomial coefficient clearings. We claim
that, on (8),
\[
                  \operatorname{rank}\mathsf A
                         =\text{number of unknown columns}
 \tag{11}
\]
over the coefficient field, already after formal
\(\mathbf p=0\).

First consider values. At \(\mathbf p=0\), sectors decouple. Every
unknown sector contains some \(f_i\), because the entire pure-terminal
sector is supplied. Choose such an \(i\). In the homogeneous kernel
test all supplied data are set to zero. Equations (7), for this sector,
then have the form
\[
                      [w_i d_i(D_\tau)I-\mathcal P_i]X=0,
 \tag{12}
\]
with both displayed operators independent of \(w_i\), and
\(d_i\ne0\) after specialization. Nonvanishing of the clearing follows
from the invertible companion determinants in (4), before descent;
its reflected factors and fixed conversion factors are nonzero as well.

A kernel vector has rational-function entries in \(w_i\), with
coefficients in the field of all other parameters. Take the largest
Laurent exponent at \(w_i=\infty\) among its finitely many entries,
and let \(X_*\ne0\) be the corresponding coefficient vector.
The coefficient one degree higher in (12) gives
\[
                              d_i(D_\tau)X_*=0.
\]
Extend \(X_*\) by zero outside the chosen support. The complete
collar supplies every row needed for this equation on the full
integer lattice; rows farther away are automatically zero.
Equation (10) is a contradiction. Thus every value sector vanishes.

The first-normal system is triangular over the value system.
Its diagonal uses the same value-row matrix; the extra terms are
the actual derivatives of its ordinary coefficient rows multiplying
the values. Once the value kernel has vanished, the identical argument
kills the normal kernel. No derivative of a quotient element was used.
This proves (11), including all independent first normals.

Therefore at least one full-column minor of the augmented polynomial
coefficient matrix is nonzero on (8) after \(\mathbf p=0\). It is
then nonzero before that specialization. For the physical residue
trajectory \(v=\zeta q^{p'/b'}\), this says the augmented minors do
not have the common physical binomial
\[
                            v^{b'}-\zeta^{b'}q^{p'}.
 \tag{13}
\]
The quantum-binomial criterion applies because every coefficient
degree is bounded independently of \(N\). Its fixed-level
\(p_i=P_N(w_i)\) injectivity then gives an actual nonzero microscopic
minor germ. On compact unit charts of its leading coefficient, the
physical-window conditioning estimate costs only a power of \(N\).

The use of \(\mathbf p=0\) above is solely a formal coefficient test.
It is not a claim that arbitrary independent \(w_i\) with \(p_i=0\)
are actual microscopic source parameters. Repeated actual parameters
must first be polarized for this proof. Rank on a shared-parameter
diagonal is not asserted; extension of a bound for the actual
holomorphic source would require its own uniform parameter argument.

## 5. The pure-terminal source has not disappeared

The supplied packet is the whole shifted/mirrored companion tensor
made only of the \(g_i\), followed by even/odd descent and \(U_\tau\),
with every first normal. It is not determined here by a single scalar
closing and its adjacent outputs.

Its unshifted scalar component, before the harmless rescalings of
the \(g_i\), is
\[
                       H(Z)=U_\tau\operatorname{can}\prod_iG_{n_i}(Z).
\]
It has the exact original-trace expression
\[
 \begin{split}
 H(Z)=\kappa^\tau\phi_X\Bigl[
 K_N(Z,X)R^{-\tau}(X)\,
 \phi_Y\Bigl[K_N(X,Y)
   \prod_i\phi_{W_i}\bigl[K_N(Y,W_i)R^{-n_i}(W_i)\bigr]
                    \Bigr]\Bigr].
 \end{split}
 \tag{14}
\]
The central \(Y\) row has power zero, the next row \(X\) has power
\(-\tau\), and the terminal rows have powers \(-n_i\).
The chosen normalization of the \(g_i\) adds the scalar
\((\eta h^2)^r\kappa^{\sum_i n_i}\).
The remaining supplied coordinates are its literal shifted/mirrored
source insertions, not unspecified replacements.

Thus the rank theorem reduces decorated recovery to an explicitly
simpler endpoint-parameter-free source hierarchy. That hierarchy
still contains an undecorated branching-star quantity. A bound for
the \(G_{n_i}\) before the outer turn does not bound this supplied
packet by the sum of their terminal rates after that turn.

Concretely the conditioning consequence is only
\[
 \|X_N\|\le C N^K\bigl(\|\text{full supplied pure-terminal packet}\|
                +\|\text{both supplied collars}\|
                +\|\text{other retained forcing}\|\bigr)
 \tag{15}
\]
on the stated generic microscopic unit chart. Its exponential budget
is the maximum of those actual supplied budgets. No smaller incoming
budget is inferred from a right collar known only at a global ceiling.

The theorem therefore proves a new exact generic-rank statement for
the augmented single-kernel hierarchy. It neither proves a branching
filled-action estimate nor eliminates the unknown bare-star rate.
It gives no arbitrary-product or \(r_i>1\) module closure.

## 6. Direct sources

Complete direct sources were read at these unchanged pins; used
identities and hashes were checked:

* [Finite-band operators and exact one-factor forcing](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb.
* [Full-step tensor interface and even/odd descent](research_full_step_repeated_turn_tensor_interface.md),
  SHA256 ef851eab40c8b2c44388a41d324e2fa41d4400f0f2118fe587405911e00e3398.
* [Exact physical-window conditioning](research_resonant_physical_window_conditioning.md),
  SHA256 f1af212ec05ffdb79cc9b99ce03961622740d58622213e648918000e81e5fa07.
* [Bounded-degree quantum-binomial rank criterion](research_repeated_turn_quantum_binomial_rank_criterion.md),
  SHA256 5910f76a9e70e589d07476cae663b31bc949266e187f4f2902ce33cc8cd669cf.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test or build was run.
Adopted notes and public manuscripts are unchanged.

